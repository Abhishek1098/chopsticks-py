player1 = Player()
player2 = Player()

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