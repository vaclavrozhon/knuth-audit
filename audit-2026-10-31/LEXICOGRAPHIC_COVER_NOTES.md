# Lexikografické řešení — 7.2.2.1–36

Kontrola 1. listopadu 2026. Zadání na tištěné straně 127, odpověď na 422
(PDF strany 147 a 442). Vizuálně porovnána odpověď s autorským PS,
tištěná strana 126 v `sources/fasc5c.pdf`. Oba lokální obrazy mají **4.2 Gμ**.
Textový výstup internetového vyhledávání s hodnotou 2.4 není dokladem změny
v našich vydáních; pro čtení čísel jsou rozhodující obrazy stránek.

## Co bylo ověřeno

`check_dlx_lexicographic.py` doslovně rozšiřuje již prověřený spacerový
Algorithm X o proměnnou LL, návrat z nalezeného svědka a snížení LL při
obvyklém návratu. Větev „otherwise“ v odpovědi X2 čteme uvnitř testu
`RLINK(0)=0`: mění zacházení s nalezeným řešením. Její nepodmíněné provádění
při každé návštěvě X2 by zcela odstranilo zamýšlené použití MRV.

Nezávislý oracle vybere všechny podmnožiny vstupních řádků, přímo ověří
pokrytí primárních a nepřekrývání všech položek a každé řešení zapíše
kanonickou cestou: první zbývající primární položka, pak index jejího
zvoleného řádku. Pořadí uzlů dané položky souhlasí s pořadím vstupních řádků.
Tím kontroluje celé uspořádané seznamy, nikoli jen počet nebo první řešení.

Výsledek `results/lexicographic/literal.json`:

- 9 028 běhů s různými možnostmi, nejvýše čtyři položky a čtyři možnosti;
- 392 běhů se čtyřmi možnostmi včetně opakování;
- všech 10 464 řešení ve správném pořadí, 4 359 návratů z MRV svědka;
- 38 992 kontrol stavů X2 a 63 108 přesných obnov cover/uncover;
- každý kladný počet primárních položek, obě pořadí různých řádků.

## Proč mechanismus LL funguje

Uvažujme neprázdnou počáteční množinu primárních položek. Na úrovních až
po LL se používá první zbývající položka a její možnosti se zkoušejí ve
vstupním pořadí. Úrovně nad LL pouze zjišťují existenci doplnění současného
kanonického prefixu; mohou používat libovolné úplné hledání včetně MRV.

Pokud toto hledání doplnění nenajde, lze příslušný prefix přeskočit, protože
nemá žádné řešení. Když doplnění najde v hloubce větší než LL+1, víme, že
zvolená možnost na úrovni LL má doplnění. Zvýšíme LL a přesně odvoláme
všechna hlubší rozhodnutí v opačném pořadí. Zachovaný prefix se nezměnil,
ale následující volba již bude kanonická. Z nalezeného svědka tedy nevzniká
výstup v chybném pořadí; svědek pouze ospravedlní další prohloubení prefixu.

Je-li dokončené řešení v hloubce LL+1, všechna jeho rozhodnutí už byla
kanonická a může se vypsat. Obvyklý návrat projde další možnost stejného
prefixu. Pokud se vrátíme nad LL, snížení LL zajistí správný režim dalšího
hledání. Indukce podle kanonického stromu dává úplnost, jedinečnost a
lexikografické pořadí. Strom je konečný a každé prohloubení spotřebuje
alespoň jednu primární položku, takže pomocné hledání nemůže bránit ukončení.

Tentýž argument používá jen platnost zvoleného prefixu, úplnost hledání a
přesné odvolání změn. Platí tedy i pro barevný Algorithm C, pokud jeho vlastní
operace commit/uncommit provedeme správně. Tento blok netestuje doslovnou
implementaci barevných struktur C; není to tvrzení o dokončení auditu C.

## C019 — počáteční prázdné řešení

