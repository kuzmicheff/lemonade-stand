import decimal


class MoneyConverter:
    """The MoneyConverter class enables the game currency and monetary transactions."""

    def __init__(self):
        pass

    def displayTwoDecimals(self, amount):
        decimalAmount = round(decimal.Decimal(amount), 2)
        return decimalAmount
