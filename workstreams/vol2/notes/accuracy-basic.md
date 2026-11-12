# §4.2.2: základní zákony, porovnání a rozptyl

Původní text229–245 a odpovědi613–617 byly vizuálně přečteny při prvním
průchodu. Původní souhrnné uzavření se při obnově nepřebírá: stav každého
tvrzení a celé úlohy určuje strukturovaná mapa quality-recovery.
Obnova X0209–X0213 má vlastní úplné důkazy axiomů, relativní chyby,
porovnání a celých1–9/16/25; celé6/7/16 si ponechávají přesně popsané
mezery. Další úlohy a následující text čekají na individuální revizi.
Konečné experimenty níže zůstávají archivní evidencí svého rozsahu,
ne důkazem všech vět a všech tištěných mezikroků.

## Konvence a vrstvy oprav

b>=2 je celočíselný základ, p>=1 počet cifer, q exces exponentu.
Číslo(e,f) znamená f*b^(e−q), |f|<1. Normalizace vyžaduje |f|>=1/b,
nebo f=0 s nejmenším exponentem. V tomto textu R(x) označuje nejbližší
normalizované plovoucí číslo; pro sudé b řešíme poloviny jako AlgoritmusN.
Pro liché b AlgoritmusN výběr na půlce neurčuje; základní počítačový
model zde používá výběr od nuly a všechny důsledky této volby označuje.
Symboly⊕,⊖,⊗,⊘ znamenají přesnou operaci následovanou R.
Všechny výrazy musí být definovány: nulový jmenovatel a přetečení či
podtečení jsou mimo zákony. Tuto podmínku opakuje erratum17.8.2021.

Pro úlohy v tomto bloku jsou zahrnuty opravy: absolutní hodnota
v(18) z1.3.2007; hodnoty8(c–e) z28.1.1999; zaokrouhlený součet
v7 i jeho odpovědi z31.5.2021; přeformulování15 z14.9.2019;
101.11110 v16(a) z1.3.2007; inicializace Welforda z23.9.2024;
neostrá mez za(37) z15.5.2026; nová32 i odpověď z17.1.2014.
Všechny čtyři řady errat prohledány; příslušná sazba v images/accuracy-errata-*.

## 1. Zákony a relativní chyba

R je neklesající, zachovává znaménkovou symetrii a je identitou na
reprezentovatelných číslech. Navíc R(x)=0 právě pro x=0, je-li výsledek
definovaný. Tím přímo dostáváme(2)–(8) a zákony na231. Například
u⊖v=R(u−v)=−R(v−u); komutativita a dvojí použití monotonie dává
úlohu2: při x,y>=0 je (u⊕x)⊕(v⊕y)>=u⊕v. Násobení kladnou
konstantou je neklesající, převrácená hodnota na kladné poloose
nerostoucí; jejich zaokrouhlené varianty dědí stejné pořadí.
Pokud součet nebo součin vyšel přesně, následující inverzní operace
vrací přesně reprezentovatelný vstup. Posunutí exponentu dává
R(bx)=bR(x), včetně pravidla pro poloviny, pokud je toto pravidlo
konzistentní při posunu exponentu, jako zde používané volby.

Pro nenulové x položme B=b^(e−1)<=|x|<b^e a h=b^(e−p).
Označme ρ=R(x)−x. Protože B je samo reprezentovatelné,
|ρ|<=|x|−B; dále |ρ|<=h/2. Tedy

```text
|ρ/x| <= |ρ|/(B+|ρ|) <= (h/2)/(B+h/2) < b^(1−p)/2.
```

To ověřuje(18), včetně opravené absolutní hodnoty. Označme η=b^(1−p)/2.
Dvě asociace součinu mají vůči uvw dva relativní faktory1+δ,
|δ|<η. Poměr leží mezi((1−η)/(1+η))² a jeho převrácenou hodnotou.
Největší vzdálenost od1 je menší než4η/(1−η)², což je(19).
Nulový součin je triviální; důkaz poměrem se používá pro nenulový součin.

