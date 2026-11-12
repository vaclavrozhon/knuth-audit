# §4.6.1: Brownovo zkrácení a přesné dělení, úlohy 25/27

Kontrola 4. listopadu 2026. Zadání 438–439 a odpovědi 677–678 byly
čteny v původní sazbě. Algoritmus C a jeho determinantové invarianty
jsou již prokázány v `subresultants.md`; zde se neopakují staré testy.
Úloha21 byla později uzavřena v `polynomial-c-complexity-open.md` (C0202,
výslovný model hustého školského násobení); tento blok řešil25/27.

## 1. Společný faktor vedoucích koeficientů

Označme lc(f) vedoucí koeficient polynomu f a c=gcd(lc(u),lc(v)),
kde u,v jsou vstupní primitivní polynomy. Každý koeficient členu u_j,
j>=3, posloupnosti C je determinant obsahující sloupec, jehož nenulové
prvky jsou pouze lc(u),lc(v). Rozvoj podle tohoto sloupce proto ukazuje,
že c dělí všechny koeficienty u_j. Jde o obecný důkaz první části
úlohy 25 nad libovolným oborem s jednoznačným rozkladem.

V původní posloupnosti pišme n_i=deg(u_i), delta_i=n_i-n_(i+1),
g_1=h_1=1, g_i=lc(u_i) pro i>=2. Posloupnost h splňuje
h_(i+1)=h_i^(1-delta_i)g_(i+1)^delta_i.

Předpokládejme nyní **n_1>n_2**. Brownova úprava nastaví počáteční
g=c,h=0. Nula h označuje dosud neprovedenou první normalizaci.
V první C3 se použije u_3/c místo u_3, g_2=lc(u_2) zůstane beze změny
a h_2 se nahradí h_2/c=lc(u_2)^delta_1/c. Tento podíl je v S,
protože delta_1>=1 a c|lc(u_2).

Pro další kroky platí

```
U_1=u_1, U_2=u_2, U_i=u_i/c pro i>=3;
G_2=g_2, G_i=g_i/c pro i>=3;
H_i=h_i/c pro i>=2.
```

To ověříme homogenitou pseudodělení. Ve druhém kroku se mění jen
dělitel: prem(u_2,u_3/c)=prem(u_2,u_3)/c^(delta_2+1), zatímco
normalizační faktor se zmenší c^delta_2. Později se oba polynomy
zmenší c, takže pseudoremainder se zmenší c^(delta_i+2), kdežto
normalizace c^(delta_i+1). V obou případech vznikne u_(i+2)/c.
Rekurence h zachová H_(i+1)=h_(i+1)/c.

Integrita H_i pro i>=3 plyne z jeho determinantové reprezentace:
ta má opět sloupec obsahující pouze původní dva vedoucí koeficienty
a nuly. Vstupní n_1>n_2 ošetřuje i H_2. Tím se nepředpokládá
dělitelnost, kterou teprve potřebujeme dokázat. Nové gcd zůstává stejné
po odebrání obsahu posledního nenulového polynomu. Zisk jedné mocniny
vedoucího koeficientu společného faktoru v normálním případě (28)
je správný: exponent 2j-4 se zmenší na 2j-5.

## 2. C0199: stejné počáteční stupně

**Confirmed, s přesně vymezeným dopadem.** Algoritmus C připouští
stejné stupně; při delta_1=0 Brownova uvedená inicializace požaduje
h=1/c. To obecně není prvek původního oboru S. Například nad Z:

```
u=2x^3+x+1,  v=2x^3+x^2+1,  c=2,
2u=2v+(-2x^2+2x).
```

Zbytek je nenulový a nekonstantní, takže C3 skutečně proběhne:
nové v=-x^2+x, ale nové h=2^0/2=1/2. Oba vstupy jsou primitivní.
Úprava tedy v této větvi přestává být algoritmem nad původním UFD.
Není tvrzeno, že při povolení racionální aritmetiky vyjde špatný gcd.

Oprava: uvést pro optimalizaci předpoklad deg(u)>deg(v), nebo při
stejných stupních nejprve provést jeden obvyklý krok E. Je-li jeho
zbytek nulový či konstantní, odpověď je hotova. Jinak vezmeme jeho
primitivní část a s dvojicí (v,pp(r)) Brownovu úpravu znovu inicializujeme.
Oddělený společný obsah původních vstupů ponecháme; nové primitivní
polynomy mají přísně různé stupně a stejný primitivní gcd.

150 přesných dvojic s přísně různými stupni, primitivními vstupy
a c>=2 potvrdilo celé škálované posloupnosti i integritu H.
Protipříklad se stejnými stupni je zvláštní kontrolou, nikoli timeout.

## 3. Úloha 27: známe-li nulový zbytek

