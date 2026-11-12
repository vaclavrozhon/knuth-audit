# §4.1: základní soustavy a přesná aritmetika

Původní strany 194–213 a odpovědi 604–611 byly celé přečteny vizuálně.
Tento blok uzavírá úlohy 1–15, 25, 27 a 34; další úlohy, twindragon
na 206 a historické atribuce zůstávají samostatnými bloky. Inventář
34 úloh souhlasí; ve čtyřech vrstvách errat nejsou přidané úlohy.
Relevantní historické opravy byly navíc vizuálně přečteny na stranách
13, 35 a 36 původního all2-prepre. Výňatky včetně uloženého současného TeXu jsou v
`sources/positional-errata-excerpts.txt`. Známé opravy nepočítáme jako
nové nálezy. V tomto bloku nebyla potvrzena nová chyba.

Číslice zapisujeme od nejvyšší mocniny k nejnižší. Symbol T v datech
znamená cifru −1, kterou kniha tiskne jako jedničku s čárkou nahoře.
Pro konečný řetězec d_n...d_0 v základu b je hodnota součtem d_j b^j;
Hornerovo vyhodnocení postupně násobí dosavadní hodnotu b a přičítá
příští cifru. Zlomková část přidává záporné mocniny. Nekonečné řady
níže jsou reálně či komplexně konvergentní, kromě výslovně formálního
modelu doplňků v oddílu 2.

## 1. Číselné údaje a převody: úlohy 1–3, 9, 13–15

U periodického zlomku s periodou d_1...d_r platí

```
(0.d_1...d_r d_1...d_r ...)_b
  = (d_1...d_r)_b / (b^r−1),       |b|>1.
```

To je přímo součet geometrické řady, platný i pro záporný b. Ověřuje
převody −22/7 v binární, negabinární a vyvážené trojkové soustavě:
−(11.(001))_2, (1101.(001011))_(−2), (T0.(0TT011))_3. Závorky zde
vyznačují opakující se blok. Konečné převody −49 dávají −110001,
11010011 a T11TT. Základ 1/10 pouze obrací směr desetinných mocnin:
9.4 je 49 a nekonečná část vlevo je obvyklá desetinná část čtená
opačně. Tento případ nepoužívá formální nekonvergentní součty.

Převod všech celých čísel do základu −b je dokázán v oddílu 3;
pro úlohu 1 byl zvlášť zahrnut celý interval −10..10. Osmkové zápisy
v úloze 9 se po seskupení bitů mění na A, BAD, AD0BE, FACADE, FADED.
V řešení se nula čte jako písmeno O; jde o slovní hříčku, nikoli jinou
hexadecimální cifru.

Všechny uvedené prefixy π v odpovědi 2 byly porovnány s racionálním
intervalem pro π. Použita je Machinova identita

```
π = 16 arctan(1/5) − 4 arctan(1/239).
```

Identita plyne ze vzorce pro tangens součtu a určení úhlu v příslušném
intervalu. Každý arctangens je sevřen dvěma sousedními částečnými
součty alternující řady. Použito 70 a 24 členů, pouze s přesnými
zlomky. Celý interval leží uvnitř množiny hodnot přípustného pokračování
každého vytištěného prefixu, včetně vyváženého trojkového zápisu.
Nejde o kontrolu zaokrouhlenou binární plovoucí aritmetikou.

Další přesné kontroly zahrnují příklad 192½ na 195, babylonskou
reciproční tabulku se správnou mocninou 60, násobení 153.5·16.25,
negadesítkové zápisy ±1234567890 a příklady 208.3 ve dvou trojkových
soustavách. Pro deset šedesátkových cifer kořene na 197 má polynom
f(x)=x^3+2x^2+10x−20 opačná znaménka na krajích poslední ciferné
buňky. Jeho derivace je všude kladná, takže kořen je jednoznačný a
vytištěné cifry správné. Al-Kášího údaj 2π na 198 má absolutní chybu
menší než 10^(−16). Tím se ověřuje aritmetika údajů, nikoli historické
prvenství nebo skutečnost, že je příslušná osoba vypočítala.

