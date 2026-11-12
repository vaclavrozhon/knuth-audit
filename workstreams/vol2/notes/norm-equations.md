# Kvadratická rovnice: §4.5.4-45

> Sekvenční doplnění6.11.2026: celá45 je nyní partial. Vlastní algebraická konstrukce je uzavřená s podmíněným ERH časem; nepodmíněný algoritmický důkaz citovaného zlepšení není zde rozpracovaný.

Audit zadání417 a odpovědi670–671, první dotisk třetího vydání (1997).
Všechny tři původní stránky byly vizuálně přečteny 3. listopadu2026.
Úloha je uzavřena v níže vymezeném rozsahu: vlastní algebraický důkaz,
opravená konstrukce a přesné konečné kontroly. Analytické věty o prvočíslech
za předpokladu ERH jsou výslovně externí; nepodmíněný algoritmus z citovaného
článku Adlemana, Estese a McCurleyho zde znovu nedokazujeme.

Zadání hledá jednu dvojici x,y s x²−a y²=b modulo liché kladné n,
kde gcd(ab,n)=1. Výraz **norma** zde znamená N_a(x,y)=x²−a y²;
může být záporný. Naproti tomu čtverec eukleidovské délky v oddílu3
je vždy nezáporný. **Jednotka modulo n** je číslo nesoudělné s n,
tedy číslo s násobnou inverzí. Pro n=1 je úloha triviální.

## 1. Existence, násobení a počet řešení

Pro liché prvočíslo p mají množiny {x²} a {b+a y²} obě (p+1)/2 prvků.
Proto se protínají a řešení existuje. Je-li nalezeno modulo p^e, při
nahrazení (x,y) dvojicí (x+c p^e,y+d p^e) stačí vyřešit jednu lineární
rovnici 2x c−2a y d=(b−N_a(x,y))/p^e modulo p. Aspoň jeden koeficient
je nenulový: jinak by p dělilo b. Každé řešení má právě p pokračování
modulo p^(e+1). Čínská věta o zbytcích spojí řešení pro různé prvočinitele.
To dokazuje Fact1, aniž by algoritmus musel znát rozklad n.

Součin dvojic definujme

```
(x1,y1) * (x2,y2) = (x1*x2+a*y1*y2, x1*y2+x2*y1).       (1)
```

Přímým roznásobením se smíšené členy zruší a norma součinu je součin
norem. Jednotková dvojice je (1,0). Má-li dvojice normu b nesoudělnou
s n, její inverze je b^(-1)(x,−y). Násobení pevnou dvojicí normy b tedy
bijektivně převádí řešení normy1 na řešení normy b. To je Fact2 včetně
jednoznačnosti inverzního zobrazení.

**C0169:** oba tištěné výskyty (417 v nápovědě a670 ve Fact2) mají
v první souřadnici chybně minus. Pro a=2 a obě dvojice (1,1) je součin
norem1, ale tištěná dvojice (−1,2) má normu−7. Správná (3,2) má normu1.
Příklad selhává i modulo5, kde jsou všechny vstupní normy jednotky.
Přímo pro Fact2 lze vzít modulo5 dvojice (1,1) normy4 a (2,2) normy1;
tištěný obraz (3,4) má normu2, nikoli4.

Pro kontrolu počtů označme chi_p(a)=1, je-li a nenulový čtverec modulo p,
a chi_p(a)=−1 jinak. Je-li chi=1, součin (x−r y)(x+r y)=b s r²=a
dává p−1 řešení. Je-li chi=−1, jediná dvojice nulové normy je (0,0).
Zbývajících p²−1 dvojic se podle dokázané bijekce dělí stejně mezi
p−1 nenulových norem; každá tedy má p+1 řešení. Zvedání a čínská věta dají

```
#{(x,y) modulo n : N_a(x,y)=b}
    = product over p^e || n of p^(e−1) * (p−chi_p(a)).      (2)
```

Zápis p^e || n znamená, že p^e dělí n, ale p^(e+1) už ne. Vzorec (2)
platí pro jednotky a,b a nevyžaduje žádnou neprokázanou hypotézu.

**C0172:** závorka ve Fact1 na670 uvádí nemožnost x²±y²=3 modulo8.
Pro minus je však x=2,y=1 přesným řešením. Stačí nahradit ± znaménkem+:
čtverce modulo8 jsou0,1,4 a žádný součet dvou není3. Omezení na liché
n tak má správný důvod, jen tištěný příklad zbytečně zahrnuje chybnou větev.

