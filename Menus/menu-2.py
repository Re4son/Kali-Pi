#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
##    Local Functions      ##

# Toggle ntopng
def toggle_ntopng():
    try:
        status = kalipi.run_cmd("/usr/sbin/service ntopng status")
        if ("is running" in status) or ("active (running)") in status:
            kalipi.run_cmd("/usr/sbin/service ntopng stop")
            kalipi.run_cmd("/bin/systemctl stop redis-server")
            return False
        else:
            kalipi.run_cmd("/bin/systemctl start redis-server")
            kalipi.run_cmd("/usr/sbin/service ntopng start")
            return True
    except:
        return False


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button(labelPadding * "  " + kalipi.get_date(), originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_blu, tron_ora, titleFont)
button1 = Button(labelPadding * " " + "      WWW", originX, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button2 = Button(labelPadding * " " + "       FTP", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button3 = Button(labelPadding * " " + "       SQL", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button4 = Button(labelPadding * " " + "     RAS-AP", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button5 = Button(labelPadding * " " + "   darkstat", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button6 = Button(labelPadding * " " + "    ntopng", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button7 = Button(labelPadding * " " + "        <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button8 = Button(labelPadding * " " + " Screen Off", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button9 = Button(labelPadding * " " + "        >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)



# Define each button press action
def button(number):

    if number == 1:
        if button1.disable == 1:
            return

	# WWW
        if kalipi.toggle_service("apache2"):
        #Stop Service
                button1.fntColor = green
                button1.draw()
                pygame.display.update()
        else:
        #Start Service
                button1.fntColor = tron_whi
                button1.draw()
                pygame.display.update()
        return

    if number == 2:
        if button2.disable == 1:
            return

        # FTP
        if kalipi.toggle_service("pure-ftpd"):
        #Stop Service
                button2.fntColor = green
                button2.draw()
                pygame.display.update()
        else:
        #Start Service
                button2.fntColor = tron_whi
                button2.draw()
                pygame.display.update()

    if number == 3:
        if button3.disable == 1:
            return

        # SQL
        if kalipi.toggle_service("mysql"):
                button3.fntColor = green
                button3.draw()
                pygame.display.update()

        else:
                button3.fntColor = tron_whi
                button3.draw()
                pygame.display.update()
        return

    if number == 4:
        if button4.disable == 1:
            return

        # Hostapd RAS-AP
        script=os.environ["MENUDIR"] + "RAS-AP/ras-ap.sh"

        if kalipi.toggle_script(script):
        # Stop Service
                button4.fntColor = green
                button4.draw()
                pygame.display.update()
        else:
        #Start Service
                button4.fntColor = tron_whi
                button4.draw()
                pygame.display.update()

    if number == 5:
        if button5.disable == 1:
            return

        # darkstat
        if kalipi.toggle_service("darkstat"):
                button5.fntColor = green
                button5.draw()
                pygame.display.update()

        else:
                button5.fntColor = tron_whi
                button5.draw()
                pygame.display.update()
        return

    if number == 6:
        if button6.disable == 1:
            return

        # ntopng
        if toggle_ntopng():
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

        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-1.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
        if button8.disable == 1:
            return
        # Screen off
        retPage="menu-2.py"
        kalipi.screensaver(retPage)
        menu2()

    if number == 9:
        if button9.disable == 1:
            return

        # Next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-3.py"
        os.execvp("python", ["python", page])
        sys.exit()
##        Buttons          ##
#############################


def menu2():

    # Init screen
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
        if kalipi.check_service("apache2"):
            button1.fntColor = green
            button1.draw()
        else:
            button1.fntColor = tron_whi
            button1.draw()

    # Button 2
    button2.disable = 0  # "1" disables button

    if button2.disable == 1:
        button2.draw()
    else:
        # Add button launch code here
        if kalipi.check_service("pure-ftpd"):
            button2.fntColor = green
            button2.draw()
        else:
            button2.fntColor = tron_whi
            button2.draw()

    # Button 3
    button3.disable = 0  # "1" disables button

    if button3.disable == 1:
        button3.draw()
    else:
        # Add button launch code here
        if kalipi.check_service("mysql"):
            button3.fntColor = green
            button3.draw()
        else:
            button3.fntColor = tron_whi
            button3.draw()

    # Button 4
    button4.disable = 0  # "1" disables button

    if button4.disable == 1:
        button4.draw()
    else:
        # Add button launch code here
        if kalipi.check_process("hostapd", "ras-ap.conf"):
            button4.fntColor = green
            button4.draw()
        else:
            button4.fntColor = tron_whi
            button4.draw()

    # Second Row
    # Button 5
    button5.disable = 0  # "1" disables button

    if button5.disable == 1:
        button5.draw()
    else:
        # Add button launch code here
        if kalipi.check_service("darkstat"):
            button5.fntColor = green
            button5.draw()
        else:
            button5.fntColor = tron_whi
            button5.draw()

    # Button 6
    button6.disable = 0  # "1" disables button

    if button6.disable == 1:
        button6.draw()
    else:
        # Add button launch code here
        if kalipi.check_service("ntopng"):
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
        butNo=kalipi.inputLoop("menu-2.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    menu2()