Úloha 13 má uvedenou nejednoznačnost:
(1.(90))_(−10)=(0.(09))_(−10)=1/11. Není třeba hledat konečný
protipříklad, neboť zadání výslovně připouští nekonečné rozvoje.

Pro komplexní základ 2i, kde i^2=−1, se sudé a liché pozice oddělí:
každá druhá mocnina má základ −4. Proto každé komplexní číslo lze
zapsat: reálnou část převedeme do základu −4 a imaginární koeficient
vydělený 2 také; cifry proložíme. Může být potřeba ciferná pozice −1,
i když je číslo gaussovské celé (tj. oba koeficienty jsou celá čísla).
Například (1010113.2)_(2i)=−49+i, jak vyžaduje úloha 3.

Při násobení se pro každou pozici k rozloží její koeficient jako
4q+r, 0<=r<4. Ponecháme r a do pozice k+2 přičteme −q, protože
(2i)^2=−4. Tím se hodnota zachovává. Ukončení je důsledkem ukončení
celého převodu do záporného základu v obou paritách pozic; jde o
konečný počet přenosů po skončení původního nenulového součinu.
Kontrolováno všech 4096 součinů trojciferných slov nezávislým násobením
párů celých čísel (reálná, imaginární část), oba tištěné čtverce a
každý jejich dílčí řádek. Výsledky jsou −19−180i na 205 a 9−40i v
úloze 14.

Pro úlohu 15 je množina zlomků v základu −b interval

```
I_b = [−b/(b+1), 1/(b+1)].
```

Krajní body dostaneme střídáním maximální a nulové cifry. Žádná
mezera uvnitř není: intervaly (d+I_b)/(−b), d=0,...,b−1, na sebe
navazují a jejich sjednocení je I_b. Rekurzivní volba cifry tedy
poskytne každou hodnotu intervalu, se zbytkem jdoucím k nule.
Pro negadesítkovou soustavu je to [−10/11,1/11]. U 2i jsou sudé
pozice nezávislé na lichých, takže množina zlomků je obdélník

```
−4/5 <= Re(z) <= 1/5,       −8/5 <= Im(z) <= 2/5.
```

Obě souřadnicové množiny jsou celé intervaly; neověřujeme tedy jen
krajní body obrázku A-6.

## 2. Doplňky a poloha řádové čárky: úlohy 4–7

Pro p cifer desítkové soustavy položme M=10^p. Desítkový doplněk
celého x je jeho zbytek modulo M; obvyklé znaménkové čtení vybírá
rozsah −M/2 <= x < M/2. Devítkový doplněk záporného x je M−1+x,
tedy o 1 menší než desítkový. Nula má v devítkovém doplňku dva
zápisy 0 a M−1. Přenos z poslední pozice se přičte na začátek,
protože M je kongruentní s 1 modulo M−1. Příklady (3),(4) souhlasí.

Posun doplňkového zápisu doprava s doplněním nejvyšší cifry má hodnotu
floor(x/10), včetně záporného x. Stačí napsat x=10q+r, 0<=r<10;
r je právě odstraněná cifra a zbývající kód reprezentuje q.
Známé erratum 2018 upřesňuje formulaci o dělení velikosti čísla;
oprava 1999 také odstraňuje matoucí označení „largest negative“.
Asymetrie rozsahu je skutečná: nejzápornější hodnota nemá kladný
protějšek. V p bitech jsou krajní hodnoty podepsané velikosti a
jedničkového doplňku ±(2^(p−1)−1), zatímco dvojkový doplněk má
rozsah −2^(p−1)..2^(p−1)−1. Pro p=1 první dvě soustavy reprezentují
pouze nulu (ve dvou kódech), takže vzorec zůstává platný.

