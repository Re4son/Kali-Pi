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


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                      EvilAP - Mana", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, titleFont)
button1 = Button(labelPadding * " " + "   NAT Full", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button(labelPadding * " " + " NAT Simple", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button(labelPadding * " " + "No Upstream", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_light, labelFont)
button4 = Button(labelPadding * " " + "   NU-EAP", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button(labelPadding * " " + "NU-EAP only", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button(labelPadding * " " + "    NU-All", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button(labelPadding * " " + "       <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button(labelPadding * " " + "Cleanup", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button9 = Button(labelPadding * " " + "       >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)


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

        # NAT Full
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-nat-full.sh"
        if kalipi.toggle_script(script):
                button1.color = green
                make_button(button1)
                pygame.display.update()
        else:
                button1.color = tron_light
                make_button(button1)
                pygame.display.update()
        return

    if number == 2:
        if button2.disable == 1:
            return

        # NAT Simple
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-nat-simple.sh"
        if kalipi.toggle_script(script):
                button2.color = green
                make_button(button2)
                pygame.display.update()
        else:
                button2.color = tron_light
                make_button(button2)
                pygame.display.update()
        return

    if number == 3:
        if button3.disable == 1:
            return

        # No Upstream
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream.sh"
        if kalipi.toggle_script(script):
                button3.color = green
                make_button(button3)
                pygame.display.update()
        else:
                button3.color = tron_light
                make_button(button3)
                pygame.display.update()
        return

    if number == 4:
        if button4.disable == 1:
            return

        # No Upstream EAP
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eap.sh"
        if kalipi.toggle_script(script):
                button4.color = green
                make_button(button4)
                pygame.display.update()
        else:
                button4.color = tron_light
                make_button(button4)
                pygame.display.update()
        return

    if number == 5:
        if button5.disable == 1:
            return

        # No Upstream EAP only
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eaponly.sh"
        if kalipi.toggle_script(script):
                button5.color = green
                make_button(button5)
                pygame.display.update()
        else:
                button5.color = tron_light
                make_button(button5)
                pygame.display.update()
        return

    if number == 6:
        if button6.disable == 1:
            return

        # No Upstream All
        script="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-all.sh"
        if kalipi.toggle_script(script):
                button6.color = green
                make_button(button6)
                pygame.display.update()
        else:
                button6.color = tron_light
                make_button(button6)
                pygame.display.update()
        return

    if number == 7:
        if button7.disable == 1:
            return

        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-3.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
        if button8.disable == 1:
            return

        #Cleanup
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/cleanmana.sh"
        kalipi.run_cmd(script)
        button1.color = tron_light
        make_button(button1)
        button2.color = tron_light
        make_button(button2)
        button3.color = tron_light
        make_button(button3)
        button4.color = tron_light
        make_button(button4)
        button5.color = tron_light
        make_button(button5)
        button6.color = tron_light
        make_button(button6)
        button8.color = tron_light
        make_button(button8)
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
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-nat-full.sh"
        if kalipi.check_script(script):
            button1.color = green
            make_button(button1)
        else:
            make_button(button1)


    # Button 2
    button2.disable = 0  # "1" disables button

    if button2.disable == 1:
        make_button(button2)
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-nat-simple.sh"
        if kalipi.check_script(script):
            button2.color = green
            make_button(button2)
        else:
            make_button(button2)


    # Button 3
    button3.disable = 0  # "1" disables button

    if button3.disable == 1:
        make_button(button3)
    else:
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream.sh"
        if kalipi.check_script(script):
            button3.color = green
            make_button(button3)
        else:
            make_button(button3)


    # Second Row
    # Button 4
    button4.disable = 0  # "1" disables button

    if button4.disable == 1:
        make_button(button4)
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eap.sh"
        if kalipi.check_script(script):
            button4.color = green
            make_button(button4)
        else:
            make_button(button4)


    # Button 5
    button5.disable = 0  # "1" disables button

    if button5.disable == 1:
        make_button(button5)
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eaponly.sh"
        if kalipi.check_script(script):
            button5.color = green
            make_button(button5)
        else:
            make_button(button5)

    # Button 6
    button6.disable = 0  # "1" disables button

    if button6.disable == 1:
        make_button(button6)
    else:
        # Add button launch code here
        script="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "mana/kalipi-noupstream-eaponly.sh"
        if kalipi.check_script(script):
            button6.color = green
            make_button(button6)
        else:
            make_button(button6)

    # Third Row
    # Button 7
    button7.disable = 0  # "1" disables button

    if button7.disable == 1:
        make_button(button7)
    else:
        # Add button launch code here
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

    while 1:
        butNo=kalipi.inputLoop("menu-4.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    main(sys.argv[1:])

