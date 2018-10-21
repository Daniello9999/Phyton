data = [1, 2, 3, 4, 5, 6, 7]
def test_przytnij():
    result = []




    for element in data:
        if start(element) and not stop (element):
            result.append(element)
        return result





def test_przytnij():
    assert przytnij(
        data = [1, 2, 3, 4, 5, 6, 7],
        start = lambda x: x > 3,
        stop = lambda x: x == 6,) == [4, 5, 6]







# def mniejsze_od_3(x):
#     if x > 3
#         return x > 3 == 0
#
# def rowne_6(x):
#     if x == 6
#         return x > 6 == 0




y = lambda x: x > 3
x = lambda x: x == 3
print(y())
print(x())

