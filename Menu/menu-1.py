#!/usr/bin/env python
import sys, os, time, subprocess, commands, pygame
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
launch_bg=os.environ["MENUDIR"] + "launch-bg.sh"
process = subprocess.call(launch_bg, shell=True)

# Initialize pygame modules individually (to avoid ALSA errors) and hide mouse
pygame.font.init()
pygame.display.init()

pygame.mouse.set_visible(0)

# define function for printing text in a specific place with a specific width and height with a specific colour and border
def make_button(text, xpo, ypo, height, width, colour):
    pygame.draw.rect(screen, tron_regular, (xpo-10,ypo-10,width,height),3)
    pygame.draw.rect(screen, tron_light, (xpo-9,ypo-9,width-1,height-1),1)
    pygame.draw.rect(screen, tron_regular, (xpo-8,ypo-8,width-2,height-2),1)
    font=pygame.font.Font(None,42)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))


# define function for printing text in a specific place with a specific colour
def make_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

# define function that checks for touch location
def on_touch():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # button 1 event
    if 30 <= touch_pos[0] <= 240 and 105 <= touch_pos[1] <=160:
            button(1)
    # button 2 event
    if 260 <= touch_pos[0] <= 470 and 105 <= touch_pos[1] <=160:
            button(2)
    # button 3 event
    if 30 <= touch_pos[0] <= 240 and 180 <= touch_pos[1] <=235:
            button(3)
    # button 4 event
    if 260 <= touch_pos[0] <= 470 and 180 <= touch_pos[1] <=235:
            button(4)
    # button 5 event
    if 30 <= touch_pos[0] <= 240 and 255 <= touch_pos[1] <=310:
            button(5)
    # button 6 event
    if 260 <= touch_pos[0] <= 470 and 255 <= touch_pos[1] <=310:
            button(6)

def run_cmd(cmd):
    process = Popen(cmd.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output


# Define each button press action
def button(number):
    if number == 1:
        # X TFT
        pygame.quit()
        ## Requires "Anybody" in dpkg-reconfigure x11-common if we have scrolled pages previously
##        run_cmd("/usr/bin/sudo -u pi FRAMEBUFFER=/dev/fb1 startx")
        run_cmd("/usr/bin/sudo FRAMEBUFFER=/dev/fb1 startx")
        os.execv(__file__, sys.argv)

    if number == 2:
        # X HDMI
        pygame.quit()
        ## Requires "Anybody" in dpkg-reconfigure x11-common if we have scrolled pages previously
##        run_cmd("/usr/bin/sudo -u pi FRAMEBUFFER=/dev/fb0 startx")
        run_cmd("/usr/bin/sudo FRAMEBUFFER=/dev/fb0 startx")
        os.execv(__file__, sys.argv)


    if number == 3:
        # terminal
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        pygame.quit()
        run_cmd("/usr/bin/sudo -u pi screen -RR")
        os.execv(__file__, sys.argv)

    if number == 4:
        # htop
        pygame.quit()
	process = subprocess.call("/usr/bin/htop", shell=True)
        os.execv(__file__, sys.argv)

    if number == 5:
        # next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 6:
        # next page
        pygame.quit()
        ##startx only works when we don't use subprocess here, don't know why
	page=os.environ["MENUDIR"] + "menu-2.py"
	os.execvp("python", ["python", page])
        sys.exit()



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
tron_yel = (255, 218,  10)
orange   = (255, 127,   0)
tron_ora = (255, 202,   0)

# Tron theme orange
tron_regular = tron_ora
tron_light   = tron_yel
tron_inverse = tron_whi

# Tron theme blue
##tron_regular = tron_blu
##tron_light   = tron_whi
##tron_inverse = tron_yel

# Set up the base menu you can customize your menu with the colors above

#set size of the screen
size = width, height = 480, 320
screen = pygame.display.set_mode(size)

# Background Color
screen.fill(black)

# Outer Border
pygame.draw.rect(screen, tron_regular, (0,0,479,319),8)
pygame.draw.rect(screen, tron_light, (2,2,479-4,319-4),2)

pi_hostname = run_cmd("hostname")
pi_hostname = "  " + pi_hostname[:-1]
# Buttons and labels
# First Row Label
make_label(pi_hostname, 32, 30, 48, tron_inverse)
# Second Row buttons 3 and 4
make_button("    X on TFT", 30, 105, 55, 210, tron_light)
make_button("   X on HDMI", 260, 105, 55, 210, tron_light)
# Third Row buttons 5 and 6
make_button("    Terminal", 30, 180, 55, 210, tron_light)
make_button("        hTop", 260, 180, 55, 210, tron_light)
# Fourth Row Buttons
make_button("   Screen Off", 30, 255, 55, 210, tron_light)
make_button("          >>>", 260, 255, 55, 210, tron_light)


#While loop to manage touch screen inputs
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            on_touch()

        #ensure there is always a safe way to end the program if the touch screen fails
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
    ## Reduce CPU utilisation
    time.sleep(0.1)
