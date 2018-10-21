x = (10, "koszt $cena PLN", "kwota $cena brutto")

def zmiana_ceny(cena, *args):
    out = []
    for tekst in args:
        text = tekst.replace('$cena', str(cena))
        out.append((tekst))
    return "\n".join(out)







    # print("args", args)
    # print("cena", cena)


def test_formatuj():
    assert formatuj(10, 'koszt $cena PLN',
                    'kwota $cena brutto'
                    ) == "koszt 10 PLN\nkwota 10 brutto"


    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena'
    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10"
