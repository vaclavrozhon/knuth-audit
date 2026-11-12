# §4.2.3: vymezení kontextu a průměrných časů

Kontrola2.11.2026. Matematické programy a1–8 jsou v
[double-precision.md](double-precision.md), úloha9 v
[dekker-recursive.md](dekker-recursive.md). Tento dokument doplňuje zbytek
textu246–252; nejde o audit všech článků citovaných v okolních sekcích.

Úvod sám výslovně označuje tehdejší motivaci dvojité přesnosti jako historickou.
Jeho poznámky o ceně správného zaokrouhlení a o praktických prioritách nejsou
moderní doporučení ani univerzální matematické dolní meze. Obdobně věta
s „virtually impossible“ u cosinu není tvrzení o formální nevyčíslitelnosti.
Tři požadované vlastnosti cosinu jsou správné: sudost, absolutní hodnota
nejvýše1 a nerostoucnost mezi0 a pi. Popsaný dvouslovný formát má skutečně
osm zlomkových bytů a dvě místa exponentu; znaménko druhého slova se ignoruje.
Záměna NaN a nekonečna je již opravená v erratech2004, terminologie subnormal
v2006; není nový nález.

## Tabulka časů na252

Jde výslovně o **přibližné průměry**, ne o ceny všech vstupů ani o průměr
nad explicitně definovaným konečným prostorem. Přímé sečtení cen instrukcí
dává pro úspěšné původní operace s nenulovými operandy:

```
T_mul = 106 + 6L,
T_div = 123 + 6L + C.
```

Zde L je počet levých normalizačních posunů a C je0/1 podle toho, zda se při
dělení vykoná řádek31 (půjčka do horního slova). Obojí se počítá v MIX
časových jednotkách. Při těchto operacích je L nejvýše1; případné velmi malé
odchylky aproximace od hranice normalizace nemění smysl přibližného průměru.

Pro ideální nezávislé logaritmické zlomky má násobení průměr L=1/2:
logaritmy zlomků jsou nezávislé uniformní veličiny na[-1,0] a polovina
jednotkového čtverce dává součet menší než-1. Pro dělení je pravděpodobnost
`f_u<f_v` také1/2. Proto109 odpovídá `106+6/2`;126.5 odpovídá
`123+6/2+1/2`, kde poslední1/2 je navíc aproximace četnosti půjčky C.
**Tato četnost není automatickým důsledkem samotného logaritmického zákona**;
pro přesný průměr diskrétního programu je třeba určit také rozdělení nízkých
bytů a závislosti. Tabulka netvrdí přesný takový průměr.

U sčítání je přesný výraz

```
T_add = 71 + 13S + 3E + S E + I + 6L - 15Z.
```

S značí provedení výměny operandů, E rovnost velikostí jejich horních slov
při vstupním porovnání, I provedení testu rX na řádku42, Z nulový výsledek.
Všechna čtyři označení jsou indikátory0/1; L opět počítá levé posuny.
Řádky18–40 stojí43, běžná normalizace bez posunu22; vstupní větev bez
výměny6. Průchod45–48 stojí6. Rozdíly ostatních větví dávají uvedené členy.
Pro odčítání se přidají přesně4 jednotky za STA a LDAN.

Původní osmičíselné sčítání vytváří před DNORM obvykle **jeden vedoucí
nulový byte navíc**. Proto k empirickému průměru levých posunů asi0.1
z tabulky4.2.4-2 patří zhruba další `1-0.014-0.03` posunů: nulové výsledky
neposouvají vůbec a přetečení zlomku tuto vedoucí nulu spotřebuje.
S empirickým S přibližně mezi0.5 a0.55 vychází hlavní část průměru asi84.
Shoda horních slov a vstupní test rX přidají další malé členy. Marginalizované
tabulky4.2.4 samy neurčují přesný společný průměr všech těchto indikátorů.
Údaj88 pro odčítání se shoduje s pevným příplatkem4.

[Kontrola48 vybraných tras](../results/double-precision-timing-formulas.json)
a [reprodukční skript](../verify_double_precision_timing.py) ověřují přesné
vzorce, nikoli nedoloženou distribuci všech běhů. Obecné ceny byly odvozeny
sčítáním instrukcí. Tabulka byla poprvé čtena v kontextu1997 programů;
pozdější změna jednoduchého sčítání2002 má vlastní časový rozbor v
[mix-float.md](mix-float.md). Přibližná45.5/49.5 nejsou vydávána za nově
změřený průměr upraveného programu.

## Bibliografické odkazy

Dekker1971: původní časopisecký sken a konkrétně přečtené části jsou doloženy
v [dekker-recursive.md](dekker-recursive.md). Vazba na algoritmus v úloze9
souhlasí; prostá rekurze však vyžaduje samostatný rozbor, který je tam proveden.

Ikebe1965: odkaz na *Note on triple-precision floating-point arithmetic with
132-bit numbers*, CACM8(3),175–177, odpovídá
[záznamu DBLP uloženému u VLDB](https://www.vldb.org/dblp/db/journals/cacm/cacm8.html)
a bibliografii NBS309 z1969. DOI je
[10.1145/363791.363824](https://doi.org/10.1145/363791.363824).
**Plný článek získán nebyl**: vydavatel vrací403, současný DBLP záznam
vrátil ověřovací stránku místo XML. Bibliografické souhlasy jsou pouze
kontrolou citace; obsah třístránkového článku není označen za přečtený
ani jeho algoritmy za nezávisle ověřené. Přístupové výsledky jsou uloženy
v `sources/ikebe-1965-*.json`.

Žádná další historická priorita se zde nepotvrzuje. C0091 zůstává jediným
novým nálezem této sekce; poslední fyzický dotisk nebyl ověřen.
