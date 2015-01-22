import random
import time
from wizard import Wizard, Creature
import wizard_errors

#
# def f3():
#     open("thing that doesn't exit", 'r')
#
#
# def f2():
#     f3()
#
#
# def f1():
#     f2()
#
# f1()

gandolf = Wizard(level=10)

creatures = [
    Creature("Toad", 1),
    Creature("Bat", 3),
    Creature("Tiger", 7),
    Creature("Zebra", 5),
    Creature("Dragon", 50),
    Creature("Self", 100000),
]

def parse_bool(text):
    if len(text) == 0:
        return False

    s = text.lower().strip()
    return s in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

print("A battle begins...")
time.sleep(1)


while True:

    opponent = random.choice(creatures)
    print("The wizard spots a {0}".format(opponent))

    action = input("Do you wish to attack? (no means sleep!) ")

    try:
        if parse_bool(action):
            gandolf.fight_creature(opponent)
        else:
            gandolf.rest()

    except wizard_errors.CreatureTooStrongError as x:
        print("The creature named {0} is level {1}, too strong!".format(
            x.creature.name, x.creature.level
        ))

    except wizard_errors.OutOfManaError as x:
        print("You are out of mana")

    except wizard_errors.LostBattleError as x:
        print("You have lost to {0}, you must rest".format(
            x.creature.name))
        gandolf.rest()

    except Exception as x:
        print("uh no, that failed because: " + str(x))
#
#
# def retry_operation(times, action):
#     attempts = 0
#
#     while True:
#         try:
#             action()
#             break;
#         except:
#             time.sleep(5)
#             attempts += 1
#
#
#         if attempts >= times:
#             raise Exception("Really failed")
#
#
#
#
# db = "..."
#
# retry_operation(5, db.connect)
#













