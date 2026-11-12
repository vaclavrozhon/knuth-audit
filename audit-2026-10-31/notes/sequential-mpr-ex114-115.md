# MPR 114–115: úplná kontrola polynomické meze a mřížky

Kontrola 7. listopadu 2026; D212–D213, známá oprava E134. Zadání na
str. 23 / file 43, celé odpovědi na str. 388 / file 408. Původní PDF,
autorův Pre-Fascicle 5A z 11. 9. 2019 (str. 23 a 45 / file 29 a 51)
a původní sazba známé opravy byly zobrazeny. Fyzický výtisk se netvrdí.
Žádný nový nález, kandidát ani matematický běh. Staré běhy se neopakovaly.

## 114: předpoklady a základní redukce

Pracujeme nad libovolným tělesem K, s n ≥ 1 a nezápornými celými d_j.
Množiny S_j jsou konečné a mají s_j > d_j prvků; právě to je zde doména
rovnoměrného výběru a tištěných konečných podílů. Označme D = Σ d_j.
Koeficient monomu x^d je nenulový a celkový stupeň f je nejvýše D,
tedy ve skutečnosti přesně D. Nevyžaduje se charakteristika nula.

Nejprve s_j = d_j + 1. Monický polynom
g_j(x_j) = Π_{s∈S_j}(x_j−s) má stupeň d_j+1. V monomu x^α s
α_j ≥ d_j+1 nahradíme faktor x_j^{d_j+1} polynomem
x_j^{d_j+1}−g_j(x_j). Každý vzniklý monom má menší j-tý exponent
a přísně menší celkový stupeň; ostatní exponenty se nezvětší.
Hodnota na součinu S_j se nezmění, protože g_j tam mizí.

Ukončení lze formalizovat postupným dělením v jednotlivých proměnných,
vždy od nejvyššího exponentu dolů. Pro pevné j už pozdější kroky
nemohou znovu vytvořit vyšší exponent; pozdější jiné proměnné jeho
exponent nezvětšují. Výsledný zbytek h má stupeň v x_j nejvýše d_j
pro všechna j a na celé mřížce se rovná f.

Podstatný nenulový koeficient se neztratí: monom x^d se nikdy
neredukuje. Každý nový monom vzniklý redukcí má celkový stupeň < D,
protože původní i všechny průběžné monomy mají stupeň ≤ D. Žádný
z nich tedy nemůže přispět ke koeficientu x^d. Ten zůstává původní
nenulovou hodnotou a h není nulový polynom.

Redukce je konečná i jako explicitní postup. S hustou tabulkou
M = binom(D+n,n) možných monomů lze pro každou proměnnou zpracovat
každý monom nejvýše jednou v klesajícím j-tém exponentu; jedno
odstranění změní nejvýše d_j+1 koeficientů. Stačí tedy
O(M Σ_j(d_j+1)) operací tělesa po vytvoření g_j, které stojí
O(Σ_j(d_j+1)^2) operací násobením lineárních faktorů. Paměť pro
koeficienty je O(M+D+n). Nejde o tvrzení o bitové složitosti nebo
o efektivním vyhledávání bodu z oracle reprezentace f.

## Přesný rozsah odkazu na svazek 2

Bylo přímo zobrazeno zadání 4.6.1–16 na str. 436 / DjVu file 448
a příslušný základní důkaz na str. 674–675 / file 686–687.
Pozor: textový extrakt je v těchto místech o jednu file stránku
posunutý. Uložené obrázky mají názvy podle skutečného tištěného čísla.
Nepřebírá se celé okolí úlohy ani její dodatečné poznámky.

Potřebná věta má tento úplný důkaz. Nenulový univariační polynom
stupně ≤ d má nejvýše d různých kořenů: každý další kořen dává
další odlišný lineární faktor podle věty o zbytku a postupného dělení.
Pro n proměnných napišme
h = Σ_{k=0}^{d_1} x_1^k h_k(x_2,…,x_n) a vyberme nenulové h_k.
Indukcí je alespoň Π_{j=2}^n(s_j−d_j) n-tic bez první souřadnice,
na nichž h_k není nula. Na každé takové n-tici je výsledný
univariační polynom nenulový, takže má alespoň s_1−d_1 nekořenů.
Proto má h alespoň Π_j(s_j−d_j) nekořenů. To je přesně doplněk
tištěné horní meze na počet kořenů. V základním případě s_j=d_j+1
je tedy alespoň jeden nekořen; shoda hodnot h a f dává totéž pro f.
Tím jsou doloženy všechny důkazové předpoklady odkazu.

