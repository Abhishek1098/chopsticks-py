class Hand:

    fingers = 1

    def __init__(self):
        self.fingers = 1

    def get_amount_fingers(self):
        return self.fingers

    def add_fingers(self, hand):
        if self.fingers != 0:
            self.fingers += hand.get_amount_fingers()


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

game = False
move = None

player1.hit('left', player2.rightHand)


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
            player2.hit(sideUser, player1.leftHand)
        else:
            player2.hit(sideUser, player1.rightHand)