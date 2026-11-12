# Prahové cofactors, obě váhové identity a Chowova věta

7. listopadu 2026. §7.1.1 p76/file93 a Theorem T na p77/file94,
P1057–P1065, X0113. Obě původní stránky zobrazeny. Převzaty pouze
přesné hotové výsledky: všech 12 funkcí v proof-074, všech 81 funkcí
a jejich sedm prahových reprezentantů v proof-079, padding v proof-083.
Žádný program, prohledávání 64 případů ani milionu vstupů.

## 1. Zrušení hlasů a čistá většina

Přidání jedné nuly a jedné jedničky zvýší délku lichého mediánu
z 2t−1 na 2t+1 a počet jedniček i jeho práh právě o jednu. Tím
je obecně dokázáno (85), i když se některé vstupní proměnné opakují.

Z proof-083 máme v (81) ab=0. Nahradíme proto všechny a+b konstant
jedinou proměnnou x_0 a dostaneme přesně (86). Je-li a>0, dosadíme
x_0=0; je-li b>0, x_0=1. Při a=b=0 je x_0 nepodstatná a lze
dosadit obojí. Tím vznikne čistá lichá většina bez konstant.
Je monotónní, protože zvýšení bitu nemůže snížit počet jedniček,
a self-duální: při liché délce L se počet jedniček k doplní na
L−k, takže právě jedna z těchto hodnot převýší L/2.

Opačně má cofactor každé čisté většiny s násobnostmi c,w_1,…,w_n
tvar [Σw_j x_j ≥ (c+Σw_j+1)/2 − c x_0]. Je tedy pozitivně prahový.
Obecné záporné váhy se předtím odstraní změnou polarit z proof-083.
Výrok „znát všechny“ tedy znamená tyto explicitní převody, nikoli
bijekci mezi počty reprezentací. Nulové váhy dovolují vynechat
nepodstatné proměnné; konstantní funkce vzniknou z projekce x_0.

## 2. Každý z dvaceti vytištěných cofactorů

Všech 12 čistých čtyřproměnných většin je již doloženo v proof-074.
Po dosazení w=0/1 jsou přesně tyto funkce v pořadí (87). Tabulka
uvádí všechny minimální jedničkové podpory; tím ověřuje hodnoty
na všech vstupech i odlišnost všech dvaceti funkcí. Zápis xy zde
označuje podporu {x,y}, nikoli další proměnnou.

| Medián z (87) | Minimální jedničkové podpory |
|---|---|
| ⟨0⟩ | žádná |
| ⟨1⟩ | ∅ |
| ⟨00xyz⟩ | xyz |
| ⟨11xyz⟩ | x, y, z |
| ⟨0yz⟩ | yz |
| ⟨1yz⟩ | y, z |
| ⟨0xyzz⟩ | xz, yz |
| ⟨1xyzz⟩ | z, xy |
| ⟨xyz⟩ | xy, xz, yz |
| ⟨z⟩ | z |
| ⟨0xyyz⟩ | xy, yz |
| ⟨1xyyz⟩ | y, xz |
| ⟨y⟩ | y |
| ⟨0xz⟩ | xz |
| ⟨1xz⟩ | x, z |
| ⟨0xxyz⟩ | xy, xz |
| ⟨1xxyz⟩ | x, yz |
| ⟨x⟩ | x |
| ⟨0xy⟩ | xy |
| ⟨1xy⟩ | x, y |

Každý řádek plyne z porovnání počtu jedniček s polovinou liché
délky. Například x+y+2z≥3 znamená z∧(x∨y); po přidání stálé
jedničky x+y+2z≥2 znamená z∨(x∧y). Ostatní vážené řádky jsou
jen přejmenování téže analýzy. Zbylé řádky jsou konjunkce,
disjunkce, projekce nebo již dokázaná většina.

Úplnost není census: každá pozitivní prahová funkce tří proměnných
má podle §1 rozšíření na některou z oněch 12 funkcí. Čtyři z nich
jsou na w nezávislé (x,y,z,⟨xyz⟩); ostatních osm dává dva řádky.
Proto uvedených 4+2·8=20 řádků vyčerpává všechny možnosti.

