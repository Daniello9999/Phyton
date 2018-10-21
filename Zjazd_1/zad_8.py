
int(input (podaj_wymiary [cm]: "))

a = int(input("wysokość: "))
b = int(input("szerokość: "))
c = int(input("głębokość: "))

if a*b*c > 1000:
    print("objetosc przekroczyla litr")
else:
    print("objetosc mniejsza lub rowna litrowi")
