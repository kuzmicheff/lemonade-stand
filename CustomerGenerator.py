import random


class CustomerGenerator:
    """The CustomerGenerator class generates customers for the day based on the weather and alerts."""

    def __init__(self):
        pass

    def generateDayCustomers(self, dayWeather, alertItem, dayAds):
        if dayWeather == "Cloudy":
            minCustomers = 10
            maxCustomers = 80
        elif dayWeather == "Sunny":
            minCustomers = 20
            maxCustomers = 160
        else:
            minCustomers = 40
            maxCustomers = 320
        if alertItem == 0:
            maxCustomers /= 2
        elif alertItem == 1:
            maxCustomers /= 1.5
        elif alertItem == 2:
            maxCustomers *= 2
        if dayAds == 1:
            minCustomers *= 1.25
        elif dayAds == 2:
            minCustomers *= 1.75
        elif dayAds == 3:
            minCustomers *= 2.75
        minCustomers = int(round(minCustomers))
        maxCustomers = int(round(maxCustomers))
        customerList = range(minCustomers, maxCustomers)
        dayCustomers = random.choice(customerList)
        return dayCustomers
