# §3.3.1: Kolmogorovův–Smirnovův test

Datum kontroly: 1. listopadu 2026. Podklad: třetí vydání, první tisk
(1997), str. 48–58 a odpovědi na str. 559–562. Obrázky zdroje jsou
`images/vol2-pNNN.png`; číslo strany souboru je tištěná strana + 12.

Tato poznámka uzavírá základní matematiku KS testu a úlohy 5, 7–9, 13,
17, 18, 20 a 23. Výzkumné úlohy 19, 21, 22 uzavírá [samostatný blok](ks-generalizations.md);
historické experimenty jsou vedeny zvlášť. V odpovědi 5 je chybný percentil, evidovaný jako
[V2-C0015](C0015-ks-percentile.md). Samotné dvě hodnoty statistik a závěr
nezamítnout výběr jsou správné.

## 1. Definice a redukce na rovnoměrné rozdělení

Distribuční funkce `F(x) = Pr(X <= x)` udává pravděpodobnost, že náhodná
veličina X nepřekročí x. V této části je F spojitá a pozorování
`X_1,...,X_n` jsou nezávislá se stejnou distribucí F. Empirická distribuční
funkce `F_n(x)` je podíl pozorování nejvýše x. Definujeme

```
D+ = sup_x (F_n(x) - F(x)),   K+ = sqrt(n) D+,
D- = sup_x (F(x) - F_n(x)),   K- = sqrt(n) D-.
```

Supremum je nejmenší horní mez; nemusí být dosaženo. Známá errata
3. února 2005 a 18. června 2024 opravují původní `max` na `sup`, včetně
odpovědí 6 a 13. Není to nový nález. Rozdíl těsně před skokem F_n obecně
nemá své maximum v samotném bodě skoku.

Pro `0 < y < 1` existuje díky spojitosti bod x s `F(x)=y`. Případné celé
intervaly, na kterých F zůstává rovna y, mají pravděpodobnost nula.
Proto `Pr(F(X) <= y)=y`. V krajních bodech se závěr získá limitou.
Tedy `U_j=F(X_j)` jsou nezávislá rovnoměrná čísla v [0,1]. Toto zdůvodnění
nevyžaduje, aby F byla ostře rostoucí. Knižní krátký důkaz na str. 57
je správný jako rovnost pravděpodobností; události se na plochém úseku
mohou lišit o množinu pravděpodobnosti nula.

## 2. Výpočet statistik, úlohy 7, 8, 9, 13, 18

Označme seřazené transformované hodnoty `u_1 <= ... <= u_n`. Po skoku
v bodě u_j je empirická distribuční funkce nejvýše j/n, před skokem
nejméně (j-1)/n. Na otevřených úsecích mezi skoky roste rovnoměrná
referenční funkce a empirická funkce je konstantní. Z toho plyne

```
D+ = max_(1<=j<=n) (j/n - u_j),
D- = max_(1<=j<=n) (u_j - (j-1)/n).                   (KS1)
```

Při shodných pozorováních vybere první maximum poslední index svazku
shodných hodnot, druhé první index. Vzorec tedy zvládá i shody; původní
model má sice shody s pravděpodobností nula, ale vytištěná data jsou
zaokrouhlená. Vně rozsahu pozorování nevznikne větší hodnota. Toto je
přímý důkaz úlohy 13 i vzorce (13) v textu.

**Úloha 7.** Člen j=n v D+ a člen j=1 v D- dokazují nezápornost.
Obě statistiky jsou nejvýše sqrt(n). Výběr samých nul dává K+=sqrt(n),
samých jedniček K-=sqrt(n). Při nezávislém spojitém modelu mají krajní
případy pravděpodobnost nula, ale supremum možných hodnot je stejné.

**Úloha 18.** Zobrazení `u_j -> 1-u_(n+1-j)` zachová objem uspořádaného
simplexu a prohodí D+, D-. Proto mají K+ a K- stejnou distribuci. Nemají
však společně distribuci součinu dvou nezávislých veličin.

**Úloha 8.** Ve druhé vrstvě experimentu je 20 nezávislých statistik,
každá vypočtená z 10 jiných pozorování. Distribuce K_10 slouží jako F;
velikost nového výběru je 20, proto se použije řádek n=20.

