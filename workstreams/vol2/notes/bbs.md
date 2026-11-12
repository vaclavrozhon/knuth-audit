# §4.5.4-43: bit BBS a faktorizace

**Rozsah.** Původní zadání 416–417 a odpověď 668–669 byly přečteny
vizuálně. Hlavní úkoly (a), (b) mají níže úplnou konstruktivní opravu.
Čtyři nálezy C0182–C0185 se týkají vytištěných pomocných vzorců a důkazu,
ne prokázané možnosti prolomit BBS bez faktorizace. Tištěný exemplář nebyl
prověřen. Nečiníme žádný předpoklad ani závěr o dnešní konkrétní obtížnosti
faktorizace. Silnější optimalizace citovaná na konci odpovědi je oddělena
v §8 jako externí výsledek.

Generátor Blum–Blum–Shub (BBS) opakovaně umocňuje stav modulo m
na druhou a vydává jeho paritu. Redukce má ukázat, jak z prediktoru
jediného bitu získat celý kořen a následně faktor. Základní myšlenka
je půlit interval, v němž kořen leží, a chybující bity opravovat hlasováním.
Značíme Pr pravděpodobnost, E střední hodnotu a var rozptyl; log je
přirozený logaritmus, log2 dvojkový. O vyjadřuje asymptotickou horní mez
s absolutní konstantou při uvedeném výpočetním modelu.

## 1. Značení a algebra

m = pq je součin různých prvočísel p,q = 3 modulo 4. Má r bitů,
tj. 2^(r−1) <= m < 2^r. Kniha navíc požaduje intervaly z 3.5P na 174;
protipříklady s m = 209 = 11*19 je splňují:
64 < 11² < 128, 256 < 19² < 512, 128 < 209 < 256.
Z_m je množina zbytků 0,...,m−1; jednotka je zbytek nesoudělný s m.
Q je množina všech druhých mocnin v Z_m, Q* její invertibilní část.
Čínská věta o zbytcích dává

```
|Q| = (p+1)(q+1)/4,
|Q*| = (p−1)(q−1)/4.
```

V každé souřadnici je na nenulových čtvercích mocnění na druhou
permutací: jejich grupa má lichý řád (p−1)/2, resp. (q−1)/2.
Nula se zobrazuje na sebe. Každé y v Q proto má právě jednu odmocninu
s v Q. Tuto **kanonickou odmocninu** značíme sqrt_Q(y). Výskyt S_m
namísto Q_m v jedné větě zadání 416 je již opraven v erratu
z 27.4.2001; nejde o nový nález.

Pro pevné y definujme s = sqrt_Q(y), tau(v) = v*s mod m a
lambda(v) = tau(v) mod 2. Pro s jednotku platí

```
lambda(−v) + lambda(v) = 1, pokud v != 0 modulo m,
tau(v/2) = (tau(v) + m*lambda(v))/2,
lambda(v1+...+vk) = sum lambda(vi) + floor(sum tau(vi)/m) modulo 2.
```

Zde v/2 znamená násobení inverzí 2 v Z_m; poslední rovnost platí
s celočíselnými koeficienty i pro záporné součty. První rovnost obecně
potřebuje tau(v) != 0. V zadání dovolujícím y = 0 je bez této výhrady
nepravdivá, například m = 209,y = 0,v = 1. V redukci níže jsou s a
použité nenulové multiplikátory jednotky, nebo již známe faktor.

Pro jednotku v definujeme znaménko chi(v): +1 na Q*, −1 na −Q*,
0 při Jacobiho symbolu −1. Jacobiho symbol je zde součin Legendreových
symbolů modulo p a q; jeho výpočet nepotřebuje rozklad m. Protože −1
je nečtverec v obou prvočíselných tělesech, jednotky s Jacobiho symbolem
+1 se disjunktně rozkládají na Q* a −Q*. Dále

```
chi(4v) = chi(v),
sqrt_Q(v² y) = chi(v)*tau(v) mod m, pokud chi(v) != 0.
```

Na nejednotkách pro účely pravděpodobnostních odhadů klademe chi = 0.
Algoritmus při vlastním gcd ihned vrátí faktor; samotnou nulu ignoruje.

