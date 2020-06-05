"""
1. Porozumění HTML

Cílem tohoto cvičení je pokusit se vyznat ve zdrojovém kódu jednoduché webové
stránky a získat tak povědomí o tom jak funguje jazyk HTML. Postupujte dle
následujících kroků.

Stáhněte si následující ZIP soubor, který rozbalte někam na váš počítač.
V rozbalené složce dhmo rozkliněte soubor index.html. V prohlížeči by se vám
měla otevřít jednoduchá webová stránka pojednávající o škodlivosti jedné velmi
zajímavé chemikálie. Stránka nevypadá příliš vábně, protože není napojena na
žádné CSS styly, a vidíme tedy jen čistý obsah.

Složku dhmo si otevřete ve Visual Studiu a podívejte se na obsah souboru
index.html. Uvidíte spoustu HTML značek. Některé z nich znáte, některé jste
v životě neviděli. Nenechte se vylekat tím, že některým částem tohoto souboru
vůbec nerozumíte. Zkuste v souboru najít nějaký kousek textu, který vidíte na
vaší otevřené webové stránce a tím se trochu zorientovat.

V úvodním odstavci stránky jsou tři překlepy. Opravte je přímo v souboru
index.html. Nezapomeňte jej uložit. Obnovte stránku ve vašem prohlížeči
(zkratka Ctrl+R nebo CMD+R) a měli byste vidět změny, které jste provedli.

Najděte v souboru index.html část, která obsahuje výčet faktů o DHMO. Tyto
seznamy jsou číslované, což naznačuje HTML značka <ol>. Změňte u obou seznamů
tuto značku na <ul>, což znamená nečíslovaný seznam. Nezapomeňte změnit i
uzavírací značku seznamu (ta s lomítkem). Otevírací a uzavírací značky musí
vždy souhlasit!

Najděte poblíž začátku souboru index.html značku <img>, která do stránky
vkládá úvodní obrázek. Atribut src udává cestu k souboru s obrázkem. Všimněte
si, že blízko ke konci souboru těsně před seznamem odkazů je ještě jedna značka
<img>, které ale atribut src chybí a proto na stránce žádný obrázek nevidíme.
Nastavte atribut src na hodnotu img/dhmo-ban.png a podívejte se, jak se stránka
změnila.

Podobně jako náš obrázek, poslední odkaz v seznamu odkazů nemá atribut href,
což způsobuje, že se odkaz na stránce nezobrazuje jako odkaz. Atribut href
říká, na kterou adresu má odkaz vést. Nastavte proto v posledním odkazu hodnotu
atributu href na http://www.snopes.com/science/dhmo.asp.

Téměř na začátku souboru index.html najdete značku <title>. Ta udává
název stránky, který se zobrazuje v záložce prohlížeče. Změňte tento název
prostě na “DHMO šíří hrůzu”.
Pokud chcete vidět, jak by tato stránka vypadala nastylovaná, vložte na nový
řádek před značkou <title> tento kód

<link rel="stylesheet" href="style.css" />

Uložte soubor, obnovte stránku v prohlížeči a kochejte se.
"""

from requests_html import HTMLSession

"""
2. Scraping DHMO

Napište program, který bude pracovat se stránkou o DHMO na adrese 
http://scrape.kodim.cz/dhmo/index.

    Nechť program vypíše na výstup nadpisy všech sekcí (značka h2).
    Nechť program vypíše na výstup cesty všech odkazů na stránce 
    (značka a, atribut href).
    Nechť program vypíše na výstup cesty ke všem obrázkům na stránce 
    (značka img, atribut src).
"""
#
# session = HTMLSession()
# stranka = session.get('http://scrape.kodim.cz/dhmo/index')
#
# # sekce
# for nadpis in stranka.html.find('h2'):
#     print(nadpis.text)
#
# # odkazy
# for odkaz in stranka.html.find('a'):
#   print(odkaz.attrs['href'])
#
# # obrazky
# obrazky = stranka.html.find('img')
# for obrazek in obrazky:
#   print(obrazek.attrs['src'])
# # Ulozeni do souboru
# soubor = open("result.csv", "w")
# for obrazek in obrazky:
#     soubor.write(obrazek.attrs['src']+"\n")
"""
3 Scraping Kodim.cz

Jistě vás nepřekvapí, že stránky, které právě čtete, se dají také snadno 
scrapovat.

Napište program, který vypíše na výstup všechny povinné a nepovinné domácí 
úložky z lekce První programy spolu s jejich obtížností.
"""
session = HTMLSession()
stranka = session.get(
    'http://nove.kodim.cz/czechitas/python-data/zaklady-programovani/prvni-programy')

# najde vsechny cisla cviceni
index = stranka.html.find('.exercise__num')[8:]

# najde vsechny nadpisy cviceni
nadpisy = stranka.html.find('.exercise h3')[8:]

# najde vsechny obtiznosti cviceni
obtiznosti = stranka.html.find('.exercise .demand-text')[8:]

# VYSVETLENI MEHO POSTUPU
# No me nenapadl lepsi zpusob jak to vyfiltrovat, takze jsem si v html kodu
# nasla ze bych mela zacit vypisovat od devateho cviceni, jelikoz vysledky
# jsou listy(vsechny stejne dlouhe), tak mi staci vsechno indexovat od devate
# polozky tedy [8:]
# Udelala jsem si zvlast tri listy ciste proto, ze to chci vypisovat vedle
# sebe, slo by najednou vyhledat vsechny tri polozky a oddelit je carkou
# jako jsme si ukazovali

for i in range(len(obtiznosti)):
    # trocha cerne magie s f stringy :)
    print(f"{index[i].text:>2}. "
          f"{nadpisy[i].text.strip('¶ ')} - "
          f"{obtiznosti[i].text}")
