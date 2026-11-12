# Souvislá revize: spektrální úlohy 16–24

6. listopadu 2026. Znovu vizuálně přečtena zadání na 116–117 a odpovědi
580–582. Přečten celý `verify_spectral_extensions.py`, celý
`verify_spectral_research.py`, obě staré poznámky, výsledkové souhrny
a dokončovací logy. Žádný výpočet se neopakoval. Výsledky tohoto bloku
neuzavírají zbývající text F/G ani úlohy 25–32.

## Algoritmy pro počet rovin a všechna minima

Úloha 16 je správná po dvou úpravách C0044 a s výslovným omezením na
neposunutou mříž. Pro Y=XU a neškálovanou duální bázi V platí
`x_k=Y·V_k`, tedy `|x_k|<=||Y||_1 ||V_k||_inf`. Pravá strana obsahuje
f(X), protože f(X)=||XU||_1; tištěné f(Y) není platná alternativa.
V uloženém příkladu U=((1,-1),(0,2)), X=(4,3) máme Y=(4,2),
f(Y)=||(4,2)U||_1=4 a druhý řádek V=(1/2,1/2). Tištěná mez by byla
3<=2. Tato U je skutečná báze kongruence u1+u2=0 modulo 2.

Pro neposunutou mříž je počet protínajících rovin
`g(Y)=||Y||_1-delta(Y)`, kde delta je 1 při přítomnosti obou znamének,
jinak 0. Je-li k minimální L1 norma, minimum g je k-1, existuje-li
smíšený minimalizátor, jinak k: vektor s L1>=k+1 nemůže dát méně.
Všechny striktní zlepšující vektory pro dosavadní celé s splňují
g(Y)<s, a proto ||Y||_1<=s. Pro škálované V v algoritmu je tedy
`floor(s*||V_k||_inf/m)` dostatečná souřadnicová mez. Přidání jedničky
není nutné, pokud chceme pouze hodnotu minima. Při přechodu dimenze
se původní svědek doplní nulou; zůstává platnou horní mezí.

Tištěná instrukce pro aktualizace normy odkazuje na S4/S7, ale správně
jde o S4/S5. S7 žádný takový starý příkaz nemá. To samo nedokládá
nesprávnou číselnou odpověď: i čtverec celočíselné eukleidovské normy
je horní mez L1 normy, a případný větší kvádr zůstává úplný. Opravený
program aktualizuje právě měněný řádek. Jeho nezávislý soupis přímo
v souřadnicích Y používá L1 kouli a řeší poslední složku kongruencí;
nesdílí bázový kvádr. Uložených 5036 shod pro 1259 párů a,m je přijatý
konečný doplněk obecného důkazu, nikoli nový běh.

V úloze 17 je úprava S9 správná pro t>=3. Počáteční kvádr zahrnuje
všechny vektory o délce nejvýše tehdejší meze; aktualizace s v průběhu
neodstraní žádné konečné minimum. Jeden reprezentant dvojice ±Y se
navštíví právě jednou. Při přísném zlepšení se seznam vyprázdní, při
rovnosti rozšíří. **C0047** má dvě nezávisle doložené části:

- Pro t=2 S9 nikdy neběží. Například a=2,m=5 vyžadují výstup
  ±(2,-1), ±(1,2), ale změna pouze S9 žádný dvourozměrný výstup nepřidá.
  Je třeba zvláštní výpis po S3 nebo stejný kvádr použít i pro t=2.
- Pro řádek 3 tabulky a=2^18+1,m=2^35,t=6 jsou dvě různé minimální
  dvojice s nenulovými konci: ±(1,-1,0,0,-1,1) a ±(1,0,-1,-1,0,1).
  Položíme-li b=2^18, pak a^j=1+jb modulo m. Obě kongruence plynou
  ze součtu koeficientů a ze součtu indexovaných koeficientů, oba jsou 0.
  Norma 1 je vyloučena invertibilitou a; norma 2 by potřebovala
  a^i=±a^j pro rozdíl indexů 1–5. Kladná varianta by vyžadovala
  2^17 | (i-j), záporná dává 2=0 modulo b. Norma 3 má lichý součet
  tří znamének, který není 0 modulo b. Čtverec minima je tedy 4.