## 2. C0183: rozdělení ve vytištěném algoritmu (a)

Zadání předpokládá úspěch G na **rovnoměrném Q**. Rovnoměrné x v Z_m
ale nedává rovnoměrné x²: jednotkový čtverec má čtyři vzory, nenulový
nejednotkový dva a nula jeden. Totéž rozdělení má x⁴, protože druhá
mocnina permutuje Q. Proto tvrzení EX_j >= 1/2+epsilon na 668 neplyne.

Přesný protipříklad: m = 209. Q má 60 prvků, z nich 45 jednotkových
a 15 nejednotkových. Nechť G správně předpovídá kanonickou odmocninu
na všech 15 nejednotkových vstupech a na prvních 16 jednotkových
vstupech Q v rostoucím pořadí; jinde vrátí opačný bit. Celá tabulka
je v `results/bbs.json`. Pak

```
Pr_Q(G správně) = 31/60 = 1/2 + 1/60,
Pr_x(G(x⁴) = x² mod 2) = (1+14*2+16*4)/209 = 93/209 < 1/2.
```

Pro y = 1 je tedy většinové hlasování obráceno. Při delta = 1/4
kniha zvolí n = 2496. Hoeffdingova nerovnost dává pravděpodobnost
**správné** odpovědi nejvýše
exp(−2n*(1/2−93/209)²) < 3*10^−7. Nejde pouze o nepřesnou konstantu
v důkazu. Omezení x na jednotky samo nestačí, protože výhoda G byla
slíbena na jiné množině. Zároveň to nevyvrací existenci algoritmu A.

### Úplná oprava (a)

Uvažujme 0 < epsilon <= 1/2 a 0 < delta <= 1/2. Nejdříve spočteme
gcd(y,m). Vlastní gcd dává rozklad a příslušnost k Q rozhodneme dvěma
Legendreovými symboly; y = 0 přijmeme. Jednotku s Jacobiho symbolem
−1 odmítneme. Zbývá jednotkové y s Jacobiho symbolem +1.

Vezmeme n = ceil(8 epsilon^−2 log(2/delta)) nezávislých x z 1,...,m−1.
Každé vlastní gcd(x,m) využijeme stejně. Pokud jsou všechna x jednotky,
hlasujeme podle G(y²x⁴) = (yx² mod m) mod 2 jako v knize.

Označme rho = (p+q−2)/(pq−1), pravděpodobnost vlastního gcd takto
vybraného x, a theta = |Q\Q*|/|Q| = 2(p+q)/((p+1)(q+1)). Platí
theta <= 4 rho. Jsou dvě možnosti, které algoritmus nemusí rozlišovat:

- Pokud rho >= epsilon/8, pravděpodobnost, že neobjevíme faktor,
  je nejvýše exp(−n epsilon/8) <= delta/2.
- Pokud rho < epsilon/8, je theta < epsilon/2. Z celkového úspěchu G
  plyne na rovnoměrném Q* úspěch alespoň
  1/2 + (epsilon−theta/2)/(1−theta) >= 1/2+3epsilon/4.
  Podmíněně na všech gcd = 1 jsou x nezávislé rovnoměrné jednotky.
  Pro y v Q* má yx² rovnoměrné rozdělení na Q*. Pro y v −Q* má −yx²
  rovnoměrné rozdělení na Q* a jeho parita je opačná. Hlas má tedy
  správné znaménko s odchylkou nejméně epsilon/2; Hoeffding dává chybu
  nejvýše exp(−n epsilon²/2) <= delta/2.

Čas je O(epsilon^−2 log(2/delta)*(T(G)+r²)). Jacobiho symbol, gcd
a konstantní počet modulárních násobení mají klasicky O(r²) cenu.
Známé faktory dovolí rozhodování symboly, nepotřebujeme pomalé
vyčíslení odmocniny. Pro delta > 1/2 stačí férový náhodný odhad.

## 3. C0182: chybějící plus v definici hlasu

Na 669 je v definici G_j vytištěno
`floor(alpha_t*j*beta_t + beta_(t+1))`. Správně má být
`floor(alpha_t + j*beta_t + beta_(t+1))`. **Následující samostatný
vzorec v knize již plus má správně**; oprava se týká pouze definice G_j.

