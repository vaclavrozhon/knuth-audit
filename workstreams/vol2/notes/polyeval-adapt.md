# Adaptace koeficientů: §4.6.4, strany 490–494 a úlohy 18–24

Kontrola V2-X0077, 4. listopadu 2026. Matematický rozsah končí před
odstavcem „Polynomial chains“ na straně 494. Původní sazba stran
490–494, 516–517 a 701–702 byla prohlédnuta. Jde o třetí vydání,
první dotisk z roku 1997; pořadí stránky DjVu je tištěné číslo plus 12.

Výsledek: schémata a řešení úloh 18–24 jsou algebraicky ověřena.
C0235 potvrzuje obrácené směry v odpovědi 23; C0237 chybějící omezení
na sudý stupeň v závěru důkazu E. C0236 zůstává kandidátem na zpřesnění
podmínky Panova schématu. Oprava počtu faktorů v E je známé erratum.
Historické citace nejsou všechny uzavřeny; přesný stav je v oddílu 8.

## 1. Model a označení

`u(x)=sum(u_j x^j, j=0..n)`, kde `u_n != 0`, je reálný polynom.
**Monický** znamená `u_n=1`. Předběžná adaptace znamená jednorázový
výpočet parametrů z koeficientů; její náklady nejsou zahrnuty do
následného vyhodnocení pro každé nové x. Písmena M a A označují počet
násobení a počet sčítání nebo odčítání při tomto vyhodnocení.
Násobení dvou stejných hodnot se počítá jako jedno M. Vynechání známé
nulové konstanty či násobení jedničkou může počet snížit.

Ověřujeme přesné reálné identity a uvedené počty, nikoli všeobecnou
numerickou stabilitu nebo minimální počet instrukcí konkrétního stroje.
Dolní meze z pozdějších stran budou samostatným blokem.

## 2. Stupně čtyři a pět, úlohy 18–20

Obě kvartická schémata lze psát se znaménkem `s` rovným 1 nebo −1:

```
y = (x+a0)x+a1
u(x) = ((y+s*x+a2)y+a3)a4.
```

Položme `v_j=u_j/u4`. Koeficienty po roznásobení postupně určují

```
a0=(v3-s)/2,  b=v2-a0(a0+s),  a1=s(v1-a0*b),
a2=b-2a1,  a3=v0-a1(a1+a2),  a4=u4.
```

Koeficient u3 určuje a0, u2 určuje součet 2a1+a2 a koeficient u1
pak určuje a1. Konstantní člen určuje a3. To dává (10) i odpověď 18.
Vyhodnocení má 3M+5A proti Hornerovým 4M+4A. Zrychlení tedy závisí
na cenách operací; samotný součet je v obou případech osm.

Fikeho změna proměnné má smysl jako `t=|u4|^(1/4)x` a nové koeficienty
`u_j/|u4|^(j/4)`. Vedoucí koeficient v proměnné t je pak ±1.
Nejde o tvrzení, že dosazení zvětšeného argumentu do nezměněného u
normalizuje vedoucí koeficient. Poznámku o přesnosti obou znamének
čteme jako závislost na konkrétních datech, ne jako záruku pro každé x.

Pro stupeň pět nejprve normalizujeme u5 na 1. Nechť t je reálný kořen

```
C(t)=40t^3-24u4*t^2+(4u4^2+2u3)t+u2-u3*u4.
```

Existuje, protože jde o reálnou kubiku s nenulovým vedoucím členem.
Odpověď 19 určuje `a0=t`, `a3=u4-4t`,
`a1=u3-4t*a3-6t^2`,
`a2=u1-t(t*a1+4t^2*a3+2a1*a3+t^3)` a
`a4=u0-a3(t^4+a1*t^2+a2)`.
Přímé roznásobení schématu (11), s a5=1, dává přesně

```
hodnota schematu - u(x) = -x^2 C(t).
```

To dokazuje všechny koeficientové rovnice současně, včetně případu
násobného kořene C. Původní u5 se vrátí posledním násobením.
Počet je 4M+5A. Zadaná kubika je `40t(t-1)(t-2)` a všechny tři
vytištěné šestice parametrů přesně souhlasí.