Úloha 4 se týká měřítka, nikoli jiné instrukční sady. Nechť B je
počet hodnot bytu a A_0,B_0 neznaménkové celočíselné obsahy operandů;
jejich interpretované hodnoty jsou A_0/B^2 a B_0/B^3. MUL vytvoří
součin A_0 B_0 v deseti bytech, tedy po dělení B^5 leží čárka mezi
registry A a X. SRAX 5 přesune první operand do X. Následné DIV dá
A_0=q B_0+r, proto

```
A_0/B^2 = (q B)(B_0/B^3) + r/B^2.
```

Podíl má čárku o jeden byt za koncem registru A, zbytek mezi byty
3 a 4 registru X. Záporná znaménka pouze určují znaménko podílu a
zbytku podle MIX; škálování je stejné. Nutnou implicitní podmínkou
instrukce DIV je nenulový dělitel a nepřetečení podílu; nejde o
přislíbení výsledku při dělení nulou.

Úloha 7 nemůže používat oboustranně nekonečný zápis jako obyčejnou
konvergentní reálnou řadu. Přesný model záporného reálného x je:
vybereme N s 10^N+x>0, zapíšeme 10^N+x a vlevo doplníme devítky.
Hodnotu čteme jako hodnotu části od pozice N−1 doprava minus 10^N.
Tato hodnota se při zvětšení N nemění. U nezáporných čísel vlevo
přidáváme nuly. Devítkový doplněk konečného desetinného zápisu má
nekonečný devítkový ocas; rovná se proto hodnotě desítkového doplňku
s následující cifrou zvýšenou o 1. Pro neukončující desetinné rozvoje
se oba zápisy shodují. Knižní N−10N=9 je formální vysvětlení této
konvence, nikoli důkaz konvergence 9+90+900+... v reálných číslech.
S 2-adickou konvergencí z úlohy 31 se tato konstrukce neztotožňuje.

## 3. Záporný základ a vyvážená trojková soustava: úlohy 11–12

Pro základ −b, b>=2, je nejnižší cifra celého n nuceně d=n mod b,
0<=d<b. Zbývající prefix má hodnotu q=(n−d)/(−b). Je-li |n|>1,
platí |q|<|n|; malé případy se ukončí přes 1→0 nebo −1→1→0.
Algoritmus tedy skončí pro každé celé n, a indukce podle nucené
nejnižší cifry dává jednoznačnost konečného zápisu bez úvodních nul.
Pro reálná čísla použijeme interval I_b z oddílu 1 a vhodné vynásobení
mocninou −b; nula leží uvnitř I_b. To dokazuje hlavní tvrzení na 204.

V odpovědi 11 je přenos k v množině {−1,0,1}. Součet nebo rozdíl
vstupních bitů a přenosu je z v intervalu −2..3. Předepsané tři větve
naleznou c v {0,1} a nový přenos k' tak, aby z=c−2k'. Po vynásobení
(−2)^m je to invariant hodnoty zpracovaných pozic. Nad posledním
vstupním bitem zbývá přenos nejvýše 1 v absolutní hodnotě. Kladný
se spotřebuje hned, záporný se změní na kladný a spotřebuje v dalším
kroku. Dvě přidané nulové pozice tedy postačují. Ve skutečné sazbě
je v první větvi k←−1; OCR ztrácí znaménko.

Pro převod podle odpovědi 12 oddělíme cifry na sudých a lichých
pozicích: v základu −2 mají sudé mocniny stejné a liché opačné
znaménko než v základu 2. Rozdíl těchto dvou řetězců, provedený již
ověřeným sčítáním, má požadovanou hodnotu. Známá oprava 1999 dává
na výstupu v části (a) pozice n+2,...,0, které jsou potřeba například
u −3. Zpětný převod je prostý rozdíl kladných binárních celých čísel.

