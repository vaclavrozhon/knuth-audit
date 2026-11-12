# V0054–V0055: formát a plovoucí porovnání, doplnění 6. listopadu 2026

Tento blok má vlastní důkazy níže; nedokazuje celý modul MMIX-ARITH ani
úplnou shodu s IEEE. Fascikl p. 12–13 / file 20–21 odkazuje na MMIXware
pro podrobnosti. P. 13 znovu zobrazeno z původního PDF
(`images/file-021-p013.png`). Architektonické definice jsou ve zmrazeném
primárním `sources/mmix-doc-20131017.w:1120–1616`; konkrétní kód porovnání
je v obou `mmix-arith-{20131017,20250620}.w`, §37 a §50–53, §82.
Metadata všech verzí a veřejných oprav jsou v `sources/fp-primary-metadata.json`.

## 1. Převzatý formát a přesný kontrakt rozbalení

Přebírá se důkaz V0054 o rozkladu E,F a návaznosti normálů a subnormálů,
nikoli jeho tehdy výslovně otevřená shoda celého IEEE. Pro libovolné
64bitové slovo je sign bit s, E ∈ [0,2047] a F ∈ [0,2^52). Klasifikace
zero, num, inf, nan je disjunktní a úplná. U NaN určuje bit F≥2^51
quiet, jinak signaling. Tento bit je konvence MMIX, ne reálná hodnota NaN.

`funpack` pro normál vrací `f=4(2^52+F), e=E−1`; proto

```text
|x| = f · 2^(e−1076),       2^54 ≤ f < 2^55,       f mod 4 = 0.
```

Pro subnormál začne s `f=4F` a posouvá vlevo, dokud bit 2^54 není jedna;
současně s každým posunem sníží e o jednu. Invariant `f·2^e=4F` zachovává
hodnotu a první jednička se k cíli přiblíží o jedno místo. Je zapotřebí
1 až 52 posunů, protože F≠0 a F<2^52. Nevzniká přetečení: poslední f je
v [2^54,2^55). U nuly je f=0 a sentinel e=−1000. U E=2047 je test
`f.h==0x400000 && f.l==0` přesně F=0, takže oddělí inf od všech NaN.
Vstupní octa se nemění; pomocné `exceptions` se nastaví na nulu.

Pomocné `shift_left/right` provádějí unsigned posuny dvojice 32bitových
polovin: po každém odečtení 32 je hodnota posunuta o 32 bitů; zbytek je
0..31. Větev `if(s)` zamezí nativnímu posunu o 32. Disjunktní přenášená
bitová pole se sečtou bez přenosu. Pro všechny zde užité posuny 0..54 jde
tedy o násobení modulo 2^64, respektive floor dělení mocninou dvou.
`oplus/ominus` přenášejí unsigned carry/borrow mezi polovinami, a proto
realizují součet/rozdíl modulo 2^64. V porovnávacím důkazu níže všechny
kladné mezivýsledky zůstávají pod 2^56, takže modulární redukce nic nemění.

## 2. FCMP, FEQL a FUN — všechny vstupy

Za nepřítomnosti NaN jsou nezáporné hodnoty ve stejném pořadí jako jejich
63bitový magnitude vzor: uvnitř E rostou s F; poslední subnormál je pod
prvním normálem; mezi sousedními normálními exponenty je největší hodnota
nižšího exponentu pod první hodnotou vyššího; +∞ je nad všemi konečnými.
Záporné hodnoty mají toto pořadí obrácené. Opačná znaménka dávají záporné
číslo menší, s jedinou výjimkou dvojice nul.

Tím je pokryto všech 16 dvojic typů v `fcomp`: sedm s alespoň jedním NaN
vrací 2; zero/zero vrací 0; zbývajících osm používá právě uvedené pořadí
znaménka a dvojice unsigned polovin. Pro dvě záporná čísla závěrečná
negace porovnání obrací pořadí. Pro různá znaménka obrací podle prvního
znaménka a vrací správně −1 nebo +1. Pro identické nenulové vzory vrací 0.

Dispatcher `mmix-sim-20131017.w:2049–2060` pak dává:

| Instrukce | Uspořádané vstupy | Aspoň jeden qNaN nebo sNaN | I výjimka |
|---|---|---|---|
| FCMP | −1,0,+1 podle pořadí | 0 | právě při NaN |
| FEQL | 1 právě při rovnosti | 0 | nikdy |
| FUN | 0 | 1 | nikdy |

