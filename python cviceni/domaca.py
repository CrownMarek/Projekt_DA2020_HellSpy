"""
Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte nejdříve na všechna pímena malá a poté na všechna písmena velká.

jmeno = 'Veronika'
volanie = (jmeno).upper()
volanie2 = (jmeno).lower()
print(volanie,volanie2)
"""
"""
Mějme seznam desetinných čísel zadaných jako text

hodnoty = ['12', '1', '7', '-11']
Potřebujeme k třetímu číslu v seznamu přičíst 4, aby vysledek vypadal takto:

hodnoty = ['12', '1', '11', '-11']

hodnoty = ['12', '1', '7', '-11']
a = hodnoty[2]
vysledek = int(a) + 4
hodnoty[2] = vysledek
print(hodnoty)
"""
"""
Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána nikoliv v seznamu ale v řetězci oddělená mezerou K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto

hodnoty = '12.1 1.68 7.45 -11.26'
Určitě se vám budou hodit metody split a join.
#####
hodnota = '12.1 1.68 7.45 -11.51'
hodnota2 = hodnota.split()
hodnota3 = float(hodnota2[-1]) + 0.25
hodnota2[-1]= str(hodnota3)
hodnota =' '.join(hodnota2)
print(hodnota2)
"""
# počet kilometrov
"""
kilometry = [2.4, 2.6, 0, 3.5, 1.8]
zaok = [round(beh) for beh in kilometry]
print(zaok)
"""
"""
pisemky = [
  [1, 3, 2, 1],
  [3, 1, 1, 2],
  [4, 2, 2, 2],
  [1, 1, 1, 1],
  [1, 2, 2, 1],
  [1, 4, 1, 3] ]

prvni = [znamky[0] for znamky in pisemky]
print(prvni)
"""
"""
 Vytvořte seznam, který obsahuje

každé z čísel ze seznamu cisla vynásobené dvěma,
každé z čísel ze seznamu cisla s opačným znaménkem,
každé z čísel ze seznamu cisla umocněné na druhou,
každé z čísel ze seznamu cisla jako řetězec.
cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
prve = [cislo * 2 for cislo in cisla]
druhe = [cislo * -1 for cislo in cisla]
tretie =[cislo **2 for cislo in cisla]
stvrte = [str(cislo) for cislo in cisla]
print(prve, druhe, tretie, stvrte)
"""
""""
Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
Vytvořte seznam průměrných teplot pro každý den.
Vytvořte seznam ranních teplot.
Vytvořte seznam nočních teplot.
Vytvořte seznam dvouprvkových seznamů obsahujících pouze denní a noční teplotu.
Spočítejte celkovou průměrnou teplotu za celý týden.

teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]

priemer =[sum(teplo)/len(teplo) for teplo in teploty]
rano = [rano[0] for rano in teploty]
vecer = [vec[-1] for vec in teploty]
dennoc= [[dn[1],dn[3]] for dn in teploty]
tyden = (sum(priemer)/ len(priemer))
print("zoznam priemerných teplot je" ,priemer)
print("zoznam ranných teplot je", rano)
print("zoznam nočných teplot je", vecer)
print("denné a nočné teploty sú", dennoc)
print("piermerná týždenná teplojta je",round(tyden,2))
"""
"""
seznam = [1, 4, 9, 16, 25, 36, 49, 64]
a =[x**0.5 for x in seznam] #odmocnina
b = [x % 2 for x in seznam] #zistenie zbytku čisla pri delení dvoma
c = [[x // 2, x % 2] for x in seznam] # vydelenie čisla dvoma zo zvyškom
print(a,b,c)
"""
"""
seznam = ['12.10.2014', '10.01.2015', '06.06.1986']
a = [int(datum[3:5]) for datum in seznam] #určí presný mesiac
b = [int(datum[:2])-1 for datum in seznam] # den zmenení o jeden 
c = [int(datum[:2]), int(datum[3:5]), int(datum[6:])] for datum in seznam
]# určí celý datum
print(a, b, c)
"""
"""
vek = 9
print(vek == 89)
"""
"""
Ověřování věku
pohodička
Následující seznam obsahuje věky uživatelů naší malé sociální sítě.

veky = [35, 12, 44, 11, 18, 21, 28, 18]
Vytvořte pomocí chroustání seznamů seznam celých čísel, které udávají, kolik jednotlivým uživatelům zbývá do 18ti let. Záporná čísla budou znamenat, že uživatel už věk překročil.
Vytvořte pomocí chroustání seznamů seznam pravdivostních hodnot, které udávají, který uživatel je starší 18ti let.
Vytvořte pomocí chroustání seznamů seznam pravdivostních hodnot, které udávají, který uživatel má přesně 18 let.
veky = [35, 12, 44, 11, 18, 21, 28, 18]
zaznam = [ vek -18 for vek in veky]
starsi = [ vek >18 for vek in veky]
ma18 = [vek ==18 for vek in veky]
print(zaznam)
print(starsi)
print(ma18)
"""
"""
nazvy = [
  'Někdo to rád horké, extended edition',
  'Adéla ještě nevečeřela',
  'Kulový blesk'
]
"""

