# Dlaždice 121 a symetrie barev 122–123

Stav 2. listopadu 2026: **123 je úplně prověřena; 121 a 122 zůstávají
částečné.** Nový kandidát C031 není započten mezi potvrzené chyby. E061–E063
jsou již publikovaná errata. U 117 jsou nově přijaty všechny požadované
konečné počty Mycielského grafů také původním Algoritmem C s úpravou 122.

## 121: zdroj dat a přesný rozsah

Zobrazeny originály 4B str. 138 a 446, autorův draft str. 74 a 150,
svazek 1 str. 385, 586 a 587 a aktuální obrazová errata. Specifikace 92
typů byla přepsána z původní strany 385, nikoli převzata z poškozeného OCR.
Základní čtveřice mají pořadí **sever, jih, západ, východ**; program je
převádí na **sever, východ, jih, západ**. Prázdný kód B nic nepřidává.
Složky složených kódů se řadí abecedně. Příklad βYQT má tedy hrany
`3QY, 1T, 4QY, 2T`. Vzniká 92 různých typů a 46 různých barev hran.

Nezávislý řešič udržuje bitovou množinu přípustných typů každé buňky.
Odstraní typ pouze tehdy, když pro něj soused nemá žádnou kompatibilní
hranu. Větvení rozdělí doménu jedné buňky na všechny její jednotlivé
možnosti. Úplný návrat ze všech větví proto znamená úplný konečný výčet;
časový limit tuto vlastnost nemá. Každá výsledná mřížka má samostatnou
kontrolu všech společných hran i pevně předepsaných buněk.

Druhá metoda je nezměněný autorův DLX2. Obsahuje jednu primární položku
pro každou buňku a barevné sekundární položky pro hrany. Zachovává i volné
vnější hrany: bez nich by dvě různé okrajové dlaždice mohly mít totožný
textový zápis volby, což by ztratilo jejich identitu při čtení výstupu.
První malý nativní běh bez vnějších hran správně skončil s nulou; jeho
výstup zůstává archivován. Přijaté úplné množiny používají explicitní
vnější hrany a jednoznačné mapování voleb na dlaždice.

### Část (a): obecný důkaz z konečných překážek

Oba řešiče dokazují, že neexistuje 2×2 mřížka s βUS vpravo dole ani
3×4 mřížka s βUS vlevo dole. V libovolném m×n obdélníku s m,n≥4 tedy
βUS mimo horní řádek nemůže ležet mimo první sloupec: nad ní a vlevo
by existovala zakázaná 2×2 mřížka. V prvním sloupci zase nemůže ležet
ve třetím nebo nižším řádku, protože nad ní a napravo by existovala
zakázaná 3×4 mřížka. Zbývá jen n pozic horního řádku a levá pozice
druhého řádku. Jde o možné pozice, nikoli tvrzení, že všechny lze
současně obsadit βUS. V nekonečné rovině má každá buňka okolní 2×2
mřížku, takže βUS nelze použít nikde.

### Konečné počty a již známá oprava E061

| k | Strana | δRD | δRU | δLD | δLU | δSU |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 3 | 1 | 2 | 2 | 3 | 3 |
| 3 | 7 | 1 | 2 | 2 | 3 | 57 |
| 4 | 15 | 1 | 2 | 2 | 3 | 57 |
| 5 | 31 | 1 | 2 | 2 | 3 | 57 |
| 6 | 63 | 1 | 2 | 2 | 3 | 57 |

Všech 30 počtů je úplných; spolu se dvěma překážkami jde o 32 výčtů.
Pro k≤4 souhlasí celé množiny mřížek s DLX2, nejen jejich počty:
20 ukotvených případů a dvě překážky, celkem 22 nezávislých porovnání.
Pro k=5,6 je zatím pouze úplný výčet druhým řešičem a validace mřížek.

**E061:** erratum ze 7. ledna 2023 mění zadání z (2,3,3,57) na
(2,2,3,57). Následující den byla nahrazena také odpověď 121(c).
Opravené pořadí rohových bloků je pro δLD `B,A,D,C`, nikoli
`C,D,A,B` jako pro δRU. V našem PDF ani draftu tyto změny ještě nejsou.

