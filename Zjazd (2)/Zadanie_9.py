# produkt = input("Podaj jaki produkt chcesz kupić: ")
#
# produkt = print ("produkt")
#
# waga = input("Podaj wagę produktu")
#
# waga = print("waga")
#
# Cena = 1,99
# kg = 0
# cena_za_kg = dict(cena )

produkty = {"Ziemniaki": 2, "Bataty": 4, "Pomidory": 6}
magazyn = {"Ziemniaki": 10, "Bataty": 10, "Pomidory": 10}
do_zapłaty = 0

while True:
    print("-"*40)
    print("Nasz sklep oferuje: ")
    for produkt in produkty:
        print(f' - {produkt} - {produkty[produkt]} PLN')

    komenda = input("Co chcesz zrobić: [d]odać, [k]upić, [koniec] by by przerwać zakupy")
    if komenda == 'koniec':
        break
    produkt_wybrany = input("Co chcesz kupić? ")
    if produkt_wybrany not in produkty:
        print("Nie mamy takiego produktu!")
        continue

    waga = float(input("Ile chcesz kupić wybranego produktu[{produkt_wybrany}]"))
    if magazyn[produkt_wybrany] < waga:
        print(f"Mamy za mało [{produkt_wybrany}")
        continue
     magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - waga

        cena = produkty[produkt_wybrany]
        koszt = waga * cena
        do_zapłaty += koszt
    elif komenda == 'd':
        produkt_do_dodania = input(("Jaki produkt chcesz dodać?"))
     if produkt_do_dodania not in magazyn:
         magazyn
        ile_produktu_dodajemy = float(input("Ile tego dodać? "))
        magazyn[produkt_do_dodania] += ile_produktu_dodajemy
    else
        print("Niepoprawna komenda!!")
print("="*40)
print(f"Za zakupy zapłacisz: {do_zapłaty} PLN")
for produkt in koszyk:
        print(f" - {produkt} - {koszyk[produkt]} PLN")
        suma += koszyk[produkt]
print("-"*40)
print(f"Suma: {suma} PLN")