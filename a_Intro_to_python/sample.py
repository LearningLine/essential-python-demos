#!/usr/bin/python

import sys


text = "Hello python, version {0}"

print( text.format(sys.version) )

# Python 2 vs 3 weirdness...

# print("Hello", "world")
#
# print "hello"
#
# list = 7
# stuff = list()
#
# tuple_t =  ("Hello", "world")
#
# print tuple_t
#
