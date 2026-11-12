# V2-C0137: maximum continuantu v úloze 4.5.3-37

Stav: **confirmed**, zadání 378, odpověď 654. První tvrzení
neplatí pro povolené opakované vstupy. Při navzájem různých
kladných celých vstupech je správné. Druhé tvrzení o minimu
je správné i s opakováním. Obě kladná tvrzení níže dokazujeme.

Continuant K(a_1,...,a_n) je polynom, který dává jmenovatel
řetězového zlomku [0;a_1,...,a_n]. Definujeme jej rekurencí

```
K()=1, K(a)=a,
K(a_1,...,a_n)=a_n K(a_1,...,a_(n-1))+K(a_1,...,a_(n-2)).
```

Písmena A,B,C označují konečné posloupnosti; jejich zřetězení
píšeme bez čárky. B^R je B v obráceném pořadí. Všechny jejich
členy jsou kladná celá čísla, pokud není výslovně řečeno jinak.

## 1. Krátký protipříklad a celá rodina

Vezměme multiset {1,2,2,2,2}. Předepsané pořadí pro maximum
vynucuje (2,2,1,2,2). Jeho continuant je však 45, zatímco
permutace (2,1,2,2,2) má hodnotu 46. Rekurence dává po sobě

```
(2,2,1,2,2):  K_0,...,K_5 = 1,2,5,7,19,45;
(2,1,2,2,2):  K_0,...,K_5 = 1,2,3,8,19,46.
```

Obecně pro libovolná celá 1<=a<b je

```
K(b,b,a,b,b)=a(b^4+2b^2+1)+2b^3+2b,
K(b,a,b,b,b)=a(b^4+2b^2)+2b^3+3b.
```

Rozdíl druhé hodnoty minus první je b-a>0. Všechny vstupy
přitom vyhovují zadání. Není třeba zjišťovat globální maximum,
aby byla vyvrácena maximalita předepsaného uspořádání.

Bezpečná oprava první části je doplnit, že a_1,...,a_n jsou
**navzájem různá** kladná celá čísla. Důkaz v části 4 tuto
opravu ověřuje nezávisle na citovaném článku. Minimum doplnění
nepotřebuje, jak ukazuje část 3.

## 2. Dvě identity pro obracení bloku

Definujme R(A)=[0;A], tedy převrácenou hodnotu kladného
řetězového zlomku se členy A, a R()=0. Pro neprázdné A platí

```
R(A)=K(A bez prvního členu)/K(A),       0<R(A)<=1.
```

R(A^R) obdobně vznikne odstraněním posledního členu A.
Definujme také

```
Q(B)=K(B bez posledního členu)-K(B bez prvního členu).
```

Součin symetrických matic M(a)=[[a,1],[1,0]] má v prvním
řádku hodnoty K(A),K(A bez posledního členu). Obrácení B
transponuje jeho maticový součin. Vynásobení levým řádkem
pro A a pravým sloupcem pro C proto dává

```
K(ABC)-K(AB^R C)
 = K(A)K(C) (R(C)-R(A^R)) Q(B).                       (R1)
```

Pro prázdný A či C zde použijeme K()=1 a R()=0.

Je-li B=(b_1,...,b_t), t>=2, a b_1!=b_t, potom

```
sign Q(B)=sign(b_1-b_t).                              (R2)
```

Pro t=2 je to přímé. Pro t>=3 položme I=(b_2,...,b_(t-1)).
Rozvoj z obou konců dává

```
Q(B)=(b_1-b_t)K(I)+K(I bez posledního)-K(I bez prvního).
```

Oba poslední continuanty jsou kladné a nejvýše K(I), takže
absolutní hodnota jejich rozdílu je ostře menší než K(I).
Protože nenulové celé b_1-b_t má absolutní hodnotu alespoň 1,
platí (R2). Když krajní hodnoty souhlasí, (R2) se netvrdí.
Níže v takovém případě ponecháme již správný kraj na místě.

