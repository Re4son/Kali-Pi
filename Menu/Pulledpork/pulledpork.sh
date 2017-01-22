#!/bin/bash
script="/home/pi/pitftmenu/menu_pause.py"
setterm -term linux -back default -fore white -clear all
/usr/bin/env perl /usr/local/bin/pulledpork.pl -c /usr/local/etc/snort/pulledpork.conf -lT
/usr/bin/env python $script
setterm -term linux -back default -fore black -clear all
