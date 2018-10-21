liczby = set()



while True:
    komenda = input("Podaj liczby lub k by zakończyć:  ")
    if komenda == 'k':
        break
    liczba = int(komenda)
    liczby.add(liczba)
print(len(liczby & set(range(2, 101, 2))))





