outer = 6


def scopeMethod():
    global outer
    outer = 2
    print(outer)  # global, prints 6

# def scopeMethod(a, b):
# print("this is the a b one")


print(outer)

#scopeMethod(1, 2)
scopeMethod()

print(outer)

print("---------- as args ----------------- ")


def our_filter(items, test):
    data = []
    for i in items:
        if test(i):
            data.append(i)

    return data


names = [
    "Ted",
    "Jeff",
    "Zoe",
    "Rich",
    "Ralph",
    "Sarah"
]


def isShortText(text):
    return len(text) <= 3


filtered_data = our_filter(names, isShortText)

print("short names:")
for f in filtered_data:
    print(f)

filtered_data = our_filter(names, lambda t: len(t) > 3)

print("long names:")
for f in filtered_data:
    print(f)

nums = [1, 3, -4, 38, -84, 93, 2]

nums.sort()

print("Standard sort")
print(nums)

import math

f = lambda n: math.fabs(n)
def f2(n):
    return math.fabs(n)

a = False#bool(input("Do you want sort ascending? (true/false)"))
flip = 1 if a else -1
print("flip is " +str(flip))
#nums.sort(key=f)
nums.sort(key=lambda n: flip * math.fabs(n))
print("abs sort")
print(nums)

def f3():
    print("F3 from program...")

    # def z(): print('this is the z')
    #
    # return z

import order
#from order import f2, f1
order.f3()
f3()

# main here...
