## Obecné velikosti a známá oprava

Položme R = Σ_j(s_j−d_j−1) ≥ 0. Předpokládejme pro spor, že
počet nekořenů q je nejvýše R. Dokud q>0 a R>0, zvolme jeden
nekořen a libovolný index j s s_j>d_j+1; odeberme ze S_j jeho
j-tou souřadnici. Zmizí alespoň tento nekořen, R klesne o 1,
všechny velikosti zůstanou alespoň d_j+1 a invariant q≤R trvá.
Pokud q klesne na nulu dříve, zbývající přebytky můžeme libovolně
odstranit. Nejpozději po původních R krocích získáme základní
mřížku s velikostmi d_j+1 a s nulou nekořenů, což odporuje
právě dokázanému případu. Proto q≥R+1.

Nezávislý rovnoměrný výběr dává každému bodu pravděpodobnost
1/Π_j s_j, a tedy přesně požadovanou mez (R+1)/Π_j s_j.
Čitatel je kladný a nepřesahuje jmenovatel, protože
Π_j s_j = Π_j(1+(s_j−1)) ≥ 1+Σ_j(s_j−1) ≥ R+1.
Případ R=0 již pokrývá základní důkaz. Pro n=1 jde o běžnou
mez s_1−d_1 nekořenů; pro všechna d_j=0 je f nenulová konstanta.
Nulové jednotlivé d_j ani jednoprvkové S_j tedy nezpůsobují výjimku.

Tento postup je už známá oprava Fascicle 5, str. 200, řádky 7–8
odpovědi 114, z 5. 1. 2022. Starý PS uvádí formulaci o podmnožinách,
svazek 4B už výslovně používá postupné odebírání. Originál all4f5,
file 10, a TeX řádky 781–785 souhlasí. Evidence E134 zohledňuje
historickou opravu; není to nový nález, karta ani chybová lokace.

## Celá poznámka o silnější mezi

Předpoklad poznámky je n≥2, d_j=d a
c = ceil(d/(n−1)), s=d+1+c, s_j≥s. Výraz s má pro n=1
přirozeně vyloučený jmenovatel; tento případ byl už samostatně
vyřešen univariační mezí a nevytváří podezření na chybu.

Nejprve doložíme přenos meze z menších mřížek zpět na původní
pravděpodobnost. Vyberme nezávisle a rovnoměrně s-prvkové
T_j⊆S_j. Na každé jejich součinové mřížce má f podíl nekořenů
alespoň B=(ns−n(d+1)+1)/s^n=(nc+1)/s^n. Každý původní bod
je do náhodné podmřížky zařazen s pravděpodobností Π_j(s/s_j).
Očekávaný podíl nekořenů v T_1×…×T_n je proto
q Π_j(s/s_j)/s^n = q/Π_j s_j, tedy původní pravděpodobnost.
Jelikož každý podíl je alespoň B, je i původní pravděpodobnost ≥B.
Samotná existence nekořenu v jedné malé mřížce by tento krok
nenahrazovala; zde je přenos doložen přesně průměrováním.

Zbývá ověřit tištěné tvrzení, že pravá strana se zlepší při
zmenšování velikostí na s. Pro pevné ostatní velikosti lze původní
pravou stranu psát jako (1+A/s_j)/Π_{i≠j}s_i, kde
A=Σ_{i≠j}s_i−n(d+1)+1. Dokud všechny ostatní velikosti jsou ≥s,
platí A≥(n−1)s−n(d+1)+1=(n−1)c−d≥0. Zmenšení s_j na s
tedy pravou stranu nezmenší. Postupným provedením pro všechna j
dostaneme přesně B. Rovnost je přípustná: slovo „increase“ zde
označuje zlepšení dolní meze, nikoli tvrzení ostré nerovnosti
v každém degenerovaném případě. Při d=0 je s=1 a B=1, správně.

