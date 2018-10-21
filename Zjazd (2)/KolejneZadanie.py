liczby = [5, 2, 1, 4, 3]

print("Przed: ", liczby)

for i in range(len(liczby)):
    index_minimum = i
   # print('i: ', i, 'liczby: ', liczby[i:])
    for j in range(i + 1, len(liczby)):
        if liczby[j] < liczby[index_minimum]:
            index_minimum = j
    liczby[i], liczby[index_minimum] = liczby[index_minimum], liczby[i]
    print('i: ', i, 'liczby: ', liczby)

liczby[0], liczby[1] = liczby[2], liczby[3]


print("Po: ", liczby)

