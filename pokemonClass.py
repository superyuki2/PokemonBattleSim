

class Pokemon:
	def __init__(self, stats, types, mods, moveset):
		'''
		stats: dictionary with keys {hp, att, def, spa, spd, spe} and number values corresponding to power levels
		types: size-2 tuple - can either have 1 or two values
		mods: dictionary with keys {m_hp, m_att, m_def, m_spa, m_spd, m_spe} and values intialized to 1.  Act as a multiplier
			for stat changes due to power up moves or status ailments
		moveset: array of pokemon's 4 possible actions
		'''

		self.stats = stats
		self.type = types
		self.mods = {'m_hp', 1.0, 'm_att', 1.0, 'm_def', 1.0, 'm_spa', 1.0, 'm_spd', 1.0, 'm_spe', 1.0}
		self.moveset = moveset

	def pokemon_action(self, action):
		

	def update(self):



