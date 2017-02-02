#!/bin/bash

pkill dnsmasq
pkill sslstrip
pkill sslsplit
pkill hostapd
pkill python
pkill dnsspoof
pkill tinyproxy
pkill ruby
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT
iptables -t nat -F
hostname kali-pi
