class Hand:

    fingers = 1

    def __init__(self):
        self.fingers = 1

    def add_fingers(self, hand):
        if self.fingers != 0:
            self.fingers += hand.fingers
        self.check_fingers()
        hand.check_fingers()
    def check_fingers(self):
        if self.fingers >= 5:
            self.fingers = 0

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

import random

player1 = Player()
player2 = Player()

print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)

game = True
move = None
user_turn = True

print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)

def left_or_right():
    if random.randint(0,1) > 0:
        return 'left'
    else:
        return 'right'

while(game==True):
    print('******************************')
    if user_turn:
        print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
        print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)
        print('choose move')
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
    else:
        print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
        print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)
        print('choose move')
        move = 'hit'
        print(move)
        if move=='hit':
            print('choose hand')
            sideUser = left_or_right()
            print(sideUser)
            print('choose hand to hit')
            sideCPU = left_or_right()
            print(sideCPU)
            if sideCPU=='left':
                player2.hit(sideUser, player1.leftHand)
            else:
                player2.hit(sideUser, player1.rightHand)
                
    if user_turn == True:
        user_turn = False
    else:
        user_turn = True