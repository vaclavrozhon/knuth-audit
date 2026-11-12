# §4.5.2: základní identity a Eukleidův algoritmus

## Rozsah a zdroje

První část bloku V2-X0044: matematický obsah str. 333–343, programy A/B,
úlohy 1–9, 15 a 37. Zbytek oddílu, pravděpodobnostní věta D a historické
atribuce zatím nejsou uzavřeny touto poznámkou. Oddíl má 42 původních úloh,
text a zadání na str. 333–356, odpovědi na 640–647.

Zobrazeny originály 333–343, 353–356, 640–641, 645–647, tedy nikoli jen OCR.
Tištěná strana p odpovídá straně p+12 souboru našeho prvního dotisku z roku 1997.
Obrázky jsou v `images/vol2-p*.png`. Prohledány a čteny relevantní úseky všech
čtyř vrstev `all2-prepre`, `all2-pre`, `all2`, `err2`, dne 2026-11-02.

Známé opravy v této části: na str. 334 se mění stáří algoritmu z 2250 na
2300 let (2015); na 335 je doplněno, že dělitelnost F je předpoklad (1999);
na 339 jde o formulační změnu popisu délky programu (2013); na 343 jsou
opravy přepisu jmen a datování (2002, 2021). Opravy str. 641 k úlohám 10
a 14 se vyřídí v navazujícím bloku. Pro níže doložené C0117–C0120 nebyla
v těchto vrstvách nalezena oprava. Prvenství a aktuální fyzický dotisk nejsou
ověřeny; návrhy hlášení zůstávají neodeslané.

## Značení a identity: úlohy 1–4

`gcd(u,v)` je nezáporný největší společný dělitel celých čísel u,v;
`gcd(0,0)=0`. `lcm(u,v)` je nezáporný nejmenší společný násobek, s hodnotou
0 při nulovém argumentu. Pro kladné číslo u značí `e_p(u)` exponent
prvočísla p v jeho rozkladu. Dělitelnost se pak testuje porovnáním exponentů;
gcd vybírá jejich minimum a lcm maximum.

1. Rovnice (8) a (9) přičtou k oběma exponentům exponent w; (10) používá
   `min(a,b)+max(a,b)=a+b`. Rovnice (11), (12) jsou distributivní identity
   minima a maxima na lineárně uspořádané množině. Nulové argumenty ověříme
   přímo definicí, znaménka odstraníme absolutní hodnotou. Podmínky `w>=0`
   a `u,v>=0` jsou v originálu výslovně uvedeny, včetně rovnosti.
2. Jestliže nezáporná čísla a,b_i splňují `a<=sum b_i`, pak
   `a<=sum min(a,b_i)`: buď některé b_i>=a, nebo se součet nezmění.
   Aplikace na prvočíselné exponenty dokazuje úlohu pro nenulové argumenty.
   Je-li některé v_i=0, součin gcd obsahuje |u|; pro u=0 předpoklad
   vynucuje nulový součin v_i a také nulový součin gcd. Znaménka nevadí.
3. Pro `p^e || n` existuje `(e+1)^2-e^2=2e+1` možností exponentů dvojice
   s maximem e. Součin těchto počtů je počet dělitelů n². Druhá odpověď
   dává bijekci: exponent j dělitele d z intervalu 0..2e se zobrazí na
   `(min(j,e), 2e-max(j,e))`. Pro j<=e dostaneme `(j,e)`, jinak `(e,2e-j)`.
   Tyto větve se nepřekrývají a pokrývají všechny požadované páry.
4. Pro každé p přiřadíme celou mocninu `p^max(e_p(u),e_p(v))` tomu číslu,
   v němž se vyskytuje s větším exponentem; při rovnosti zvolíme u.
   Součiny přiřazených mocnin jsou hledaná u'|u a v'|v, jsou nesoudělné
   a jejich součin je lcm(u,v).

Příklad 7000,4400 má gcd 200 a lcm 154000. Nezávislá konečná kontrola
obsahuje 9261 trojic s nulami a 1194 dvojic z bijekcí pro 1<=n<=100.

## Algoritmy E a A; program A

