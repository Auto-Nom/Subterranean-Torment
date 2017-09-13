"""
Fighter component for Subterranean Torment
"""

from random import randint

import libtcodpy as libtcod

from game_messages import Message

class Fighter:
    """
    Properties:
        strength, agility, constitution, intelligence, cunning, max_hp, strength_accuracy, agility_accuracy, dodge, hp_regen, spellpower, magic_resist, crit_chance, insanity_resist, physical_resist, damage
    """
    def __init__(self, strength=10, agility=10, constitution=10, intelligence=10, cunning=10, base_str_acc=50, base_agi_acc=50, base_dodge=5, base_hp=100, base_hp_regen=1, base_spellpower=50, base_magic_res=5, base_crit_chance=5, base_insane_res=5, base_phys_res=5, base_damage=5, xp=0, base_accuracy_stat="strength"):
        self.base_strength = strength
        self.base_agility = agility
        self.base_constitution = constitution
        self.base_intelligence = intelligence
        self.base_cunning = cunning

        self.base_str_acc = base_str_acc
        self.base_agi_acc = base_agi_acc
        self.base_dodge = base_dodge
        self.base_max_hp = base_hp
        self.base_hp_regen = base_hp_regen
        self.base_spellpower = base_spellpower
        self.base_magic_res = base_magic_res
        self.base_crit_chance = base_crit_chance
        self.base_insane_res = base_insane_res
        self.base_phys_res = base_phys_res
        self.base_damage = base_damage
        self.xp = xp
        self.base_accuracy_stat = base_accuracy_stat

        #self.hp = self.max_hp
        self.hp = self.base_max_hp + ((self.base_constitution - 10) * 5)

    @property
    def strength(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.strength_bonus
        else:
            bonus = 0

        return self.base_strength + bonus

    @property
    def agility(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.agility_bonus
        else:
            bonus = 0

        return self.base_agility + bonus

    @property
    def constitution(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.constitution_bonus
        else:
            bonus = 0

        return self.base_constitution + bonus

    @property
    def intelligence(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.intelligence_bonus
        else:
            bonus = 0

        return self.base_intelligence + bonus

    @property
    def cunning(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.cunning_bonus
        else:
            bonus = 0

        return self.base_cunning + bonus

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        stat_mod = (self.constitution - 10) * 5

        return self.base_max_hp + stat_mod + bonus

    @property
    def strength_accuracy(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.str_acc_bonus
        else:
            bonus = 0

        stat_mod = (self.strength - 10) * 4

        return self.base_str_acc + stat_mod + bonus

    @property
    def agility_accuracy(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.agi_acc_bonus
        else:
            bonus = 0

        stat_mod = (self.agility - 10) * 4

        return self.base_agi_acc + stat_mod + bonus

    @property
    def dodge(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.dodge_bonus
        else:
            bonus = 0

        stat_mod = (self.agility - 10) * 4

        return self.base_dodge + stat_mod + bonus

    @property
    def hp_regen(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.hp_regen_bonus
        else:
            bonus = 0

        stat_mod = (self.constitution - 10) // 2
        if stat_mod < 0:
            stat_mod = 0

        return self.base_hp_regen + stat_mod + bonus

    @property
    def spellpower(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.spellpower_bonus
        else:
            bonus = 0

        stat_mod = (self.intelligence - 10) * 10

        total = self.base_spellpower + stat_mod + bonus
        if total < 0:
            total = 0

        return total

    @property
    def magic_resist(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.magic_res_bonus
        else:
            bonus = 0

        stat_mod = (self.intelligence - 10) * 4

        return self.base_magic_res + stat_mod + bonus

    @property
    def crit_chance(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.crit_chance_bonus
        else:
            bonus = 0

        stat_mod = (self.cunning - 10) * 4

        return self.base_crit_chance + stat_mod + bonus

    @property
    def insanity_resist(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.insane_res_bonus
        else:
            bonus = 0

        stat_mod = (self.cunning - 10) * 4

        return self.base_insane_res + stat_mod + bonus

    @property
    def physical_resist(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.phys_res_bonus
        else:
            bonus = 0

        return self.base_phys_res + bonus

    @property
    def damage(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.damage_bonus
        else:
            bonus = 0

        return self.base_damage + bonus

    @property
    def accuracy_stat(self):
        if self.owner and self.owner.equipment and self.owner.equipment.accuracy_stat:
            return self.owner.equipment.accuracy_stat
        else:
            return self.base_accuracy_stat

    def take_damage(self, amount, physical=True, magical=False):
        results = []
        
        if physical:
            amount *= (1- (self.physical_resist / 100))
        
        if magical:
            amount *= (1 - (self.magic_resist / 100))

        self.hp -= amount

        results.append({'message': Message('{0} takes {1} damage after resistances'.format(self.owner.name.capitalize(), amount), libtcod.light_orange)})
        
        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp >= self.max_hp:
            self.hp = self.max_hp

    def attack(self, target, accuracy_stat):
        results = []

        dmg = self.damage
        crit = False
        
        hit = randint(1, 100)
        if hit < self.crit_chance:
            crit = True

        if accuracy_stat == "strength":
            hit *= self.strength_accuracy
        
        elif accuracy_stat == "agility":
            hit *= self.agility_accuracy

        enemy_dodge = target.fighter.dodge * randint(1, 100)

        if crit or (hit > enemy_dodge):

            if crit:
                dmg *= 2
                results.append({'message': Message('{0} deals a critical hit on {1} for {2} hit points!'.format(self.owner.name.capitalize(), target.name, str(dmg)), libtcod.red)})
                results.extend(target.fighter.take_damage(dmg))
            else:
                results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(self.owner.name.capitalize(), target.name, str(dmg)), libtcod.white)})
                results.extend(target.fighter.take_damage(dmg))
        else:
            results.append({'message': Message('{0} misses {1}.'.format(self.owner.name.capitalize(), target.name), libtcod.white)})

        return results


