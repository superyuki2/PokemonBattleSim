import sys
import copy
import random
import pokeAndmoves
import pokemon

class Player: 
	def __init__(self):
		self.pokemonSet = [] #All Pokemon
		self.curPoke = None #Current Pokemon
		self.spikes = False #Spikes
		self.poisonSpikes = False #Poison Spikes
		self.reflect = False #Reflect
		self.screen = False #Light Screen
		self.weather = None #Current weather
		

######Global methods for actual gameplay######

#Chooses 6 random numbers for initial Pokemon selection.
def choosePokeRandom(player):
	six = random.sample(range(0, len(pokeAndmoves.allPokemon)), 6)
	for i in six:
		player.pokemonSet.append(copy.deepcopy(pokeAndmoves.allPokemon[i]))

#Show the 6 Pokemon chosen, and prompts user to choose starting Pokemon.
def beginningPrompt(player, opponent):
	print("The following are the Pokemon that have been chosen.")
	for i in range(len(player.pokemonSet)):
		print(player.pokemonSet[i].name + ": " + str(i))
	goodInput = False
	while not goodInput:
		try: 
			starter = int(raw_input("Please choose which Pokemon to start with (0 - 5)."))
			print(starter)
			while (starter < 0 or starter > 5):
				starter = int(raw_input("Please enter a valid number (0 - 5)."))
			goodInput = True
		except ValueError: 
			print("Please enter a valid number (0 - 5).")
			continue
	player.curPoke = player.pokemonSet[starter]
	opponent.curPoke = opponent.pokemonSet[random.randint(0, 5)]
	print(player.curPoke.name + ", I choose you!")
	print("Your opponent's first Pokemon is " + opponent.curPoke.name + "!")

#Handles cases where move is ineffective against the opponent Pokemon. If effective, return False.
#Takes the type of the move and attribute of the receiving Pokemon as arguments. 
def isIneffective(m, a):
	if ((m == 'Normal' and a == 'Ghost') or (m == 'Electric' and a == 'Ground')
		or (m == 'Fighting' and a == 'Ghost') or (m == 'Poison' and a == 'Steel')
		or (m == 'Ground' and a == 'Flying') or (m == 'Psychic' and a == 'Dark')
		or (m == 'Ghost' and a == 'Normal') or (m == 'Dragon' and a == 'Fairy')):
		return True
	return False