Program v odpovědi 20 se čte po sloupcích. Po prvním STA je
`TEMP1=x+a3`. Přičtení předpočítaného `a0-a3` dá `x+a0`;
další dvě STA a FMUL vytvoří `TEMP2=(x+a0)^2`. Zbytek je schéma (11).
Přesný interpreter kontroluje celý tok dat a počty
1 LDA, 3 STA, 5 FADD, 4 FMUL. V plovoucí řádové čárce může
`(x+a3)+(a0-a3)` zaokrouhlit jinak než `x+a0`; úloha dovoluje
malé změny schématu a identické zaokrouhlení nepožaduje.

## 3. Knuthovo schéma stupně šest a úloha 21

Normalizujme u6 na 1 a označme beta1,…,beta8 z (13)–(14) jako b1,…,b8.
Při `b6=t` mají dva násobené kubické polynomy jednoduchý tvar:

```
w       = x^3+b1*x^2+t*x+b7,
w+z+a4  = x^3+(b1+1)x^2+(b2-t)x+b8.
```

Platí `b7=t^2+b4*t+b5`, `b8=b3-t-b7`.
První rovnice pro b1,b2,b3 nastavují koeficienty x5,x4,x3.
Rovnice pro b4,b5,b7 pak nastavují koeficient x2. Zbývající
koeficient x vyžaduje právě kubiku (13); konstantní člen napraví
`a5=u0-b7*b8`. Tato kubika má vedoucí koeficient 2, a tedy vždy
reálný kořen. Symbolický zbytek každého koeficientu modulo tuto
kubiku je nulový. Počet ve (12) je 4M+7A.

U zadaného příkladu je kubika `2(t-2)(t-3)(t+1)`.
Pro kořen 2 vyjde dvojí `x+3`, takže společný výsledek lze použít
dvakrát. S a6=1 tím skutečně získáme 3M+6A. Kořeny 3 a −1 dávají
obě další řešení z odpovědi 21; všech sedm koeficientů souhlasí.

## 4. Panovo schéma, úloha 22 a C0236

Pro monický sextický polynom označme `a0=u5/3` a

```
D = u3-2a0*u4+5a0^3,
N = u1-a0*u2+a0^2*u3-a0^3*u4+2a0^5.
```

Vzorec (17) předepisuje `a1=N/D`. Necháme-li ale a1 volné a
ostatní parametry vypočteme podle (19), přesná identita je

```
hodnota schematu (16) - u(x) = (D*a1-N)x.
```

Je to také úplná podmínka: porovnání vyšších koeficientů nejprve
vynutí a0=u5/3 a vztahy (19); nad reálnými čísly lze potřebné
rovnice pro a2,a3 dělit dvěma. Zbývá právě `D*a1=N`.

- D nenulové: jediná volba a1=N/D, přesně jako v knize.
- D=0, N nenulové: schéma (16) daný polynom nereprezentuje.
- D=N=0: libovolné reálné a1 a (19) dávají reprezentaci.

Podmínka (18) je po odnormalizování násobkem D, konkrétně
`27u6^3 D`. Je tedy správným předpokladem vytištěného podílového
vzorce. Doslovné tvrzení, že samotné (16) lze použít pouze při
nenulové (18), však vynechává třetí možnost. Nejkratší příklad:

```
u=x^6-x^4,  a0=a1=a2=a3=a4=a5=0,  a6=1,
z=x^2,  w=x^2+x,  u=((z-x)w)z.
```

Obecně každý sudý monický sextický polynom
`x^6+u4*x^4+u2*x^2+u0` má D=N=0 a lze vzít
`a0=a1=0`, `a2=a3=(u4+1)/2`, `a4=u2-a2*a3`, `a5=u0`.
Naproti tomu `x^6+x` má D=0,N=1 a schéma opravdu neexistuje.

**C0236 zůstává candidate.** Algebraický rozdíl je doložen;
redakční závažnost závisí na tom, zda „Pan's method“ v dané větě
znamená celý předpis včetně dělení (17), nebo samotnou identitu (16).
Bezpečná úprava by omezila nutnost podmínky na výpočet podle (17).

