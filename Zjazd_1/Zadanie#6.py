liczby = [5, 2, 1, 4, 3]

min_i = None
max_i = None

#print(liczby)
#print(list(range(len(liczby))))
indeksy = (list(range(len(liczby))))

for i in indeksy:
    if min_i == None or liczby[i] < liczby[min_i]:
        min_i = i
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i = i

if min_i is not None and max_i is not None:
    tmp = liczby[max_i]
    liczby[min_i] = liczby[max_i]
    liczby[max_i] = tmp


    print(i)
    print(max_i)
#assert liczby == [1, 2, 3, 4, 5]