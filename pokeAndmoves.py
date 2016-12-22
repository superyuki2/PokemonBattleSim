import pokemon

#All pokemon and moves are defined here.

#0.66 for decrease, 1.5 for increase
#All moves have effect
allMoves = [
pokemon.Move('Draco Meteor', 'Dragon', 130, False, 90, 5),
#spAtt 2 stages down
pokemon.Move('Fire Blast', 'Fire', 110, False, 85, 5),
#10% chance of burn
pokemon.Move('Superpower', 'Fighting', 120, True, 100, 5),
#att, def 1 stage down
pokemon.Move('ExtremeSpeed', 'Normal', 80, True, 100, 5),
#priority

pokemon.Move('Pain Split', 'Normal', 0, None, 100, 20),
#add hp together and distribute numerically evenly
pokemon.Move('Will-O-Wisp', 'Fire', 0, None, 85, 15),
#Burn
pokemon.Move('Night Shade', 'Ghost', 0, None, 100, 15),
#always 50 damage
pokemon.Move('Confuse Ray', 'Ghost', 0, None, 100, 10),
#confuse

pokemon.Move('Spikes', 'Ground', 0, None, 100, 20),
#1/8 of basehp damage per layer, 3 layers
pokemon.Move('Giga Drain', 'Grass', 75, False, 100, 10),
#gain back 1/2 of numerical damage given
pokemon.Move('Hidden Power Fire', 'Fire', 60, False, 100, 15),
#10% chance of burn
pokemon.Move('Rest', 'Psychic', 0, None, 100, 10),
#Falls asleep, heals. wake up will be random

pokemon.Move('Light Screen', 'Psychic', 0, None, 100, 30),
#1/2 any spAtt
pokemon.Move('Reflect', 'Psychic', 0, None, 100, 20),
#1/2 ant att
pokemon.Move('Hidden Power Fire', 'Fire', 60, False, 100, 15),
#10% chance of burn
pokemon.Move('Volt Change', 'Electric', 70, False, 100, 20),
#forced switch right after

pokemon.Move('Substitute', 'Normal', 0, None, 100, 10),
#takes 1/4 and make substitute. doesn't work if hp < 1/4 base
pokemon.Move('Thunder Wave', 'Electric', 0, None, 90, 20),
#Paralyze
pokemon.Move('Acid Bomb', 'Fire', 40, False, 100, 20),
#lower spDef by 2 stages
pokemon.Move('U-turn', 'Bug', 70, True, 100, 20),
#forced switch right after

pokemon.Move('Swords Dance', 'Normal', 0, None, 100, 20),
#att up by 2 stages
pokemon.Move('Close Combat', 'Fighting', 120, True, 100, 5),
#lower def and spDef by 1 stage
pokemon.Move('Stone Edge', 'Rock', 100, True, 80, 5),
#(critical) double the attack damage by 1.5, 30% chance
pokemon.Move('Leaf Blade', 'Grass', 90, True, 100, 15),
#critical, x1.5 30% chance

pokemon.Move('Earthquake', 'Ground', 100, True, 100, 10),
#Nothing
pokemon.Move('Slack Off', 'Normal', 0, None, 100, 10),
#1/2 base hp recover
pokemon.Move('Stealth Rock', 'Rock', 100, None, 80, 5),
#1/8 of basehp damage x typeEffect multiplier against rock
pokemon.Move('Ice Fang', 'Ice', 65, True, 95, 15),
#10% chance of ice

pokemon.Move('Ice Shard', 'Ice', 40, True, 100, 30),
#priority
pokemon.Move('Icicle Crash', 'Ice', 85, True, 90, 10),
#critical x1.5, 30% chance
pokemon.Move('Earthquake', 'Ground', 100, True, 100, 10),
#Nothing
pokemon.Move('Stone Edge', 'Rock', 100, True, 80, 5),
#(critical) double the attack damage by 1.5, 30% chance

pokemon.Move('Night Burst', 'Dark', 85, False, 95, 10),
#lower accuracy by 1 stage, 40% chance
pokemon.Move('Hidden Power Ice', 'Ice', 60, False, 100, 15),
#10% chance of Ice
pokemon.Move('Focus Blast', 'Fighting', 120, False, 70, 5),
#lower spD by 1 stage, 10% chance
pokemon.Move('Sucker Punch', 'Dark', 70, True, 100, 5),
#has priority, but fails if opponent chose a move that gives damage

pokemon.Move('Hurricane', 'Flying', 110, False, 70, 10),
#confuse 30% chance
pokemon.Move('Hammer Arm', 'Fighting', 100, True, 90, 10),
#Lower user speed by 1 stage
pokemon.Move('Rain Dance', 'Water', 0, None, 100, 5),
#weather change to rain
pokemon.Move('Taunt', 'Dark', 0, None, 100, 20),
#opponent can only attack for 5 turns, disappears if switched out

pokemon.Move('Toxic Spikes', 'Poison', 0, None, 100, 20),
#1 layer - normal poison, 2 layers - toxic
pokemon.Move('Earth Power', 'Ground', 90, False, 100, 10),
#10% lower spDef
pokemon.Move('Flamethrower', 'Fire', 90, False, 100, 15),
#10% burn
pokemon.Move('Ice Beam', 'Ice', 90, False, 100, 10),
#10% ice

pokemon.Move('Surf', 'Water', 90, False, 100, 15),
#Nothing
pokemon.Move('Fire Blast', 'Fire', 110, False, 85, 5),
#10% chance of burn
pokemon.Move('Psychic', 'Psychic', 90, False, 100, 10),
#Lower spDef 10% chance
pokemon.Move('Energy Ball', 'Grass', 90, False, 100, 10),
#Lower spDef 10% chance


pokemon.Move('Curse', 'Ghost', 0, None, 100, 10),
#att def 1 stage up, spd one stage down
pokemon.Move('Return', 'Normal', 102, True, 100, 20),
#Nothing
pokemon.Move('Fire Punch', 'Fire', 75, True, 100, 15),
#burn 10% chance
pokemon.Move('Rest', 'Psychic', 0, None, 100, 10),
#Falls asleep, heals. wake up will be random

pokemon.Move('Megahorn', 'Bug', 120, True, 85, 10),
#Nothing
pokemon.Move('Close Combat', 'Fighting', 120, True, 100, 5),
#lower def and spDef by 1 stage
pokemon.Move('Stone Edge', 'Rock', 100, True, 80, 5),
#(critical) double the attack damage by 1.5, 30% chance
pokemon.Move('Facade', 'Normal', 70, True, 100, 20),
#damage x2 if paralyze, burn, poison, toxic

pokemon.Move('Close Combat', 'Fighting', 120, True, 100, 5),
#lower def and spDef by 1 stage
pokemon.Move('ExtremeSpeed', 'Normal', 80, True, 100, 5),
#priority
pokemon.Move('Crunch', 'Dark', 80, True, 100, 15),
#lower def 20% chance
pokemon.Move('Ice Punch', 'Ice', 75, True, 100, 15),
#10% ice

pokemon.Move('Swords Dance', 'Normal', 0, None, 100, 20),
#att up by 2 stages
pokemon.Move('Sucker Punch', 'Dark', 70, True, 100, 5),
#has priority, but fails if opponent chose a move that gives damage
pokemon.Move('Substitute', 'Normal', 0, None, 100, 10),
#takes 1/4 and make substitute. doesn't work if hp < 1/4 base
pokemon.Move('Brick Break', 'Fighting', 75, True, 100, 15),
#breaks light screen or reflect


]