Program dále vytváří Aₖ,Bₖ,Cₖ,Dₖ pro k≤6 z předepsaných čtyř menších
rohových bloků a prostředního δN(a,b,c,d). Každý z 20 nových křížů
má právě jednu výplň. Všech 49 jmen v obrázku A₃ na straně 587 souhlasí.
A₆ obsahuje přesně 86 typů; chybí βUS a pět výše uvedených typů δ.
Tím je ověřeno konkrétní tvrzení o A₆, ne následná obecná věta o všech
dostatečně velkých dlážděních.

Pro k=2,…,6 má δRD rohy `D,C,B,A`; δRU navíc `C,D,A,B`; δLD navíc
`B,A,D,C`; δLU a δSU mají obě dodatečná pořadí. U δSU pro k≥3 zbývá
54 mřížek. V každé je vlevo nahoře Cₖ₋₂ a ve středním sloupci se
nezávisle kombinují přesně těchto devět a šest typů:

- řádek 2ᵏ⁻²: δLJ, δLU, δPJ, δPU, δSJ, δSU, δTJ, δTU, δRU;
- řádek 3·2ᵏ⁻²: δLU, δKU, δPU, δRU, δSU, δTU.

Řádky jsou číslovány od jedničky. Všechny kombinace 9×6 byly ověřeny
pro k=3,…,6 a odpovídají opravenému erratu.

Při omezení větších mřížek na prostřední menší čtverec zůstává u δSU
přes jeden stupeň někdy ještě dvojice. Přes dva nebo více stupňů je ve
všech 50 dostupných porovnáních jediný vzor. Nelze tedy z jednoho
rozšíření nesprávně vyvodit okamžitou jednoznačnost celé roviny.

**Zbývá:** obecná indukce výčtů a rohových klasifikací pro všechna k,
z ní existence a jednoznačnost nekonečných limitů v (b,d), tvrzení o
výskytu 86 typů v každém dostatečně velkém dláždění, souvislost s dračí
posloupností a doložení historické poznámky Tyburec 2017. Konečné
stabilizované počty těmito důkazy nenahrazuji. Cizí audit svazku 1
nebyl měněn.

## 122: invariant, zpětný chod a kandidát C031

Θ je nejmenší dosud nepoužitá zvláštní barva. Při prvním použití barvy
Θ se zvýší o jedna; nižší barvy mohou být použity znovu. Vyšší barva
je nepřípustná. Již očištěné uzly mají záporné COLOR a nepřiřazují
novou barvu. Barva 0 znamená nebarvenou položku a pracuje jako dříve.

Před každým skutečným `purify` se staré Θ uloží do CTH dané sekundární
položky. Položku nelze podruhé purifikovat před jejím `unpurify`, protože
zbývající kompatibilní výskyty už jsou záporné. Jediné pole CTH tedy
stačí jako zásobníková paměť: opačné pořadí odvolávání přesně obnoví Θ.
CTH sekundární hlavičky samo zůstává mezipamětí; nemusí se nulovat.

Při odmítnutí `COLOR(p)>Θ` se musí odvolat právě již potvrzený prefix
volby. Neodvolává se odmítnutá položka ani ještě neprošlý suffix.
Skok na konec (56) ponechá p a j a provede teprve `p←p−1`, což je
správné. Funguje i při odmítnutí hned prvního uzlu a při přechodu přes
spacer. Naše nativní úprava skutečně skáče dovnitř smyčky; nezávislý
interpret odvolává explicitně uložený prefix v opačném pořadí.

Primární CTH je jiná věc: říká, kdy je dovoleno na položce větvit.
Pro obyčejné barevné permutace s pevnými jmény primárních položek je
nulové. Pokud není žádná přípustná položka, C3 přejde rovnou do C8,
bez odkrývání dosud nepokryté položky. Libovolně nastavené prahy
samozřejmě mohou řešení ztratit; jejich správnou volbu musí zdůvodnit
konkrétní kódování. Příklad s názvy dílků v 126 zůstává součástí
budoucího auditu této úlohy.

### Proč při invariantním pořadí vzniká jeden zástupce

