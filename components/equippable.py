"""
Equippable component for Subterranean Torment
"""

class Equippable:
    def __init__(self, slot, strength_bonus=0, agility_bonus=0, constitution_bonus=0, intelligence_bonus=0, cunning_bonus=0, max_hp_bonus=0, str_acc_bonus, agi_acc_bonus, dodge_bonus, hp_regen_bonus, spellpower_bonus, magic_res_bonus, crit_chance_bonus, insane_res_bonus, phys_res_bonus, damage_bonus):
        self.slot = slot
        self.strength_bonus = strength_bonus
        self.agility_bonus = agility_bonus
        self.constitution_bonus = constitution_bonus
        self.intelligence_bonus = intelligence_bonus
        self.cunning_bonus = cunning_bonus
        self.max_hp_bonus = max_hp_bonus
        self.str_acc_bonus = str_acc_bonus
        self.agi_acc_bonus = agi_acc_bonus
        self.dodge_bonus = dodge_bonus
        self.hp_regen_bonus = hp_regen_bonus
        self.spellpower_bonus = spellpower_bonus
        self.magic_res_bonus = magic_res_bonus
        self.crit_chance_bonus = crit_chance_bonus
        self.insane_res_bonus = insane_res_bonus
        self.phys_res_bonus = phys_res_bonus
        self.damage_bonus = damage_bonus


