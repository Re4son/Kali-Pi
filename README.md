# KALI-PI Launcher

Simple touch menu for Raspberry Pi projects using a 3.5" (480x320) or 2.8" (320x240) touch screen based on garthvh's original project.

Thanks to JPearn for porting it to 2.8" and to ArmyGuy255a for cleaning up the code and improving the layout.


It runs as a python script in the framebuffer without needing a desktop environment.

This menu is the default launcher in [Sticky Finger's Kali Pi](http://www.whitedome.com.au/kali-pi)
![Kali-Pi in action](http://whitedome.com.au/re4son/wp-content/uploads/2015/11/2015.11-Kali-Pi-Drone_small2.jpg)

I was after an easy way to launch X Window on either the TFT screen or through HDMI without the need for massive reconfigurations.
I came accross [garthvh's project featured on Adafruit](https://blog.adafruit.com/2015/05/08/simple-pitft-touchpi-menu-system-piday-raspberrypi-raspberry_pi/) and used it as basis for this project


## Installation

    git clone https://github.com/re4son/Kali-Pi
    cd Kali-Pi
    
    customise the file "menu" to match the path, define the screen size, etc.
    cusomise the scripts to suit your needs
    
**Important: Pygame is broken on on Debian Jessie. I'll explain below how to fix it.**


## Usage
	sudo ./menu
    
## Layout

### Start Screen

The first menu is menu_kali-1.py, which provides the following options:

![menu-1](https://whitedome.com.au/re4son/wp-content/uploads/2017/01/menu-1-1.png)

All functions are self explainatory.
After exiting and application, the screen returns back to the last menu.

The "Screen Off" function launches the python script "menu_screenoff.py", which uses the RPi.GPIO module to turn the screen off.
You can turn it back on by pressing anywhere on the screen.

Using the ">>>" button, we can scroll to the next screen, namely "menu_kali-2.py"

### menu-2.py

This script allows us to stop and start services:

![menu-2.py](https://whitedome.com.au/re4son/wp-content/uploads/2017/01/menu-2.png)

Press a button to start a service.

The button changes to green when the service is running:

![running service](https://whitedome.com.au/re4son/wp-content/uploads/2017/01/menu-2-on.png)

Press the button again to stop the service.


### menu-3.py

Some more applications:

![menu-3.py](https://whitedome.com.au/re4son/wp-content/uploads/2017/01/menu-3-1.png)


### menu_kali-4.py

![menu-4.py](https://whitedome.com.au/re4son/wp-content/uploads/2017/01/menu-4.png)

### menu-9.py
The last script displays some health information:

![menu-9](https://whitedome.com.au/re4son/wp-content/uploads/2017/01/menu-9.png)


### menu-pin.py
The variable "KPPIN" in the file ~/menu can be set to "1" to enable PIN authentication to hide the menus from spying eyes:

![menu-pin](https://whitedome.com.au/re4son/wp-content/uploads/2017/01/menu-pin.png)


### Screensaver
The screensaver can be enabled by setting the variable KPTIMEOUT in the file "./menu". Set it to the number of minutes after which the screensaver should kick in (very approximate value). Use 1 for 1 min, 0.5 for 30sec, etc.
Touch anywhere on the screen to wake the system up.
When KPPIN is set, the screen will return to the PIN menu after waking up.


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

