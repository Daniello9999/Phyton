def wiecej_niz()
    return set()








def test_wiecej_niz_dla_pustego_napis():
    assert wiecej_niz("", 0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("a", 2) == {'aaaaabbbccd', 2}