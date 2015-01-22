
class Cart:

    def __init__(self):
        self.__items = []

    def add(self, item):
        if not isinstance(item, CartItem):
            raise TypeError()

        self.__items.append(item)

    def __iter__(self): # return an object which has a
                        # __next__() method and implements
                        # the iterable behavior.
        return self.__items.__iter__()

class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name



cart = Cart()

cart.add( CartItem("Book", 19.99) )
cart.add( CartItem("CD", 9.99) )
cart.add( CartItem("Toy car", 150.99) )

for item in cart:
    print("Contains {0} for ${1}".format(item.name, item.price))


# def get_fib(limit):
#
#     # 1,1,3,5,8,13,21
#     nums = []
#     current = 0
#     next = 1
#     while len(nums) < limit:
#         nums.append(next)
#         current, next = next, current + next
#
#     return nums


def get_fib():
    current = 0
    nxt = 1
    while True:
        yield nxt
        current, nxt = nxt, current + nxt


for f in get_fib():
    if f < 100000:
        print(f, end=",")
    else:
        break
















