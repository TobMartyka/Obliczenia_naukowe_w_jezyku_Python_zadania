t = (2, 4) # Stworzenie krotki zawierającej int 2 i 4
print(t[1]) #Ze wzlędu na to, że indeksy obietków zaczynają się od 0 do w krotce zawierającej 2 elementy możliwe argumenty to 0 lub 1
t.append(6) #Ponieważ krotki są obiektami niemodyfikowalnymi nie możliwe jest zastosowanie funkcji .append dodające obiekty. Możliwe jest jedynie dodawanie do list
a, b = t ; print(a, b) #W tym przypadku krotka jest rozpakowywana poprzez przydzielenie zmiennych a i b do zawartości krotki
