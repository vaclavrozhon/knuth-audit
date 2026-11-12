# Inverzní generátory: §3.2.2-34–37

Stav 1. listopadu 2026: všechny čtyři úlohy a související text na
str. 32–33 matematicky prověřeny. Dvě drobné chyby v důkazech:
[C0013](C0013-inversive-doubling-index.md), chybný index v odpovědi 36,
a [C0014](C0014-inversive-pole-sign.md), nedokončená oprava znamének
v odpovědi 37. Hlavní tvrzení obou úloh jsou správná. Podkladem je
první tisk třetího vydání 1997, str. 40 a 558–559, viz původní obrázky.

## Značení a projektivní přímka

Pro prvočíslo p značí F_p těleso zbytků modulo p. Přidáním symbolu
infinity vznikne **projektivní přímka** P=F_p∪{infinity}, obsahující
p+1 bodů. Pro a!=0 je zobrazení F(x)=c+a/x její permutací:
F(0)=infinity a F(infinity)=c. Takový předpoklad je potřebný už
pro smysl aritmetiky s infinity v textu. Podmínka(i) úlohy 34 jej
sama vynutí, takže nevznikají dodatečné vyhovující případy s a=0.
Při implementaci s 0^(-1)=0 se bod infinity vypouští a plný cyklus
má p bodů, zatímco věty34–37 používají nevypuštěný cyklus p+1.

Zaveďme q_0=0, q_1=1 a q_(n+1)=c*q_n+a*q_(n-1). Pro matici
T=((0,1),(a,c)) dokazuje indukce

```
T^n = ((a*q_(n-1), q_n), (a*q_n, q_(n+1))),
F^n(x) = (q_(n+1)*x+a*q_n)/(q_n*x+a*q_(n-1)),
x^n mod (x^2-c*x-a) = q_n*x+a*q_(n-1).                 (I)
```

Zlomek je vyhodnocen projektivně, takže nenulový čitatel s nulovým
jmenovatelem znamená infinity. Oba nemohou být současně nulové:
det(T^n)=(-a)^n!=0. Matice T působí na řádkové souřadnice (1,x).
Identita posledního řádku se týká formální proměnné x, nikoli hodnoty
počátečního stavu, i když kniha používá stejné písmeno.

## Úloha 34: přesná podmínka plné periody

Z(I) plyne, že F^n(0)=0 právě tehdy, když q_n=0. Tehdy je T^n
nenulová skalární matice, protože q_(n+1)=a*q_(n-1), a zbytek
polynomu x^n je nenulová konstanta. Naopak nenulová konstanta dává
q_n=0. Hledáme tedy nejmenší kladné n, pro které je x^n skalár.

Podmínka(i) říká, že tento nejmenší n dělí p+1. Podmínka(ii) vylučuje
každý vlastní dělitel: vlastní dělitel p+1 dělí (p+1)/q pro nějaké
prvočíslo q|(p+1). Dřívější n nemůže dát nulový skalár, neboť x je
jednotka v podílovém okruhu; a!=0. Výsledná perioda bodu0 je p+1,
tedy jediný cyklus celé P, a proto stejná perioda platí pro každý seed.
V opačném směru plná perioda libovolného seedu obsahuje celou P
včetně0 a obě podmínky následují. Platí také pro p=2.

## Úloha 35: počet vhodných dvojic

Redukovatelný kvadratický polynom s nenulovými kořeny je buď součin
dvou různých lineárních faktorů, nebo druhá mocnina jednoho.
V prvním případě x^(p-1)=1 v podílovém okruhu, ve druhém je x^p
skalár. Ani možnost nemá nejmenší skalární exponent p+1. Případ
nulového kořene odporuje podmínce(i). Hledané polynomy jsou tedy
ireducibilní.

Těleso F_(p²) má cyklickou multiplikativní grupu řádu p²-1.
Zvolme její generátor zeta. Podgrupa F_p^* sestává z mocnin
zeta^(p+1). Pro kořen theta=zeta^j je nejmenší n s theta^n∈F_p^*
rovno (p+1)/gcd(j,p+1). Hledáme právě gcd(j,p+1)=1. Mezi exponenty
modulo p²-1 jich je (p-1)*phi(p+1), kde phi(N) počítá zbytky
nesoudělné s N. Každý kvadratický polynom má dva různé konjugované
kořeny theta a theta^p; oba splňují stejnou podmínku. Počet dvojic je

