"""
Lantern component for Subterranean Torment
"""

import libtcodpy as libtcod

from entity import Entity
from components.item import Item
from item_functions import add_oil

from game_messages import Message

class Lantern:
    def __init__(self, max_brightness=10, brightness=10, max_fuel=100):
        self.max_brightness = max_brightness
        self.brightness = brightness
        self.max_fuel = max_fuel
        self.fuel = max_fuel

    def increase_brightness(self, amount):
        results = []
        
        if self.fuel == 0:
            results.append({'message': Message('The lantern has no fuel', libtcod.dark_amber)})
            return results

        self.brightness = round(self.brightness + amount)
        if self.brightness >= self.max_brightness:
            self.brightness = self.max_brightness
            results.append({'message': Message('The lantern is at max brightness.', libtcod.light_yellow), 'brightness': self.brightness})
        else:
            results.append({'message': Message("The lantern's brightness increases to {0}.".format(self.brightness), libtcod.yellow),'brightness': self.brightness})
        
        return results

    def decrease_brightness(self, amount):
        results = []

        self.brightness = round(self.brightness - amount)
        if self.brightness <= 0:
            self.brightness = 0
            results.append({'message': Message('The lantern is off.', libtcod.darker_yellow), 'brightness': self.brightness})
        else:
            results.append({'message': Message("The lantern's brightness decreases to {0}.".format(self.brightness), libtcod.dark_yellow),'brightness': self.brightness})
        
        return results

    def add_fuel(self, amount):
        results = []

        self.fuel = round((self.fuel + amount), 2)
        if self.fuel >= self.max_fuel:
            leftover = round((self.fuel - self.max_fuel), 2)
            self.fuel = self.max_fuel
            results.append({'message': Message('The lantern cannot hold any more fuel.', libtcod.dark_amber)})
            if leftover:
                results.append({'message': Message('{0} fuel was left over'.format(leftover), libtcod.dark_amber)})
                item_component = Item(use_function=add_oil, amount=leftover)
                leftover_oil = Entity(0, 0, '0', libtcod.amber, "Oil: {0}".format(leftover), item=item_component)
                self.owner.inventory.add_item(leftover_oil)
        else:
            results.append({'message': Message('The lantern now has {0} fuel.'.format(self.fuel), libtcod.amber)})
        
        return results

    def decrease_fuel(self, amount):
        results = []

        self.fuel = round((self.fuel - amount), 2)
        if self.fuel <= 0:
            self.fuel = 0
            self.brightness = 0
            results.append({'message': Message('The lantern has run out of fuel.', libtcod.darker_yellow), 'brightness': self.brightness})
        #else:
        #    results.append({'message': Message("The lantern's fuel decreases to {0}.".format(self.fuel))})
        
        return results