# def __init__(self, name, attribute, damage, phys, acc, PP):

allPokemon = [
pokemon.Pokemon('Dragonite', 'Dragon', 'Flying', 151, 197, 95, 163, 100, 81, allMoves[0:4]),
pokemon.Pokemon('Dusclops', 'Ghost', None, 147, 70, 150, 60, 174, 26, allMoves[4:8]),
pokemon.Pokemon('Roserade', 'Grass', 'Poison', 167, 70, 95, 125, 139, 90, allMoves[8:12]),
pokemon.Pokemon('Magnezone', 'Electric', 'Steel', 177, 70, 94, 130, 130, 60, allMoves[12:16]),
pokemon.Pokemon('Eelektross', 'Electric', None, 192, 115, 81, 168, 80, 50, allMoves[16:20]),
pokemon.Pokemon('Virizion', 'Grass', 'Fighting', 152, 153, 72, 90, 129, 171, allMoves[20:24]),
pokemon.Pokemon('Hippowdon', 'Ground', None, 215, 112, 181, 68, 73, 47, allMoves[24:28]),
pokemon.Pokemon('Mamoswine', 'Ice', 'Ground', 171, 193, 80, 70, 60, 143, allMoves[28:32]),
pokemon.Pokemon('Zoroark', 'Dark', None, 120, 106, 60, 183, 60, 168, allMoves[32:36]),
pokemon.Pokemon('Tornadus', 'Flying', None, 139, 115, 70, 188, 80, 174, allMoves[36:40]),
pokemon.Pokemon('Nidoqueen', 'Ground', 'Poison', 197, 82, 150, 75, 86, 76, allMoves[40:44]),
pokemon.Pokemon('Slowbro', 'Water', 'Psychic', 202, 75, 111, 163, 80, 30, allMoves[44:48]),
pokemon.Pokemon('Snorlax', 'Normal', None, 250, 110, 91, 65, 164, 30, allMoves[48:52]),
pokemon.Pokemon('Heracross', 'Bug', 'Fighting', 144, 185, 75, 40, 95, 148, allMoves[52:56]),
pokemon.Pokemon('Lucario', 'Fighting', 'Steel', 131, 173, 70, 115, 70, 153, allMoves[56:60]),
pokemon.Pokemon('Bisharp', 'Dark', 'Steel', 172, 188, 101, 60, 70, 70, allMoves[60:64]),

]

# def __init__(self, name, attribute1, attribute2, hp, attack, \
#		defense, spAttack, spDefense, speed, moves):


