hodin = 7
mzdou = 450
dnu = 21

prijem = 7 * 450 * 21
print("prijem", prijem)

pausal = 0.6
naklady = prijem * pausal
print("naklady", naklady)

zaklad = prijem - naklady
print("zaklad", zaklad)

dan = zaklad * 0.15
print("dan", dan)

print("cisty prijem", prijem - dan)

