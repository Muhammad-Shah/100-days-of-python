from ast import If
# Program to print "Head" or "Tail" to user randomly

import random

rand_int = random.randint(0,1)

if rand_int == 1:
    print("Head")
else:
    print("Tail")