**Úloha 9.** Pro n=1 platí `K+ + K- = 1`, což je nejkratší protipříklad
nezávislosti obou statistik. Spojení obou výsledků každého výběru do
jednoho seznamu neopravňuje použít tabulku pro nezávislá pozorování.
Stejný problém nastává u různých testů nad týmž úsekem generátoru.
Knižní tvrzení o nezávislosti testů na disjunktních úsecích je interpretováno
v referenčním modelu nezávislých náhodných vstupů, nikoli jako důkaz
nezávislosti deterministického generátoru.

## 3. Přesná distribuce a úloha 17

Nechť `H_n(s)=Pr(K+ <= s)`. Pro `0<t<n` položme `s=t/sqrt(n)` a
`y_j=n*u_j`. V uspořádaném simplexu
`0<=y_1<=...<=y_n<=n` má společná distribuce konstantní hustotu n!/n^n.
Podmínka K+<=s znamená `y_j>=max(0,j-t)`. Odtud přímo vzniká poměr
integrálů (24). Objem celého simplexu je n^n/n!, protože n! pořadí
souřadnic rozloží krychli kromě hranic nulového objemu.

Pro úplnost definujme polynomy z úlohy 17 rekurentně. Hodnota t je pevná:

```
P_00(x) = 1,
P_nn(x) = x^n/n!,
P_nk(x) = integral_(n-t)^x P_(n-1),k(z) dz,   0<=k<n.
```

To je totéž jako knižní vnořené integrály: prvních k dolních mezí je
nula, další jsou j-t. Orientované integrály dávají polynomy i tehdy,
když některá mez překročí horní mez; pro pravděpodobnost použijeme jen
geometricky přípustné meze v (24).

(a) Posun každé integrační proměnné o t dává dolní meze t pro prvních
k proměnných, j pro ostatní, a konečnou horní mez x+t.

(b) Pro n>=1 indukce integrací dává

```
P_n0(x) = (x+t)^n/n! - (x+t)^(n-1)/(n-1)!.
```

Dolní dosazení z=n-t v primitivní funkci je nula. Případ n=0 zůstává
samostatnou konvencí.

(c) Při přechodu z k-1 na k se změní jediná dolní mez. Rozdíl vnitřních
integrálů je objem orientovaného k-simplexu, `(k-t)^k/k!`. Ve zbývajících
n-k proměnných odečteme k. Dostaneme

```
P_nk(x)-P_n,k-1(x) = (k-t)^k/k! * P_(n-k),0(x-k).
```

(d) Sečtení těchto rozdílů spolu s (b) dává

```
P_nk(x) = (x+t-n) sum_(r=0..k)
          (r-t)^r (x+t-r)^(n-r-1)/(r!(n-r)!).        (KS2)
```

Je-li r=n, nejprve se zkrátí faktor x+t-n; výsledný člen je
`(n-t)^n/n!`. Není správné dosadit do nezkráceného výrazu bod 0/0.
V pravděpodobnostní aplikaci je k=floor(t)<n, takže tento problém nenastává.
Dosazení x=n dává

```
H_n(t/sqrt(n)) = t/n^n * sum_(0<=k<=t)
                C(n,k)(k-t)^k(t+n-k)^(n-k-1).        (KS3)
```

Symbol `C(n,k)` znamená binomický koeficient n!/(k!(n-k)!). Součet přes
všechna k=0,...,n je n^n/t, protože P_nn(n)=n^n/n!. Odečtení zbývající
části dává ekvivalentně

```
H_n(t/sqrt(n)) = 1 - t/n^n * sum_(t<k<=n)
                C(n,k)(k-t)^k(t+n-k)^(n-k-1).        (KS4)
```

Tím je prokázána i ekvivalence knižních (25), (26) bez odkladu na
Abelovu binomickou větu v jiném svazku. Pro t<=0 je H=0, pro t>=n je H=1.
Uvnitř intervalu je distribuce spojitá, takže na ostré či neostré
nerovnosti nezáleží. V (KS3) se odečítají velké členy, zatímco suma v
(KS4) má nezáporné členy; knižní upozornění na numerické rušení platí.
Ani druhý vzorec ovšem není bez ztráty relativní přesnosti, když se
výsledný velmi malý CDF získá odečtením čísla blízkého jedné.

## 4. Tabulka 2 a úloha 5

