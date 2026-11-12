# Základní backtracking a dámy: 7.2.2, úlohy 1–16

Průchod zahájen 1. listopadu 2026. Znění zadání a odpovědí bylo přečteno
v obrazech stran 30, 55, 398 a 399. Archivován původní autorův Pre-Fascicle 5B
z 11. září 2019, včetně data stažení a SHA-256. Jeho strana 36 odpovídá
odpovědím na straně 398 hlavního svazku.

## F081: rekurzivní přepis opomíjí mezerovité domény

Odpověď 5 na straně 398 prochází všechna celá čísla od minima do maxima
domény. Algorithm B na straně 30 ale výslovně postupuje k dalšímu prvku
domény; nevyžaduje, aby doména byla interval. I odpověď 1(i) připouští
libovolnou doménu.

Pro n=1, D₁={1,3} a vždy pravdivou P₁ jsou řešení 1 a 3. Rekurzivní
přepis navíc vydá 2. Stačí nahradit cyklus průchodem prvků D_l v rostoucím
pořadí, případně doplnit test příslušnosti do domény. Původní Algorithm B
je v tomto ohledu správný. Znění potvrzeno v PDF i autorově PS; příslušná
oprava nenalezena v celých textech err4b a err4f5.

[Protipříklad](results/backtrack_basics/recursive-domain-counterexample.json),
[PDF](images/vol4b-p398.png), [PS](images/fasc5b-p36.png),
[návrh zprávy](knuth-report-f081-draft.txt).

## E012: známá oprava rekonstrukce dámy

Poslední věta odpovědi 10 má a_l−a_(l−1) místo a_(l+1)−a_l.
Jde o oficiální opravu z **21. ledna 2026**, nikoli náš nový nález.
Pole a_l obsahuje sloupce zvolené před vstupem do řádku l, takže nový bit
je přesně rozdíl následujícího a současného pole. Samotné bitové aktualizace
v odpovědi jsou správné.

## Obecná správnost B, B* a W; úlohy 1–6

Invariant: při vstupu na úroveň l je uložen právě přípustný prefix délky l−1
a datové struktury odpovídají tomuto prefixu. Neúspěšné rozšíření nemůže mít
přípustného potomka díky podmínce (1). Úspěšné rozšíření vytvoří právě jednoho
potomka; při návratu se přesně zruší poslední aktualizace. Konečné neprázdné
domény a rostoucí průchod zajišťují úplnost, jedinečnost a lexikografické pořadí.
W pouze předem spočítá přípustné děti a prochází tentýž strom.

Domény prázdné nebo nekonečné vyžadují zvláštní ošetření: min a max v B
nejsou obecně definované. Toto obvyklé implicitní omezení zde nevydáváme
za další nález. V úloze 2 může předfiltrování dát prázdnou doménu; v tom
případě lze ihned vrátit nulový počet řešení. Samotné tvrzení o omezení P₁ platí.

Doslovné stavové implementace B a W byly porovnány na 500 náhodných
prefixových stromech, včetně mezerovitých domén, slepých větví a n=0.
Samostatný úplný výčet ověřil nejen řešení, ale celou množinu navštívených
prefixů. Aktualizace a návraty se kontrolují proti explicitnímu zásobníku.

V úloze 1 jsou všechna uvedená kódování správná:

- N-tice jsou kartézský součin; permutace mají navzájem různé prvky.
- Klesající kombinace mají k-tý prvek nejvýše N+1−k.
- U celočíselné particie doplněné nulami má k-tý prvek nejvýše floor(n/k).
  Součet dosavadních částí nesmí překročit n a zbývajících n−l částí,
  nejvýše velikosti x_l, musí ještě dovolit součet n. To je dolní mez v P_l.
  Při l=n proto vyjde přesně n. Podmínky jsou dědičné směrem ke kořeni.
- Restricted growth strings kódují bloky podle pořadí prvního výskytu.
- Rostoucí pozice levých závorek s x_k≤2k−1 jsou přesně podmínka nezáporné
  bilance v každém prefixu; výsledná délka je 2n.

