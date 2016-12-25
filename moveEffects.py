import staticMethods as sm 
import random

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

#Updates status counter for attacking Pokemon before each attack.
def statusTurnCheck(p):
	if p.curPoke.sleep:
		p.curPoke.sleep -= 1
		if p.curPoke.sleep == 0:
			print(p.curPoke.name + " woke up!")
		else:
			print(p.curPoke.name + " is asleep!")
			return True
	elif p.curPoke.confused:
		p.curPoke.confused -= 1
		if p.curPoke.confused == 0:
			print(p.curPoke.name + " is no longer confused!")
		else:
			if random.randint(0, 99) in range(50):
				print(p.curPoke.name + " is confused and attacked itself!")
				p.curPoke.hp -= 40
				return True
	elif p.curPoke.ice:
		p.curPoke.ice -= 1
		if p.curPoke.ice == 0:
			print(p.curPoke.name + " is no longer frozen!")
		else:
			print(p.curPoke.name + " is frozen and can not move!")
			return True
	elif p.curPoke.paralyze:
		if random.randint(0, 99) in range(25):
			print(p.curPoke.name + " is paralyzed and can not move!")
			return True
	return False

#A hefty function that takes care of all moves!
#In order of: 

#	status attacks where attributes matter
#	regular attacks that calculate damage
def attack(p, o, pM):
	cannotmove = statusTurnCheck(p)
	if cannotmove:
		return

	n = pM.name
	print(p.curPoke.name + " used " + pM.name + "!")
	#attacks where attributes don't matter
	if n in (['Pain Split', 'Spikes', 'Rest', 'Light Screen', 'Reflect', 'Substitute', 
	'Swords Dance', 'Slack Off', 'Stealth Rock', 'Rain Dance', 'Taunt', 'Toxic Spikes', 'Curse']):
		if n == 'Pain Split':
			avghp = int((p.curPoke.hp + o.curPoke.hp) / 2)
			p.curPoke.hp = avghp
			o.curPoke.hp = avghp
			if p.curPoke.hp > p.curPoke.basehp:
				p.curPoke.hp = p.curPoke.basehp
			if o.curPoke.hp > o.curPoke.basehp:
				o.curPoke.hp = o.curPoke.basehp
		elif n == 'Spikes':
			o.spikes += 1
		elif n == 'Rest':
			p.curPoke.hp = p.curPoke.basehp
			p.curPoke.sleep = 3




