znalezione_max = None
znalenione_min = None


while True:
    dane_wejsciowe = input("podaj liczbe, lub wpisz KONIEC by zakonczyc: ")
    if dane_wejsciowe == "KONIEC":
        break
iczba = int(dane_wejsciowe)

    if znalezione_max is None or liczba > znalezione_max:
        znalezione_max = liczba
    if znalezione_min is None or liczba < znalezione_min:
        znalezione_min = liczba

if not znalezione_max:
    print("nie wprowadzono danych:")
else:
    print(f"minimum = {znalezione_min}, maximum = {znalezione_max}")