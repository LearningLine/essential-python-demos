# apparently circular is ok
#import func_program

def f1():
    print("running f1")
    f2()
    #module.__dict__["f2"]()

def f2():
    print("running f2")
    f3()

#f1() # error

def f3():
    print("running f3")

#f1() # ok

# is either order or __main__
# print("My name is " + __name__)
#
if __name__ == "__main__":
    f1()

# list: [1,2,3]
# hash: {7: "Sunday"}
# tup: ()
# set: set()

#hash["fifth"] = "Friday"

d = dict(name="Jeff", age=7)
print(d)

#lookup_user()