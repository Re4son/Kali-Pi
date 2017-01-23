#!/usr/bin/env python
import sys, os, pygame, subprocess, commands, time, socket
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

#############################
## Global display settings ##


# colors    R    G    B
white    = (255, 255, 255)
tron_whi = (189, 254, 255)
red      = (255,   0,   0)
green    = (  0, 255,   0)
blue     = (  0,   0, 255)
tron_blu = (  0, 219, 232)
black    = (  0,   0,   0)
cyan     = ( 50, 255, 255)
magenta  = (255,   0, 255)
yellow   = (255, 255,   0)
tron_yel = (255, 215,  10)
orange   = (255, 127,   0)
tron_ora = (255, 202,   0)


# Set up the base menu you can customize your menu with the colors above
# Initialize pygame modules individually (to avoid ALSA errors) and hide mouse
pygame.font.init()
pygame.display.init()
pygame.mouse.set_visible(0)

#set size of the screen
size = width, height = 480, 320
screen = pygame.display.set_mode(size)

# Background Color
screen.fill(black)

#set size of the screen
screen_x = 480
screen_y = 320

size = width, height = screen_x, screen_y



screen = pygame.display.set_mode(size)

# Background Color
##screen.fill(black)

#Define the aspect of the menu
originX = 40
originY = 115
spacing = 10
buttonWidth = 133
buttonHeight = 55
labelFont = 24

class Button(object):
        text = ""
        xpo = ""
        ypo = ""
        height = ""
        width = ""
        color = ""
        fntSize = ""
        def __init__(self, text, xpo, ypo, height, width, color, fntSize):
                self.text = text
                self.xpo = xpo
                self.ypo = ypo
                self.height = height
                self.width = width
                self.color = color
                self.fntSize = fntSize


## Global display settings ##
#############################


#############################
##   Global Functions      ##

# Get todays date
def get_date():
    d = time.strftime("%a, %d %b %Y  %H:%M:%S", time.localtime())
    return d

# Get your external IP address
def get_ip():
    ip_msg = "Not connected"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.connect(('<broadcast>', 0))
##        ip_msg=" IP: " + s.getsockname()[0]
        ip_msg=s.getsockname()[0]
    except Exception:
        pass
    return ip_msg

# Get hostname
def get_hostname():
    pi_hostname = run_cmd("hostname")
    pi_hostname = "  " + pi_hostname[:-1]
    return pi_hostname

def get_temp():
    command = "vcgencmd measure_temp"
    process = Popen(command.split(), stdout=PIPE)
    output = process.communicate()[0]
    temp = 'Temp: ' + output[5:-1]
    return temp

def get_clock():
    command = "vcgencmd measure_clock arm"
    process = Popen(command.split(), stdout=PIPE)
    output = process.communicate()[0]
    clock = output.split("=")
    clock = int(clock[1][:-1]) / 1024 /1024
    clock = 'Clock: ' + str(clock) + "MHz"
    return clock

def get_volts():
    command = "vcgencmd measure_volts"
    process = Popen(command.split(), stdout=PIPE)
    output = process.communicate()[0]
    volts = 'Core:   ' + output[5:-1]
    return volts

# Restart Raspberry Pi
def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    process = Popen(command.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output

# Shutdown Raspberry Pi
def shutdown():
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    process = Popen(command.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output

# Run command
def run_cmd(cmd):
    process = Popen(cmd.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output

#This function is used to check individual services, not processes.
def check_service(srvc):
    try:
        check = "/usr/sbin/service " + srvc + " status"
        status = run_cmd(check)
        if ("is running" in status) or ("active (running)") in status:
            return True
        else:
            return False
    except:
        return False

# Toggle service
def toggle_service(srvc):
    check = "/usr/sbin/service " + srvc + " status"
    start = "/usr/sbin/service " + srvc + " start"
    stop = "/usr/sbin/service " + srvc + " stop"
    status = run_cmd(check)
    if ("is running" in status) or ("active (running)") in status:
        run_cmd(stop)
        return False
    else:
        run_cmd(start)
        return True

# Toggle script
def toggle_script(script):
    check = script + " status"
    start = script + " start"
    stop = script + " stop"
    status = call(check, shell=True)
    if (status == 1) :
        call(stop, shell=True)
        return False
    else:
        call(start, shell=True)
        return True

#This function is used to kill a process.
def kill_process(proc, file=":"):
    try:
        check = "ps auxww | grep [" + proc[0] + "]" + proc[1:] + " | grep " + file
        status = commands.getoutput(check)
        #print(status)
        if status:
            #Process exists, kill it
            kill = "kill $(" + check + " | awk '{print $2}')"
            commands.getoutput(kill)
            return True
        else:
            return False
    except:
        return False

#This function is used to check individual processes, not services.
def check_process(proc, file=":"):
    try:
        check = "ps auxww | grep [" + proc[0] + "]" + proc[1:] + " | grep " + file
        status = commands.getoutput(check)
        #print(status)
        if status:
            return True
        else:
            return False
    except:
        return False

def on_touch():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # button 1 event
    if originX <= touch_pos[0] <= (originX + buttonWidth) and originY <= touch_pos[1] <= (originY + buttonHeight):
            return 1
    # button 2 event
    if originX + buttonWidth + spacing <= touch_pos[0] <= originX + (buttonWidth * 2) + spacing and originY <= touch_pos[1] <= (originY + buttonHeight):
            return 2
    # button 3 event
    if originX + (buttonWidth * 2) + (spacing * 2) <= touch_pos[0] <= originX + (buttonWidth * 3) + (spacing * 2) and originY <= touch_pos[1] <= (originY + buttonHeight):
            return 3
    # button 4 event
    if originX <= touch_pos[0] <= (originX + buttonWidth) and (originY + buttonHeight + spacing) <= touch_pos[1] <= originY + (buttonHeight * 2) + spacing:
            return 4
    # button 5 event
    if originX + buttonWidth + spacing <= touch_pos[0] <= originX + (buttonWidth * 2) + spacing and originY + buttonHeight + spacing <= touch_pos[1] <= originY + (buttonHeight * 2) + spacing:
            return 5
    # button 6 event
    if originX + (buttonWidth * 2) + (spacing * 2) <= touch_pos[0] <= originX + (buttonWidth * 3) + (spacing * 2) and originY + buttonHeight + spacing <= touch_pos[1] <= originY + (buttonHeight * 2) + spacing:
            return 6
    # button 7 event
    if originX <= touch_pos[0] <= (originX + buttonWidth) and originY + (buttonHeight * 2) + (spacing * 2) <= touch_pos[1] <= originY + (buttonHeight * 3) + (spacing * 2):
            return 7
    # button 8 event
    if originX + buttonWidth + spacing <= touch_pos[0] <= originX + (buttonWidth * 2) + spacing and originY + (buttonHeight * 2) + (spacing * 2) <= touch_pos[1] <= originY + (buttonHeight * 3) + (spacing * 2):
            return 8
        # button 9 event
    if originX + (buttonWidth * 2) + (spacing * 2) <= touch_pos[0] <= originX + (buttonWidth * 3) + (spacing * 2) and originY + (buttonHeight * 2) + (spacing * 2) <= touch_pos[1] <= originY + (buttonHeight * 3) + (spacing * 2):
            return 9