Přesný lokální příklad v pravé větvi: m = 209,y = s = 1,t = 0,
epsilon = 1/2,a = 1,b = 2,j = −6. Přípustné počáteční aproximace
jsou alpha_0 = 1/128, beta_0 = 5/512, beta_1 = 5/1024. Obě počáteční
chyby jsou menší než požadované epsilon/64, resp. epsilon³/64.
Máme u = 199 v Q*, tau(u) = 199 a u leží mimo obě chybové krajní
oblasti šířky epsilon*m/16. Přesto

```
floor((1−6*2+1)/209) = −1,
floor(alpha_0−6*beta_0+beta_1) = −1,
floor(alpha_0*(−6)*beta_0+beta_1) = 0.
```

Vynechané plus tedy může obrátit bit hlasu. Nejde o chybu OCR.

## 4. C0184: definice Z_j ignoruje záporné chi

V definici Z_j na 669 je oracle označen za chybný, když
G(u²y) != lambda(u), ať je chi(u) +1 nebo −1. Při chi(u) = −1 ale
správný prediktor vrací lambda(−u) = 1−lambda(u). Hlas Y_j už toto
znaménko opravuje; definice Z_j nikoli. Správná podmínka je
G(u²y) != lambda(chi(u)*u).

To není pouze otázka nejednotek. I na rovnoměrných jednotkách,
pro dokonalý G a s = 1, se mimo krajní pásy ruší příspěvky +1
z Q* a −1 z −Q*. Vytištěný průměr je proto nekladný namísto
>= 3epsilon/4. Při m = 209,epsilon = 1/2 vychází přesně −2/45;
opravená definice dává 37/90. Nedokazuje se tím chyba samotného
znaménka v hlasování, které je správné.

## 5. C0185: v součtu chyb chybí etapa nula

Algoritmus na 668 začíná t = 0 a zná lambda(a),lambda(b).
V této etapě ještě musí odhadnout lambda(a/2),lambda(b/2), takže nejde
o etapu bez hlasování. Vytištěná mez pro dvě chyby v etapě je
4/(9 min(r,2^t)). Následující součet na 669 však geometrickou část
začíná až t >= 1. Pro r = 8 je součet skutečně uvedených mezí

```
(4/9) sum_(t=0)^7 1/min(8,2^t) = 19/18 > 8/9.
```

Tedy deklarovaná celková mez 4/9+4/9+1/90 není tímto výpočtem
odvozena. Netvrdíme, že skutečná chybovost programu musí překročit 9/10;
jde o chybný součet horních mezí. Vlastní důkaz níže počítá všechny
etapy od nuly a používá volnější konstanty. Původní článek má jiné
indexování: jeho RSA smyčka skutečně začíná t = 1 (226).

## 6. Úplná konstruktivní redukce (b)

Následující konstanty nejsou optimalizované. Volíme dyadické eta,
tj. zápornou celočíselnou mocninu 2, s epsilon/8 < eta <= epsilon/4.
Pak 0 < eta <= 1/8 a eta^−1 = O(epsilon^−1). Položme

```
B = 4096 r eta^−2,              n_max = 64 r eta^−2,
n_t = 64 min(r,2^t) eta^−2,     0 <= t < r.
```

Zkusíme dělitele do B, případně jen do sqrt(m). Pokud žádný nenajdeme,
p,q > B. Tím dostáváme zároveň všechny potřebné podmínky pro párovou
nezávislost a malé příspěvky nejednotek. Jejich podíl v Q je
< 4/B < eta/1024, takže úspěch G na Q* je alespoň 1/2+2eta.

Náhodným výběrem najdeme x s Jacobiho symbolem −1; vlastní gcd dává
faktor rovnou. Položme y = x². Kanonická odmocnina s má oba Legendreovy
symboly +1, kdežto x má smíšené symboly. Proto s != ±x a
`gcd(x−s,m), gcd(x+s,m)` jsou přesně p,q. Stačí rekonstruovat s.

Vybereme a,b nezávisle rovnoměrně v Z_m. Vlastní gcd využijeme a při
a = 0 nebo b = 0 pokus opakujeme. V analýze níže pracujeme na původním
nepodmíněném prostoru všech (a,b); nuly připočteme do neúspěchu, abychom
podmiňováním neztratili párovou nezávislost.

