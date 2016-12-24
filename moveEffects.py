import staticMethods as sm 

##### Methods that take care of individual moves. #####

#Boolean for priority: True for human player, False for opponent player.
def calculatePriority(p, o, pM, oM):
	pp = False
	op = False
	if pM.name in ['ExtremeSpeed', 'Ice Shard', 'Sucker Punch']:
		pp = True
	if oM.name in ['ExtremeSpeed', 'Ice Shard', 'Sucker Punch']:
		op = True

	if pp == op:
		return (p.curPoke.speed >= o.curPoke.speed)
	else:
		if pp:
			return True
		elif op:
			return False

#A hefty function that takes care of all moves!
#In order of: 
#	attacks where attributes don't matter
#	status attacks where attributes matter
#	regular attacks that calculate damage
def attack(p, o, pM):
	print(p.curPoke.name + " used " + pM.name + "!")

