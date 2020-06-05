"""
1. Studenti - zapni hlavu

Stáhněte si datové sety, se kterými budeme pracovat v tomto cvičení:
jmena100.csv, studenti1.csv, studenti2.csv. První set už známe z minulé lekce.
Druhé dva sety obsahují seznam studentů na nějaké menší IT fakultě. Proveďte
následující úkoly a zodpovězte předložené otázky.

1. Načtěte dva datové sety studentů do oddělených pandas DataFrame a pomocí
   funkce concat je spojte do jednoho setu.

2. Pokud studentovi chybí ročník, znamená to, že již nestuduje. Pokud mu chybí
   číslo skupiny, znamená to, že jde o dálkového studenta. Kolik studentů
   v datovém setu již nestuduje a kolik jsou dálkoví studenti?

3. Vyčistěte data od studentů, kteří nestudují nebo studují jen dálkově.
   Nadále budeme pracovat pouze s prezenčními studenty.

4. Zjistěte, kolik prezenčních studentů je v každém z oborů.

5. Zjistěte průměrný prospěch studentů v každém oboru.

6. Načtěte datový set s křestními jmény. Proveďte join s tabulkou studentů tak
   abychom věděli pohlaví jednotlivých studentů.

7. Zjistěte, zda na naší fakultě studují IT spíše ženy nebo spíše muži.

"""

import pandas as pd

jmena = pd.read_csv('jmena100.csv', encoding='utf-8')
studenti1 = pd.read_csv('studenti1.csv', encoding='utf-8')
studenti2 = pd.read_csv('studenti2.csv', encoding='utf-8')

# spojeni
studenti = pd.concat([studenti1, studenti2], ignore_index=True)

# kolik nestuduje
nestuduji = studenti[studenti['ročník'].isnull()]
# print(nestuduji.shape)
print(f"Nestuduje: {(nestuduji.shape)[0]}")

# kolik jsou dalkovy
dalkovi = studenti[studenti['kruh'].isnull()]
# print(dalkovi.shape)
print(f"Dalkovych: {(dalkovi.shape)[0]}")

dalkovi_nestuduji = studenti[
    studenti['kruh'].isnull() & studenti['ročník'].isnull()]

print(f"Dalkovi a uz nestuduji: {(dalkovi_nestuduji.shape)[0]}")

# smazeme ty co jsou dalkovi a co uz nestuduji
studenti = studenti.dropna()

# kolik je v kazdym oboru lidi
print(studenti.groupby('obor')['jméno'].count())

# prumer studentu
print(studenti.groupby('obor')['prospěch'].mean())

# join tak abychom vedeli pohlavi
studenti_pohlavi = pd.merge(studenti, jmena, on=['jméno'])
print(studenti_pohlavi)

# zeny a muzi
print(studenti_pohlavi.groupby('pohlaví')['jméno'].count())
