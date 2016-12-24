##### All methods that don't change variables. #####

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

#Calculates the damage (int) given user field status, opponent field status, player's Pokemon, 
#opponent's Pokemon, and the move used. Also, critical hit is not accounted for in this damage calculation.
def damageCalculation(p, o, pokeP, pokeO, move):
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
	#Weather and status effects on damage taken into account.
	extra = 1
	if p.weather == 'Rain':
		if move.attribute == 'Fire':
			extra = extra / 2
		elif move.attribute == 'Water':
			extra = extra * 2
	if p.weather == 'Hail' and move.attribute == 'Ice':
		extra = extra * 2
	if pokeP.status == 'Burn' and move.phys:
		a = a / 2
	if (o.reflect and move.phys) or (o.screen and (not move.phys)):
		a = a / 2

	nonMod = (0.44 * (a/d) * move.damage) + 2
	mod = stab * typeEffect * extra * random.uniform(0.85, 1.00)
	totalDamage = int(nonMod * mod)
	return totalDamage