Při nulovém počtu primárních položek a nulovém počtu možností má Algorithm X
jediné prázdné řešení. To platí i tehdy, obsahuje-li instance nepoužité
sekundární položky. Na začátku je ovšem `l=LL=0`. Vytištěný test
`l=LL+1` neuspěje; LL vzroste na 1 a následuje výběr položky z prázdného
aktivního seznamu.

Doslovný test zachycuje tento stav pro n=0 i pro dvě nepoužité sekundární
položky. Jednorázové přijetí počátečního prázdného řešení problém opraví;
alternativně lze výslovně požadovat kladný počáteční počet primárních položek.

**Klasifikace: nízká závažnost, kandidát na upřesnění.** Je to okraj konvence
o přípustných rozměrech, podobně jako C018. Algoritmus pro kladný počet
primárních položek tuto potíž nemá. PDF i PS mají stejnou inicializaci;
relevantní errata neobsahují odpovídající změnu. Nezapočítáváme jako potvrzený
nový nález. Fyzický výtisk nebyl kontrolován.

## Nativní provedení a 32 dam

`dlx1-lexicographic.ch` aplikuje mechanismus LL na archivovaný původní DLX1.
Je to auditní úprava, nikoli nalezený historický Knuthův program pro úlohu 36.
`check_dlx_lexicographic_native.py` sestaví tuto variantu a samostatnou
variantu volící vždy první položku. Zdrojové i binární hashe a sestavovací
příkazy jsou v `results/lexicographic/native-build.json`.

Všech 18 úplných seznamů pro n=1 až 9 souhlasí s nezávislým souřadnicovým
backtrackingem. Každé rozmístění je navíc zkontrolováno na řádky, sloupce
a obě úhlopříčky. Pro n=32 obě metody vracejí přesně všech 32 hodnot knihy:

```text
1 3 5 2 4 9 11 13 15 6 18 24 26 30 25 31
28 32 27 29 16 19 10 8 17 12 21 7 14 23 20 22
```

Při primárním pořadí r1,…,r32,c1,…,c32 má varianta LL+MRV
9 190 176 uzlů a 4 125 263 016 memů; bez MRV 87 491 426 uzlů a
35 619 100 543 memů. Druhý údaj reprodukuje knižní zaokrouhlení 35.6 Gμ.
První je přibližně o 1.8 % pod knižními 4.2 Gμ. Odlišné účtování či pořadí
nerozhodnutých položek může měnit časování; samotný rozdíl není důkaz chyby.
Další přesně specifikovanou změnu pořadí sloupců eviduje
`check_dlx_order_costs.py` a `results/lexicographic/n32-lex-organpipe-columns.json`.
Tato varianta dává 4 119 678 486 memů a stejné první řešení; přesný rozdíl
proti historickým 4.2 Gμ tedy nevysvětlila.

Před prvním přijetím výsledků byly opraveny dvě vlastní chyby change souboru:
chybějící úvodní `@ ` u značky CWEB a potřebné složené závorky kolem jeho
rozvinutého bloku. Netýkají se knihy. Finální soubor se sestavil a prošel
všemi uvedenými porovnáními.

## Historie a zbylý rozsah

Archivovaný primární [článek Fischettiho a Salvagnina](https://arxiv.org/abs/1907.08246)
má 14 stran a v příloze výsledky pro 56–61 a další větší rozměry.
[OEIS A141843](https://oeis.org/A141843) obsahuje Knuthův datovaný komentář
z 23. července 2019: tehdy byl prvním nezjištěným případem n=62 a výsledky
48–55 připisuje Schubertovi. Při rešerši 1. listopadu 2026 nebyl nalezen nový
doložený výsledek pro 62; to samo o sobě nedokazuje jeho dnešní nevyřešenost.
OEIS uvádí prosinec 2017, kniha listopad; zveřejnění a první výpočet mohou
být různé události. Přesný měsíc prvního výpočtu zde nezávisle nepotvrzujeme.

Úloha 36 zůstává **partial** pro historické časování a přesný historický
měsíc. Obecný mechanismus, úplné pořadí malých modelů a první řešení pro 32
jsou ověřeny; otevřený okraj nprim=0 je veden samostatně jako C019.
