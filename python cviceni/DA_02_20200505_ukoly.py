import pandas as pd

# UKOL 1

"""
Stáhněte si soubor jmena100.csv, který obsahuje tabulku 100 nejpoužívanějších českých křestních jmen seřazených od nejpoužívanějšího k nejméně používanému. Otevřete Python konzoli a pomocí Pandasu načtěte tuto tabulku jako DataFrame. Jako index zvolte sloupec s názvem ‘jméno’.

Datový soubor obsahuje následující sloupečky

jméno - křestní jméno
četnost - počet obyvatel ČR mající toto jméno
věk - průměrný věk nositelů jména
pohlaví - zda je jméno mužské či ženské
svátek - datum, kdy má dané jméno svátek
původ - původ jména
"""

jmena = pd.read_csv('jmena100.csv', index_col='jméno', encoding='utf-8')

# Vypište na konzoli informace o jménu Martin.
print('\nInformace o jménu Martin.\n')
print(jmena.loc['Martin'])

# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
print('\nInformace pro jména Martin, Zuzana a Josef.\n')
print(jmena.loc[['Martin', 'Zuzana', 'Josef']])

# Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
print('\nInformace o všech nejčastějších jménech až po Martina.\n')
print(jmena.loc[:'Martin'])

# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
print('\nPrůměrné věky osob mající jména mezi Martinem a Terezou.\n')
print(jmena.loc['Martin':'Tereza', 'věk'])

# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
print('\nPrůměrný věk a původ pro všechna jména od Libora dolů.\n')
print(jmena.loc['Libor':, ['věk', 'původ']])

# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
print('\nSloupečky mezi věkem a původem pro všechna jména v tabulce.\n')
print(jmena.loc[:, 'věk':'původ'])


# UKOL 2

"""
Budeme pokračovat s daty o českých jménech z předchozího cvičení. 
Minule jsme používali sloupeček se jmény jako index. 
Tentokrát načtěte soubor se jmény tak, aby Pandas vyrobil index číselný. 
"""

jmena = pd.read_csv('jmena100.csv', encoding='utf-8')

# Vypište všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
print('\nJména, jejichž nositelé mají průměrný věk vyšší než 60.\n')
print(jmena[jmena['věk'] > 60])

# Vypište pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
print('\nJména, kde četnost je mezi 80 000 a 100 000.\n')
print(jmena[(jmena['četnost'] >= 80000) & (jmena['četnost'] <= 100000)]['jméno'])

# Vypište jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
print('\nJména se slovanským původem a jejich četnost.\n')
slovanska = jmena[jmena['původ'].isin(['slovanský'])][['jméno', 'četnost']]
print(slovanska)
print(f'\nPočet: {slovanska.shape[0]}')

print('\nJména s hebrejským původem a jejich četnost.\n')
hebrejska = jmena[jmena['původ'].isin(['hebrejský'])][['jméno', 'četnost']]
print(hebrejska)
print(f'\nPočet: {hebrejska.shape[0]}')

# Vypište všechna jména, která mají svátek prvních 7 dní v únoru.
print('\nJména se svátkem během prvních 7 dní v únoru.\n')
print(jmena[jmena['svátek'].isin(['1.2', '2.2', '3.2', '4.2', '5.2', '6.2', '7.2'])]['jméno'])

# UKOL 3

# Načtěte naše data o českých jménech.
jmena = pd.read_csv('jmena100.csv', encoding='utf-8')

# Vytvoří z něj DataFrame, který obsahuje jména a četnosti jmen, která nejsou ani hebrejského, ani aramejského ani slovanského původu.
jmenaNovyDF = jmena[~jmena['původ'].isin(['hebrejský', 'aramejský', 'slovanský'])][['jméno', 'četnost']]
#print(jmenaNovyDF)

# Převede tento DataFrame na obyčejné Python seznamy. Pomocí chroustání seznamů spočítá součet všech četností těchto jmen.
seznam = jmenaNovyDF.values.tolist()
#print(seznam)
pocet = sum([polozka[1] for polozka in seznam])
print(f'\nSoučet četností jmen v novém DF: {pocet}\n')

# Na výstup vypíše, jaké procentuální zastoupení mají tato jména v celé ČR. Podle odhadů OSN má k osmému květnu 2019 Česká Republika 10 629 798 obyvatel.
print(f'Procentuální zastoupení v ČR: {pocet/10629798*100:.2f} %.')