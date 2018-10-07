#lista = []

#for el in range (0,101):
 #   lista.append(el)
#print(lista)

#podzielne przez 3 = []

#for el in podzielne przez 3
 #   if el 3==0:
 #   print(el)

#podzielne przez 5 = []

lista = list(range(101))

wynik = []

for el in lista:
    if el % 3 == 0 or el % 5 == 0:
        wynik.append(el)

print (f"W przedziale od 0-100 jest {len(wynik)} liczba podzielna przez 3 lub 5")


print("  ", end="")

x = range(1, 50)

for i in x:
    print(f"{i:6}", end="")
    print("cost")