## 2. Náhodný výběr: C0171

Fact2 počítá všechny dvojice z celého okruhu zbytků. První věta671 však
vybírá u,v pouze z1,…,n−1. Následné tvrzení o rovnoměrnosti proto neplyne.
Pro n=7,a=3,b=1 mají hodnoty s=u²−3v² následující četnosti:

| s | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| 1≤u,v≤6 | 4 | 4 | 8 | 4 | 8 | 8 |
| 0≤u,v≤6 | 8 | 8 | 8 | 8 | 8 | 8 |

V prvním řádku nevzniká nulová norma a všechny gcd předtesty procházejí:
odchylku tedy nevysvětluje podmínění na d=1. U druhého řádku je navíc
jediná dvojice normy0, totiž (0,0).

Vlastní oprava vybírá u,v nezávisle ze všech n zbytků a nejprve zpracuje
gcd(w,n), kde w=N_a(u,v). Při jednotkovém w pokračuje bez dalšího odmítání
podle v. Podmíněně na tuto větev je w podle (2) přesně rovnoměrné mezi
jednotkami; násobení jednotkou b zachová rovnoměrnost s=bw mod n.
Nestačí pouze změnit dolní mez v tištěném textu a ponechat bez úprav
větev gcd(v,n)>1: nově povolené v=0 by v ní vyžadovalo zvláštní zacházení.
Nález popírá přesnou distribuční větu, nikoli sám o sobě účinnost metody.

## 3. Krátký vektor a zmenšení koeficientu: Fact3

Nechť s>0, z²=a+ms a a,m jsou nenulová celá čísla. Položme A=|a|.
Mříž je množina vektorů (zu+mv,sqrt(A)u), u,v celá; plocha její základní
buňky je |m|sqrt(A). Čtverec délky je Q(u,v)=(zu+mv)²+A u².

Dvourozměrná Gaussova redukce najde bázi B,C s ||B||≤||C|| a
2|B·C|≤||B||². B je nejkratší nenulový vektor: pro celočíselný násobek
B je to okamžité; pro koeficient C rovný±1 je nejbližší projekční posun
0, případně při shodě±1. Pro koeficient C absolutně alespoň2 už samotná
kolmá složka dává čtverec délky nejméně3||B||². Dále

```
det(B,C)^2 = ||B||² ||C||² − (B·C)² ≥ 3||B||^4/4,
min Q ≤ |m| sqrt(4A/3).                                    (3)
```

Efektivní dvourozměrnou redukci používáme jako standardní algoritmický
výsledek, stejně jako kniha odkazující na §3.3.4. Její skalární součiny
jsou celá čísla; odmocninu A není třeba numericky aproximovat.

**C0170:** v druhé nerovnosti Fact3 na670 chybí faktor |m|. Pro
a=2,s=17,z=6 je m=2. Minimum (6u+2v)²+2u² je2, dosažené u=1,v=−3.
Je-li u nenulové, hodnota je alespoň2; při u=0 je nenulová hodnota
alespoň4. Tištěná mez sqrt(8/3) je menší než2, tedy neplatí.

Pro nejkratší dvojici definujme w=zu+mv a

```
t = (w²−a u²)/m = s u²+2zuv+mv²,
alpha = (s u+zv, v).
```

Číslo t je celé. Z (3) plyne |t|≤sqrt(4A/3). Navíc přímá identita dává
N_a(alpha)=st a alpha není nulová, protože s≠0 a (u,v)≠(0,0).
Dvojice m*alpha tedy splňuje přesně požadované N_a(m*alpha)=m²st.
Tato volba je součinem (z,1)*(w,−u) podle (1) a předem vykrátí m.
Tím je objasněno i znaménko druhé složky, které při neurčité volbě
součinu mohlo zbytečně vést k nulové dvojici.

Je-li m=0, máme a=z² a můžeme rovnou použít (x,y)=(z,1), t=0.
Je-li a=0, lze pro samotné tvrzení Fact3 rovnou volit (x,y)=(0,1), t=0.
Tyto degenerace nepotřebují mřížovou redukci. V rekurzi je a vždy jednotka.

