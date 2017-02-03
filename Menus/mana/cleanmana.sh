#!/bin/bash

pkill dnsmasq
pkill sslstrip
pkill sslsplit
pkill hostapd
pkill python
pkill dnsspoof
pkill tinyproxy
pkill ruby
pkill msfconsole
pkill stunnel4
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT
iptables -t nat -F
service apache2 stop
hostname kali-pi
