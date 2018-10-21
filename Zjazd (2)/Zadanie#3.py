def policz_znaki(napis, start  = "<", end = ">" ):
     wynik = 0
     start_i = 0
     end_i = 0
     if "<" in napis:
         start_i = napis.index('<')
     if ">" in napis:
         end_i = napis.index('>')
     if start_i and end_i:
         wynik = end_i - start_i

     return wynik




def test_policz_znaki_pusty_napis():
    assert policz_znaki('') == 0

def test_policz_znak_napis_bez_znacznikow():
    assert policz_znaki('To jest napis') == 0


def test1_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test2_policz_znaki():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18

def test3_policz_znaki():
    assert policz_znaki('a <a<a<a>>>') == 6
