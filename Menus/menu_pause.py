#!/usr/bin/env python
import pygame, os, sys, subprocess, time
import RPi.GPIO as GPIO
from pygame.locals import *
from subprocess import *
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
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()

        #Debug:
        #ensure there is always a safe way to end the program if the touch screen fails
        ##if event.type == KEYDOWN:
        ##    if event.key == K_ESCAPE:
        ##        sys.exit()

    time.sleep(0.4)
