import sys
import pokeAndmoves
import pokemon

class Player: 
	def __init__(self, pokemonSet):
		self.pokemonSet = pokemonSet
		self.spikes = False #Spikes
		self.poisonSpikes = False #Poison Spikes
		self.reflect = False #Reflect
		self.screen = False #light Screen


#Global methods for actual gameplay

def main():
	print("Welcome to Pokemon Battle Simulator! Your Pokemon will be chosen now.")
	player = Player(pokeAndmoves.allPokemon[0:6])
	for poke in player.pokemonSet:
		print(poke.name)
		for move in poke.moves:
			print(move.name)
	print(player)

if __name__ == "__main__":
	main()