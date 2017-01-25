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

# Toggle ntopng
def toggle_ntopng():
    try:
        check = "/usr/sbin/service ntopng status"
        status = run_cmd("/usr/sbin/service ntopng status")
        if ("is running" in status) or ("active (running)") in status:
            run_cmd("/usr/sbin/service ntopng stop")
            run_cmd("/usr/sbin/service redis stop")
            return False
        else:
            run_cmd("/usr/sbin/service redis start")
            run_cmd("/usr/sbin/service ntopng start")
            return True
    except:
        return False


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                   EvilAP", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, titleFont)
button1 = Button(labelPadding * " " + "     WWW", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button(labelPadding * " " + "      FTP", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button(labelPadding * " " + "      SQL", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_light, labelFont)
button4 = Button(labelPadding * " " + "     hTop", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button(labelPadding * " " + "  darkstat", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button(labelPadding * " " + "    ntopng", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button(labelPadding * " " + "      <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button(labelPadding * " " + " Screen Off ", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
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
        # SQL
        if kalipi.toggle_service("mysql"):
                button3.color = green
                make_button(button3)
                pygame.display.update()

        else:
                button3.color = tron_light
                make_button(button3)
                pygame.display.update()
        return

    if number == 4:
	# hTop
        pygame.quit()
        subprocess.call("/usr/bin/htop", shell=True)
        os.execv(__file__, sys.argv)

    if number == 5:
        # darkstat
        if kalipi.toggle_service("darkstat"):
                button5.color = green
                make_button(button5)
                pygame.display.update()

        else:
                button5.color = tron_light
                make_button(button5)
                pygame.display.update()
        return

    if number == 6:
        # ntopng
        if toggle_ntopng():
                button6.color = green
                make_button(button6)
                pygame.display.update()

        else:
                button6.color = tron_light
                make_button(button6)
                pygame.display.update()
        return

    if number == 7:
        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-3.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
        # Screen off
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 9:
        # Next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-9.py"
        os.execvp("python", ["python", page])
        sys.exit()


# Buttons and labels
# See variables at the top of the document to adjust the menu

# Title
make_button(titleButton)

# First Row
# Button 1
if check_service("apache2"):
    button1.color = green
    make_button(button1)
else:
    button1.color = tron_light
    make_button(button1)

# Button 2
if check_service("pure-ftpd"):
    button2.color = green
    make_button(button2)
else:
    button2.color = tron_light
    make_button(button2)

# Button 3
if check_service("mysql"):
    button3.color = green
    make_button(button3)
else:
    button3.color = tron_light
    make_button(button3)

# Second Row
# Button 4
make_button(button4)

# Button 5
if check_service("darkstat"):
    button5.color = green
    make_button(button5)
else:
    button5.color = tron_light
    make_button(button5)

# Button 6
if check_service("ntopng"):
    button6.color = green
    make_button(button6)
else:
    button6.color = tron_light
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
