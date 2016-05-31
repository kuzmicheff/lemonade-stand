import curses
import textwrap
import time


mainScreen = curses.initscr()
screenSize = mainScreen.getmaxyx()

# dimensional variables for main screen
verTopPosition = 0
verMidPosition = int(round(screenSize[0] / 2))
verBottomPosition = int(round(screenSize[0] - 1))
horLeftPosition = 0
horMidPosition = int(round(screenSize[1] / 2 - 20))
horRightPosition = int(round(screenSize[1] - 1))

# properly initialiaze screen
# user input will be hidden from the screen
curses.noecho()
# allow character break
curses.cbreak()
# make cursor invisible
curses.curs_set(0)
# enable multi-byte sequences
mainScreen.keypad(1)

# add title and menu strings
mainScreen.addstr(verTopPosition, horMidPosition, "LEMONADE STAND: BUSINESS SIMULATION GAME")
mainScreen.addstr(verBottomPosition, horMidPosition, "PRESS RETURN TO CONTINUE OR ESC TO QUIT")

openWindow = 0
while openWindow != 27:
    openWindow = mainScreen.getch()
# open game window
gameWindow = curses.newwin(10, 42, verTopPosition + 1, horMidPosition - 1)
textWindow = gameWindow.subwin(8, 40, verTopPosition + 2, horMidPosition)
introFile = open("files/messages/GameIntro.txt", "r", encoding="utf-8")
textLine = introFile.read()
introFile.close()
capsLine = str.upper(textLine)
# textWindow.addstr(capsLine)
paragraphLines = textwrap.wrap(capsLine, 40)
lineCounter = 0
for paragraphLine in paragraphLines:
    textWindow.addstr(lineCounter, 0, paragraphLine)
    lineCounter += 1
gameWindow.box()

# update internal window structures
mainScreen.noutrefresh()
gameWindow.noutrefresh()
# redraw the screen
curses.doupdate()

# testing .nodelay with timeout
gameWindow.nodelay(1)
time.sleep(5)

# take user input to exit game window
exitWindow = gameWindow.getch()
textWindow.clear()

# refresh windows from bottom up
mainScreen.noutrefresh()
gameWindow.noutrefresh()
textWindow.noutrefresh()
curses.doupdate()

# take user input to exit main screen
exitScreen = mainScreen.getch()

# restore terminal settings
curses.echo()
curses.nocbreak()
curses.curs_set(1)
mainScreen.keypad(0)
curses.endwin()

# test version of WindowLoader

# def loadGameWindow(self, messageContents):
#     stdscr = curses.initscr()
#     curses.noecho()
#     curses.cbreak()
#     curses.curs_set(0)
#     # Check for and turn on color support
#     # if curses.has_colors():
#     #     curses.start_color()
#     #     # Initialize the color combinations we're going to use
#     #     curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
#     #     curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
#     #     curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
#     # Optionally enable the multi-byte sequences such as F1, F2, etc.
#     # stdscr.keypad(1)
#
#     # Begin program
#     screenDimensions = stdscr.getmaxyx()
#     # stdscr.chgat(20, curses.A_REVERSE)
#     if len(messageContents) > 40:
#         messageLines = textwrap.wrap(messageContents, screenDimensions[1] - 40)
#         lineCounter = 0
#         for messageLine in messageLines:
#             stdscr.addstr(1 + lineCounter, int(round(screenDimensions[1] / 2 - 20)), messageLine)
#             lineCounter += 2
#     else:
#         stdscr.addstr(1, int(round(screenDimensions[1] / 2 - 20)), messageContents)
#
#     # stdscr.chgat(-1, curses.A_REVERSE)
#     # Get current screen dimensions; curses.LINES and curses.COLS do not work
#     # stdscr.chgat(screenDimensions[0] - 1, 0, 20, curses.A_REVERSE)
#     stdscr.addstr(screenDimensions[0] - 2, int(round(screenDimensions[1] / 2 - 20)),
#                   "Press Return to continue or Esc to quit", curses.A_BLINK)
#     # stdscr.chgat(-1, curses.A_REVERSE)
#
#     # # Change the r to green
#     # stdscr.chgat(screenDimensions[0] - 1, 26, 1, curses.A_BOLD | curses.color_pair(2))
#     # # Change the q to red
#     # stdscr.chgat(screenDimensions[0] - 1, 54, 1, curses.A_BOLD | curses.color_pair(1))
#
#     # # Set up the window to hold the random quotes
#     # gameWindow = curses.newwin(screenDimensions[0] - 2, screenDimensions[1] - 1, 1, 1)
#     # # Create a sub-window so as to cleanly display text without worrying about overwriting the quote window's borders
#     # textWindow = gameWindow.subwin(screenDimensions[0] - 2, screenDimensions[1] - 2, 1, 1)
#     # textWindow.addstr(1, 1, "Welcome to the awesomest version of Lemonade Stand ever!")
#     # # Draw a border around the main application window
#     # textWindow.box(124, 45)
#     #
#     # # Update the internal window data structures
#     # stdscr.noutrefresh()
#     # gameWindow.noutrefresh()
#     #
#     # # Redraw the screen
#     # curses.doupdate()
#     #
#     # # Create the event loop
#     # while True:
#     #     c = gameWindow.getch()
#     #     if c == ord("r") or c == ord("R"):
#     #         textWindow.clear()
#     #         textWindow.addstr("Loading...", curses.color_pair(3))
#     #         textWindow.refresh()
#     #         textWindow.clear()
#     #         textWindow.addstr("Something new goes in here!")
#     #     elif c == ord("q") or c == ord("Q"):
#     #         break
#     #
#     #     # Refresh the windows from the bottom up
#     #     stdscr.noutrefresh()
#     #     gameWindow.noutrefresh()
#     #     textWindow.noutrefresh()
#     #     curses.doupdate()
#
#     # Restore the terminal settings
#     userInput = 0
#     while userInput != ord("\n"):
#         userInput = stdscr.getch()
#     stdscr.clear()
#     curses.nocbreak()
#     # stdscr.keypad(0)
#     curses.echo()
#     curses.curs_set(1)
#     # Restore the terminal itself to its "former glory"
#     curses.endwin()
