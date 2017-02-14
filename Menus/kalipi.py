#!/usr/bin/env python
import sys, os, pygame, subprocess, commands, time, socket
import RPi.GPIO as GPIO
from pygame.locals import *
if "TFT" in os.environ and os.environ["TFT"] == "0":
    pass
else:
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
    os.environ["SDL_MOUSEDRV"] = "TSLIB"

#####################################################
##           Global display settings               ##


# colors    R    G    B
white    = (255, 255, 255)
tron_whi = (189, 254, 255)
grey     = ( 50,  50,  50)
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



###########################
##  Screen layouts       ##

## 3.5" screens: ##
if os.environ["KPSCREENSIZE"] == "3.5":
#  9 Button Layout  #
    if os.environ["KPLAYOUT"] == "9":
        #set size of the screen
        screen_x = 480
        screen_y = 320

        size = width, height = screen_x, screen_y
##        screen = pygame.display.set_mode(size)

        #Define the aspect of the menu
        originX = 40
        originY = 115
        spacing = 10
        buttonWidth = 133
        buttonHeight = 55
        labelFont = 24
        labelPadding = 3
        titleFont = 34

# 2.8" Screens:
else:
#  9 Button Layout  #
    if os.environ["KPLAYOUT"] == "9":
        #set size of the screen
        screen_x = 320
        screen_y = 240

        size = width, height = screen_x, screen_y
##        screen = pygame.display.set_mode(size)

        #Define the aspect of the menu
        originX = 22
        originY = 85
        spacing = 5
        buttonWidth = 96
        buttonHeight = 48
        labelFont = 19
        labelPadding = 0
        titleFont = 26

##  Screen layouts       ##
###########################

##           Global display settings               ##
#####################################################


#############################
##   Global Functions      ##

# Create button
class Button(object):
        text = ""
        xpo = ""
        ypo = ""
        height = ""
        width = ""
        color = ""
        fntColor = ""
        fntSize = ""
        disable = ""
        def __init__(self, text, xpo, ypo, height, width, color, fntColor, fntSize, disable=0):
                self.text = text
                self.xpo = xpo
                self.ypo = ypo
                self.height = height
                self.width = width
                self.color = color
                self.fntColor = fntColor
                self.fntSize = fntSize
                self.disable = disable
        def draw(self):
                if self.disable == 1:
                    self.fntColor = grey

                if self.color == tron_blu:
                    pygame.draw.rect(screen.canvas, tron_blu, (self.xpo-10,self.ypo-10,self.width,self.height),3)
                    pygame.draw.rect(screen.canvas, tron_whi, (self.xpo-9,self.ypo-9,self.width-1,self.height-1),1)
                    pygame.draw.rect(screen.canvas, tron_blu, (self.xpo-8,self.ypo-8,self.width-2,self.height-2),1)
                    font=pygame.font.Font(None,self.fntSize)
                    label=font.render(str(self.text), 1, (self.fntColor))
                    screen.canvas.blit(label,(self.xpo,self.ypo+7))
                elif self.color == tron_ora:
                    pygame.draw.rect(screen.canvas, tron_ora, (self.xpo-10,self.ypo-10,self.width,self.height),3)
                    pygame.draw.rect(screen.canvas, tron_yel, (self.xpo-9,self.ypo-9,self.width-1,self.height-1),1)
                    pygame.draw.rect(screen.canvas, tron_ora, (self.xpo-8,self.ypo-8,self.width-2,self.height-2),1)
                    font=pygame.font.Font(None,self.fntSize)
                    label=font.render(str(self.text), 1, (self.fntColor))
                    screen.canvas.blit(label,(self.xpo,self.ypo+7))
                else:
                    pygame.draw.rect(screen.canvas, self.color, (self.xpo-10,self.ypo-10,self.width,self.height),3)
                    pygame.draw.rect(screen.canvas, self.color, (self.xpo-9,self.ypo-9,self.width-1,self.height-1),1)
                    pygame.draw.rect(screen.canvas, self.color, (self.xpo-8,self.ypo-8,self.width-2,self.height-2),1)
                    font=pygame.font.Font(None,self.fntSize)
                    label=font.render(str(self.text), 1, (self.fntColor))
                    screen.canvas.blit(label,(self.xpo,self.ypo+7))


# Initialis the screen
def screen():
    pygame.font.init()
    pygame.display.init()

    if "TFT" in os.environ and os.environ["TFT"] == "0":
        pygame.mouse.set_visible(1)
    else:
        pygame.mouse.set_visible(0)
        
    screen.canvas = pygame.display.set_mode(size)

    # Background Color
    screen.canvas.fill(black)
    return True

