x = 100923094230958203582390184312094
x = str(x)
zero_num = 0

for num in x:
    if num == "0":
        zero_num += 1

print(x)
print("Liczba zer:",zero_num)