```
(p-1)*phi(p+1)/2 = (p²-1)/2 * product_(q prime, q|p+1) (1-1/q).
```

Přesně odpovídá odpovědi 35. Nejde o počet pouze primitivních
kvadratických polynomů: stačí plný řád v podílu F_(p²)^*/F_p^*.

## Úloha 36: mocniny dvou

Nyní a=1 mod4, c=2 mod4, m=2^e a e>=3. Liché zbytky jsou všechny
jednotky modulo m a F je permutuje. Posloupnost q modulo 4 je
0,1,2,1 opakovaně, přímo z rekurence. Z(I), popřípadě součinem
matic T^n*T^n, plynou správné celočíselné identity

```
q_(2n) = q_n*(q_(n+1)+a*q_(n-1)),
q_(2n-1) = a*q_(n-1)^2+q_n^2,
q_(2n+1)-a*q_(2n-1)
 = (q_(n+1)-a*q_(n-1))*(q_(n+1)+a*q_(n-1)).             (II)
```

Poslední faktor je v knize chybně vytištěn; viz C0013. Při sudém n
je součet q_(n+1)+a*q_(n-1)=2 mod4. Začneme q_1=1, q_2=c a pomocí
prvního řádku(II) indukcí dostaneme v2(q_(2^h))=h pro každé h>=0;
v2(z) značí počet faktorů 2 v nenulovém celém čísle z. Dále
q_(n+1)-a*q_(n-1)=c*q_n dává v2 tohoto rozdílu =h+1 při n=2^h.

V projektivním vzorci pro F^n(1) jsou čitatel A=q_(n+1)+a*q_n
a jmenovatel B=q_n+a*q_(n-1). B je lichý pro n=2^h, včetně n=1.
Jejich rozdíl má zvlášť jednoduchý tvar

```
A-B = (a+c-1)*q_n,   v2(A-B)=h+1 při n=2^h.            (III)
```

Proto F^(2^(e-1))(1)=1 mod2^e, ale F^(2^(e-2))(1)!=1 mod2^e.
Nejmenší perioda dělí první exponent a nedělí jeho polovinu, tedy
je přesně 2^(e-1). Vyčerpá všechny liché zbytky; každý lichý seed
má tutéž periodu. Knižní kongruence mezi A,B s posunem 2^(h+1)
mod2^(h+2) je také přesně(III).

Nutnost podmínek je správná. Pro a liché a c sudé platí modulo 8
F(x)=a*x+c, protože každé liché x splňuje x^(-1)=x mod8. Pak
F²(1)=1+c*(a+1). Plný cyklus lichých zbytků modulo 8 vyžaduje
F²(1)!=1, tedy právě a=1 mod4 a c=2 mod4. Opačná parita,
a sudé a c liché, sice také zachovává liché stavy, ale
F(x+m/2)=F(x), takže není permutací a nemůže mít plný cyklus.
Knižní doplňující věta „otherwise X_(2n)=1 mod8“ používá běžný
předpoklad a liché,c sudé. Bez něj neplatí: a=2,c=1 vede
1→3→7→7 modulo 8. Toto upřesnění není samostatný nový nález;
samotná nutnost podmínek i hlavní zadání36 jsou správné.

Redukce plného cyklu modulo2^j má periodu2^(j-1) pro j>=3.
Tím je přesně vysvětlen komentář o krátkých periodách nižších bitů.
Je to strukturální vlastnost, nikoli důkaz univerzální statistické
převahy prvočíselného modulu ve všech aplikacích.

## Úloha 37: proč nadrovina obsahuje nejvýše d bodů

Nadrovinou nad F_p rozumíme množinu řešení r_1*v_1+...+r_d*v_d=r_0,
kde alespoň jeden koeficient r_1,...,r_d je nenulový. Posuny časů
b_1,...,b_d jsou různé modulo p+1. Posunutím společného počátku
můžeme předpokládat b_1=0; ostatní jsou v 1,...,p. Jediný cyklus
P znamená, že vynechání infinity v každé souřadnici odstraní právě d
různých časů, tedy |V|=p+1-d.