#Handles all type relations and returns the multiplier value. Same args as isIneffective(). 
def typeRelation(m, a):
	if m == 'Normal':
		if a == 'Rock' or a == 'Steel':
			return 0.5
	elif m == 'Fire':
		if a == 'Water' or a == 'Rock' or a == 'Fire' or a == 'Dragon':
			return 0.5
		elif a == 'Grass' or a == 'Ice' or a == 'Steel' or a == 'Bug':
			return 2.0
	elif m == 'Water':
		if a == 'Water' or a == 'Dragon' or a == 'Grass':
			return 0.5
		elif a == 'Rock' or a == 'Ground' or a == 'Fire':
			return 2.0
	elif m == 'Electric':
		if a == 'Grass' or a == 'Electric' or a == 'Dragon':
			return 0.5
		elif a == 'Water' or a == 'Flying':
			return 2.0
	elif m == 'Grass':
		if (a == 'Grass' or a == 'Fire' or a == 'Dragon' or a == 'Flying' or a == 'Poison'
		or a == 'Steel' or a == 'Bug'):
			return 0.5
		elif a == 'Water' or a == 'Rock' or a == 'Ground':
			return 2.0
	elif m == 'Ice':
		if a == 'Fire' or a == 'Water' or a == 'Steel' or a == 'Ice':
			return 0.5
		elif a == 'Ground' or a == 'Dragon' or a == 'Grass' or a == 'Flying':
			return 2.0
	elif m == 'Fighting':
		if a == 'Flying' or a == 'Poison' or a == 'Psychic' or a == 'Fairy' or a == 'Bug':
			return 0.5
		elif a == 'Normal' or a == 'Ice' or a == 'Rock' or a == 'Dark' or a == 'Steel':
			return 2.0
	elif m == 'Poison':
		if a == 'Poison' or a == 'Ground' or a == 'Rock' or a == 'Ghost':
			return 0.5
		elif a == 'Grass' or a == 'Fairy':
			return 2.0
	elif m == 'Ground':
		if a == 'Grass' or a == 'Bug':
			return 0.5
		elif a == 'Rock' or a == 'Poison' or a == 'Steel' or a == 'Fire' or a == 'Electric':
			return 2.0
	elif m == 'Flying':
		if a == 'Rock' or a == 'Electric' or a == 'Steel':
			return 0.5
		elif a == 'Grass' or a == 'Fighting' or a == 'Bug':
			return 2.0
	elif m == 'Psychic':
		if a == 'Psychic' or a == 'Steel':
			return 0.5
		elif a == 'Fighting' or a == 'Poison':
			return 2.0
	elif m == 'Bug':
		if (a == 'Fire' or a == 'Fighting' or a == 'Poison' or a == 'Flying' 
		or a == 'Fairy' or a == 'Ghost' or a == 'Steel'):
			return 0.5
		elif a == 'Grass' or a == 'Psychic' or a == 'Dark':
			return 2.0
	elif m == 'Rock':
		if a == 'Ground' or a == 'Fighting' or a == 'Steel':
			return 0.5
		elif a == 'Flying' or a == 'Fire' or a == 'Ice' or a == 'Bug':
			return 2.0
	elif m == 'Ghost':
		if a == 'Dark':
			return 0.5
		elif a == 'Psychic' or a == 'Ghost':
			return 2.0
	elif m == 'Dragon':
		if a == 'Steel':
			return 0.5
		elif a == 'Dragon':
			return 2.0
	elif m == 'Dark':
		if a == 'Dark' or a == 'Fighting' or a == 'Fairy':
			return 0.5
		elif a == 'Psychic' or a == 'Ghost':
			return 2.0
	elif m == 'Steel':
		if a == 'Steel' or a == 'Fire' or a == 'Electric' or a == 'Water':
			return 0.5
		elif a == 'Rock' or a == 'Ice' or a == 'Fairy':
			return 2.0
	elif m == 'Fairy':
		if a == 'Fire' or a == 'Poison' or a == 'Steel':
			return 0.5
		elif a == 'Fighting' or a == 'Dark' or a == 'Dragon':
			return 2.0
	return 1.0

#Checks if all 6 Pokemon have fainted. If so, returns the losing player.
def gameOver(player):
	for poke in player.pokemonSet:
		if poke.hp != 0:
			return False
	return player

#Calculates the damage (int) given user field status, opponent field status, player's Pokemon, 
#opponent's Pokemon, and the move used. Also, critical hit is not accounted for in this damage calculation.
def damageCalculation(user, receiver, pokeP, pokeO, move):
	typeEffect = typeRelation(move.attribute, pokeO.attribute1) * typeRelation(move.attribute, pokeO.attribute2)
	print(typeEffect)
	if move.phys:
		a = pokeP.attack
		d = pokeO.defense
	elif move.phys == False:
		a = pokeP.spAttack
		d = pokeO.spDefense
	if move.attribute == pokeP.attribute1 or move.attribute == pokeP.attribute2:
		stab = 1.5
	else:
		stab = 1
	nonMod = (0.44 * (a/d) * move.damage) + 2
	mod = stab * typeEffect * random.uniform(0.85, 1.00)
	totalDamage = int(nonMod * mod)
	return totalDamage


def main():
	print("Welcome to Pokemon Battle Simulator! Your Pokemon will be chosen now.")
	player = Player()
	opponent = Player()
	#Choose the 6 initial pokemon for both players.
	choosePokeRandom(player)
	choosePokeRandom(opponent)

	#Handles beginning where starter Pokemon are chosen. 
	beginningPrompt(player, opponent)
	### Player chooses which Pokemon to start with. Opponent can be random -> curPoke are set. ###

	# Beginning of every turn, print the following:
	# 	Pokemon names, HP, status
	# 	Options 1-4 along with name of each move
	# 	Option 5, which is for replacing Pokemon. Then, print 5 other Pokemon along w/ HP
	# 	Option 6 can be printing all other stats of the curPoke
	# Both players choose a move, and order does not matter for either.

	#Testing
	# p1 = player.curPoke
	# p2 = opponent.curPoke

	# print(player.curPoke.name)
	# print(opponent.curPoke.name)

	# print(damageCalculation(player, opponent, p1, p2, p1.moves[0]))





if __name__ == "__main__":
	main()