Program [verify_ks.py](../verify_ks.py) kontroluje všech 105 konečných
kvantilů: pro 15 velikostí n a 7 pravděpodobností řeší H_n(s)=p při
70 desetinných místech. Výsledný kořen leží ve vytištěném intervalu
zaokrouhlení. Druhý přesný vzorec nezávisle kontroluje každou nalezenou
hodnotu CDF; tolerance je 10^-37. Výsledky jsou uloženy po řádcích v
[ks.json](../results/ks.json). Sedm limitních kvantilů y_p z posledního řádku prošlo samostatnou
kontrolou v `results/ks-extensions.json`; celkem tedy 112 číselných
položek tabulky 2. Není to formální intervalový certifikát,
ale přesnost výrazně převyšuje požadované 4–5 desetinných míst.

Samotné distribuční vzorce navíc prošly 265 přesnými racionálními
porovnáními s přímou integrací polynomů pro n=1,...,10. Všech 36
polynomů P_nk pro n=0,...,7 bylo symbolicky porovnáno s vnořenými
integrály. Jde o doplňkové kontroly obecného důkazu v oddílu 3.

Pro data úlohy 5 vychází přesně

```
D+ = 129/500,  K+ = sqrt(20)*129/500 = 1.153811...,
D- = 6/125,    K- = sqrt(20)*6/125   = 0.214662...,
H_20(K+) = 0.94200185499927180511744186897241521...,
H_20(K-) = (6/125)*(131/125)^19
          = 0.11697838135556601251310821352537364....
```

Obě distribuční hodnoty byly navíc ověřeny přímou racionální integrací
20 proměnných, nikoli pouze srovnáním dvou uzavřených součtů. Nesprávný
údaj 86 % a možnosti jeho interpretace rozebírá samostatný nález C0015.

## 5. Asymptotika, úloha 20

Rovnice (15) je jen limitní distribuční funkce
`H_infinity(s)=1-exp(-2s^2)` pro s>=0. Rovnice (27) už obsahuje korekci
řádu n^-1/2. Pro pevné s>0 odpověď 20 správně doplňuje

```
H_n(s) = 1-exp(-2s^2) * [1 - 2s/(3sqrt(n))
         + (2s^2/3 - 4s^4/9)/n + O(n^-3/2)].        (KS5)
```

