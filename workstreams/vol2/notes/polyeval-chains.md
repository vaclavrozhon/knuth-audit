# Polynomiální řetězce a dolní meze: §4.6.4, úlohy 25–31

V2-X0078, 4. listopadu 2026. Uzavřený matematický rozsah tvoří
definice na straně 494 od „Polynomial chains“, strany 495–496
a dokončení věty o algebraicky nezávislých koeficientech na začátku
497; dále úlohy 25–31 na 517–518 a odpovědi 702–703.
Externí kvantitativní meze na straně 497 a maticové algoritmy
498–499 do tohoto uzavřeného bloku nepatří.

Věty M, A a C a řešení úloh jsou správné. C0238 potvrzuje
nesprávný rozklad množiny výsledků v důkazu A. Níže uvádíme
opravený úplný důkaz, který se obejde bez rozdělování výjimek.

## 1. Definice a význam stupňů volnosti

**Polynomiální řetězec** je konečná posloupnost hodnot začínající
proměnnou x. Každý další krok sečte, odečte nebo vynásobí dvě
starší hodnoty, případně jednu starší hodnotu a nový reálný
parametr. U kroku se dvěma staršími hodnotami je dovoleno také
znaménko minus před prvním operandem. Takový krok nazýváme
řetězcový; krok s novým parametrem parametrický.
Konečný výstup je polynom v x, jehož koeficienty jsou celočíselné
polynomy v parametrech. To plyne indukcí podle jednotlivých kroků.

Nechť N je největší formální stupeň výstupu. Množina výsledků R
obsahuje všechny vektory jeho koeficientů `(q_N,...,q_0)`, když
parametry probíhají všechna reálná čísla. Zahrnuje také výstupy
nižšího stupně a nulový polynom. Pouze při konkrétním tvrzení
„stupně n“ vyžadujeme, aby příslušný vedoucí koeficient byl nenulový.

Definice knihy říká, že R má **nejvýše t stupňů volnosti**, pokud
pro každý výběr t+1 různých souřadnic existuje nenulový polynom
s celočíselnými koeficienty, který na těchto souřadnicích všech
prvků R vymizí. Jinými slovy, libovolných t+1 souřadnic splňuje
nějakou pevnou algebraickou relaci. To je zde přesná definice;
není třeba zavádět obecnou teorii geometrické dimenze.

Vlastnost se přenáší na podmnožiny. Z nejvýše t stupňů volnosti
plyne nejvýše t+1: na větším výběru souřadnic použijeme relaci
na jeho podvýběru. Pro větší t než počet souřadnic je definice
prázdným požadavkem, což nezpůsobuje problém v používaných mezích.

## 2. Úlohy 27–29: elementární algebraické základy

Nenulový reálný polynom se nemůže rovnat nule ve všech bodech.
Pro jednu proměnnou má nejvýše tolik kořenů, kolik je jeho stupeň.
Indukčně vybereme hodnoty všech proměnných kromě poslední tak,
aby některý nenulový koeficient jako polynom v poslední proměnné
zůstal nenulový; pak použijeme případ jedné proměnné.

**Úloha 27.** Pokud R obsahuje všechny vektory s q_n nenulovým
a mělo by nejvýše n stupňů volnosti, existoval by nenulový
celočíselný polynom g ve všech n+1 souřadnicích, který na R
vymizí. Součin q_n*g je ale nenulový polynom (součin dvou
nenulových polynomů nad reálnými čísly je nenulový), který
vymizí všude: při q_n=0 i při q_n nenulovém. To je spor.

**Úloha 28.** Máme s+1 polynomů f0,…,fs s celočíselnými
koeficienty v s proměnných alpha.
Označme D největší z jejich stupňů. Součiny

```
f0^e0 ... fs^es,   e0+...+es <= k,
```

tvoří seznam délky `binom(k+s+1,s+1)` a leží ve vektorovém
prostoru polynomů v alpha stupně nejvýše Dk. Tento prostor má
dimenzi `binom(Dk+s,s)` nad racionálními čísly. Pro dostatečně
velké k je první počet větší: roste jako k^(s+1), druhý jako k^s.
Existuje tedy netriviální racionální lineární závislost mezi
uvedenými součiny. Po vynásobení společným jmenovatelem dostáváme
nenulový celočíselný polynom g s `g(f0,...,fs)=0`.
Je-li D=0, stačí `g(X0,...)=X0-f0`; případ s=0 je stejný.

