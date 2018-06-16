#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
##  Kismet version         ##
if "KISMETVER" in os.environ and os.environ["KISMETVER"] == "2":
    kismetver = 2
else:
    kismetver = 1


#############################
##    Local Functions      ##

# Toggle Kismet
def toggle_kismet():
    check = "/bin/systemctl status kismet"
    start = "/bin/systemctl start kismet"
    stop = "/bin/systemctl stop kismet"
    status = run_cmd(check)
    if ("is running" in status) or ("active (running)") in status:
        run_cmd(stop)
        return False
    else:
	run_cmd(start)
        return True

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


# Check msf session status
def check_msf():
    if 'SCREEN -R -S msf' in commands.getoutput('/bin/ps -ef'):
        return True
    else:
        return False

# Check kismet session status
def check_kismet():
    if 'SCREEN -R -S kismet' in commands.getoutput('/bin/ps -ef'):
        return True
    else:
        return False


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                        Misc Tools", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_blu, tron_ora, titleFont)
button1 = Button(labelPadding * " " + "  Metasploit", originX, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button2 = Button(labelPadding * " " + "  SDR-Scan", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button3 = Button(labelPadding * " " + "     Kismet", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button4 = Button(labelPadding * " " + "    OpenVAS", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button5 = Button(labelPadding * " " + "      Snort", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button6 = Button(labelPadding * " " + "  PulledPork", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button7 = Button(labelPadding * " " + "        <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button8 = Button(labelPadding * " " + " Screen Off", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)
button9 = Button(labelPadding * " " + "        >>>", originX + (buttonWidth * 2) + (spacing * 2), originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, tron_blu, tron_whi, labelFont)


# Define each button press action
def button(number):

    if number == 1:
        if button1.disable == 1:
            return

	# Metasploit
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        pygame.quit()
        kalipi.run_cmd("/usr/bin/sudo -u " + KPUSER + " screen -R -S msf msfconsole")
        process = subprocess.call("setterm -term linux -back default -fore black -clear all", shell=True)
        os.execv(__file__, sys.argv)

        if check_msf():
                button1.fntColor = green
                button1.draw()
                pygame.display.update()

        else:
                button1.fntColor = tron_whi
                button1.draw()
                pygame.display.update()
        return


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
        if kismetver == 1:
            process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
            pygame.quit()
            kalipi.run_cmd("/usr/bin/sudo -u " + KPUSER + " screen -R -S kismet /usr/bin/kismet")
            process = subprocess.call("setterm -term linux -back default -fore black -clear all", shell=True)
            os.execv(__file__, sys.argv)

            if check_kismet():
                    button3.fntColor = green
                    button3.draw()
                    pygame.display.update()

            else:
                    button3.fntColor = tron_whi
                    button3.draw()
                    pygame.display.update()
            return
        else: # Kismet github version
            if toggle_kismet():
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

	# OpenVAS
        if toggle_openvas():
                button4.fntColor = green
                button4.draw()
                pygame.display.update()

        else:
                button4.fntColor = tron_whi
                button4.draw()
                pygame.display.update()
        return

    if number == 5:
        if button5.disable == 1:
            return

        # Snort
        if toggle_snort():
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
        retPage="menu-3.py"
        kalipi.screensaver(retPage)
        menu3()

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


def menu3():

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
        if check_msf():
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
        button2.draw()

    # Button 3
    button3.disable = 0  # "1" disables button

    if button3.disable == 1:
        button3.draw()
    else:
        # Add button launch code here
        if kismetver == 1:
            if check_kismet():
                button3.fntColor = green
                button3.draw()
            else:
                button3.fntColor = tron_whi
                button3.draw()
        else:
            if check_service("kismet"):
                button3.fntColor = green
                button3.draw()
            else:
                button3.fntColor = tron_whi
                button3.draw()

    # Second Row
    # Button 4
    button4.disable = 1  # "1" disables button

    if button4.disable == 1:
        button4.draw()
    else:
        # Add button launch code here
        if check_service("openvas-manager"):
            button4.fntColor = green
            button4.draw()
        else:
            button4.fntColor = tron_whi
            button4.draw()

    # Button 5
    button5.disable = 1  # "1" disables button

    if button5.disable == 1:
        button5.draw()
    else:
        # Add button launch code here
        if check_service("snortbarn"):
            button5.fntColor = green
            button5.draw()
        else:
            button5.fntColor = tron_whi
            button5.draw()

    # Button 6
    button6.disable = 1  # "1" disables button

    if button6.disable == 1:
        button6.draw()
    else:
        # Add button launch code here
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
        butNo=kalipi.inputLoop("menu-3.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    menu3()
