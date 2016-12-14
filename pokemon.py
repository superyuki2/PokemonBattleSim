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
		#change in stats, actually used in battle
		self.curA = attack
		self.curD = defense
		self.curSA = spAttack
		self.curSD = spDefense
		self.curS = speed
		#set of moves, length 4 Move array
		self.moves = moves
		#self.items = items mmmm maybe later

#The Move Class
class Move:
	def __init__(self, name, attribute, damage, effect):
		#Strings
		self.name = name
		self.attribute = attribute
		#Ints
		self.damage = damage
		#Boolean
		self.effect = effect