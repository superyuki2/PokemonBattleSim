#The Pokemon Class
class Pokemon:
	def __init__(self, name, attribute1, attribute2, hp, attack, \
		defense, spAttack, spDefense, speed, moves):
		#Strings
		self.name = name
		self.attribute1 = attribute1
		self.attribute2 = attribute2
		self.status = None
		#base stats, ints
		self.basehp = hp
		self.baseattack = attack
		self.basedefense = defense
		self.basespAttack = spAttack
		self.basespDefense = spDefense
		self.basespeed = speed
		#modified stats. used in actual battles
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.spAttack = spAttack
		self.spDefense = spDefense
		self.speed = speed

		self.moves = moves #set of moves, length 4 Move array
		#self.items = items mmmm maybe later
		#Booleans
		self.sub = False #Substitute existence
		self.protect = False #Protect

#The Move Class
class Move:
	def __init__(self, name, attribute, damage, effect, phys, acc, pp):
		#Strings
		self.name = name
		self.attribute = attribute
		#Ints
		self.damage = damage
		self.acc = acc
		self.pp = pp
		#Boolean
		self.effect = effect
		self.phys = phys #physical attack - True, special attack - False, neither - None
