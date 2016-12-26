import staticMethods as sm 
import main
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
			p.curPoke.status = None
			print(p.curPoke.name + " woke up!")
		else:
			print(p.curPoke.name + " is asleep!")
			return True
	elif p.curPoke.confused:
		p.curPoke.confused -= 1
		if p.curPoke.confused == 0:
			p.curPoke.status = None
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
			p.curPoke.status = None
		else:
			print(p.curPoke.name + " is frozen and can not move!")
			return True
	elif p.curPoke.status == 'Paralyzed':
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

	#Check if the attack actually hit.
	if random.randint(0, 99) in range(pM.acc * p.curPoke.accuracy):
		hit = True
	else:
		hit = False

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
				p.curPoke.status = 'Sleep'
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
			if not p.curPoke.sub and p.curPoke.hp > int(p.curPoke.basehp / 4):
				p.curPoke.sub = True
				p.curPoke.hp -= int(p.curPoke.basehp / 4)
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

		### Have to fix the problem of taunting first -> the latter Pokemon uses status move. ###
		#maybe just make it a low priority move?
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
		if (sm.isIneffective(pM.attribute, o.curPoke.attribute1) or sm.isIneffective(pM.attribute, o.curPoke.attribute2)
			or o.curPoke.sub):
			success = False
		else:
			if n == 'Will-O-Wisp':
				if not o.curPoke.status and hit:
					o.curPoke.status = 'Burn'
				else:
					success = False
			elif n == 'Night Shade':
				if hit:
					o.curPoke.hp -= 50
				else:
					success = False
			elif n == 'Confuse Ray' and hit:
				if not o.curPoke.status and hit:
					o.curPoke.status = 'Confused'
					o.curPoke.confused = 3
				else:
					success = False
			### Code 1/2 speed for paralyzed, probably in calculatePriority. ###
			elif n == 'Thunder Wave':
				if not o.curPoke.status and hit:
					o.curPoke.status = 'Paralyzed'
				else:
					success = False

	#regular attacks that calculate damage
	elif n in (['Struggle', 'Draco Meteor', 'Fire Blast', 'Superpower', 'ExtremeSpeed', 'Giga Drain', 'Hidden Power Fire',
	'Volt Change', 'Acid Bomb', 'U-turn', 'Close Combat', 'Stone Edge', 'Leaf Blade', 'Earthquake', 'Ice Fang',
	'Ice Shard', 'Icicle Crash', 'Night Burst', 'Hidden Power Ice', 'Focus Blast', 'Sucker Punch', 'Hurricane',
	'Hammer Arm', 'Earth Power', 'Flamethrower', 'Ice Beam', 'Surf', 'Psychic', 'Energy Ball', 'Return', 'Fire Punch',
	'Megahorn', 'Facade', 'Crunch', 'Ice Punch', 'Brick Break']):
		if sm.isIneffective(pM.attribute, o.curPoke.attribute1) or sm.isIneffective(pM.attribute, o.curPoke.attribute2):
			success = False
		else:
			### Additional damage calculations included. Maybe move over to damageCalc? ###
			totalDamage = sm.damageCalculation(p, o, p.curPoke, o.curPoke, pM)
			if n in (['Leaf Blade', 'Stone Edge', 'Icicle Crash']) and random.randint(0, 99) in range(30):
				totalDamage = int(totalDamage * 1.5)
				print("It is a critical hit!")
			elif n in (['Facade']) and p.curPoke.status:
				totalDamage *= 2

			#Substitute check
			if o.curPoke.sub:
				if totalDamage > int(o.curPoke.basehp / 4):
					print("The Substitute was destroyed!")
					o.curPoke.sub = False
					pM.pp -= 1
				else:
					print("The Substitute was not destroyed!")
					pM.pp -= 1
				if n in (['Volt Change', 'U-turn']):
					main.switchPokemon(p)
					return
			#The attack hits.
			if hit:
				o.curPoke.hp -= totalDamage

				#Attacks with no status effects.
				if n in (['ExtremeSpeed', 'Hidden Power Fire', 'Hidden Power Ice', 'Leaf Blade', 'Stone Edge',
				 'Icicle Crash', 'Earthquake', 'Ice Shard', 'Sucker Punch', 'Surf', 'Megahorn', 'Return']):
					pM.pp -= 1
					return
				#Attacks with effects that affect players.
				elif n in (['Struggle']):
					p.curPoke.hp -= int(totalDamage / 2)
				elif n in (['Draco Meteor']):
					p.curPoke.spAttack *= 0.44
				elif n in (['Superpower']):
					p.curPoke.attack *= 0.66
					p.curPoke.defense *= 0.66
				elif n in (['Giga Drain']):
					p.curPoke.hp += int(totalDamage / 2)
					if p.curPoke.hp > p.curPoke.basehp:
						p.curPoke.hp = p.curPoke.basehp
				elif n in (['Volt Change', 'U-turn']):
					main.switchPokemon(p)
				elif n in (['Close Combat']):
					p.curPoke.spDefense *= 0.66
					p.curPoke.defense *= 0.66
				elif n in (['Hammer Arm']):
					p.curPoke.speed *= 0.66
				elif n in (['Brick Break']):
					o.reflect = 0
					o.screen = 0

				#Opponent hp check. If the opponent fainted, then no need to check additional effects. 
				if o.curPoke.hp <= 0:
					pM.pp -= 1
					return
				
				#Attacks with effects that affect opponent.
				if n in (['Fire Blast', 'Flamethrower', 'Fire Punch']):
					if random.randint(0, 99) in range(10) and not o.curPoke.status:
						o.curPoke.status = 'Burn'
				elif n in (['Ice Fang', 'Ice Beam', 'Ice Punch']):
					if random.randint(0, 99) in range(10) and not o.curPoke.status:
						p.curPoke.status = 'Ice'
						p.curPoke.ice = 3
				elif n in (['Acid Bomb']):
					o.curPoke.spDefense *= 0.44
				elif n in (['Night Burst']):
					if random.randint(0, 99) in range(40):
						o.curPoke.accuracy *= 0.66
				elif n in (['Focus Blast', 'Earth Power', 'Psychic', 'Energy Ball']):
					if random.randint(0, 99) in range(10):
						o.curPoke.spDefense *= 0.66
				elif n in (['Hurricane']):
					if random.randint(0, 99) in range(30) and not o.curPoke.status:
						o.curPoke.status = 'Confused'
						o.curPoke.confused = 3
				elif n in (['Crunch']):
					if random.randint(0, 99) in range(20):
						o.curPoke.defense *= 0.66

			#Attack did not hit.
			else:
				success = False

	if not success:
		print("But it failed!")

	pM.pp -= 1

	