Každý výběr s+1 koeficientů výstupního polynomu je takovou
soustavou f0,…,fs. Proto řetězec se s parametry má nejvýše
s stupňů volnosti. Pro samotný důkaz není nutný citovaný
van der Waerdenův aparát algebraické závislosti.

**Úloha 29.** Pro vybraných t+1 souřadnic vezměme relace g_j
pro konečně mnoho množin R_j. Jejich součin je nenulový
celočíselný polynom a vymizí na celé unii. Konečná unie proto
zachovává stejnou mez. Nekonečný součin tento důkaz neposkytuje.

## 3. Věta M a ostřejší úloha 30

Označme m_c počet řetězcových násobení, m_p počet parametrických
násobení a m jejich součet. Vyjmenujme všechny výsledky násobení
chronologicky jako mu1,…,mu_m. Mezi násobeními se pouze sčítá
a odčítá, takže oba operandy každého násobení a konečný výstup
jsou celočíselné lineární kombinace starších mu, proměnné x
a původních parametrů. Oddělíme poslední část jako beta_j:

```
mu_i = (T_(2i-1)+beta_(2i-1))(T_(2i)+beta_(2i)),
u = T_(2m+1)+beta_(2m+1).
```

Každé T_j je celočíselná lineární kombinace starších mu a x;
beta_j je celočíselná lineární kombinace původních parametrů.
Když beta prohlásíme za nezávislé parametry, množina výstupů
se může zvětšit, ale stále obsahuje původní R. To dává zatím
nejvýše 2m+1 stupňů volnosti.

Následující eliminace provádíme **chronologicky**. Pokud krok
i odpovídá parametrickému násobení, můžeme jeho levý operand
zapsat jako beta_(2i−1), tedy T_(2i−1)=0. Označme A tuto beta
a B pravou beta. Identita

```
A(T+B) = A*T + A*B
```

dovoluje položit B=0 a konstantní opravu A*B přenést do všech
pozdějších beta_j: obsahuje-li T_j člen c*mu_i, přičteme c*A*B.
Stejně opravíme výstupní konstantu. Jeden volný parametr tak
zmizí. Přenos do budoucích kroků neovlivní již odstraněné beta.

Je-li m_c kladné, uvažujme první řetězcové násobení. Všechny
předchozí násobicí výstupy po právě popsaných eliminacích jsou
násobky x bez konstantního členu. První řetězcové násobení tedy
má tvar `(g1*x+A)(g2*x+B)`, kde g1,g2 závisejí jen na dřívějších
parametrech. Pro g1 nenulové použijeme

```
(g1*x+A)(g2*x+B) = g1*x*(g2*x+B+g2*A/g1) + A*B.
```

Nahradíme B novým parametrem, A položíme rovno nule a konstantu
A*B opět přeneseme do budoucích beta. Výsledná rodina je
polynomiálně parametrizovaná: podíl g2*A/g1 slouží jen k přiřazení
hodnot novému volnému parametru, ne jako operace jejího výstupu.

Na výjimečné větvi g1=0 máme místo toho
`A(g2*x+B)=A*g2*x+A*B`; odstraníme B. Pro zastřešující
polynomiální rodinu nastavíme první x-část tohoto operandu
identicky na nulu a ostatní parametry necháme volné. Může obsahovat
více výstupů než původní výjimečná větev, což pro horní mez
nevadí. Obě větve mají o jeden parametr méně. Úloha 29 dovoluje
jejich konečnou unii. Pozdější parametrická násobení odstraníme
stejným chronologickým postupem, takže se jejich úspory nesčítají
s již neplatnou mezireprezentací.

Celkem z 2m+1 parametrů odstraníme m_p a, pokud m_c>0, ještě
jeden. Výsledná mez je

```
2m_c + m_p + [m_c=0],
```

kde hranatá závorka má hodnotu 1 při splnění podmínky a 0 jinak.
To je přesně úloha 30. Pokud m>0, je tato mez nejvýše 2m:
pro m_c=0 použijeme m+1≤2m, jinak 2m_c+m_p≤2m.
Tím je dokázána věta M i její výjimka m=0.

## 4. Věta A a C0238

