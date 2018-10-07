lista = [-1, 100, 20, 30, -15, 0, 200, -1000]

# 1, licznik
licznik_ujemny = 0
licznik_dodatni = 0

for el in lista:
    if el < 0:
    licznik_ujemny += 1
    elif el > 0:
       licznik_dodatni += 1

    # na listach

    dodatnie = []
    ujemne = []

    for el in lista:
        if el