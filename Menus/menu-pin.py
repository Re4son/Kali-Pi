#!/usr/bin/env python
import kalipi, hashlib
from kalipi import *

#############################
##        Variables        ##
pin = ""
c = 0  # Character counter for PIN



# Overwrite dimensions

###########################
##  Screen layouts       ##

newOriginX = originX
newOriginY = originY
newSpacing = spacing
newButtonWidth = buttonWidth
newButtonHeight = buttonHeight / 4 * 3
newLabelFont = labelFont / 3 * 2
newLabelPadding = labelPadding
newTitleFont = titleFont / 3 * 2


##  Screen layouts       ##
###########################

# define all of the buttons
titleButton = Button("       Environmental Survey    -    Humidity Sensor    ", newOriginX, newOriginX, buttonHeight, buttonWidth * 3  + spacing * 2, tron_blu, tron_ora, newTitleFont)
button1 = Button(" " * 18 + "1", newOriginX, newOriginY, newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button2 = Button(" " * 18 + "2", newOriginX + newButtonWidth + newSpacing, newOriginY, newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button3 = Button(" " + " " * 18 + "3", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY, newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button4 = Button(" " + " " * 18 + "4", newOriginX, newOriginY + newButtonHeight + newSpacing, newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button5 = Button(" " + " " * 18 + "5", newOriginX + newButtonWidth + newSpacing, newOriginY + newButtonHeight + newSpacing, newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button6 = Button(" " + " " * 18 + "6", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY + newButtonHeight + newSpacing, newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button7 = Button(" " + " " * 18 + "7", newOriginX, newOriginY + (newButtonHeight * 2) + (newSpacing * 2), newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button8 = Button(" " + " " * 18 + "8", newOriginX + newButtonWidth + newSpacing, newOriginY + (newButtonHeight * 2) + (newSpacing * 2), newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button9 = Button(" " + " " * 18 + "9", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY + (newButtonHeight * 2) + (newSpacing * 2), newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
buttonc = Button(newLabelPadding * " " + "          CLEAR", newOriginX, newOriginY + (newButtonHeight * 3) + (newSpacing * 3), newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
button0 = Button(" " * 18 + "0", newOriginX + newButtonWidth + newSpacing, newOriginY + (newButtonHeight * 3) + (newSpacing * 3), newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)
buttone = Button(newLabelPadding * " " + "          ENTER", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY + (newButtonHeight * 3) + (newSpacing * 3), newButtonHeight, newButtonWidth, tron_blu, tron_whi, newLabelFont)


#############################
##    Local Functions      ##

def local_on_touch(posx=0, posy=0):
    # get the position that was touched
    if SCREEN==4:
        touch_pos = (posx, posy)
    else:
        touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # button 1 event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and newOriginY <= touch_pos[1] <= (newOriginY + newButtonHeight):
            return 1
    # button 2 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY <= touch_pos[1] <= (newOriginY + newButtonHeight):
            return 2
    # button 3 event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY <= touch_pos[1] <= (newOriginY + newButtonHeight):
            return 3
    # button 4 event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and (newOriginY + newButtonHeight + newSpacing) <= touch_pos[1] <= newOriginY + (newButtonHeight * 2) + newSpacing:
            return 4
    # button 5 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY + newButtonHeight + newSpacing <= touch_pos[1] <= newOriginY + (newButtonHeight * 2) + newSpacing:
            return 5
    # button 6 event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY + newButtonHeight + newSpacing <= touch_pos[1] <= newOriginY + (newButtonHeight * 2) + newSpacing:
            return 6
    # button 7 event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 3) + (newSpacing * 2):
            return 7
    # button 8 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 3) + (newSpacing * 2):
            return 8
        # button 9 event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 3) + (newSpacing * 2):
            return 9
    # button c event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and newOriginY + (newButtonHeight * 3) + (newSpacing * 3) <= touch_pos[1] <= newOriginY + (newButtonHeight * 4) + (newSpacing * 3):
            return "c"
    # button 0 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY + (newButtonHeight * 3) + (newSpacing * 3) <= touch_pos[1] <= newOriginY + (newButtonHeight * 4) + (newSpacing * 3):
            return 0
    # button e event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 4) + (newSpacing * 3):
            return "e"

def verifyPin():
    global pin, c

    if pin == "":
        retPage=kalipi.get_retPage()
        kalipi.screensaver(retPage)
        menuPin()
    elif pin == "111":
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-9p.py"
        retPage=kalipi.get_retPage()
        args = [page, retPage]
        os.execvp("python", ["python"] + args)
        sys.exit()
    elif pin == "110":
        pygame.quit()
        kalipi.run_cmd("/usr/bin/sudo /sbin/shutdown -h now")
        sys.exit()
    else:
        file = ".kalipi"
        pinFile=os.environ["MENUDIR"] + ".kalipi"
        file_conn = open(pinFile)
        file_pin = file_conn.readline()[:-1]
        file_conn.close()
        hashed_pin=hashlib.sha512(file + pin).hexdigest()
        if file_pin == hashed_pin:
            pygame.quit()
            launch_bg=os.environ["MENUDIR"] + "launch-bg.sh"
            process = subprocess.call(launch_bg, shell=True)
            retPage=kalipi.get_retPage()
            page=os.environ["MENUDIR"] + retPage
            args = [page]
            os.execvp("python", ["python"] + args)
            sys.exit()
        else:
           pin=""
           c = 0
           return
            ## Debug
##            process = subprocess.call("setterm -term linux -back black -fore white -clear all", shell=True)
##            pygame.quit()
##            print pin
##            sys.exit()


##    Local Functions      ##
#############################

# Define each button press action
def button(number):
    global pin, c

    if number == 1:
        if button1.disable == 1:
            return

        # 1
        pin=pin+"1"
        c = c + 1
        return

    if number == 2:
        if button2.disable == 1:
            return

	# 2
        pin=pin+"2"
        c = c + 1
        return

    if number == 3:
        if button3.disable == 1:
            return

        # 3
        pin=pin+"3"
        c = c + 1
        return

    if number == 4:
        if button4.disable == 1:
            return

        # 4
        pin=pin+"4"
        c = c + 1
        return

    if number == 5:
        if button5.disable == 1:
            return

	# 5
        pin=pin+"5"
        c = c + 1
	return

    if number == 6:
        if button6.disable == 1:
            return

	# 6
        pin=pin+"6"
        c = c + 1
        return

    if number == 7:
        if button7.disable == 1:
            return

        # 7
        pin=pin+"7"
        c  = c + 1
        return

    if number == 8:
        if button8.disable == 1:
            return

        # 8
        pin=pin+"8"
        c = c + 1
        return

    if number == 9:
        if button9.disable == 1:
            return

        # 9
        pin=pin+"9"
        c = c + 1
        return

    if number == "c":
        if buttonc.disable == 1:
            return

        # Clear
        pin = ""
        c = 0
        return
        ## Debug
##        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
##        pygame.quit()
##        sys.exit()

    if number == 0:
        if button9.disable == 1:
            return

        # 0
        pin=pin+"0"
        c = c + 1
        return

    if number == "e":
        if buttone.disable == 1:
            return

        # Enter
        verifyPin()
        return
        ## Debug
##        process = subprocess.call("setterm -term linux -back black -fore white -clear all", shell=True)
##        pygame.quit()
##        print pin
##        sys.exit()


def menuPin (argv):

    global c

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
        button3.draw()


    # Second Row
    # Button 4
    button4.disable = 0  # "1" disables button

    if button4.disable == 1:
        button4.draw()
    else:
        # Add button launch code here
        button4.draw()

    # Button 5
    button5.disable = 0  # "1" disables button

    if button5.disable == 1:
        button5.draw()
    else:
        # Add button launch code here
        button5.draw()

    # Button 6
    button6.disable = 0  # "1" disables button

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

    # Button c
    buttonc.disable = 0  # "1" disables button

    if buttonc.disable == 1:
        buttonc.draw()
    else:
        # Add button launch code here
        buttonc.draw()

    # Button 0
    button0.disable = 0  # "1" disables button

    if button0.disable == 1:
        button0.draw()
    else:
        # Add button launch code here
        button0.draw()

    # Button e
    buttone.disable = 0  # "1" disables button

    if buttone.disable == 1:
        buttone.draw()
    else:
        # Add button launch code here
        buttone.draw()

    ##        Buttons          ##
    #############################


    #############################
    ##        Input loop       ##


    if "KPTIMEOUT" in os.environ:
        timeout = float(os.environ["KPTIMEOUT"]) * 60 / 3 # Convert timeout to seconds

        #While loop to manage touch screen inputs
        t = timeout
        state = [False for x in range(10)]

        while True:
            if SCREEN==4:
                for touch in ts.poll():
                    if state[touch.slot] != touch.valid:
                        if touch.valid:
                            num = local_on_touch(touch.x, touch.y)
                            button(num)
                            if c > 0:
                                pygame.draw.rect(screen.canvas, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                                new_titleButton = Button("      " + c * "* ", newOriginX, newOriginX, buttonHeight, buttonWidth * 3  + spacing * 2, tron_blu, green, newTitleFont * 2)
                                new_titleButton.draw()
                                if c > 15:
                                    c = 0
                            else:
                                pygame.draw.rect(screen.canvas, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                                titleButton.draw()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        t = timeout
                        pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                        num = local_on_touch()
                        button(num)
                        if c > 0:
                            pygame.draw.rect(screen.canvas, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                            new_titleButton = Button("      " + c * "* ", newOriginX, newOriginX, buttonHeight, buttonWidth * 3  + spacing * 2, tron_blu, green, newTitleFont * 2)
                            new_titleButton.draw()
                            if c > 15:
                                c = 0
                        else:
                            pygame.draw.rect(screen.canvas, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                            titleButton.draw()

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
        retPage=kalipi.get_retPage()
        kalipi.screensaver(retPage)
        menuPin()


    else:

        #While loop to manage touch screen inputs
        state = [False for x in range(10)]
        while True:
            if SCREEN==4:
                for touch in ts.poll():
                    if state[touch.slot] != touch.valid:
                        if touch.valid:
                            num = local_on_touch(touch.x, touch.y)
                            button(num)
                            if c > 0:
                                pygame.draw.rect(screen.canvas, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                                new_titleButton = Button("      " + c * "* ", newOriginX, newOriginX, buttonHeight, buttonWidth * 3  + spacing * 2, tron_blu, green, newTitleFont * 2)
                                new_titleButton.draw()
                                if c > 15:
                                    c = 0
                            else:
                                pygame.draw.rect(screen.canvas, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                                titleButton.draw()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                        num = local_on_touch()
                        button(num)
                        if c > 0:
                            pygame.draw.rect(screen, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                            new_titleButton = Button("      " + c * "* ", newOriginX, newOriginX, buttonHeight, buttonWidth * 3  + spacing * 2, green, newTitleFont * 2)
                            new_titleButton.draw()
                            if c > 15:
                                c = 0
                        else:
                            pygame.draw.rect(screen, black, (newOriginX, newOriginX,buttonWidth * 3, buttonHeight),0)
                            make_button(titleButton)

               #Debug:
               #ensure there is always a safe way to end the program if the touch screen fails
               ## if event.type == KEYDOWN:
               ##     if event.key == K_ESCAPE:
               ##         sys.exit()

            pygame.display.update()

            ## Reduce CPU utilisation
            time.sleep(0.1)

    ##        Input loop       ##
    #############################


if __name__ == "__main__":
    menuPin(sys.argv[1:])
