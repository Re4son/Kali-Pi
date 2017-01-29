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

def check_mana():
    try:
        check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_get_state | grep 'ENABLE'"
        status = kalipi.run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

def check_mana_loud():
    try:
        check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_state | grep 'ENABLE'"
        status = kalipi.run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

def toggle_FireLamb():
    check = "/usr/sbin/service FireLamb-manager status"
    start = "/usr/bin/FireLamb-start"
    stop = "/usr/bin/FireLamb-stop"
    status = kalipi.run_cmd(check)
    if ("is running" in status) or ("active (running)") in status:
        kalipi.run_cmd(stop)
        return False
    else:
        kalipi.run_cmd(start)
        return True

##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                        EvilAP", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, titleFont)
button1 = Button(labelPadding * " " + "  AP Open", originX, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button2 = Button(labelPadding * " " + "  AP Secure", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_light, labelFont)
button3 = Button(labelPadding * " " + "       Mana", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_light, labelFont)
button4 = Button(labelPadding * " " + "       Beef", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button5 = Button(labelPadding * " " + "   Firelamb", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button6 = Button(labelPadding * " " + "  Mana Loud", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_light, labelFont)
button7 = Button(labelPadding * " " + "      <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button8 = Button(labelPadding * " " + "  DNS2Proxy", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)
button9 = Button(labelPadding * " " + "      >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_light, labelFont)


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

        # Hostapd Open
        script=os.environ["MENUDIR"] + "/mana/manaSimple.sh"
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

        # Hostapd Secure
        script=os.environ["MENUDIR"] + "/mana/manaSecure.sh"

        if kalipi.toggle_script(script):
        # Stop Service
                button2.color = green
                make_button(button2)
                pygame.display.update()
        else:
        #Start Service
                button2.color = tron_light
                make_button(button2)
                pygame.display.update()

    if number == 3:
        if button3.disable == 1:
            return

        #Mana Attack
        if check_mana():
        # Stop Mana
                kalipi.run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_disable")
                button3.color = tron_light
                make_button(button3)
                pygame.display.update()
        else:
        # Start Mana
                run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_enable")
                button3.color = green
                make_button(button3)
                pygame.display.update()

    if number == 4:
        if button4.disable == 1:
            return

        # Beef
        if kalipi.toggle_service("beef-xss"):
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

        # FireLamb
        if toggle_FireLamb():
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

        #Mana Loud Attack
        if check_mana_loud():
        #Stop Mana
                kalipi.run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_off")
                button6.color = tron_light
                make_button(button6)
                pygame.display.update()
        else:
        #Start Mana Loud Attack
                kalipi.run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_on")
                button6.color = green
                make_button(button6)
                pygame.display.update()

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

                #DNS2Proxy
        if kalipi.toggle_script("/root/Desktop/Scripts/dns2proxy.sh"):
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
    button1.disable = 1  # "1" disables button

    if button1.disable == 1:
        make_button(button1)
    else:
        # Add button launch code here
        if kalipi.check_process("hostapd", "mana.conf"):
            button1.color = green
            make_button(button1)
        else:
            button1.color = tron_light
            make_button(button1)

    # Button 2
    button2.disable = 1  # "1" disables button

    if button2.disable == 1:
        make_button(button2)
    else:
        # Add button launch code here
        if kalipi.check_process("hostapd", "wpa2.conf"):
            button2.color = green
            make_button(button2)
        else:
            button2.color = tron_light
            make_button(button2)

    # Button 3
    button3.disable = 1  # "1" disables button

    if button3.disable == 1:
        make_button(button3)
    else:
        # Add button launch code here
        if check_mana():
            button3.color = green
            make_button(button3)
        else:
            button3.color = tron_light
            make_button(button3)

    # Second Row
    # Button 4
    button4.disable = 1  # "1" disables button

    if button4.disable == 1:
        make_button(button4)
    else:
        # Add button launch code here
        if kalipi.check_service("beef-xss"):
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
        if kalipi.check_service("FireLamb-manager"):
            button5.color = green
            make_button(button5)
        else:
            button5.color = red
            make_button(button5)

    # Button 6
    button6.disable = 1  # "1" disables button

    if button6.disable == 1:
        make_button(button6)
    else:
        # Add button launch code here
        if check_mana_loud():
            button6.color = green
            make_button(button6)
        else:
            button6.color = tron_light
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
    button8.disable = 1  # "1" disables button

    if button8.disable == 1:
        make_button(button8)
    else:
        # Add button launch code here
        if check_process("python", "dns2proxy.py"):
            button8.color = green
            make_button(button8)
        else:
            button8.color = tron_light
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

                #Debug:
                #ensure there is always a safe way to end the program if the touch screen fails
                ##if event.type == KEYDOWN:
                ##    if event.key == K_ESCAPE:
                ##        sys.exit()

            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)
            t = t - 0.1

            if t <= 0:
                break

        ## Screensaver
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        retPage="menu-4.py"
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

                #Debug:
                #ensure there is always a safe way to end the program if the touch screen fails
                ##if event.type == KEYDOWN:
                ##    if event.key == K_ESCAPE:
                ##        sys.exit()

            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)


        ##        Input loop       ##
        #############################


if __name__ == "__main__":
    main(sys.argv[1:])
