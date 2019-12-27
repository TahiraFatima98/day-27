import random
print('Welcome to the Dice rolling game:')
startgame=input('do you want to roll the dice? ')

def rolldice():
    print('your number is:' + str(random.randint(1,6)))
    global play_again
    play_again=input('would you like to play again?')
if startgame=='yes':
    rolldice()
    while play_again=='yes':
        rolldice()
elif startgame=='no':
    print('Game over')
else:
    print('exit game')
