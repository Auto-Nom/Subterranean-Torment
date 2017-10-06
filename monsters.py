"""
Monsters for Subterranean Torment
"""

import libtcodpy as libtcod

from render_functions import RenderOrder
from entity import Entity

from components.fighter import Fighter
from components.ai import BasicMonster

from random_utils import from_dungeon_level, random_choice_from_dict

def choose_monster(x, y, dungeon_level):

    monster_chances = {
        'kobold': 80,
        'goblin': from_dungeon_level([[15, 2], [25, 4], [40, 6]], dungeon_level),
        'ogre': from_dungeon_level([[10, 3], [30, 5], [60, 7]], dungeon_level),
        'troll': from_dungeon_level([[5, 5], [10, 7], [20, 9]], dungeon_level)
    }

    monster_choice = random_choice_from_dict(monster_chances)

    if monster_choice == 'kobold':
        fighter_component = Fighter('Kobold', 'Monster', strength=8, agility=8, constitution=8, intelligence=8, cunning=8, base_hp=20, base_hp_regen=0, base_spellpower=5, base_damage=10, xp=35)
        ai_component = BasicMonster()

        monster = Entity(x, y, 'k', libtcod.dark_chartreuse, 'Kobold', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
    
    elif monster_choice == 'goblin':
        fighter_component = Fighter('Goblin', 'Monster', strength=10, agility=10, constitution=8, intelligence=8, cunning=8, base_hp=25, base_hp_regen=0, base_spellpower=5, base_damage=15, xp=45)
        ai_component = BasicMonster()

        monster = Entity(x, y, 'g', libtcod.desaturated_green, 'Goblin', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)

    elif monster_choice == 'ogre':
        fighter_component = Fighter('Ogre', 'Monster', strength=10, agility=10, constitution=10, intelligence=8, cunning=8, base_hp=30, base_spellpower=10, base_damage=20, xp=100)
        ai_component = BasicMonster()
        monster = Entity(x, y, 'O', libtcod.darker_green, 'Ogre', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)

    elif monster_choice == 'troll':
        fighter_component = Fighter('Troll', 'Monster', strength=12, agility=12, constitution=12, intelligence=10, cunning=10, base_hp=40, base_spellpower=10, base_damage=25, xp=150)
        ai_component = BasicMonster()
        monster = Entity(x, y, 'T', libtcod.darkest_green, 'Troll', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
    return monster


