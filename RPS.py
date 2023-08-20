import random


options=('rock', 'paper', 'scissors')
running = True 
while running:

    player=None
    computer=random.choice(options)

    name=input('what is your name:')

    comp=0
    p=0
   


    while player not in options:
        player=input('enter a choice(rock paper scissors):')


    print(f'player: {player}')
    print(f'computer: {computer}')

    if player==computer:
        print('its a tie!')
        p=+1
        comp=+1
    elif player == 'rock' and computer == 'scissors':
        print( f"{name} wins" )
        p=+1
    elif player == 'paper' and computer == 'rock':
        print( f"{name} wins")
        p=+1
    elif player == 'scissors' and computer == 'paper':
        print( f"{name} wins")
        p=+1
    else:
        print('computer wins')
        comp=+1

    if not input("Play again? (y/n): ").lower() == "y":
        running = False


    print('the computer has',comp,'points')
    print(f"{name} has", p, 'points')