Nuly opačných znamének se rovnají. NaN se nerovná ani sobě.
Toto je důkaz konkrétního architektonického chování a jeho dispatchera.
Dokumentace výslovně upozorňuje, že nesignalizující FEQL pro sNaN může
být odchylka od IEEE; žádný obecný předpoklad „IEEE tedy vše vyřeší“ zde
použit není. Výsledek je jediný datový výstup; běžná pravidla pro cíl
lokálního/marginal registru platí následně a tento blok je nemění.

## 3. Epsilon relace — definice pro konečné nezáporné epsilon

Fixujme **konečné** ε≥0. Zadané hodnoty y,z mohou být konečné nebo nekonečné,
ale nesmějí být NaN. Nuly obou znamének zde představují stejné reálné 0.
Pro konečné u definujme poloměr R(u): u=0 dává 0; subnormál dává
ε·2^−1021; normál s uloženým E dává ε·2^(E−1022). To jsou přesně
neighborhoods v primární specifikaci, včetně její záměrné zvláštní nuly.

Pro konečné y,z přímo z členství v uzavřených intervalech dostáváme

```text
y ~ z       ⇔ |y−z| ≤ max(R(y),R(z)),
y ≈ z       ⇔ |y−z| ≤ min(R(y),R(z)),
y ≺ z       ⇔ z−y > max(R(y),R(z)),
y ≻ z       ⇔ y−z > max(R(y),R(z)).
```

Proto přesně jedna z ≺,~,≻ platí, včetně rovnosti na hranici. Relace ≈
implikuje ~. Nejde o tranzitivitu; tu knižní vzorce netvrdí. Tento
argument navazuje na `vol2/notes/accuracy-basic.md`, ale **nepřebírá jeho
zacházení s nulou ani nedovolenými overflow/underflow**; právě uvedená
R(0)=0 a subnormální škála jsou MMIX rozšíření a jsou odvozena zvlášť.

Z N(0)={0} plyne 0≈z právě pro z=0. Naproti tomu 0~z pro nenulový normál
právě když `1+F/2^52 ≤ 2ε`; pro subnormál právě když `F/2^52 ≤ 2ε`.
Při ε=1/2 tedy podobnost s nulou mají všechny subnormály a právě normály
s F=0. Při ε=0 jde u všech konečných čísel o obyčejnou rovnost.

Nekonečna se kontrolují přímo z jejich tří definovaných okolí:

- stejná nekonečna jsou ~ i ≈ pro každé ε≥0;
- opačná nekonečna jsou ~ i ≈ právě pro ε≥2;
- konečné číslo a nekonečno jsou ~ právě pro ε≥1 a nikdy nejsou ≈,
  protože konečné uzavřené okolí při konečném ε nekonečno neobsahuje.

Pokud ~ neplatí, obě okolí mají správnou orientaci a platí právě přísné
uspořádání ≺ či ≻. Tím jsou pokryty hranice ε=0,1,2 i všechny nečíselné
vstupy tohoto smluveného oboru. `FCMPE` dává znaménko přísného vztahu,
`FEQLE` indikátor ≈; `FUNE` je na tomto oboru 0 a jeho výjimkové vstupy
jsou rozebrány zvlášť v oddílu 5.

## 4. Přesný celočíselný invariant fepscomp

Nejprve se dokazuje matematická redukce, **ne pravdivost celého původního
kódu**. Ten v jedné větvi níže selhává (MMIX-S0001).

Po `unsubnormalize` má každý nenulový konečný operand dvojici (A,q),
kde normál má A=4(2^52+F), q=E−1, a subnormál A=4F,q=0. Platí
`|u|=A·2^(q−1076)` a `R(u)=ε·2^(q−1021)`; A je násobek 4 a A<2^55.
Výměna operandů uspořádá nejprve q, potom A. Není-li menší operand nula,
je q_y≥q_z≥0. Nulu lze v testu ~ položit do stejné škály q_y s A_z=0;
test ≈ s právě jednou nulou už skončil false.

Položme d=q_y−q_z. Pro ~ nechť ε'=ε; pro ≈ nechť ε'=ε/2^d.
V obou případech se přesná podmínka redukuje na

```text
D = A_y + (-1)^[stejná znaménka] A_z/2^d  ≤  T=2^55 ε'.
```

Pro stejné znaménko je D≥0 díky uspořádání; pro opačné je součet.
Obě strany jsou nenegativní. D<2^56. Efektivní exponent ee epsilon
se v případě ≈ sníží o d; nejde o plovoucí zaokrouhlení epsilon.

Je-li ε'≥2 (ee≥1023), T≥2^56>D a návrat true je správný. Je-li D=0,
návrat true je správný i při ε=0. Je-li D≠0 a ε'<2^−54 (ee<968),
T<2 a je nutné false: pro d=0 je nenulové D násobkem 4; pro d=1
je nejméně 2; pro d≥2 je větší než 2^53 (větší operand je normální,
pokud exponenty různě velké), takže rovněž nejméně 2.

