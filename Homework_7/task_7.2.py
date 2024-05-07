import itertools
import random

def iter_cycle():
    return itertools.cycle([0,1])
def iter_random():
    while True:
        yield random.choice([0,1])
def iter_random2():
    while True:
        yield 0
        yield 1
        yield 0
        yield -1

a = iter_cycle()
b = iter_random()
c = iter_random2()

print("| a | b | c |")
for i in range(20):
    print(f"|{next(a):^3}|{next(b):^3}|{next(c):^3}|")
