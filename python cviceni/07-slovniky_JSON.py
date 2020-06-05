"""
Cvičení - slovníky
1 Kurz

Založte si program v Pythonu a zkopírujte si do něj datovou strukturu kurzu
Úvod do programování z lekce výše.

    Vypište na výstup počet účastnic na posledním konání kurzu.
    Vypište na výstup jméno posledního kouče na prvním konání kurzu.
    Vypište na výstup celkový počet konání kurzu.
    Vypište na výstup všechna místa, na kterých se kurz konal. Použijte c
    hroustání seznamů.
"""

kurz = {
    'nazev': 'Úvod do programování',
    'lektor': 'Martin Podloucký',
    'konani': [
        {
            'misto': 'T-Mobile',
            'koucove': [
                'Dan Vrátil',
                'Filip Kopecký',
                'Martina Nemčoková'
            ],
            'ucastnic': 30
        },
        {
            'misto': 'MSD IT',
            'koucove': [
                'Dan Vrátil',
                'Zuzana Tučková',
                'Martina Nemčoková'
            ],
            'ucastnic': 25
        },
        {
            'misto': 'Škoda DigiLab',
            'koucove': [
                'Dan Vrátil',
                'Filip Kopecký',
                'Kateřina Kalášková'
            ],
            'ucastnic': 41
        }
    ]
}
print(kurz['konani'][-1]['ucastnic'])
print(kurz['konani'][0]['koucove'][-1])
print(len(kurz['konani']))
print([konani['misto'] for konani in kurz['konani']])

"""
2 Knihovna

Uvažte, jak byste pomocí slovníku reprezentovali údaje o knize v knihovně. 
Jaké klíče a hodnoty ve slovníku budou? Zcela jistě bude každá kniha obsahovat 
například název. Chtěli bychom také, aby kniha umožňovala mít vícero autorů a 
vícero vydání. Ve vašem programu vytvořte proměnnou, který bude obsahovat 
jednu knihu s vámi vymyšlenou strukturou.
"""
knihovna = {
    'Adresa': "Za sedmero horami 365",
    'knihy': [
        {
            'ISBN': '123459876-6',
            'Nazev': 'Harry Potter',
            'Rok vydani': 2000
        },
        {
            'ISBN': '8654566-4',
            'Nazev': 'Pan prstenu',
            'Rok vydani': 1976
        }
    ]
}

# pocet knih v knihovne
print(len(knihovna['knihy']))

# nazvy vsech knih
[print(kniha['Nazev'])for kniha in knihovna['knihy']]

"""
3 Recepty

Prohlédněte na následujicí reprezentaci receptu:
"""

recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

"""
Uložte si tuto strukturu do proměnné recept na začátek nového programu. 
Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na
celé koruny nahoru.

"""
# from math import ceil
#
# # jako prvni me logicky napadlo vytahnout si jen ceny ze slovniku
# # jde to urcite udelat ve vice krocich, cviceni na indexaci
#
# ceny = [ingredience[-1] for ingredience in recept['ingredience']]
# print(ceny)
#
# # potrebuju dat pryc Kc a prevest na cislo, pouziju split a vezmu si jen
# # prvni prvek ze splitu (teda to cislo)
# ceny_cisla = [cena.split()[0] for cena in ceny]
# print(ceny_cisla)
#
# # ted to predelam na cisla at s tim muzu pocitat (bud na float nebo int)
# ceny_final = [float(cena )for cena in ceny_cisla]
# print(ceny_final)
#
# # no a staci dat sum a zaokrouhlit (pouzivam ceil z math)
# print(f"Cele jidlo bude stat: {ceil(sum(ceny_final))} Kc")


"""
Cvičení - API a JSON
4 Seznam lidí

Jak už jsme si ověřili v lekci, datové API na adrese 
http://api.kodim.cz/python-data/people obsahuje seznam lidí. Napište program, 
který tento seznam z API stáhne a převede z formátu JSON na Python slovníky. 
Proveďte následující úkoly.

    Zjistěte kolik lidí celkem seznam obsahuje.
    Zjistěte jaké všechny informace máme o jednotlivých osobách.
    Zjistěte, kolik je v souboru mužů a žen.
# """
# import requests
# import json
# response = requests.get('http://api.kodim.cz/python-data/people')
#
# # data uz je slovnik kde muzu indexovat jak je libo
# data = json.loads(response.text)
# # pocet lidi (staci mi funkce len, protoze cele je to jeden seznam)
# pocet_zaznamu = (len(data))
# print(pocet_zaznamu)
#
# # funkce keys vraci klice daneho slovniku (predpokladam tady ze prvni zaznam
# # ma stejne klice jako vsechny ostatni zaznamy)
# print(data[0].keys())
# print([i for i in data[0])
# #
# muzi = len([zaznam for zaznam in data if zaznam['gender'] == 'Male'])
# zeny = len([zaznam for zaznam in data if zaznam['gender'] == 'Female'])
# ostatni = pocet_zaznamu - muzi - zeny
#
# print(f"Zeny: {zeny}\nMuzi: {muzi}\nOstatni: {ostatni}\n")

"""
5 Svátky

Na adrese http://svatky.adresa.info/json najdete API, které vám odpoví, 
kdo má dneska svátek.

    Využijte toto API k tomu, abyste napsali program, který po spuštění 
    vypíše na obrazovku kdo má dneska svátek.
    Pokud použijete adresu http://svatky.adresa.info/json?date=DDMM, kde místo
     DDMM doplníte datum, dostanete jméno, které má svátek v zadaný den. 
     Formát DDMM znamená že 6. ledna bude zapsáno jako 0601, 12. září jako 1
     209 apod. Napište program, který dostane na příkazové řádce číslo dne a 
     číslo měsíce a vypíše na výstup kdo má v daný den svátek. Použijte váš 
     program abyste zjistili, kdo má svátek 29. února.
"""
import requests
import json
import sys


# resp = requests.get('http://svatky.adresa.info/json')
# data = json.loads(resp.text)
#
# # 22.2
# print(data[0]['name'])

def kdo_ma_svatek(den, mesic):
    if len(den) != 2 or len(mesic) != 2:
        return "Error: Musis zadat den a mesic ve formatu DD respektive MM"

    resp = requests.get('http://svatky.adresa.info/json?date=' + den + mesic)
    data = json.loads(resp.text)
    return [zaznam['name'] for zaznam in data]


print(kdo_ma_svatek(sys.argv[1], sys.argv[2]))