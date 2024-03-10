x = 5
x == 5 and 3 + 8   # 11 - ponieważ x = 5 to drugi warunek może być spełniony czyli dodanie 3 + 8
x == 4 and 3 + 8   # False - ponieważ x > 4 to zdanie nie jest prawdziwe
3 + 8 and x == 5   # True - w tych przypadkach została zamieniona kolejność ale ze względu, że 3+8 jest wartością niezerową to ten warunek jest prawdziwy
3 + 8 and x == 4   # False

isinstance(True, int)    # True - True jest wartością logiczną dlatego jest podklasą zmiennych typu int oraz bool 
isinstance(True, bool)   # True co sprawia, że te zdania również są prawidziwe
