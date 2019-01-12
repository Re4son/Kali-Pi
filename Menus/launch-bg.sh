#!/bin/bash
case $KPSCREENSIZE in
    2.8)
        BACKGROUND="Pictures/Kali-Pi-2.8.jpg"
        ;;
    3.5)
        BACKGROUND="Pictures/Kali-Pi-3.5.jpg"
        ;;
    5.0)
        BACKGROUND="Pictures/Kali-Pi-5.0.jpg"
        ;;
    7.0)
        BACKGROUND="Pictures/Kali-Pi-5.0.jpg"
        ;;
    *)
        exit 1
esac
##setterm -term linux -back default -fore black -clear all
fbi -t 2 -1 -d $FRAMEBUFFER -noverbose -a $MENUDIR$BACKGROUND