Pro část 3 budeme potřebovat ještě jednoduchou monotonicitu:
f_h(x_1,...,x_h)=[0;x_1,...,x_h] pro kladné reálné argumenty
klesá v lichých pozicích a roste v sudých. To plyne skládáním
zobrazení x -> 1/x. Prodloužení rozvoje za h-tý člen přičte
k tomuto poslednímu argumentu nezápornou hodnotu R(ocasu);
změna celé hodnoty má tedy znaménko (-1)^h.

## 3. Minimum je správné i s opakováním

**Konstrukce.** Do pozic 1,n vložíme postupně dva nejmenší
zbývající členy, do pozic 2,n-1 dva největší, do pozic 3,n-2
znovu dva nejmenší a tak dále. Poslední osamocená pozice
vezme poslední člen. To je přesně pořadí předepsané v knize.

**Myšlenka důkazu.** Začneme libovolnou permutací a zafixujeme
postupně tytéž krajní pozice. Potřebný člen přesuneme na místo
obrácením jediného souvislého bloku. Již zvolené krajní členy
poskytují střídavé dolní a horní meze pro R v (R1). Spolu
s (R2) to zaručí, že žádné obrácení nezvětší K.

Předpokládejme, že z obou stran je již správně zafixováno r
členů. Označme je l_h=a_h a d_h=a_(n-h+1), h=1,...,r.
Člen l_h byl vybrán jako minimum zbývajících hodnot při lichém
h, jako maximum při sudém h; d_h byl vybrán jako následující
minimum či maximum po odebrání l_h. Tyto extremální vlastnosti
zůstávají platné při všech pozdějších změnách uvnitř pole.

Nejprve vybíráme nový levý člen na i=r+1. Pokud již má
požadovanou extremální hodnotu, nic neměníme. Jinak najdeme
požadovaný člen na některém j>i, j<=n-r, a obrátíme B=a_i...a_j.
V (R1) je A=a_1...a_r a C=a_(j+1)...a_n.
Tvrdíme, že

```
(-1)^r (R(C)-R(A^R)) >= 0.                            (R3)
```

Pro r=0 je to R(C)>=0. Pro r>0 má C alespoň r členů.
Porovnejme jeho h-tý člen c_h=a_(j+h) s l_(r-h+1).
Index j+h leží uvnitř pole, z něhož byl tehdy tento levý
krajní člen vybrán: pro s=r-h+1 platí

```
s <= j+h <= n-s+1.
```

Proto je c_h>=l_s při lichém s a c_h<=l_s při sudém s.
Při přechodu z [0;l_r,...,l_1] na [0;c_1,...,c_r] tudíž
každá změna argumentu mění hodnotu ve směru (-1)^r podle
monotonicity z části 2. Případný zbytek C má stejný účinek.
To dokazuje (R3).

Je-li r sudé, vybíráme minimum: b_1>b_t, takže Q(B)>0,
a (R3) dává R(C)-R(A^R)>=0. Je-li r liché, vybíráme
maximum: b_1<b_t, Q(B)<0 a rozdíl R je <=0. V obou
případech je pravá strana (R1) nezáporná, tedy nová hodnota je nejvýše stará. Nový levý člen je správně zafixován.

Nyní zafixujeme pravý člen na n-r stejným typem extrému,
ale až po odebrání nového levého členu. Postup zrcadlíme.
Jeho pevný prefix má členy d_r,...,d_1. Přesouvaný člen
před zrcadlením leží na j>=r+2. H-tý člen protějšího kontextu
je a_(j-h). Pro s=r-h+1 leží v intervalu

```
s+1 <= j-h <= n-s+1.
```

Právě tento interval byl k dispozici, když jsme vybírali d_s
po odebrání l_s. Má tedy stejnou potřebnou mez vůči d_s.
Protější kontext má alespoň r+1 členů. Tentýž argument
monotonicity dokazuje zrcadlenou (R3), a opět (R1),(R2)
zaručují nezvětšení K. Obrácení nepohne již zafixovanými
kraji. Indukce skončí v předepsané permutaci, která je proto
globálním minimem. Rovnosti vstupů nikde nevadí.

## 4. Maximum po doplnění různých vstupů

Nyní předpokládejme, že všechny vstupy jsou navzájem různé.
Do pozic 1,n,2,n-1,3,n-2,... chceme postupně vkládat
zbývající největší hodnoty. Opět použijeme obrácení bloku.

