#The Pokemon Class
class Pokemon:
	def __init__(self, name, attribute1, attribute2, status, hp, attack, \
		defense, spAttack, spDefense, speed, moves):
		#Strings
		self.name = name
		self.attribute1 = attribute1
		self.attribute2 = attribute2
		self.status = status
		#original stats, ints
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.spAttack = spAttack
		self.spDefense = spDefense
		self.speed = speed
		#set of moves, length 4 Move array
		self.moves = moves
		#self.items = items mmmm maybe later

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
		self.phys = phys #physical attack - True, special attack - False
