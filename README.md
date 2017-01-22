# KALI-PI Launcher

Simple touch menu for Raspberry Pi projects using a 3.5" (480x320) or 2.8" (320x240) touch screen based on garthvh's original project.

Thanks to JPearn for porting it to 2.8" and to ArmyGuy255a for cleaning up the code and layout.


It runs as a python script in the framebuffer without needing a desktop environment.

This menu is the default launcher in [Sticky Finger's Kali Pi](http://www.whitedome.com.au/kali-pi)
![Kali-Pi in action](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/2015.11-Kali-Pi-Drone_small2.jpg)

I was after an easy way to launch X Window on either the TFT screen or through HDMI without the need for massive reconfigurations.
I came accross [garthvh's project featured on Adafruit](https://blog.adafruit.com/2015/05/08/simple-pitft-touchpi-menu-system-piday-raspberrypi-raspberry_pi/) and used it as basis for this project


## Installation

    git clone https://github.com/re4son/Kali-Pi
    cd Kali-Pi
    For 2.8" screens: git checkout 2.8
    customise the file "menu" to match the path
    cusomise the scripts to suit your needs
    
**Important: Pygame is broken on on Debian Jessie. I'll explain below how to fix it.**

## Usage
	sudo ./menu
    
## Layout

### Start Screen

The first menu is menu_kali-1.py, which provides the following options:

![menu_kali-1](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/kali-pi_01-menu_kali-1.png)

All functions are self explainatory.
After exiting and application, the screen returns back to the last menu.

The "Screen Off" function launches the python script "menu_screenoff.py", which uses the RPi.GPIO module to turn the screen off.
You can turn it back on by pressing anywhere on the screen.

Using the ">>>" button, we can scroll to the next screen, namely "menu_kali-2.py"

### menu_kali-2.py

Some more applications to launch:

![menu_kali-2.py](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/kali-pi_03-menu_kali-2.png)

Kismet and SDR-Scanner have to be installed for this to work.
If you want to enable the reboot and shutdown commands you will need to make the following updates

    sudo visudo
Add the following line:

    %pi	ALL=(ALL:ALL) NOPASSWD: /sbin/poweroff, /sbin/reboot, /sbin/shutdown, /home/pi/Kali-Pi/menu

### menu_kali-3.py

This script allows us to stop and start services:

![menu_kali-3.py](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/kali-pi_06-menu_kali-3.png)

Press a button to start a service.

The button changes to green when the service is running:

![running service](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/kali-pi_09-services-on.png)

Press the button again to stop the service.

### menu_kali-4.py

This script allows us to stop and start MySQL & Snort and allows to update the Snort rules via PulledPork:
![menu_kali-4.py](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/kali-pi_10-1-menu_kali-4.png)

### menu_kali-9.py
The last script displays some health information:

![menu_kali-9](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/kali-pi_10-menu_kali-9.png)

### Run menu at startup

The preferred method to run this script on startup is to add it to the end of ".profile"

    nano ~/home/.profile

And add the following line to the bottom of the file

    sudo /home/pi/Kali-Pi/menu
    
## Fix Pygame on Debian Jessie
The package "libsdl1.2-15-10", which ships with Debian Jessie, breaks pygame.
To make it work we have to revert back to "libsdl1.2-15-5" from Wheezy.

The quickest way is to comment everything out in your /etc/apt/sources.list and temporarily add:

```
deb http://archive.raspbian.org/raspbian wheezy main contrib non-free
```


Import the corresponding keys:
```
deb http://archive.raspbian.org/raspbian wheezy main contrib non-free
gpg -a --export 9165938D90FDDD2E | sudo apt-key add -
```

Remove the offending package and replace it with the working one:
```
sudo apt-get update
sudo apt-get remove libsdl1.2debian python-pygame
apt-get install libsdl-image1.2 libsdl-mixer1.2 libsdl-ttf2.0-0 libsdl1.2debian libsmpeg0 python-pygame
sudo apt-mark hold libsdl1.2debian
```

Restore "/etc/apt/sources.list" to it's original state.

That's it. Pygame is fixed :-)

## References

This project is a fork of garthvh's work, available here:
[https://github.com/garthvh/pitftmenu](https://github.com/garthvh/pitftmenu)