Vyvážený trojkový zápis používá cifry −1,0,1. Nejnižší cifra je
opět nucena modulo 3; zbytek (n−d)/3 má menší velikost. Zlomková
část zaplňuje [−1/2,1/2], neboť tři intervaly (d+I)/3 pokrývají I.
To poskytuje rigorózní verzi převodu s „přičtením nekonečných jedniček“
na 207, bez nelegitimního sčítání divergentních řad. Na krajích
intervalu jsou dvě reprezentace, stejně jako u běžných desetinných
rozvojů. Truncace zlomku je vždy jednou z nejbližších celých hodnot;
při vzdálenosti 1/2 jde o dovolenou volbu mezi dvěma stejně blízkými.
Znaménko konečného či nekonečného čísla určuje první nenulová cifra,
protože absolutní velikost následujícího ocasu je nejvýše polovina
její váhy. Lexikografické porovnání má obvyklou výjimku rovnosti
obou krajních rozvojů; při kanonické volbě funguje jako v desítkové
soustavě.

Pro součet tří tritů s v −3..3 je přenos floor((s+1)/3) a výsledná
cifra s minus trojnásobek přenosu. Všech 27 vytištěných sloupců bylo
přepsáno a ověřeno. Násobení 17·17 na 208 používá po známé opravě
2000 dílčí hodnoty −17, −17·9, 17·27; součet je 289. Nadbytečná nula
v původním prostředním řádku není nový nález.

## 4. Seskupování a smíšený základ: úlohy 8 a 10

Nechť w_0=1 a w_(j+1)=b_j w_j pro všechna celá j; žádné b_j není
nula. To definuje váhu každé pozice i pro záporné j. Smíšený zápis
má hodnotu sum_j a_j w_j, kdykoli součet konverguje. Máme-li základ
stále b a seskupíme k sousedních cifer, získáme číslici
A_j=sum_(r=0..k−1) a_(kj+r)b^r a váhu b^(kj). Roznásobení dokazuje
rovnici (5), včetně zlomkové části; pro nekonečné absolutně konvergentní
rozvoje smíme seskupovat právě díky konvergenci.

Obecně zvolme přísně rostoucí, oboustranně nekonečné celé indexy k_j
s k_0=0. Blok j zahrnuje pozice k_j,...,k_(j+1)−1. Položme

```
B_j = product_(r=k_j..k_(j+1)−1) b_r,
A_j = sum_(r=k_j..k_(j+1)−1) a_r (w_r/w_(k_j)).
```

Nová váha W_j=w_(k_j) splňuje W_0=1 a W_(j+1)=B_j W_j, takže
sum A_j W_j=sum a_r w_r. Je to přesně odpověď 10 po známé opravě
2006: oboustrannost a k_0=0 jsou podstatné, aby nechyběly pozice a
zůstalo stejné absolutní měřítko. Samotná přísně rostoucí posloupnost
celých čísel má na obou koncích neomezený rozsah.

Pro celé nezáporné číslo a celočíselné b_j>=2 je nejnižší cifra
n mod b_0, zbytek je floor(n/b_0); opakováním se podíl zmenšuje a
získáme jediný konečný zápis. Faktoriálová soustava má b_j=j+2 a
w_j=(j+1)!, tedy koeficient c_k v 0..k u váhy k!. Rovnice (10),
příklady času a britské měny souhlasí. Čtyři sta smíšených seskupení
s kladnými i zápornými základy byla porovnána přesnými zlomky;
navíc 10001 faktoriálových zápisů bylo nezávisle vyhodnoceno.

## 5. Zakázaná dlouhá řada maximálních cifer: úloha 25

Nechť u,v jsou kladná celá čísla, b>=2 a 0<v<b^m. Pokud by standardní
rozvoj u/v obsahoval m cifer b−1 od pozice −n−1, měl by tvar

```
u/v = c/b^n + (b^m−θ)/b^(n+m),   n,c>=0 celé, 0<θ<=1.
```

