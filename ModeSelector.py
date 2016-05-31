class ModeSelector:
    """The ModeSelector class enables the player to choose whether to play a new game or load an existing game."""

    def __init__(self):
        pass

    def selectMode(self, modeChoice):
        # I will need to code restrictions on inputs from user with help of the curses module.
        ModeChoice = modeChoice.lower()
        print(ModeChoice)
        if ModeChoice.startswith("yes"):
            selectedMode = "new game"
            return selectedMode
        else:
            selectedMode = "saved game"
            return selectedMode
