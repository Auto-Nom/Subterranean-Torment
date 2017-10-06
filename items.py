"""
Items for Subterranean Torment
"""

import libtcodpy as libtcod

from render_functions import RenderOrder
from game_messages import Message
from entity import Entity

from components.item import Item
from components.equipment import EquipmentSlots
from components.equippable import Equippable

from random_utils import random_choice_from_dict, from_dungeon_level
from item_functions import heal, cast_lightning, cast_fireball, cast_confuse, add_oil, heal_insanity

def choose_item(x, y, dungeon_level):
    item_chances = {
        'healing_potion': 35,
        'oil': 30,
        'laudanum': from_dungeon_level([[30, 2], [40, 4], [50, 6]], dungeon_level),
        'sword': from_dungeon_level([[10, 4]], dungeon_level),
        'shield': from_dungeon_level([[15, 8]], dungeon_level),
        'helmet': from_dungeon_level([[10, 4]], dungeon_level),
        'necklace': from_dungeon_level([[10, 2]], dungeon_level),
        'copper_ring': from_dungeon_level([[10, 3]], dungeon_level),
        'iron_ring': from_dungeon_level([[10, 5]], dungeon_level),
        'bracer': from_dungeon_level([[10, 6]], dungeon_level),
        'breastplate': from_dungeon_level([[10, 6]], dungeon_level),
        'leggings': from_dungeon_level([[10, 3]], dungeon_level),
        'boots': from_dungeon_level([[10, 5]], dungeon_level),
        'lightning_scroll': from_dungeon_level([[25, 4]], dungeon_level),
        'fireball_scroll': from_dungeon_level([[25, 6]], dungeon_level),
        'confusion_scroll': from_dungeon_level([[10, 2]], dungeon_level)
    }


    item_choice = random_choice_from_dict(item_chances)

    if item_choice == 'healing_potion':
        item_component = Item(use_function=heal, amount=40)
        item = Entity(x, y, '!', libtcod.purple, 'Healing Potion', render_order=RenderOrder.ITEM, item=item_component)
    elif item_choice == 'oil':
        item_component = Item(use_function=add_oil, amount=50)
        item = Entity(x, y, '0', libtcod.amber, 'Oil: 50', render_order=RenderOrder.ITEM, item=item_component)
    elif item_choice == 'laudanum':
        item_component = Item(use_function=heal_insanity, amount=30)
        item = Entity(x, y, 'i', libtcod.dark_sky, 'Laudanum', render_order=RenderOrder.ITEM, item=item_component)

    elif item_choice == 'sword':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, str_acc_bonus=5, crit_chance_bonus=1, damage_bonus=10, accuracy_stat="strength")
        item = Entity(x, y, '/', libtcod.sky, 'Sword', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'shield':
        equippable_component = Equippable(EquipmentSlots.OFF_HAND, magic_res_bonus=5, phys_res_bonus=10, damage_bonus=1, accuracy_stat="strength")
        item = Entity(x, y, '(', libtcod.darker_orange, 'Shield', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'helmet':
        equippable_component = Equippable(EquipmentSlots.HEAD, intelligence_bonus=1, cunning_bonus=1)
        item = Entity(x, y, '^', libtcod.grey, 'Helmet', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'necklace':
        equippable_component = Equippable(EquipmentSlots.NECK, spellpower_bonus=10, dodge_bonus=5)
        item = Entity(x, y, 'v', libtcod.light_blue, 'Necklace', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'copper_ring':
        equippable_component = Equippable(EquipmentSlots.RING_FINGER_L, cunning_bonus=1, agi_acc_bonus=5)
        item = Entity(x, y, 'o', libtcod.copper, 'Copper Ring', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'iron_ring':
        equippable_component = Equippable(EquipmentSlots.RING_FINGER_R, constitution_bonus=1, str_acc_bonus=5)
        item = Entity(x, y, 'o', libtcod.dark_grey, 'Iron Ring', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'bracer':
        equippable_component = Equippable(EquipmentSlots.ARMS, agility_bonus=1, phys_res_bonus=5)
        item = Entity(x, y, '=', libtcod.dark_sepia, 'Bracer', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'breastplate':
        equippable_component = Equippable(EquipmentSlots.TORSO, constitution_bonus=2, max_hp_bonus=25, dodge_bonus=-5, phys_res_bonus=5)
        item = Entity(x, y, '[', libtcod.dark_grey, 'Breastplate', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'leggings':
        equippable_component = Equippable(EquipmentSlots.LEGS, magic_res_bonus=5, crit_chance_bonus=5)
        item = Entity(x, y, ']', libtcod.light_sepia, 'Leggings', render_order=RenderOrder.ITEM, equippable=equippable_component)
    elif item_choice == 'boots':
        equippable_component = Equippable(EquipmentSlots.FEET, insane_res_bonus=5, max_hp_bonus=10)
        item = Entity(x, y, 'l', libtcod.darker_grey, 'Boots', render_order=RenderOrder.ITEM, equippable=equippable_component)

    elif item_choice == 'fireball_scroll':
        item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message('Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan), damage=25, radius=3)
        item = Entity(x, y, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM, item=item_component)
    elif item_choice == 'confusion_scroll':
        item_component = Item(use_function=cast_confuse, targeting=True, targeting_message=Message('Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan))
        item = Entity(x, y, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM, item=item_component)
    elif item_choice == 'lightning_scroll':
        item_component = Item(use_function=cast_lightning, damage=40, maximum_range=5)
        item = Entity(x, y, '#', libtcod.yellow, 'Lightning Scroll', render_order=RenderOrder.ITEM, item=item_component)

    return item