Předchozí prefix dává c, následující ocas dává 1−θ. Nerovnost θ>0
používá právě zákaz nekonečného ocasu samých b−1. Po vynásobení je

```
θ v = b^m (cv+v−b^n u).
```

Levá strana je proto kladný celočíselný násobek b^m, avšak současně
nejvýše v<b^m: spor. Argument je obecný, nevyžaduje výčet rozvojů.
Známá stylistická změna 2007 v poslední větě odpovědi nemění důkaz.
Pro jiné cifry závěr neplatí; číslo a/(b−1) má nekonečný ocas a.

## 6. Střídavé mocniny dvou: úloha 27

Reversing representation je zde konečný součet 2^e0−2^e1+2^e2−...
s přísně rostoucími nezápornými exponenty. Je-li n sudé, nejnižší
exponent je kladný a vydělíme vše dvěma. Je-li n liché, první člen
musí být 1 a zbývá −2 násobek reprezentace (1−n)/2. Pro |n|>1 má
nový argument menší absolutní hodnotu; n=1 se ukončí, n=−1 přejde
na 1. Nula má prázdný zápis. Nenulový konečný střídavý součet nemůže
být nulou, protože jeho nejvyšší mocnina je větší než součet všech
nižších mocnin. Každý krok je tedy nucený a dokazuje existenci i
jednoznačnost, včetně malých případů, které stručná odpověď odděluje.

Doplňující tvrzení o dvou zápisech kladného n s klesajícími exponenty
plyne stejně: podle znaménka posledního členu je takový zápis buď
obrácením jediné rostoucí reprezentace n, nebo záporným obrácením
jediné rostoucí reprezentace −n. Obě možnosti začínají kladným
nejvyšším členem a mají opačnou paritu počtu přechodů znaménka.

## 7. Nejmenší počet nenulových cifer: úloha 34

Pro celé n nechť H(n) je nejmenší počet nenulových cifer v konečném
binárním zápisu s ciframi −1,0,1. Minimum existuje, protože běžný
binární zápis dává alespoň jednu možnost. Kanonický zápis, často
nazývaný nonadjacent form, nemá dvě sousední nenulové cifry. Jeho
nejnižší cifra je určena takto:

```
n sudé: d=0;
n=1 modulo4: d=1;
n=−1 modulo4: d=−1;
n <- (n−d)/2.
```

Po nenulové cifře je další podíl sudý, proto následuje nula. Algoritmus
skončí zmenšováním |n|, přičemž ±1 přejdou rovnou na 0. Modularita
ukazuje i jednoznačnost zápisu bez sousedních nenulových cifer:
parita určí nulovou cifru, zbytek modulo 4 určí znaménko nenulové.
To je tvrzení o kanonickém zápisu, nikoli o jednoznačnosti všech
zápisů s minimální vahou; například 3=2+1=4−1 má dva minimální zápisy.

Důkaz minimality lze provést nezávisle na přepisovacích pravidlech
vytištěných v odpovědi. Parita nejnižší cifry dává přesné vztahy

```
H(2n)=H(n),
H(2n+1)=1+min(H(n),H(n+1)).
```

Navíc |H(n+1)−H(n)|<=1: k libovolnému zápisu přidáme nebo odebereme
1. Je-li nejnižší cifra téhož znaménka, přeneseme 2 do další pozice;
pokud je opačná, vyruší se. Přenos přes několik stejných cifer
odstraní nenulové cifry a přidá nejvýše jednu. Počet tedy naroste
nejvýše o 1, a obrácený postup dává druhou nerovnost.

Pro n=4k+1 mají dvě volby nejnižší cifry zbývající váhy H(2k)=H(k)
a H(2k+1)=1+min(H(k),H(k+1))>=H(k). Kanonická volba +1 je proto
optimální. Pro n=4k−1 je analogicky optimální −1. Indukce dokazuje
minimalitu celého kanonického zápisu pro kladná i záporná n.

