"""
Item functions for Subterranean Torment
"""

import libtcodpy as libtcod

from entity import Entity

from game_messages import Message
from components.ai import ConfusedMonster
from components.item import Item

def heal(*args, **kwargs):
    """
    Heals the entity by a certain amount
    """
    entity = args[0]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at full health', libtcod.yellow)})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('Your wounds start to feel better!', libtcod.green)})

    return results

def add_oil(*args, **kwargs):
    """
    Adds oil to the lantern
    """
    entity = args[0]
    amount = kwargs.get('amount')

    results = []

    if entity.lantern.fuel == entity.lantern.max_fuel:
        results.append({'consumed': False, 'message': Message('The lantern is already full', libtcod.dark_amber)})
    else:
        results.extend(entity.lantern.add_fuel(amount))
        results.append({'consumed': True, 'message': Message('Fuel was succesfully added to the lantern')})

    return results

def heal_insanity(*args, **kwargs):
    """
    Decreases insanity level
    """
    entity = args[0]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.insanity == 0:
        results.append({'consumed':False, 'message': Message('You are perfectly sane')})
    else:
        entity.fighter.decrease_insanity(amount)
        results.append({'consumed': True, 'message': Message('Your mind starts to clear', libtcod.light_sky)})

    return results

def ranged_attack(*args, **kwargs):
    caster = args[0]
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'message': Message('You cannot target a tile outside your field of view', libtcod.yellow)})
        return results

    for entity in entities:
        if entity.x == target_x and entity.y == target_y and entity.ai:
            results.append({'used': True, 'message': Message('You make a ranged attack on the {0}'.format(entity.name), libtcod.light_green)})
            results.extend(caster.fighter.attack(entity, caster.fighter.accuracy_stat))
            break
    
    else:
        results.append({'message': Message('There is no targetable enemy at that location.', libtcod.yellow)})

    return results


def cast_lightning(*args, **kwargs):
    """
    A lightning bolt strikes the nearest visible enemy within a certain range
    """
    caster = args[0]
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    damage = kwargs.get('damage')
    maximum_range = kwargs.get('maximum_range')
    
    damage *= (caster.fighter.spellpower/100)

    results = []

    target = None
    closest_distance = maximum_range + 1

    for entity in entities:
        if entity.fighter and entity != caster and libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
            distance = caster.distance_to(entity)

            if distance < closest_distance:
                target = entity
                closest_distance = distance

    if target:
        results.append({'consumed': True, 'target': target, 'message': Message('A lightning bolt strikes the {0} with a loud thunder! The damage is {1}'.format(target.name, damage))})
        results.extend(target.fighter.take_damage(damage, physical=False, magical=True))
    else:
        results.append({'consumed': False, 'target': None, 'message': Message('No enemy is close enough to strike.', libtcod.red)})

    return results

def cast_fireball(*args, **kwargs):
    """
    A fireball explodes with a specified radius, centered on a tile within the fov
    """
    caster = args[0]
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    damage = kwargs.get('damage')
    radius = kwargs.get('radius')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    damage *= (caster.fighter.spellpower/100)

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view.', libtcod.yellow)})
        return results

    results.append({'consumed': True, 'message': Message('The fireball explodes, burning everything within {0} tiles!'.format(radius), libtcod.orange)})

    for entity in entities:
        if entity.distance(target_x, target_y) <= radius and entity.fighter:
            results.append({'message': Message('The {0} gets burned for {1} hitpoints.'.format(entity.name, damage), libtcod.orange)})
            results.extend(entity.fighter.take_damage(damage, physical=False, magical=True))

    return results

def cast_confuse(*args, **kwargs):
    """
    A spell that causes the target to be confused for a few turns
    """
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view', libtcod.yellow)})
        return results

    for entity in entities:
        if entity.x == target_x and entity.y == target_y and entity.ai:
            confused_ai = ConfusedMonster(entity.ai, 10)

            confused_ai.owner = entity
            entity.ai = confused_ai

            results.append({'consumed': True, 'message': Message('The eyes of the {0} look vacant, as it starts to stumble around!'.format(entity.name), libtcod.light_green)})

            break
    
    else:
        results.append({'consumed': False, 'message': Message('There is no targetable enemy at that location.', libtcod.yellow)})

    return results


