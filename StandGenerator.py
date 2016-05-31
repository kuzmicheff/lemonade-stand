class StandGenerator:
    """The StandGenerator class takes the number of players and returns a list with stand identifiers."""

    def __init__(self):
        pass

    def assignStands(self, countChoice):
        standCount = int(countChoice)
        print(type(standCount))
        standIdList = []
        print(type(standIdList))
        if standCount > 1:
            for standNumber in range(standCount):
                 standId = "Stand " + str(standNumber + 1)
                 standIdList.append(standId)
        else:
            standIdList.append("Stand 1")
        return standIdList
