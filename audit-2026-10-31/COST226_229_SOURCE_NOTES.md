# Úplný zdrojový průchod 226–229 a Langfordovy ceny

3. listopadu 2026. Obě znění zadání na 152/draft88 a odpovědi na
475–476/draft179–180 byla přímo přečtena, včetně pokračování 228
na následující straně. Hlavní text 111–112/draft47–48 byl zkontrolován
po začátek příkladu s dámami. Nová potvrzená chyba nepřibyla;
F077 zůstává potvrzená. E102 je známá textová změna z 3. července 2023:
před (108) přidat „Langford“. Obě naše verze mají původní znění.

Obecné důkazy používají M=2n+1. V Langfordově párování jsou dvě
kopie každé hodnoty 1,…,n, proto Σa=n(n+1) a
Σa²=n(n+1)(2n+1)/3. Obrácení pozice k na M−k dává

```
Σ₁ + obrácená Σ₁ = M n(n+1),
S + obrácené S   = M² n(n+1)/3,
obrácená Σ₂ = M² Σa − 2M Σ₁ + Σ₂.
```

Poslední rovnice spolu s obrácenou Σ₁=MΣa−Σ₁ dokazuje
invarianci Σ₂−MΣ₁ pro libovolnou posloupnost, jak tvrdí odpověď 226.
Nejde jen o test několika malých n.

V možnosti (16) leží obě kopie i na pozicích j a k=j+i+1. Jejich
příspěvky jsou i(j+k), i(j²+k²) a i²(j+k), přesně podle hlavního
textu a 227. Každé úplné řešení má n možností. Cena C−i(j²+k²)
tedy minimalizuje nC−Σ₂ a správně maximalizuje Σ₂, pokud C zaručuje
nezápornost. Tato podmínka je v textu uvedena.

Pro první výskyty j_i v odpovědi 228 sečteme obě pozice každé hodnoty:

```
Σ[2j_i+i+1] = Σ(k=1..2n) k = n(2n+1),
Σj_i = (3n−1)n/4.
```

Součet čtverců obou pozic pak je
Σ(k=1..2n)k² = 2Σj_i² + Σ₁ + n(2n+1).
Odtud Σj_i²=(4n²−1)n/3−Σ₁/2, přesně jako v pokračování odpovědi.
Tato identita sama neurčuje Σ₂ a nedokazuje údajnou obecnou korelaci.

Všech **204 vytištěných hodnot v každé verzi** bylo porovnáno se
zdrojovým textem po vizuálním přečtení. Všech osm posloupností má
správné dvojice a rozestupy. Oba protipříklady v odpovědi 228 skutečně
ukazují různé jevy:

| Příklady | Σ₁ první / druhé | Σ₂ první / druhé |
|---|---:|---:|
| dvě posloupnosti řádu 8 | 592 / 592 | 6208 / 6368 |
| dvě posloupnosti řádu 11 | 1634 / 1638 | 25100 / 25100 |

(106) je přesným obrácením (107). Mají ceny
(5268,120360,60004) a (3708,68880,38732). (108) má
(3708,68880,37552). Minimum ze 229 má (5240,119192,60324).
Dosavadní úplné výsledky pro n=7 a minima n=16 se pouze přebírají
z [dřívějších poznámek](LANGFORD_COST_NOTES.md) a přijatých dat.
Žádný starý výčet, MILP, SAT prefix ani validace 163997 modelů
se znovu nespouštěly.

Původní přijatý soubor obsahuje 6525 různých platných modelů s cenou
3720; jejich cenové hlavičky byly nově sečteny bez opakování validace.
To více než stačí pro 484 takových řešení, která doplní 12016 optim
do K=12500. Není to tvrzení, že modelů s cenou 3720 existuje celkem
právě 6525. Jejich úplná množina nebyla nově určována.

Postup 229 pomocí ostrého minimaxu je obecně správný. Po fixaci
dosavadního prefixu má každé zbývající řešení možnost pokrývající
nejmenší neurčený slot s_j. Tato možnost musí mít první výskyt právě
v j; jinak by pokrývala už fixovaný menší slot. Uspořádání podle
klesajícího j dává všem pozdějším slotům menší pořadové číslo.
Minimax proto rozhoduje právě o hodnotě v j. Při shodě j jsou hodnoty
seřazeny správně pro požadované lexikografické minimum či maximum.
Přesun zvolené možnosti na začátek ji přestane zahrnovat do dalšího
maxima pořadových čísel; smazání všech ostatních možností obsahujících
s_j fixaci vynutí. Indukce dává lexikografické optimum.

Samostatná nová malá kontrola fixovala prvních osm možností knižního
minima a úplně prohledala pouze zbylou úlohu: **1040 uzlů, 12 řešení**,
nejmenší z nich je přesně vytištěné minimum. Celý checker zdrojů,
aritmetiky a tohoto suffixu trval 1,423 s s nice 15.

F077 zůstává: (108) není lexikografické maximum. Nový
[samostatný verifier](verify_f077.py) kontroluje pouze vytištěnou
posloupnost a krátký větší svědek, žádné hledání. Rozhoduje čtvrtá
pozice: 11 > 9. Maximálnost našeho svědka je navíc dříve přijata
z DFS a SAT; samostatný krátký důkaz ji nepotřebuje.

Důležité zpřesnění rozsahu: ze shody množin minimalizujících Σ₁ a Σ₂
neplyne automaticky, že jejich obrácení globálně maximalizují také Σ₂.
Obrácení maximalizuje Σ₁, ale obrácená Σ₂ závisí na kombinaci
Σ₂−2MΣ₁. Přijaté staré výpočty dokazují minima a dávají 12016
obrácených svědků ceny 120360, nikoli nový úplný důkaz maximálnosti
této druhé ceny. Jeden nový jednovláknový pokus o nalezení ceny
alespoň 120361 skončil po **20,038 s timeoutem**, bez svědka.
To není UNSAT ani důkaz horní meze. Pokus se neopakuje ani neprodlužuje.

Podle uživatelova pokynu jsou výslovně vynechány:

- úplný počet 653443600 párování řádu 16, citovaný v hlavním textu;
- samostatná globální horní mez 120360 pro Σ₂ a přesná úplnost její
  maximalizující množiny, včetně tvrzení, že obsahuje právě obrácená minima;
- historické náklady 60G, 2,2T, 70G, 28G, 10G na straně 112;
  u 229 jednotlivé kroky pod 110K, výjimky 4,5M/500K, součet 6M
  včetně vstupu 465K a maximum pod 2M. Aritmetika 2,2T/60G>36 sedí,
  ale tyto konkrétní konfigurace nejsou znovu měřené.

Všechny výjimky mají `verified:false`; nevymazávají jiné mezery auditu.
Úlohy 226–229 mají dokončený průchod s těmito přesnými výjimkami.
Hlavní 111 a odpovědní 475 jsou dokončené. Strany 112, 152 a 476
zůstávají částečné pro další příklady s dámami a úlohy od230 dále.
Žádná zpráva autorovi se nevytvářela.

[Přesné výsledky](results/cost226_229/source-checked.json),
[omezený pokus](results/cost226_229/reversed-sigma2-bounded.json),
[zdroje a šest vrstev errat](sources/cost226_229/source-observations.json).