Noga Alon, autorův primární PDF, Theorem 1.2 a Lemma 2.1 včetně
důkazu na jeho str. 2–3, byly přímo přečteny i zobrazeny. Autorův
seznam publikací potvrzuje CPC 8 (1999), 7–29. Zdejší argument
včetně počtu nekořenů a průměrování je celý výše, není jen citací.
Jedna výslovná bibliografická výjimka: původní §6.2 a §6.3 knihy
Bollobáse z roku 1978 a jejich přesný další asymptotický obsah nebyly
rychle dostupné. Tento odkaz je vynechán; žádná konkrétní mez z něj
není použita ani prohlášena za ověřenou.

## 115: všechny přímkové faktory a koeficient

Nechť p,q,r jsou nezáporná celá čísla a
m=p+2 floor(r/2)+1, n=q+2 ceil(r/2)+1. Souřadnice jsou jako
v odpovědi řádek x a sloupec y. Vodorovné přímky mají rovnice
x=a_j, svislé y=b_j; obě diagonální rodiny lze zapsat
x+y+c_j=0 a x−y+d_j=0. Pořadí označení sklonů po výměně
řádkové a kartézské osy nehraje roli, obě rodiny mají r členů.
Pracujeme nad R, takže konstanty mohou být libovolná reálná čísla
a žádné nenulové celé binomické číslo nezanikne charakteristikou.

Vytvořme polynom přesně z odpovědi jako součin všech těchto
lineárních faktorů. Bod je pokryt právě tehdy, když aspoň jeden
faktor mizí, tedy právě tehdy, když f(x,y)=0. To platí i při
opakovaných přímkách a při přímkách mimo mřížku.

Nejvyšší homogenní složka f je
x^p y^q (x+y)^r(x−y)^r = x^p y^q(x^2−y^2)^r.
Je nenulová, má stupeň p+q+2r=m+n−2 a žádný výběr konstantního
členu nemůže přispět k tomuto stupni. Rozvoj posledního faktoru
je Σ_{k=0}^r binom(r,k) x^{2k} (−1)^{r−k} y^{2(r−k)}.
Pro x^{m−1}y^{n−1} je jediná možnost k=floor(r/2); přesný
koeficient je proto (−1)^{ceil(r/2)} binom(r,floor(r/2)),
což je nenulové a odpovídá tištěnému ± binom(r,floor(r/2)).

Použijme právě doloženou 114 s d_1=m−1,d_2=n−1,
S_1={1,…,m},S_2={1,…,n}. Dává pravděpodobnost nekořenu
alespoň 1/(mn)>0, tedy alespoň jeden nepokrytý bod. To je spor
s úplným pokrytím. Mřížka je neprázdná i při nulových parametrech.
Pro r=0 má koeficient hodnotu 1, prázdné součiny mají hodnotu 1;
stejně argument funguje pro p=0, q=0 a pro m=1 nebo n=1.
Nejde o tvrzení nad každým konečným tělesem: použitá geometrie je
reálná a nenulovost binomického koeficientu je zajištěna touto volbou.
Úloha neuvádí algoritmus, enumeraci ani asymptotický náklad; důkaz
má konečný součin p+q+2r faktorů a jediný explicitní koeficient.

## Rozsah uzavření

Celé 114 a 115 jsou doloženy včetně každého tištěného matematického
mezikroku, poznámky, kraje a odkazu potřebného pro důkaz. Šest vrstev
errat a tři TeX zdroje byly prohledány podle současné i fasciklové
stránky, čísel úloh a formulací. Jediná relevantní oprava je E134;
opravy odpovědí 114–115 na str. 444 jsou jiné úlohy ze Sudoku.
Samostatný soubor mpr-114-115-nullstellensatz-errata.json obsahuje
otisky zdrojů a okolí všech shod. Stránka file 43 nyní může být
reviewed s převzetím D208–D211 pro předchozí zadání. File 408
zůstává partial pouze pro dřívější matematickou mezeru C048 v
poznámce ke 113, s celkem čtyřmi přesnými bibliografickými výjimkami.
Nové 114–115 tuto mezeru nezakrývají.