Všechny generátory byly zkontrolovány do n=8 proti nezávislým konstrukcím
a počtům; kombinace pro N≤9. U úlohy 3 lze každý konečný zakořeněný strom
očíslovat Deweyho adresami. Příslušnost prefixu ke stromu zajišťuje požadovanou
dědičnost; listy mohou být i před maximální hloubkou.

Úloha 4 používá zrcadlení sloupců. Pro osm dam nemá žádné řešení fixovaný
první sloupec při tomto zrcadlení, takže omezení na první čtyři sloupce dává
46 z 92 řešení. Úloha 6 byla úplně přepočítána jako permutace sedmi různých
sloupců na sedmi vybraných řádcích; obě osmičlenné řady odpovídají knize.

## Úlohy 7–14: svědci a obecné důkazy

**7 a 8.** Sedmnáctidámový rámovaný svědek a všechny čtyři uvedené
osmidámové permutace jsou platné. Dodatečná [kontrola rámovaných dam](FRAMED_QUEENS_NOTES.md)
ověřila úplné výčty do n=22, rotační redukci a Spragueovu původní citaci
včetně obr. 52. Počet pro n=27 se ještě počítá; přesný obecný práh17
není doložen. Úloha7 je proto v úplném registru částečná, i když existenční
otázku jejího zadání svědek řeší.

**9.** Uvedené svědky pro 16 a 24 dam mají 12 a 18 dam na jedné barvě.
Na desce 4m×4m je počet dam každé barvy sudý: součet všech souřadnic
je 4m(4m+1), tedy sudý, takže počet lichých součtů souřadnic je sudý.
Pro m=5 nemůže být na bílé barvě požadovaných 15 dam. Otázka o všech sudých
m je v odpovědi výslovně položena jako otázka, ne jako dokázané tvrzení.

**10.** Aktualizace a_(l+1)=a_l+t zachytí nový sloupec. Posun b doprava
a c doleva odpovídá posunu zakázaných sloupců při přechodu do dalšího řádku.
Ořezání c maskou stačí, b vpravo bity samo zahazuje. Pole všech úrovní dovolují
návrat bez změn starších stavů. Nejnižší bit určuje nejmenší sloupec.

**11.** Zrcadlená dvojice dam se napadá podél řádku, sloupce nebo diagonály;
pro kladné n je proto řešení se zrcadlovou symetrií možné jen při n=1.
Čtvrtotáčkové orbity mají velikost čtyři kromě případného středového pole.
To vylučuje n≡2,3 modulo 4. Překlopení nakloněného čtverce zachová množiny
jeho řádků, sloupců a obou diagonálních souřadnic: vzhledem ke středu jsou
to ±a, ±b a ±(a+b), ±(a−b). Proto nemůže vzniknout nový konflikt s ostatními
damami. Každou ze floor(n/4) orbit lze nezávisle orientovat tak, aby v horní
polovině ležela nad hlavní diagonálou; to dává faktor 2^floor(n/4).
Počty i kanonická podmínka byly přepočítány pro n≤12.

**12.** Součet sloupců a řádků modulo n vylučuje sudá n. Pro lichá n dělitelná
třemi označme S=Σk². Z předpokládaných permutací obou diagonálních reziduí
plyne 2S≡4S modulo n, ale 2S≡n/3, což je spor. Pro gcd(n,6)=1 fungují
směrnice 2 i 3: jejich rozdíly od ±1 jsou jednotky modulo n. Konstrukce
zkontrolovány do n=500, toroidální výčet do n=12.

**13.** Franelova konstrukce je správná. Napišme n=2m, δ=k−j a
r=[j≤m<k]. Pak x_k−x_j≡2δ+3r modulo n. Konflikt může nastat jen při
δ+3r≡0 nebo 3δ+3r≡0. Protože 3 nedělí n, při r=0 není možný; při r=1
zbývají δ=n−3 nebo n−1. Pro n≥8 mají příslušné rozdíly sloupců −3 a 1,
nikoli ±δ; n=4 se ověří přímo. Konstrukce je permutace, protože obě poloviny
vyčerpají opačné parity sloupců. Má prázdnou hlavní diagonálu, takže lze
přidat rohovou dámu a dostat případy n≡3,5 modulo 6. Případy n≡0,4
vzniknou odstraněním rohu z toroidální konstrukce na n+1; n≡1,5 mají
toroidální konstrukci přímo. Nula a jedna jsou triviální, dvě a tři nemožné.
Franelovy konstrukce i přidaný roh byly ověřeny do velikosti 501.

