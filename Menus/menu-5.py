#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
##    Local Functions      ##


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                      My custom menu", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_blu, tron_ora, titleFont)
button1 = Button(labelPadding * " " + "   Bettercap", originX, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button2 = Button(labelPadding * " " + " Warberry", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button3 = Button(labelPadding * " " + "  Wifiphisher.", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button4 = Button(labelPadding * " " + "   to add", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button5 = Button(labelPadding * " " + "to add", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button6 = Button(labelPadding * " " + "    to add", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button7 = Button(labelPadding * " " + "       <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button8 = Button(labelPadding * " " + "   Cleanup", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button9 = Button(labelPadding * " " + "       >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)


# Define each button press action
def button(number):

    if number == 1:
        if button1.disable == 1:
            return

        # NAT Full
        run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd bettercap_enable")
        if kalipi.toggle_script(script):
                button1.fntColor = green
                button1.draw()
                pygame.display.update()
        else:
                button1.fntColor = tron_light
                button1.draw()
                pygame.display.update()
        return

    if number == 2:
        if button2.disable == 1:
            return

        # NAT Simple
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-nat-simple.sh"
        if kalipi.toggle_script(script):
                button2.fntColor = green
                button2.draw()
                pygame.display.update()
        else:
                button2.fntColor = tron_light
                button2.draw()
                pygame.display.update()
        return

    if number == 3:
        if button3.disable == 1:
            return

        # No Upstream
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream.sh"
        if kalipi.toggle_script(script):
                button3.fntColor = green
                button3.draw()
                pygame.display.update()
        else:
                button3.fntColor = tron_light
                button3.draw()
                pygame.display.update()
        return

    if number == 4:
        if button4.disable == 1:
            return

        # No Upstream EAP
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eap.sh"
        if kalipi.toggle_script(script):
                button4.fntColor = green
                button4.draw()
                pygame.display.update()
        else:
                button4.fntColor = tron_light
                button4.draw()
                pygame.display.update()
        return

    if number == 5:
        if button5.disable == 1:
            return

        # No Upstream EAP only
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eaponly.sh"
        if kalipi.toggle_script(script):
                button5.fntColor = green
                button5.draw()
                pygame.display.update()
        else:
                button5.fntColor = tron_light
                button5.draw()
                pygame.display.update()
        return

    if number == 6:
        if button6.disable == 1:
            return

        # No Upstream All
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-all.sh"
        if kalipi.toggle_script(script):
                button6.fntColor = green
                button6.draw()
                pygame.display.update()
        else:
                button6.fntColor = tron_light
                button6.draw()
                pygame.display.update()
        return

    if number == 7:
        if button7.disable == 1:
            return

        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-4.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
        if button8.disable == 1:
            return

        #Cleanup
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/cleanmana.sh"
        kalipi.run_cmd(script)
        button1.fntColor = tron_light
        button1.draw()
        button2.fntColor = tron_light
        button2.draw()
        button3.fntColor = tron_light
        button3.draw()
        button4.fntColor = tron_light
        button4.draw()
        button5.fntColor = tron_light
        button5.draw()
        button6.fntColor = tron_light
        button6.draw()
        button8.fntColor = tron_light
        button8.draw()
        return

    if number == 9:
        if button9.disable == 1:
            return

        # Next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-9.py"
        os.execvp("python", ["python", page])
        sys.exit()
##        Buttons          ##
#############################


def menu5():

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
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-nat-full.sh"
        if kalipi.check_script(script):
            button1.fntColor = green
            button1.draw()
        else:
            button1.draw()


    # Button 2
    button2.disable = 0  # "1" disables button

    if button2.disable == 1:
        button2.draw()
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-nat-simple.sh"
        if kalipi.check_script(script):
            button2.fntColor = green
            button2.draw()
        else:
            button2.draw()


    # Button 3
    button3.disable = 0  # "1" disables button

    if button3.disable == 1:
        button3.draw()
    else:
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream.sh"
        if kalipi.check_script(script):
            button3.fntColor = green
            button3.draw()
        else:
            button3.draw()


    # Second Row
    # Button 4
    button4.disable = 0  # "1" disables button

    if button4.disable == 1:
        button4.draw()
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eap.sh"
        if kalipi.check_script(script):
            button4.fntColor = green
            button4.draw()
        else:
            button4.draw()


    # Button 5
    button5.disable = 0  # "1" disables button

    if button5.disable == 1:
        button5.draw()
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eaponly.sh"
        if kalipi.check_script(script):
            button5.fntColor = green
            button5.draw()
        else:
            button5.draw()

    # Button 6
    button6.disable = 0  # "1" disables button

    if button6.disable == 1:
        button6.draw()
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eaponly.sh"
        if kalipi.check_script(script):
            button6.fntColor = green
            button6.draw()
        else:
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
        butNo=kalipi.inputLoop("menu-5.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    menu5()

