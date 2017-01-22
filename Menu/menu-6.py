#!/usr/bin/env python
import sys, os, pygame, subprocess, commands, time, socket
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

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

# Tron theme orange
##tron_regular = tron_ora
##tron_light = tron_yel
##tron_inverse = tron_whi

# Tron theme blue
tron_regular = tron_blu
tron_light = tron_whi
tron_inverse = tron_yel

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

# Outer Border
pygame.draw.rect(screen, tron_light, (0,0,480,320),10)

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

# define function for printing text in a specific place with a specific width and height with a specific colour and border
#def make_button2(text, xpo, ypo, height, width, colour, fntSize):
#    pygame.draw.rect(screen, tron_regular, (xpo-10,ypo-10,width,height),3)
#    pygame.draw.rect(screen, tron_light, (xpo-9,ypo-9,width-1,height-1),1)
#    pygame.draw.rect(screen, tron_regular, (xpo-8,ypo-8,width-2,height-2),1)
#    font=pygame.font.Font(None,fntSize)
#    label=font.render(str(text), 1, (colour))
#    screen.blit(label,(xpo,ypo+7))

def make_button(button):
    pygame.draw.rect(screen, tron_regular, (button.xpo-10,button.ypo-10,button.width,button.height),3)
    pygame.draw.rect(screen, tron_light, (button.xpo-9,button.ypo-9,button.width-1,button.height-1),1)
    pygame.draw.rect(screen, tron_regular, (button.xpo-8,button.ypo-8,button.width-2,button.height-2),1)
    font=pygame.font.Font(None,button.fntSize)
    label=font.render(str(button.text), 1, (button.color))
    screen.blit(label,(button.xpo,button.ypo+7))


	
# define function for printing text in a specific place with a specific colour
def make_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