# Draw the outer border
def border(color):
    if color == tron_blu:
        pygame.draw.rect(screen.canvas, tron_blu, (0,0,screen_x-1,screen_y-1),8)
        pygame.draw.rect(screen.canvas, tron_whi, (2,2,screen_x-5,screen_y-5),2)
    elif color == tron_ora:
        pygame.draw.rect(screen.canvas, tron_ora, (0,0,screen_x-1,screen_y-1),8)
        pygame.draw.rect(screen.canvas, tron_yel, (2,2,screen_x-5,screen_y-5),2)
    else:
        pygame.draw.rect(screen.canvas, color, (0,0,screen_x-1,screen_y-1),8)
        pygame.draw.rect(screen.canvas, color, (2,2,screen_x-5,screen_y-5),2)


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
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    temp = 'Temp: ' + output[5:-1]
    return temp

def get_clock():
    command = "vcgencmd measure_clock arm"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    clock = output.split("=")
    clock = int(clock[1][:-1]) / 1024 /1024
    clock = 'Clock: ' + str(clock) + "MHz"
    return clock

def get_volts():
    command = "vcgencmd measure_volts"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    volts = 'Core:   ' + output[5:-1]
    return volts

# Run command
def run_cmd(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
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

# Check script
def check_script(script):
    check = script + " status"
    status = subprocess.call(check, shell=True)
    if (status == 1) :
        return True
    else:
        return False

# Toggle script
def toggle_script(script):
    check = script + " status"
    start = script + " start"
    stop = script + " stop"
    status = subprocess.call(check, shell=True)
    if (status == 1) :
        subprocess.call(stop, shell=True)
        return False
    else:
        subprocess.call(start, shell=True)
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

# define function for printing text in a specific place with a specific colour
def make_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

# Get return page
def get_retPage():
    retPage = "menu-1.py"
    if len(sys.argv) > 1:
        retPage = str(sys.argv[1])
    return retPage

# Screensaver
def screensaver(retPage="menu-1.py"):

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

    #While loop to manage touch screen inputs
    screen_off(backlightControl)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen_on(retPage, backlightControl)
                return()
                #Debug:
                #ensure there is always a safe way to end the program if the touch screen fails
                ##if event.type == KEYDOWN:
                ##    if event.key == K_ESCAPE:
                ##        sys.exit()
        time.sleep(0.4)

# Turn screen on
def screen_on(retPage, backlightControl):

    if os.environ["KPPIN"] != "1":
        launch_bg=os.environ["MENUDIR"] + "launch-bg.sh"
        process = subprocess.call(launch_bg, shell=True)

    pygame.quit()
    if backlightControl == "3.5r":
        process = subprocess.call("echo '1' > /sys/class/backlight/soc\:backlight/brightness", shell=True)
    else:
        backlight = GPIO.PWM(18, 1023)
        backlight.start(100)
        GPIO.cleanup()
    if os.environ["KPPIN"] == "1":
        page=os.environ["MENUDIR"] + "menu-pin.py"
        args = [page, retPage]
    else:
        page=os.environ["MENUDIR"] + retPage
        args = [page]

    os.execvp("python", ["python"] + args)

# Turn screen off
def screen_off(backlightControl):

    screen.canvas.fill(black)
    pygame.display.update()
    if backlightControl == "3.5r":
        process = subprocess.call("echo '0' > /sys/class/backlight/soc\:backlight/brightness", shell=True)
    else:
        backlight = GPIO.PWM(18, 0.1)
        backlight.start(0)

    process = subprocess.call("setterm -term linux -back black -fore white -clear all", shell=True)
    return()

# Input loop for touch event
def inputLoop(retPage="menu-1.py"):
    #############################
    ##        Input loop       ##

    if "KPTIMEOUT" in os.environ:
        timeout = float(os.environ["KPTIMEOUT"]) * 60 / 3 # Convert timeout to seconds

        #While loop to manage touch screen inputs
        t = timeout
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    t = timeout
                    pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                    num = on_touch()
                    return(num)

                #Debug
                #ensure there is always a safe way to end the program if the touch screen fails
                ##if event.type == KEYDOWN:
                ##    if event.key == K_ESCAPE:
                ##        sys.exit()

            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)
            t = t - 0.1

            if t <= 0:
                break

        ## Screensaver
        screensaver(retPage)

    else:
        #While loop to manage touch screen inputs
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                    num = on_touch()
                    return(num)

                #Debug:
                #ensure there is always a safe way to end the program if the touch screen fails
                ##if event.type == KEYDOWN:
                ##    if event.key == K_ESCAPE:
            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)
    return

        ##        Input loop       ##
        #############################

