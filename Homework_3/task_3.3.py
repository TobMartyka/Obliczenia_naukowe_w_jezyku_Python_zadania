'''''
Create the following variables:
n = 2022
x = math.pi   # save with 5 digits after a dot (import 'math' first!)
word = "Python"
polish = "książka"   # 'book' in English
Write the variables to a text file "vars.txt",
one line for one variable.
Print the file content on the screen.

'''''

import math

n = 2022
x = f'pi is {math.pi:.5f}'
word = "Python"
polish = "ksiązka"

with open('vars.txt', 'w') as outfile:
    outfile.write(f"{n}\n{x}\n{word}\n{polish}\n")

with open('vars.txt', 'r') as readfile:
    file = readfile.read()
    print(file)

