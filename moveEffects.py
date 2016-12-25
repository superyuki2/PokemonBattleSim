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
def attack(p, o, pM):
	cannotmove = statusTurnCheck(p)
	if cannotmove:
		return

	#naming it n for simplicity.
	n = pM.name
	print(p.curPoke.name + " used " + pM.name + "!")

	success = True

	#attacks where attributes don't matter (not affected by Substitute)
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
			if o.spikes < 3:
				o.spikes += 1
			else:
				success = False
		elif n == 'Rest':
			if not p.curPoke.sleep:
				p.curPoke.hp = p.curPoke.basehp
				p.curPoke.sleep = 3
			else: 
				success = False
		elif n == 'Light Screen':
			if not p.screen:
				p.screen = 5
			else:
				success = False
		elif n == 'Reflect':
			if not p.reflect:
				p.reflect = 5
			else: 
				success = False
		elif n == 'Substitute':
			if not p.curPoke.sub:
				p.sub = True
			else:
				success = False
		elif n == 'Swords Dance':
			p.curPoke.attack *= 2.25
		elif n == 'Slack Off':
			p.curPoke.hp += int(p.curPoke.basehp / 2)
			if p.curPoke.hp > p.curPoke.basehp:
				p.curPoke.hp = p.curPoke.basehp
		elif n == 'Stealth Rock':
			if not o.stealthRock:
				o.stealthRock = True
			else:
				success = False
		elif n == 'Rain Dance':
			if not p.weather == 'Rain':
				p.weather = 'Rain'
				o.weather = 'Rain'
			else:
				success = False

		### Have to fix the problem of taunting first -> the latter Pokemon uses status mvove. ###
		elif n == 'Taunt':
			if not o.curPoke.taunt:
				o.curPoke.taunt = 5
			else:
				success = False
		elif n == 'Toxic Spikes':
			if o.toxicSpikes < 2:
				o.toxicSpikes += 1
			else:
				success = False
		elif n == 'Curse':
			p.curPoke.attack *= 1.5
			p.curPoke.defense *= 1.5
			p.curPoke.speed *= 0.66

	#status attacks where attributes matter
	elif n in (['Will-O-Wisp', 'Night Shade', 'Confuse Ray', 'Thunder Wave']):
		return

	#regular attacks that calculate damage
	elif n in (['Draco Meteor', 'Fire Blast', 'Superpower', 'ExtremeSpeed', 'Giga Drain', 'Hidden Power Fire',
	'Volt Change', 'Acid Bomb', 'U-turn', 'Close Combat', 'Stone Edge', 'Leaf Blade', 'Earthquake', 'Ice Fang',
	'Ice Shard', 'Icicle Crash', 'Night Burst', 'Hidden Power Ice', 'Focus Blast', 'Sucker Punch', 'Hurricane',
	'Hammer Arm', 'Earth Power', 'Flamethrower', 'Ice Beam', 'Surf', 'Psychic', 'Energy Ball', 'Return', 'Fire Punch',
	'Megahorn', 'Facade', 'Crunch', 'Brick Break']):
		return

	if not success:
		print("But it failed!")

	pM.pp -= 1

	




