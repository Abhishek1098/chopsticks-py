class Hand():
    fingers = 1

    def __init__(self):
        self.fingers = 1
    def make_hand(fingers):
        hand = Hand(fingers)

    def addFingers(hand):
        if fingers != 0:
            fingers += hand.fingers

    def checkFingers():
        if fingers >= 5:
            fingers = 0

class Player():
    leftHand = Hand()
    leftHand = Hand()
    def __init__(self, isUser):
        self.leftHand = Hand()
        self.rightHand = Hand()
        self.isUser = isUser

    def hit(side, opponentHand):
        if side == 'left':
            leftHand.addFingers(opponentHand.fingers)
        else:
            rightHand.addFingers(opponentHand.fingers)


player1 = Player(True)
player2 = Player(False)

print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)

game = False
move = None

player1.hit('left', player2.rightHand)


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