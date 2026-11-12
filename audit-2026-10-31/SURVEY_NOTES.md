# Pole a pevné body survey propagation: SAT 357–361

Kontrola 31. 10. 2026. F044 opravuje krajní hodnotu v357; F045 doplňuje
celou vynechanou rodinu pevných bodů v360. Samostatné slovní
nepřesnosti odpovědi 361 zůstávají jako kandidát C008.

## F044: y=0 místo y=1

Odpověď357 na str. 619 (PS 255) uvádí při (p,q)=(1,0) podmínky
0<x≤1,y=1. Správně je **y=0**. Při x=π_(¬v),y=π_v jsou podle155

`p=x(1−y)/D, q=y(1−x)/D, r=xy/D, D=x+y−xy`.

Pokud r=0 a x>0, pak y=0. Vytištěné x=1/2,y=1 dává naopak
(p,q,r)=(0,1/2,1/2), nikoli (1,0,0). Pro r>0 platí obě inverzní
formule x=r/(1−p), y=r/(1−q) správně.

Úloha358 je rovněž správná: r≥p právě když x(2y−1)≥0 a r≥q právě
když y(2x−1)≥0. Po vyloučení (x,y)=(0,0), kde pole není definované,
je jejich souběh ekvivalentní x,y≥1/2. Přesný výčet 288 bodů na
mřížce po 1/16 kontroluje inverze i všechny krajní případy.

##359: výpočet s nulovými faktory

Reprezentace součinu jako součin nenulových členů a počet nul je
správná. Při vynechání nenulového členu dělíme součin tímto členem,
ale výsledek je nula, pokud počet nul není nula. Při vynechání
nulového členu dostaneme nenulový součin právě tehdy, když šlo
o jedinou nulu. Stejná konstrukce funguje pro (156) i (157).
Test enumeruje všechny posloupnosti z {0,1/3,1} délky nejvýše 7
a porovnává každé vynechání s přímým novým součinem.

## F045: při d=1 existuje výjimečná spojitá rodina

Odpověď360 na str. 619 (PS 255) říká, že pokud d=0 nebo 1,
pak x=y=z=d. To neplatí pro **a=b=c=0,d=1**: každý

`x=y=z=t, 0≤t≤1`

je pevným bodem. Uvedený obecný zlomek má právě v tomto případě
tvar0/0. Například t=1/2 přímo vyvrací tvrzení x=y=z=1.

Ověření nepoužívá pouze tři zjednodušené rovnice: byly přepsány
všechny původní klauzule (7), všech 21 zpráv η_(C→l), všech 8 hodnot
π_l a všechny rovnice(154),(156),(157). Pro t=0,1/16,…,1 se
celý stav po jednom přesném přepočtu zachová. Nedochází k
nedefinovanému poli, protože π₁=π_(¬2)=π_(¬4)=π₃=1.

Konkrétní stav pro libovolné t má jedinou nenulovou posilující
zprávu η_(¬3)=1. Ze zpráv od klauzulí jsou nenulové jen

```
η_((-1,-2,3)→-1)=t,
η_((2,3,-4)→2)=t,
η_((1,3,4)→4)=t.
```

Koeficienty flexibility jsou π_(¬1)=π₂=π₄=1−t,
π_(¬3)=0 a ostatní1. Každá z uvedených zpráv se z rovnic
přepočítá na následující t v cyklu, ostatní zůstanou0.

## Úplné řešení360

Symetrie klauzulí současně zamění proměnné2↔4 a literály3↔¬3.
Protože η₃η_(¬3)=0, lze touto symetrií předpokládat η₃=0,
jak činí kniha. Podmínky π₁=π_(¬2)=π_(¬4)=1 vynutí nulové
posílení těchto literálů i všechny příchozí zprávy do nich.
Z(156)pak plyne, že γ_(-1→C)=γ_(2→C)=γ_(4→C)=0.
Tím všechny zprávy od klauzulí kromě tří výše musejí být nula.

Při značení knihy a=η_(¬1),b=η₂,c=η₄,d=η_(¬3) zbývá

