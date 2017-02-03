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
upstream=eth0
phy=wlan1
conf=/home/pi/Kali-Pi/Menus/mana/hostapd-mana.conf
hostapd=/usr/lib/mana-toolkit/hostapd
cmdline="${hostapd} ${conf}"
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

        service network-manager stop
        rfkill unblock wlan

        ifconfig $phy up

        sed -i "s/^interface=.*$/interface=$phy/" $conf
        $cmdline & echo $! > ${PIDFILE}
        sleep 5
        ifconfig $phy 10.0.0.1 netmask 255.255.255.0
        route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

        dnsmasq -z -C /etc/mana-toolkit/dnsmasq-dhcpd.conf -i $phy -I lo

        echo '1' > /proc/sys/net/ipv4/ip_forward
        iptables --policy INPUT ACCEPT
        iptables --policy FORWARD ACCEPT
        iptables --policy OUTPUT ACCEPT
        iptables -F
        iptables -t nat -F
        iptables -t nat -A POSTROUTING -o $upstream -j MASQUERADE
        iptables -A FORWARD -i $phy -o $upstream -j ACCEPT

}
stop() {

        echo "--------------------------------"
        echo "   STOPPING $PROGSHORT"
        echo "--------------------------------"
        if [[ -z "${PID}" ]]; then
            echo "${PROGSHORT} is not running (missing PID)."
        elif [[ -e /proc/${PID}/cmdline && "`tr -d '\0' < /proc/${PID}/cmdline`" == *"$( echo -e "${cmdline}" | tr -d '[:space:]')"* ]]; then
            pkill dnsmasq
            pkill sslstrip
            pkill sslsplit
            pkill hostapd
            pkill python
            iptables -t nat -F
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
