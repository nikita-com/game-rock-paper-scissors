import random
bot = 0
player = 0
print('game: stone, scissors, paper')
while (bot < 3) and (player < 3):
	print('    ')
	print('bot', bot, 'you', player)
	print('choose and write stone, scissors or paper')
	a = input()
	botrud = random.randint(1, 3)
	c = botrud
	if c == 1:
		print('opponent chose stone')
	elif c == 2:
		print('opponent chose scissors')
	else:
		print('opponent chose paper')

	if a == 'stone':
		playerrud=1
	elif a == 'scissors':
		playerrud = 2
	else:
		playerrud = 3
		
	if playerrud == botrud:
		print('dead heat')
	elif playerrud < botrud:
		if (playerrud == 1) and (botrud == 3):
			print('you win')
			bot = bot+1
		else:
			print('you win')
			player = player+1
	else:
		if (playerrud == 3) and (botrud == 1):
			print('you win')
			player = player+1
		else:
			print('you lose')
			bot = bot+1
print('  ')
print('bot',bot, 'you',player,)
print('end of the game')
if bot >= 3:
	print('win bot, you lose')
else:
	print('bot lose, you win')