Projdeme všechny počáteční odhady alpha_0,beta_0 na středových dyadických
mřížkách s chybami < eta/4096 a < eta³/4096, a obě možné parity
lambda(a),lambda(b). Celkem je O(eta^−4) větví a jedna z nich je pravá.
Nesprávnou větev nikdy nepřijmeme bez ověření výsledného vlastního faktoru.

### Etapy a hlasování

Pišme a_t = 2^−t a mod m a b_t = 2^−t b mod m. V pravé větvi známe
parity lambda(a_t),lambda(b_t) a aproximace

```
|tau(a_t)/m − alpha_t| < eta/(4096*2^t),
|tau(b_t)/m − beta_t|  < eta³/(4096*2^t).
```

Nejdříve spočteme alpha_(t+1) = (alpha_t+lambda(a_t))/2 a stejně beta.
Pro −n_t/2 <= j < n_t/2 použijeme

```
u_(t,j) = a_t + j*b_t + b_(t+1) mod m,
v_(t,j) = a_(t+1) + j*b_(t+1) mod m.
```

Z identity v §1 hlasujeme pro lambda(b_(t+1)) pomocí

```
H_j = G(u²y) + lambda(a_t) + j*lambda(b_t)
      + floor(alpha_t+j*beta_t+beta_(t+1)) modulo 2,
Y_j = (2H_j−1)*chi(u).
```

Bit je 1 právě při nezáporném součtu hlasů. Potom analogicky pro
lambda(a_(t+1)) použijeme v, již zjištěný bit lambda(b_(t+1)) a
`floor(alpha_(t+1)+j*beta_(t+1))`. Jde o dvě různá hlasování;
pořadí dovoluje použít nový bit b v druhém z nich.

Celková numerická chyba v argumentu prvního floor je nejvýše
eta/4096 + eta/128 + eta³/8192 < eta/64. Druhá je ještě menší.
Shoda podlah proto platí, když tau(u)/m, resp. tau(v)/m, neleží
ve vzdálenosti eta/64 od 0 nebo 1. Totéž platí při použití konečné
pracovní přesnosti popsané níže.

### Párová nezávislost a pravděpodobnost

Pro různá j,k má zobrazení (a,b)->(u_j,u_k) determinant roven
nenulové mocnině 2 krát (k−j); totéž platí pro v. Protože |k−j| < n_t
< p,q, determinant je jednotka modulo m. Zobrazení je tedy bijekce
na Z_m². Jednotlivé u_j jsou rovnoměrné a každá dvojice nezávislá.
Volání náhodného G používají nezávislé mince pro různé pozice.

Pro jednotkové u s chi != 0 nechť W(u) = +1, pokud G(u²y) správně
vrátí lambda(chi(u)*u), jinak −1; jinde W = 0. Na každé z tříd
Q* a −Q* se kanonický kořen rovnoměrně pohybuje po Q*. Počet jednotek označme phi(m) = (p−1)(q−1). Proto

```
E W >= (phi(m)/m)*2eta.
```

Definujeme Z stejně jako W,
ale v krajních pásech šířky eta/64 jej snížíme na −1, pokud chi != 0.
Tau je permutace Z_m, takže pravděpodobnost těchto pásů je nejvýše
eta/32+1/m. Pro p,q > B z toho plyne

```
E Z >= 2eta*(1−2/B) − 2*(eta/32+1/m) >= eta,
var(Z) <= 1.
```

Z závisí pouze na u a na jeho čerstvých mincích, nikoli na ostatních
aproximacích. Veličiny Z_j jsou tedy párově nezávislé. Pokud je součet
Z_j kladný, hlasování v pravé větvi je správné. Čebyševova nerovnost
dává chybu jedné majority nejvýše 1/(n_t eta²). Součet pro obě
hlasování ve všech etapách **včetně t = 0** je menší než

```
(1/32) sum_(t=0)^(r−1) 1/min(r,2^t) < (1/32)*(2+1) = 3/32.
```

