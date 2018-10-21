zbior = {1,2,3,4,1}
print(zbior)
zbior.add("a")
print(zbior)
print(1 in zbior)
print(6 in zbior)

for i in zbior:
    print(i)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # suma
print(a.union(b))
print(a - b)   # różnica
print(a.difference(b))
print(a & b)   # część wspólna - iloczyn
print(a.intersection(b))
print(a ^ b)   # różnica symetryczna
print((a.symmetric_difference(b))
print((dir(a))

# print((set([1, 2, 3, 4]))
#
# print(set(range(1, 10)))

kwadraty = {(x, x**2, x**3) for x in range(1, 101)}