Množina společných dělitelů u,v se při nahrazení `(u,v)` dvojicí
`(v,u-qv)` nezmění pro žádné celé q. To dokazuje invariant E i A.
V A se druhý kladný argument striktně zmenšuje; konec `(g,0)` vrací g.
E na vstupu A,C>1 zvlášť rozlišuje nulový zbytek, jednotkový zbytek a
zbytek větší než 1. V posledním případě pokračuje s menším C.

Program A nejprve načte v do A a u do X. Jeho první dělení tedy počítá
`v mod u`, nikoli `u mod v`; symetrie gcd to dovoluje. Před každým DIV
je A nulové po SRAX 5 a dělitel je nenulový obsah X před STX. Nevzniká
přetečení. Pokud původní u=0, program vrátí v bez dělení, včetně dvojice
(0,0). Sedm instrukcí je přepsáno v `sources/gcd-basic.mix`.

Při T děleních jsou počty instrukcí 1,1,T,T,T,T+1,T+1. Cena je
`2+1+2T+2T+12T+2(T+1)+(T+1)=19T+6`. Asymptotický průměr T se
ověří v §4.5.3; zde není vydáván za již dokázaný.

## Algoritmus B, jeho program a čas

Vstupy jsou kladné. Po vyjmutí společné mocniny `2^A` je alespoň jeden
argument lichý. Dělení sudého argumentu dvěma při lichém druhém argumentu
gcd zachovává. Po B5 jsou oba argumenty liché. Nenulový rozdíl je sudý;
jeho lichá část nahradí větší argument číslem menším než jeho předchozí
hodnota. Součet argumentů tím klesá, takže algoritmus skončí rovností.
Při návratu se vyjmutá mocnina dvojky vrátí do výsledku.

Binární posuny SLB/SRB pracují s velikostí spojeného registru AX; znaménka
A a X zachovávají samostatně. Během společného půlení je A sudé, takže
do X nepřeteče žádný nízký bit A. Později na obsahu X nezáleží: vysoká
část SRB je vždy `floor(|A|/2)`. Poslední SLB má X=0 a jeho výsledek
gcd se vejde do slova, protože nepřevyšuje vstupy. To platí i pro MIX
s bajtem o 100 hodnotách, nikoli jen s bajtem o 64 hodnotách.

V časovém vzorci A počítá společná půlení, B je indikátor počátečního
sudého u po jejich odstranění, C počet odečtení v B6 včetně posledního
nulového, D počet jednotlivých půlení v B3 a E počet kladných t při B5.
Součet cen vytištěných instrukcí je přesně

```text
9A + 2B + 6C + 3D + E + 13.
```

Výpočet byl porovnán s instrukčním interpretem ve 20210 bězích programů
A/B, na bajtových základech 64 a 100. Kontrolují se výsledky, absence
přetečení, jednotlivé počty průchodů i celkový čas. Rozšíření interpretu
o SLB/SRB má dalších 1600 přímých kontrol podle definice spojeného
registru. Ostatní instrukce nebyly změněny.

## Nejhorší případ a úloha 37

Pišme `S(u,v)=C` pro počet odečtení a `lg=log_2`. Silnější tvrzení
`S(u,v)<=lg(u+v)` dokážeme indukcí podle součtu kladných vstupů.
Odstranění sudého faktoru z argumentu C nemění a součet nezvětšuje.
Pro liché u=v máme S=1. Pro liché u>v platí

```text
S(u,v) = 1 + S((u-v)/2,v)
       <= 1 + lg((u-v)/2+v) = lg(u+v).
```

Proto `C<=1+floor(lg max(u,v))`, jak požaduje úloha. Je-li
`1<=u,v<2^N`, po společných půleních mají argumenty nejvýše N-A bitů.
Tedy C<=N-A. Každé jednotlivé půlení snižuje součet bitových délek
o jeden, ostatní kroky jej nezvětšují, a závěrečný součet je alespoň 2.
Proto `D<=2(N-A)-2`. Každé kladné t při B5 předchází alespoň jedno
půlení argumentu u, takže `E<=N-A-1`. S B<=1 dostáváme

```text
time <= 9A+2+6(N-A)+3(2(N-A)-2)+(N-A-1)+13
     = 13N+8-4A <= 13N+8.
```

