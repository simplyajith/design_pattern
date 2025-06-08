from abc import ABC,abstractmethod


class WeaponBehavior(ABC):

    @abstractmethod
    def useweapon(self):
        pass



class KnifeBehavior(WeaponBehavior):


    def useweapon(self):
        print("I am using knife")


class AxeBehavior(WeaponBehavior):

    def useweapon(self):
        print("I am using axe")


class Character:

    def __init__(self):
        self.weapon = None

    def fight(self):
        if not self.weapon: print("no weapon")
        else:
            self.weapon.useweapon()

    def setWeapon(self, weaponBehavior):
        self.weapon = weaponBehavior

class King(Character): 

    def __init__(self):
        super().__init__()
        self.weapon = KnifeBehavior()


# chara = Character()
# chara.fight()
# chara.setWeapon(AxeBehavior())
# chara.fight()


chara = King()
chara.fight()
chara.setWeapon(AxeBehavior())
chara.fight()