"""
"""
"""
delky = str[1,2,3]
znak = [ cast + '+' for cast in delky]
print(znak)
"""
"""
delky = [136, 105, 82]
a = [ str(m // 60) + ":" + str(m % 60) for m in delky ]
print(a)
"""
"""
delky = str([1,2,3])
znak = [ cast + ':' for cast in delky]
print(znak)
"""
""""
kraje = [
  ['Hlavní město Praha', '1280508'],
  ['Jihočeský kraj', '638782'],
  ['Jihomoravský kraj', '1178812'],
  ['Karlovarský kraj', '296749'],
  ['Kraj Vysočina', '508952'],
  ['Královéhradecký kraj', '550804'],
  ['Liberecký kraj', '440636'],
  ['Moravskoslezský kraj', '1209879'],
  ['Olomoucký kraj', '633925'],
  ['Pardubický kraj', '517087'],
  ['Plzeňský kraj', '578629'],
  ['Středočeský kraj', '1338982'],
  ['Ústecký kraj', '821377'],
  ['Zlínský kraj', '583698']
]
sez1 = [sez[0] for sez in kraje]
sez2 = [int(sez[1]) for sez in kraje]
seznam = [sez1,sez2]
print(seznam)
"""
"""
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
Rezek = sum([(volba[0]) for volba in hlasy ])
print("Rezek získal ", Rezek, " hlasov")
Doležal = sum([(volba[1]) for volba in hlasy ])
print("Rezek získal ", Doležal, " hlasov")
Bednar = sum([(volba[2]) for volba in hlasy ])
print("Bednár získal ", Bednar, " hlasov")
Brotz = sum([(volba[3]) for volba in hlasy ])
print("Brotz získal ", Brotz, " hlasov")
Kašpar = sum([(volba[4]) for volba in hlasy ])
print("Kašpar získal ", Kašpar, " hlasov")

zoznam =max([Rezek,Doležal, Bednar, Brotz,Kašpar])
if zoznam == Rezek:
  vyherca = "Rezek"
elif zoznam == Doležal:
  vyherca = "Doležal"
elif zoznam == Bednar:
  vyherca = "Bednar"
elif zoznam == Brotz:
  vyherca = "Brotz"
elif zoznam == Brotz:
  vyherca = "Brotz"
elif zoznam == Kašpar:
    vyherca = "Kašpar"
print("Voľby vyhral: ", vyherca, "s", zoznam, "hlasmi")

Hlavní_město_Praha
Středočeský_kraj
Jihočeský_kraj
Plzeňský_kraj
Karlovarský_kraj
Ústecký_kraj
Liberecký_kraj
Královéhradecký_kraj
Pardubický_kraj
Kraj_Vysočina
Jihomoravský_kraj
Olomoucký_kraj
Zlínský_kraj
Moravskoslezský_kraj
"""

"""
Králičí farma si objednala sestavení modelu množení králičí populace, aby dokázala odhadnout své zisky. Model funguje takto.

Počet králičích párů na farmě v aktuálním roce (např. 2005) získáme tak, že sečteme počet králíků na farmě v roce minulém (2004) a roce předminulém (2003). Pokud tedy například v roce 2003 žilo na farmě 13 párů a v roce 2004 zde žilo 21 párů, model předpovídá, že v roce 2005 zde bude žít 13 + 21 tedy 34 králičích párů.

Králičí farma započala svůj chov v předminulém roce (2017) s nulovým počtem králíků a v minulém roce 2018 pořídili svůj první králičí pár. Uložte si tyto počty do proměnných predminuly a minuly. V aktuálním roce 2019 tak máme stále jeden pár (predminuly + minuly). Uložte tuto hodnotu do proměnné aktualni.

Zodpovězte následující otázky:

Kolik králičích párů bude mít farma za deset let, tedy v roce 2029?
Kdy bude mít farma alespoň 300 králičích párů?
"""
"""
predminuly = 0
minuly = 1
rok = 2
aktualni = predminuly + minuly
print("Rok: ", rok, "Paru: ", aktualni)
rok = rok + 1
predminuly = minuly
minuly = aktualni
aktualni = predminuly + minuly
print("Rok: ", rok, "Paru: ", aktualni)
rok = rok + 1
predminuly = minuly
minuly = aktualni
"""
"""
#Do místnosti tvaru čtverce o rozloze 30 m2 potřebujeme koupit nový koberec. Jakou délku má mít strana koberce? Vejde #se nám srolovaný do dodávky s nákladovým prostorem dlouhým 5 m?
strana = 30**0.5
if strana <= 5.00 :
  print("koberec sa vôjde")
else:
  print("Koberec sa nevôjde do dodávky.")
  """

"""seznam = [1,2,3,5,6,7]
seznam2 =[3,7,6,8]
prumer1 = [sum(sez)/len(sez) for sez in seznam]
#prumer2 =sum(seznam2/len(seznam2))
print(prumer1)
"""
"""
Vytvoř 2 proměnné. Do jedné ulož nějaké heslo (jako text) a do druhé vstup od uživatele.
Pokud se hodnota zadaná uživatelem bude rovnat heslu v proměnné, tak vypiš "přihlášen", v
opačném případě "přístup zamítnut". 
"""