Protože |R(x)|>=B, také |ρ|<=η|R(x)|. Spolu s předchozí nerovností
plyne opravená mez `|ρ|<=η min(|x|,|R(x)|)` za(37).
Neostrost je nutná: v určitých binárních formátech a polovinách nastává
rovnost vůči zaokrouhlenému výstupu. Racionální kontrola12 060 hodnot
ve27 formátech obsahuje8 těchto rovností. Pro x=0 je závěr triviální.
(38) a(39) následují z definice aproximace popsané dále.

Tištěné příklady neasociativity součtu a součinu i selhání distributivity
souhlasí přesně; viz results/accuracy-basic.json. Úloha4: v desítkovém
formátu s exponenty−50..50 lze vzít u=10^−40,v=w=10^30.
Levá asociace má mezivýsledek10^−10 a výsledek10^20; pravá potřebuje
10^60, které přeteče. Úloha5:9⊘9=1, ale9⊗(1⊘9)=.99999999 pro p8.
V6(a) je dvojí negace přesná.

## 2. Porovnávací relace a nalezená hranice nuly

Obnova X0213: úplné důkazy každé21–39 a všech částí8–9 jsou v
[podrobné poznámce](recovery-accuracy-comparisons-2026-11-06.md).
Zahrnuje oba původní i opravené soubory hodnot, všechny mezikroky,
nutné rozšíření38 na přesné reálné argumenty a nulové okraje.

Položme B_u=b^(e_u−q). Definice21–24 jsou:

```text
u≺v(ε)  iff v−u>ε max(B_u,B_v),
u~v(ε)  iff |u−v|<=ε max(B_u,B_v),
u≈v(ε)  iff |u−v|<=ε min(B_u,B_v).
```

Relace≻ je převrácením≺. První tři možnosti tvoří rozklad všech dvojic,
a≈implikuje~. Uzavřené intervaly N(u)=[u−εB_u,u+εB_u] dávají přesně
interpretaci na234. Symetrie, reflexivita a změna ε ve25–31 jsou přímé.
Pro32 sečteme dvě kladné mezery; první je větší než min(ε1,ε2)B_u,
druhá větší než min(ε1,ε2)B_w, takže součet překračuje požadované maximum.

**V(33) jsou oba předpoklady≈.** Trojúhelníková nerovnost dává

```text
|u−w| <= ε1 min(B_u,B_v)+ε2 min(B_v,B_w)
       <= ε1 B_u+ε2 B_w <= (ε1+ε2) max(B_u,B_w).
```

Závěr nelze změnit na≈: pro b10,p2,q0 vezměme u=(0,.50),
v=(1,.05),w=(1,.06), ε1=ε2=.01. První dvojice má stejnou hodnotu,
druhá rozdíl.1<=.01*10; ale |u−w|=.1>.02*1. Jde o dovolené
nenormalizované reprezentace, na které se definice výslovně vztahují.
Úloha8 po opravách dává~a≈v(a–c), pouze~v(d,e).

Protože |u|<B_u, podmínky34–35 implikují požadované relace.
Naopak pro **nenulové** normalizované u je B_u<=b|u|, takže36–37
následují přímo. Zahrnutí nuly však36 vyvrací: viz samostatný
[nález C0083](C0083-essential-zero-boundary.md). Dostatečná jednotná
oprava je ε<1/b místo ε<1. Výsledek37 s „nebo“ platí i pro nulu,
protože její exponent je minimální.

## 3. Převrácená hodnota, Cauchy a předčasné odříznutí

Pro6(b) položme N=b^p,u=1−1/N. Jestliže b>=3 a b+p>4,
platí (b−2)N>b, takže1/u=1+1/(N−1) je blíže1 než dalšímu číslu1+b/N.
Dvojí převrácení pak vrátí1≠u. Pro b2,p>=3 první převrácení
vrátí1+2/N a druhé1−2/N≠1−1/N; rozhodne N>6.
Pro b2,p1 stačí jediný normalizovaný zlomek, pro b2,p2 zlomky1/2,3/4:
oba se po dvojím převrácení vrátí. Pro b3,p1 se vracejí zlomky1/3,2/3
při polovinách od nuly nebo na sudé; **při polovinách na liché nikoli**.
Takto je třeba číst malou ternární výjimku odpovědi, protožeN její
poloviny nespecifikuje. Volba ovlivňuje i úlohu15, viz oddíl5.

