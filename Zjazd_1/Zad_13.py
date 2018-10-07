liczba_dni_tygodnia = 7

numer_dnia = 1
suma_temperatur = 0

while numer_dnia <= liczba_dni_tygodnia:
    temp = int(input (f"podaj temperaturę z dnia {numer dnia}"))
    suma_temperatur +=  temp
    numer_dnia += 1

srednia_temperatur = suma_temperatur / liczba_dni_tygodnia

print (f"srednia temperatura w tygodniu to {srednia temperatur}")