# §2.2.3-26–27: výběr podprogramů a jejich umístění

Přečteny obrazy s.271–272 a549–550. Výběr podprogramů je
výpočet dosažitelnosti v orientovaném grafu závislostí, nikoli
topologické třídění: cyklické závislosti jsou dovoleny.

## Reprezentace a obecný důkaz

Záznam adresáře začíná hlavičkou s velikostí SPACE a odkazem LINK
na další podprogram v pořadí pásky. Za ní je n≥0 odkazů závislostí,
po dvou ve slově. Poslední slovo záznamu má B=−1, ostatní B=0;
lichý poslední odkaz má druhý slot0. Bez závislostí je posledním
slovem už hlavička. X[1..N] obsahuje požadované hlavičky.

A0 označí všechny přímo požadované hlavičky přičtením2 do B,
ale pouze pokud B≤0. Původní0 se mění na2, původní−1 na1.
V originále je v A0 i A3 skutečně **≤**, přestože OCR vynechává
vodorovnou čárku. Označení nelze aplikovat dvakrát.

Invariant A1: každý označený podprogram byl buď původně požadován,
nebo je závislostí označeného podprogramu. Každý označený
podprogram, jehož závislosti ještě nebyly zpracovány, je na
zásobníku X (případně je právě zpracováván). A3 přidá dosud
neoznačený požadovaný podprogram a současně jej označí, takže
cyklus závislostí nemůže generovat nekonečnou posloupnost vložení.
Každá hlavička je nově vložena nejvýše jednou; počáteční duplicitní
požadavky mohou způsobit opětovné čtení, ale ne nové označování.

A2 pozná konec záznamu podle |B(P)|=1. Platí to i pro označenou
bezodkazovou hlavičku s B=1. U označené neukončující hlavičky je
B=2 a pokračování stále obsahuje0 nebo−1. Posun P o1 proto čte
právě slova uvnitř daného záznamu; nulový doplňovací druhý slot
se nikdy nepovažuje za hlavičku adresáře.

Po vyprázdnění zásobníku je označená množina uzavřená na všechny
závislosti a obsahuje počáteční požadavky. Žádný jiný vrchol nebyl
označen. Jde přesně o nejmenší uzavřenou množinu, tedy množinu
všech dosažitelných podprogramů.

V B1–B4 se prochází **pořadí pásky**, ne pořadí přidělených adres.
Po zpracování libovolného prefixu má X právě všechny požadované
podprogramy z tohoto prefixu ve správném pořadí. MLOC je původní
základ plus součet jejich délek. Nový vybraný záznam dostane
aktuální základ; zvětšení o SPACE zajistí navazující, nepřekrývající
se intervaly. Nulová délka je neškodná. Po konci pásky dostane
poslední položka SUB=0 a BASE první nevyužitou adresu.

Počáteční N=0 dává prázdný výběr a právě tuto koncovou položku.
Dostatek místa pro pracovní zásobník a výsledné X, platnost adresáře
a nepřetečení adresních/velikostních polí jsou vstupní předpoklady;
nejde o validátor poškozeného adresáře.

## MIX a známé erratum

MIX používá B=(0:1), tedy znaménko a první bajt. A2 záměrně
čte pouze(1:1): testuje absolutní hodnotu B. A0/A3 s JAP rozlišují
kladné označení od obou nekladných počátečních hodnot a provedou
stejnou transformaci0→2,−1→1. Jen označené hlavičky mohou mít
kladné B; pokračovací slova se neoznačují.

V první fázi je rI1 velikost zásobníku. Původní skok při N=0
přeskočí jeho inicializaci a není správný pro obecný vstupní rI1.
Známé erratum26.2.2008 opravuje J2Z B1 na J2Z 2F a přidává
2H před LD1 N. Tato oprava byla přečtena v originále vrstvy
all1-prepre,s.41 a v běhu reprodukována (nenulový počáteční rI1).
Po ní rI1 při přechodu do druhé fáze vždy obsahuje0.

B1 má zdánlivě překvapivé `ENT2 FIRST`, nikoli `LD2 FIRST`.
Je to **správně**: nejprve uloží první BASE a skočí přes B3
k B4, kde `LD2 0,2(LINK)` dereferencuje právě proměnnou FIRST.
Teprve pak začne skutečný první záznam. Další průchody B4
načítají LINK skutečné hlavičky. Není dovoleno v testovacím
harnessu zaměnit symbol FIRST za adresu prvního záznamu;
je to adresa slova obsahujícího tento odkaz.

Druhá fáze předem zapisuje BASE příští položky. U vybrané
hlavičky zvýší rI1, do této již připravené položky zapíše SUB,
přičte SPACE a připraví BASE následující položky. Po skončení
vynuluje SUB poslední položky. MLOC se drží v rA; zápis zpět
do původní proměnné není požadovaným výstupem zadání.

`check_programs.py` s nezávislým průchodem grafu testuje160
instancí pro radix64/100, včetně nulového N, prázdného adresáře,
cyklů, sdílených závislostí, opakovaných požadavků, nulových délek
a pořadí pásky odlišného od adres. Testy nejsou důkazem pro
všechny adresáře; tím jsou invarianty výše. Přesný příklad272
má označené hlavičky1003,1010,1000,1006,1002 a výsledné pořadí
1002,1010,1006,1000,1003 se základy2400,2430,2450,2510,2530,
koncovým2730. Každý součet odpovídá příslušným SPACE30/20/60/20/200.