Nejkratší (u,v) je primitivní, tj. gcd(u,v)=1; jinak by společným dělením
vznikl kratší vektor. Pro s nesoudělné s n je proto gcd(alpha_x,alpha_y,n)=1.
To níže umožní bezpečně zpracovat t=0.

## 4. Základní případy a rekurze

Pro a=1 stačí x=(b+1)/2, y=(b−1)/2, kde půlení znamená násobení inverzí2
modulo n. Známe-li r²=a s r jednotkou, nahradíme y hodnotou y/r.
Pro a=−1 zvolíme prvočíslo p=b modulo n a p=1 modulo4. Tyto kongruence
určují třídu nesoudělnou s4n. Vyjádření p jako součtu dvou čtverců,
jaké používá §3.3.4-11, dává hledané řešení modulo n. Existence prvočísla
je Dirichletova věta; rychlé náhodné nalezení v dostatečně dlouhém úseku
je odlišný analytický vstup, viz oddíl6.

Pro obecné a nejprve zvolíme zástupce |a|≤n/2. V jednotkové větvi výběru
z oddílu2 najdeme s=bw mod n a kořen z²=a modulo s; kořen vždy přímo
ověříme. U prvočísel s s příznivým kvadratickým charakterem ho lze najít
náhodným polynomiálním algoritmem; neúspěšné pokusy opakujeme. s=1 lze
vyřídit okamžitě: inverze dvojice (u,v) už má normu b.

Získáme m=(z²−a)/s. Vlastní dělitel gcd(m,n) rozdělí problém; při n|m
je z kořenem a modulo n. Jinak oddíl3 dává alpha normy st. Pro t=0
je buď alpha_y jednotka a alpha_x/alpha_y je kořenem a, nebo gcd(alpha_y,n)
poskytne vlastní dělitel. Případ n|alpha_y je vyloučen primitivností alpha.

Pro nenulové t nejprve prověříme gcd(t,n). Je-li větší než1, je vlastní,
protože |t|<|a|≤n/2. Jinak lze rekurzivně řešit X²−tY²=a modulo n.
Je-li gcd(Y,n) vlastní dělitel, znovu rozdělíme problém. Je-li n|Y,
už známe kořen X²=a. V jednotkové větvi položme beta=(X/Y,1/Y).
Její norma vůči původnímu a je t. Proto

```
delta = alpha * beta^(-1)     has norm s,
answer = delta * (u,v)^(-1)   has norm s/w = b.              (4)
```

Inverze i násobení jsou explicitní v oddílu1. Kniha jejich závěrečné
provedení pouze naznačuje; (4) dokládá správnost včetně všech jmenovatelů.
Mez |t|≤sqrt(4|a|/3) dává O(log log n) zmenšení koeficientu až k±1:
po k krocích je log|a_k|≤2^(−k)log|a_0|+log(4/3).
Jakmile |a_k|<2, je celočíselný nenulový koeficient±1.

## 5. Co přesně znamená rozdělit n

Dělitel d a n/d nemusí být nesoudělné. Z n postupně odebíráme gcd(zbytek,d),
dokud není1. Získáme n=M R, kde gcd(M,R)=1, d|M a M|d^L pro nějaké
L≤log_2 n. Potřebujeme pouze řešení modulo d a případně modulo R.

Řešení modulo q zdvojíme na modulo q² pomocí rovnice

```
2x c−2a y d' = (b−N_a(x,y))/q modulo q.
```

Koeficienty mají společný největší dělitel nesoudělný s q, protože b je
jednotka. Rozšířený Eukleidův algoritmus tedy poskytne c,d' i tehdy,
když ani jeden koeficient samostatně nemá inverzi modulo q. Opakujeme
pro q=d,d²,d^4,…, až M|q; redukujeme výsledek modulo M a spojíme s R.
Bitová délka posledního q je O((log n)²), tedy zůstává polynomiální.
Neznáme a nepotřebujeme úplné rozklady M,R. Rekurzivní podmoduly jsou
menší, jejich součin dR≤n; počet skutečných rozdělení je polynomiálně omezený.

Tento detail je doplněním zkráceného odkazu na Fact1, nikoli samostatně
hlášenou chybou. Stejně tak gcd(t,n) je zde výslovnou vstupní kontrolou
před rekurzí, jejíž předpoklady by jinak nebyly zaručeny.

## 6. Čas, primární prameny a limity

