
class Cart:

    def __init__(self):
        self.__items = []
        self.__mandatory_items = [
            CartItem("lolcat", 0.00),
            CartItem("top", 0.00),
            ]

    def add(self, item):
        if not isinstance(item, CartItem):
            raise TypeError()

        self.__items.append(item)


    def __iter__(self):

        for m in self.__mandatory_items:
            yield m

        for i in self.__items:
            yield i


    # def __iter__(self): # return an object which has a
    #                     # __next__() method and implements
    #                     # the iterable behavior.
    #     return self.__items.__iter__()

class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name



cart = Cart()

cart.add( CartItem("Book", 19.99) )
cart.add( CartItem("CD", 9.99) )
cart.add( CartItem("Toy car", 150.99) )

cached = list(cart)

for item in cached:
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
    print("first iterator line")
    current = 0
    nxt = 1
    while True:
        print(".... computing next item as {0}".format(nxt))
        yield nxt
        current, nxt = nxt, current + nxt

print("Building iterator")
iterator = get_fib()
print("Iterator built")

for f in iterator:
    print("Processing item {}".format(f))
    if f < 100:
        print(f, end=",")
    else:
        break



#
#
#
# def get_interesting_lines(file):
#
#     with open(file) as fin:
#
#         for line in fin:
#             if list.find("cat error"):
#                 yield line
#
# for error in get_interesting_lines(""):
#     if error
#









