#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
## Global display settings ##

#++++++++++++++++++++++++++++#
#+   Select color scheme    +#
global tron_regular, tron_light, tron_inverse
# Tron theme orange
##tron_regular = tron_ora
##tron_light = tron_yel
##tron_inverse = tron_whi

# Tron theme blue
##global tron_blu, tron_whi, tron_yel
tron_regular = tron_blu
tron_light = tron_whi
tron_inverse = tron_yel

#+           End            +#
#++++++++++++++++++++++++++++#

# Outer Border
pygame.draw.rect(screen, tron_light, (0,0,screen_x,screen_y),10)

## Global display settings ##
#############################

#############################
##    Local Functions      ##

# Check mana status
def check_mana():
    try:
	check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_get_state | grep 'ENABLE'"
	status = kalipi.run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

# Check mana_loud status
def check_mana_loud():
    try:
	check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_state | grep 'ENABLE'"
	status = kalipi.run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

# Toggle FireLamp
def toggle_FireLamb():
    check = "/usr/sbin/service FireLamb-manager status"
    start = "/usr/bin/FireLamb-start"
    stop = "/usr/bin/FireLamb-stop"
    status = kalipi.run_cmd(check)
    if ("is running" in status) or ("active (running)") in status:
        run_cmd(stop)
        return False
    else:
	run_cmd(start)
        return True

# Check VNC status
def check_vnc():
    if 'vnc :1' in commands.getoutput('/bin/ps -ef'):
        return True
    else:
        return False


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                  System Services", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, 34)
button1 = Button("      Apache2", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button("          FTP", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button("     Shutdown", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, green, labelFont)
button4 = Button("   VNC Server", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button("          SMB", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button("        Restart", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button("          <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button("      Bluetooth", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button9 = Button("          >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)


def make_button(button):
    pygame.draw.rect(screen, tron_regular, (button.xpo-10,button.ypo-10,button.width,button.height),3)
    pygame.draw.rect(screen, tron_light, (button.xpo-9,button.ypo-9,button.width-1,button.height-1),1)
    pygame.draw.rect(screen, tron_regular, (button.xpo-8,button.ypo-8,button.width-2,button.height-2),1)
    font=pygame.font.Font(None,button.fntSize)
    label=font.render(str(button.text), 1, (button.color))
    screen.blit(label,(button.xpo,button.ypo+7))

# Define each button press action
def button(number):

    if number == 1:
	#WWW
        if kalipi.toggle_service("apache2"):
        #Stop Service
		button1.color = green
		make_button(button1)
		pygame.display.update()
	else:
        #Start Service
		button1.color = tron_light
		make_button(button1)
		pygame.display.update()
	return

    if number == 2:
        #FTP
        if kalipi.toggle_service("pure-ftpd"):
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
        #Shutdown
         pygame.quit()
         kalipi.shutdown()
         sys.exit()

    if number == 4:
	#VNC
	if kalipi.check_process("Xtightvnc", ":1"):
		kalipi.run_cmd("pkill Xtightvnc")
		button4.color = tron_light
		make_button(button4)
		pygame.display.update()

	else:
		kalipi.run_cmd("su root -c vncserver")
		button4.color = green
		make_button(button4)
		pygame.display.update()
	return

    if number == 5:
	#SMB
	if kalipi.toggle_service("smbd"):
		button5.color = green
		make_button(button5)
		pygame.display.update()

	else:
		button5.color = tron_light
		make_button(button5)
		pygame.display.update()
	return

    if number == 6:
        #Reboot
         screen.fill(black)
         font=pygame.font.Font(None,72)
         label=font.render("Rebooting. .", 1, (white))
         screen.blit(label,(40,120))
         pygame.display.flip()
         pygame.quit()
         kalipi.restart()
         sys.exit()

    if number == 7:
        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-1.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
	#Bluetooth
        if kalipi.toggle_service("hciuart"):
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
        page=os.environ["MENUDIR"] + "menu-6.py"
        os.execvp("python", ["python", page])
        sys.exit()


# Buttons and labels
# See variables at the top of the document to adjust the menu

# Title
make_button(titleButton)

# First Row
# Button 1
if kalipi.check_service("apache2"):
	button1.color = green
	make_button(button1)
else:
	button1.color = tron_light
	make_button(button1)

# Button 2
if kalipi.check_service("pure-ftpd"):
	button2.color = green
	make_button(button2)
else:
	button2.color = tron_light
	make_button(button2)

# Button 3
button3.color = yellow
make_button(button3)


# Second Row
# Button 4
if kalipi.check_process("Xtightvnc", ":1"):
	button4.color = green
	make_button(button4)
else:
	button4.color = tron_light
	make_button(button4)

# Button 5
if kalipi.check_service("smbd"):
	button5.color = green
	make_button(button5)
else:
	button5.color = tron_light
	make_button(button5)

# Button 6
button6.color = yellow
make_button(button6)


# Third Row
# Button 7
make_button(button7)

# Button 8
if kalipi.check_service("hciuart"):
	button8.color = green
	make_button(button8)
else:
	button8.color = tron_light
	make_button(button8)

# Button 9
make_button(button9)

##        Buttons          ##
#############################


#############################
##        Input loop       ##

#While loop to manage touch screen inputs
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            num = kalipi.on_touch()
            button(num)

        #ensure there is always a safe way to end the program if the touch screen fails
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
    ## Reduce CPU utilisation
    time.sleep(0.1)

##        Input loop       ##
#############################
