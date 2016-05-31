import random
import MoneyConverter


class AssetTracker:
    """The AssetTracker class stores current player assets and generates customer assets."""

    def __init__(self):
        pass

    # def updatePlayerAssets(self, assetList):
    #     currentAssetList = []
    #     for updatedAmount in assetList:
    #         currentAssetList.append(updatedAmount)
    #     print(currentAssetList)


    def generateCustomerAssets(self, dayCustomers):
        print(dayCustomers)

        customerAssets = []
        for customerNumber in range(dayCustomers):
            randomAmount = random.choice(range(10, 500)) / 100
            moneyConverter = MoneyConverter.MoneyConverter()
            convertedAmount = moneyConverter.displayTwoDecimals(randomAmount)
            customerAssets.append(convertedAmount)
        return customerAssets
