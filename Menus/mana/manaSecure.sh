### BEGIN INIT INFO
# Provides:          ManaSecure
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Control Basic Mana-Toolkit with WPA2
# Description:       Control Basic Mana-Toolkit Services with WPA2
### END INIT INFO

start() {
	echo "--------------------------------"
	echo "   START Secure Mana SERVICES"
	echo "--------------------------------"
        upstream=eth0
        phy=wlan1
        conf=$MENUDIR/hostapd-mana-wpa2.conf
        hostapd=/usr/lib/mana-toolkit/hostapd

        service network-manager stop
        rfkill unblock wlan

        ifconfig $phy up

        sed -i "s/^interface=.*$/interface=$phy/" $conf
        $hostapd $conf&
        sleep 5
        ifconfig $phy 10.0.0.1 netmask 255.255.255.0
        route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

        dnsmasq -z -C $MENUDIR//dnsmasq-dhcpd.conf -i $phy -I lo

        #Enable NAT
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
        echo "   STOP Secure Mana SERVICES"
        echo "--------------------------------"
        pkill dnsmasq
        pkill sslstrip
        pkill sslsplit
        pkill hostapd
        pkill python
        #Flush the NAT table
        iptables -t nat -F

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
        PID=$(ps auxww | grep "[h]ostapd-mana-wpa2.conf" | awk '{print $2}')
        if test ${PID:-0} -gt 0
        then
            echo "Secure Mana is running."
            return 1
        else
            echo "Secure Mana is not running."
            return 0
        fi
       ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
esac

