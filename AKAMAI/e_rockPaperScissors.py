'''
def rockPaperScissorsSimple():
    items=['Rock', 'Paper', 'Scissors']
    player_1 = False
    player_2 = False
    player_1 = int(input("Player 1. Choose: 0. Rock 1. Paper 2. Scissors: "))
    print("Player 1 chose: "+ str(items[player_1]))
    player_2 = int(input("Player 2. Choose: 0. Rock 1. Paper 2. Scissors: "))
    print("Player 1 chose: " + str(items[player_2]))
    if player_1 == player_2:
        print("Tie")
    elif player_1==0:
        if player_2==1:
            print("Player 2 wins.")
        else:
            print("Player 1 wins.")
    elif player_2==1:
'''

