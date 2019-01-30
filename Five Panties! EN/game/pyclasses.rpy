init 2 python:
    class Player:
        def __init__(self, name, hp, dmg, weapon):
            self.name = name
            self.hp = hp
            self.dmg = dmg + weapon.dmg
            self.weapon = weapon
            self.skills = []
            
        def add_skill(self, skill):
            self.skills.append(skill)      
            
    class UnarmedEnemy:
        def __init__(self, name, hp, dmg):
            self.name = name
            self.hp = hp
            self.dmg = dmg
            
    class ArmedEnemy:
        def __init__(self, name, hp, dmg, weapon):
            self.name = name
            self.hp = hp
            self.dmg = dmg + weapon.dmg
            self.weapon = weapon
            
    class Weapon:
        def __init__(self, name, dmg):
            self.name = name
            self.dmg = dmg