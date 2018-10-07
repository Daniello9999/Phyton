liczba_dni_tygodnia = 7

numer_dnia = 1
suma_temperatur = 0

min_ = None
max_ = None

while numer_dnia <= liczba_dni_tygodnia:
    temp = int(input (f"podaj temperaturę z dnia {numer dnia}"))
    suma_temperatur +=  temp
    
   if numer_dnia == 1
       min_ = temp
       max_ = temp
   else:
       if temp < min_ :
           min_ = temp
       if temp > max_ :
           max_= temp
   numer_dnia += 1


srednia_temperatur = suma_temperatur / liczba_dni_tygodnia
print (srednia_temperatur)
print (min_, max_)
