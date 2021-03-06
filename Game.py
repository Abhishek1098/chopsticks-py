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
            opponentHand.add_fingers(self.leftHand)
        else:
            opponentHand.add_fingers(self.rightHand)

    def find_greatest_hand(self):
        if self.leftHand.fingers < self.rightHand.fingers:
            return self.rightHand
        else:
            return self.leftHand

    def find_least_hand(self):
        if self.leftHand.fingers < self.rightHand.fingers:
            return self.rightHand
        else:
            return self.leftHand

class Bot:

    leftHand = Hand()
    rightHand = Hand()

    def __init__(self):
        self.leftHand = Hand()
        self.rightHand = Hand()

    def find_greatest_hand(self):
        if self.leftHand.fingers < self.rightHand.fingers:
            return self.rightHand
        else:
            return self.leftHand

    def find_least_hand(self):
        if self.leftHand.fingers < self.rightHand.fingers:
            return self.rightHand
        else:
            return self.leftHand

    def hit(self, opponent):
        opponent.find_least_hand().add_fingers(self.find_greatest_hand())


import random

# TODO: We have to change this to Player and CPU

player1 = Bot()
player2 = Player()

game = True
move = None
user_turn = True
turn = 1

def left_or_right():
    if random.randint(0,1) > 0:
        return 'left'
    else:
        return 'right'

while(game==True):
    print('******************************')
    print('Opponent Left: ', player1.leftHand.fingers, '\t', 'Opponent Right: ', player1.rightHand.fingers)
    print('Your Left: ', player2.leftHand.fingers, '\t', 'Your Right: ', player2.rightHand.fingers)
    if user_turn: 
        print('USER TURN \t Turn: ', turn)   
        print('choose move')
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
    else:
        print('CPU TURN \t Turn: ', turn)   
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
                player1.hit(player2)
            else:
                player1.hit(player2)
    turn += 1
    user_turn = not user_turn