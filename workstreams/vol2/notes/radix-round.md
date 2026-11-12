# §4.4 D a úlohy 17–18: přesné zaokrouhlení při změně základu

Audit 2. listopadu 2026. Třetí vydání, první tisk 1997; původní
strany 326,329,638 a erratum 15. dubna 1999 byly přečteny v sazbě.
`verify_radix_round.py` používá přesná celá a racionální čísla.
Výpočet doplňuje následující obecné důkazy, nenahrazuje je.

## 17: algoritmus pro skutečně nejbližší reprezentovatelné číslo

Číslo s P číslicemi v základu B>=2 má tvar q*B^(E-P), kde
q je celé, B^(P-1)<=q<B^P, a E je celý exponent. Dovolujeme
koncové nulové číslice. Nejprve počítáme s neomezenými exponenty.
Vstupní konečné binární či desítkové číslo lze přesně vyjádřit
jako zlomek N/D; převod tedy nemusí používat nepřesnou mezihodnotu.

Nulu vrátíme přímo. Pro x=abs(N/D)>0 najdeme celé ell tak, aby
B^ell<=x<B^(ell+1), a položíme E=ell+1. Určíme přesný zlomek
y=x*B^(P-E), tedy B^(P-1)<=y<B^P. Celočíselné dělení čitatele
jmenovatelem dá q a zbytek r. Zaokrouhlíme nahoru právě tehdy,
když 2r převyšuje jmenovatel; při rovnosti použijeme pravidlo
pro poloviny ze zadání. Pro binární/desítkovou aritmetiku zde
volíme sudé q. Pokud vznikne q=B^P, nahradíme q hodnotou q/B
a zvýšíme E o jedna. Nakonec obnovíme znaménko.

V intervalu [B^(E-1),B^E] leží cílová čísla na rovnoměrné mřížce
s krokem B^(E-P), včetně obou konců. Přesné porovnání 2r se
jmenovatelem vybírá nejbližší bod této mřížky. Číslo pod dolním
koncem nemůže být k x blíže než tento konec; obdobně nahoře.
Tím je dokázána globální správnost i u mocnin základu, kde
vzdálenosti k předchůdci a následníku nejsou stejné. Normalizace
po přenosu nemění hodnotu. Znaménková symetrie řeší záporné vstupy.

V programu se logaritmus používá jen k počátečnímu odhadu ell
z délek celých čísel. Obě rozhodující nerovnosti jsou následně
ověřeny a opraveny přesnou aritmetikou. Matematicky lze odhad
nahradit exponenciálním a binárním hledáním mezi mocninami B.
Velká celá čísla jsou záměrná: jde o obecný správný algoritmus,
nikoli o důkaz, že jediná operace v pracovní přesnosti vždy stačí.
Při omezených exponentech je ještě nutné vyřešit překročení rozsahu
podle zvoleného formátu; tento důkaz nepředstírá implementaci
všech zvláštních hodnot a podnormálních čísel určitého standardu.

Text D používá správné identity f*2^e=(f*F)*10^E a opačný postup.
Volba E poblíž e*log_10(2) je škálování; případnou normalizaci
je třeba dokončit. U tabulkových aproximací text výslovně upozorňuje
na šíření chyb. Nevyvozuje z nich bezpodmínečnou správnost poslední
číslice; právě tu zajišťuje výše uvedený přesný algoritmus.

Clingerův opravený technický report z roku 1990 obsahuje obdobný
celočíselný Algorithm M (soubor strana 7). Přečteny byly úvod,
tento algoritmus, schéma Bellerophon a poslední stránka s opravami
(strany souboru 3,7,9,13). Steele–White: přečten úvod původního
článku, požadavky na výpis a tabulky s oběma okrajovými vzdálenostmi
(strany souboru 4,7,12). Jejich výpis s nejkratším počtem číslic
řeší další požadavek nad rámec pevné cílové přesnosti v úloze 17.
Celé optimalizované algoritmy Bellerophon a Dragon4 zde nezávisle
neověřujeme; vlastní algoritmus a důkaz odpovídají zadání.

## 18: přesná podmínka převodu tam a zpět

Nechť b,B>=2 jsou celé základy a p,P>=1 počty významných číslic.
Funkce round_b(x,p) znamená nejbližší reprezentovatelné číslo
v tomto formátu; v polovině může použít libovolné pevné přípustné
pravidlo. Předpokládáme neomezené exponenty a iracionální log_B(b).
Tvrzení je: pro každé p-místné u v základu b se převod do základu B
s přesností P a zpět vrátí do u právě tehdy, když

```text
B^(P-1) >= b^p.                                      (1)
```

Rovnost za předpokladu iracionality nenastane. Sazba strany 329
obsahuje >=; OCR znaménko nespolehlivě rozpoznává.

**Postačitelnost.** Nula a znaménko jsou okamžité. Pro u>0 položme
U=round_B(u,P) a v=round_b(U,p). Dokažme, že v!=u vyžaduje
B^(P-1)<b^p. Důležitá je volba otevřených konců intervalů:

Pokud v<u, zvolme e,E tak, že b^(e-1)<u<=b^e a
B^(E-1)<=U<B^E. Krok pod u je b^(e-p), krok nad U je B^(E-P).
Nejbližší zaokrouhlení dává

```text
u <= U + B^(E-P)/2,     U <= u - b^(e-p)/2,
B^(P-1) <= B^(P-E)*U < B^(P-E)*u <= b^(p-e)*u <= b^p.
```