**14.** Složené rozmístění je injektivní funkcí n menších rozmístění a jednoho
toroidálního. Konflikt sloupců nebo diagonál modulo n by nejprve vynutil
stejný index j; pak by vynutil konflikt v menším rozmístění. Zbytky sloupců
modulo n obnoví y, jejich podíly všechna x^(j), takže je zobrazení injektivní.
Přepočteno všech 320 konstrukcí pro m=4,n=5.

## Tabulky a meze rozsahu

Doslovná B* do n=10, bitový průchod do n=12 a nezávislé permutace do n=9
dávají stejná řešení. C++ přepočet potvrdil všechny hodnoty Q(0),…,Q(16),
úplný profil 16 dam i 1 141 190 303 uzlů. U úlohy 16 používají tři směry
šestiúhelníkové mřížky souřadnice řádku, sloupce a jejich rozdílu; jde tedy
o jednu vypuštěnou diagonální podmínku. Všech patnáct hodnot H(0),…,H(14)
souhlasí; pro n≤10 je ověřil také úplný výčet permutací.

Úloha 15 byla dokončena následnou [kontrolou asymptotiky a konstanty](QUEENS_CONSTANT_NOTES.md): knižní tvar odvozen ze Simkinovy publikované věty, dolní duální svědek a přesně přípustný racionální horní svědek vyhodnoceny intervalově. Zaokrouhlení 0.389068 je doloženo; celý Simkinův teorém je výslovně přiznaný vstup, nikoli náš nový nezávislý důkaz.
Memové údaje na str32–33 a celý obrázek68 byly následně dokončeny níže.
Historické citáty a velké počty n=27 zůstávají samostatnými kontrolami.
Žádný test zde neprokazuje formální správnost všech budoucích implementací
backtrackingu.

Reprodukce: [check_backtrack_basics.py](check_backtrack_basics.py),
[backtrack_profiles.cpp](backtrack_profiles.cpp),
[verify_backtrack_profiles.py](verify_backtrack_profiles.py).
Výsledky: [základní kontroly](results/backtrack_basics/verified.json),
[profily](results/backtrack_basics/profiles.json),
[porovnání](results/backtrack_basics/profiles-verified.json).

## Hlavní text str31–33: náklady přístupů do paměti

Všechny tři knižní hodnoty112Gμ,34Gμ a9.1Gμ souhlasí s přesným účtováním
popsaných metod. [queen_backtrack_mems.cpp](queen_backtrack_mems.cpp) projde
celý strom přípustných prefixů a matematicky sečte přístupy pomalejších
variant. [check_queen_backtrack_mems.py](check_queen_backtrack_mems.py)
porovnal tyto součty se čtyřmi doslovnými stavovými výpočty pro n1–10:
porovnávání v obou pořadích, tři booleovská pole a bitový Walker.
Všech40 dvojic souhlasí v memech i v celém profilu stromu.

| Varianta pro n16 | Přesný počet memů | Zaokrouhlené tvrzení knihy |
|---|---:|---:|
| Postupná porovnání od prvního řádku | 111920275172 | 112Gμ, asi98 na uzel |
| Tři booleovská pole B* | 33859294243 | 34Gμ, asi30 na uzel |
| B* s poli v registrech | 2282380604 | 2 na uzel |
| Walker se čtyřmi uloženými slovy | 9129522416 | 9.1Gμ, 8 na uzel |

