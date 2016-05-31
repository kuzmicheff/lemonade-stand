import random


class EventGenerator:
    """The EventGenerator class sets the weather before each new day in the game."""

    def __init__(self):
        pass

    def generateDayEvent(self, dayWeather):
        if dayWeather == "Cloudy":
            eventList = ["Thunderstorm", "Shower", "Overcast", "None", "None", "None", "None", "None", "None", "None"]
        elif dayWeather == "Sunny":
            eventList = ["Robbery", "Road work", "Garage sale", "None", "None", "None", "None", "None", "None", "None"]
        else:
            eventList = ["Ice melt", "UV radiation", "Perfect day", "None", "None", "None", "None", "None", "None", "None"]
        dayEventList = []
        for randomEvent in range(10):
            randomEvent = random.choice(eventList)
            dayEventList.append(randomEvent)
        # print(dayEventList)
        dayEvent = random.choice(dayEventList)
        return eventList, dayEventList, dayEvent

    def postAlertMessage(self, dayWeather, eventList, dayEventList):
        countList = []
        maxCount = 1
        alertItem = 3
        dayAlert = None
        for eventItem in range(3):
            itemCount = dayEventList.count(eventList[eventItem])
            countTuple = (eventItem, itemCount)
            countList.append(countTuple)
            print(itemCount)
            if itemCount > maxCount:
                maxCount = itemCount
                alertItem = eventItem
        if maxCount > 1:
            if dayWeather == "Cloudy":
                if alertItem == 0:
                    dayAlert = "There is great chance of rain with a possibility of thunderstorm today!"
                elif alertItem == 1:
                    dayAlert = "There is good chance of rain today, but it's not raining yet."
                elif alertItem == 2:
                    dayAlert = "It doesn't look bad now, it is likely to stay nice and dry all day."
            elif dayWeather == "Sunny":
                if alertItem == 0:
                    dayAlert = "The crime has been reported close to your neighborhood. Be cautious!"
                elif alertItem == 1:
                    dayAlert = "The roadwork signs on your street might affect your sales today."
                elif alertItem == 2:
                    dayAlert = "Neighbors put up garage sale signs! Sales might be better than usual!"
            else:
                if alertItem == 0:
                    dayAlert = "Dangerous heatwave is on today's forecast! It might melt your ice!"
                elif alertItem == 1:
                    dayAlert = "High UV radiation levels are expected today. It might affect your sales."
                elif alertItem == 2:
                    dayAlert = "Seems as the perfect day to be outside. Great sales are possible!"
        else:
            dayAlert = "Local news aren't reporting anything special for your neighborhood."
        print(countList)
        print(alertItem, maxCount, dayAlert)
        return alertItem
