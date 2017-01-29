#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
## Global display settings ##

#++++++++++++++++++++++++++++#
#+   Select color scheme    +#

# Tron theme orange
##tron_regular = tron_ora
##tron_light = tron_yel
##tron_inverse = tron_whi

# Tron theme blue
tron_regular = tron_blu
tron_light = tron_whi
tron_inverse = tron_yel

#+           End            +#
#++++++++++++++++++++++++++++#

## Global display settings ##
#############################

#############################
##    Local Functions      ##


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
titleButton = Button(" " + kalipi.get_hostname() + "    " + kalipi.get_ip(), originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, titleFont)
button1 = Button(labelPadding * " " + "       Exit", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button(labelPadding * " " + "  X on TFT", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button(labelPadding * " " + " X on HDMI", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_light, labelFont)
button4 = Button(labelPadding * " " + "  Shutdown", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button(labelPadding * " " + "VNC Server", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button(labelPadding * " " + "  Terminal", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button(labelPadding * " " + "    Reboot", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button(labelPadding * " " + " Screen Off", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button9 = Button(labelPadding * " " + "        >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)


def make_button(button):
    if button.disable == 1:
        button.color = grey

    pygame.draw.rect(screen, tron_regular, (button.xpo-10,button.ypo-10,button.width,button.height),3)
    pygame.draw.rect(screen, tron_light, (button.xpo-9,button.ypo-9,button.width-1,button.height-1),1)
    pygame.draw.rect(screen, tron_regular, (button.xpo-8,button.ypo-8,button.width-2,button.height-2),1)
    font=pygame.font.Font(None,button.fntSize)
    label=font.render(str(button.text), 1, (button.color))
    screen.blit(label,(button.xpo,button.ypo+7))

# Define each button press action
def button(number):

    if number == 1:
        if button1.disable == 1:
            return

        # Exit
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        pygame.quit()
        sys.exit(37)

    if number == 2:
        if button2.disable == 1:
            return

	# X TFT
        pygame.quit()
        ## Requires "Anybody" in dpkg-reconfigure x11-common if we have scrolled pages previously
        ## kalipi.run_cmd("/usr/bin/sudo -u pi FRAMEBUFFER=/dev/fb1 startx")
        kalipi.run_cmd("/usr/bin/sudo FRAMEBUFFER=/dev/fb1 startx")
        os.execv(__file__, sys.argv)

    if number == 3:
        if button3.disable == 1:
            return

        # X HDMI
        pygame.quit()
        ## Requires "Anybody" in dpkg-reconfigure x11-common if we have scrolled pages previously
        ## kalipi.run_cmd("/usr/bin/sudo -u pi FRAMEBUFFER=/dev/fb0 startx")
        kalipi.run_cmd("/usr/bin/sudo FRAMEBUFFER=/dev/fb0 startx")
        os.execv(__file__, sys.argv)

    if number == 4:
        if button4.disable == 1:
            return

        # Shutdown
        pygame.quit()
        kalipi.run_cmd("/usr/bin/sudo /sbin/shutdown -h now")
        sys.exit()

    if number == 5:
        if button5.disable == 1:
            return

	# VNC
	if check_vnc():
		kalipi.run_cmd("/usr/bin/vncserver -kill :1")
		button5.color = tron_light
		make_button(button5)
		pygame.display.update()

	else:
		kalipi.run_cmd("/usr/bin/vncserver :1")
		button5.color = green
		make_button(button5)
		pygame.display.update()
	return

    if number == 6:
        if button6.disable == 1:
            return

	# Terminal
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        pygame.quit()
        kalipi.run_cmd("/usr/bin/sudo -u pi screen -RR")
        os.execv(__file__, sys.argv)

    if number == 7:
        if button7.disable == 1:
            return

        # Reboot
        pygame.quit()
        kalipi.run_cmd("/usr/bin/sudo /sbin/shutdown -r now")
        sys.exit()

    if number == 8:
        if button8.disable == 1:
            return

        # Lock
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        retPage="menu-1.py"
        args = [page, retPage]
        os.execvp("python", ["python"] + args)
        sys.exit()

    if number == 9:
        if button9.disable == 1:
            return

        # Next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-2.py"
        os.execvp("python", ["python", page])
        sys.exit()

##        Buttons          ##
#############################


def main (argv):

    # Outer Border
    pygame.draw.rect(screen, tron_light, (0,0,screen_x,screen_y),10)

    #############################
    ##        Buttons          ##

    # Buttons and labels
    # See variables at the top of the document to adjust the menu

    # Title
    make_button(titleButton)

    # First Row
    # Button 1
    button1.disable = 0  # "1" disables button

    if button1.disable == 1:
        make_button(button1)
    else:
        # Add button launch code here
        button1.color = yellow
        make_button(button1)

    # Button 2
    button2.disable = 0  # "1" disables button

    if button2.disable == 1:
        make_button(button2)
    else:
        # Add button launch code here
        make_button(button2)

    # Button 3
    button3.disable = 0  # "1" disables button

    if button3.disable == 1:
        make_button(button3)
    else:
        # Add button launch code here
        make_button(button3)


    # Second Row
    # Button 4
    button4.disable = 0  # "1" disables button

    if button4.disable == 1:
        make_button(button4)
    else:
        # Add button launch code here
        button4.color = yellow
        make_button(button4)

    # Button 5
    button5.disable = 0  # "1" disables button

    if button5.disable == 1:
        make_button(button5)
    else:
        # Add button launch code here
        if check_vnc():
	    button5.color = green
	    make_button(button5)
        else:
	    button5.color = tron_light
	    make_button(button5)

    # Button 6
    button6.disable = 0  # "1" disables button

    if button6.disable == 1:
        make_button(button6)
    else:
        # Add button launch code here
        make_button(button6)

    # Third Row
    # Button 7
    button7.disable = 0  # "1" disables button

    if button7.disable == 1:
        make_button(button7)
    else:
        # Add button launch code here
        button7.color = yellow
        make_button(button7)

    # Button 8
    button8.disable = 0  # "1" disables button

    if button8.disable == 1:
        make_button(button8)
    else:
        # Add button launch code here
        make_button(button8)

    # Button 9
    button9.disable = 0  # "1" disables button

    if button9.disable == 1:
        make_button(button9)
    else:
        # Add button launch code here
        make_button(button9)

    ##        Buttons          ##
    #############################

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
                    num = kalipi.on_touch()
                    button(num)

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
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        retPage="menu-1.py"
        args = [page, retPage]
        os.execvp("python", ["python"] + args)
        sys.exit()


    else:
        #While loop to manage touch screen inputs
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                    num = kalipi.on_touch()
                    button(num)

                #Debug:
                #ensure there is always a safe way to end the program if the touch screen fails
                ##if event.type == KEYDOWN:
                ##    if event.key == K_ESCAPE:
                ##        sys.exit()

            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)


        ##        Input loop       ##
        #############################


if __name__ == "__main__":
    main(sys.argv[1:])
