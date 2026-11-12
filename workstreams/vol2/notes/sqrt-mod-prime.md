# Odmocniny modulo prvočíslo: §4.6.2–15

Stav k 4. listopadu 2026: matematická část úlohy uzavřena. Vlastní důkazy
níže zahrnují přesnou pravděpodobnost, přímé vzorce, Shanksův algoritmus
a Cipollovu metodu. C0207 a C0208 jsou potvrzené chyby doprovodného
tvrzení a vzorce v historických erratech. Samotný Shanksův algoritmus
pracuje správně. Historická omezení jsou oddělena v §7.

Původní zadání 456 a odpověď 681–682 byly vizuálně přečteny; šest vrstev
errat je v `sources/polynomial-factorization-errata.txt`. Oprava ze
7. srpna 2001 správně odvolává původní pravděpodobnost vždy větší než 1/2
a upřesňuje náhodné posuny. Původní oprava na straně 43 byla zobrazena.
Manifest zdrojů a kontrol: `sources/sqrt-mod-prime.json`.

## 1. Předpoklady a rozhodnutí o existenci

F_p označuje těleso zbytků modulo liché prvočíslo p. Případy p=2 a u=0
se vyřeší přímo. Dále u je nenulový prvek F_p. Charakter χ(t) je 0 pro
t=0, 1 pro nenulový čtverec a −1 pro ostatní prvky. Eulerovo kritérium
říká χ(t)=t^((p−1)/2) pro t≠0. Cykličnost násobicí grupy byla obecně
dokázána v [berlekamp.md](berlekamp.md), v části o úlohách 16–17.

Polynom x²−u má dva různé lineární faktory právě při χ(u)=1. Právě tehdy
Frobeniovo zobrazení z↦z^p na F_p[x]/(x²−u) je identické, tedy Q−I=0.
Tím souhlasí počáteční Berlekampovo rozhodnutí s Eulerovým kritériem.
Při výpočtu kořenů dále předpokládáme χ(u)=1 a volíme a s a²=u.
Shanksův algoritmus v §4 navíc sám rozezná i nenulový nečtverec.

## 2. Náhodné posuny: přesný počet

Nechť g_s=gcd(x²−u,(x+s)^((p−1)/2)−1), kde s je rovnoměrné v F_p.
Úspěchem je stupeň g_s rovný 1. Ten nastane právě tehdy, když přesně
jeden z prvků s+a, s−a je nenulový čtverec. Označíme jejich indikátory
I_+, I_−; indikátor čtverce v bodě t je (1+χ(t)−[t=0])/2.

Základní součet je Σ_s χ(s²−a²)=−1. Počet dvojic (s,b) s b²=s²−a²
je totiž p+Σχ; přepsáním na (s−b)(s+b)=a² dostaneme p−1 dvojic,
jednu pro každou nenulovou hodnotu s−b. Dělení dvěma je dovoleno.

Rozvinutí indikátorů, s výjimkami s=±a zahrnutými výslovně, dává

```text
sum_s I_+ I_- = (p − 3 − χ(2a) − χ(−2a))/4,
N := #successful shifts = (p + 1 + χ(2a) + χ(−2a))/2.
```

Pro p≡3 (mod4) je N=(p+1)/2. Pro p≡1 (mod4) je N buď (p−1)/2,
nebo (p+3)/2. Například p=5,u=1 dává 2/5, kdežto u=4 dává 4/5.
To potvrzuje věcnou část známé opravy z roku 2001. Vždy N/p≥1/3,
takže očekávaný počet nezávislých pokusů je nejvýše 3. Každý vyžaduje
O(log p) násobení polynomů stupně nejvýše 1 modulo x²−u. Při školské
aritmetice stojí jedno O((log p)²) bitových operací; celkově tedy
očekávaně O((log p)³). Tato pravděpodobnostní analýza sama nedokazuje
stejnou mez pro deterministické zkoušení s=0,1,2,… .

**C0208.** První vzorec opravy z roku 2001 má místo x+s výraz sx+t,
ačkoli se dále počítají hodnoty s a algoritmus používá posuny. Je-li
p=5,u=1,t=0, žádné s neuspěje. Dokonce i s nenulovým t: pro p=7,u=1,t=3
uspějí jen s=2,5, tedy 2 hodnoty namísto deklarovaných nejméně 3.
Náhrada sx+t výrazem x+s obnoví výše dokázaný počet.

**C0207.** Při p≡1 (mod4) je zbytek x^((p−1)/2) roven u^((p−1)/4),
ale gcd po odečtení 1 nemusí být 1, jak tvrdí strana 681. Je celé x²−u,
pokud u^((p−1)/4)=1, a je 1 při hodnotě −1. Nejkratší příklad:
p=5,u=1, gcd(x²−1,x²−1)=x²−1. Doporučení první gcd vynechat je správné:
v obou případech neposkytne netriviální faktor.

## 3. Přímé vzorce a Atkin

Pro p≡3 (mod4) je r=u^((p+1)/4) kořenem, neboť r²=uχ(u)=u.
Odpovídá také lineárnímu gcd při s=0.

