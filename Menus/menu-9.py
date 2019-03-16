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
label1 = Button(labelPadding * " " + " ", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_ora, tron_yel, labelFont)
label2 = Button(labelPadding * " " + " ", originX, originY, buttonHeight, buttonWidth * 3 + spacing * 2, tron_ora, tron_yel, labelFont)
label3 = Button(labelPadding * " " + " ", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth * 3 + spacing * 2, tron_ora, tron_yel, labelFont)
button7 = Button(labelPadding * " " + "       <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_ora, tron_yel, labelFont)
button9 = Button(labelPadding * " " + "     Refresh", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_ora, tron_yel, labelFont)


# Define each button press action
def button(number):

    if number == 7:
        if button7.disable == 1:
            return

        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-5.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 9:
        if button9.disable == 1:
            return

        # Refresh
        pygame.quit()
        menu9()

##        Buttons          ##
#############################

def menu9():

    # Init screen
    kalipi.screen()
    # Outer Border
    kalipi.border(tron_ora)

    #############################
    ##        Buttons          ##

    # Buttons and labels
    # See variables at the top of the document to adjust the menu

    # First Row
    # label 1
    label1.text=labelPadding * " " + kalipi.get_clock()
    label1.draw()


    # Second Row
    # Button 2
    label2.text=labelPadding * " " + kalipi.get_temp()
    label2.draw()

    # Third Row
    # Label 3
    label3.text=labelPadding * " " + kalipi.get_volts()
    label3.draw()

    # Fourth Row
    # Button 7
    button7.disable = 0  # "1" disables button

    if button7.disable == 1:
        button7.draw()
    else:
        # Add button launch code here
        button7.draw()

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
        butNo=kalipi.inputLoop("menu-9.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    menu9()
