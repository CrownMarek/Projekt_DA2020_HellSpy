# """
# Vytvořte seznam, který obsahuje pouze názvy všech krajů, tedy první sloupeček této tabulky.
# Vytvořte seznam, který obsahuje počty obyvatel jako čísla. Pro zbavení se mezer v číslech se vám jistě bude hodit metoda řetězců jménem replace().
# Do vhodně pojmenované proměnné uložte seznam, který reprezentuje výše uvedenou tabulku jako dva seznamy: seznam jmen a seznam počtů obyvatel jako čísla.
# """
#
# kraje = [
#     ['Hlavní město Praha', '1 280 508'],
#     ['Jihočeský kraj', '638 782'],
#     ['Jihomoravský kraj', '1 178 812'],
#     ['Karlovarský kraj', '296 749'],
#     ['Kraj Vysočina', '508 952'],
#     ['Královéhradecký kraj', '550 804'],
#     ['Liberecký kraj', '440 636'],
#     ['Moravskoslezský kraj', '1 209 879'],
#     ['Olomoucký kraj', '633 925'],
#     ['Pardubický kraj', '517 087'],
#     ['Plzeňský kraj', '578 629'],
#     ['Středočeský kraj', '1 338 982'],
#     ['Ústecký kraj', '821 377'],
#     ['Zlínský kraj', '583 698']
# ]
#
# nazvy_kraju = [kraj[0] for kraj in kraje]
# obyvatele = [int(kraj[1].replace(" ", "")) for kraj in kraje]
#
# vysledek = [nazvy_kraju, obyvatele]
# list_ovoce = ['jabko', 'hruska']
#
# result = list(map(lambda a: a > 517087, obyvatele))
# print(result)

# print(nazvy_kraju)
# print(obyvatele)

# for kraj in list(zip(nazvy_kraju, obyvatele)):
#     print(list(kraj))


hlasy = [
    [78774, 43179, 225111, 144799, 242854],
    [91062, 22451, 17475, 53391, 46450],
    [179186, 216499, 4493, 156305, 61222],
    [9619, 53476, 926, 64737, 34566],
    [66904, 85730, 27271, 12964, 38041],
    [118755, 1929, 30426, 25178, 31952],
    [64467, 40993, 81181, 39392, 4335],
    [11221, 97970, 26179, 98539, 112578],
    [171064, 7638, 8752, 96666, 39738],
    [74235, 101680, 18920, 45904, 1922],
    [39309, 1505, 10531, 30458, 40228],
    [131584, 1812, 241122, 22267, 99326],
    [194133, 39985, 200997, 28229, 20780],
    [66188, 51607, 15977, 177272, 17664]
]

# https://stackoverflow.com/questions/6473679/transpose-list-of-lists
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# zip(*l) == zip([1, 2, 3], [4, 5, 6], [7, 8, 9])


transponovana = list(map(list, zip(*hlasy)))
# print(transponovana)

soucty_hlasu = [sum(radek) for radek in transponovana]

kandidati = ["Igor Rezek", "Augustýn Doležal", "Vladan Bednář", "Ondřej Brotz",
             "Radim Kašpar"]


# vysledek = list(zip(kandidati, soucty_hlasu))
#
# max_hlasu = max(soucty_hlasu)
#
# # Print maxima
# for i in vysledek:
#     if i[1] == max_hlasu:
#         print(i[0])
#         break
# # print vsech
# print(vysledek)

# Priklad 13
# https://stackoverflow.com/questions/18072759/list-comprehension-on-a-nested-list
vysledek = []
for kraj in hlasy:
    soucet = sum(kraj)

    procenta = []
    for kandidat in kraj:
        procenta.append((kandidat/soucet) * 100)

    vysledek.append(procenta)

vysledek2 = [[kandidat/sum(kraj)*100 for kandidat in kraj] for kraj in hlasy]


for kraj in vysledek:
    print(kraj)

print()

for kraj in vysledek2:
    print(kraj)