Pro N>=2 dosahuje rovnosti dvojice `(2^N-2,2^N-1)`: A=0, B=1,
C=N, D=2N-2, E=N-1. Po prvním půlení u následuje rozdíl `-2^(N-1)`;
jeho N-1 půlení sníží v na 1. Potom se u opakovaně mění z `2^j-1`
na `2^(j-1)-1`. To současně dokazuje uvedené počty.

**C0117:** při N=1 je jediný vstup (1,1), B=0 a čas 19, takže 13N+8
je stále horní mez, ale není dosažené maximum. Stejná drobná výjimka je
v poslední větě odpovědi 37: dvojice `(2^(n-1)+1,2^(n-1)-1)` potřebuje
n odečtení a má nejmenší možný součet 2^n pro n>=2. Při n=1 dává
nepovolený vstup (2,0); správná nejmenší dvojice je (1,1).
Vstupy pro n>=2 mají po prvním rozdílu argumenty 1 a `2^(n-1)-1`,
což dokazuje tvrzení o n odečteních. Dolní mez součtu plyne z důkazu S.

## Trojková varianta: úloha 5

Nejprve se vyjme společná mocnina 3 a z každého argumentu se odstraní
zbývající faktory 3. Když jsou argumenty kladné a nedělitelné třemi,
právě jedno z u+v a u-v je dělitelné třemi. **Je však nutné použít
absolutní hodnotu rozdílu.** Pro různé argumenty zvolený výraz není 0;
jeho kladná část po odstranění faktorů 3 je menší než max(u,v):
pro součet nejvýše `(u+v)/3<=2 max(u,v)/3`, pro rozdíl ještě méně.
Gcd se zachovává a kladný součet klesá. Rovnost argumentů je koncový stav.

**C0119:** doslovné u-v v odpovědi 5 při (1,7) dává po dělení třemi -2.
Nahrazení max(1,7) vede na (1,-2). Další rozdíl 3 se zkrátí na 1 a
nahrazení max(1,-2) ponechá stav (1,-2), tedy nekonečný cyklus. Již první
řádek tabulky na 640 používá kladné `24140-13634`, ačkoli tištěná instrukce
určuje opačné znaménko. Oprava `|u-v|` sjednotí popis, tabulku i důkaz.
Nejde o vadu myšlenky algoritmu ani samotného vytištěného číselného příkladu.

## Úlohy 6–8: přesné konečné a limitní průměry

Náhodné vstupy v tomto odstavci znamenají nezávislou rovnoměrnou volbu
z `1..2^N-1`; limitní hodnoty jsou limity při N do nekonečna.
Označme `M=2^N-1`. Pro k>=1 máme
`Pr(A>=k)=(2^(N-k)-1)^2/M^2`, pro k>N je pravděpodobnost nula.
Sečtení této geometrické sumy dává přesně

```text
E[A] = 1/3 - 4/(3M) + N/M^2.
```

Koeficient 4/3 je v originálu správně; OCR není spolehlivé. Limitní
pravděpodobnost `Pr(A=k)=3/4^(k+1)` má střední hodnotu 1/3 a rozptyl
4/9, tedy směrodatnou odchylku 2/3. Oba momenty konvergují také z konečných
vstupů, protože pravděpodobnosti ocasu jsou stejnoměrně geometricky omezené.

Pro B=1 po společném dělení je u sudé a v liché. Pro každý možný počet
společných půlení k je těchto dvojic
`(2^(N-k-1)-1)*2^(N-k-1)`. Sečtením pro k=0..N-1 dostaneme
`E[B]=1/3-1/(3M)`, v souladu s odpovědí 7.

Označme F počet odečtení, při nichž u>v. Kromě počátečního B nastává
kladný reset právě po těchto odečteních, tedy E=F+B. Záměna vstupů
zachovává C a převádí F na C-1-F, protože poslední odečtení má u=v.
Symetrické rozdělení vstupů proto dává přesnou identitu
`E[E]=(E[C]-1)/2+E[B]`. Zde E[.] znamená střední hodnotu, zatímco samotné
E uvnitř závorek je výše definovaný počet resetů. Asymptotické zkrácení
na `E[C]/2` má pouze konstantní chybu; kniha je označuje jako přibližné.

Všechny tyto konečné identity a dosažená maxima časů byly ověřeny přesným
sčítáním pro N=1..8, celkem 86368 dvojic. Výpočty nenahrazují uvedené důkazy.