Pro p=8k+5 položme v=(2u)^k a i=2uv². Potom
i²=(2u)^((p−1)/2)=χ(2)χ(u)=−1. Pro r=uv(i−1) tedy platí

```text
r² = u²v²(i²−2i+1) = −2u²v²i = −ui² = u.
```

To dokazuje přesně tištěný Atkinův vzorec. Nulový vstup se musí ošetřit
předem; pro nečtverec se nejprve použije Eulerovo kritérium. Čas je
O(log p) násobení v F_p, tedy O((log p)³) bitových operací.

## 4. Shanks: invariant a ukončení

Pišme p−1=2^e q, kde q je liché a e≥3. Řád prvku je nejmenší kladná
mocnina dávající 1. V S1 se x volí rovnoměrně z 2,…,p−1. Nečtverců je
(p−1)/2 mezi p−2 možnostmi, takže průměrný počet pokusů je
2(p−2)/(p−1)<2. Po úspěchu z=x^q má řád 2^e. Alternativní zkoušení
malých lichých prvočísel v knize využívá kvadratickou reciprocitu:
pro p≡1 (mod4) jsou symboly (p/x) a (x/p) stejné. Stejný náhodný
odhad se na toto deterministické zkoušení automaticky nevztahuje.

V S2 jsou y=z, r=e, t=u^((q−1)/2), v=ut a w=ut²=u^q. Udržujeme

```text
uw = v²,      ord(y)=2^r,      w^(2^r)=1.
```

Je-li u čtverec, platí navíc w^(2^(r−1))=1. Je-li u nečtverec,
má počáteční w řád 2^e a S3 správně vrátí „žádný kořen“ při k=r.
Silnější invariant vytištěný v knize je tedy podmíněn existencí kořene
nebo průchodem prvním testem k<r. Například p=17,u=3 má w^8=−1.
Tuto podmíněnou formulaci zaznamenáváme, **netvrdíme selhání algoritmu
ani samostatnou potvrzenou chybu**: v kontextu hledání existujícího
kořene je přirozený předpoklad čtvercovosti.

Je-li w=1, první invariant dává v²=u. Jinak nechť 2^k je řád w.
Pro k<r položme b=y^(2^(r−k−1)). Tištěná současná aktualizace je

```text
y' = b²,     r' = k,     v' = vb,     w' = wb².
```