```
x=d(b+(1−b)y),
y=d(c+(1−c)z),
z=d(a+(1−a)x).
```

Dosazením získáme přesně zlomek pro x vytištěný v knize a jeho
cyklické varianty pro y,z. Jmenovatel
`1−d³(1−a)(1−b)(1−c)` je kladný kromě jediného bodu
(a,b,c,d)=(0,0,0,1). Tam rovnice říkají jen x=y=z.
To dokazuje úplnost doplnění F045, nikoli pouze existenci několika
numerických pevných bodů.

Bylo ověřeno624 běžných parametrů z{0,1/4,1/2,3/4,1}⁴
a 17 bodů spojité rodiny. Tabulka (159) odpovídá a=b=c=1/2,d=1/3,
x=y=z=1/5; všechny její π, η i γ souhlasí přesně.

##361: přesná klasifikace binárních zpráv

Pro π_l,π_(¬l)∈{0,1}, ne obě0, nabývá γ_(l→C)hodnoty1
právě když l je nepravdivý. Proto musí mít každá klauzule alespoň
jeden pravdivý literál nebo dva neurčené. Jinak by zpětná zpráva
vynucovala neslučitelnou hodnotu π. To je přesně stabilita podle363.

Pro libovolné stabilní ohodnocení jsou klauzulové zprávy jednoznačné:
jednička směřuje do jediného pravdivého literálu klauzule, jsou-li
všechny ostatní literály nepravdivé; jinak jsou všechny nula.
Posílení má tyto přesné možnosti:

- Pokud π_l=1, musí být η_l=0.
- Pokud π_l=0 a existuje příchozí klauzulová zpráva 1, lze η_l volit0 nebo 1.
- Pokud π_l=0 a žádná příchozí zpráva 1 není, musí být η_l=1.

Pro současné pevné body posilování sκ=1 se vezme η_l=1−π_l,
což souhlasí s posledním řádkem odpovědi 361.

Úplný výčet všech 256 formulí na dvou proměnných, včetně jednotkových
klauzulí a prázdné formule, prochází všechny binární klauzulové
a posilující zprávy. Výsledné pevné body se přesně porovnávají
s výše uvedenou klasifikací. Stabilní ohodnocení s k omezenými
proměnnými má 2^k možností pro posílení; žádné další pevné body
s definovanými poli nevznikají. Výsledky jsou v`results/surveys.json`.

## C008: slovní neúplnost odpovědi 361

Věta, že η_l lze volit0 nebo 1s jedinou uvedenou výjimkou, opomíjí
nutnou podmínku η_l=0 při π_l=1. Také označení všech těchto stabilních
ohodnocení jako „covering“ nesouhlasí s užší definicí 364, která navíc
požaduje, aby každá přiřazená proměnná byla omezená klauzulí.

Příkladem je jediná klauzule (x∨y) a ohodnocení x=y=1: je stabilní,
žádná proměnná není omezená, přesto s oběma pravdivými posíleními 1
a všemi klauzulovými zprávami 0 tvoří pevný bod. Není „covering“
ve smyslu 364. Nesprávná volba posílení nepravdivého literálu by
navíc vytvořila nedefinované pole.

Tuto položku zatím vedeme jako kandidáta na upřesnění, protože
omezení posílení je přímo v definici 154 a autor je mohl považovat
za implicitní. Nezapočítáváme ji mezi F044–F045.

## Doklady

F044, F045 i znění C008 byly vizuálně ověřeny v PDF na str. 619
a v autorově PS na str.255. Definice a příklad jsou na str.275–276
(PS 91–92). Ve stažených kompletních erratech 4B a Fascicle 6 nebyly
odpovídající opravy nalezeny. Fyzický exemplář dosud ověřen není.
Reprodukce: `check_surveys.py`, výstup `results/surveys.json`.

## Následující kontrola

Úlohy 362–365 ještě nejsou uzavřené. U 362 prověřit počáteční
protikladné jednotkové klauzule: seznam L se na počáteční rozpor
výslovně nekontroluje a popsaný krok neřeší vznik prázdné klauzule.
Nejprve zkontrolovat předpoklady Algorithm S / S8; zatím žádný nález.
