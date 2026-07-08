# module calling 
# from lecture8 import fact
# print(int(fact(3)))


# import math
# print(math.factorial(14))
# print(math.floor(6.7))
# print(math.ceil(6.7))
# print(math.)


import random
print(random.randint(1,10))

import random 
fruits = ['apple','orange','pineapple','grapes','mango','watermelon']
print(random.choice(fruits))


# import random
# ch = ['heads','tails']
# print(random.choice(ch))

import random
z = random.randint(0,1)
if z==1:
    print('heads')
else:
    print('tails')

import random 
ch = ['rock','paper','scissor']
comp = random.choice(ch)
player = ''

while player not in ch:
    player == input('enter your choice rock/paper/scissor :-').lower()
print(f'player :- {player} \ncomputer :- {comp}')
if player == comp:
    print('its a tie !!!!')
elif comp == 'rock':
    if player=='scissor':
        print('rock destroys scissor and the computer wins')
    else:
        print('paper covers rock and player wins')
elif comp=='paper':
    if player=='rock':
        print('paper covers rock nd comp wins')
    else:
        print('rock destroys scissor and player wins') 


create a rpg game
player vs enemy

import random
playerhp = 100
enemyhp = 100
player = input('Enter your name:')
enemy = random.choice(['dragon','goblin','troll'])
turn = 1
while playerhp>0 and enemyhp>0:
    print(f'your turn {turn}')
    print(f'{enemy} attacks player')
    playerhp = playerhp - random.randint(8,20)
    print('player hp {playerhp}') 
    print(f'{player} attacks back')
    enemyhp = enemyhp - random.randint(8,20)
    print(f'enemy hp {enemyhp}')
    turn = turn+1
    if playerhp<=0:
        print(f'{enemy} won')
        break
    elif enemyhp<=0:
        print(f'{player} won')
        break

