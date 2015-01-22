
class Animal: #(object):

    # typically avoid this
    # name = ""
    # age = 0

    def __init__(self, age = 0):
        self.age = age
        self.__db_pointer = 74773758

    @property
    def db_pointer(self):
        # if self.__db_pointer == None:
        #     self.__db_pointer = compute_new_pointer()

        return self.__db_pointer

    @db_pointer.setter
    def db_pointer(self, value):
        if value <= 0:
            raise ArithmeticError("Can't be zero")

        self.__db_pointer = value

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self.age > other.age

    def have_birthday(self):
        #self.happiness_level = 2
        self.age += 1
        print("The animal is now {0} years old".format(
            self.age
        ))

    def wake_up(self):
        print("The animal is waking up")

    def sleep(self, hours):
        print("The animal is sleeping for {0} hours".format(hours))

    @staticmethod
    def state_type():
        print("I am of type Animal")


class Pet(Animal):

    def __init__(self, name, age=0):
        super().__init__(age)
        self.name = name

    def play(self):
        print("{0} is playing".format(self.name))

    def have_birthday(self):
        super().have_birthday()
        print("{0}'s age is {1}".format(
            self.name, self.age
        ))

    def wake_up(self):
        print("{0} groans and wakes up...".format(self.name))

    def __str__(self):
        return "str: A pet with name {0}".format(self.name)

    def __repr__(self):
        return "repr: A pet with name {0}".format(self.name)

class Laptop:
    def __init__(self):
        self.name = "laptop"

    def wake_up(self):
        print("One moment while the computer restores it state...")

animal = Animal()

# suboptimal
#p = animal.__db_pointer
#animal.db_pointer = -1

print( dir(animal)  )

print("The db id is ... {0}".format(animal.db_pointer))
animal.db_pointer = 5
print("The db id is ... {0}".format(animal.db_pointer))

tiger = Pet("Fluffy the tiger", 10)

tiger.have_birthday()
tiger.have_birthday()
tiger.have_birthday()
tiger.play()
tiger.sleep(8)


Animal.state_type()




def use_animal(ani):
    print("Making animal wake up...")
    ani.wake_up()

lap = Laptop()

wakable_things = [tiger, lap] #[animal, pet, lap]

for w in wakable_things:
    print(w.name)
    use_animal(w)

# use_animal(animal)
# use_animal(pet)
# use_animal(lap)

bear = Pet("Teddy", 5)

print(bear < tiger)
print(bear > tiger)

l = [bear]
print(l)
print("there is a {0} over there".format(bear))


#bear.__dict__["_Animail__db_pointer"] = 5

















