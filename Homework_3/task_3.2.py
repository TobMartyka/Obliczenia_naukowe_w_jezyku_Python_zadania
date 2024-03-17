'''
Make a loop over integer numbers from 1 to 40.
If x is divided by 5 then print a message 'x is divided by 5'.
If x is divided by 7 then print a message 'x is divided by 7'.
If x is divided by 5 and 7 then print a message 'x is divided by 5 and 7'.
Skip x = 13.
If x is not divided by 5 and x is not divided by 7
then print a message 'x is not important'.
Prepare two solutions with 'while' and 'for' loops.
'''

for num in range(1,41):
    if num == 13:
        continue
    if num%5 == 0 and num%7 == 0:
        print(f'{num} is divided by 5 and 7')
    elif num%5 == 0:
        print(f'{num} is divided by 5')
    elif num%7 == 0:
        print(f'{num} is divided by 7')
    elif num%5 > 0 and num%7 > 1:
        print(f'{num} is not imporant')

num = 1
while num <= 40:
    if num == 13:
        num += 1
        continue
    if num % 5 == 0 and num % 7 == 0:
        print(f'{num} is divided by 5 and 7')
    elif num % 5 == 0:
        print(f'{num} is divided by 5')
    elif num % 7 == 0:
        print(f'{num} is divided by 7')
    else:
        print(f'{num} is not important')
    num += 1
