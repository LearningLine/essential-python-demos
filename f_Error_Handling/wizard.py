import random
import time
from wizard_errors import CreatureTooStrongError, OutOfManaError, LostBattleError


class Wizard:
    def __init__(self, level=5):
        self.mana = 0
        self.level = level
        self.fight_count = level * 2 - 1

    def fight_creature(self, creature):
        print("The wizard aims at {0} menacingly".format(creature.name))
        time.sleep(1)
        print("The wizard attacks!")
        time.sleep(1)
        self.mana -= 1

        if creature.level > self.level:
            raise CreatureTooStrongError(creature,"Cannot attack")

        if self.mana <= 0:
            raise OutOfManaError("out of mana")

        self.fight_count += 1
        success = random.randint(0, 10) > 2

        time.sleep(1)

        if not success:
            raise LostBattleError(creature,"wizard is dead")
        else:
            print("The wizard stands tall over {0}".format(creature.name))
            if self.fight_count / 2 > self.level:
                self.level = self.fight_count // 2
                print("** The wizard has leveled up! Now level {0}! **".format(self.level))

        print("The wizard's mana is now at {0}".format(self.mana))


    def rest(self):
        print("The wizard is sleeping...")
        time.sleep(5)

        self.mana += 5
        print("The wizard stirs!")


class Creature:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def __str__(self):
        return "{0} of level {1}".format(self.name, self.level)