Předpoklad je skutečná přesná dělitelnost u=vq, v!=0. Nechť
d=deg(q)=deg(u)-deg(v). Pokud v má nejnižší nenulový člen x^t,
odstraníme x^t z obou vstupů. Potom v_0!=0; symbol n v tomto oddílu
označuje stupeň takto zkráceného v. Z porovnání nízkých koeficientů
dostáváme trojúhelníkovou soustavu

```
q_0=u_0/v_0,
q_k=(u_k - sum_(i=1)^min(n,k) v_i q_(k-i))/v_0, 0<=k<=d.
```

Nad tělesem je v_0 invertibilní. Nad UFD jsou všechna tato skalární
dělení přesná právě díky příslibu u=vq. Vysoké koeficienty u nemusíme
číst pro ověřování zbytku: již víme, že zbytek bude nula. Bez tohoto
příslibu by konečný součin u=vq musel být ověřen zvlášť.

Počet součinů je sum_(k=0)^d min(n,k), tedy d(d+1)/2 pro n>=d.
Obvyklé úplné dělení používá n(d+1) součinů. Vedle toho zůstává
d+1 skalárních dělení. Odkaz na součin mocninných řad 4.7-(3) je správný.

Lze současně určit K nejnižších koeficientů q tímto postupem a zbytek
od nejvyššího pomocí obvyklého dělení. Tyto části se neovlivňují:
v koeficientu u_k pro k<K se neobjeví žádné q_j s j>=K, zatímco
v koeficientu u_(n+k) pro k>=K se neobjeví q_j s j<K.
Celkový počet součinů je

```
sum_(k=0)^(K-1) min(n,k) + sum_(k=0)^(d-K) min(n,k).
```

Rostoucí přírůstky obou součtů ukazují, že optimum je uprostřed:
K=floor((d+2)/2). Pro n>=d se hlavní kvadratický člen zmenší
z přibližně d^2/2 na d^2/4. Nejde o tvrzení konstantního zrychlení
ve všech poměrech stupňů; při malém n a velkém d je zisk menší.

180 konstruovaných přesných součinů s různými nulovými počátečními
koeficienty, stupni i vedoucími/konstantními koeficienty ověřilo oba
směry a přesné počty součinů proti předem zvolenému q.

## 4. Dovětek o Fourierově transformaci

Fourierova transformace polynomu vyhodnocuje jeho koeficientový vektor
v pravidelně rozmístěných bodech; inverzní transformace z těchto hodnot
rekonstruuje koeficienty. Zvolíme délku L>deg(u), primitivní L-tou
odmocninu jednotky omega a body alpha*omega^j. Je-li v v každém bodě
nenulové, hodnoty u/v jsou přesně hodnoty q a inverzní transformace
vrátí q bez cyklického překrytí koeficientů.

Nenulovost jmenovatelů je nutná: v=x-1 má při nepootočené transformaci
v(1)=0. Nad nekonečným tělesem lze vybrat alpha mimo konečnou množinu
zakázaných hodnot; v dostatečně velkém konečném tělese obdobně.
Zde byla metoda ověřena přesně nad F_257, pro L=16 a 60 dvojic;
test obsahuje v=x-1 a výběr pootočení alpha s nenulovými jmenovateli.
Nebyla tím ověřována zaokrouhlovací chyba plovoucí transformace.
Pro skutečnou numerickou realizaci se musí použít kontrola přesnosti
a případně konečné ověření součinu; §4.6.4–57 zůstává v pozdějším auditu.

Alternativní rychlá konstrukce nad tělesem počítá q=u/v modulo x^(d+1)
pomocí inverze v mocninných řadách. Newtonův krok
b -> b(2-vb) zdvojnásobí počet správných koeficientů, protože
1-vb(2-vb)=(1-vb)^2. Začneme b=1/v_0. Při obvyklém předpokladu
pravidelného růstu ceny M(d) násobení polynomů je celková cena O(M(d))
operací v tělese. To dokazuje existenci rychlého přesného dělení;
nejde o převzetí dosud nekontrolované analýzy plovoucí FFT.

## 5. Evidence

`verify_polynomial_c_extensions.py`, tři checkpointy v
`results/polynomial-c-extensions.json`: 150+1 případů Brownovy úpravy,
180 přesných dělení,60 konečných Fourierových transformací.
PID1324149,limit120s,exit0,celkem0.079756s. Staré kontroly C neopakovány.

Všechny relevantní historické i aktuální vrstvy errat prohledány,
protokol `sources/polynomial-c-extensions-errata.txt`; shodná oprava
pro C0199 nenalezena. Nejnovější fyzický dotisk a prvenství neověřeny.
Návrh hlášení pouze uložen, neodeslán. V době tohoto bloku zůstávala21 partial,
protože důkaz obecné časové meze ani definitivní protipříklad v jejím
zamýšleném výpočetním modelu nebyl hotov. Pozdější uzavření a omezení
modelu jsou v samostatné poznámce C0202.
