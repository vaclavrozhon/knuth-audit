# §4.5.4 — závěrečné úlohy a návrat ke kryptografickému odkazu

6. listopadu 2026, V2-X0149. Párovány zbývající úlohy 38–43 a45–46
ze stran415–417 s úplnými odpověďmi665–671 a relevantními erraty.
Strany666–671 byly znovu přečteny obrazově; ostatní původní stránky
byly přečteny v předchozích blocích. Nově se vracíme k celé straně36,
jejíž kryptografický odkaz čekal právě na úlohu43. Jednotlivá tvrzení
mají adresy v results/sequential-factoring-tail-evidence.json.

Žádný nový nález nebo ověřovací běh. Vlastní obecné důkazy i hotové
certifikáty se přebírají bez opakování. V oddílu je nyní spárováno
všech47 úloh, ale jeho úplné uzavření se netvrdí:16,21,24,27,33,37,
40,45 a47 zůstávají partial, stejně jako přesně vymezené části textu.

## 38–39: číslice a prvočíselné řetězce

`prime-digits.md` uzavírá všech deset hodnot v38. Každá má vlastní
prvočíselný certifikát a vyloučené všechny konkurenty pro obě postupná
optimalizační kritéria. Dvě uložené enumerace souhlasí také na vedoucí
nule, délce50 a pořadí hodnot. Celkem22962 svědků složenosti,40 vazeb
ECPP a152 Lucasových uzlů už prošlo validací; nový census se nespouští.

`prime-chains.md` dokládá všechny vytištěné přechody, doplněné34ciferné
číslo a jeho nejmenší103ciferný následník. Uložené prodloužení má15
vrcholů a každý přechod má certifikát i vyloučení menších exponentů.
Jde o konečnou konstrukci v rozsahu otevřeného zadání, ne důkaz
globální nejdelší délky. Neúspěch dalšího omezeného hledání není
neexistence následníka. Obecná existence následníků a předpovědi,
co se nikdy nepodaří rozhodnout, nejsou prokázané matematické věty.

Obě konečná krytí pro78557 a271129 dávají obecný důkaz složenosti
všech exponenciálních členů; jsou rozepsána po zbytkových třídách.
Základ78557 sám není prvočíslo, což odpověď přirozeně rozšiřuje
z prvočíselných řetězců na liché koeficienty. Nekonečná aritmetická
rodina má stejná krytí. Všech12 Cunninghamových čísel je certifikováno;
tištěná mez k<12 je správná. Historických69 kandidátů má primární
doklad u Kellera, ale jejich celý tehdejší průzkum nereprodukujeme.
C0181 opravuje pouze Kellerův svazek40 na41.

## 40–42: model výpočtu, počítání prvočísel a dělitelé

`shamir-factor.md` dokládá celou konstrukci40(a,b) v přesně zadaném
jednotkovém modelu neomezených celých čísel. Každé mocnění je sestaveno
z povolených kroků, počet registrů je konstantní a bitová velikost
není vydávána za konstantu. Balení binomických koeficientů, faktoriál,
správná monotónní oblast, Fibonacciho sestup a konečná gcd mají vlastní
argument. Výjimka4 je vyřízena. Cena celé faktorizace O((log n)^2)
plyne ze součtu cen po hladinách stromu rozkladů.

C0176 je konkrétní porušení tištěného horního invariantu pro n=35,
platné i po známém přepisu s na s'. Netvrdí, že jsme tím samostatně
dokázali chybný konečný výstup f(35). Opravená obecná konstrukce
zůstává doložená. Celá40 je nyní partial kvůli výzkumným dovětkům
na666: lepší čas a získání nejmenšího či největšího prvočinitele
v O(log n). Ty nejsou vyřešené hlavním algoritmem.

`prime-count.md` uzavírá všechny čtyři části41, přesně oba typy
rekurzních listů i jejich hraniční rovnosti. Je doložen součtový
strom, celý rozvrh segmentovaných dotazů a O(N) slov paměti bez
skrytého dalšího faktoru N v čase. Příklad N=10 dává f2=63,
f=228 a pi(1000)=168. Posun listových indexů v sazbě je interpretován
s přičtením čísla1; není novou chybou. Všechny známé změny argumentu
f, závorky a historického odstavce jsou již zahrnuty a nemají karty.

Analytická metoda s časem O(x^(1/2+epsilon)) a novější citovaný
algoritmus mají výslovné externí vstupy. Rekordní hodnoty pi(10^20),
pi(10^23), pi(10^24) a pi(10^29) jsou ověřeny v rozsahu primárních
zpráv či tabulek; nejde o naše přepočty. Modrý dodatek tabulky z2006
není vydáván za údaj z původního vydání článku.

`lenstra-residues.md` uzavírá42 obecným důkazem všech výstupů
i úplnosti: převod na dvě rovnice, Eukleidovy vektory, vážená mez,
krajní větve, kvadratická eliminace a počet operací. C0177 je chybný
jmenovatel mu, který dovolí vypsat4 jako dělitele14. C0178 se týká
nepravdivé pomocné nerovnosti s floor; oprava používá ceil. Samotná
varianta s floor nebyla obecným důkazem vyvrácena a konečné pokusy
nejsou důkazem její úplnosti. Celočíselná odmocnina je pojmenovaná
aritmetická operace a mez O(log N) bitů dovoluje konstantní násobek.

