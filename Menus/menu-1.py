#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
##    Local Functions      ##


# Check VNC status
def check_vnc():
    if 'vnc :1' in commands.getoutput('/bin/ps -ef'):
        return True
    else:
        return False

# Check Terminal session status
def check_terminal():
    if 'SCREEN -R -S term' in commands.getoutput('/bin/ps -ef'):
        return True
    else:
        return False


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button(" " + kalipi.get_hostname() + "    " + kalipi.get_ip(), originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_blu, tron_ora, titleFont)
button1 = Button(labelPadding * " " + "       Exit", originX, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button2 = Button(labelPadding * " " + "  X on TFT", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button3 = Button(labelPadding * " " + " X on HDMI", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button4 = Button(labelPadding * " " + "  Shutdown", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button5 = Button(labelPadding * " " + " Misc Tools", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button6 = Button(labelPadding * " " + "  Terminal", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu,tron_whi, labelFont)
button7 = Button(labelPadding * " " + "    Reboot", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button8 = Button(labelPadding * " " + " Screen Off", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button9 = Button(labelPadding * " " + "  Services", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)



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
        ## kalipi.run_cmd("/usr/bin/sudo -u " + KPUSER + " FRAMEBUFFER=/dev/fb1 startx")
        kalipi.run_cmd("/usr/bin/sudo FRAMEBUFFER=/dev/fb1 startx")
        os.execv(__file__, sys.argv)

    if number == 3:
        if button3.disable == 1:
            return

        # X HDMI
        pygame.quit()
        ## Requires "Anybody" in dpkg-reconfigure x11-common if we have scrolled pages previously
        ## kalipi.run_cmd("/usr/bin/sudo -u " + KPUSER + " FRAMEBUFFER=/dev/fb0 startx")
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

        # Next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-3.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 6:
        if button6.disable == 1:
            return

	# Terminal
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        pygame.quit()
        kalipi.run_cmd("/usr/bin/sudo -u " + KPUSER + " screen -R -S term")
        process = subprocess.call("setterm -term linux -back default -fore black -clear all", shell=True)
        os.execv(__file__, sys.argv)

        if check_terminal():
		button6.fntColor = green
		button6.draw()
		pygame.display.update()

	else:
		button6.fntColor = tron_whi
		button6.draw()
		pygame.display.update()
	return


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
        retPage="menu-1.py"
        kalipi.screensaver(retPage)
        menu1()

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


def menu1():

    # Init Pygame
    kalipi.screen()
    # Outer Border
    kalipi.border(tron_blu)

    #############################
    ##        Buttons          ##

    # Buttons and labels
    # See variables at the top of the document to adjust the menu

    # Title
    titleButton.draw()

    # First Row
    # Button 1
    button1.disable = 0  # "1" disables button

    if button1.disable == 1:
        button1.draw()
    else:
        # Add button launch code here
        button1.fntColor = yellow
        button1.draw()

    # Button 2
    button2.disable = 0  # "1" disables button

    if button2.disable == 1:
        button2.draw()
    else:
        # Add button launch code here
        button2.draw()

    # Button 3
    button3.disable = 0  # "1" disables button

    if button3.disable == 1:
        button3.draw()
    else:
        # Add button launch code here
        button3.draw()


    # Second Row
    # Button 4
    button4.disable = 0  # "1" disables button

    if button4.disable == 1:
        button4.draw()
    else:
        # Add button launch code here
        button4.fntColor = yellow
        button4.draw()

    # Button 5
    button5.disable = 0  # "1" disables button

    if button5.disable == 1:
        button5.draw()
    else:
	button5.draw()

    # Button 6
    button6.disable = 0  # "1" disables button

    if button6.disable == 1:
        button6.draw()
    else:
        # Add button launch code here
        if check_terminal():
            button6.fntColor = green
            button6.draw()
        else:
            button6.fntColor = tron_whi
            button6.draw()

    # Third Row
    # Button 7
    button7.disable = 0  # "1" disables button

    if button7.disable == 1:
        button7.draw()
    else:
        # Add button launch code here
        button7.fntColor = yellow
        button7.draw()

    # Button 8
    button8.disable = 0  # "1" disables button

    if button8.disable == 1:
        button8.draw()
    else:
        # Add button launch code here
        button8.draw()

    # Button 9
    button9.disable = 0  # "1" disables button

    if button9.disable == 1:
        button9.draw()
    else:
        # Add button launch code here
        button9.draw()

    ##        Buttons          ##
    #############################

    #############################
    ##        Input loop       ##

    while 1:
        butNo=kalipi.inputLoop("menu-1.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    menu1()
