# §1.3.3: Program B a cvičení1–11

Kontrola s.173–175 a182, odpovědí522–523, 1. listopadu2026. Originály
přečteny; vydání3, dotisk1. Pro kód se započítává známé erratum
`ENT3 1` na `ENT3 0` z13.7.2000. Nová kapacitní vada je součástí
C0029, nikoli podruhé počítaný nález. Technický důkaz předpokládá
neprázdné cykly s různými jmény uvnitř cyklu a dostatečné pole odpovědi.

## Invariant pravostranného skládání

T[x] je obraz jména x pod už zpracovanou částí součinu napravo.
Celý cyklus `(c_1 ... c_k)` nalevo před aktuální permutací P má
posílat c_i na P(c_(i+1)), poslední c_k na P(c_1). Ostatní obrazy
se nemění. To je přesně cyklické přesunutí starých položek T[c_i].

Po pravé závorce B2 nastaví pomocnou hodnotu Z=0, kde0 není jméno.
Po zpracování jmen c_k,c_(k−1),...,c_r platí:

```
T[c_k]=0;
T[c_i]=P(c_(i+1)) pro r<=i<k;
Z=P(c_r).
```

Ostatní dosud nezměněné položky stále odpovídají P. Proměnná j
si pamatuje c_k, jedinou pozici s nulou. Levá závorka ji doplní
hodnotou Z=P(c_1). Invariant tedy dokazuje správné připojení každého
faktoru zleva; indukcí celý součin. Zároveň dokazuje tabulku2:
znak `)` v jejích mezistavech označuje nulovou, zatím neznámou položku.
Vygenerované sloupce `results/permutation-b-table2.txt` byly porovnány
s původním obrazem; vysvětlení rozdílu `)` versus `?` pod tabulkou
je známé doplnění z15.12.2013.

Program nezná jména předem. Udržuje jejich seznam X[1..n]; X[0]
slouží jako zarážka pro hledání. Nové jméno se nemohlo vyskytnout
v již zpracovaných faktorech napravo, takže je tam pevným bodem.
Proto smí vzniknout nová položka T[n]=n. Počáteční n musí být0.
Tištěná1 přidává neexistující první jméno. Na knižním příkladu skutečně
vytiskne navíc neplatný cyklus s prázdným jménem a A; tento konkrétní
projev je v `results/permutation-b-exploration.json`. Je to reprodukce
známého errata, ne nový nález. Upřesnění významu n z7.12.2024 je
rovněž zahrnuto.

Po dokončení součinu se prochází seznam jmen sestupně. Je-li jméno
neoznačené a není pevným bodem, program sleduje celý jeho T-cyklus,
vytiskne a označí všechna jeho jména. Protože T je bijekce, první
opakované jméno je počáteční a cyklus se zde uzavře. RegistrI3 se
vrátí na počáteční index cyklu a pak se sníží o1; vnější kontrola
proto navštíví přesně n indexů. Pevné body se přeskočí. Tím vznikne
správný disjunktní rozklad bez singletonů.

## Frekvence a čas

X,Y,M,N,U,V znamenají postupně počet karet, neprázdných vstupních
polí bez koncového znaku, vstupních cyklů, různých jmen, výsledných
cyklů včetně singletonů a singletonů. F je počet porovnání při
vyhledávání ve jmenné tabulce. Jiná velká písmena v následujících
rovnicích jsou četnosti označené v Programu B, nesouvisejí s četnostmi A.

```
A=M+1; B=16X−1; C=Y; D=Y−M;
E=G=J=Y−2M; H=N; K=L=M; P=16X−1−Y+M;
Q=Z=N; R=U; S=W=U−V; T=N−V.
```

Každý výskyt jména se hledá jednou. Je-li v aktuálním seznamu na
pozici i mezi1..n, potřebuje n−i+1 porovnání; nové jméno n+1 včetně
zarážky. Tím je F definováno nezávisle na strojovém běhu. Zbývající
četnosti plynou přímo z invariantu a z právě jednoho výpisu každého
nepevného jména. Zachování příchodů do instrukcí dává též všechny
rovnice v části(1) odpovědi10.

Čtyři jednotky u připadají řádkům25,26,54,55. Zbylé ceny v pořadí
A,B,C,D,E,F,G,H,J,K,L,P,Q,R,S,T,W,Z jsou
`1,4,3,3,3,4,1,6,7,2,2,1,3,3,3,10,3,2`.
Dosazení dává přesně knižní vzorec

```
4F+16Y+80X+21N−19M+9U−16V.
```

Poloha prázdných polí nemění žádnou z těchto četností ani F; pouze
změna počtu karet změní X. Pro příklad(6) je F=74 a čas983u,
oproti2161u Programu A.

Lze také obecně odůvodnit tvrzení o rychlosti, včetně vnitřních mezer.
Každé hledání má nejvýše N porovnání, tedy F<=N(Y−2M). Korekce času A
za mezery je nejméně−8(16X−1−Y). Po dosazení těchto dvou mezí a
Y<=16X−1 vychází pro rozdíl časů A minus B dolní mez

```
48X(N−1)+8NM−17N+17M+2U+18V+6.
```