Při levém kroku s r zafixovanými členy na každé straně je
A=a_1...a_r. Pro r=0 platí R(C)>=R()=0. Pro r>0 je
první člen c_1 kontextu C menší než a_r: leží buď uvnitř
zbývajícího pole, nebo na nejbližším pevném pravém kraji.
Celá čísla jsou různá, takže c_1<=a_r-1. Zapišme

```
R(A^R)=1/(a_r+eta),    R(C)=1/(c_1+delta),
0<=eta<=1,            0<=delta<=1.
```

Pak c_1+delta<=a_r<=a_r+eta, a tudíž R(C)>=R(A^R).
Pokud levý člen není již největší, má obracený blok b_1<b_t,
tedy Q(B)<0. Z (R1) plyne staré K <= nové K.

Pravý krok má po zrcadlení tutéž vlastnost: první člen
protějšího kontextu je menší než nejbližší pevný pravý člen.
Nově vybraný levý člen je také menší než všechny dříve pevné
členy. Tentýž důkaz proto platí. Indukce převádí libovolnou
permutaci na knižní uspořádání bez poklesu K; to je globální
maximum. Předpoklad rozdílu alespoň 1 je právě místo, kde
opakované hodnoty nelze automaticky zahrnout.

## 5. Prameny a rozsah kontroly

Původní zadání na 378 a odpověď na 654 byly vizuálně přečteny.
V zadání není podmínka různosti. Všechny čtyři řady
all2-prepre, all2-pre, all2 a err2 byly 2026-11-03 prohledány
podle stránek, úlohy 37, jmen Motzkin/Straus a hesla
organ-pipe. Oprava podmínky nalezena nebyla. Zásah na 378
z roku 2020 se týká úlohy 43. Poslední fyzický dotisk a
priorita nálezu neověřeny; návrh hlášení zůstává neodeslán.

Původní článek Motzkina a Strause (Proc. AMS 7, 1956,
1014–1021; DOI 10.1090/S0002-9939-1956-0083457-1) se
nepodařilo získat: vydavatelské PDF vrátilo 403. Netvrdíme,
že původní článek obsahuje chybu TAOCP.

Vizuálně přečtena strana 2 každé z následujících prací:
Ramharter, *Maximal continuants and periodicity* (2006);
De Luca–Zamboni, arXiv:2108.11313 (2021);
De Luca–Edson–Zamboni, arXiv:2105.00496v2 (2023).
Všechny rozlišují původní výsledek pro různé členy od
pozdějšího řešení s předepsanými násobnostmi. Poslední práce
uvádí na straně 2 i jiné obecné maximalizující uspořádání,
které v našem příkladu dává (2,1,2,2,2). Zde se nepřebírá
jeho obecný důkaz ani se netvrdí audit celých těchto článků.
Části 2–4 jsou samostatný obecný důkaz výsledků potřebných
pro opravenou úlohu.

## 6. Nezávislé konečné kontroly

Běh verify_euclid_rearrangements.py, PID 1220711, relace 50507,
limit 120 s, exit 0 (4,37 s): 210 členů rodiny protipříkladů;
3279 srovnání rekurence s nezávislým součtem vah dláždění cesty
jednotlivými vrcholy a dvojicemi sousedních vrcholů; 3006 identit
(R1), 2004 znamének (R2). Konstrukce minima ověřena krok za
krokem na 29523 vstupech, celkem 97062 obratů. Konstrukce
maxima pro různé členy na 47193 vstupech, 241332 obratů.
Každý obrat má přesně zkontrolované oba faktory v (R1),
směr změny a dosažení konečného předepsaného uspořádání.

Dřívější pilot porovnal minimum se všemi 265719 posloupnostmi
nad {1,2,3} délky 1 až 11; výsledek prošel. Další pilot určil
minima přes všechny permutace 1..n pro n<=8. Tyto hotové
výpočty nebyly znovu opakovány; finální běh kontroluje nově
jednotlivé kroky důkazu. Obecné závěry zajišťují části 2–4,
nikoli samotné konečné enumerace.