ERH zde znamená rozšířenou Riemannovu hypotézu pro Dirichletovy L-funkce.
Používáme její standardní důsledky o počtech prvočísel: dostatečně mnoho
prvočísel s≤n má a jako kvadratický zbytek, a dostatečně mnoho prvočísel
v úseku velikosti O(n³) leží v předepsané jednotkové třídě modulo4n.
Tyto analytické odhady zde znovu nedokazujeme. Podmíněně rovnoměrné s
z oddílu2 pak potřebuje O(log n) pokusů; náklady získání jednotkové normy
jsou také polynomiální v log n. Z (2) je pravděpodobnost této větve
product_p (1−1/p)(1−chi_p(a)/p), alespoň (phi(n)/n)². Zde phi(n)
je počet jednotek. Má-li n k různých prvočinitelů, j-tý z nich je
aspoň j+1, takže phi(n)/n≥1/(k+1)≥1/(1+log_2 n). Už tento hrubý
elementární odhad stačí pro polynomiální čas.

Polynomiální prvočíselný test (například dříve auditovaný AKS), modulární
odmocniny a redukce ve dvou rozměrech dokončují podmíněný polynomiální
algoritmus. Konečná kontrolní implementace níže záměrně používá přesné
malé orákulum: zkušební dělení a úplný soupis odmocnin. Její měřený čas
není experimentálním důkazem asymptotického tvrzení.

[McCurleyho autorská kopie](https://www.mccurley.org/papers/oddsends.pdf),
*Odds and Ends from Cryptology and Computational Number Theory* (1990),
strany152–154 byly přečteny celé vizuálně. Dokládají podmíněný výsledek,
náhodné prvočíslo v progresi a sestup koeficientu; používají jinou variantu
sestupu než knižní Fact3. Strana152 také výslovně potvrzuje nepodmíněné
zlepšení Adlemana, Estese a McCurleyho. Originál jejich článku1987 nebyl
z AMS dostupný (403), takže celý jeho důkaz netvrdíme jako přečtený.

[Autorský záznam Pollard–Schnorr](https://www.researchgate.net/publication/262234058_An_efficient_solution_of_the_congruencex2_ky2_mpmodn)
potvrzuje čas O((log n)² |log log |a||) aritmetických kroků za GRH a citaci
IT-33 (1987),702–709. Čten byl abstrakt a metadata; PDF nástroj rozpoznal,
ale přenos neposkytl obrázky a místní stažení vrátilo403. Není to vizuálně
přečtený originál. Bibliografie nepodmíněného výsledku odpovídá vydavatelským
metadatům DOI10.1090/S0025-5718-1987-0866095-8. Historická priorita ani
novější fyzický dotisk knihy nejsou ověřeny.

## 7. Reprodukovatelné kontroly a errata

`verify_norm_equations.py` dokončil tři samostatně ukládané bloky:

- 5625 normových identit;31872 vláken (tj. množin dvojic se stejnou normou)
  nad všemi lichými moduly3…65;1883016 dvojic a1562576 kontrol bijekce.
- 2315 mříží s přesnými bázemi;5712 nezávisle probraných kandidátů
  v uzavřené kouli potvrzuje minimum, meze i identitu pro st.
- Všech62448 přípustných trojic a,b,n s lichým3≤n≤81; navíc18 vynucených
  rozdělení s překrývajícími se prvočiniteli.14573 rozdělení,5303 zvedání
  a10804 spojení čínskou větou. Maximální hloubka volání5.

Celkem13.443308884s, všechny bloky passed; PID1303343, obal1303342,
relace64048, limit180s, exit0. Výsledky v `results/norm-equations.json`
a logu. Úspěšné bloky nebyly opakovány. Testy ověřují opravený algoritmus;
neprohlašují chybný tištěný pseudopostup za úspěšný.

Dne3.11.2026 prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` i aktuální
TeX podle417/670/671,45, Pollard, Schnorr, uniform, modulo8 a formulací
pomocných tvrzení. Oprava6.2.1998 na670 opravuje pouze y_2 na y² ve Fact2;
byla ověřena vizuálně na straně42 souboru all2-prepre. Neopravuje znaménko
součinu, faktor|m|, distribuci ani ± v příkladu modulo8. Čtyři samostatné
nálezy C0169–C0172 jsou potvrzené vůči dostupnému skenu a řadám errat;
priorita se netvrdí a žádné hlášení nebylo odesláno.