Pokud v>u, zvolme b^(e-1)<=u<b^e a B^(E-1)<U<=B^E.
Teď je krok nad u roven b^(e-p) a krok pod U roven B^(E-P):

```text
u >= U - B^(E-P)/2,     U >= u + b^(e-p)/2.
```

Předchůdce U je U-B^(E-P)>=B^(E-1) a je ostře menší než u.
Proto

```text
B^(P-1) <= B^(P-E)*(U-B^(E-P))
        < B^(P-E)*u <= b^(p-e)*u < b^p.
```

Oba případy odporují (1), nezávisle na volbě v přesných polovinách.

**Nutnost.** Označme A=b^p a C=B^(P-1). Jsou-li C<A, pak
C<=A-1, protože jde o celá čísla. Položme

```text
alpha = 1/(1-1/(2A)),     beta = 1+1/(2C).
```

Platí 1<alpha<beta<B: prostřední nerovnost je ekvivalentní
C<A-1/2. Iracionalita log_B(b) zaručuje hustotu zlomkových částí
e*log_B(b). Vybereme tedy celá e,E s
alpha<b^e/B^E<beta. Pro u=b^e pak u leží nad B^E, ale pod
polovinou vzdálenosti k jeho následníku v B-formátu. Proto
U=round_B(u,P)=B^E. Zároveň

```text
U < u*(1-1/(2A)) = u - b^(e-p)/2,
```

což leží pod středem mezi u a jeho předchůdcem v b-formátu.
Následný převod tedy vrací v<u. Obě nerovnosti jsou ostré, žádné
pravidlo pro poloviny příklad nezachrání.

Použitá hustota má standardní elementární důkaz: princip přihrádek
na zlomkové části 0,theta,...,m*theta poskytuje nenulový násobek
theta modulo 1 libovolně blízko nule. Jeho postupné násobky
projdou kružnici s libovolně malými mezerami. Totéž platí pro
-theta a pro každý posunutý začátek posloupnosti. Husté jsou tedy
i libovolné kladné a záporné koncové úseky exponentů e. Nutnost
proto dává protipříklady i libovolně blízko nule: bez dalšího
omezení neexistuje nejmenší kladný reálný protipříklad.

Bibliografické údaje obou Matulových článků (CACM 11,47–50;
Proc. AMS 19,716–723, oba 1968) souhlasí s autorovým CV. Původní
články nebyly pro tento blok získány; důkaz výše je vlastní kontrola
úplného důkazu vytištěného v odpovědi, nikoli tvrzení o přečtení článků.

## Číselné příklady, minimalita a nová chyba v erratu

Původní příklad s u=2^6408 je správný: při b=2,p=10,B=10,P=4
jde přes 10^1929 zpět na 2^6408-2^6398. Přesný výpočet obě
zaokrouhlení ověřil bez vazby v polovině.

Náhrada posledních dvou řádků odpovědi z 15. dubna 1999 obsahuje
tři překlepy. Správně je

```text
u = (.1111111001)_2 * 2^784 = 1017*2^774,
round_10(u,4) = .1011*10^237 = 1011*10^233,
round_2(1011*10^233,10) = (.1111111010)_2 * 2^784.
```

Podrobný důkaz a původní sazba jsou v
[C0112](C0112-radix-roundtrip-example.md). Uvedená minimalita
platí mezi kladnými **celými** čísly reprezentovatelnými deseti
binárními číslicemi: úplný konečný průchod ověřil všech 397304
menších takových vstupů. Exponenty jdou vzestupně 1,...,784,
mantisy 512,...,1023; pro exponent menší než 10 se berou jen
násobky 2^(10-E), aby byl vstup celý. To pokrývá všechna menší
přípustná kladná celá čísla bez mezer a duplicit. Mezi libovolnými
reálnými čísly minimalita neplatí; například program našel také
u=1020*2^(-784)<1. V hlášení navrhujeme výslovně doplnit „integer“.

## Reprodukovatelnost a rozsah

Čtyři úspěšné checkpointy v `results/radix-round.json`:

- 5250 porovnání s nezávisle vyčíslenou sousední mřížkou, 2052
  hraničních případů a celkem 1374 přesných polovin;
- 275902 převodů tam a zpět splňujících (1), osm dvojic základů,
  a 29 příkladů selhání pod hranicí (nejde o důkaz nutnosti);
- oba knižní příklady, přímé celočíselné certifikáty C0112;
- úplný průchod menších kladných celých vstupů a příklad pod 1.

První běh selhal kvůli rozsahu vlastního generátoru mimo konečnou
testovací mřížku; rozsah a nekanonické okrajové mantisy byly opraveny.
Pokračování 62906 uložilo všechny čtyři úspěšné checkpointy; nástroj
při pozdějším vyzvednutí relace vrátil 143, nikoli doložený exit 0.
Dokončovací běh s --resume skončil exit 0 a všechny hotové bloky
přeskočil, nic znovu netestoval. Oba logy zůstávají uložené.

Všechny čtyři vrstvy errat byly prohledány podle stran i výrazů
638,784,Tydeman,Clinger,Matula a binárních číslic. Následná oprava
tří překlepů z roku 1999 nebyla nalezena. Úloha 17 a text D jsou
checked, úloha 18 má confirmed C0112 při správné obecné větě.
Poslední fyzický dotisk, priorita a nárok na odměnu zůstávají neověřeny.
