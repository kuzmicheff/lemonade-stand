import datetime


class MessagePrinter:
    """The MessagePrinter class allows to display pre-formatted game messages on the screen."""

    def __init__(self):
        pass

    def displayMessage(self, fileName):
        try:
            messageFile = open(fileName, "r", encoding="utf-8")
            messageContents = messageFile.read()
            messageFile.close()
            return messageContents
        except:
            errorTimeStamp = "{:%b %d, %Y at %H:%M:%S}".format(datetime.datetime.now())
            errorContents = errorTimeStamp + ": " + fileName + " cannot be located!\n"
            errorFile = open("files/ErrorLog.txt", "a+", encoding="utf-8")
            errorFile.write(errorContents)
            errorFile.close()
            messageContents = fileName + " cannot be located!"
            return messageContents
