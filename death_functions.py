"""
Death Functions for Subterranean Torment
"""

import libtcodpy as libtcod

from game_states import GameStates
from render_functions import RenderOrder
from game_messages import Message


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return Message('YOU DIED', libtcod.red), GameStates.PLAYER_DEAD

def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange) 

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message

def kill_boss(monster):
    death_message = Message('You killed {0}!'.format(monster.name.capitalize()), libtcod.flame) 

    monster.char = '%'
    monster.color = libtcod.darker_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message, GameStates.VICTORY