Tyto meze jsou nepodmíněné: pomocí pravých tau a aproximací definujeme
ideální chyby pro každou etapu. První skutečná chyba je obsažena
v jejich sjednocení. Nepředpokládáme párovou nezávislost po podmínění
na úspěch předchozích etap.

Znaménka chi lze připravit pro obě rodiny pouze v etapách 0 a 1,
protože posun o dvě etapy znamená dělení čtvercem 4. Je nejvýše
4 n_max vstupů. Opravené A z §2 použijeme s delta = 1/(64 n_max).
Souhrnná chyba těchto rozhodnutí je nejvýše 1/16. Vlastní gcd z kteréhokoli
podprogramu ukončuje faktorizaci úspěšně. Pravděpodobnost a = 0 nebo
b = 0 je nejvýše 2/m. Celkový úspěch jednoho pokusu je tedy větší
než 1−3/32−1/16−2/m > 1/2.

Po r etapách má m*beta_r od tau(b_r) vzdálenost menší než 1/2.
Zaokrouhlení určí tau(b_r) přesně a
`s = 2^r*b^−1*round(m*beta_r) mod m`. V každé větvi ověřujeme nejen
s² = y, ale i výsledné vlastní gcd s původním x. Pouhá rovnost čtverců
nerozliší všechny čtyři kořeny; nesprávná větev nesmí skončit trivialitou.

### Čas a výpočetní model

Položme T* = T(G)+r². Stejně jako Fischlin–Schnorr 222/228 počítáme
v pomocných hlasováních operace se slovy o O(log(r/eta)) bitech;
nejde o tvrzení, že všechny tyto operace mají jeden **bitový** krok.
Při čistě bitovém účtování se cena krátké aritmetiky musí doplnit.

Předvýpočet chi potřebuje O(r eta^−4 log(r/eta) T*) času. Všechna
volání G v etapách potřebují O(r² eta^−2 T*); odpovědi uchováme podle
pozice (t,j,rodina) a sdílíme mezi větvemi. Nesdílíme nové náhodné
mince mezi různými pozicemi jen proto, že se náhodou shodly jejich vstupy.
Výpočet zbytků a gcd i předběžné dělení do B se do požadované meze vejdou.

Vlastní práce ve všech O(eta^−4) větvích je O(r² eta^−6) slovních
operací. Pro floor stačí L = ceil(log2(1024*(n_max+2)/eta)) počátečních
bitů každé aproximace. Jejich zahazování při půlení přidá do argumentu
floor chybu menší než eta/1024; spolu s předchozí mezí je stále < eta/64.
Půlení aktualizuje tento krátký začátek v konstantním počtu slovních
operací. Pro konečné zaokrouhlení uchováváme celý proud získaných bitů;
ten lze zapisovat bez opakovaného kopírování rbitového čísla. Závěrečné
sestavení a násobení stojí O(r²) na větev a mez nezhorší.

Protože log(r/eta) = O(r log(1/eta)), dostáváme požadovaný čas

```
O(r²*(epsilon^−6 + epsilon^−4 log(1/epsilon)*(T(G)+r²))).
```

Za předpokladu T(G) >= r² z (a) je to přesně uvedený tvar (b).
Konstantní očekávaný počet opakování jej nezmění.

## 7. Přesné výpočetní kontroly a jejich omezení

`verify_bbs.py --resume` má tři samostatně ukládané bloky. První prochází
všechny povolené malé moduly s r <= 12, ověřuje kanonické kořeny dvěma
modely (úplné množiny proti CRT a modulárnímu umocnění), četnosti vzorů,
půlení a znaménka. Úplné obrazy pěti lineárních zobrazení na Z_209²
kontrolují i ztrátu nezávislosti, když rozdíl indexů dělí m.

Druhý blok přesně vyčísluje všechny čtyři protipříklady a racionální
meze konzervativních konstant. Třetí rekonstruuje kořeny na 12 vstupech
modulo 383*787, s dokonalým prediktorem a **dodanou pravou počáteční
větví**. Testuje jednotlivé parity, podlahy a bodovou dominanci Z vůči
podepsanému hlasu. Není to úplná enumerace všech odhadů, statistický
důkaz úspěšnosti ani experiment dokládající obtížnost faktorizace.

