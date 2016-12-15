import pokemon

#All pokemon and moves are defined here.

# Dragonite @ Life Orb 
# Trait: Inner Focus 
# EVs: 252 Atk / 252 SAtk / 4 Spd 
# Rash Nature 
# - Draco Meteor 
# - Fire Blast 
# - Superpower 
# - ExtremeSpeed 

# 	def __init__(self, name, attribute1, attribute2, status, hp, attack, \
#		defense, spAttack, spDefense, speed, moves):
# def __init__(self, name, attribute, damage, effect, phys, acc, PP):

allMoves = [pokemon.Move('Draco Meteor', 'Dragon', 130, True, False, 90, 5),
pokemon.Move('Fire Blast', 'Fire', 110, True, False, 85, 5),
pokemon.Move('Superpower', 'Fighting', 120, True, True, 100, 5),
pokemon.Move('ExtremeSpeed', 'Normal', 80, True, True, 100, 5),
]

allPokemon = [pokemon.Pokemon('Dragonite', 'Dragon', 'Flying', None, 292, 197, 95, 163, 100, 81, allMoves[0:4])
]

# Dusclops @ Eviolite 
# Trait: 
# EVs: 252 HP / 80 Def / 176 SDef 
# Calm Nature 
# - Pain Split 
# - Will-O-Wisp 
# - Night Shade 
# - Confuse Ray 

# Roserade @ Leftovers 
# Trait: Natural Cure 
# EVs: 252 HP / 120 Def / 136 SDef 
# Calm Nature 
# - Spikes 
# - Giga Drain 
# - Hidden Power [Fire] 
# - Rest 

# Magnezone @ Light Clay 
# Trait: Magnet Pull 
# EVs: 252 HP / 96 Def / 162 SDef 
# Calm Nature 
# - Light Screen 
# - Reflect 
# - Hidden Power [Fire] 
# - Volt Change 

# Eelektross @ Leftovers 
# Trait: 
# EVs: 252 HP / 4 Def / 252 SAtk 
# Quiet Nature 
# - Substitute 
# - Thunder Wave 
# - Acid Bomb 
# - U-turn 

# Virizion @ Life Orb 
# Trait: 
# EVs: 4 HP / 252 Atk / 252 Spd 
# Jolly Nature 
# - Swords Dance 
# - Close Combat 
# - Stone Edge 
# - Leaf Blade 
