import random

def random_walk(start):
    position = 0
    for i in range(start):
        step = random.choice([-1, 1])
        position += step
        yield position

final = random_walk(100)

final_position = None
for position in final:
    final_position = position

print(final_position)