U úlohy 22 vyjdou parametry `(-1,1,0,-4,4,-2,1)`.
Zjednodušené `w=x^2+1`, `z=w-x` opravdu ušetří jedno A:
vytištěná specializace má 3M+7A, upravená 3M+6A.
Obecné schéma (16) má 4M+8A. V modulární aritmetice fungují tytéž
identity, pokud jsou všechny použité dělitele jednotkami: pro (9)
stačí invertibilní 2u4, pro (16) invertibilní 6u6 a D. Navazující
obecné tvrzení z úlohy 44 zůstává předmětem pozdějšího bloku.

## 5. Eveovo lemma a C0235: směry v odpovědi 23

Nechť f je reálný polynom stupně n. Jeho část g obsahuje mocniny
stejné parity jako n, část h ostatní mocniny, takže f=g+h.
Předpokládejme h nenulové a alespoň n−1 kořenů v uzavřené pravé
polorovině. Kořeny vždy počítáme s násobnostmi. „Imaginární“ zde
zahrnuje nulu: jde o kořeny s nulovou reálnou částí.

Nejprve odstraníme případné kořeny na imaginární ose. Faktor z
vytkneme z f,g,h; nenulový kořen ib dává společný faktor z²+b².
Po dělení je stále splněn předpoklad o všech kořenech až na jeden.
Indukce tedy vrací požadované počty i s násobnostmi. Stupně n<2
jsou triviální. Dále předpokládáme, že na ose není žádný kořen.

Podél celé osy existuje spojitě zvolený argument `phi(t)=arg f(it)`.
Argument je úhel komplexního čísla, zde sledovaný spojitě bez skoků
o 2π. Kořen `rho=a+ib`, a nenulové, přispívá k jeho derivaci

```
d arg(it-rho)/dt = -a/(a^2+(t-b)^2).
```

Integrál přes reálnou osu je −π pro a>0 a +π pro a<0.
Jsou-li L a R počty kořenů vlevo a vpravo, celková změna
argumentu je `π(L-R)`. Protože L≤1, jde o −nπ nebo −(n−2)π.
Koncové směry při t→±∞ leží na ose určené paritou vedoucího členu.
Spojitost argumentu vynutí nejméně n−2 průchodů opačnou osou
a nejméně n−3 průchodů stejnou osou, mezi koncovými směry.
První odpovídají nulám g(it), druhé nulám h(it). Nevyžadujeme
monotonicitu celé phi: každý mezilehlý úhel je dosažen aspoň jednou.
Tím je dokázána část (a).

Reálné koeficienty a parita znamenají, že kořen a+ib s a,b nenulovými
by vyvolal čtveřici ±a±ib. Ale g má stupeň n a již alespoň n−2
kořenů na ose; h má stupeň nejvýše n−1 a alespoň n−3 na ose.
U obou tedy zbývají nejvýše dvě místa. Čtveřice je nemožná.
Všechny kořeny g,h jsou reálné nebo imaginární a jejich čtverce
jsou reálné. To dokazuje (b), včetně násobných kořenů.

**C0235 confirmed:** odpověď 23(a) na straně 702 říká, že
`f(R exp(it))`, π/2≤t≤3π/2, obíhá po směru hodinových ručiček,
a `f(it)`, −R≤t≤R, proti směru. Oba směry jsou obráceně.
Obr. 16 na straně 517 ukazuje kladně orientovaný obvod levého
půlkruhu, v souladu s parametrizací. Na kruhovém oblouku vedoucí
člen dává změnu argumentu přibližně +nπ, tedy proti směru hodin.
Po imaginární ose je čistá změna záporná podle předchozího důkazu.

Pro konkrétní f(z)=(z−1)^4, které nemá žádný kořen na ose, platí
`d arg f(it)/dt=-4/(1+t^2)<0`. Příklad tak splňuje všechny
předpoklady a jednoznačně vyvrací tištěný směr. Stačí zaměnit
slova clockwise a counterclockwise; počty kořenů i závěr zůstávají.