Primární podklad: H. A. Lauwerier, zpráva TW90/62 (1962),
[PDF CWI](https://ir.cwi.nl/pub/7767/7767D.pdf), uložená v
`sources/lauwerier-smirnov-asymptotic.*`. Je to předchůdce článku z roku
1963 citovaného knihou, nikoli jeho časopisecký otisk. Přečteny str. 1–8;
na původním obrazu str. 1 potvrzen příslušný člen vzorce (1.4).

Vlastní kontrola koeficientů používá parametr p v transformaci
`z=(p/sinh(p))*exp(-p*coth(p))`. Platí

```
-log(e*z) = p^2/2 - p^4/36 + O(p^6),
g = p*exp(p)/sinh(p),
d(log(g))/dp = 1-p/3+p^3/45+O(p^5).
```

Po dosazení p=v/sqrt(n) má integrand u sedlového bodu, po odebrání
faktoru `exp(v^2/2-2sv)`, do potřebného řádu tvar

```
1 - v/(3sqrt(n)) - v^4/(36n)
  + (v^3/45+v^5/108)/n^(3/2) + O(n^-2).
```

Definujme Hermiteovy polynomy `He_m(x)` rovností
`(-1)^m (d/dx)^m exp(-x^2/2)=He_m(x)exp(-x^2/2)`.
Gaussův komplexní integrál převádí v^m na He_m(2s). Stirlingův faktor
navíc násobí výsledek `1+1/(12n)+O(n^-2)`. Proto je koeficient 1/n
`(3-He_4(2s))/36 = 2s^2/3-4s^4/9`, přesně jako v (KS5).
Tato algebraická kontrola je naše; oprávnění deformace kontury a odhady
vzdálených částí integrálu přebíráme ze zdroje, nevydáváme je za nově
samostatně dokázané.

Tentýž výpočet dává další koeficient uvnitř hranaté závorky:

```
[12 He_3(2s) + 5 He_5(2s) - 15 He_1(2s)]/540.
```

Pozor: dostupná zpráva na str. 1 tiskne v tomto vyšším členu He_4 místo
He_5. Nepřebíráme tuto sazbu; přímý součin výše dává lichý polynom stupně
5. Není to chyba Knuthovy vytištěné odpovědi, která tento člen neuvádí.
Přesnou časopiseckou sazbu roku 1963 zde nemáme ověřenu.

Kontrolní výpočty pro n=100,400,1600 a s=1/4,1/2,1,3/2,2 jsou v JSON.
Vyčíslují zbytek po (KS5), násobený n^(3/2). Taková kontrola sama není
důkaz asymptotiky. Uvedený režim je pevné s>0; netvrdíme uniformitu až
k s=0 ani pro libovolně rostoucí s.

Pro kvantil s_p položme `y_p=sqrt(log(1/(1-p))/2)`. Dosazení
`s_p=y_p+c/sqrt(n)+O(1/n)` do (KS5) dává `4y_p*c+2y_p/3=0`, tedy
`c=-1/6`. Tím je odvozen asymptotický řádek tabulky 2.

## 6. Lineární algoritmus, úloha 23

Rozdělme [0,1) do m polouzavřených přihrádek délky 1/m, kde m>=n.
Pro seřazené u_i>u_j ve stejné přihrádce a i>j platí

```
(i/n-u_i) - (j/n-u_j) = (i-j)/n-(u_i-u_j)
                      > 1/n-1/m >= 0.
```

Totéž platí při shodných hodnotách. Maximum pro D+ v přihrádce tedy
určuje její poslední hodnota, maximum pro D- její první hodnota.
Stačí uchovat minimum a_k, maximum b_k a počet c_k v každé přihrádce.
Před zpracováním přihrádky nechť j značí počet prvků v předchozích
přihrádkách. Aktualizace jsou přesně

```
r- = max(r-, a_k-j/n),
j  = j+c_k,
r+ = max(r+, j/n-b_k).
```

Inicializace r+=r-=0 je oprávněná oddílem 2. Celkový čas je O(n+m),
paměť O(m); pro m=n tedy lineární čas. Při plnění přihrádek stačí předem
znát horní odhad m>=n, samotné n se může dopočítat. Kniha výslovně
předpokládá F(X_j)<1, takže index m pro hodnotu 1 není přehlédnutá chyba.

Nahradíme-li všechna u z k-té přihrádky středem `(k+1/2)/m`, změní se
každá souřadnice seřazeného výběru nejvýše o 1/(2m). Maximum výrazů
v (KS1) se také změní nejvýše o tuto hodnotu. Chyba K+ či K- je tedy
nejvýše sqrt(n)/(2m), jak stojí v původní sazbě odpovědi. Tento argument
platí i pro m<n; OCR půlku snadno ztrácí.

Přesná kontrola zahrnuje 3760 neuspořádaných multisouborů z racionálních
mřížek, vždy porovnání (KS1) s přímými hodnotami empirické funkce před
a po skocích, a 25355 porovnání přesných či přibližných přihrádkových
výsledků. Obsahuje nuly, shody i případ n=1. Hodnota 1 v přihrádkové
implementaci není součástí kontraktu; ve vzorci a reflexní kontrole ano.

## 7. Historie běhu a rozsah

První běh, session 22339, úspěšně dokončil 265 racionálních porovnání
a 36 symbolických polynomů. Pak selhal na API: `mpmath.mpf` nepodporuje
operátor `//`. Změna na `math.floor` opravila pouze tuto technickou věc.
Úspěšné části byly uloženy a při obnovení se neopakovaly. Obnovený běh
80988 skončil s kódem 0; logy `ks-first-pass.log` a `ks.log` zachovávají
obě fáze. Dodatečná přímá integrace obou případů úlohy 5 je uvedena
v JSON odděleně.

Všechny relevantní historické řady `all2-prepre`, `all2-pre`, `all2`
a `err2` byly prohledány a změny §3.3.1 zahrnuty. Současný TeX zdroj
`err2.textxt` kontroluje význam OCR. Oprava Smirnovových stran na 179–206
je známá změna z 10. listopadu 2022. Původní slovo „maximum“ není znovu
hlášeno. Novější fyzický dotisk ani prvenství nálezu C0015 nejsou ověřeny.

Doplněk ke zdroji algoritmu 23: autorský odkaz na článek z roku 1977
vrátil HTTP404. V navazujícím článku Gonzalez–Sahni–Franta (1978),
`sources/gonzalez-sahni-franta-1978-ks-approx.pdf`, byly vizuálně přečteny
str. 258–260. Definice algoritmu, přihrádková aproximace a mez chyby
sqrt(n)/(2m) souhlasí. Výsledky starých časových měření se nereprodukovaly.
