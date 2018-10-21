napis = input("Podaj napis: ")

SAMOGLOSKI = 'aeiou'
ile_samoglosek = 0

for znak in napis:
    # jesli samogloski to powieksz licznik
    if znak in SAMOGLOSKI:
        ile_samoglosek += 1