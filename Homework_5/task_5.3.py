import random

def random_walk(start=0):
    position = start
    while True:
        step = random.choice([-1, 1])
        position += step
        yield position
results = []
for iteration in range(10):
    walker = random_walk()
    for step in range(100):
        next(walker)
    results.append(next(walker))
print(results)
