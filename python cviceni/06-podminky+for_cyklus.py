"""
Cvičení - podmínky
1 Dělení

Napište program deleni.py, který na příkazové řádce obdrží dvě celá čísla a
vypíše jejich podíl zaokrouhlený na tři desetinná čísla. Pokud je druhé číslo
0, program vypíše hlášku, že nulou dělit nelze.
"""
import sys
delenec = int(sys.argv[1])
delitel = int(sys.argv[2])

if delitel == 0:
    print("Neni mozno delit nulou")
else:
    print(f"Vysledek {round(delenec/delitel,3)}")

"""
2 Kontrola souboru

Napište program zpracovani.py, který na příkazové řádce obdrží název souboru. 
Pokud soubor končí příponou .csv, program vypíše název tohoto souboru na 
obrazovku. Pokud má soubor jinou příponu, programu zahlásí, že daný soubor 
neumí zpracovat.

V tomto příkladu se vám může hodit metoda řetězců s názvem endswith (viz 
dokumentace).
"""
# import sys
# soubor = sys.argv[1]
# if soubor.endswith(".csv"):
#     print(soubor)
# else:
#     print("Dany soubor nejde zpracovat")

"""
3 Maximum ze dvou čísel

Napište program max2.py, který dostane na vstupu dvě celá čísla a vrátí větší 
z nich. Vyhněte se použití funkce max().
"""
# import sys
#
# cislo1 = int(sys.argv[1])
# cislo2 = int(sys.argv[2])
#
# if cislo1 > cislo2:
#     vetsi_cislo = cislo1
# else:
#     vetsi_cislo = cislo2
#
# # Stejny vysleek, kratsi zapis, vhodne jen pro kratke vyrazy
# # vetsi_cislo = cislo1 if cislo1 > cislo2 else cislo2
#
# print(vetsi_cislo)

"""
4 Maximum ze tří čísel

Opět bez použití funkce max() napište program max3.py, který dostane na vstupu
 tři celá čísla a vrátí největší z nich.

"""
# import sys
# cislo1 = int(sys.argv[1])
# cislo2 = int(sys.argv[2])
# cislo3 = int(sys.argv[3])
#
# if cislo1 > cislo2 and cislo1 > cislo3:
#     print(f"Nejvetsi je: {cislo1}")
# elif cislo2 > cislo1 and cislo2 > cislo3:
#     print(f"Nejvetsi je: {cislo2}")
# else:
#     print(f"Nejvetsi je: {cislo3}")

# stejny vysledek da pouziti max nasledujicicm zpusobem
# max(max(cislo1, cislo2), cislo3)

# Hrátky s cykly
#
# Napište program, který dostane na příkazové řádce seznam celých čísel a
#
#     vypíše všechna tato čísla pod sebe, každé na nový řádek,
#     vypíše každé číslo spolu s jeho opačnou hodnotu (obrácené znaménko),
#     vypíše pouze čísla větší než 0,
#     čísla větší než 0 vypíše tak jak jsou, čísla menší než nula vypíše
#     s obráceným znaménkem.

import sys

argumenty = sys.argv[1:]
# vypíše všechna tato čísla pod sebe, každé na nový řádek,
[print(arg) for arg in argumenty]

# vypíše každé číslo spolu s jeho opačnou hodnotu (obrácené znaménko),
[print(arg + " " + str(int(arg)*-1)) for arg in argumenty]

# vypíše pouze čísla větší než 0,
[print(arg) for arg in argumenty if int(arg) > 0]
for arg in argumenty:
    if int(arg) > 0:
        print(arg)

# čísla větší než 0 vypíše tak jak jsou, čísla menší než nula vypíše
# s obráceným znaménkem.
for arg in argumenty:
    if int(arg) > 0:
        print(arg)
    else:
        print(int(arg)*-1)

# 6 Poznávačky
#
# Popište vlídným, ale přesným slovem, co dělají následující cykly:

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in cisla:
    if x % 2 == 0:
        print(x)

# List comprehension jen s podminkou
# [print(x) for x in cisla if x % 2 == 0]

#######################################

jmena = ["Klara", "Andrea", "Monika"]

for jmeno in jmena:
    if jmeno[0] == 'p':
        print('pako')
    else:
        print(jmeno)

# List comprehension i s else vetvi
# [print('pako') if jmeno[0] == 'p' else print("jmeno") for jmeno in jmena]




# In general,
#
# [f(x) if condition else g(x) for x in sequence]
#
# And, for list comprehensions with if conditions only,
#
# [f(x) for x in sequence if condition]