## Rozšíření C a X, úlohy 9 a 15

Asociativita gcd plyne ze stejné množiny společných dělitelů. Opakované
nahrazování ostatních vstupů zbytkem po dělení nejmenším kladným vstupem
tuto množinu zachovává; nejmenší kladný vstup klesá, nebo zůstane jediný
nenulový vstup. Redukce C zpracovává argumenty zprava a může skončit při
d=1, protože další gcd s 1 je 1.

**C0120, pouze kandidát:** C je formulován pro celá čísla a n>=1, ale
C1 nastaví d=u_n bez absolutní hodnoty. Pro n=1,u_1=-1 vrátí -1.
Pro n>=2 s úplnou rutinou gcd znaménko opraví první volání. Předchozí
odstavec však pracoval s nezápornými vstupy; pokud má tento předpoklad
platit i pro C, nejde o chybu. Proto tento okraj není potvrzeným nálezem.
Jednoznačná formulace by nastavila `d=|u_n|` nebo doplnila obor vstupů.

V X jsou první dvě souřadnice celočíselné koeficienty původních vstupů;
třetí je jejich lineární kombinace. Odečítání celého násobku a výměna
vektorů zachovávají tyto vztahy, zatímco třetí souřadnice provádějí A.
Také determinant matice prvních dvou souřadnic je stále +1 nebo -1.
Každý její řádek proto má nesoudělné souřadnice. Na konci, pro g=gcd(u,v)>0,
vztah `u*v1+v*v2=0` a nesoudělnost dávají
`(v1,v2)=±(v/g,-u/g)`. To platí i s jedním nulovým vstupem. Při (u,v)=(0,0)
X ihned skončí s `(v1,v2)=(0,1)`; výraz s dělením g se zde nepoužije.

Pro kladné u,v jsou i mezilehlé koeficienty omezeny koncovými:
`|u1|,|v1|<=v/g` a `|u2|,|v2|<=u/g`. Po počátečních jednotkových
vektorech mají po sobě jdoucí nenulové koeficienty opačná znaménka,
takže odečtení násobku zvětšuje absolutní hodnotu jako
`|nový|=|předchozí|+q|současný|`. Všechny další kvocienty jsou kladné;
možný první nulový kvocient pouze vymění počáteční vektory. To dokazuje
mez i pro mezilehlé stavy. Při nulovém vstupu se přímo vracejí počáteční
jednotkové vektory, případně jejich výměna.

**C0118:** dovětek odpovědi 15 chybně píše `v1*u=lcm(u,v)`. Správně
`|v1*u|=lcm(u,v)`. Pro u=1,v=2 končí X s vektorem (-2,1,0), takže
levá strana bez absolutní hodnoty je -2, pravá 2. Také vlastní tabulka
na str. 343 končí záporným v1=-710. První věta odpovědi 15 obě znaménka
správně rozlišuje; chyba je jen v následném důsledku a chybějící výjimce
(0,0) pro podílový vzorec.

Úloha 9: B nejprve dosáhne `(u,v)=(1963,1359)` a další rozdíl 604
se zkrátí na 151; výsledkem po vrácení společného faktoru 2 je 302.
X dává `2*31408-23*2718=302`. Větší příklad v textu dává
`337*40902-571*24140=34`; všechny řádky tabulek A/B/X a trojkového
příkladu jsou uloženy v přesném výsledku a souhlasí s originálem.

Bradleyho úspora druhé souřadnice funguje pro v>0, kde ji zpětně dopočítáme
jako `(g-u*u1)/v`. Případ v=0 je počáteční koncová větev X a vrátí se
bez této operace; nepovažujeme její přirozené přeskočení za samostatnou chybu.

## Reprodukce

`python3 workstreams/vol2/verify_gcd_basic.py --resume`

Úspěšné části se znovu nespouštějí. `results/gcd-basic.json` a `.log`
obsahují 16884 dvojic pro matematické algoritmy (včetně 500 náhodných
vstupů až 2048 bitů), instrukční kontroly, algebraické identity, konečná
rozdělení a samostatné přesné protipříklady. Referenční gcd je nezávislé
`math.gcd`, programy MIX jsou samostatnou cestou proti aritmetickému popisu.