Nechť q je počet sčítání a odčítání. Vyjmenujme jejich výsledky
chronologicky jako kappa1,…,kappa_q. Mezi nimi se jen násobí,
takže každý operand je až na znaménko součin dřívějších kappa,
x a původních parametrů. Oddělme `T_j=A_j B_j`, kde A_j je
součin parametrů a B_j součin x a kappa. Prázdný součin je 1.

Pokud jsou původní parametry nenulové, lze při každém sčítání
vytknout A_(2i−1), zavést `beta_i=A_(2i)/A_(2i−1)` a příslušně
upravit konstantní násobitele pozdějších výskytů kappa_i.
Předposlední normalizované výstupy jsou polynomy v beta a x;
poslední celkový násobitel výstupu přidá beta_(q+1).
Dostáváme polynomiální rodinu v q+1 parametrech obsahující všechny
původní výstupy pro nenulová alpha. Úloha 28 dává pro každých
q+2 souřadnic nenulovou celočíselnou relaci g.

**Opravené dokončení důkazu.** Koeficienty původního řetězce jsou
polynomiální, a tedy spojité funkce všech alpha. Každé zadání
s nulovými alpha je limitou zadání se všemi alpha nenulovými.
Dosadíme-li do g tyto koeficienty, dostáváme spojitou funkci
nulovou na husté množině; je tedy nulová všude. Každá nalezená
relace platí na celém R. Věta A, nejvýše q+1 stupňů volnosti,
je dokázána i pro nulové parametry. Pro q=0 zbývá přímo jediný
celkový koeficient před mocninou x, takže argument platí také.

**C0238 confirmed.** Kniha na straně 496 tvrdí
`R=R1 union ... union Rq union R'`, kde R_i odpovídá
`A_(2i−1)=0` a R' všem původním alpha nenulovým. Tato rovnost
obecně neplatí. Vezměme přípustný řetězec

```
lambda0=x,
lambda1=lambda0+lambda0,
lambda2=a*lambda1.
```

Má q=1 a jediný parametr a. Při normalizaci jediného sčítání
jsou A1=A2=1, protože oba operandy jsou x a nemají parametrický
násobitel. R1 je tedy prázdné. R' obsahuje právě nenulové
násobky x, zatímco R obsahuje i nulu pro a=0. Nulový výstup
je legitimní součástí definovaného R.

Rozklad lze opravit definicí R' pomocí nenulovosti skutečných
dělitelů A_(2i−1), nikoli všech původních alpha. Pro plně
jednoznačnou organizaci výjimečných větví lze použít první nulový
dělitel v chronologickém pořadí. Důkaz spojitostí uvedený výše
se těmto větvím zcela vyhýbá. Výsledek věty se nemění.

## 5. Věta C, monické polynomy a řetězec (27)

Pro obecný polynom stupně n≥2 potřebuje množina výsledků
alespoň n+1 stupňů volnosti ve smyslu úlohy 27. Bez násobení
nevznikne stupeň alespoň dva. Z věty M proto `2m≥n+1`, tedy
`m≥floor(n/2)+1`; z A plyne `q+1≥n+1`, tedy q≥n.
Úloha 29 rozšíří závěr také na libovolnou konečnou kolekci
řetězců nesplňujících některou z těchto mezí.

Koeficienty jsou **algebraicky nezávislé nad racionálními čísly**,
pokud nesplňují žádnou nenulovou celočíselnou polynomiální relaci.
Každá taková konkrétní sada proto vyžaduje stejné meze. U
racionálních koeficientů algebraická nezávislost není splněna;
tento argument sám o sobě neurčuje jejich individuální složitost.

**Úloha 31.** K řetězci pro všechny monické polynomy stupně n
přidáme jediné závěrečné násobení novým parametrem. Tím získáme
všechny polynomy stupně n s nenulovým vedoucím koeficientem.
Věta C proto dává původně nejméně floor(n/2) násobení a n
sčítání. Pro n=1 je násobicí mez triviální a bez sčítání nelze
vytvořit x+b pro b nenulové; pro n=0 jsou obě meze nulové.

Pro liché n=2h+1≥3 má (27) h iterací. Úvodní kroky spotřebují
jedno A, jedno řetězcové M a jedno parametrické M; každá iterace
další dvě parametrická A a jedno řetězcové M. Celkem tedy
h+2 násobení, 2h+1 sčítání, h+1 řetězcových kroků a n+1
parametrických kroků, přesně jako v knize. Jde o schéma E:
konstantu před posledním nulovým beta lze přesunout před
příslušné násobení. Přesněji iterace má tvar
`z <- (z+b_i)(w-a_i)`, což rozbalí stejné vnoření jako E
s beta_m=0, když b1=beta0 a b_i=beta_(i−1) pro i>1.

