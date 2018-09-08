class Hand:

    fingers = 1

    def __init__(self):
        self.fingers = 1

    def add_fingers(self, hand):
        if self.fingers != 0:
            self.fingers += hand.fingers


class Player:

    leftHand = Hand()
    rightHand = Hand()

    def __init__(self):
        self.leftHand = Hand()
        self.rightHand = Hand()

    def hit(self, side, opponentHand):
        if side == 'left':
            self.leftHand.addFingers(opponentHand.fingers)
        else:
            self.rightHand.addFingers(opponentHand.fingers)
