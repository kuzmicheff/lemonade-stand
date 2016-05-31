import curses
import textwrap
import time


class WindowLoader:
    """The WindowLoader class renders all windows in the game."""

    def __init__(self):
        pass

    def loadGameWindow(self, messageContents, windowType):
        mainScreen = curses.initscr()
        screenSize = mainScreen.getmaxyx()

        # dimensional variables for windows
        windowHeight = screenSize[0]
        windowWidth = 40
        stringLength = windowWidth
        verTopPosition = 0
        verMidPosition = int(round(screenSize[0] / 2))
        verBottomPosition = windowHeight
        horLeftPosition = 0
        horMidPosition = int(round(screenSize[1] / 2 - 20))
        horRightPosition = windowWidth

        # properly initialiaze screen
        # user input will be hidden from the screen
        curses.noecho()
        # allow character break
        curses.cbreak()
        # make cursor invisible
        curses.curs_set(0)
        # enable multi-byte sequences
        mainScreen.keypad(1)

        if windowType == 0:
            # open static window and display it for five seconds
            gameWindow = curses.newwin(windowHeight, windowWidth, verTopPosition, horMidPosition)
            textWindow = gameWindow.subwin(windowHeight, windowWidth, verTopPosition, horMidPosition)
            capsLine = str.upper(messageContents)
            stringLength = len(capsLine)
            halfString = int(round(stringLength / 2))
            textWindow.addstr(verMidPosition, horMidPosition - halfString, capsLine)

            # update internal window structures
            mainScreen.noutrefresh()
            gameWindow.noutrefresh()
            # redraw the screen
            curses.doupdate()

            # testing .nodelay with timeout
            gameWindow.nodelay(1)
            time.sleep(5)

            # take user input to exit game window
            # exitWindow = gameWindow.getch()
            # textWindow.clear()

            # refresh windows from bottom up
            mainScreen.noutrefresh()
            gameWindow.noutrefresh()
            textWindow.noutrefresh()
            curses.doupdate()

            # take user input to exit main screen
            # exitScreen = mainScreen.getch()

            # restore terminal settings
            curses.echo()
            curses.nocbreak()
            curses.curs_set(1)
            mainScreen.keypad(0)
            curses.endwin()

        elif windowType == 1:
            # open game window
            gameWindow = curses.newwin(windowHeight, windowWidth, verTopPosition, horMidPosition)
            textWindow = gameWindow.subwin(windowHeight, windowWidth, verTopPosition, horMidPosition)

            # render game menu
            textWindow.nodelay(0)
            textWindow.keypad(1)
            selection = - 1
            option = 0
            while selection < 0:
                graphics = [0] * 5
                graphics[option] = curses.A_REVERSE

                capsLine = str.upper(messageContents)
                paragraphLines = capsLine.split(",")
                lineCounter = verMidPosition - 4
                i = 0
                for paragraphLine in paragraphLines:
                    strippedLine = paragraphLine.strip()
                    stringLength = len(strippedLine)
                    halfString = int(round(stringLength / 2))
                    if paragraphLine == "GAME MENU":
                        textWindow.addstr(verTopPosition + 2, horMidPosition - halfString, strippedLine)
                    else:
                        textWindow.addstr(lineCounter, horMidPosition - halfString, strippedLine, graphics[i])
                        lineCounter += 2
                        i += 1

                # update internal window structures
                mainScreen.noutrefresh()
                gameWindow.noutrefresh()
                # redraw the screen
                curses.doupdate()

                # take user input to navigate menu
                action = textWindow.getch()
                if action == curses.KEY_UP:
                    option = (option - 1) % 4
                elif action == curses.KEY_DOWN:
                    option = (option + 1) % 4
                elif action == 10:
                    selection = option

                # refresh windows from bottom up
                mainScreen.noutrefresh()
                gameWindow.noutrefresh()
                textWindow.noutrefresh()
                curses.doupdate()

            # take user input to exit main screen
            # exitScreen = mainScreen.getch()

            # restore terminal settings
            curses.echo()
            curses.nocbreak()
            curses.curs_set(1)
            mainScreen.keypad(0)
            curses.endwin()

        # # add title and menu strings
        # mainScreen.addstr(verTopPosition, horMidPosition, "LEMONADE STAND: BUSINESS SIMULATION GAME")
        # mainScreen.addstr(verBottomPosition, horMidPosition, "PRESS RETURN TO CONTINUE OR ESC TO QUIT")
        #
        # openWindow = 0
        # while openWindow != 27:
        #     openWindow = mainScreen.getch()
        # # open game window
        # gameWindow = curses.newwin(10, 42, verTopPosition + 1, horMidPosition - 1)
        # textWindow = gameWindow.subwin(8, 40, verTopPosition + 2, horMidPosition)
        # introFile = open("files/messages/GameIntro.txt", "r", encoding="utf-8")
        # textLine = introFile.read()
        # introFile.close()
        # capsLine = str.upper(textLine)
        # # textWindow.addstr(capsLine)
        # paragraphLines = textwrap.wrap(capsLine, 40)
        # lineCounter = 0
        # for paragraphLine in paragraphLines:
        #     textWindow.addstr(lineCounter, 0, paragraphLine)
        #     lineCounter += 1
        # gameWindow.box()
        #
        # # update internal window structures
        # mainScreen.noutrefresh()
        # gameWindow.noutrefresh()
        # # redraw the screen
        # curses.doupdate()
        #
        # # testing .nodelay with timeout
        # gameWindow.nodelay(1)
        # time.sleep(5)
        #
        # # take user input to exit game window
        # exitWindow = gameWindow.getch()
        # textWindow.clear()
        #
        # # refresh windows from bottom up
        # mainScreen.noutrefresh()
        # gameWindow.noutrefresh()
        # textWindow.noutrefresh()
        # curses.doupdate()
        #
        # # take user input to exit main screen
        # exitScreen = mainScreen.getch()
        #
        # # restore terminal settings
        # curses.echo()
        # curses.nocbreak()
        # curses.curs_set(1)
        # mainScreen.keypad(0)
        # curses.endwin()