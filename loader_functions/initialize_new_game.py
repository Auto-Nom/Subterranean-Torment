"""
Initializer functions for starting a new game of Subterranean Torment
"""

import libtcodpy as libtcod

from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment
from components.equippable import Equippable

from entity import Entity
from equipment_slots import EquipmentSlots
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap
from render_functions import RenderOrder


def get_constants():
    window_title = "Subterranean Torment"

    screen_width = 80
    screen_height = 50

    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    max_monsters_per_room = 3
    max_items_per_room = 2

    colors = {
            'light_wall': libtcod.Color(0, 0, 150),
            'light_ground': libtcod.Color(50, 50, 250),
            'dark_wall': libtcod.Color(25, 25, 150),
            'dark_ground': libtcod.Color(75, 75, 250)
    }

    
    constants = {
            'window_title': window_title,
            'screen_width': screen_width,
            'screen_height': screen_height,
            'bar_width': bar_width,
            'panel_height': panel_height,
            'panel_y': panel_y,
            'message_x': message_x,
            'message_width': message_width,
            'message_height': message_height,
            'map_width': map_width,
            'map_height': map_height,
            'room_max_size': room_max_size,
            'room_min_size': room_min_size,
            'max_rooms': max_rooms,
            'fov_algorithm': fov_algorithm,
            'fov_light_walls': fov_light_walls,
            'fov_radius': fov_radius,
            'max_monsters_per_room': max_monsters_per_room,
            'max_items_per_room': max_items_per_room,
            'colors': colors
    }

    return constants


def get_game_variables(constants, race, role):
    
    player = create_player(race, role)

    entities = [player]

    game_map = GameMap(constants['map_width'], constants['map_height'])
    game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'], constants['map_width'], constants['map_height'], player, entities) 

    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])

    game_state = GameStates.PLAYERS_TURN

    return player, entities, game_map, message_log, game_state

def create_player(race, role):
    """
    Creates a player character with the chosen race and role
    """
    
    print(race + " " + role)
     
    fighter_component = Fighter(strength=10, agility=10, constitution=10, intelligence=10, cunning=10, base_str_acc=50, base_agi_acc=50, base_dodge=5, base_hp=100, base_hp_regen=1, base_spellpower=50, base_magic_res=5, base_crit_chance=5, base_insane_res=5, base_phys_res=5, base_damage=5, xp=0, base_accuracy_stat="strength")
    inventory_component = Inventory(26)
    level_component = Level()
    equipment_component = Equipment()
    player = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, inventory=inventory_component, level=level_component, equipment=equipment_component)
 
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, strength_bonus=0, agility_bonus=0, constitution_bonus=0, intelligence_bonus=0, cunning_bonus=0, max_hp_bonus=0, str_acc_bonus=0, agi_acc_bonus=0, dodge_bonus=0, hp_regen_bonus=0, spellpower_bonus=0, magic_res_bonus=0, crit_chance_bonus=2, insane_res_bonus=0, phys_res_bonus=0, damage_bonus=5, accuracy_stat="strength")
    dagger = Entity(0, 0, '-', libtcod.sky, 'Dagger', equippable=equippable_component)
    player.inventory.add_item(dagger)
    player.equipment.toggle_equip(dagger)

    return player


