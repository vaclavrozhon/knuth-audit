# C$ a úlohy 247–250 — zdrojový průchod

Dokončeno 3. listopadu 2026. Rozsah: konec hlavní strany 116, celé 117–118,
zadání 247–250 na 153–154 a odpovědi na 479–480. Autorův Pre-Fascicle 5C:
52–54, 89–90, 183–184. Strany byly vizuálně prohlédnuty; při sdílení
stránky s dalšími úlohami se kontrola vztahuje jen na tento rozsah.

**Výsledek:** jedna drobná terminologická chyba [F150](F150_OPTIONS_NOT_ITEMS_248.md),
žádná nová zjištěná chyba ve výsledcích C$. **E108** odděluje dvě již
publikované opravy 249. Knižní PDF je obsahuje, draft z roku 2019 nikoli.
Celý 4B tím hotov není. Následují ZDD a úlohy 251 dál.

## K nejlevnějších řešení a proměnlivá mez

Maximová halda obsahuje K nejmenších cen dosud navštívených řešení,
zpočátku doplněných nekonečnem. Nahrazení jejího maxima novou menší cenou
zachovává invariant; maximum T nikdy neroste. Po naplnění K skutečnými
cenami lze jiné řešení s cenou alespoň T přeskočit. Rovnost cen nevadí:
cílem je libovolná nejlepší K-prvková množina řešení, včetně násobností
cen. Tvrzení neslibuje výpis všech řešení se stejnou optimální cenou.

Obě vytištěné posloupnosti mezí pro K=3 a K=4 byly přepočteny beze změny
pořadí vstupních cen. Pro K=3 je přijata posloupnost 3,1,4,1,2; následná
další řešení už nezlepší tři uložené ceny 1,1,2.

## Proč lze omezit cover/purify cenou

Je důležité zesílit původní invariant algoritmu C. Aktivní seznam může
obsahovat také drahé možnosti, které kolidují s již vybranými položkami:
nebyly skryty, protože pro žádné přijatelné pokračování nemohou být použity.
Všechny možnosti s cenou **menší než aktuální T−C_l** však mají správné
seznamy a barevné příznaky.

Při zakrytí hlavní položky v C4 nechť nejlevnější možnost stojí c_min a
mez v okamžiku zakrytí je T_old. Neskrytá možnost má cenu alespoň
TH0=T_old−C_l−c_min. Každá větev zvolená v tomto seznamu přitom zaplatí
alespoň c_min. Taková neskrytá možnost by tedy dosáhla alespoň T_old;
po případném snížení T je stále nepřípustná. Tentýž argument pro další
commit používá přesnou cenu zvolené možnosti a TH=T_old−C_l−c.

To platí i pro zvláštní případ **c≥TH0**: vybraná možnost sama nemusí být
v C4 skryta. Její vlastní další výskyty ale nemohou projít přísnou novou
cenovou podmínkou v podstromu. Při purify se její kladný barevný uzel
nezmění na −1: pokud nebyl skryt, jeho cena je mimo procházený prefix.
Proto zůstane správným vlastníkem pozdějšího unpurify.

Undo musí použít uložené TH0/TH, nikoli mez odvozenou z novějšího T.
V opačném případě by část dříve odstraněných uzlů zůstala skrytá. Ve
stejném cenovém prefixu se cover/uncover a purify/unpurify vracejí dolů,
hide/unhide doprava. Již prokázané cvičení 2 zaručuje konečnou obnovu
seznamu při **stejném** pořadí odstraňování a vkládání; neplatí to pro
libovolné promíchání a mezistavy nemusí tvořit konzistentní seznam.
Vnější série commit se nadále ruší v opačném pořadí.

Nový [spacerový interpret](csharp_spacer.py) proto kontroluje paměť až po
celé párové operaci. Převzal pouze již přijatou vstupní reprezentaci z
`colored_dlx.py`; starý soubor se nezměnil. Nejde o strojově formalizovaný
důkaz ani o kontrolu přetečení konkrétního 64bitového C programu.

## 247: nezáporné ceny, daně a citace

Odečtení minima cen možností jedné primární položky zachová nezápornost
a sníží každé úplné řešení o tutéž částku. Jakmile vznikne nulová možnost,
pozdější odečet ji nezmění: každá další její položka má minimum nula.
Po jediném průchodu má tedy každá primární položka nulovou možnost.
Sekundární položky se nezdaňují. Součet daní se přičítá k hlášeným cenám.

Celkové seřazení možností a opětovné vložení jejich uzlů zaručuje (118)
v každém sloupci. Veřejný DLX5 používá ekvivalentní stabilní třídění
jednotlivých sloupců; tato implementační odlišnost nemění požadovaný
invariant. Prázdná primární položka znamená nesplnitelnost.

