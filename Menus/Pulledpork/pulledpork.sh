#!/bin/bash
script="/home/pi/Kali-Pi/Menus/menu_pause.py"
/usr/bin/env perl /usr/local/bin/pulledpork.pl -c /usr/local/etc/snort/pulledpork.conf -lT
/usr/bin/env python $script
