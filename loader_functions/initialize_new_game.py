"""
Initializer functions for starting a new game of Subterranean Torment
"""

import libtcodpy as libtcod

from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment
from components.equippable import Equippable
from components.item import Item

from item_functions import cast_confuse, ranged_attack
from entity import Entity
from equipment_slots import EquipmentSlots
from game_messages import Message, MessageLog
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
    
    # Stats
    player_str = 10
    player_agi = 10
    player_con = 10
    player_int = 10
    player_cun = 10
    player_base_str_acc = 50
    player_base_agi_acc = 50
    player_base_dodge = 5
    player_base_hp = 100
    player_base_hp_regen = 1
    player_base_spellpower = 50
    player_base_magic_res = 5
    player_base_crit = 5
    player_base_insane_res = 5
    player_base_phys_res = 5
    player_base_damage = 5
    player_base_accuracy_stat = "strength"
    player_color = libtcod.white

    if race == 'Human':
        player_base_hp_regen -= 0.5
        player_base_damage += 1
    
    elif race == 'Orc':
        player_str += 2
        player_con += 1
        player_int -= 1
        player_cun -= 1
        player_base_dodge -= 2
        player_base_hp += 20
        player_base_magic_res += 5
        player_base_phys_res += 5
        player_color = libtcod.light_green

    elif race == 'Gnome':
        player_str -= 1
        player_con -= 2
        player_int += 1
        player_cun += 2
        player_base_dodge += 2
        player_base_hp -= 20
        player_base_insane_res += 1

    elif race == 'Dwarf':
        player_str += 1
        player_agi -= 1
        player_base_str_acc += 5
        player_base_spellpower -= 10
        player_base_phys_res += 2

    elif race == 'Elf':
        player_agi += 1
        player_int += 1
        player_base_agi_acc += 5
        player_base_dodge += 1
        player_base_hp -= 10
        player_base_spellpower += 5
        player_base_magic_res -= 1
        player_base_damage -= 1
        player_base_accuracy_stat = "agility"

    if role == 'Ranger':
        player_agi += 1
        player_con -= 1
        player_base_agi_acc += 5
        player_base_crit += 1
        player_base_phys_res -= 1
        player_base_accuracy_stat = "agility"

    elif role == 'Barbarian':
        player_str += 1
        player_con += 2
        player_int -= 1
        player_cun -= 1
        player_base_dodge -= 2
        player_base_hp += 10
        player_base_spellpower -= 15
        player_base_crit -= 2
        player_base_phys_res += 2
        player_base_accuracy_stat = "strength"

    elif role == 'Fighter':
        player_str += 1
        player_agi += 1
        player_base_str_acc += 5
        player_base_spellpower -= 10
        player_base_damage += 1
        player_base_accuracy_stat = "strength"

    elif role == 'Mage':
        player_str -= 1
        player_con -= 2
        player_int += 2
        player_base_str_acc -= 5
        player_base_agi_acc -= 5
        player_base_hp -= 10
        player_base_spellpower += 15
        player_base_damage -= 2
        player_base_accuracy_stat = "agility"

    elif role == 'Rogue':
        player_agi += 1
        player_con -= 1
        player_cun += 2
        player_base_str_acc += 5
        player_base_agi_acc += 5
        player_base_dodge += 2
        player_base_hp -= 10
        player_base_hp_regen -= 0.5
        player_base_crit += 3
        player_base_insane_res += 2
        player_base_accuracy_stat = "agility"


    fighter_component = Fighter(race, role, strength=player_str, agility=player_agi, constitution=player_con, intelligence=player_int, cunning=player_cun, base_str_acc=player_base_str_acc, base_agi_acc=player_base_agi_acc, base_dodge=player_base_dodge, base_hp=player_base_hp, base_hp_regen=player_base_hp_regen, base_spellpower=player_base_spellpower, base_magic_res=player_base_magic_res, base_crit_chance=player_base_crit, base_insane_res=player_base_insane_res, base_phys_res=player_base_phys_res, base_damage=player_base_damage, xp=0, base_accuracy_stat=player_base_accuracy_stat)
    inventory_component = Inventory(26)
    level_component = Level()
    equipment_component = Equipment()
    player = Entity(0, 0, '@', player_color, 'Player', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, inventory=inventory_component, level=level_component, equipment=equipment_component)
 

    # Equipment
    if race == 'Human':
        equippable_component = Equippable(EquipmentSlots.HEAD, phys_res_bonus=5)
        helm = Entity(0, 0, '^', libtcod.grey, 'Helm', equippable=equippable_component)
        player.inventory.add_item(helm)
        player.equipment.toggle_equip(helm)
    
    elif race == 'Orc':
        equippable_component = Equippable(EquipmentSlots.RING_FINGER_L,magic_res_bonus=5, damage_bonus=1, accuracy_stat="strength")
        ring_l = Entity(0, 0, 'o', libtcod.sky, 'Ring', equippable=equippable_component)
        player.inventory.add_item(ring_l)
        player.equipment.toggle_equip(ring_l)

        equippable_component = Equippable(EquipmentSlots.RING_FINGER_R,str_acc_bonus=5)
        ring_r = Entity(0, 0, 'o', libtcod.sky, 'Ring', equippable=equippable_component)
        player.inventory.add_item(ring_r)
        player.equipment.toggle_equip(ring_r)

    elif race == 'Gnome':
        equippable_component = Equippable(EquipmentSlots.ARMS, spellpower_bonus=5, phys_res_bonus=5)
        bracers = Entity(0, 0, '=', libtcod.dark_sepia, 'Bracers', equippable=equippable_component)
        player.inventory.add_item(bracers)
        player.equipment.toggle_equip(bracers)

    elif race == 'Dwarf':
        equippable_component = Equippable(EquipmentSlots.LEGS, constitution_bonus=1, phys_res_bonus=5)
        leggings = Entity(0, 0, '[', libtcod.darker_sepia, 'Leggings', equippable=equippable_component)
        player.inventory.add_item(leggings)
        player.equipment.toggle_equip(leggings)

    elif race == 'Elf':
        equippable_component = Equippable(EquipmentSlots.TORSO, dodge_bonus=3, phys_res_bonus=1)
        tunic = Entity(0, 0, ']', libtcod.sepia, 'Tunic', equippable=equippable_component)
        player.inventory.add_item(tunic)
        player.equipment.toggle_equip(tunic)

    if role == 'Ranger':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, agi_acc_bonus=2, crit_chance_bonus=1, damage_bonus=3, accuracy_stat="agility")
        arrow_component = Item(use_function=ranged_attack, targeting=True, targeting_message=Message('Left-click an enemy to target it, or right-click to cancel.', libtcod.light_cyan))
        bow = Entity(0, 0, ')', libtcod.brass, 'Bow', equippable=equippable_component, item=arrow_component)
        player.inventory.add_item(bow)
        player.equipment.toggle_equip(bow)

    elif role == 'Barbarian':
        equippable_component = Equippable(EquipmentSlots.FEET, magic_res_bonus=1, crit_chance_bonus=1, phys_res_bonus=3, damage_bonus=2, accuracy_stat="strength")
        boots = Entity(0, 0, 'l', libtcod.darker_sky, 'Boots', equippable=equippable_component)
        player.inventory.add_item(boots)
        player.equipment.toggle_equip(boots)

    elif role == 'Fighter':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, crit_chance_bonus=2, damage_bonus=5, accuracy_stat="strength")
        sword = Entity(0, 0, '/', libtcod.light_azure, 'Sword', equippable=equippable_component)
        player.inventory.add_item(sword)
        player.equipment.toggle_equip(sword)

    elif role == 'Mage':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, spellpower_bonus=5, insane_res_bonus=(-1), damage_bonus=1, accuracy_stat="agility")
        staff = Entity(0, 0, '\\', libtcod.brass, 'Staff', equippable=equippable_component)
        player.inventory.add_item(staff)
        player.equipment.toggle_equip(staff)

        item_component = Item(use_function=cast_confuse, targeting=True, targeting_message=Message('Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan))
        scroll = Entity(0, 0, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM, item=item_component)
        player.inventory.add_item(scroll)

    elif role == 'Rogue':
        equippable_component = Equippable(EquipmentSlots.NECK, dodge_bonus=5)
        amulet = Entity(0, 0, 'v', libtcod.dark_fuchsia, 'Amulet', equippable=equippable_component)
        player.inventory.add_item(amulet)
        player.equipment.toggle_equip(amulet)



    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, strength_bonus=0, agility_bonus=0, constitution_bonus=0, intelligence_bonus=0, cunning_bonus=0, max_hp_bonus=0, str_acc_bonus=0, agi_acc_bonus=0, dodge_bonus=0, hp_regen_bonus=0, spellpower_bonus=0, magic_res_bonus=0, crit_chance_bonus=2, insane_res_bonus=0, phys_res_bonus=0, damage_bonus=4, accuracy_stat="strength")
    dagger = Entity(0, 0, '-', libtcod.sky, 'Dagger', equippable=equippable_component)
    player.inventory.add_item(dagger)

    return player


