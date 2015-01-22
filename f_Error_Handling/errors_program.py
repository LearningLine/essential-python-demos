import random
import time
from wizard import Wizard, Creature

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

    if parse_bool(action):
        gandolf.fight_creature(opponent)
    else:
        gandolf.rest()

