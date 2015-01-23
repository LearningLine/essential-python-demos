
def all_nums():
    i = 0
    while True:
        print("getting all: " + str(i))
        yield i
        i+= 1


def evens(nums):
    for n in nums:
        if n % 2 == 0:
            print("getting even: " + str(n))
            yield n

def thirds(nums):
    for n in nums:
        if n % 3 == 0:
            print("getting third: " + str(n))
            yield n

        if n > 10:
            break;

def double_num(nums):
    for n in nums:
        print("getting double: " + str(n))
        yield 2*n



pipe = all_nums()
pipe = evens(pipe)
pipe = thirds(pipe)
#pipe = double_num(pipe)
pipe = (
    2*n
    for n in pipe
    if n > 6
)


for n in pipe:
    if n > 1000:
        break;
    print(n, end=',')

























