import random
player_position = 0

# snake
snakes = {99: 10,95: 75,92: 66,74: 54,62: 19,49: 11}

# ladder
ladders = {2: 23,8: 34,20: 77,32: 68,41: 77,74: 91}

print('Welcome to the game of snake and ladder')
print('Reach position 100 to win the game')

while player_position < 100:
    input('Press enter to roll the dice....')
    dice = random.randint(1, 6)
    print(f'You rolled a {dice}')
    print(f'You are now at position {player_position}')

    if player_position + dice <=100:
        player_position = player_position + dice
    else:
        print('You cannot move forward as it exceeds position 100')
    print(f'You position is {player_position}')

    if player_position in snakes:
        player_position = snakes[player_position]
        print(f'You got bitten by a snake! You are now at position {player_position}')


    if player_position in ladders:
        player_position = ladders[player_position]
        print(f'You climbed a ladder! You are now at position {player_position}')

if player_position >= 100:
    print('Congratulations! You have won the game!')