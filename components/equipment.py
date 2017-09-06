"""
Equipment component for Subterranean Torment
"""

from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, head=None, neck=None, ring_finger_l=None, ring_finger_r=None, arms=None, torso=None, legs=None, feet=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.head = head
        self.neck = neck
        self.ring_finger_l = ring_finger_l
        self.ring_finger_r = ring_finger_r
        self.arms = arms
        self.torso = torso
        self.legs = legs
        self.feet = feet


    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_hp_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.max_hp_bonus

        if self.ring_finger_l and self.ring_finger_l.equippable:
            bonus += self.ring_finger_l.equippable.max_hp_bonus

        if self.ring_finger_r and self.ring_finger_r.equippable:
            bonus += self.ring_finger_r.equippable.max_hp_bonus

        if self.arms and self.arms.equippable:
            bonus += self.arms.equippable.max_hp_bonus

        if self.torso and self.torso.equippable:
            bonus += self.torso.equippable.max_hp_bonus

        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.max_hp_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_hp_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.power_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.power_bonus

        if self.ring_finger_l and self.ring_finger_l.equippable:
            bonus += self.ring_finger_l.equippable.power_bonus

        if self.ring_finger_r and self.ring_finger_r.equippable:
            bonus += self.ring_finger_r.equippable.power_bonus

        if self.arms and self.arms.equippable:
            bonus += self.arms.equippable.power_bonus

        if self.torso and self.torso.equippable:
            bonus += self.torso.equippable.power_bonus

        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.power_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.defense_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.defense_bonus

        if self.ring_finger_l and self.ring_finger_l.equippable:
            bonus += self.ring_finger_l.equippable.defense_bonus

        if self.ring_finger_r and self.ring_finger_r.equippable:
            bonus += self.ring_finger_r.equippable.defense_bonus

        if self.arms and self.arms.equippable:
            bonus += self.arms.equippable.defense_bonus

        if self.torso and self.torso.equippable:
            bonus += self.torso.equippable.defense_bonus

        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.defense_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.defense_bonus

        return bonus


    def toggle_equip(self, equippable_entity):
        """
        Equip an item, or unequip it if it is already equipped

        HP percentage stays the same when equipping/unequipping max_hp_bonus providing items
        """
        results = []

        # keep hp percentage
        hp_percent = self.owner.fighter.hp / self.owner.fighter.max_hp

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'unequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'unequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        elif slot == EquipmentSlots.HEAD:
            if self.head == equippable_entity:
                self.head = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.head:
                    results.append({'unequipped': self.head})

                self.head = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.NECK:
            if self.neck == equippable_entity:
                self.neck = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.neck:
                    results.append({'unequipped': self.neck})

                self.neck = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.RING_FINGER_L:
            if self.ring_finger_l == equippable_entity:
                self.ring_finger_l = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.ring_finger_l:
                    results.append({'unequipped': self.ring_finger_l})

                self.ring_finger_l = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.RING_FINGER_R:
            if self.ring_finger_r == equippable_entity:
                self.ring_finger_r = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.ring_finger_r:
                    results.append({'unequipped': self.ring_finger_r})

                self.ring_finger_r = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.ARMS:
            if self.arms == equippable_entity:
                self.arms = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.arms:
                    results.append({'unequipped': self.arms})

                self.arms = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.TORSO:
            if self.torso == equippable_entity:
                self.torso = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.torso:
                    results.append({'unequipped': self.torso})

                self.torso = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.LEGS:
            if self.legs == equippable_entity:
                self.legs = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.legs:
                    results.append({'unequipped': self.legs})

                self.legs = equippable_entity
                results.append({'equipped': equippable_entity})
        
        elif slot == EquipmentSlots.FEET:
            if self.feet == equippable_entity:
                self.feet = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.feet:
                    results.append({'unequipped': self.feet})

                self.feet = equippable_entity
                results.append({'equipped': equippable_entity})
        
        
        # account for hp changes
        self.owner.fighter.hp = int(self.owner.fighter.max_hp * hp_percent)
        # don't let hp reach zero from unequipping an item
        if self.owner.fighter.hp == 0:
            self.owner.fighter.hp = 1

        #if self.owner.fighter.hp > self.owner.fighter.max_hp:
        #    self.owner.fighter.hp = self.owner.fighter.max_hp

        return results


