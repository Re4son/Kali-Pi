#!/bin/sh
# Ugly hack to work around #787480
iptables -F
iptables -t nat -F
iptables -t mangle -F
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

exec /usr/local/sbin/bt-pan --systemd --debug server pan