Citovaný [Gondran–Laurière 1974](https://www.numdam.org/item/RO_1974__8_1_27_0/)
byl získán v původním znění. Na stranách 28–29 je redukce cen po řádcích
a duální lineární program; bibliografie i obsah citace souhlasí. PDF 27–29
byly zobrazeny. Duální proměnné odpovídají rovnostem primárního pokrytí,
proto nejsou obecně omezeny na nezáporné hodnoty. Barevné a sekundární
podmínky mohou zpřísnit původní úlohu; spodní mez z primární relaxace
zůstává bezpečná. Citace není vydávána za důkaz rychlosti konkrétního C$.

## 248: omezená prohlídka seznamu

Počítadlo s udává počet již zjištěných levných možností. Jestli další
uzel existuje a je levný, ale s=t, je skutečný počet větší než současný
nejlepší odhad; položku lze přeskočit. Při dosažení limitu L se použije
LEN(j), což je horní mez skutečného počtu levných možností. Tento odhad
může být nepřesný, ale ovlivňuje pouze volbu větvení. Když má položka
prázdný seznam nebo již první cena dosahuje meze, neexistuje přijatelné
pokračování. Remízy se správně rozhodují pro větší minimální cenu.

Nových 3 600 kombinací dvou krátkých seznamů, tří mezí a L=1,2,10
souhlasí s nezávislou deklarativní volbou podle uvedeného odhadu.
Historickou zkušenost autora, že úplné měření délky bylo horší, nepřebírám
jako nezávisle změřený výkon ani jako tvrzení o univerzálně nejlepším L.
Záměna slova „options“ za „items“ v zadání je samostatná nízká F150.

## 249–250: nejostřejší mez a nezávislé akumulátory

Po t přečtených nezáporných cenách je nejostřejší možná mez součet každé
k-té hodnoty v seznamu doplněném dk−t nulami a seřazeném vzestupně.
Je dosažitelná právě tímto doplněním; žádná vyšší mez neplyne jen ze
známého prefixu. Inkrementální posuny v odpovědi 249 opravují přesně ty
sčítané pozice, které nová cena zasáhne. Starých 157 497 prefixových
kontrol se přijímá bez opakování.

Vytištěný příklad d=6,k=2,θ=16 má po šesti hodnotách mez **14**, po
sedmé hodnotě 2 mez **16**. Zastavení je opravdu nejdříve možné na sedmé
hodnotě. V použití uvnitř C$ je θ>0; pro obecné API s θ≤0 je špatnost
známa už z počátečního nulového odhadu, před čtením vstupu.

Pro skupiny z položek seřaďme minima jako c_1≤…≤c_dz. Každá budoucí
možnost musí stát alespoň maximum minim svých položek. Po seřazení d
skupinových maxim musí být j-té maximum alespoň c_jz: prvních j skupin
pokrývá jz položek. Součet c_z+c_2z+…+c_dz je tedy bezpečná mez.
Pro z=1 jde přímo o (119). Každá Z-kategorie dává další samostatnou mez,
protože každá možnost obsahuje právě jednu její primární položku.
**Tyto meze se nesčítají**; stačí překročení kterékoli z nich. Předem se
ověřuje platnost hintů. Sudoku, Langfordovy možnosti a prvočíselné čtverce
mají v textu uvedené počty primárních položek správně.

E108: oprava 26. 1. 2020 mění rovnosti na přiřazení; oprava 8. 12. 2021
doplňuje y←0 při každé nové ceně. Obě jsou v lokální knize již zapracovány.

## Nová kontrola a přijaté starší výsledky

[Nová kontrola](results/csharp247_250/spacer-checked.json) trvala **1,705 s**
s **nice 15**. U všech **512** malých vstupů souhlasí K nejnižších cen
s úplným výčtem nejvýše 1 024 podmnožin; každý skutečně přijatý model je
nezávisle validován včetně původní ceny. Zahrnuty jsou nuly, duplicity,
barevné kolize, shodné barvy, prázdné sloupce a K větší než počet řešení.
Paměť se přesně obnovila po **1 739** cover/uncover a **386** purify/unpurify;
**727** návratů nastalo po snížení meze. Kontrola zastaví po 20 sekundách.

Jeden cílený vstup má primární a,b, sekundární s a možnosti
`a s:red |0`, `a s:blue |1`, `b s:red |5`, `b s:blue |2`, `b s:green |0`.
Při K=1 po červeném řešení ceny 5 následuje modré ceny 3; v posledním
sloupci platí cena=TH0=2. Tím se ověřuje výše vysvětlený hraniční případ,
který původní náhodný vzorek nepokryl. Vývojový záznam rozlišuje tuto
neúspěšnou kontrolu pokrytí od matematické chyby knihy.

Přijaty beze změny a bez opakování: původních **1 000** testů nativního
DLX5, **157 497** prefixových kontrol, důkazy obnovy seznamů z úloh 1–2
a barevný invariant C. Nový průchod není dalším velkým cenzem nebo
optimalizací. Všechny dříve spuštěné dlouhé běhy zůstávají s nízkou prioritou.

Doklady: [zdrojová kontrola](results/csharp247_250/source-checked.json),
[prohlédnuté stránky](sources/csharp247_250/source-observations.json),
[šest vrstev errat](results/csharp247_250/errata-search.json),
[metadata článku](sources/csharp247_250/retrieval.json).
