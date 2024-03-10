roman_num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

input_roman = input("Wpisz rzymską liczbę: ")

output_arabic = 0


for num in input_roman:
    value = roman_num.get(num, 0)
    output_arabic += value


print("Liczba arabska:", output_arabic)
