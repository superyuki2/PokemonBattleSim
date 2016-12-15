import sys
import pokeAndmoves
import pokemon

#Global methods for actual gameplay

def main():
	print("Welcome to Pokemon Battle Simulator! Your Pokemon will be chosen now.")
	print([poke.name for poke in pokeAndmoves.allPokemon])
	print([move.name for move in poke.moves for poke in pokeAndmoves.allPokemon])
	player = []
	opponent = []
	player.append(pokeAndmoves.allPokemon[0])
	print(player)

if __name__ == "__main__":
	main()