# CTENI
# 1 vyplata presneji
# import statistics
# vstup = open('vykaz.txt', encoding='utf-8')
# vykaz = [int(radek) for radek in vstup]
# print(vykaz)
# vstup.close()
#
# hodinova_mzda = int(input("Zadej hodinovou mzdu: "))
# vyplaty = [mesic*hodinova_mzda for mesic in vykaz]
# print(f"Vyplata za rok celkem: {sum(vyplaty)}")
# print(f"Prumerna vyplata: {statistics.mean(vyplaty)}")

# 2 pocet slov
# vstup = open('slohova_prace.txt', encoding='utf-8')
# radky = [radek for radek in vstup]
# vstup.close()
#
# radky_slov = [radek.split() for radek in radky]
# pocet_slov_na_radku = [len(radek) for radek in radky_slov]
# print(pocet_slov_na_radku)
# print(f"Celkem slov: {sum(pocet_slov_na_radku)}")

# 3 pujcovna
# import sys
# vstup = open(sys.argv[1], encoding='utf-8')
# radky = [radek for radek in vstup]
# vstup.close()
#
# radky_rozd = [radek.split()[1] for radek in radky]
# radky_rozd_opr = [float(km.replace(",", ".")) for km in radky_rozd]
# print(f"Najeto kilometru: {sum(radky_rozd_opr)}")

# PSANI
# 1 dny v mesici
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mesice = ["Leden", "Unor", "Brezen", "Duben", "Kveten", "Cerven", "Cervenec",
          "Srpen", "Zari", "Rijen", "Listopad", "Prosinec"]

soubor = open('kalendar.txt', 'w', encoding='utf-8')
soubor.write("Mesice,Pocet dni\n")
# Toto funguje
# [soubor.write(mesice[i] + "," + str(pocty_dni[i]) + "\n")for i in range(len(pocty_dni))]

# toto mi prijde prehlednejsi..
for i in range(len(pocty_dni)):
    soubor.write(mesice[i] + "," + str(pocty_dni[i]) + "\n")
soubor.close()

# 2 rozepsana vyplata
# import statistics
# vstup = open('vykaz.txt', encoding='utf-8')
# vykaz = [int(radek) for radek in vstup]
# # print(vykaz)
# vstup.close()
#
# hodinova_mzda = int(input("Zadej hodinovou mzdu: "))
# vyplaty = [mesic*hodinova_mzda for mesic in vykaz]
# vystup = open('vyplaty.txt', "w", encoding='utf-8')
# [vystup.write(str(vyplata) + "\n") for vyplata in vyplaty]
# vystup.close()

# 3 hody kostkou
# from random import randint
# import sys
#
# pocet_hodu = int(sys.argv[1])
# # predelala jsem je na string pro jednodusi zapis do souboru pomoci metody join
# hody = [str(randint(1, 6)) for i in range(pocet_hodu)]
# # print(hody)
#
# vystup = open('hody.txt', "w", encoding='utf-8')
# vystup.write(", ".join(hody))
# vystup.close()
