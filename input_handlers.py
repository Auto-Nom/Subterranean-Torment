"""
Input Handlers for Subterranean Torment

"""

import libtcodpy as libtcod

from game_states import GameStates


def handle_keys(key, game_state):
    """
    Handle keys correctly based on the game state
    """
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state in (GameStates.PLAYER_DEAD, GameStates.VICTORY):
        return handle_player_dead_keys(key)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY, GameStates.ACTIVATE_INVENTORY, GameStates.EQUIP_INVENTORY):
        return handle_inventory_keys(key)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key)
    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen(key)
    
    return {}

def handle_targeting_keys(key):
    """
    Targeting is mouse based at the moment, only need to handle cancelling from the keyboard
    """
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}

    return {}

def handle_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    if key.vk == libtcod.KEY_ESCAPE:
        # exit the menu
        return {'exit': True}

    return {}

def handle_main_menu(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'new_game': True}
    elif key_char == 'b':
        return {'load_game': True}
    elif key_char == 'c' or key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_level_up_menu(key):
    if key:
        key_char = chr(key.c)

        if key_char == 'a':
            return {'level_up': 'strength'}
        elif key_char == 'b':
            return {'level_up': 'agility'}
        elif key_char == 'c':
            return {'level_up': 'constitution'}
        elif key_char == 'd':
            return {'level_up': 'intelligence'}
        elif key_char == 'e':
            return {'level_up': 'cunning'}

    return {}


def handle_character_screen(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_player_turn_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        return {'move': (1, 0)}
    elif key_char == 'y':
        return {'move': (-1, -1)}
    elif key_char == 'u':
        return {'move': (1, -1)}
    elif key_char == 'b':
        return {'move': (-1, 1)}
    elif key_char == 'n':
        return {'move': (1, 1)}
    elif key_char == 'z':
        return {'wait': True}
    
    elif key_char == 'g':
        return {'pickup': True}

    elif key_char == 'f':
        return {'fire': True}

    elif key_char == 'i':
        return {'show_inventory': True}

    elif key_char == 'd':
        return {'drop_inventory': True}

    elif key_char == 'a':
        return {'activate_inventory': True}

    elif key_char == 'e':
        return {'equip_inventory': True}

    elif key_char == 'w':
        return {'increase_brightness': True}

    elif key_char == 'q':
        return {'decrease_brightness': True}

    elif key.vk == libtcod.KEY_ENTER:    # can't get '>' to work?
        return {'take_stairs': True}

    elif key_char == 'c':
        return {'show_character_screen': True}


    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt + Enter: toggle fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    return {}


def handle_player_dead_keys(key):
    key_char = chr(key.c)

    if key_char == 'i':
        return {'show_inventory': True}

    elif key_char == 'c':
        return {'show_character_screen': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_race_select_menu(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'race': 'Human'}
    elif key_char == 'b':
        return {'race': 'Orc'}
    elif key_char == 'c':
        return {'race': 'Gnome'}
    elif key_char == 'd':
        return {'race': 'Dwarf'}
    elif key_char == 'e':
        return {'race': 'Elf'}
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_role_select_menu(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'role': 'Ranger'}
    elif key_char == 'b':
        return {'role': 'Barbarian'}
    elif key_char == 'c':
        return {'role': 'Fighter'}
    elif key_char == 'd':
        return {'role': 'Mage'}
    elif key_char == 'e':
        return {'role': 'Rogue'}
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