Zbývá porovnat D a T, přičemž ε' je v [2^−54,2). Pokud A_z/2^d
není celé, je d>2, A_y≥2^54 a A_z/2^d<2^52. Pak
D>3·2^52, tedy D/2^55>3/8. Pro ee<1020 je ε'<1/4 a okamžité false
je bezpečné. Pro ee≥1020 je T celé: mantisa epsilon je násobkem 4,
takže posun doprava nejvýše o 1 je přesný, a ostatní posuny jsou vlevo
nejvýše o 1. Proto se smí D nahradit **ceil(D)**.

Je-li A_z/2^d celé, je i D celé, a pro libovolné T platí
`D≤T ⇔ D≤floor(T)`. Tím je zdůvodněn pravý posun mantisy epsilon v
posledním porovnání. Tato dvě zaokrouhlení se nekombinují v neplatném
oboru: jakmile se D zaokrouhluje, T je celé. Poslední porovnání dvou
unsigned polovin je tudíž správné, pokud předchozí větev opravdu vyrobila
ceil(D). Jeho mezivýsledky jsou menší než 2^56, takže je oktabyte unese.

Při d≤54 kód správně detekuje ztracený zbytek pomocí
`oo=(A_z>>d)<<d`. Pro stejná znaménka je
`ceil(A_y−A_z/2^d)=A_y−floor(A_z/2^d)`; pro opačná je to
`A_y+floor(A_z/2^d)+1`, je-li zbytek nenulový. Přesně to dělá
`incr(o,ys==zs?0:1)`.

Při d>54 se však původní kód nastaví `o=0,oo=A_z`, takže test zbytku
nikdy neselže a chybějící +1 pro opačná znaménka nepřidá. Příklad a rodina
jsou v `notes/MMIX-S0001-fepscomp.md`. Auditní change file mění pouze
`oo=A_z` na `oo=0`. Pro d>54 je totiž 0<A_z<2^55≤2^d, takže zbytek
je vždy nenulový a právě tato větev má dostat ceil(D). Tím se výše
uvedený důkaz uzavře pro všechny **konečné** ε≥0 a konečné y,z.
Kód okolních větví pro ±∞ v y,z odpovídá tabulce z oddílu 3.

Ukončení: kromě rozbalení tří subnormálů jsou všechny větve konečné
posloupnosti operací; každé rozbalení provede nejvýše 52 posunů.
Žádné pozdější posuny nepřesahují 54 bitů. Neodvozuje se tím cena
architektonické instrukce z tabulky 1: ta je jiný, deklarovaný model,
nikoli počet C operací softwarového modulu.

## 5. Výjimkové hranice a zůstávající povinnosti

Zdroj odmítá rE s **nastaveným znaménkovým bitem**, tedy také −0.0,
a každý NaN v rE,y,z. `FCMPE/FEQLE` pro takový vstup vrátí 0 a nastaví I;
`FUNE` vrátí 1 bez I, i pro signaling NaN. To plyne z úplného switch a
dispatchera, nikoli z dosazení do reálných intervalů. U +∞ v rE používá
kód sentinel ee=10000: všechny dvě nenulové konečné hodnoty pak jsou
~ i ≈, zatímco právě jedna nula stále vylučuje ≈; konečné/nekonečné
stále nemají ≈. Doslovná intervalová definice při ε=+∞ a popis „negative“
pro −0 mají nejednoznačný rozsah. Tyto okraje jsou zaznamenány jako
**neuzavřená specifikační závislost**, ne jako nový potvrzený knižní nález.

V0054 a V0055 nadále zůstávají partial, ale následné poznámky již
uzavřely všechny aritmetické rekurence, konverze a disabled-trip eventy,
včetně samostatných programových rozporů a jejich auditních oprav.
`fp-contract-boundaries.md` nyní obsahuje úplnou tabulku skutečného
chování rE=+∞, přesné dva nevyjasněné významy rE a samostatné konkrétní
povinnosti širší IEEE deklarace. `fp-short-arithmetic-recovery.md`
dokazuje single emulaci hodnot i příznaků. Pozdější úlohy o úplném
seznamu změn rA (např. 1.3.1′–54) se tím automaticky neuzavírají.
Známé opravy `sfpack` a `fplus` z autorovy verze 2025 jsou zaznamenány
jako převzatá errata, nikoli naše nálezy. První čtení ani barva stránky
se tímto dílčím blokem nepovyšují na úplnou kontrolu.
