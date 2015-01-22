class MemoryTester:
    def __init__(self, id):
        self._id = id
        print("Creating test {0}...".format(self._id))

    def __del__(self):
        print("Deleting test {0}...".format(self._id))



t1 = MemoryTester(1)
print("after 1 allocated")
t1_1 = t1
t1_2 = t1
print("copied 1 a few times")
print("nulling out 1")
t1 = None
print("nulling out 1v1")
t1_1 = None
print("nulling out 1v2")
t1_2 = None

t2 = MemoryTester(2)