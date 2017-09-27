"""
Game map for Subterranean Torment
"""

import libtcodpy as libtcod
from random import randint

from map_objects.tile import Tile
from map_objects.rectangle import Rect
from render_functions import RenderOrder
from game_messages import Message
from entity import Entity

from components.fighter import Fighter
from components.ai import BasicMonster, BossMonster
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.item import Item
from components.stairs import Stairs

from monsters import choose_monster
from items import choose_item

from random_utils import random_choice_from_dict, from_dungeon_level
from item_functions import heal, cast_lightning, cast_fireball, cast_confuse


class GameMap:
    def __init__(self, width, height, dungeon_level=1):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        self.dungeon_level = dungeon_level

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities):
       
        rooms = []
        num_rooms = 0

        center_of_last_room_x = None
        center_of_last_room_y = None

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)

            # random position without going out of the map boundaries
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            # Rect class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)

            # run through other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break

            else:
                # this means there are no intersections, the room is valid

                # paint it to the map's tiles
                self.create_room(new_room)

                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()

                center_of_last_room_x = new_x
                center_of_last_room_y = new_y

                if num_rooms == 0:
                    # this is the first room, where the player starts
                    player.x = new_x
                    player.y = new_y
           
                else:
                    # all rooms after the first
                    # connect it to the previous room with a tunnel
                
                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    # flip a coin
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # vertically then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                # place items and monsters in the room
                self.place_entities(new_room, entities)

                # finally, append new room to the list
                rooms.append(new_room)
                num_rooms += 1
    
        if self.dungeon_level < 10:
            stairs_component = Stairs(self.dungeon_level + 1)
            down_stairs = Entity(center_of_last_room_x, center_of_last_room_y, '>', libtcod.white, 'Stairs', render_order=RenderOrder.STAIRS, stairs=stairs_component)
            entities.append(down_stairs)
        else:

            fighter_component = Fighter('Human', 'Boss', strength=18, agility=18, constitution=18, intelligence=18, cunning=18, base_hp=100, base_spellpower=100, base_damage=50, xp=0)
            ai_component = BossMonster()
            monster = Entity(center_of_last_room_x, center_of_last_room_y, 'B', libtcod.darker_red, 'Boss', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)

            entities.append(monster)


        
    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def place_entities(self, room, entities):
        """
        Randomly place monsters and items in a room
        """
        max_monsters_per_room = from_dungeon_level([[2, 1], [3, 4], [5, 6]], self.dungeon_level)
        max_items_per_room = from_dungeon_level([[2, 1], [3, 4]], self.dungeon_level)

        # get a random number of monsters
        number_of_monsters = randint(0, max_monsters_per_room)
        number_of_items = randint(0, max_items_per_room)

        for i in range(number_of_monsters):
            # choose a random location in the room
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            # If there is not already an entity at that location
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                monster = choose_monster(x, y, self.dungeon_level)
                entities.append(monster)

        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                item = choose_item(x, y, self.dungeon_level)
                entities.append(item)

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False


    def next_floor(self, player, message_log, constants):
        self.dungeon_level += 1
        entities = [player]

        self.tiles = self.initialize_tiles()
        self.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'], constants['map_width'], constants['map_height'], player, entities)

        player.fighter.heal(player.fighter.max_hp // 2)
        player.fighter.decrease_insanity(50)

        message_log.add_message(Message('You take a moment to rest, and recover your strength.', libtcod.light_violet))

        return entities


