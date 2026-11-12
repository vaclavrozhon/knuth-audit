# V2-C0136: posun horní meze v úloze 4.5.3-38

Stav: **confirmed**, zadání na straně 378. Pomocná horní mez je
nesprávná; dolní mez, kterou úloha požaduje dokázat, je správná.
Níže jsou obecné důkazy obou správných tvrzení.

Pro kladné celé n označuje T(m,n) počet dělení Eukleidova algoritmu,
včetně případného počátečního nulového podílu i posledního nulového
zbytku. Definice (18) na straně 360 je

```
T(m,0)=0,       T(m,n)=1+T(n,m mod n) pro n>=1.
L(n)=max_(m>0) T(m,n).
```

Maximum je konečné, protože počet závisí jen na m mod n. Dále
phi=(1+sqrt(5))/2 je zlatý řez, log_phi logaritmus o tomto základu
a F_j Fibonacciho čísla: F_0=0, F_1=1, F_(j+2)=F_(j+1)+F_j.

## 1. Protipříklad a opravená horní mez

V původní sazbě je bez zaokrouhlovacích závorek napsáno

```
L(n) <= log_phi(sqrt(5)*n+1)-2.                       (B0, chybně)
```

Pro n=3 volání s m=5 provede přesně tři dělení:

```
5 = 1*3+2,   3 = 1*2+1,   2 = 2*1+0.
```

Pravá strana (B0) je přitom menší než 3, neboť
3sqrt(5)+1 < phi^5=(11+5sqrt(5))/2. Tato nerovnost je ekvivalentní
sqrt(5)<9. Není třeba desetinného výpočtu ani počátečního nulového
podílu. Nejmenší protipříklad je již n=1: L(1)=1, zatímco
sqrt(5)+1 < phi^3=2+sqrt(5).

Správná ostrá logaritmická mez a její celočíselná podoba jsou

```
L(n) < log_phi(sqrt(5)*n+1)-1,                        (B1)
L(n) <= ceil(log_phi(sqrt(5)*n+1))-2.                 (B2)
```

Ve vytištěné větě tedy stačí buď nahradit závěrečné -2 za -1
(i s původním neostrým znaménkem), nebo doplnit horní celou část
kolem logaritmu. Nejde o změnu definice T či L.

**Důkaz.** Nechť jedno volání trvá s dělení. Je-li s=1,
n>=1=F_2. Pro s>=2 po prvním dělení zbývá volání (n,r), kde
0<r<n, s počtem s-1 dělení. Věta F, případně přímo zpětné
nerovnosti mezi zbytky, dává

```
n >= F_(s+1).
```

Binetův vzorec sqrt(5)F_j=phi^j-(-1)^j phi^(-j) proto vede k

```
sqrt(5)*n+1 >= phi^(s+1)+1-(-1)^(s+1)phi^(-s-1)
              > phi^(s+1).
```

To platí pro každé m, a dokazuje (B1). Celočíselnost L pak dává
(B2), bez jakéhokoli předpokladu o tom, zda logaritmus je celý.

**Ostrost konstanty.** Pro n=F_(s+1), s>=1, vstup
m=F_(s+2) dosáhne s dělení. Zpětná mez vylučuje více, takže
L(F_(s+1))=s. Rozdíl

```
log_phi(sqrt(5)F_(s+1)+1)-L(F_(s+1))
 = 1 + log_phi(1+phi^(-s-1)-(-1)^(s+1)phi^(-2s-2))
```

konverguje k 1. Žádná větší univerzální odečítaná konstanta
v (B1) tedy není možná.

## 2. Obecný důkaz požadované dolní meze

Dokážeme dokonce ostrou nerovnost

```
2L(n) > log_phi(sqrt(5)*n+1)-2.                       (B3)
```

**Myšlenka.** Vezmeme racionální číslo těsně nad 1/phi. Jeho
řetězový zlomek musí začínat dlouhou řadou jedniček. První podíl
odlišný od jedničky lze vyjádřit pomocí Fibonacciho čísel; tento
výraz převádí vzdálenost od 1/phi na dolní mez počtu dělení.

Případy n=1 a n=2 jsou přímo L(1)=1, L(2)=2. V obou platí
sqrt(5)*n+1 < phi^(2L(n)+2), tedy (B3).

Nechť n>=3, m=ceil(n/phi) a x=m/n. Potom 0<m<n a

```
x=phi^(-1)+epsilon,       0<epsilon<1/n.             (B4)
```

