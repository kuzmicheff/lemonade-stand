import random
import MoneyConverter


class SalesCalculator:
    """The SalesCalculator class performs calculations of daily sales for each player."""

    def __init__(self):
        pass

    def calculateDailySales(self, assetList, dayGlasses, dayCost, dayAds, dayPrice, dayWeather, customerAssets, dayEvent):
        moneyConverter = MoneyConverter.MoneyConverter()
        daySales = moneyConverter.displayTwoDecimals(0)
        adCost = moneyConverter.displayTwoDecimals(0.15)
        salesCounter = 0
        totalCost = dayGlasses * dayCost + dayAds * adCost
        print(totalCost)
        print(type(totalCost))
        likelyBuyers = []
        lemonadeBuyers = []
        saleModifiers = ["Thunderstorm", "Robbery", "Ice melt"]
        if dayEvent not in saleModifiers:

            for customerAmount in customerAssets:
                if customerAmount / 2 > dayPrice:
                    likelyBuyers.append(customerAmount)
            print(len(likelyBuyers))

            for customerAmount in likelyBuyers:
                if dayWeather == "Cloudy":
                    decisionList = ["Yes", "No", "No", "No"]
                    purchaseDecision = random.choice(decisionList)
                    if purchaseDecision == "Yes" and dayGlasses > 0:
                        daySales += dayPrice
                        customerAmount -= dayPrice
                        dayGlasses -= 1
                        salesCounter += 1
                        lemonadeBuyers.append(customerAmount)
                elif dayWeather == "Sunny":
                    decisionList = "Yes", "No", "No"
                    purchaseDecision = random.choice(decisionList)
                    if purchaseDecision == "Yes" and dayGlasses > 0:
                        daySales += dayPrice
                        customerAmount -= dayPrice
                        dayGlasses -= 1
                        salesCounter += 1
                        lemonadeBuyers.append(customerAmount)
                else:
                    decisionList =["Yes", "No"]
                    purchaseDecision = random.choice(decisionList)
                    if purchaseDecision == "Yes" and dayGlasses > 0:
                        daySales += dayPrice
                        customerAmount -= dayPrice
                        dayGlasses -= 1
                        salesCounter += 1
                        lemonadeBuyers.append(customerAmount)

        else:
            print("Special event has taken place! It nicked all your sales for today!")
        print(salesCounter)
        return daySales
