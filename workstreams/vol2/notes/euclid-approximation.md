# §4.5.3-42–44: nejlepší aproximace a mediantové zaokrouhlení

Původní zadání 378–379 a odpovědi 656 byly vizuálně přečteny.
Úlohy 42 a 44 jsou správné; 43 má známou opravu chybějících
řádků pouze v dotiscích 2019, opravenou 2020-01-01. Obsah
těchto řádků je v našem dotisku 1997 přítomen. Čtyři řady
errat a aktuální TeX byly prohledány 2026-11-03.

## 1. Nejlepší aproximace druhého druhu: úloha 42

Pro reálné X z (0,1] označíme jeho pravidelný řetězový
zlomek [0;A_1,A_2,...]. Jeho n-tý konvergent, tedy hodnota
useknutého rozvoje, je p_n/q_n=[0;A_1,...,A_n]. Počáteční
hodnoty jsou p_0=0,q_0=1,p_(-1)=1,q_(-1)=0. Souřadnice
splňují p_n=A_n p_(n-1)+p_(n-2), obdobně q_n.
Označení ||y|| znamená vzdálenost y od nejbližšího celého čísla.

**Myšlenka důkazu.** Dva sousední konvergenty tvoří celočíselnou
bázi: determinant jejich souřadnic je +1 nebo -1. Menší
jmenovatel q než q_n proto nutí opačná znaménka koeficientů.
Protože chyby sousedních konvergentů mají také opačná znaménka,
příslušné absolutní chyby se sčítají místo odečítání.

Vezměme celé 1<=q<q_n a celé p nejbližší qX. Z determinantové
identity dostáváme jednoznačná celá u,v taková, že

```
(p,q)=u(p_(n-1),q_(n-1))+v(p_n,q_n).                  (A1)
```

Číslo u není nula: jinak by q bylo kladným násobkem q_n.
Pokud v=0, pak u>=1 a
|qX-p|=u|q_(n-1)X-p_(n-1)|>=||q_(n-1)X||.
Pokud v>0, nerovnost q<q_n vynucuje u<0. Pokud v<0,
kladnost q vynucuje u>0. Tedy uv<0.

Položme e_j=q_j X-p_j. Z úplného podílu za n-tým místem
nebo z determinantové identity plyne e_(n-1)e_n<=0;
rovnost může nastat na konečném racionálním konci. V (A1)
se tedy obě chyby sčítají ve stejném směru:

```
||qX||=|u| |e_(n-1)|+|v| |e_n|
       >= |e_(n-1)| >= ||q_(n-1)X||.                 (A2)
```

Tím je dokázán požadovaný výrok pro všechny přípustné n,
včetně konečných racionálních rozvojů. Pro n=1,A_1=1 není
žádné přípustné q, takže není třeba předpokládat, že p_0
je nejbližší celé číslo k X. Neostrá nerovnost je podstatná:
pro X=2/5 jsou ||2X||=||3X||=1/5 a q_n=5.

## 2. Zaokrouhlení přes konvergenty: úloha 43

Zlomek je vždy redukovaný. Přípustnost kladných dvojic
(p,q) je u fixed slash i floating slash formátu uzavřena
směrem dolů v obou souřadnicích: menší čitatel a jmenovatel
nemohou překročit žádnou bitovou nebo obdélníkovou mez.
Používáme také 0/1 a pomocné +infinity=1/0. Dvojice a/b<c/d
má mediant (a+c)/(b+d). Zaokrouhlení vybírá levý nebo pravý
kraj podle polohy vůči mediantu; v rovnosti menší jmenovatel,
při shodě menší čitatel. To je pravidlo ze stran 331–332.

Pravidelný rozvoj x=[a_0;a_1,...] zde znamená přesně
algoritmus podlah z (10) na 358; podle 359 končí racionální
rozvoj členem >=2, pokud má neprázdnou zlomkovou část.
Tato konvence je důležitá právě v rovnosti na mediantu.
Libovolná alternativní reprezentace s poslední jedničkou
by nemusela dát správný tie výsledek, ale není definovaným
pravidelným rozvojem knihy.

Označme P_i=(p_i,q_i) poslední přípustný konvergent a
P_(i+1) první nepřípustný. Předchozí P_(i-1) je také
přípustný. Zlomek x můžeme psát pomocí úplného podílu A:

```
x=(A p_i+p_(i-1))/(A q_i+q_(i-1)),
A=a_(i+1)+z,   0<=z<1.                              (A3)
```

Na cestě ve Sternově–Brocotově stromu jsou mezi těmito
konvergenty postupné mezizlomky

```
P(t)=t P_i+P_(i-1),   t=1,...,a_(i+1).
```

