

class PokemonAction:
	def __init__(self, name, act_type, act_class, power, effect, priority):
		'''
		name: string- actions name
		act_type: string- what type attack belongs under
		act_class: physical or special 
		power: float- power of attack -> 0 if it is a status move
		priority: int- some moves have a +/- priority value
		effect: indirect effects
		'''

		self.name = name
		self.act_type = act_type
		self.act_class = act_class
		self.power = power
		self.effect = effect
		self.priority = priority


	def calculate():

		
