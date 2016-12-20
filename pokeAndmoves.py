import pokemon

#All pokemon and moves are defined here.

allMoves = [pokemon.Move('Draco Meteor', 'Dragon', 130, True, False, 90, 5),
pokemon.Move('Fire Blast', 'Fire', 110, True, False, 85, 5),
pokemon.Move('Superpower', 'Fighting', 120, True, True, 100, 5),
pokemon.Move('ExtremeSpeed', 'Normal', 80, True, True, 100, 5),

pokemon.Move('Pain Split', 'Normal', 0, True, None, 100, 20),
pokemon.Move('Will-O-Wisp', 'Fire', 0, True, None, 85, 15),
pokemon.Move('Night Shade', 'Ghost', 0, True, None, 100, 15),
pokemon.Move('Confuse Ray', 'Ghost', 0, True, None, 100, 10),

pokemon.Move('Spikes', 'Ground', 0, True, None, 100, 20),
pokemon.Move('Giga Drain', 'Grass', 75, True, False, 100, 10),
pokemon.Move('Hidden Power Fire', 'Fire', 60, False, False, 100, 15),
pokemon.Move('Rest', 'Psychic', 0, True, None, 100, 10),

pokemon.Move('Light Screen', 'Psychic', 0, True, None, 100, 30),
pokemon.Move('Reflect', 'Psychic', 0, True, None, 100, 20),
pokemon.Move('Hidden Power Fire', 'Fire', 60, False, False, 100, 15),
pokemon.Move('Volt Change', 'Electric', 70, True, False, 100, 20),

pokemon.Move('Substitute', 'Normal', 0, True, None, 100, 10),
pokemon.Move('Thunder Wave', 'Electric', 0, True, None, 90, 20),
pokemon.Move('Acid Bomb', 'Fire', 40, True, False, 100, 20),
pokemon.Move('U-turn', 'Bug', 70, True, True, 100, 20),

pokemon.Move('Swords Dance', 'Normal', 0, True, None, 100, 20),
pokemon.Move('Close Combat', 'Fighting', 120, True, True, 100, 5),
pokemon.Move('Stone Edge', 'Rock', 100, True, True, 80, 5),
pokemon.Move('Leaf Blade', 'Grass', 90, True, True, 100, 15),

]

# def __init__(self, name, attribute, damage, effect, phys, acc, PP):

allPokemon = [pokemon.Pokemon('Dragonite', 'Dragon', 'Flying', 151, 197, 95, 163, 100, 81, allMoves[0:4]),
pokemon.Pokemon('Dusclops', 'Ghost', None, 147, 70, 150, 60, 174, 26, allMoves[4:8]),
pokemon.Pokemon('Roserade', 'Grass', 'Poison', 167, 70, 95, 125, 139, 90, allMoves[8:12]),
pokemon.Pokemon('Magnezone', 'Electric', 'Steel', 177, 70, 94, 130, 130, 60, allMoves[12:16]),
pokemon.Pokemon('Eelektross', 'Electric', None, 192, 115, 81, 168, 80, 50, allMoves[16:20]),
pokemon.Pokemon('Virizion', 'Grass', 'Fighting', 152, 153, 72, 90, 129, 171, allMoves[20:24])

]

# def __init__(self, name, attribute1, attribute2, status, hp, attack, \
#		defense, spAttack, spDefense, speed, moves):

# Hippowdon @ Leftovers 
# Trait: Sand Stream 
# EVs: 252 HP / 252 Def / 4 SDef 
# Impish Nature 
# - Earthquake 
# - Slack Off 
# - Stealth Rock 
# - Ice Fang 

# Mamoswine @ Life Orb 
# Trait: Snow Cloak 
# EVs: 4 HP / 252 Atk / 252 Spd 
# Adamant Nature 
# - Ice Shard 
# - Icicle Crash 
# - Earthquake 
# - Stone Edge 

# Zoroark @ Life Orb 
# Trait: 
# EVs: 4 Atk / 252 SAtk / 252 Spd 
# Naive Nature 
# - Night Burst 
# - Hidden Power [Ice] 
# - Focus Blast 
# - Sucker Punch 

# Tornadus @ Life Orb 
# Trait: Prankster 
# EVs: 4 Atk / 252 SAtk / 252 Spd 
# Naive Nature 
# - Hurricane 
# - Hammer Arm 
# - Rain Dance 
# - Taunt 
