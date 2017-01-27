#!/usr/bin/env python
import pygame, os, sys, subprocess, time, os.path
import RPi.GPIO as GPIO
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

if os.environ["KPPIN"] != "1":
    launch_bg=os.environ["MENUDIR"] + "launch-bg.sh"
    process = subprocess.call(launch_bg, shell=True)

# Initialize pygame modules individually (to avoid ALSA errors) and hide mouse
pygame.font.init()
pygame.display.init()
pygame.mouse.set_visible(0)

## Initialise backlight control

if os.path.isfile("/sys/class/backlight/soc:backlight/brightness"):
    # kernel 4.4 STMP GPIO on/off for ada 3.5r
    backlightControl="3.5r"
else:
    # GPIO 18 backlight control
    # Initialise GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    backlightControl="GPIO18"

def get_retPage():
    retPage = "menu-1.py"
    if len(sys.argv) > 1:
        retPage = str(sys.argv[1])
    return retPage

def run_cmd(cmd):
    process = Popen(cmd.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output

# Turn screen on
def screen_on():
        pygame.quit()
        if backlightControl == "3.5r":
            process = subprocess.call("echo '1' > /sys/class/backlight/soc\:backlight/brightness", shell=True)
        else:
            backlight = GPIO.PWM(18, 1023)
            backlight.start(100)
            GPIO.cleanup()
        retPage=get_retPage()
        if os.environ["KPPIN"] == "1":
            page=os.environ["MENUDIR"] + "menu-pin.py"
            args = [page, retPage]
        else:
            page=os.environ["MENUDIR"] + retPage
            args = [page]

        os.execvp("python", ["python"] + args)

# Turn screen off
def screen_off():
        if backlightControl == "3.5r":
            process = subprocess.call("echo '0' > /sys/class/backlight/soc\:backlight/brightness", shell=True)
        else:
            backlight = GPIO.PWM(18, 0.1)
            backlight.start(0)

        process = subprocess.call("setterm -term linux -back black -fore black -clear all", shell=True)


#While loop to manage touch screen inputs
screen_off()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen_on()

        #ensure there is always a safe way to end the program if the touch screen fails
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    time.sleep(0.4)
