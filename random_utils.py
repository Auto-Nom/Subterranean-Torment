"""
Random utilities for Subterranean Torment
"""

from random import randint


def from_dungeon_level(table, dungeon_level):
    """
    This function returns the weighting for a given dungeon level

    table is a list of 2 item lists
    The first item is the weighting of how likely a thing is to appear at a level
    The second item is the dungeon level corresponding to that weighting
    """
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value

    return 0


def random_choice_index(chances):
    """
    Returns a random index from a list of chance weightings
    """
    random_chance = randint(1, sum(chances))

    running_sum = 0
    choice = 0
    for w in chances:
        running_sum += w

        if random_chance <= running_sum:
            return choice
        choice += 1


def random_choice_from_dict(choice_dict):
    """
    Returns a random dictionary key using the weighted chances

    choice_dict = {'item': int(chance)}
    """
    choices = list(choice_dict.keys())
    chances = list(choice_dict.values())

    return choices[random_choice_index(chances)]


