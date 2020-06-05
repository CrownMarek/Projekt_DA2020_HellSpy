import math

"""
1 Obsah elipsy - pohodička

Tentokrát chceme spočítat plochu pozemku ve tvaru elipsy jako na obrázku.

Z matematiky víme, že známe-li šířku a výšku elipsy, její obsah je polovina
šířky krát polovina výšky krát číslo pí. Napište funkci elipseArea, která
spočítá plochu pozemku dle zadané šířky a výšky. Číslo pí najdete v modulu
math jako math.pi.
"""


def elipse_area(width, height):
    return (width / 2) * (height / 2) * math.pi


"""
2 Větší ze dvou čísel - pohodička

Napište funkci jménem max2, který vrátí větší ze dvou zadaných čísel.
"""


def max2(a, b):
    if a > b:
        return a
    return b


"""
3 Geometrický průměr - to dáš

Napište funkci jménem gmean, která spočítá takzvaný geometrický průměr ze 
zadaného seznamu čísel. Geometrický průměr n čísel se spočítá tak, že se 
všechny hodnoty navzájem vynásobí a z výsledného součinu se spočítá n-tá 
odmocnina.
"""


def gmean(num_list):
    n = len(num_list)
    res = 1
    for num in num_list:
        res *= num
    return res ** (1 / n)


"""
4 Větší ze tří čísel - zapni hlavu

Napište funkci jménem max3, který vrátí největší ze tří zadaných čísel.

"""


def max3(a, b, c):
    return max2(max2(a, b), c)
