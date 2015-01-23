class Person:
    def __init__(self, name, age, hobbies):
        self.hobbies = hobbies
        self.age = age
        self.name = name

people = [
    Person("ted", 45, ['ski', 'bike', 'run']),
    Person("jef", 40, [ 'bike', 'run']),
    Person("pierre", 32, ['boat', 'bike', ]),
    Person("sarah", 41, ["ski" ]),
    Person("zeo", 10, ["run" ]),
]

#print(people)

"SELECT id, name, age, FROM Users WHERE created > yesterday"

bikers = (
   (p.name, p.age)         # projection
   for p in people         # source
   if 'bike' in p.hobbies  # filter
)

print(type(bikers), bikers)

older_bikers_names = (
    p[0].upper()
    for p in bikers
    if p[1] >= 40
)

# s1 = "a "
# s2 = "b "
# s3 = s1 + s2


# import os
# os.execvp()

# import re
#
# print("regex match")
# text = "The big cat was 20, but the small was 7"
# print( re.match("[0-9]+", text) )
#

for b in older_bikers_names:
    print(b)

