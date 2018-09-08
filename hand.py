class hand():
    fingers = 1

    def __init__(self, Fingers):
        self.fingers = Fingers
    def make_hand(fingers):
        hand = Hand(fingers)


    def getFingers(self):
        return self.fingers

    def addFingers(self,hand):
        if self.fingers != 0:
            add = hand.getFingers()
            self.fingers = self.fingers + add
            checkFingers()

    def checkFingers(self):
        if self.fingers >= 5:
            self.fingers = 0

class Player():
    leftHand = hand(1)
    rightHand = hand(1)
    isUser = True

    def hit(side, opponentHand):
        if side == 'left':
            leftHand.addFingers(opponentHand)
        else:
            rightHand.addFingers(opponentHand)


player1 = Player()
player2 = Player()

print(player1.leftHand.fingers)