## 43: úplná oprava redukce BBS

`bbs.md` obsahuje vlastní konstruktivní důkazy(a,b), včetně následujících
samostatných bodů, které nelze nahradit konečnými testy:

- CRT velikost všech čtverců a jednotkové podgrupy, jediný kanonický
  kořen, parity a půlení s vyřízenými nulami a nejednotkami;
- správné rozdělení vstupů, gcd větev a koncentrace v opraveném(a);
- konečný počet počátečních aproximací a dvě odhadované parity;
- párová nezávislost z invertibilních determinantů a nové mince
  při různých pozicích volání náhodného prediktoru;
- chyby floor podle okrajových pásů závislých jen na multiplikátoru;
- nepodmíněné sjednocení chyb všech etap od t=0, bez chybného
  podmínění nezávislosti na úspěchu dřívějších etap;
- konečná pracovní přesnost, přesná rekonstrukce kořene, ověření
  vlastního gcd i při nesprávné počáteční větvi;
- čas s výslovně uvedenou slovní aritmetikou a účtováním T(G)+r².

C0182 mění součin na součet v definici hlasu. C0183 dokazuje, že
rovnoměrné x nedává rovnoměrné x^4 na všech Q: platný prediktor
modulo209 obrátí většinový odhad, jehož správná odpověď pak má
pravděpodobnost pod3·10^−7. C0184 opravuje znaménko pouze v pomocné
definici chyby, hlas samotný je v tomto bodě správný. C0185 je
vynechání etapy nula v součtu horních mezí, nikoli doložená skutečná
chybovost větší než9/10. Všechny čtyři jsou oddělené od známých errat.

Silnější Fischlinova–Schnorrova optimalizace je pojmenovaný externí
výsledek, který vlastní oprava hlavní úlohy nepotřebuje. Následná
kompozice s3.5P4 výslovně rozlišuje cenu původního statistického testu
od ceny prediktoru po předgenerování bitů. Rozšíření na RSA odkazuje
na původní zdroj a není dalším samostatně dokázaným algoritmem zde.

## 45–46: normová rovnice a diskrétní logaritmus

`norm-equations.md` dokládá existenci a stejnou velikost vláken,
správné násobení norem, Gaussovu mez, primitivitu krátkého vektoru,
degenerace, všechny inverze a úplnou rekurzi. Rozdělení modulu
nepředpokládá nesoudělnost nalezeného dělitele s jeho doplňkem:
je rozepsáno zvedání a CRT pro skutečně nesoudělné části.
Vzorec smršťování koeficientu dává O(log log n) hladin.

C0169 opravuje minus na plus v součinu na417 a670. C0170 vrací
ztracený faktor|m| v délkové mezi. C0171 popírá přesnou rovnoměrnost
normy při vynechání nulových souřadnic; nepředstírá samostatný důkaz
neúčinnosti celého postupu. C0172 opravuje jen minus ve vedlejším
modulo8 příkladu:2²−1²=3. Zadaná lichost modulu má nadále dobrý důvod.

Celá45 je nyní partial: pro vlastní konstrukci máme podmíněný
polynomiální čas s explicitními ERH analytickými vstupy. Nepodmíněné
zlepšení Adleman–Estes–McCurley je doložené v autorově přehledu,
ale jeho vlastní algoritmický důkaz zde není rozpracovaný. Konečné
orákulové kontroly ani bibliografická shoda tento rozdíl neuzavírají.

`discrete-log.md` naproti tomu uzavírá46 i nepodmíněně. Celá faktorová
báze vznikne s doloženou pravděpodobností zvětšení podgrupy, bez
hypotézy náhodné matice. Počty hladkých čísel mají elementární dolní
mez. Celočíselná eliminace nepotřebuje invertibilní pivoty modulo p−1
ani faktorizaci tohoto modulu. Očekávaný subexponenciální čas dává
pomocí Markovovy nerovnosti i požadované almost always. C0173 je
chybný součet pro logaritmy malých prvočísel a nesjednocené indexy
koeficientů. Známá oprava posledního modulu p na p−1 je samostatná.

## Návrat ke straně36 a další kurzor

Odkazy na3.5F a4.5.4–43 jsou nyní skutečně spárované. Vztah(17),
skalární bitový součin a specializace Z=1 souhlasí. Na jednotkových
čtvercích je druhá mocnina permutací; obě redukce a podmíněný význam
statistické nerozlišitelnosti jsou doloženy. Musí se zachovat stejné
rozdělení modulů a započítat převod testu na prediktor.

Strana36 zůstává partial kvůli přesnému kvantitativnímu výkladu
historických100 let a srovnání potřebných modulů. Redukce není
nepodmíněný důkaz obtížnosti faktorizace ani současné bezpečnostní
doporučení. Fráze o větším M se čte jako porovnání postačujících
odhadů v daném modelu, ne dokázaná nezbytnost. Nová karta nevzniká.

Gaussova závěrečná citace na417 nebyla nově porovnána s původním
článkem329; je explicitní bibliografický skip. Další kurzor je
§4.6 Polynomial Arithmetic, tištěná418 / file430. Odpovědi4.6 na
spodku671 zatím nejsou tímto blokem uzavřené.