## 6. Věta E, úplná volba posunu a C0237

Používáme **opravené** `m=ceil(n/2)-1`, n≥3.
Položme `p(X)=u(X-c)=sum(a_j X^j)`. Lichou část p zapíšeme
`X q(X²)`, tedy

```
q(W)=a_(2m+1) W^m + ... + a3 W + a1.
```

Zbytek při dělení p výrazem X²−alpha má koeficient u X právě
q(alpha). Je konstantní právě tehdy, když q(alpha)=0.
Opakováním dělení vznikne schéma (20) právě tehdy, když
q je nulové nebo má stupeň m a m reálných kořenů s násobnostmi.
V nulovém případě p i všechny podíly zůstanou sudé a libovolné
takové dělení má konstantní zbytek. Pro liché n se nulové q
nevyskytne, protože jeho vedoucí koeficient je u_n.

Eveovo lemma z oddílu 5 dává reálné kořeny q po vhodném posunu.
Zbývá zařídit zároveň kvadratický faktor p, aby poslední beta_m
byla nula, a u sudého n ohlídat stupeň q.

Seřaďme reálné části kořenů u vzestupně jako r1,…,rn.
Z dolního konce zvolíme následující pár:

- Je-li nejnižší kořen nereálný a±ib, vezmeme jeho sdružený pár.
- Je-li nejnižší reálný a druhý nereálný, vezmeme sdružený pár druhého.
- Jsou-li dva nejnižší reálné, napíšeme je a−b,a+b.

V prvních dvou případech dá c=−a imaginární pár a alpha_m=−b²;
ve třetím dá c=−a reálný symetrický pár a alpha_m=b².
Po posunu je nejvýše jeden kořen vlevo. Stejná konstrukce od
horního konce má nejvýše jeden kořen vpravo. Obě varianty zajišťují
kvadratický faktor X²−alpha_m a beta_m=0. Při shodných reálných
částech smíme volit pořadí v rámci shody.

Pro sudé n je `a_(n-1)=0` právě tehdy, když střed zvoleného páru
je roven průměru reálných částí všech kořenů, označenému A.
Dolní střed leží v [r1,r2], horní v [r_(n−1),rn]. Kdyby oba
byly A, musely by všechny prostřední reálné části být A.
Buď jsou i oba krajní A, takže po posunu jsou všechny kořeny
imaginární a p je sudé; nebo r1<A<rn a průměr vynutí r1+rn=2A.
V druhém případě jsou krajní kořeny reálné (jinak by jejich
sdružené protějšky tvořily další krajní kořeny). Je-li mezi
prostředními nějaký reálný kořen A, volba tohoto kořene jako
druhého nejnižšího dá střed menší než A, tedy nenulové a_(n−1).
Pokud žádný takový není, prostřední kořeny se po posunu seskupí
do čistě imaginárních sdružených párů a krajní jsou ±b; opět je p
sudé. Tím je úplně doložena výjimka q=0 pro sudý stupeň.

**C0237 confirmed:** závěrečná věta důkazu na straně 494 tvrdí
bez omezení parity, že některá z popsaných voleb má a_(n−1)
nenulové, ledaže q=0. Pro `u(x)=x^3+x` mají všechny kořeny
0,±i stejnou reálnou část. Každá popsaná volba má c=0, a2=0,
ale q(W)=W+1 není nulové. Větu je třeba omezit na sudé n;
u lichého n je potřebný vedoucí koeficient q vždy u_n.
Věta E samotná je správně: příklad vyhodnotí `x(x²+1)`.

Pro kontrolu počtu operací: počáteční y=x+c a w=y² stojí A+M.
Počáteční z stojí pro sudé n 2M+2A, pro liché n M+A.
Dalších m faktorů stojí mM+2mA, ale beta_m=0 šetří poslední A.
Celkem dostáváme `floor(n/2)+2` násobení a n sčítání, jak je uvedeno.

## 7. Úloha 24

Pro zadaný polynom mají dvě vytištěné volby tyto parametry:

