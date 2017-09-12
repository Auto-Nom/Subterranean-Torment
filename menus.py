"""
Menus for Subterranean Torment
"""

import libtcodpy as libtcod

def menu(con, header, options, width, screen_width, screen_height):
    # uses the 26 letters of the alphabet for the options
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')

    # calculate total height for the header
    header_height = libtcod.console_get_height_rect(con, 0, 0, width, screen_height, header)
    height = len(options) + header_height

    # create an off screen console that represents the windows menu
    window = libtcod.console_new(width, height)

    # print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)

    # print all the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1

    # blit the contents of window to the root console
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)


def inventory_menu(con, header, player, inventory_width, screen_width, screen_height):
    # show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty']
    else:
        options = []

        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (main hand)'.format(item.name))
            elif player.equipment.off_hand == item:
                options.append('{0} (off hand)'.format(item.name))
            elif player.equipment.head == item:
                options.append('{0} (head)'.format(item.name))
            elif player.equipment.neck == item:
                options.append('{0} (neck)'.format(item.name))
            elif player.equipment.ring_finger_l == item:
                options.append('{0} (left ring finger)'.format(item.name))
            elif player.equipment.ring_finger_r == item:
                options.append('{0} (right ring finger)'.format(item.name))
            elif player.equipment.arms == item:
                options.append('{0} (arms)'.format(item.name))
            elif player.equipment.torso == item:
                options.append('{0} (torso)'.format(item.name))
            elif player.equipment.legs == item:
                options.append('{0} (legs)'.format(item.name))
            elif player.equipment.feet == item:
                options.append('{0} (feet)'.format(item.name))
            else:
                options.append(item.name)

    menu(con, header, options, inventory_width, screen_width, screen_height)


def main_menu(con, background_image, screen_width, screen_height):
    libtcod.image_blit_2x(background_image, 0, 0, 0)

    libtcod.console_set_default_foreground(0, libtcod.light_yellow)
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 4, libtcod.BKGND_NONE, libtcod.CENTER, 'SUBTERRANEAN TORMENT')
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 2), libtcod.BKGND_NONE, libtcod.CENTER, 'By Auto_Nom')

    menu(con, '', ['Play a new game', 'Continue last game', 'Quit'], 24, screen_width, screen_height)


def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
    options = ['Base Strength +1 (from {0})'.format(player.fighter.base_strength),
            'Base Agility +1 (from {0})'.format(player.fighter.base_agility),
            'Base Constitution +1 (from {0})'.format(player.fighter.base_constitution),
            'Base Intelligence +1 (from {0})'.format(player.fighter.base_intelligence),
            'Base Cunning +1 (from {0})'.format(plater.fighter.base_cunning)]

    menu(con, header, options, menu_width, screen_width, screen_height)


def character_screen(player, character_screen_width, character_screen_height, screen_width, screen_height):
    window = libtcod.console_new(character_screen_width, character_screen_height)

    libtcod.console_set_default_foreground(window, libtcod.white)

    libtcod.console_print_rect_ex(window, 0, 1, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Character Information')

    libtcod.console_print_rect_ex(window, 0, 2, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Level: {0}'.format(player.level.current_level))
    
    libtcod.console_print_rect_ex(window, 0, 3, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Experience: {0}'.format(player.level.current_xp))

    libtcod.console_print_rect_ex(window, 0, 4, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Experience required to level up: {0}'.format(player.level.experience_to_next_level))

    libtcod.console_print_rect_ex(window, 0, 6, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Maximum HP: {0}'.format(player.fighter.max_hp))

    libtcod.console_print_rect_ex(window, 0, 7, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Damage: {0}'.format(player.fighter.damage))

    libtcod.console_print_rect_ex(window, 0, 8, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Strength: {0}'.format(player.fighter.strength))

    libtcod.console_print_rect_ex(window, 0, 9, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Agility: {0}'.format(player.fighter.agility))

    libtcod.console_print_rect_ex(window, 0, 10, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Constitution: {0}'.format(player.fighter.constitution))

    libtcod.console_print_rect_ex(window, 0, 11, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Intelligence: {0}'.format(player.fighter.intelligence))

    libtcod.console_print_rect_ex(window, 0, 12, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Cunning: {0}'.format(player.fighter.cunning))

    libtcod.console_print_rect_ex(window, 0, 13, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Accuracy Stat: {0}'.format(player.fighter.accuracy_stat))

    libtcod.console_print_rect_ex(window, 0, 14, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Strength Accuracy: {0}'.format(player.fighter.strength_accuracy))
    
    libtcod.console_print_rect_ex(window, 0, 15, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Agility Accuracy: {0}'.format(player.fighter.agility_accuracy))

    libtcod.console_print_rect_ex(window, 0, 16, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Dodge Chance: {0}'.format(player.fighter.dodge))

    libtcod.console_print_rect_ex(window, 0, 17, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'HP Regen: {0}'.format(player.fighter.hp_regen))

    libtcod.console_print_rect_ex(window, 0, 18, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Spellpower: {0}'.format(player.fighter.spellpower))

    libtcod.console_print_rect_ex(window, 0, 19, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Magic Resistance: {0}'.format(player.fighter.magic_resist))

    libtcod.console_print_rect_ex(window, 0, 20, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Crit Chance: {0}'.format(player.fighter.crit_chance))

    libtcod.console_print_rect_ex(window, 0, 21, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Insanity Resist: {0}'.format(player.fighter.insanity_resist))

    libtcod.console_print_rect_ex(window, 0, 22, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Physical Resist: {0}'.format(player.fighter.physical_resist))

    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    libtcod.console_blit(window, 0, 0, character_screen_width, character_screen_height, 0, x, y, 1.0, 0.7)


def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)