Pro j>=2 položme s_j=q_(b_j), u_j=a*q_(b_j-1)/s_j a

```
t_j = a-a*q_(b_j+1)*q_(b_j-1)/s_j² = -(-a)^(b_j)/s_j².
```

Podle úlohy 34 je s_j!=0, jinak by dřívější mocnina T byla skalární.
Dále t_j!=0 z determinantu. Identita(I) se přepíše na

```
F^(b_j)(x) = q_(b_j+1)/s_j + t_j/(x+u_j).              (IV)
```

Pólem je **x=-u_j**, nikoli u_j. Póly jsou různé: jejich shoda by
znamenala, že ze stejného stavu dospějeme do infinity po dvou
různých počtech kroků menších než p+1, proti plné periodě.
Znaménko ve(IV) opravilo erratum 3. 2. 2005; navazující dosazení
na str. 559 zůstalo chybně kladné, což je C0014.

Dosadíme(IV) do rovnice nadroviny a vynásobíme
D(x)=product_(j=2..d)(x+u_j). Dostaneme polynom P(x) stupně nejvýše d.
Kdyby nadrovina obsahovala d+1 bodů V, P by měl d+1 různých kořenů,
a byl by identicky nulový. Dosazení x=-u_j pak dává
r_j*t_j*product_(ell!=j)(u_ell-u_j)=0, tedy r_j=0 pro j>=2.
Zbývající P=(r_1*x-r_0)*D vynutí také r_1=r_0=0, spor.
Pro d=1 je D=1 a důkaz zůstává platný. Pokud |V|<d+1, tvrzení
je prázdné a netřeba předpokládat, že taková podmnožina existuje.

Libovolných d bodů naopak leží v nějaké nadrovině: d homogenních
lineárních rovnic v d+1 koeficientech r_0,...,r_d má nenulové řešení.
To potvrzuje obě části úlohy i ekvivalentní formulaci s nezávislostí
řádků matice (1,v_1,...,v_d). Výrok na str. 33 o nepřítomnosti
mřížkové struktury je vykládán přesně v tomto prokázaném smyslu.

## Výpočty a zdroje

`verify_inversive.py` / `results/inversive.json`, exit 0:

- Všech 74836 dvojic a!=0,c pro prvočísla p<=101; celkem 3322025
  přímo iterovaných stavů. Polynomické mocniny, délka cyklu a počty
  z úlohy 35 se shodují. Pro p<=13 dalších 49938 porovnání(I)
  s maticemi a přímými iteracemi ze všech počátečních bodů.
- Všech 5460 vhodných parametrů pro e=3,...,8, celkem 599184 stavů.
  Dalších 2720 parametrů obou parit zachovávajících liché stavy
  pro e=3,...,6 ověřuje nutnost včetně neprostých zobrazení.
- 38400 přesných celočíselných identit(II), včetně záporných
  koeficientů; dále kontrola dvouadických ohodnocení a kongruence(III).
- Pro všechna plnoperiodická a,c s p<=13 a všechny relativní sady
  posunů v dimenzích 1–3: 1201827 nenulových determinantů přímo
  vytvořených bodů, vedle 8414 samostatných kontrol(IV).

Původní sazba str. 558–559 a errata str. 31 vizuálně přečteny;
`images/vol2-p558-inversive-detail.png` je jen věrný zvětšený výřez.
Prohledány čtyři vrstvy errat a aktuální TeX, stav 1. 11. 2026.
Relevantní oprava 3. 2. 2005 mění jen dva jmenovatele na str. 558;
žádná oprava indexů36 ani dosazení37 na str. 559 nalezena.
Novější fyzický tisk neověřen; digitální náhled 2026 odpovědi neobsahuje.

Citace 1988 má institucionální primární
[záznam](https://open.metu.edu.tr/handle/11511/66701) se shodnými autory,
rokem a tématem. Pokusy získat plné PDF 1988 a 1991 od AMS skončily 403,
zrcadlo nebylo síťově dostupné. Nepředstíráme přečtení jejich důkazů:
audit matematických vět zde stojí na výše uvedených vlastních důkazech
s nezávislými přesnými kontrolami. Metadata a neúspěšné pokusy jsou
zapsány v `sources/inversive-citations.json`.