Číselná tabulka tím není vyvrácena; chybná je poznámka o počtu dvojic.
Počet rovin pro posunutou mříž zůstává samostatný C0038, nikoli skrytý
předpoklad tohoto L1 algoritmu.

## Redukce a půlčíselné zaokrouhlení

Úloha 18: pro J složenou z jedniček, y=(1-m)/3, m>1 a m=1 modulo 3,
jsou U=I-yJ a V=mI+yJ. Z J²=3J vyjde UV^T=mI, det U=m a součet
každého řádku U je m. Přímé skalární součiny dávají

```
V_j·V_k=(1-m²)/3       pro j!=k,
V_j·V_j=(2m²+1)/3,
U_j·U_j=(m²+2)/3.
```

**C0045** je opačné znaménko prvního vzorce. S5 používá absolutní
hodnotu, takže hlavní příklad je správný: všechny redukce selžou,
z_j je asymptoticky sqrt(2)*m/3 a půlkvádr roste kubicky. Rozdíly
řádků U přesto mají čtverec normy 2; normu 1 vylučuje kongruence.
Po záměně rolí U,V dává redukce s j=1 oba násobky q=1. Řádky
U2=(-1,1,0), U3=(-1,0,1), V1=(1,1,1) souhlasí i s celou tištěnou
maticí pro m=64. Starý výsledek 419280903 pro m=1000 je velikost
kvádru získaná vzorcem, nikoli počet nově vyzkoušených bodů.

Úloha 19: všechny řádky V zůstávají v pevné diskrétní mříži a jejich
normy nerostou. Existuje pouze konečně mnoho možných bází v příslušné
omezené množině. Nekonečný běh by se po posledním přísném zkrácení
skládal z půlek s q=1 a musel by opakovat bázi. Tyto změny U mají
elementární matice I+E_ji. Jejich neprázdný součin nemůže být I:
nezáporné přidané prvky nemohou zmizet. Tím je doplněn konečnostní krok
tištěného argumentu. Když se dovolí i q=-1 při záporné půlce, důkaz
neplatí. Uložený příklad se třemi řádky (1,-1,0),(0,1,-1),(1,1,1)
má cyklus 18 průchodů indexu j a 12 provedených změn. Seznam změn
v JSON odpovídá přesným skalárním součinům; nebyl znovu spouštěn.

## Skutečná orbita a její mřížový obal

Úloha 20: pro m=2^e, e>=3 a a=5 modulo 8 má lichá orbita periodu
m/4 a obsahuje jednu celou třídu modulo 4. Substituce X=4Y+tau,
tau=X0 mod4, dává přírůstek ((a-1)/4)*tau modulo m/4. Známá oprava
z 25. července 2005 doplňuje chybějící tau i správný vektor posunutí.
Tuto chybu nepočítáme mezi nové nálezy. Dolní hranice e>=3 je zde
součástí použitého periodového tvrzení; malá větev m=4,a=3 má periodu 2
a musí být oddělena, nikoli zahrnuta do m/4.

**C0046 potvrzen.** Pro typ a=3 modulo 8 nelze všechny skutečné body
převést jedinou pevnou reflexí souřadnic na tvrzenou posunutou mříž
s modulem m/4. Rozhodující příklad m=16,a=3,X0=1 má body
(1,3),(3,9),(9,11),(11,1), dělené 16. Rozdíly od prvního bodu jsou
p=(1,3)/8, q=(1,1)/2 a r=(5,-1)/8. Platí