Použijeme kanonický konečný řetězový zlomek
x=[0;a_1,...,a_t], jehož poslední podíl a_t>=2. Označme k první
index s a_k>=2 a z=[a_k;a_(k+1),...,a_t] jeho úplný podíl;
zejména z>=2. Protože x>1/phi>1/2 a x<1, je a_1=1 a k>=2.
Vzorec pro prefix k-1 jedniček je

```
x=(F_(k-1) z+F_(k-2))/(F_k z+F_(k-1)).              (B5)
```

Po dosazení (B4) a vyřešení pro z dostáváme přesně knižní výraz

```
z=(phi^(1-k)+(-1)^k F_(k-1) epsilon)
  /(phi^(-k)-(-1)^k F_k epsilon).                    (B6)
```

Jestliže k je liché, jmenovatel je větší než phi^(-k),
čitatel menší než phi^(1-k), tedy z<phi<2. To odporuje z>=2.
Proto k je sudé. Čitatel v (B6) je pak kladný, a protože z>0,
je kladný i jmenovatel. Můžeme tudíž násobit nerovnost z>=2:

```
2-phi <= phi^k (F_(k-1)+2F_k) epsilon
        = phi^k F_(k+2) epsilon
        = (phi^(2k+2)-phi^(-2)) epsilon/sqrt(5).     (B7)
```

Použili jsme F_(k+2)=F_(k-1)+2F_k a Binetův vzorec se sudým k.
Nyní 2-phi=phi^(-2), a tedy

```
sqrt(5) <= (phi^(2k+4)-1) epsilon
          < (phi^(2k+4)-1)/n,
sqrt(5)*n+1 < phi^(2k+4).                            (B8)
```

Rozvoj m/n má t>=k podílů za úvodní nulou. Při volání T(m,n)
se však tato počáteční nula rovněž počítá, takže
L(n)>=T(m,n)=t+1>=k+1. Z (B8) plyne
log_phi(sqrt(5)*n+1)<2k+4<=2L(n)+2, což je (B3).
Tento krok současně vysvětluje důležitost přesné konvence počítání.

## 3. Rozsah pramenů a errat

Vizuálně přečteno zadání 378, věta F a definice T na 360,
příklady T na 361 a odpověď 654. V zadání nejsou značky horní
ani dolní celé části; v odpovědi naopak m=ceil(n/phi) horní celou
část skutečně má. OCR tento rozdíl nezachovává spolehlivě.

Všechny čtyři řady all2-prepre, all2-pre, all2 a err2 byly
2026-11-03 prohledány podle stránek 378/654, čísla úlohy 38,
jména Mikusiński a sousedních vzorců. Oprava této meze nalezena
nebyla. Zásah na 378–379 z roku 2020 se týká úlohy 43;
opravy na 654 se týkají odpovědí 39 a 40. Aktuální zdroj err2
byl kontrolován i v TeXu. Poslední fyzický dotisk a priorita
nálezu zůstávají neověřené; návrh hlášení je neodeslán.

Vydavatelská stránka Mikusińského článku potvrzuje titul
*Sur certaines fractions continues finies*, svazek 1, strany
203–206 a DOI 10.4064/ap-1-1-203-206. PDF odkaz vrátil 403,
originál zatím nezískán. Metadata uvádějí 1955, kniha 1954;
tento rozdíl není klasifikován jako chyba, protože ročník vycházel
1954–1955 a samotná metadata neurčují datum konkrétního sešitu.
Důkaz (B3) je úplný bez závislosti na nedostupném článku.

## 4. Přesné konečné kontroly

Běh verify_euclid_maximum.py, PID 1217962, relace 33103,
limit 120 s, exit 0 (7,83 s):

- Všech 2098176 zbytkových vstupů pro n<=2048; pro každé n
  spočteno skutečné L(n) a obě správné meze. Původní horní
  mez selhala pro 65 těchto jmenovatelů.
- 8268 konstrukcí m=ceil(n/phi), včetně n=3..8192 a sousedů
  velkých Fibonacciho čísel až F_200. Identita (B6), sudost k,
  znaménko jmenovatele a nerovnosti (B7),(B8) ověřeny přesně
  v kvadratickém tělese Q(phi), tedy bez plovoucí řádové čárky.
- 200 Fibonacciho rodin dosahujících zpětné meze. Tři konkrétní
  protipříklady mají navíc úplné stopy a rigorózní intervalové
  hodnoty vytištěného logaritmu. Pro n=3 je přibližně 2,244046179.

Výpočet podporuje obecné důkazy; neomezené n pokrývají části 1 a 2.
