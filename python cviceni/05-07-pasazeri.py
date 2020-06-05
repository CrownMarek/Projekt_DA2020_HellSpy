pasazeri = open('pasazeri.txt', encoding='utf-8')
jizdy = []
for radek in pasazeri:
    radek = radek.strip('\n')
    radek = radek.split(' ')
    #pro kazdy den bude vnoreny seznam, na indexu 0 vnoreneho seznamu bude seznam vsech 4 jizd tam a na indexu 1 seznam vsech 4 jizd zpet
    den =  [[int(jizda.split(',')[0]) for jizda in radek],[int(jizda.split(',')[1]) for jizda in radek] ]
    jizdy.append(den)
#kontrolni print
print(jizdy)
celkem_tam = 0
celkem_zpet = 0
for den in jizdy:
    celkem_tam += sum(den[0])
    celkem_zpet += sum(den[1])
print('1. den tam:', sum(jizdy[0][0]), 'zpet:', sum(jizdy[0][1]))
print('za cely tyden tam:', celkem_tam, 'zpet:', celkem_zpet)
