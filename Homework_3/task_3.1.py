#For a given word (you may use your name), print it in squares.
#If word = "Python", then the result is
#+---+---+---+---+---+---+
#| P | y | t | h | o | n |
#+---+---+---+---+---+---+

word = "Tobiasz"

print("+" + "---+" * len(word))

for char in word:
    print(f"|{char:^3}", end='')
print('|')


print("+" + "---+" * len(word))
