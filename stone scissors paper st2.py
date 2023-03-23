import random
print('game: stone, scissors, paper, lizard, spock')
defeated_by = {'stone': ['scissors', 'lizard'],
               'scissors': ['paper', 'lizard'],
               'paper': ['stone', 'spock'],
               'lizard': ['spock', 'paper'],
               'spock': ['scissors', 'stone']}
bot = 0
you = 0
dead_heat = 0
counter = 1
rounded = int(input('enter the number of rounds :'))
while counter <= rounded:
    print(counter, 'Round')
    a = input()
    b = random.choice(list(defeated_by.keys()))

    if a in defeated_by[b]:
        print('bot win')
        counter += 1
        bot += 1
    elif a == b:
        dead_heat += 1
        print('dead heat')
    else:
        print('you win')
        counter += 1

if bot < you:
    print('in the end you Win')
else:
    print('in the end bot Win')
print('bot win ', bot, 'you win ', you, 'dead heat ', dead_heat)