```
q-4p=(0,-1),
8p-3(0,1)=(1,0),
r=5p-2(0,1).
```

Jejich celočíselný obal je tedy generován p a (0,1) a již obsahuje Z².
Všechny přípustné normály jsou celá (u,v) s u+3v=0 modulo 8.
Nejkratší jsou ±(2,2); všechny menší možné čtverce 1,2,4,5 se
vyloučí přímým dosazením. Skutečný největší rozestup je 1/sqrt(8).
Vytištěná redukce modulo 4 připouští ±(1,1) a dává 1/sqrt(2).
Důkaz zde nezávisí na sporné konvenci o přidávání periodických kopií:
Z² již leží v obalu rozdílů konečné množiny. Při reflexi druhé
souřadnice se také přímo liší uvedené dvě množiny čtyř bodů.

Obecně D=gcd(m,{x-X0})=gcd(m,a-1), protože X0 je liché a první
rozdíl je (a-1)X0 modulo m; ostatní jsou jeho násobky. Celočíselná
normála má konstantní fázi na orbitě právě tehdy, když
`sum u_j*a^j=0 modulo (m/D)`. Pro typ 5 vyjde D=4, pro typ 3 D=2.
Tento vzorec určuje afinní mřížový obal s periodickými kopiemi.
Netvrdí, že orbita typu 3 obsahuje všechny jeho body v jednotkové krychli.
Přijatý konečný test kontroloval 120 orbit a 18000 normál; obecný
argument nestojí na tomto omezeném soupisu.

RANDU má pro dimenze 2–9 stejné minimum i po přechodu z kongruence
modulo 2^29 na modulo 2^30: silnější mříž je podmnožinou slabší
a v každé dimenzi má již doložený svědek stejnou minimální normu.
Nová krátká kontrola těchto osmi svědků patří do předchozího bloku
`sequential-spectral-certificates.json`; nyní se neopakovala.
Jde o rovnost nu, **nikoli důkaz shodného normalizačního jmenovatele
pro mu**. Normalizace periodou a normalizace hustotou celého obalu
jsou u typu 3 různé; knižní aritmetický výsledek mu9=11.98 s 2^29
zůstává zvlášť označen. Nález nestojí na tvrzení, že celý řádek RANDU
má chybné hodnoty.

Z archivovaného Steele–Vigna znovu přečteny pasáže §2 a §7 o typech
3/5 a spektrálních konvencích. Autoři sami omezují vyhledávání na
typ 5. Článek nepoužíváme jako nezávislý důkaz opravy m/2. Jeho
experimenty a seznam doporučených násobitelů se zde neprověřovaly.

Úloha 21: pro d=gcd(4,m) podposloupnost X_(4n) navštíví m/d stavů
jedné třídy modulo d. Vybraná trojice má modulo 1 základní směr
`d*(1,a²,a³)/m` a konstantní posun
`(X0*(1,a²,a³)+c*(0,a+1,a²+a+1))/m`.
Přidáme-li e2,e3, dostaneme celý periodický obal. **C0048** je jen
malá hranice: pro m=2,a=c=1 je jediná trojice (0,0,1/2), její kopie
jsou posunem Z³. Tištěná báze má determinant 2; náhrada 4 hodnotou
d=2 dává determinant 1. Pro e>=2 je tištěná báze správná. Starých
252 modelů je přijato bez opakování.

## Výzkumné otázky a rekurence druhého řádu

Úlohy 22/23 jsou v originálu označeny M46 a nemají tištěnou odpověď.
Kontrolujeme formulaci a konkrétní tvrzení; jejich stav není prohlášením,
že jsme vyřešili všechny výzkumné otázky. V úloze 22 obě Hermitovy
konstanty souhlasí. Obecná mez z úlohy 8 neurčuje optimální vzájemný
vztah při přibližování k maximům. Původní rešerše nenašla rozhodující
primární řešení; není tím dokázáno, že je problém dnes otevřený.