Prvek y' má řád 2^k. Oba w a y' mají jejich 2^(k−1)-tou mocninu −1,
takže (w')^(2^(k−1))=1. Rovnost uw'=v'² zůstává platná. Nové r je
menší než staré, což dokazuje ukončení a správnost pro každý vstup.

## 5. Přesná cena S3 a význam průměru

V úspěšné neterminální iteraci stojí nalezení k celkem k čtverců,
výpočet b dalších r−k−1 čtverců a aktualizace vb,b²,wb² tři násobení.
Celkem r+2. V odmítací větvi k=r stačí r čtverců; formulace r+2 je
tedy cena aktualizace. Maximální úspěšná posloupnost úrovní je e,…,2,
takže přesné maximum je (e²+5e−6)/2=binom(e+3,2)−6, menší než v knize.

Průměr zde definujeme přes **rovnoměrné nenulové čtverce u**, při pevném
z řádu 2^e. Počáteční w je rovnoměrný v podgrupě čtverců cyklické grupy
řádu 2^e. Na úrovni r je P(w=1)=2^(1−r) a P(k=j)=2^(j−r),
1≤j<r. Podmíněně na j má w'=wy^(2^(r−j)) opět rovnoměrné rozdělení
na čtvercích podgrupy řádu 2^j: lichý exponent w se posune o 1.
Očekávaný zbývající počet násobení T(r) tedy splňuje

```text
T(1)=0,
T(r)=(r+2)(1−2^(1−r)) + sum_{j=1}^{r−1} 2^(j−r) T(j),
T(r)−T(r−1)=(r+3)/2 − 2^(1−r),
T(e)=(e²+7e−12)/4 + 2^(1−e) < (1/2) binom(e+4,2).
```

To prokazuje knižní průměr v explicitním přirozeném modelu vstupů.
Nelze bez vysvětlení zaměnit tento model za pevné u a náhodné z.
Má-li pevné u^q řád 2^k>1, v druhém modelu vyjde e+2+T(k);
pro k=e−1 a e≥11 to překračuje uvedenou knižní mez. Kniha model
průměrování blíže nerozepisuje; naše ověření používá první model.

S1/S2 mají očekávanou bitovou cenu O((log p)³), S3 cenu
O(e²(log p)²). Podíl ceny algoritmů v praxi se z těchto odhadů
nedá odvodit; vlastní měření není historický benchmark.

## 6. Cipollova metoda: vlastní důkaz

Zvolíme rovnoměrné a∈F_p, až d=a²−u bude nečtverec. Ze součtu
Σχ(a²−u)=−1 a dvou nul plyne právě (p−1)/2 úspěšných a, tedy
očekávaně 2p/(p−1)≤3 pokusy. Pracujeme v kvadratickém rozšíření
F_p[t]/(t²−d); protože d je nečtverec, je to těleso a t^p=−t.
Pro α=a+t platí α^(p+1)=(a+t)(a−t)=u. Proto
β=α^((p+1)/2) splňuje β²=u. Oba kořeny x²−u leží už v F_p,
takže β∈F_p. Mocnění potřebuje O(log p) násobení v rozšíření;
jedno používá konstantně mnoho operací v F_p. Očekávaná bitová cena
je O((log p)³). Tím je uvedená časová možnost dokázána nezávisle
na nedostupném původním článku; prvenství tím nedokazujeme.

## 7. Primární prameny a přesné hranice ověření

- **Tonelli 1891, 344–346:** celé tři strany článku vizuálně přečteny
  z digitalizace Göttingen, PDF a IIIF manifest uloženy. Text předchází
  postupnému určování binárních korekcí: p=α2^s+1, nečtverec g,
  po k korekcích g^(α2^(s−k)E_k)c^(α2^(s−k−1))=1.
  E_k=ε_0+2ε_1+…+2^(k−1)ε_(k−1) a další bit vybírá znaménko ±1.
  Pro k=s−1 je kořen g^(αE_(s−1))c^((α+1)/2). Indukce je tatáž
  redukce řádu jako výše, po jednotlivých bitech. Článek též uvádí
  zvednutí kořene modulo p^λ:
  x_1=x^(p^(λ−1)) c^((p^λ−2p^(λ−1)+1)/2). Jeho čtverec je c
  modulo p^λ, neboť x²≡c modulo p implikuje
  x^(2p^(λ−1))≡c^(p^(λ−1)) modulo p^λ, a zbývající exponent je
  φ(p^λ)+1. Historická atribuce i rozsah 344–346 souhlasí.
  Citace není důkaz obecné praktické převahy Shankse.
- **Pocklington 1917, 57–59:** celé tři strany vizuálně přečteny
  z originálního svazku XIX. První strana uvádí přijetí 22. ledna
  a přednesení 5. února 1917. Vazba obsahuje i svazek XX; rok 1920
  na souborném titulu není datum chyby v Knuthově citaci.
  §2 obsahuje přímé vzorce pro p≡3 (mod4), p≡5 (mod8), §3 pracuje
  s normou v kvadratickém rozšíření. To dokládá relevanci odkazu
  „see also“. Navazující kubické metody v §4–5 byly přečteny pro
  rozsah článku, nikoli nezávisle auditovány.
- **Atkin:** oprava 7. července 1999 konkretizuje International Press
  1998, strany 1–11. Vlastní vzorec je dokázán v §3; původní kapitola
  a historické tvrzení o objevu v devadesátých letech zůstávají
  zdrojově nedokončené. Zdrojem bibliografické navigace je AMS/IP
  Studies in Advanced Mathematics 7, DOI 10.1090/amsip/007.
- **Shanks:** původní příspěvek *Five number-theoretic algorithms*
  (citované strany 58–62) zatím nebyl získán. Sekundární rozdíl
  1972 jako rok konference a 1973 jako rok publikace není novým
  potvrzeným nálezem. Správnost, maximum a vymezený průměr jsou
  plně doloženy vlastním důkazem, historické srovnání výkonu ne.
- **Cipolla:** původní článek 1903, citovaný rozsah 154–163, dosud
  nezískán. Vyhledávací výpis oficiálního akademického rejstříku
  ukazuje začátek 154, nikoli konkurenční sekundární 153. To samo
  není vizuální ověření článku ani jeho konce; atribuce a prvenství
  zůstávají v otevřeném historickém podbloku §4.6.2.

## 8. Nezávislé přesné kontroly a běhy

`verify_sqrt_mod_prime.py` má čtyři oddělené checkpointy; všechny prošly
v session 69983, exit 0, s limitem 180 sekund na blok. Závislosti se
pouze importují, dřívější testy Berlekampa a Sturma se nespouštějí.

| Blok | Přesný rozsah | PID | Čas v sekundách |
|---|---|---:|---:|
| shifts | 37417 polynomických gcd, 567 úplných distribucí pro lichá p<102; proti přímému členství kořenů | 1334161 | 1.959855286 |
| algorithms | 19705 přímých, 9498 Atkinových a 46480 Shanksových výpočtů; 81656 stavů invariantu, p<1000 | 1334166 | 1.180821008 |
| cipolla | 18425 výpočtů v rozšíření, 567 úplných distribucí | 1334168 | 0.111557427 |
| average | 16382 stavů abstraktních cyklických grup, e=2,…,14; přesné maximum a průměr | 1334170 | 0.039592762 |

Celkem 3.291826483 sekund; to je čas kontrol správnosti, nikoli
asymptotický nebo historický benchmark. Testy jsou hotové a nemají
se opakovat bez změny či konkrétní pochybnosti. Výsledky a čtyři logy
jsou v `results/sqrt-mod-prime*`; žádný výpočet nezůstal aktivní.