Označme N=1141190303 počet uzlů a E=N−1 počet úspěšných hran.
Jednoduchá varianta potřebuje dva memy na každou hranu k uložení a
obnovení zvoleného sloupce. Samotná porovnávání dají109637894568 čtení.
Tento počet lze odvodit bez simulace každého pokusu: před testem j-té
předchozí dámy se načte její sloupec pro právě ty kandidátní sloupce,
které dosavadní testy ještě nevyloučily. Jejich počet je n minus počet
bitů ve sjednocení dosavadních útoků. Součet těchto počtů přes každý
přípustný prefix je přesně počet jednotlivých čtení.

U B* je na uzlu s r již umístěnými dámami n čtení pole a, n−r čtení
pole b a n−popcount(A∪B) čtení pole c. Celkem24729771749 čtení.
Každá úspěšná hrana přidává čtyři zápisy při sestupu a čtyři přístupy
při návratu. Inicializace tří polí potřebuje5n−2=78 zápisů.
Při použití zrcadlové symetrie se dva diagonální směry prohodí; kontrola
proto sčítá správné obě hodnoty, nikoli slepě dvojnásobek jedné z nich.

Bitový Walker může držet a,b,c,S v registrech. Před sestupem je uloží
čtyřmi zápisy a po návratu obnoví čtyřmi čteními; výpočet další množiny
kandidátů už je čistě registrový. To dává přesně8E memů. Rekonstrukce
řešení a statistiky se stejně jako v knize neúčtují do samotného hledání.

Pokud jednoduchá varianta porovnává předchozí dámy v opačném pořadí,
má jiný správný náklad90264262066 memů. To není protipříklad ke knižním
112Gμ: text popisuje jednu implementaci, nikoli náklad všech možných
pořadí testů. Čas našeho výpočtu50.04 sekund se s knižními memy nezaměňuje.
Data a příkazy jsou v [n16.json](results/queen_backtrack_mems/n16.json)
a [run.json](results/queen_backtrack_mems/run.json).

## Obrázek68: ověřeny všechny nakreslené uzly a hrany

Z původní [PDF str32](images/vol4b-p32.png), pořadí52 v souboru, byly
vyčteny přímo vektorové operace. Obsahují2057 bodových značek a2056 hran.
Každý konec hrany byl jednoznačně přiřazen nejbližšímu bodu. Kvůli
zaokrouhlení souřadnic v PDF je největší odchylka0.069642 bodu; druhý
nejbližší bod je vždy vzdálen alespoň0.476303 bodu. Použitá pevná mez
0.1 bodu tedy přiřazení bezpečně rozlišuje.

Vznikl jediný zakořeněný strom. Po seřazení potomků zleva doprava
souhlasí **každý** podstrom s úplným lexikografickým generováním
neútočících dam, nejen celkový počet nebo profil. Každému bodu se přiřadí
právě jeden přípustný prefix; všechny2057 prefixy jsou různé a žádný
nechybí. Profil je1,8,42,140,344,568,550,312,92. Čísla sloupců obrázek
neuvádí; v kontrolních datech je přidává dané pořadí generování.

[check_queen_tree_figure.py](check_queen_tree_figure.py) ukládá všechny
souřadnice, rodiče, potomky a přiřazené prefixy do
[figure68-verified.json](results/backtrack_basics/figure68-verified.json).
Ověřuje také obě aritmetická srovnání ze str31:
2057/8^8≈0.01% a8^8/binom(64,8)≈0.38%, včetně přesného binomického
čísla4426165368. Čtyřdámový strom(4), jeho popis a obě řešení2413/3142
byly přímo porovnány s původní stránkou a předchozím úplným výčtem.

## E021: dvě již publikované úpravy str33

V [aktuálních erratech](../errata/originals/err4b.textxt) jsou dvě drobné
úpravy Walkerova výkladu: dne27.11.2022 doplněno „(Otherwise stop.)“
na konec W4 a dne10.1.2025 zvětšena pravá závorka množiny v(5).
Naše PDF má původní znění. Nejde o nové nálezy ani o změnu správných
číselných výsledků; doplnění ukončení je zahrnuto v doslovné kontrole W.

Strany31 a32 jsou nyní celé prověřené v popsaném rozsahu. U str33
zůstává historické připsání Walkerovi a závěrečné tvrzení o výpočtech
19.století; tyto prameny se nezaměňují za právě ověřenou matematiku.