Cauchyho protipříklad7: b2,p6,u=33/64,v=34/64. Součet se zaokrouhlí
na2v; jeho zaokrouhlený čtverec je větší než2(u⊗u⊕v⊗v).
Kontrola počítá obě strany přesnými zlomky. Zahrnuta oprava2021.

Úloha10 o odříznutí před normalizací: b3,p2,u=8/9<v=1,w=5/9.
Surový zlomek u*w=40/81 se odřízne na4/9. Pro v má surový zlomek
hodnotu5/27 a exponent1: odříznutí dává1/9 a výslednou hodnotu1/3.
Tedy u⊗w>v⊗w. Obecné desítkové označení cifer v odpovědi614
znamená cifru b−1, ne desetinnou devítku. V rámci stejného exponentu
je odříznutí monotónní. Na hranici exponentu položme B=b^p a označme
celý significand druhého činitele F, B/b<=F<B. Pro poslední hodnotu
před hranicí je v jednotkách společného exponentu odříznutý výsledek
floor(F(B−1)/B)=F−1; pro první za hranicí b*floor(F/b)=F−(F mod b).
Druhý výsledek je nejméně první právě pro F mod b<=1. To vždy platí
v binární soustavě, zatímco větší základ dovolí propad.

Úloha13: jsou-li m,n celá, |m|<=2b^(p−1),0<|n|<b^p, všechna tato
čísla jsou reprezentovatelná. Pokud n dělí m, podíl je reprezentovatelné
celé číslo. Pokud n nedělí m, vzdálenost m/n od každého celého čísla
je nejméně1/|n|, ale chyba zaokrouhlení podílu je podle18 menší než
`|m/n| b^(1−p)/2 <= 1/|n|`. Nemůže tedy vyjít celé číslo.
A R(z mod1)=0 právě pro z mod1=0, při definovaných operacích.
Konečná doplňková kontrola25 625 dvojic souhlasí; záporná znaménka
pokrývá symetrie. V b2 je dovoleno i krajní m=b^p, které je přesná mocnina.

## 4. Welford a úloha16

**Obnova X0211:** všechny části(a–c) a každý přechod mají úplné argumenty
v [nové poznámce](recovery-accuracy-welford-2026-11-06.md). Dodatečná
věta o „errors of order n“ zůstává partial pro neurčené měřítko chyby;
původní obecné uzavření16 se na tuto větu nerozšiřuje.

Pro přesné operace označme M_k průměr prvních k hodnot a S_k součet
čtverců odchylek těchto hodnot od M_k. Z identity
M_k=M_(k−1)+(x_k−M_(k−1))/k a rozvoje čtverců vyjde

```text
S_k = S_(k−1)+(x_k−M_(k−1))(x_k−M_k).
```

Počáteční M0=S0=0 funguje i pro k1. Výběrový rozptyl je S_n/(n−1),
pro n>=2. To vysvětluje opravené15–16; záměna přesných operací
za plovoucí samozřejmě negarantuje přesný statistický výsledek.

Pro nezápornost výpočtu stačí dokázat, že aktualizace průměru leží
mezi starým průměrem a x_k. Dokážeme silnější pomocné tvrzení:
pro t>=0 a k>=2 je R(R(t)/k)<=t. Označme d=R(t). Je-li d<=t,
stačí monotonie a R(d)=d. Je-li d>t, nechť l je předchozí kladné
plovoucí číslo; t>=(l+d)/2, zatímco d/k<=d/2<(l+d)/2. Proto
R(d/k)<=l<t. Případ, kdy by požadované číslo nebylo v rozsahu,
je vyloučen obvyklým předpokladem definovaných operací.

Pro v>=u tedy přírůstek R(R(v−u)/k) leží v[0,v−u]. Vnější R
nemůže překročit reprezentovatelné konce u,v. Pro v<u použijeme
znaménkovou symetrii. Proto mají x_k−M_(k−1) a x_k−M_k stejná
znaménka; jejich zaokrouhlený součin je nezáporný a totéž indukcí
platí pro S_k. V k1 je M1=x1 a S1=0. Pomocné tvrzení ověřeno
navíc pro12 884 konkrétních aktualizací v pěti různých formátech.