V úloze 23 Alexeevova konstrukce skutečně dává dualitu, jednotkové
řádky U a normu V1 na druhou (t+2)/3. Všechny párové podmínky se
ověří přímo ze součinů 1/2,1/4,-2/3 a diagonály 4/3. Pro t=2
dává Gramova matice ((1,r),(r,1)), |r|<=1/2, horní mez 4/3.
Nezávisle znovu přezkoumán uložený důkaz neomezenosti pro t>=6:
symetrická uvedená matice C má C²=5I; pro p²-5q²=1 a N=p²+5q²
matice U=(pI+qC)/sqrt(N), V=sqrt(N)*(pI-qC) jsou duální,
jejich Gramovy diagonály jsou 1 a N² a oba párové testy plynou z
`N-4pq=(p-2q)²+q²>0`. Rekurence p'=9p+20q,q'=4p+9q zachovává
Pellovu rovnici a roste. Už p=9,q=4 dává N²=25921. Pro vyšší
dimenze se přidá jednotkový blok. Alternativní důkaz přes
`(I+rC)^(-1)=(I-rC)/(1-5r²)` potvrzuje neomezenost pro
r blížící se 1/sqrt(5) zdola. Dimenze 3–5 nejsou vyřešeny.
Toto není nová chyba knihy ani prohlášení prvenství; historické
„known to be achievable“ není tvrzení o univerzální horní mezi.

Úloha 24: plná nenulová orbita rekurence druhého řádu pokrývá všechny
nenulové stavy F_p². Lineární funkce konstantní na nich je nulová:
pro p>2 stačí v,2v; pro p=2 použijeme v,w,v+w. Přidání nulového
stavu tedy nemění afinní rodiny s celočíselnou normálou. Koeficientová
matice R se aktualizuje násobením ((0,b),(1,a)); její poslední
sloupec (f,g) popisuje nový člen. Pro t=4 jsou obě vytištěné
kongruence u1+b*u3+ab*u4=0 a u2+a*u3+(a²+b)*u4=0 správné.

Inicializace U=pI2,V=I2 má UV^T=pI a duální determinant p².
Nový řádek (-f,-g,0,...,1) spolu se starými řádky doplněnými nulou
generuje přesně obě kongruence. Nová poslední souřadnice V_i je
V_i1*f+V_i2*g. Odečtení qp od ní se musí vyvážit přičtením qU_i
k novému řádku U_t, přesně podle S4'. Poslední řádek V je p*e_t.
Všechny indexy, inicializace s a návaznost na S5–S10 souhlasí.
Uložených 31 primitivních rekurencí a 124 nezávisle porovnaných minim
je přijato po čtení programu a logu; velký příklad se neopakoval.
Obecná poznámka o řádu k používá k koeficientových kongruencí a stejnou
maticovou konstrukci; tato kontrola neprohlašuje nové hledání všech
primitivních rekurencí ani kontrolu všech příkladů citovaných autorů.

## Errata, bibliografie a pokračování

Znovu prohledány čtyři úplné vrstvy errat i aktuální TeX podle stran,
odpovědí a klíčových výrazů. Zaznamenány opravy Alexeevova jména na
117 z roku 2001 a seedu na 581 z roku 2005; navazující změny úloh 26/31
jsou předány dalšímu bloku. Žádná nalezená položka neopravuje C0044–48.
Pozdější fyzický dotisk ani prvenství nejsou ověřeny. Přesné odstavce
Dieter 1975, osobní Gosperova atribuce a citované numerické příklady
Grube / L’Ecuyer–Blouin–Couture nebyly nově dohledány a jsou výslovné
bibliografické výjimky; algebra výše je prověřena nezávisle. Žádné nové návrhy zpráv
nevznikly a nic nebylo odesláno.

Další kurzor: původní 109, F/G, potom úlohy 25–32 a odpovědi 582–584.