Použijme deterministické rozhodování, které je invariantní při přejmenování
dosud nepoužitých barev, například MRV s pevně uspořádanými primárními
položkami. Dále musí být pořadí položek v odpovídajících volbách stejné
při barevné permutaci. V dané orbitě řešení pak zvolíme první použitou
barvu v, druhou novou v+1 atd. Dokud není přiřazena nová barva, jsou
všechny dosud nepoužité názvy zaměnitelné; permutace zachovává počty
aktivních voleb i následující primární položku. Indukcí po potvrzovaných
uzlech existuje právě jeden kanonický průchod každou orbitou. Při
použití všech d barev má každá orbita d! prvků, jak požaduje zadání.
Při k<d použitých barvách má d!/(d−k)! prvků; tento obecnější případ
je potřebný v úloze 123.

200 různých konečných symetrických instancí bylo porovnáno s úplným
výčtem všech podmnožin voleb a nezávislou kanonizací přes všechny
permutace barev. Nativní program a spacerový interpret mají celé
stejné množiny zástupců. Zvláštní testy zahrnují nebarvené sekundární
položky, více primárních položek v jedné volbě, opakování barev,
oběh přes spacer, částečné odvolání a odloženou primární položku.
Při návratu jsou kontrolovány všechny linkové struktury a Θ.

### C031: pořadí uzlů není pouze kosmetické

Na straně 66 jsou volby výslovně definovány jako množiny položek.
Vezměme jedinou primární položku p, sekundární x,y a dvě volby:

```
p x:1 y:2
p y:1 x:2
```

Jako množiny jsou uzavřené při prohození barev 1 a 2; obě řešení používají
obě barvy. Přesto v obou volbách algoritmus potká nejprve barvu 1 a pak
2, takže obě přijme. Očekávaný jediný zástupce se nezíská. Při zápisu

```
p y:2 x:1
p x:2 y:1
```

odmítne obě volby hned na první barvě. Původní Algoritmus C má v obou
případech dvě řešení. Nativní úprava i nezávislý interpret potvrzují
výsledky 2 a 0. Ze všech 36 dvojic uspořádání vyjde devětkrát 0,
osmnáctkrát 1 a devětkrát 2. Seřazení každé volby podle pevného pořadí
položek dá ve všech 36 případech právě jedno řešení.

**Proč zatím kandidát:** výraz „input options are totally symmetric“ může
autor zamýšlet také pro uspořádanou reprezentaci, nejen pro matematické
množiny. Pak příklad tento silnější předpoklad nesplňuje a nejde o chybu
algoritmu. Pro implementaci je podstatné výslovně zajistit invariantní
pořadí položek. Nenalezl jsem příslušnou opravu v osmi prohledaných
vrstvách errat; stejná odpověď je v PDF i autorově PS. Fyzický výtisk
neověřen. Úloha zůstává partial kvůli tomuto výkladu, ne kvůli tvrzení,
že by základní zásobníková úprava byla chybná.