Nechť t je první nepřípustný z nich. Potom P_i a P(t-1)
jsou přípustné meze s determinantem +1 nebo -1 a jejich
mediant je právě P(t). Každý zlomek ostře mezi nimi je
kladnou celočíselnou kombinací těchto mezí (důkaz S2 v
euclid-stern-brocot.md), takže obě jeho souřadnice jsou
alespoň souřadnicemi nepřípustného P(t). Žádný přípustný
vnitřní zlomek tudíž neexistuje: jde o sousední hodnoty.

Protože A>=a_(i+1)>=t, leží x na straně mediantu P(t)
směrem k P_i, nebo přímo na mediantu. V ostrém případě
zaokrouhlení tedy vrací P_i. V rovnosti je A=t=a_(i+1),
rozvoj končí a kanonická konvence dává t>=2. Jmenovatel
druhého kraje je (t-1)q_i+q_(i-1)>=q_i. Shoda je možná
pouze pro i=0,t=2, kdy jsou kraje a_0 a a_0+1; menší
čitatel opět vybírá P_i. Pravidlo je dokázáno i na hranici.

Počáteční konvergent je P_0=(a_0,1), P_(-1)=(1,0).
Je-li již P_0 nepřípustný, jde o přetečení: všechny konečné
přípustné hodnoty jsou pod a_0, mediant poslední z nich
s nekonečnem je nejvýše a_0 a x se zaokrouhlí na nekonečno.
Pro úplnou implementaci tedy dovolíme i i=-1 s tímto
výslovným pomocným konvergentem. To pouze doplňuje způsob
zacházení s nekonečnem ze §4.5.1; indexy prázdné zlomkové
části se nesmí předat neexistujícímu členu rozvoje.

Pro x reprezentovatelné vracíme x přímo. Pro iracionální x
skončí hledání prvního nepřípustného konvergentu, protože
jejich jmenovatele rostou a formát je konečný. Pro racionální
nepřípustné x skončí nejpozději na jeho úplném rozvoji.

## 3. Přičtení a odečtení stejného čísla: úloha 44

Píšeme R pro mediantové zaokrouhlení v obdélníkovém formátu
|p|<M,0<=q<N. Nula a nekonečna mají výše uvedené zvláštní
tvary. Knižní protipříklad M=N=100 je přesný:

```
u=1/3, v=67/99,
u+v=100/99,
R(100/99)=1,
R(1-67/99)=R(32/99)=32/99 != 1/3.                    (A4)
```

První součet je přesně mediant sousedních přípustných hodnot
1/1 a 99/98. Sousednost plyne z determinantu 1 a z toho,
že každý vnitřní zlomek má čitatel alespoň 100. Tie pravidlo
vybere jmenovatel 1. Druhý výsledek je přesně přípustný.
Žádné přetečení nenastane a 3<sqrt(100).

Obecně pro celé k>=3 vezměme M=N=3k+1, u=1/3,
v=(2k+1)/(3k), případně zkrácené. Součet je N/(N-1),
mediant 1/1 a (N-1)/(N-2), a opět se zaokrouhlí na 1.
Výsledkem druhé operace je (k-1)/(3k), který se od 1/3
liší o 1/(3k). Vstupy i druhý výsledek jsou přípustné a
3<sqrt(3k+1). Už M=N=10 dává menší protipříklad
u=1/3,v=7/9, s výsledkem 2/9.

Věta odpovědi o tom, že identita platí „téměř vždy“, nemá
uvedenou pravděpodobnostní míru ani asymptotický parametr.
Jde o kvalitativní komentář; zde z něj neděláme obecný
pravděpodobnostní výrok. Požadované vyvrácení identity je (A4).

## 4. Nezávislé přesné kontroly

Program verify_euclid_approximation.py ověřil 586465 voleb
(X,n,q) pro všechna redukovaná 0<X<1 se jmenovatelem nejvýše
128. Nezávislé zaokrouhlení qX na celé číslo dalo (A2);
zároveň byly přesně ověřeny všechny celočíselné souřadnice
a znaménkové kroky důkazu (A1).

Pro 81 obdélníkových formátů 2<=M,N<=10 a deset floating
slash formátů s 1 až 10 bity byla přípustná čísla vypsána
přímo. Takto nalezení sousedé a mediantové pravidlo poskytly
nezávislé orákulum pro algoritmus posledního konvergentu.
Všech 33765 vstupů prošlo, včetně 6673 přesných mediantů,
5602 návratů nekonečna, reprezentovatelných vstupů a dalších
racionálních hodnot nezávislých na hranicích formátu.
Deset členů rodiny (A4), včetně původních M=N=100, bylo
ověřeno úplným výčtem přípustných hodnot.

Běh 75200, PID 1225243, limit 120 sekund, exit 0, čas
4.23 sekundy. Výsledky jsou v results/euclid-approximation.json.
Žádná nová chyba knihy v tomto bloku nebyla doložena.