Tištěná redukční pravidla jsou hodnotově správná: sousední opačné
cifry se nahradí jednou cifrou a běh r>=2 stejných jedniček se
přepíše pomocí 2^r−1 na dvě krajní cifry. Negativní pravidla jsou
jejich negací. Počet nenulových cifer nenarůstá. Výše uvedený důkaz
navíc dává ukončující algoritmus a nezávislou záruku optimality.
Změna formulace 2009 a nový odkaz v erratech jsou započteny.

Je ověřeno i doplňující pravidlo pro počet nenulových cifer v posledním
odstavci odpovědi. Pro kladné n počítá určité jedničky v obyčejném
binárním zápisu: bezprostředně vlevo mají buď 0, nebo řetězec
00(10)^k1 pro nějaké k>=0. Vedoucí nuly se implicitně doplní.
Následující konečný argument dokazuje pravidlo pro všechny délky.
Při čtení prefixu s hodnotou n sledujme rozdíl
δ=H(n+1)−H(n) z množiny {−1,0,1}. Před prvním bitem je δ=1,H(0)=0.
Z obou rekurencí výše dostaneme tabulku; druhá složka je přírůstek H:

| δ | připojení 0: (nové δ,přírůstek) | připojení 1 |
|---|---|---|
| 1 | (1,0) | (0,1) |
| 0 | (1,0) | (−1,1) |
| −1 | (0,0) | (−1,0) |

Stejný počet vypočítává automat pro tištěný vzor. Rozdělme stav δ=0
na A (suffix 00(10)^k1) a C (poslední bit 0, ale ne suffix 00(10)^k).
E znamená suffix 00(10)^k a B znamená poslední bit 1 bez vzoru A.
Počáteční stav je E. Přechody na 0/1 jsou E→E/A, A→E/B, B→C/B,
C→E/B. Jedničku započítáme právě ve stavech E,A,C. Sloučením A,C
vznikne přesně tabulka pro δ, takže vzor počítá H(n).

Další nezávislá kontrola používá rozdíl binárních čísel 3n a n:

```
n = sum_i ((3n)_i − n_i) 2^(i−1).
```

Nejnižší rozdíl je nula. V součtu 3n=n+2n se dva sousední rozdíly
nemohou stát nenulovými: liší-li se výstupní bit od bitu n v pozici i,
jsou předchozí bit n a vstupní přenos opačné; výstupní přenos se pak
rovná bitu n v pozici i, což vynutí nulový další rozdíl. Vzniká tedy
kanonický zápis. Jeho váha je počet jedniček v (3n) XOR n, kde XOR
znamená bitový součet modulo 2. Tato identita i automat souhlasily
pro všechna 0<=n<65536. Úplný výčet 59049 desetimístných podepsaných
slov zvlášť ověřil, že žádné nemá menší váhu než kanonická hodnota;
obecný závěr plyne z důkazu, nikoli z tohoto konečného výčtu.

## Rozsah výpočtu

`verify_positional_basic.py` má šest checkpointovaných bloků, všechny
prošly. Vedle 36 tištěných číselných kontrol byly ověřeny 11140 posuny,
10538 modulárních součtů, 98 škálování MIX, 15375 převodů do záporného
základu, 43688 úplných krátkých součtů a rozdílů, 4096 převodů přes
paritu pozic, 4097 vyvážených celých čísel, 27 sloupců tabulky,
4096 komplexních součinů, 400 smíšených seskupení, 10001 faktoriálových
zápisů, 59049 podepsaných slov, 65536 stavů pravidla vah a 4097
střídavých reprezentací. Výsledky jsou v `results/positional-basic.json`.

Tyto kontroly nepotvrzují historická prvenství ani všechny pozdější
bibliografické poznámky sekce. Fyzický pozdější tisk není ověřen.
