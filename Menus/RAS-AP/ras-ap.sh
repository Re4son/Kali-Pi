### BEGIN INIT INFO
# Provides:          ManaSimple
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Control hostapd access point
# Description:       Control hostapd access point Services
### END INIT INFO

start() {
	echo "--------------------------------"
	echo "   START Remote Access WiFi AP"
	echo "--------------------------------"
        upstream=eth0
        phy=wlan0
        conf=$MENUDIR/RAS-AP/hostapd.conf
        hostapd=/usr/sbin/hostapd

        service network-manager stop
        rfkill unblock wlan

        ifconfig $phy up

        sed -i "s/^interface=.*$/interface=$phy/" $conf
        $hostapd $conf&
        sleep 5
        ifconfig $phy 192.168.201.1 netmask 255.255.255.0
        route add -net 192.168.201.0 netmask 255.255.255.0 gw 192.168.201.1

        dnsmasq -z -C $MENUDIR/RAS-AP/dnsmasq-dhcpd.conf -i $phy -I lo

##        #Enable NAT
##        echo '1' > /proc/sys/net/ipv4/ip_forward
##        iptables --policy INPUT ACCEPT
##        iptables --policy FORWARD ACCEPT
##        iptables --policy OUTPUT ACCEPT
##        iptables -F
##        iptables -t nat -F
##        iptables -t nat -A POSTROUTING -o $upstream -j MASQUERADE
##        iptables -A FORWARD -i $phy -o $upstream -j ACCEPT

}

stop() {

        echo "---------------------------------------"
        echo "   STOP Remote Access Wifi-AP SERVICES "
        echo "---------------------------------------"
        pkill dnsmasq
        pkill hostapd
        pkill python
        #Flush the NAT table
##        iptables -t nat -F

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
        PID=$(ps auxww | grep "[h]ostapd-mana.conf" | awk '{print $2}')
        if test ${PID:-0} -gt 0
        then
            echo "Simple Mana is running."
            return 1
        else
            echo "Simple Mana is not running."
            return 0
        fi
       ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
esac