Pro16(a,b) je n=10^6 a x_k=1.1111111. Nezávislý celočíselný model
udržuje součet v jednotkách10^−7 a zaokrouhluje celočíselným dělením.
Všech šest přechodů exponentu souhlasí s odpovědí po opravě2007;
poslední je **k=900819**, nikoli908191 (náš prvotní chybný přepis byl
opraven). Výsledky:

```text
opakovaný součet x_k       = 1109099.1,
zaokrouhlené x_k²          = 1.2345679,
opakovaný součet x_k²      = 1224782.1,
rozptyl z(14)              = −.0053187053.
```

Odmocnina není reálná. Welford naproti tomu drží M_k=x1,S_k=0 přesně,
protože všechny pozdější rozdíly jsou0. Varovná poznámka o jiných datech
se neinterpretuje jako obecná bezchybnost Welforda.

## 5. Střed intervalu a ternární krajní případ

Monotonie redukuje úlohu15 na diagonálu: pro u<=v je
R(R(2u)/2)<=R(R(u+v)/2)<=R(R(2v)/2). V b2 je škálování2 přesné,
takže střed leží v intervalu. Pro větší základy jsou protipříklady
běžné, např.b10,p2,u=v=99: výsledek100. Oprava2019 správně
nahrazuje původní argument neprostotou zdvojení podmínkou na diagonále.

Zůstává však výjimka **b3,p1 s polovinami od nuly nebo na sudé**.
Každé nenulové číslo je ±3^e nebo ±2*3^e. Pro1 je
R(R(2)/2)=1; pro2 je R(4)=3 a R(3/2)=2. Znaménková symetrie
a násobení mocninou3 dávají diagonální identitu pro všechna čísla,
a monotonie tedy vlastnost středu pro všechny dvojice. Při polovinách
na liché místo toho R(3/2)=1 a pro u=v=2 vlastnost selže.
Chybějící výjimku eviduje potvrzený nález C0084 (viz samostatná poznámka);
nejde o problém desítkové ani běžné binární aritmetiky.

Pro b>=5 selže diagonála u=b^p−1:2u se zaokrouhlí na2b^p,
polovina je b^p. Pro b4 oba možné výběry poloviny dají buď b^p,
nebo b^p−2, takže také selžou. Pro b3,p>=2 mají u=b^p−1
a v=b^p−2 stejný zaokrouhlený dvojnásobek2b^p−3; alespoň jeden
z nich se tedy nevrátí, ať se následná polovina rozhodne jakkoli.

## 6. Nová úloha32

Zde písmena a,b označují parametry vzorce, **b není základ soustavy**.
Požadujeme `round_even(x)=floor(ax+b)+ceil(ax−b)` pro každé reálné x.
Porovnání růstu při x→∞ vynutí2a=1. Celočíselný posun b se mezi
podlahou a stropem zruší, takže stačí0<=b<1. Dosazení x=1/2
vynutí1/4<=b<3/4. První kladný skok pravé strany nastává v
min(2b,2−2b); musí být v1/2. V uvedeném rozmezí tím zbývá b=1/4.

Naopak pišme x=2n+t, n celé,0<=t<2. Pro a=1/2,b=1/4 pravá strana je

```text
2n + [t>=3/2] + [t>1/2],
```

což přesně odpovídá zaokrouhlení na nejbližší celé se sudým výběrem
polovin. Všechna řešení tedy jsou a=1/2,b mod1=1/4. Kontrola5194
racionálních vstupů a posunů zahrnuje i obě strany všech polovin.

## Reprodukce a rozsah

`python3 workstreams/vol2/verify_accuracy_basic.py` obnovuje jen chybějící
bloky. Sedm bloků je hotových v results/accuracy-basic.json; nic z nich
se bez nového důvodu nemá opakovat. První běh se zastavil na našem
chybně opsaném indexu přechodu16(a), po opravě byly obnoveny jen
poslední dva bloky. Model accuracy_model.py používá již nezávisle
ověřenou normalizaci4.2.1; dlouhé součty mají oddělený celočíselný model.
Důkazy výše nespoléhají na úplnost konečných numerických kontrol.
