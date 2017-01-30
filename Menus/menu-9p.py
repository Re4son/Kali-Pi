#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
## Global display settings ##

#++++++++++++++++++++++++++++#
#+   Select color scheme    +#

# Tron theme orange
tron_regular = tron_ora
tron_light = tron_yel
tron_inverse = tron_whi

# Tron theme blue
##tron_regular = tron_blu
##tron_light = tron_whi
##tron_inverse = tron_yel

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
label1 = Button(labelPadding * " " + kalipi.get_clock(), originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_light, labelFont)
label2 = Button(labelPadding * " " + kalipi.get_temp(), originX, originY, buttonHeight, buttonWidth * 3 + spacing * 2, tron_light, labelFont)
label3 = Button(labelPadding * " " + kalipi.get_volts(), originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth * 3 + spacing * 2, tron_light, labelFont)
button7 = Button(labelPadding * " " + "       <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button9 = Button(labelPadding * " " + "     Refresh", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)


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

    if number == 7:
        if button7.disable == 1:
            return

        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-pin.py"
        retPage=kalipi.get_retPage()
        args = [page, retPage]
        os.execvp("python", ["python"] + args)
        sys.exit()

    if number == 9:
        if button9.disable == 1:
            return

        # Refresh
        pygame.quit()
        os.execv(__file__, sys.argv)

##        Buttons          ##
#############################


def main (argv):

    # Outer Border
    pygame.draw.rect(screen, tron_light, (0,0,screen_x,screen_y),10)

    #############################
    ##        Buttons          ##

    # Buttons and labels
    # See variables at the top of the document to adjust the menu

    # First Row
    # label 1
    make_button(label1)

    # Second Row
    # Button 2
    make_button(label2)

    # Third Row
    # Label 3
    make_button(label3)

    # Fourth Row
    # Button 7
    button7.disable = 0  # "1" disables button

    if button7.disable == 1:
        make_button(button7)
    else:
        # Add button launch code here
        make_button(button7)

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
        butNo=kalipi.inputLoop("menu-9p.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    main(sys.argv[1:])
