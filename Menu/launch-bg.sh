#!/bin/bash
BACKGROUND="Pictures/Kali-Pi-3.5.jpg"
setterm -term linux -back default -fore black -clear all
fbi -t 2 -1 -d /dev/fb1 -noverbose -a $MENUDIR$BACKGROUND