| c | alpha0 | beta0 | alpha1 | beta1 | alpha2 | beta2 |
|---|---|---|---|---|---|---|
| 2 | 6 | 16/3 | 1/3 | −74/9 | −1 | 0 |
| 4 | −6 | 12 | −3 | −26 | 9 | 0 |

První posun dává `q(W)=6(W+1)(W−1/3)` a podíl po posledním
faktoru `X^4+6X^3+5X²−2X−10`. Druhý posun dává druhou řádku
tabulky. Přesné roznásobení obou celých schémat vrací původní
součin čtyř faktorů. Pro c=3 má q(W)=20W+20 místo požadovaného
stupně dva; není nulové, takže tato volba skutečně nefunguje.

## 8. Zdroje, errata a hranice uzavření

Prohledány všechny šestice relevantních vrstev: all2-prepre,
all2-pre, all2, err2, err2-2e a zdrojový err2.textxt. Výpis stránek
je v sources/polyeval-adapt-errata.txt; navíc proběhlo hledání
clockwise, counterclockwise, Eve, Pan, denominator a identically zero.
U druhého vydání byly přečteny také odpovídající změny stran
474–475 a okolí odpovědí 640–647. Opravu C0235/C0237 ani řešení
výjimky C0236 jsme v těchto vrstvách nenašli.

Známé změny: 7. 6. 1999 opravuje stranu 493 na `ceil(n/2)-1`;
29. 4. 2013 mění na straně 490 hodnocení úspory na hodnocení změny.
Starší erratum z 11. 11. 1985 měnilo počet m ve druhém vydání
na chybný ceil(n/2), který byl převzat do prvního dotisku třetího.
Oprava odpovědi 16 z 25. 3. 2001 nespadá do nynějších úloh.

Eveův původní článek, Numerische Mathematik 6 (1964), 17–21,
byl získán z GDZ a všech pět stran vizuálně přečteno. PDF má
vlastní úvodní list, takže tištěná 17 odpovídá souborové straně 2.
Jeho metoda používá index racionální funkce podél osy; náš důkaz
v oddílu 5 se opírá přímo o změnu argumentu a na tomto externím
indexovém pravidle nezávisí. Článek dokládá příslušnou atribuci;
jeho vlastní číselný příklad stupně osm zde nebyl přepočítán.

Caltech potvrzuje bibliografii Knuthova článku z roku 1962,
ale záznam je pouze metadatový a ACM PDF vrátilo HTTP 403.
Panův přehled z roku 1966 je přístupný přes webový nástroj,
lokální stažení vrátilo 403. Přečteny byly úvodní historické
poznámky a bibliografie, nikoli celý matematický obsah přehledu.
Jeho vlastní bibliografie uvádí Problemy Kibernetiki 5 (1961),
17–29, v souladu s knihou; Eve uvádí 1959. Tento rozpor není
nález proti Knuthovi. Primární vydání tohoto Panova článku,
Panův článek o praktických parametrech z roku 1963, Fike 1967
a původní Motzkin/Todd zůstávají historickou mezerou sekce.

Potvrzení nálezů se vztahuje k našemu skenu a prohledaným erratům.
Pozdější fyzický dotisk ani prvenství nejsou doloženy. Žádné
hlášení nebylo odesláno. Celý svazek ani celá §4.6.4 nejsou uzavřeny.

## 9. Reprodukovatelnost

`verify_polyeval_adapt.py` má tři samostatně checkpointované bloky.
Všechny prošly bez chyby; běh session93624, limit 180 sekund na blok.
Vlastní časy: low_degrees 0.195088303 s, sextics 0.536526272 s,
eve 0.259916193 s. PID výpočtů 1595155,1595159,1595161;
PID obalů a časy včetně startu Pythonu jsou v run.json.
Úspěšné bloky neopakovat bez nové konkrétní pochybnosti nebo změny.

Symbolické rovnosti jsou doplňkem rozepsaných důkazů, nikoli
náhradou obecného důkazu o kořenech. Výstupy, zdroje, původní
stránky a neodeslané návrhy hlášení propojuje manifest
sources/polyeval-adapt.json.
