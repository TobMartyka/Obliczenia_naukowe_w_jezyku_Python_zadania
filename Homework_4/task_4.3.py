def iter_even():
    x = 0
    while True:
        yield x
        x += 2

def iter_odd():
    x = 1
    while True:
        yield x
        x += 2

def iter_power(k):
    x = 1
    while True:
        yield x
        x *= k

print("|even|odd|power|")
even, odd, power = iter_even(), iter_odd(), iter_power(2)
for i in range(10):
    print(f"|{next(even):4}|", f"{next(odd):2}|", f"{next(power):4}|")
