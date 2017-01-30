
#!/bin/sh
### BEGIN INIT INFO
# Provides:          DNS2Proxy
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Control DNS2Proxy
# Description:       Control DNS2Proxy
### END INIT INFO

start() {
	echo "--------------------------------"
	echo "   START DNS2Proxy SERVICES"
	echo "--------------------------------"
        upstream=eth0
        phy=wlan1
        share=/usr/share/mana-toolkit
        logs=/var/lib/mana-toolkit

		#Kill dnsmasq and restart it without the DNS server.
		DNSMASQ=$(ps auxww | grep "[d]nsmasq" | awk '{print $2}')
		kill $DNSMASQ
		#Restart dnsmasq for the DHCP server (-p 0 disables the DNS feature)
		dnsmasq -z -C $MENUDIR/dns2proxy/dnsmasq-dhcpd.conf -i $phy -I lo -p 0
        #Enable DNS2Proxy
        cd $share/sslstrip-hsts/dns2proxy/
		phyIP=$(ifconfig $phy | grep netmask | awk '{print $2}')
        python dns2proxy.py -i $phy -u $phyIP&
        cd -


}

stop() {
	
        echo "--------------------------------"
        echo "   STOP DNS2Proxy SERVICES"
        echo "--------------------------------"
		phy=wlan1
        DNS2PROXY=$(ps auxww | grep "[p]ython dns2proxy.py" | awk '{print $2}')
		kill $DNS2PROXY
		DNSMASQ=$(ps auxww | grep "[d]nsmasq" | awk '{print $2}')
		kill $DNSMASQ
		#Restart the normal DNS server
		dnsmasq -z -C /etc/mana-toolkit/dnsmasq-dhcpd.conf -i $phy -I lo
        #iptables -t nat -D PREROUTING -i $phy -p tcp --destination-port 80 -j REDIRECT --to-port 10000
        #Flush the NAT table


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
        PID=$(ps auxww | grep "[p]ython dns2proxy.py" | awk '{print $2}')
        if test ${PID:-0} -gt 0
        then
            echo "DNS2Proxy is running. $PID[0]"
            return 1
        else
            echo "DNS2Proxy is not running. $PID"
            return 0
        fi
       ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
esac