## 3. Přesný počet150 bez nového censu

Označme Df(x)=1−f(¬x) dualitu a A množinu cofactorů g(0,x), kde
g probíhá všech 81 monotónních self-duálních funkcí pěti proměnných
z proof-079. V tomtéž důkazu má každá z nich čistou většinovou
reprezentaci, včetně všech sedmi typů. Self-dualita určuje druhý
cofactor jednoznačně jako g(1,x)=D(g(0,x)), takže první cofactor
jednoznačně určuje celé g. Máme tedy |A|=81, nikoli jen≤81.
Množina druhých cofactorů je DA a má také81 prvků.

Pro f∈A dává monotónnost v x_0 nerovnost f≤Df. Je-li zároveň
f∈DA, dostaneme Df≤f, a tedy f=Df. Opačně každá monotónní
self-duální čtyřproměnná h leží v průniku: rozšíření g(x_0,x)=h(x)
je monotónní self-duální pětiproměnná funkce. Průnik A∩DA proto
tvoří právě 12 funkcí z proof-074. Podle §1 unie A∪DA dává
všechny pozitivní prahové funkce čtyř proměnných. Počet je přesně

    81+81−12=150.

Zde se nepřebírá otevřený šestiproměnný census P1026 a nic se
nepřepočítává. Použity jsou jen již dokázané strukturální klasifikace.

## 4. Obecná konečnost a konkrétní identita (88)

Pro pevné n existuje nejvýše 2^(2^n) bitových funkcí. Při n≥1
je vahových reprezentací nekonečně mnoho; například libovolná
kladná lichá násobnost jediné proměnné dává stále tutéž projekci.
Věta o ekvivalentních vahách proto platí bez jakéhokoli censu.

Vlevo v (88) jsou váhy (2,3,5,7,11,13), součet41 a práh21.
Vpravo jsou (1,2,2,3,4,5), součet17 a práh9. Porovnáme všechny
minimální vítězné podpory strukturálně. Jedinou vítěznou dvojicí
je v obou případech56: největší jiná dvojice46 má součet20,
respektive8. Trojice obsahující56 nejsou minimální.

Pro dvojice z prvních čtyř pozic máme:

| Dvojice | Původní váha | Nová váha |
|---|---:|---:|
|12|5|3|
|13|7|3|
|14|9|4|
|23|8|4|
|24|10|5|
|34|12|5|

S proměnnou6 potřebujeme alespoň8, respektive4: vyhoví přesně
14,23,24,34. S proměnnou5 potřebujeme alespoň10, respektive5:
vyhoví přesně24,34. Trojice bez5/6 nevyhoví. Žádná podmnožina
prvních čtyř pozic nevyhraje ani při použití všech čtyř: její
součet je17, respektive8. Ze čtveřic s6 obsahuje každá již
některou uvedenou vítěznou trojici. Ze čtveřic s5 pouze1235
neobsahuje dřívější vítěznou podmnožinu; její součet je21,
respektive9, takže vyhraje v obou reprezentacích. Každá množina
alespoň pěti pozic obsahuje56 nebo některou právě zkontrolovanou
vítěznou čtveřici/trojici.

Úplný shodný seznam minimálních podpor je tedy

    56, 146, 236, 246, 346, 245, 345, 1235.

Obě funkce jsou monotónní, proto tato shoda dokazuje (88) na
všech vstupech. Nebylo třeba zkoušet64 přiřazení.

## 5. Celá dvacetibitová identita (89)

Prahový řetězec je

    0110 0100 1000 0111 1110 = 0x6487e = 411774.

Součet binárních vah je2^20−1=1048575. Podle (82) dostaneme
b=1048576−2·411774=225028 a a=0, přesně vytištěnou první
většinovou reprezentaci. Její délka je1273603, práh636802,
tedy po odečtení b opět411774.

Malá reprezentace (89) má323 stálých jedniček a tyto váhy:

    (764,323,323,118,118,87,31,31,25,6,6,6,6,1,1,1,1,1,1,0).

