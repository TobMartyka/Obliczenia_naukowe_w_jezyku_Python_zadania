S = "przykładowe zdanie z dużą ilością znaków"
print(S)
black_char = 0

for char in S:
    if not char.isspace():
        black_char += 1

print("Liczba znaków:", black_char)

words_num = S.split()
print("Słowa:" , words_num)
print("Ilość słów:" , len(words_num))

longest_word = max(words_num, key = len)

print("Najdłuższe zdanie:", longest_word)

print("Sortowanie po ilości znaków:", sorted(words_num, key = len))
print("Sortowanie po leksograficzne:", sorted(words_num))
