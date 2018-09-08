class hand():
    fingers = 1

    def getFingers():
        return fingers

    def addFingers(hand):
        if fingers != 0:
            add = hand.getFingers()
            fingers = fingers + add
            checkFingers()

    def checkFingers():
        if fingers >= 5:
            fingers = 0