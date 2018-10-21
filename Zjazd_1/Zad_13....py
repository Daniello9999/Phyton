liczba_dni_tygodnia = 7

def pobieranie_danych(ile_razy = 7):
    temperatury = []
    for i in  range(ile_razy):
        temp = int(input(f"podaj temperaturę z dnia {numer dnia}"))
        temperatury.append(temp)
    return temperatury

def srednia_temp(temperatury):
    srednia_temperatura = sum(temperatury / len(temperatury))
    return srednia_temperatura

def znajdz_ekstrem(temperatury):
    min_ = min(temperatury)
    max_ = (temperatury)
    return min_,max_


def prezentuj_dane(srednia_temperatura, min_, max_):
    print(f'Średnia temperatura w tygodniu to {srednia_temperatur}')
    print(f'Temperatura minimalna to było: {min_}')
    print(f'Temperatura minimalna to było: {max_}')

dane = pobieranie_danych()
sr_temp = srednia_temp(dane)
min_, max_ = znajdz_ekstrem(dane)
prezentuj_dane((sr_temp, min_, max_))



#     numer_dnia = 1
#     suma_temperatur = 0
#     return numer_dnia, suma_temperatur, liczba_dni_tygodnia
#
# min_ = None
# max_ = None
#
#
#
#
# while numer_dnia <= liczba_dni_tygodnia:
#     temp = int(input (f"podaj temperaturę z dnia {numer dnia}"))
#     suma_temperatur +=  temp
#
#    if numer_dnia == 1
#        min_ = temp
#        max_ = temp
#    else:
#        if temp < min_ :
#            min_ = temp
#        if temp > max_ :
#            max_= temp
#      numer_dnia += 1
#
#
# srednia_temperatur = suma_temperatur / liczba_dni_tygodnia
#
#
# print (srednia_temperatur)
# print (min_, max_)
