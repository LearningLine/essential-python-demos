def some_method(name):
    '''
    some_method is super awesome

    :param name: A string with your name
    :return: nothing
    '''
    if name == "Michael":
        print("hi michael")
    else:
        print("Have we met?")
        print("My name is {0}.................\n" +
              "...............................\n" +
              "......\n".format("Ted")
        )


s = "part 1" "part 2"
s = "part 1" + "part 2"
# print("a", "a", "a")
some_method("Jeff")

print("------ vars -------------")

name = "Ted"
print( type(name) )

numText = "1"
num = 7

s = int(numText) + num
print(s)


print("-------- scope ----------")
num1 = 50

if num1 > 10:
    num2 = 2
    print("Num from if: " + str(num2))

print("Looks like the number is " + str(num1 + num2))

# prints 'Looks like the number is 42'


sharedVal = 3

def method1():
    local_thing = 2
    global sharedVal
    sharedVal = 1
    if sharedVal == 3:
        sharedVal = 7

    sharedVal += 1

method1()

#print(local_thing)
print( sharedVal ) # prints 8

print("------------ conditionals ------------")

b = True
b = 0
b = ""
print(type(b))
b = ''
b = {} # dictionary
print(type(b))
b = str()
b = "not empty"
b = []
b = [1,2,3]
b = "I am the B"

if hasattr(b, 'upper'):
    print("B has upper!")
    print(b.upper())

if b:
    print("thing is true")
else:
    print("thing is false")

# string len:
print( len(b) )

# not pythonic
#if len(b) > 0:
if b:
    print("long b")
else:
    print("short b")


def fun_new_function(param, param1, param2):
    pass
    # return None


fun_new_function(1,2,3)

print("-------------- loops ------------- ")

s = "This is fun for looping with."

for ch in s:
    print(ch, end='.')
print()

for n in range(0, 4):
    print(n, end=',')
print()

# bad...
l = [1,5,6,3]
for n in range(0, 4):
    val = l[n]
    print("{0} -> {1}".format(n, val))
print()

l = [1,5,6,3, 92,39,42,20]
for index, val in enumerate( l ):
    print(
        "{0} -> {1}, index was {0}".format(
            index, val))
print()

index = 0
while index < 500:
    if index == 10:
        index = 498
    index+=1
    print(index, end='+')


# e  = enumerate(l)
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())

print("------------ imports ------------ ")
# import our own modules
import lib as library

#b_The_Python_Language.lib.libFunc()
library.libFunc()

# import standing modules
import random
print("Let's get a random number...")
print( random.randint(0, 100) )

import sys
try:
    import requests
except:
    print("You must have requests installed to run")
    sys.exit(-299)


resp = requests.get("http://www.mentor.com")
html = resp.text
print(html[:1000])

print("-------------- files / with ----------")
import load_file

load_file.load_file()

