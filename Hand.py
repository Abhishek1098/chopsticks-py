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
            self.leftHand.add_fingers(opponentHand)
        else:
            self.rightHand.add_fingers(opponentHand)


player1 = Player()
player2 = Player()

print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)

game = True
move = None

print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)



while(game==True):
    print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
    print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)
    move = input()
    if move=='hit':
        print('choose hand')
        sideUser = input()
        print('choose hand to hit')
        sideCPU = input()
        if sideCPU=='left':
            player1.hit(sideUser, player2.leftHand)
        else:
            player1.hit(sideUser, player2.rightHand)