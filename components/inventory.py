"""
Inventory component for Subterranean Torment
"""

import libtcodpy as libtcod

from game_messages import Message
from components.item import Item
from item_functions import add_oil
from entity import Entity

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message': Message('You cannot carry any more, your inventory is full', libtcod.yellow)
            })

        else:
            results.append({
                'item_added': item,
                'message': Message('You pick up the {0}.'.format(item.name), libtcod.blue)
            })

            self.items.append(item)

        return results

    def use(self, item_entity, **kwargs):
        results = []

        item_component = item_entity.item

        if item_component.use_function is None:
            equippable_component = item_entity.equippable

            if equippable_component:
                results.append({'equip': item_entity})
            else:
                results.append({'message': Message('The {0} cannot be used'.format(item_entity.name), libtcod.yellow)})

        else:
            if item_component.targeting and not (kwargs.get('target_x') or kwargs.get('target_y')):
                results.append({'targeting': item_entity})
            else:
                kwargs = {**item_component.function_kwargs, **kwargs}
                item_use_results = item_component.use_function(self.owner, **kwargs)

                leftover = False
                for item_use_result in item_use_results:
                    if item_use_result.get('leftover_fuel'):
                        leftover = item_use_result.get('leftover_fuel')
                    if item_use_result.get('consumed'):
                        self.remove_item(item_entity)
                if leftover:
                    item_component = Item(use_function=add_oil, amount=leftover)
                    leftover_oil = Entity(self.owner.x, self.owner.y, '0', libtcod.amber, "Oil: {0}".format(leftover), item=item_component)
                    self.owner.inventory.add_item(leftover_oil)

                results.extend(item_use_results)

        return results

    def activate(self, item_entity, **kwargs):
        results = []

        item_component = item_entity.item

        if item_component.use_function is None:
            results.append({'message': Message('The {0} cannot be used'.format(item_entity.name), libtcod.yellow)})

        else:
            if item_component.targeting and not (kwargs.get('target_x') or kwargs.get('target_y')):
                results.append({'targeting': item_entity})
            else:
                kwargs = {**item_component.function_kwargs, **kwargs}
                item_use_results = item_component.use_function(self.owner, **kwargs)

                for item_use_result in item_use_results:
                    if item_use_result.get('consumed'):
                        self.remove_item(item_entity)

                results.extend(item_use_results)

        return results

    def equip(self, item_entity):
        results = []

        item_component = item_entity.item

        equippable_component = item_entity.equippable

        if equippable_component:
            results.append({'equip': item_entity})
        else:
            results.append({'message': Message('The {0} is not an equippable item'.format(item_entity.name), libtcod.yellow)})

        return results

    def remove_item(self, item):
        self.items.remove(item)

    def drop_item(self, item):
        results = []

        if item in (self.owner.equipment.main_hand, self.owner.equipment.off_hand, self.owner.equipment.head, self.owner.equipment.neck, self.owner.equipment.ring_finger_l, self.owner.equipment.ring_finger_r, self.owner.equipment.arms, self.owner.equipment.torso, self.owner.equipment.legs, self.owner.equipment.feet):
            self.owner.equipment.toggle_equip(item)

        item.x = self.owner.x
        item.y = self.owner.y

        self.remove_item(item)
        results.append({'item_dropped': item, 'message': Message('You dropped the {0}.'.format(item.name), libtcod.yellow)})

        return results


