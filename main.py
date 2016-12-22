import sys
import copy
import random
import pokeAndmoves
import pokemon

class Player: 
	def __init__(self):
		self.pokemonSet = [] #All Pokemon
		self.curPoke = None #Current Pokemon
		self.stealthRock = False #Stealth Rock
		self.reflect = False #Reflect
		self.screen = False #Light Screen
		self.weather = None #Current weather
		self.spikes = 0 #Spikes
		self.poisonSpikes = 0 #Poison Spikes


######Global methods for actual gameplay######

#Chooses 6 random numbers for initial Pokemon selection.
def choosePokeRandom(player):
	six = random.sample(range(0, len(pokeAndmoves.allPokemon)), 6)
	for i in six:
		player.pokemonSet.append(copy.deepcopy(pokeAndmoves.allPokemon[i]))

#Shows the 6 Pokemon chosen, and prompts user to choose starting Pokemon.
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

#Called in the beginning of every turn. Shows basic stats and all options.
def everyTurn(player, opp, p1, p2):
	print("")
	print("Your current Pokemon: " + p1.name + " HP: " + str(p1.hp) + "/" + str(p1.basehp) + " Status: " + str(p1.status))
	print("Opponent Pokemon: " + p2.name + " HP: " + str(p2.hp) + "/" + str(p2.basehp) + " Status: " + str(p2.status))
	print("Current weather: " + str(player.weather))
	print("What would you like to do? (0 - 5)")
	for i in range(len(p1.moves)):
		print(p1.moves[i].name + ": " + str(i))
	print("Switch Pokemon: 4")
	print("See Pokemon stats: 5")

#Asks player to choose an option.
def playerChoice(player, opp):
	goodInput = False
	while not goodInput:
		try:
			everyTurn(player, opp, player.curPoke, opp.curPoke)
			choice = int(raw_input())
			if (choice < 0 or choice > 5):
				print("Please enter a valid number (0 - 5).")
				continue
			#Use Move
			elif choice in [0, 1, 2, 3]:
				goodInput = True
			#Switch Pokemon
			elif choice == 4:
				goodInput = True
			#Show stat
			elif choice == 5:
				showStats(player.curPoke)
				continue
		except ValueError: 
			print("Please enter a valid number (0 - 5).")
			continue
	return choice

#Prompts player to choose which Pokemon to switch to. Returns the Pokemon index, or 6 for cancel. 
def switchPokemon(player):
	goodInput = False
	switchPokeList = []
	for i in range(0, len(player.pokemonSet)):
		if player.pokemonSet[i] != player.curPoke and player.pokemonSet[i].hp > 0:
			switchPokeList.append(i)
	while not goodInput:
		try:
			print("Please choose which Pokemon to switch in (0 - 5), or cancel (6).")
			for i in switchPokeList:
				print(player.pokemonSet[i].name + ": " + str(i))
			print("Cancel: 6") 
			switchPoke = int(raw_input())
			if (switchPoke not in switchPokeList) and switchPoke != 6:
				print("Please enter a valid number (0 - 6).")
				continue
			goodInput = True
		except ValueError: 
			print("Please enter a valid number (0 - 6).")
			continue
	return switchPoke

#Checks for conditions that should be checked after every switch.
def switchCheck(p, o):
	return None

#Makes a move given player, opponent, and the chosen moves of both.
def makeMove(p, o, pM, oM):
	return None

#Checks for conditions that should be checked at the end of each turn.
def turnEndCheck():
	#weatherCheck
	#statusCheck
	return None


#Shows all other basic stats of a Pokemon.
def showStats(p):
	print("")
	print("Stats of " + p.name)
	print("Types: " + str(p.attribute1) + ", " + str(p.attribute2))
	print("Attack: " + str(p.attack))
	print("Defense: " + str(p.defense))
	print("SpAttack: " + str(p.spAttack))
	print("SpDefense: " + str(p.spDefense))
	print("Speed: " + str(p.speed))

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
		if poke.hp > 0:
			return False
	return player

#Calculates the damage (int) given user field status, opponent field status, player's Pokemon, 
#opponent's Pokemon, and the move used. Also, critical hit is not accounted for in this damage calculation.
def damageCalculation(user, receiver, pokeP, pokeO, move):
	typeEffect = typeRelation(move.attribute, pokeO.attribute1) * typeRelation(move.attribute, pokeO.attribute2)
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

	#Game starts
	playing = True
	while playing:
		#Ask for choice of player. Also includes everyTurn method
		choice = playerChoice(player, opponent)

		#Pokemon switch option
		if choice == 4:
			switchPoke = switchPokemon(player)
			#Cancelled, back to playerChoice()
			if switchPoke == 6:
				continue
			#Switch Pokemon
			else:
				print("Come back, " + player.curPoke.name + "!")
				player.curPoke = player.pokemonSet[switchPoke]
				print(player.curPoke.name + ", I choose you!")
				#switchCheck(player, opponent)
		#Move option
		pMove = None
		if choice in [0, 1, 2, 3]:
			pMove = player.curPoke.moves[choice]

		#Opponent choose a move. Random for now.
		oMove = opponent.curPoke.moves[random.randint(0, len(opponent.curPoke.moves))]
		#makeMove(player, opponent, pMove, oMove). 

		playing = False


if __name__ == "__main__":
	main()

