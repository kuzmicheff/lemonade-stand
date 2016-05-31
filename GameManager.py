import time
import curses
import random

import MessagePrinter
import ModeSelector
import StandGenerator
import MoneyConverter
import AssetTracker
import WeatherCaster
import EventGenerator
import CustomerGenerator
import SalesCalculator
import WindowLoader


class GameManager:
    """The GameManager class enables the main game flow and uses all other classes."""

    def __init__(self):
        pass

    def launchGame(self):
        mainScreen = curses.initscr()
        mainScreen.nodelay(1)
        mainScreen.keypad(0)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        screenSize = mainScreen.getmaxyx()
        messagePrinter = MessagePrinter.MessagePrinter()
        messageContents = messagePrinter.displayMessage("files/messages/GameTitle.txt")
        capsLine = str.upper(messageContents)
        strippedLine = capsLine.strip()
        stringLength = len(strippedLine)
        halfString = int(round(stringLength / 2))
        mainScreen.addstr(int(round(screenSize[0] / 2)), int(round(screenSize[1] / 2 - halfString)), strippedLine)
        mainScreen.refresh()
        time.sleep(5)
        mainScreen.clear()
        curses.endwin()

    def launchMenu(self):
        mainScreen = curses.initscr()
        mainScreen.nodelay(0)
        mainScreen.keypad(1)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        screenSize = mainScreen.getmaxyx()
        menuSelection = - 1
        menuOption = 0
        while menuSelection < 0:
            graphics = [0] * 5
            graphics[menuOption] = curses.A_REVERSE
            messagePrinter = MessagePrinter.MessagePrinter()
            messageContents = messagePrinter.displayMessage("files/messages/GameMenu.txt")
            capsLine = str.upper(messageContents)
            paragraphLines = capsLine.split(",")
            lineCounter = int(round(screenSize[0] / 2 - 4))
            i = 0
            for paragraphLine in paragraphLines:
                strippedLine = paragraphLine.strip()
                stringLength = len(strippedLine)
                halfString = int(round(stringLength / 2))
                if paragraphLine == "GAME MENU":
                    mainScreen.addstr(lineCounter - 4, int(round(screenSize[1] / 2 - halfString)), strippedLine)
                else:
                    mainScreen.addstr(lineCounter, int(round(screenSize[1] / 2 - halfString)), strippedLine, graphics[i])
                    lineCounter += 2
                    i += 1
            mainScreen.addstr(screenSize[0] - 1, int(round(screenSize[1] / 2 - 15)), "SELECT OPTION AND PRESS RETURN")

            action = mainScreen.getch()
            if action == curses.KEY_UP:
                menuOption = (menuOption - 1) % 4
            elif action == curses.KEY_DOWN:
                menuOption = (menuOption + 1) % 4
            elif action == 10:
                menuSelection = menuOption

        mainScreen.clear()
        curses.endwin()
        #
        # def launchMenu(self):
        #     windowLoader = WindowLoader.WindowLoader()
        #     messagePrinter = MessagePrinter.MessagePrinter()
        #
        #     gameMenu = messagePrinter.displayMessage("files/messages/GameMenu.txt")
        #     windowType = 1
        #     gameMenuWindow = windowLoader.loadGameWindow(gameMenu, windowType)

        # windowLoader = WindowLoader.WindowLoader()
        # messagePrinter = MessagePrinter.MessagePrinter()
        #
        # gameIntro = messagePrinter.displayMessage("files/messages/GameIntro.txt")
        # gameIntroWindow = windowLoader.loadGameWindow(gameIntro)
        # modeTitle = messagePrinter.displayMessage("files/messages/ModeTitle.txt")
        # modeTitleWindow = windowLoader.loadGameWindow(modeTitle)
        # modeInput = messagePrinter.displayMessage("files/messages/ModeInput.txt")
        # modeInputWindow = windowLoader.loadGameWindow(modeInput)
        # modeChoice = input(modeInput)
        # modeSelector = ModeSelector.ModeSelector()
        # selectedMode = modeSelector.selectMode(modeChoice)
        # selectedModeWindow = windowLoader.loadGameWindow(selectedMode)
        #
        # countTitle = messagePrinter.displayMessage("files/messages/CountTitle.txt")
        # countTitleWindow = windowLoader.loadGameWindow(countTitle)
        #
        # countInput = messagePrinter.displayMessage("files/messages/CountInput.txt")
        # countChoice = input(countInput)
        # countInputWindow = windowLoader.loadGameWindow("USER SELECTED: " + countChoice)

        # standGenerator = StandGenerator.StandGenerator()
        # standList = standGenerator.assignStands(countChoice)
        #
        # moneyConverter = MoneyConverter.MoneyConverter()
        # startAssets = moneyConverter.displayTwoDecimals(2)
        # currentAssets = startAssets
        # # Check the appearance of sums of decimals.
        # print(currentAssets + startAssets)
        #
        # assetList = []
        # for standIndex in range(len(standList)):
        #     print(standIndex)
        #     assetList.append(currentAssets)
        # print(assetList)
        #
        # # Check the appearance of individual values in assetList.
        # for i in assetList:
        #     print(i)
        #
        # rulesScreen1 = messagePrinter.displayMessage("files/messages/RulesScreen1.txt")
        # print(rulesScreen1)
        #
        # rulesScreen2 = messagePrinter.displayMessage("files/messages/RulesScreen2.txt")
        # print(rulesScreen2)
        #
        # weatherCaster = WeatherCaster.WeatherCaster()
        # dayWeather = weatherCaster.generateDayWeather()
        # print("Today's weather: " + dayWeather)
        #
        # eventGenerator = EventGenerator.EventGenerator()
        # eventList, dayEventList, dayEvent = eventGenerator.generateDayEvent(dayWeather)
        # alertItem = eventGenerator.postAlertMessage(dayWeather, eventList, dayEventList)
        # print(dayEventList)
        # print("Special event: " + dayEvent)
        # print(alertItem)
        #
        # dayGlasses = random.choice(range(5, 20))
        # dayCost = random.choice(range(1, 10)) / 100
        # dayCost = moneyConverter.displayTwoDecimals(dayCost)
        # dayAds = random.choice(range(3))
        # dayPrice = random.choice(range(10, 30)) / 100
        # dayPrice = moneyConverter.displayTwoDecimals(dayPrice)
        # print(dayGlasses, dayCost, dayAds, dayPrice)
        # print("Ads purchased: " + str(dayAds))
        # customerGenerator = CustomerGenerator.CustomerGenerator()
        # dayCustomers = customerGenerator.generateDayCustomers(dayWeather, alertItem, dayAds)
        # print("Number of customers: " + str(dayCustomers))
        # print(type(dayCustomers))
        #
        # assetTracker = AssetTracker.AssetTracker()
        # customerAssets = assetTracker.generateCustomerAssets(dayCustomers)
        #
        # salesCalculator = SalesCalculator.SalesCalculator()
        # daySales = salesCalculator.calculateDailySales(assetList, dayGlasses, dayCost, dayAds, dayPrice, dayWeather, customerAssets, dayEvent)
        # print(daySales)
        # print(type(daySales))