Součet proměnných vah je1850. Medián má délku2173, práh1087,
a po odečtení323 je výsledným prahem764. Poslední proměnná je
opravdu nepodstatná; původní binární práh je sudý.

Pro obecné lexikografické porovnání s pevným řetězcem T platí:
je-li vstup větší, buď má všechny jedničkové pozice T, nebo při
prvním rozdílu na některé nulové pozici i obsahuje všechny
předchozí jedničkové pozice T a navíc i. Naopak každá taková
podpora a její nadmnožiny již vyhrají. Zde tak dostaneme tyto
postačující podpory a jejich malé váhy:

| Podpora | Váha |
|---|---:|
|1|764|
|234 nebo235|646+118=764|
|2367 nebo2368|646+87+31=764|
|2369i, i∈{10,11,12,13}|646+87+25+6=764|
|2369 a všechny pozice14..19|758+6=764|

Kandidát vzniklý nulovou pozicí20 obsahuje poslední řádek,
takže nepřidává podmínku. Tím jsou pokryty všechny pravdivé vstupy.

Každý menší řetězec má první rozdíl na jedničkové pozici j
prahu T. Je podmnožinou řetězce, který před j souhlasí s T,
na j má0 a za j samé1. Součty malých vah těchto horních
svědků všech nepravdivých vstupů jsou:

| j | Váha prefixu T před j + váha celého suffixu po j |
|---|---:|
|2|0+(1850−764−323)=763|
|3|323+(1850−764−323−323)=763|
|6|646+117=763|
|9|733+30=763|
|14≤j≤19|758+(j−14)+(19−j)=763|

Všechny malé váhy jsou nezáporné. Proto každý nepravdivý vstup
má součet≤763 a každý pravdivý≥764. To je úplný obecný certifikát
(89), včetně všech vytištěných násobností a vynechaného x_20.
Netvrdí minimálnost těchto vah; optimalizační postup je obsah103.

## 6. Index N,Σ a celý Theorem T

Pro x_1∨x_2 jsou pravdivé vektory01,10,11, tedy N=3 a Σ=(2,2),
jak je vytištěno. Pro obecnou dvojici f,g označme A={x:f=1,g=0},
B={x:f=0,g=1}. Shoda N dává |A|=|B|=k a shoda Σ dává
Σ_{x∈A}x=Σ_{y∈B}y. Má-li f celočíselný práh t, je při k>0

    w·Σ_A x ≥ kt > k(t−1) ≥ w·Σ_B y,

spor. Proto k=0 a f=g. Argument funguje i při nulových nebo
záporných vahách, pro konstantní f a v nulárním případě.
g nemusí být prahová funkce. Vytištěný důkaz používá pouze ostrou
nerovnost na nulové straně, takže platí také přímo pro reálné
parametry. Index tedy jednoznačně určuje prahovou funkci dokonce
mezi všemi bitovými funkcemi; algoritmus rekonstrukce z indexu se
tím ještě nedokazuje ani netvrdí.

## 7. Rozsah a přesné výjimky

P1065 drží partial pouze dopřednou větu na p76 o nalezení minimálních
vah metodou103. Konkrétní identity jsou prokázány; obecný lineární
a celočíselný optimalizační postup bude auditován v103. Proto zatím
nepovyšuji celou p76 a už vůbec ne celou p77 se symetrickými funkcemi.

Chowův přímý primární DOI10.1109/FOCS.1961.24 nešel v nástroji
otevřít; přesné bibliografické údaje34–38 a priorita zůstávají
výslovně přeskočené. Nejsou potřeba pro vlastní důkaz Theorem T.
Popis Murogovy monografie jako shrnutí oboru je bibliografické
hodnocení, které tento checkpoint znovu neověřuje. Prohledány
všechny vrstvy4A/F0 podle p76/77, Chow a obou číselných identit;
žádná relevantní matematická oprava ani nový rozpor.

Dodatek X0116: P1065 je nyní uzavřena úplným důkazem LP,
celočíselné parity a konečného větvení v
`notes/proof-087-selfdualization-integer-optimization.md`.
Společně tyto dvě poznámky uzavírají celý matematický obsah p76.