Odkaz pod čarou je správný: v původním článku [Knuth 1974](https://homepages.cwi.nl/~storm/teaching/reader/Knuth74.pdf)
mají příklady 6c na str. 282 a 7a na str. 286 skutečně skok dovnitř
smyčky. Obě původní strany byly zobrazeny a článek archivován.

## 123: celý počet i úplná množina rozdělení

Z každé primární položky pₖ vybereme právě jednu z m voleb. Každé qₖ
se v řešení objeví jen u tohoto pₖ, takže jde přesně o všech mⁿ funkcí.
Mají-li k neprázdných vláken, dostaneme rozdělení n prvků do k bloků
a injektivní přiřazení k různých názvů z m barev. Tedy

`m^n = Σ S(n,k) · m!/(m−k)!`, kde 1≤k≤min(m,n).

Po odstranění názvů zbude `Σ S(n,k)`. Poslední nepoužité názvy barev
nemají význam; není nutné požadovat surjektivitu. Tím je také vysvětleno,
proč lze použít obecnější formu úpravy 122, přestože některé funkce
nepoužívají všechny barvy.

Při pevném pořadí p₁,…,pₙ se kanonické hodnoty qₖ po odečtení jedničky
rovnají restricted growth strings: a₁=0 a aⱼ₊₁≤1+max(a₁,…,aⱼ).
Původní rovnice (4) byla ověřena na zobrazené straně 416 svazku 4A
(DJVU strana 433; OCR má jiný stránkový posun).

Pro m=4,n=10 původní DLX2 vyčerpal všech **1 048 576** řešení; 104
pravidelně vypisovaných vzorků bylo ověřeno. Upravený program vypsal
všech **43 947** řešení a celá množina přesně souhlasí s nezávislým
rekurzivním generátorem řetězců. Četnosti podle počtu bloků jsou
1, 511, 9 330, 34 105. Dalších 24 dvojic m=1,…,4 a n=1,…,6 bylo
ověřeno proti všem označeným funkcím, jejich orbitám a Stirlingově
rekurenci `S(n,k)=kS(n−1,k)+S(n−1,k−1)`.

Hrubé nativní náklady jsou 48 816 983 a 2 202 904 mems; po zaokrouhlení
na celé megamemy dávají vytištěných 49 a 2. Program zvlášť vypisuje
odečitatelné aktualizace délek sekundárních položek: po jejich odečtení
43 224 583 a 1 965 736. Obě konvence jsou zaznamenané, nezaměňují se.

**E062:** 26. listopadu 2024 byl odkaz 7.2.1.5–4 změněn na
7.2.1.5–(4), tedy na rovnici, nikoli úlohu. **E063:** starší oprava
z 23. prosince 2021 odstranila v zadání výraz „m parts“ a doplnila
chybějící plus. Tyto dvě starší změny už naše 4B obsahuje.

## Nově přijaté výpočty úlohy 117

K původním nebarveným kódováním hran/klik je přidána právě položka
`z_v:j` doporučená v (d), vždy na stejném místě volby. Symetrické
kopie tedy mají invariantní pořadí; C031 se zde neuplatňuje.
150 úplných grafových instancí s nejvýše čtyřmi vrcholy a dvěma či
třemi barvami dává přesně stejné orbity jako výčet všech označených
barvení, včetně izolovaných vrcholů.

Následných **105 dokončených nativních běhů** souhlasí se všemi dříve
přijatými nezávislými počty: M₂,…,M₅ mají 1,5,520,23 713 820 barevných
rozdělení; (c−1)-barvení jsou nemožná; všech 97 jednotlivých odstranění
hrany má správný počet i dříve zapsané četnosti. Ověřeny jsou koncové
stavy, kontrolní součty a všechna vypsaná barvení. Jen velký M₅ s pěti
barvami vypisuje každý 10 000. model; ostatní případy vypisují všechny.

Historické náklady z odpovědi 117 se **nepodařilo přesně reprodukovat**:
například M₅ má 5 169 240 442 hrubých mems a 4 327 060 246 po odečtu
sekundárních délek, proti přibližným 4,1 miliardy v knize. Pořadí voleb,
implementace a účtování paměti mohou náklad měnit; samotný rozdíl není
potvrzená chyba. Čísla a všechny rozdíly jsou uložené.

Dva nové oddělené běhy Q8 mají wrappery 944644 a 944645 a limit
48 hodin na případ. Nenahrazují ani nerestartují tři dřívější běhy.
Fronta Mycielského grafů 944646 už dokončila všech 105 případů.
Zbývá přijmout Q8 po terminálu, dořešit historické benchmarky,
5-barvení M₆ a Monte Carlo odhad počtu jeho 6-barvení. Úloha 117
zůstává partial.

Hlavní doklady jsou v `results/symmetry121_123/`. Přijímací kontrola
ověřila 232 krátkých nativních běhů, 52 konečných AC-3 záznamů a 105
nových grafových terminálů. Starší dokončená hledání nebyla opakována.
Knihy, společná errata, cizí worktrees a osobní poznámky zůstávají zachované.

## Stav staršího výpočtu ONE–TEN

Při závěrečné kontrole už neexistuje původní wrapper 902988 ani procesy
912693/912694. Log končí průběžným údajem 1 770 000 006 115 mems a nemá
terminální řádek; výstupní gzip má nula bajtů. Příčina ukončení není známá.
Jde o přerušený výpočet, nikoli důkaz nemožnosti ani ověření počtu 416
ze známého errata E054. Původní soubory zůstávají zachované; pozorování,
jejich velikosti a kontrolní součty jsou v
`results/symmetry121_123/torto-one-ten-interrupted.json`.

Samostatná fronta 918953 pokračuje na odlišných případech zero-eight
a ordinals. ONE–TEN nebyl znovu spuštěn. Aktuální X112, úplný registr
a anglická karta E054 nyní odpovídají tomuto pozorování.
