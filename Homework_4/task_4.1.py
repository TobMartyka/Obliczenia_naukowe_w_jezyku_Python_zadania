unit_circle = lambda p: p[0]**2 + p[1]**2 <= 1

positiv_cord = lambda p: p[0] > 0 and p[1] > 0

sorting_key_x_inc_y_dec = lambda p: (-p[1], p[0])

sorting_key_sum = lambda p: abs(p[0]) + abs(p[1])

L = [(1,2), (-3, 4), (0, 0.5), (2, -1)]
print("unit", list(filter(unit_circle, L)))
print("pos", list(filter(positiv_cord, L)))
for p in L:
    print(p, unit_circle(p), positiv_cord(p))

L.sort(key=lambda p: (-p[1], p[0]))
print(L, "y decreasing, x increasing")
