
class WizardError(Exception):
    pass

class LostBattleError(WizardError):

    def __init__(self, creature, msg="You have lost the battle"):
        self.creature = creature
        super().__init__(msg)

class OutOfManaError(WizardError):
    pass

class CreatureTooStrongError(WizardError):

    def __init__(self, creature, msg="Creature too strong"):
        self.creature = creature
        super().__init__(msg)


