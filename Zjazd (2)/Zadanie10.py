# w podanym napisie zlicz wystąpienia poszczególnych liter

napis = input("Podaj napis ")
liczniki_liter = {0}

for litera in napis:
    liczniki_liter[litera] = liczniki_liter.get[litera, 0] + 1
for litera in liczniki_liter:
    print(f"litera: {litera} wystapiła {liczniki_liter[litera]} razy"for litera in liczniki_liter)