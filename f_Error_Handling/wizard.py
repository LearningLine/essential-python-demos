import random
import time


class Wizard:
    def __init__(self, level=5):
        self.mana = 5
        self.level = level
        self.fight_count = level * 2 - 1

    def fight_creature(self, creature):
        print("The wizard aims at {0} menacingly".format(creature.name))
        time.sleep(1)
        print("The wizard attacks!")
        time.sleep(1)
        self.mana -= 1

        if creature.level > self.level:
            print("Cannot attack")
            return

        if self.mana <= 0:
            print("Out of mana")
            return

        self.fight_count += 1
        success = random.randint(0, 10) > 3

        time.sleep(1)

        if not success:
            print("The wizard is defeated!")
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