# define all of the buttons
titleButton = Button("                     EvilAP - Mana", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, 34)
button1 = Button("     AP Open", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button("    AP Secure", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button("         Mana", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, green, labelFont)
button4 = Button("         Beef", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button("     FireLamb", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button("    Mana Loud", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button("          <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button("    DNS2Proxy", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button9 = Button("          >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)


# define function that checks for touch location
def on_touch():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # button 1 event
    if originX <= touch_pos[0] <= (originX + buttonWidth) and originY <= touch_pos[1] <= (originY + buttonHeight):
            button(1)
    # button 2 event
    if originX + buttonWidth + spacing <= touch_pos[0] <= originX + (buttonWidth * 2) + spacing and originY <= touch_pos[1] <= (originY + buttonHeight):
            button(2)
    # button 3 event
    if originX + (buttonWidth * 2) + (spacing * 2) <= touch_pos[0] <= originX + (buttonWidth * 3) + (spacing * 2) and originY <= touch_pos[1] <= (originY + buttonHeight):
            button(3)
    # button 4 event
    if originX <= touch_pos[0] <= (originX + buttonWidth) and (originY + buttonHeight + spacing) <= touch_pos[1] <= originY + (buttonHeight * 2) + spacing:
            button(4)
    # button 5 event
    if originX + buttonWidth + spacing <= touch_pos[0] <= originX + (buttonWidth * 2) + spacing and originY + buttonHeight + spacing <= touch_pos[1] <= originY + (buttonHeight * 2) + spacing:
            button(5)
    # button 6 event
    if originX + (buttonWidth * 2) + (spacing * 2) <= touch_pos[0] <= originX + (buttonWidth * 3) + (spacing * 2) and originY + buttonHeight + spacing <= touch_pos[1] <= originY + (buttonHeight * 2) + spacing:
            button(6)
    # button 7 event
    if originX <= touch_pos[0] <= (originX + buttonWidth) and originY + (buttonHeight * 2) + (spacing * 2) <= touch_pos[1] <= originY + (buttonHeight * 3) + (spacing * 2):
            button(7)
    # button 8 event
    if originX + buttonWidth + spacing <= touch_pos[0] <= originX + (buttonWidth * 2) + spacing and originY + (buttonHeight * 2) + (spacing * 2) <= touch_pos[1] <= originY + (buttonHeight * 3) + (spacing * 2):
            button(8)
	# button 9 event
    if originX + (buttonWidth * 2) + (spacing * 2) <= touch_pos[0] <= originX + (buttonWidth * 3) + (spacing * 2) and originY + (buttonHeight * 2) + (spacing * 2) <= touch_pos[1] <= originY + (buttonHeight * 3) + (spacing * 2):
            button(9)


def get_date():
    d = time.strftime("%a, %d %b %Y  %H:%M:%S", time.localtime())
    return d

def run_cmd(cmd):
    process = Popen(cmd.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output

def check_mana():
    try:
	check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_get_state | grep 'ENABLE'"
	status = run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

def check_mana_loud():
    try:
	check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_state | grep 'ENABLE'"
	status = run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

# Get Your External IP Address
def get_ip():
    ip_msg = "Not connected"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.connect(('<broadcast>', 0))
        ip_msg=" IP: " + s.getsockname()[0]
    except Exception:
        pass
    return ip_msg


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

#This function is used to check individual processes, not services.
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

def toggle_FireLamb():
    check = "/usr/sbin/service FireLamb-manager status"
    start = "/usr/bin/FireLamb-start"
    stop = "/usr/bin/FireLamb-stop"
    status = run_cmd(check)
    if ("is running" in status) or ("active (running)") in status:
        run_cmd(stop)
        return False
    else:
	run_cmd(start)
        return True


# Define each button press action
def button(number):

    if number == 1:
		#Hostapd Open
        if toggle_script("/root/Desktop/Scripts/manaSimple.sh"):
        #Stop Service
        #cmd = "/root/Desktop/Scripts/manaSimple.sh stop"
        #commands.getoutput(cmd)
        #commands.getoutput("wall 'Stopping Mana'")
		button1.color = green
		make_button(button1)
		pygame.display.update()
	else:
        #Start Service
        #cmd = "/root/Desktop/Scripts/manaSimple.sh start"
        #commands.getoutput(cmd)
        #commands.getoutput("wall 'Starting Mana'")
		button1.color = tron_light
		make_button(button1)
		pygame.display.update()
	return

    if number == 2:
        #Hostapd Secure
        if toggle_script("/root/Desktop/Scripts/manaSecure.sh"):
        #Stop Service
		button2.color = green
		make_button(button2)
		pygame.display.update()
	else:
        #Start Service
		button2.color = tron_light
		make_button(button2)
		pygame.display.update()

    if number == 3:
        #Mana Attack
        if check_mana():
        #Stop Mana
		run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_disable")
		#make_button("         Mana", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_light, labelFont)
		button3.color = tron_light
		make_button(button3)
		pygame.display.update()
	else:
        #Start Mana
		run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_enable")
		#make_button("         Mana", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, green, labelFont)
		button3.color = green
		make_button(button3)
		pygame.display.update()

    if number == 4:
	if toggle_service("beef-xss"):
		button4.color = green
		make_button(button4)
		pygame.display.update()

	else:
		button4.color = tron_light
		make_button(button4)
		pygame.display.update()
	return

    if number == 5:
	if toggle_FireLamb():
		button5.color = green
		make_button(button5)
		pygame.display.update()

	else:
		button5.color = tron_light
		make_button(button5)
		pygame.display.update()
	return

    if number == 6:
        #Mana Loud Attack
        if check_mana_loud():
        #Stop Mana
		run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_off")
		button6.color = tron_light
		make_button(button6)
		pygame.display.update()
	else:
        #Start Mana Loud Attack
		run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_on")
		button6.color = green
		make_button(button6)
		pygame.display.update()

    if number == 7:
        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-5.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
		#DNS2Proxy
        if toggle_script("/root/Desktop/Scripts/dns2proxy.sh"):
        #Stop Service
		button8.color = green
		make_button(button8)
		pygame.display.update()
	else:
        #Start Service
		button8.color = tron_light
		make_button(button8)
		pygame.display.update()
	return

    if number == 9:
        # Next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-9.py"
        os.execvp("python", ["python", page])
        sys.exit()



# Buttons and labels
#See variables at the top of the document to adjust the menu
#Title
make_button(titleButton)
#First Row
if check_process("hostapd", "mana.conf"):
	button1.color = green
	make_button(button1)
else:
	button1.color = tron_light
	make_button(button1)

if check_process("hostapd", "wpa2.conf"):
	button2.color = green
	make_button(button2)
else:
	button2.color = tron_light
	make_button(button2)

if check_mana():
	button3.color = green
	make_button(button3)

else:
	button3.color = tron_light
	make_button(button3)

# Second Row
if check_service("beef-xss"):
	button4.color = green
	make_button(button4)
else:
	button4.color = tron_light
	make_button(button4)

if check_service("FireLamb-manager"):
	button5.color = green
	make_button(button5)
else:
	button5.color = red
	make_button(button5)
	
if check_mana_loud():
	button6.color = green
	make_button(button6)
	
else:
	button6.color = tron_light
	make_button(button6)
	
# Third Row
make_button(button7)

if check_process("python", "dns2proxy.py"):
	button8.color = green
	make_button(button8)
else:
	button8.color = tron_light
	make_button(button8)

make_button(button9)


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