Výsledek: 11 modulů, 117963 algebraických kontrol, 5 úplných párových
obrazů, 2024 kontrol konstant, 12 rekonstruovaných kořenů a 56746
bodových kontrol hlasů; tři bloky celkem 6.512897 s. První běh
PID 1315040/1315041, session 62256, limit 180 s, exit 1; pokračování
PID 1315200/1315201, session 87303, limit 180 s, exit 0.

První běh prošel první dva bloky a zastavil se na chybně zvoleném
modulu testu: q = 769 je 1 modulo 4, takže pro něj neplatí použitý
vzorec kanonické odmocniny. Opraveno na prvočíslo 787 = 3 modulo 4
a přidána explicitní kontrola této podmínky. První dva úspěšné bloky
se neopakovaly. Log i údaje o obou bězích jsou zachovány.

## 8. Primární články, závěrečný odstavec a errata

Fischlin–Schnorr, J. Cryptology 13 (2000),221–244:
vizuálně 221–222,224–228,239–242. Strana 227 výslovně vysvětluje,
že dřívější definice aproximačních chyb nebyla párově nezávislá,
a připisuje upozornění Knuthovi a pomoc s opravou Goldreichovi.
Zvětšení chybové události na pás závislý jen na multiplikátoru je
správný postup, který používá i kniha. Nález C0184 se týká dalšího,
odlišného problému se znaménkem při přechodu na necentrovaný BBS.

Na 241–242 originál explicitně pracuje s podgrupou Q* jednotek,
obrací bit na −Q* a uvádí silnější Theorem 8 s časem
O(r epsilon^−4 log(r/epsilon) T(G)). Naše vlastní redukce v §6 tento
optimalizovaný výsledek nepotřebuje. Neprověřovali jsme celý optimalizační
argument §3–4 článku; Theorem 8 je zde citovaný externí výsledek.
Vztah jeho optimalizací k obecnému důkazu byl přečten, nikoli nahrazen
vlastní úplnou optimalizovanou implementací.

Kombinace s opraveným 3.5P4 (viz `notes/cryptographic.md`) dává z testu A
pro N bitů prediktor s výhodou epsilon/N a časem
T_bit = T(A)+O(N R²). Dosazením do silnějšího externího výsledku dostaneme

```
O(R N^4 epsilon^−4 log(RN/epsilon)*(T_bit+R²)).
```

To odpovídá tvaru posledního odstavce při označení T(G) = T_bit.
Pokud T(G) čteme jako čas **původního testu**, musí se předgenerování
N bitů účtovat a konzervativní dosazení má T(A)+N R². Tyto dvě ceny
nezaměňujeme; ze stručné změny značení nevyvozujeme další potvrzený
protipříklad k existenci rychlejšího algoritmu. Průměrování přes moduly
musí zachovat rozdělení zdroje z 3.5P; pro dobré moduly se postupuje
jako v dřívější poznámce. Bez předpokladu obtížnosti faktorizace se
neprokazuje nepředvídatelnost konkrétního generátoru.

Alexi–Chor–Goldreich–Schnorr: původní 194 vizuálně, metadata SIAM
potvrzují 17(2),1988,194–209. Celý šestnáctistránkový důkaz nerevidován.
Ben-Or–Chor–Shamir: bibliografie STOC 1983,421–430 potvrzena institucionálním
záznamem TAU; původní článek nebyl získán ani čten. Konferenční verzi
Fischlin–Schnorr LNCS 1233(1997),267–279 potvrzuje vydavatel; aktuální
erratum správně odkazuje na rozšířenou časopiseckou verzi.

Prohledány všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
a aktuální `sources/err2.textxt`, podle stran, čísla úlohy, jmen,
pravděpodobnostních vzorců a výrazů pro hlasy. Vizuálně `all2-prepre`
strany souboru 24 a 42: známá oprava S_m na Q_m z 27.4.2001,
a opravy z 14.2.2000 v součtu X a exponentu
−2 u rozsahu j na 668; aktualizace citace z 2.7.2001. Tyto opravy
C0182–C0185 neřeší. Návrhy hlášení jsou neodeslané; potvrzení znamená
ověření v našich zdrojích, nikoli prvenství nebo ověření pozdějšího tisku.
