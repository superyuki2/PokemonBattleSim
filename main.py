import sys
import copy
import random
import pokeAndmoves
import pokemon

class Player: 
	def __init__(self):
		self.pokemonSet = []
		self.spikes = False #Spikes
		self.poisonSpikes = False #Poison Spikes
		self.reflect = False #Reflect
		self.screen = False #Light Screen
		self.curPoke = None #Current Pokemon


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
def isIneffective(moveType, att1, att2):
	return False

#Handles all type relations and returns the multiplier value.
def typeRelation():
	return None



#Checks if all 6 Pokemon have fainted. If so, returns the losing player.
def gameOver(player):
	for poke in player.pokemonSet:
		if poke.hp != 0:
			return False
	return player

#Calculates the damage (int) given user field status, opponent field status, player's Pokemon, 
#opponent's Pokemon, and the move used.
def damageCalculation(user, receiver, pokeP, pokeO, move):
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


def main():
	print("Welcome to Pokemon Battle Simulator! Your Pokemon will be chosen now.")
	player = Player()
	opponent = Player()
	#Choose the 6 initial pokemon for both players.
	choosePokeRandom(player)
	choosePokeRandom(opponent)

	#Handles beginning where starter Pokemon are chosen. 
	beginningPrompt(player, opponent)


	#Battle timeline
	# Player chooses which Pokemon to start with. Opponent can be random -> curPoke are set.
	# Beginning of every turn, print the following:
	# 	Pokemon names, HP, status
	# 	Options 1-4 along with name of each move
	# 	Option 5, which is for replacing Pokemon. Then, print 5 other Pokemon along w/ HP
	# 	Option 6 can be printing all other stats of the curPoke
	# Both players choose a move, and order does not matter for either.



if __name__ == "__main__":
	main()

	