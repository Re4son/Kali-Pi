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
        page=os.environ["MENUDIR"] + "menu-4.py"
        os.execvp("python", ["python", page])
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

                #ensure there is always a safe way to end the program if the touch screen fails
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)
            t = t - 0.1

            if t <= 0:
                break

        ## Screensaver
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        retPage="menu-9.py"
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

                #ensure there is always a safe way to end the program if the touch screen fails
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)


        ##        Input loop       ##
        #############################

if __name__ == "__main__":
    main(sys.argv[1:])
