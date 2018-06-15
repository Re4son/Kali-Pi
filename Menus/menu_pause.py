#!/usr/bin/env python
import pygame, os, sys, subprocess, time
import RPi.GPIO as GPIO
from pygame.locals import *
from subprocess import *
if "TFT" in os.environ and os.environ["TFT"] == "0":
    # No TFT screen
    SCREEN=0
    pass
elif "TFT" in os.environ and os.environ["TFT"] == "2":
    # TFT screen with mouse
    SCREEN=2
    os.environ["SDL_FBDEV"] = "/dev/fb1"
elif "TFT" in os.environ and os.environ["TFT"] == "3":
    # HDMI touchscreen
    SCREEN=3
    os.environ["SDL_FBDEV"] = "/dev/fb0"
    os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
    os.environ["SDL_MOUSEDRV"] = "TSLIB"
elif "TFT" in os.environ and os.environ["TFT"] == "4":
    # Raspberry Pi 7" touchscreen
    SCREEN=4
    from ft5406 import Touchscreen
    os.environ["SDL_FBDEV"] = "/dev/fb0"
    ts = Touchscreen()
else:
    # TFT touchscreen
    SCREEN=1
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
    os.environ["SDL_MOUSEDRV"] = "TSLIB"

# Initialize pygame modules individually (to avoid ALSA errors) and hide mouse
pygame.font.init()
pygame.display.init()
pygame.mouse.set_visible(0)

# Initialise GPIO
GPIO.setwarnings(False)


#While loop to manage touch screen inputs
state = [False for x in range(10)]
while 1:
    if SCREEN==4:
        for touch in ts.poll():
            if state[touch.slot] != touch.valid:
                if touch.valid:
                    sys.exit()
    else:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()

        #Debug:
        #ensure there is always a safe way to end the program if the touch screen fails
        ##if event.type == KEYDOWN:
        ##    if event.key == K_ESCAPE:
        ##        sys.exit()

    time.sleep(0.4)
