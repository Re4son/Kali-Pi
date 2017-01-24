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

# Outer Border
pygame.draw.rect(screen, tron_light, (0,0,screen_x,screen_y),10)

## Global display settings ##
#############################

#############################
##    Local Functions      ##


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("           System Services", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, titleFont)
button1 = Button(labelPadding * " " + "     WWW", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button(labelPadding * " " + "      FTP", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button(labelPadding * " " + "      SMB", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_light, labelFont)
button4 = Button(labelPadding * " " + "    Kismet", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button(labelPadding * " " + "SDR-Scanner", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button(labelPadding * " " + "  Metasploit", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button(labelPadding * " " + "      <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button(labelPadding * " " + "  Bluetooth", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button9 = Button(labelPadding * " " + "      >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)


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
	# WWW
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
        # FTP
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
        # SMB
        if kalipi.toggle_service("smbd"):
                button5.color = green
                make_button(button5)
                pygame.display.update()

        else:
                button5.color = tron_light
                make_button(button5)
                pygame.display.update()
        return

    if number == 4:
	# Kismet
        pygame.quit()
        subprocess.call("/usr/bin/sudo -u pi /usr/bin/kismet", shell=True)
        os.execv(__file__, sys.argv)

    if number == 5:
        # SDR-Scanner
        pygame.quit()
        prog="/bin/bash " + os.environ["MENUDIR"] + "sdr-scanner.sh"
        run_cmd(prog)
        os.execv(__file__, sys.argv)

    if number == 6:
        # Metasploit
        pygame.quit()
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        call("/usr/bin/msfconsole", shell=True)
        process = subprocess.call("setterm -term linux -back default -fore black -clear all", shell=True)
        os.execv(__file__, sys.argv)

    if number == 7:
        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-1.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
	# Bluetooth
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
make_button(button1)

# Button 2
make_button(button2)

# Button 3
make_button(button3)


# Second Row
# Button 4
make_button(button4)

# Button 5
make_button(button5)

# Button 6
make_button(button6)


# Third Row
# Button 7
make_button(button7)

# Button 8
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
