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

# Toggle OpenVAS
def toggle_openvas():
    check = "/usr/sbin/service openvas-manager status"
    start = "/usr/bin/openvas-start"
    stop = "/usr/bin/openvas-stop"
    status = run_cmd(check)
    if ("is running" in status) or ("active (running)") in status:
        run_cmd(stop)
        return False
    else:
	run_cmd(start)
        return True

# Toggle snort
def toggle_snort():
    try:
        status = run_cmd("/usr/sbin/service snortbarn status")
        if ("is running" in status) or ("active (running)") in status:
            run_cmd("/usr/sbin/service snortbarn stop")
            return False
        else:
            run_cmd("/usr/sbin/service mysql start")
            run_cmd("/usr/sbin/service snortbarn start")
            return True
    except:
        return False


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                        Misc Tools", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, titleFont)
button1 = Button(labelPadding * " " + "  Metasploit", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button(labelPadding * " " + "  SDR-Scan", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button(labelPadding * " " + "     Kismet", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_light, labelFont)
button4 = Button(labelPadding * " " + "    OpenVAS", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button(labelPadding * " " + "      Snort", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button(labelPadding * " " + "  PulledPork", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button(labelPadding * " " + "        <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button(labelPadding * " " + " Screen Off ", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
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

	# Metasploit
        pygame.quit()
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        call("/usr/bin/msfconsole", shell=True)
        process = subprocess.call("setterm -term linux -back default -fore black -clear all", shell=True)
        os.execv(__file__, sys.argv)

    if number == 2:
        if button2.disable == 1:
            return

        # SDR-Scanner
        pygame.quit()
        prog="/bin/bash " + os.environ["MENUDIR"] + "/SDR-Scanner/sdr-scanner.sh"
        kalipi.run_cmd(prog)
        os.execv(__file__, sys.argv)

    if number == 3:
        if button3.disable == 1:
            return

        # Kismet
        pygame.quit()
        subprocess.call("/usr/bin/sudo -u pi /usr/bin/kismet", shell=True)
        os.execv(__file__, sys.argv)

    if number == 4:
        if button4.disable == 1:
            return

	# OpenVAS
        if toggle_openvas():
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

        # Snort
        if toggle_snort():
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

        # Pulledpork
	pygame.quit()
	cmd="/usr/bin/sudo /bin/bash " + os.environ["MENUDIR"] + "pulledpork.sh"
	call(cmd, shell=True)
        os.execv(__file__, sys.argv)

    if number == 7:
        if button7.disable == 1:
            return

        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-2.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
        if button8.disable == 1:
            return

        # Screen off
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        retPage="menu-3.py"
        args = [page, retPage]
        os.execvp("python", ["python"] + args)
        sys.exit()

    if number == 9:
        if button9.disable == 1:
            return

        # Next page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-4.py"
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
    button4.disable = 1  # "1" disables button

    if button4.disable == 1:
        make_button(button4)
    else:
        # Add button launch code here
        if check_service("openvas-manager"):
            button4.color = green
            make_button(button4)
        else:
            button4.color = tron_light
            make_button(button4)

    # Button 5
    button5.disable = 1  # "1" disables button

    if button5.disable == 1:
        make_button(button5)
    else:
        # Add button launch code here
        if check_service("snortbarn"):
            button5.color = green
            make_button(button5)
        else:
            button5.color = tron_light
            make_button(button5)

    # Button 6
    button6.disable = 1  # "1" disables button

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