## 6. Úlohy 25 a 26

V úloze 25 se používají původní názvy parametrů, včetně mezer
v číslování. Čtyři násobicí výstupy jsou lambda4,lambda7,
lambda8,lambda9. Jejich operandy a konečný součet dávají

```
beta1=alpha2, beta2=2alpha1, beta3=alpha7, beta4=alpha6,
beta5=beta6=0, beta7=alpha1, beta8=0, beta9=2alpha1-alpha8.
```

Výstup je `2alpha2(x+alpha1)^2+2(x+alpha1)-alpha8`.
Lambda7 a lambda8 jsou v příkladu zbytečné, ale zachováváme je
při kontrole všech čtyř násobení. Odpověď přesně souhlasí.

V úloze 26 je Hornerův výstup
`alpha1*x^3+alpha2*x^2+alpha3*x+alpha4`. Normalizovaný řetězec
má kappa1=1+beta1*x, kappa2=1+beta2*kappa1*x,
kappa3=1+beta3*kappa2*x a výstup beta4*kappa3.
Pro nenulové dělitele dostaneme

```
(beta1,beta2,beta3,beta4)
  = (alpha1/alpha2,alpha2/alpha3,alpha3/alpha4,alpha4).
```

Jeho koeficienty od konstantního po kubický člen jsou
`beta4`, `beta3*beta4`, `beta2*beta3*beta4`,
`beta1*beta2*beta3*beta4`. Nulovost kteréhokoli koeficientu
vynutí nulovost kubického. Například x³+1 je v původní rodině,
ale není v normalizované. To odpovídá upozornění před chybným
rozkladem R; samo o sobě nejde o chybu v úloze 26.

## 7. Evidence a hranice

Vizuálně prohlédnuty strany 494–497, 517–518 a 702–703;
uzavřený rozsah na straně 497 je pouze dokončení první věty.
Errata all2-prepre, all2-pre, all2, err2, err2-2e a err2.textxt
prohledána podle stránek i pojmů o parametrech a množinách výsledků.
Změna z 13. 9. 2019 se týká formulace předchozího odstavce
na straně 496, nikoli chybné rovnosti R. Oprava C0238 nenalezena.
Starší oprava z 5. 7. 1997 mění v úloze 25 lambda7 na násobení;
náš třetí první dotisk už obsahuje správné násobení. Oprava
lambda_j na lambda_i v odpovědi 34 z roku 2000 patří do dalšího bloku.

Belagův článek DAN123(5),775–777(1958) byl přečten jako webový
text primárního PDF; strana 777 výslovně uvádí n aditivních
operací, takže atribuce roku 1958 je doložena. Lokální stažení
PDF vrátilo403. Panův přehled1966 byl pro tento blok čten v části
o počtu parametrů; použitý důkaz v oddílech2–5 je rozepsán zde
samostatně. Nejde o audit celého tohoto přehledu.

Motzkinův původní abstrakt je zatím nedostupný; metadata Crossref
určují článek o výroční schůzi, v němž je otištěn. Belaga1961
zůstává nepřečtený, stažení celého sborníku běží samostatně.
Tyto historické mezery jsou výslovně otevřeny v manifestu
sources/polyeval-chains.json.
Sazba knihy zůstává třetí vydání/první dotisk1997, pozdější
fyzický dotisk a prvenství C0238 neověřeny. Hlášení neodesláno.

`verify_polyeval_chains.py` prošel jednou, PID1596703,
čas0.238942888s, obalPID1596702/0.854957728s,limit180s,exit0.
Kontroluje všechny čtyři mezivýstupy úlohy25, obecnou substituci
úlohy26, čtyři normalizační identity, indexy(27) pro n3,5,7,9,11
a tři nezávisle nalezené celočíselné algebraické relace.
Poslední relace je netriviálního stupně4 pro soustavu
`a²+b, ab, b²+a`; po nalezení racionálním nulovým prostorem
je ověřena přímým dosazením. Žádná konečná kontrola není
vydávána za důkaz obecné dolní meze. Úspěšný blok neopakovat.