Pro N>=2 a neprázdný vstup použijeme X,M,U>=1: dostaneme nejméně
39N−23>0. Pro N=1 je U=V=1 a mez25M+9>0. Prázdný součin bez jmen
má rozdíl224X−11>0. S dostatečnou kapacitou je tedy B rychlejší pro
každý takový vstup; tato dodatečná obecná nerovnost není závěr jen
z jednoho příkladu.

## Cvičení1–11

1. Násobení2 modulo7 je bijekce, protože inverzí2 je4. Postupné
   obrazy dávají `(1 2 4)(3 6 5)` a pevný bod0, který se nepíše.
2. Výměny a↔c,c↔f,b↔d dávají požadované nové obsahy. Obecně pro
   cyklus x_1,...,x_k použijeme výměny x_1↔x_2,...,x_(k−1)↔x_k;
   indukcí je každý hotový prefix posunut a poslední registr drží
   původní x_1. Není třeba pomocná proměnná na úrovni operace výměny.
3. Přímé složení dvou tabulek dává dolní řádek `dbfcae`.
4. Tentýž součin je `(adcfe)`; b zůstává pevné.
5. Dva netriviální cykly lze uspořádat2! způsoby, otočit jejich zápis
   třemi a dvěma způsoby; celkem12. Jiná možnost nevznikne, protože
   disjunktní cykly bijekce jsou jednoznačné až na pořadí a otočení.
6. Obecný důkaz korekce−8a−2b je v `permutation-a.md`. Původní opačné
   znaménko a koeficienty odpovědi jsou známé erratum2005; hodnocení
   bylo současně zvýšeno z M23 na M28. Poloha mezer nemění čas B.
7. X=2,Y=29,M=5,N=7,U=3,V=1 a2161u; ověřeno i strojově.
8. Při skenování zleva doprava se reset provede u levé závorky a
   doplnění u pravé. Analogická výměna dá T_new(x)=T_old(C^(-1)(x)),
   kde C je právě čtený cyklus. Udržujeme tedy inverzi dosavadního
   součinu. Závěrečný rozklad se musí obrátit; tím vznikne původní
   permutace. To dokazuje proveditelnost i tvrzení odpovědi.
9. Program A začíná prvním dosud dostupným výskytem zleva. B začíná
   posledním dosud dostupným jménem přidaným při průchodu zprava.
   Proto dávají na příkladu `(ADG)(CEB)` a `(CEB)(DGA)`; mapy jsou
   shodné, zápisy nikoli. Celé řádky byly strojově ověřeny.
10. Frekvence a součet jsou dokázány výše, včetně nezávislého F.
11. Inverze obrací pořadí následníků každého cyklu, takže stačí
    cykly zrcadlit. Inverze součinu se násobí v opačném pořadí;
    u disjunktních cyklů pořadí nehraje roli. Značení inverze v zadání má
    známou opravu2.10.1997: π^(-1) na π^−.

## Kapacita B a reprodukce

B používá `ANS EQU PERM`, tedy stejně jako A jen1200 slov na odpověď.
Stejná rodina z C0029 s t=320 má964 neprázdných vstupních polí na61
kartách, ale1280 výstupních. Přesný běh s opravou ENT3 0 byl zastaven
před prvním zápisem mimo pole2400..3599: řádek60, I1=3600,
945974 instrukcí a1268692u. Vytištěno bylo61 kopií vstupu. Netvrdíme
nic o chování B po této zastavené hranici.

Jedna snadno ověřitelná oprava B zmenší deklarovaný vstupní limit na
`MAXWDS=960` (60karet), zavede `MAXANS=2*MAXWDS+23` a vyhradí pro
PERM/ANS toto větší pole. X a T mají po960 slovech. Jde o výslovné
snížení maximálního vstupu, nikoli zachování původního limitu75karet.
Obecný důkaz dostatečné výstupní délky je tentýž jako pro A; B navíc
singletony vůbec neukládá. Adresy jsou X=0,T=960,ANS=1920,
OUTBUF=3863,BEGIN=3887; poslední použitá adresa3962. Ve všech37
radixech tak zůstáváme pod4000 i pod dvoubajtovým limitem4096.

`check_permutation_b.py` prošel12517 kontrolami ve354 úplných bězích.
Nezávisle skládá mapy, kontroluje celou tabulku T před výstupem,
pořadí přidání jmen, celé vytištěné karty a odpovědi, všechny frekvence
a časový vzorec. Malá sada pokrývá dvojice všech neprázdných cyklů na
3 jménech,37 radixů, polohy mezer, náhodné delší vstupy a75karet.
Dva další běhy opravené alokace na60kartovém vstupu t=318 dávají
1272 slov odpovědi; b=64 i100 s asynchronním I/O. Každý má994295
instrukcí a1251068u jádra. Oddělený kapacitní prefix je
`check_permutation_b_capacity.py`. Výsledky jsou uloženy, neopakovat.

Prohledány všechny4 vrstvy errat i jejich tematické okolí. Vedle
uvedených známých oprav nebyla nalezena oprava kapacity A/B. Nejde
o tvrzení o prvenství ani fyzické ověření tištěného exempláře.
Odkaz na symbolové tabulky v kapitole6 je věcně odpovídající obsahové
navigaci svazku3; necertifikujeme tím všechny algoritmy kapitoly6.
