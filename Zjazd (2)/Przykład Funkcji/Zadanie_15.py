from random import randint

# losowanie położenia
s_x = randint(1, 10)
s_y = randint(1, 10)
g_x = randint(1, 10)
g_y = randint(1, 10)

def losowanie_polozenia():
    return randint(1, 10), randint(1, 10)

def minimalna_liczba_krokow_przed():
    return abs(s_x - g_x) + abs(s_y - g_y)

def minimalna_liczba_krokow_po():
    return abs(s_x - g_x) + abs(s_y - g_y)