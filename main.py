import sys
import copy
import random
import pokeAndmoves
import pokemon
import staticMethods as sm

class Player: 
	def __init__(self):
		self.pokemonSet = [] #All Pokemon
		self.curPoke = None #Current Pokemon
		self.stealthRock = False #Stealth Rock
		self.reflect = False #Reflect
		self.screen = False #Light Screen
		self.weather = None #Current weather
		self.spikes = 0 #Spikes
		self.toxicSpikes = 0 #Poison Spikes


######Global methods for actual gameplay######

### Functions for beginning the game, before any acutal game play. ###

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
				sm.showStats(player.curPoke)
				continue
		except ValueError: 
			print("Please enter a valid number (0 - 5).")
			continue
	return choice

#Prompts player to choose which Pokemon to switch to. Returns the Pokemon index.
def switchChoice(player):
	goodInput = False
	switchPokeList = []
	for i in range(0, len(player.pokemonSet)):
		if player.pokemonSet[i] != player.curPoke and player.pokemonSet[i].hp > 0:
			switchPokeList.append(i)
	while not goodInput:
		try:
			print("Please choose which Pokemon to switch in (0 - 5).")
			for i in switchPokeList:
				print(player.pokemonSet[i].name + ": " + str(i))
 			switchPoke = int(raw_input())
			if switchPoke not in switchPokeList:
				print("Please enter a valid number (0 - 5).")
				continue
			goodInput = True
		except ValueError: 
			print("Please enter a valid number (0 - 5).")
			continue
	return switchPoke

#Called when a Pokemon is switched in, whether it be after a switch option
#or after a Pokemon faints. 
def switchPokemon(p, switchPoke):
	print("Come back, " + p.curPoke.name + "!")
	p.curPoke = p.pokemonSet[switchPoke]
	print(p.curPoke.name + ", I choose you!")

#Checks for conditions that should be checked after every switch.
def switchCheck(p, o):
	if p.stealthRock:
		p.curPoke.hp -= (int(p.curPoke.basehp/8 * sm.typeRelation('Rock', p.curPoke.attribute1) * 
			sm.typeRelation('Rock', p.curPoke.attribute2)))
		print("Stealth Rock gave damage to " + p.curPoke.name + "!")
		if faintCheck(p.curPoke):
			return
	if p.spikes:
		if not (sm.isIneffective('Ground', p.curPoke.attribute1) or sm.isIneffective('Ground', p.curPoke.attribute2)):
			p.curPoke.hp -= int(p.curPoke.basehp/8 * p.spikes)
			print("Spikes gave damage to " + p.curPoke.name + "!")
			if faintCheck(p.curPoke):
				return
	if (p.toxicSpikes) and p.curPoke.status == None:
		if not ((p.curPoke.attribute1 in ['Flying', 'Poison', 'Steel']) or (p.curPoke.attribute2 in ['Flying', 'Poison', 'Steel'])):
			if p.toxicSpikes == 1:
				p.curPoke.status = 'Poison'
			elif p.toxicSpikes == 2:
				p.curPoke.status = 'Toxic'
			print("Toxic spikes dug into " + p.curPoke.name + "!")

#Makes a move given player, opponent, and the chosen moves of both.
def makeMove(p, o, pM, oM):
	return None

#Checks if the Pokemon has fainted, updates Pokemon hp to 0 if it becomes negative.
def faintCheck(p):
	if p.hp <= 0:
		p.hp = 0
		print(p.name + " has fainted!")
		return True
	return False

#Called when a pokemon faints. 
def afterFaint():
	return None

#Checks if all 6 Pokemon have fainted. If so, returns the losing player.
def gameOver(player):
	for poke in player.pokemonSet:
		if poke.hp > 0:
			return False
	return player

#Calculates the damage (int) given user field status, opponent field status, player's Pokemon, 
#opponent's Pokemon, and the move used. Also, critical hit is not accounted for in this damage calculation.
def damageCalculation(user, receiver, pokeP, pokeO, move):
	typeEffect = sm.typeRelation(move.attribute, pokeO.attribute1) * sm.typeRelation(move.attribute, pokeO.attribute2)
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

### Turn End Checks ###

#Checks for conditions that should be checked at the end of each turn.
def turnEndCheck(p, o):
	weatherDamageCheck(p, o)
	#statusDamageCheck
	return None

#Checks for weather, called at the end of every turn.
def weatherDamageCheck(p, o):
	if p.weather:
		if p.weather == 'Hail':
			if not (p.curPoke.attribute1 == 'Ice' or p.curPoke.attribute2 == 'Ice'):
				p.curPoke.hp -= int(p.curPoke.basehp/16)
			if not (o.curPoke.attribute1 == 'Ice' or o.curPoke.attribute2 == 'Ice'):
				o.curPoke.hp -= int(o.curPoke.basehp/16)
		elif p.weather == 'Sandstorm':
			if not (p.curPoke.attribute1 in ['Rock', 'Ground', 'Steel'] or p.curPoke.attribute2 in ['Rock', 'Ground', 'Steel']):
				p.curPoke.hp -= int(p.curPoke.basehp/16)
			if not (o.curPoke.attribute1 in ['Rock', 'Ground', 'Steel'] or o.curPoke.attribute2 in ['Rock', 'Ground', 'Steel']):
				o.curPoke.hp -= int(o.curPoke.basehp/16)


#Checks for status, called at the end of every turn.
def statusDamageCheck(p, o):
	return None


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
			switchPoke = switchChoice(player)
			switchPokemon(player, switchPoke)
			switchCheck(player, opponent)
		#Move option
		pMove = None
		if choice in [0, 1, 2, 3]:
			pMove = player.curPoke.moves[choice]

		#Opponent choose a move. Random for now.
		oMove = opponent.curPoke.moves[random.randint(0, len(opponent.curPoke.moves) - 1)]
		#makeMove(player, opponent, pMove, oMove). 

		playing = False


if __name__ == "__main__":
	main()

