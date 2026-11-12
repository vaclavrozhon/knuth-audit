# Galler–Fischer 1964 — kořenová kolace a uzavření §2.3.3–11

Root přebírá zmrazený adresář parallel/equivalence-originals.
Manifest má SHA-256
5352a7b6781fdeae5697de8b124a164001d7eb594b8779e7d1e56d2ec6e70693;
všech 69 souborů a 33 externích vstupů bylo ověřeno podle délky
a SHA-256. Paket obsahuje 28 přístupových záznamů. Neúspěšné
HTML odpovědi s příponou PDF nejsou považovány za články.

Agent i root přímo přečetli celé původní Galler–Fischer 301–303
a celý jejich opravný dopis na 506. Root dále přímo porovnal
knižní 353–355, 360 a 576, autorovo CV na 11 a NBS bibliografii
na 211. Dřívější matematické důkazy a testy zůstávají beze změny.

## Identifikace a omezení vnější sazby

An Improved Equivalence Algorithm vyšel v CACM 7(5), květen
1964, 301–303, DOI 10.1145/364099.364331. Originál 301 tiskne
Fisher. Dopis In Defense of the Equivalence Algorithm,
CACM 7(8), srpen 1964, 506, DOI 10.1145/355586.364830,
je podepsán Bernardem A. Gallerem a Michaelem J. Fischerem.
Vlastní Fischerovo CV, strana 11, položka 6, potvrzuje totožnost
práce i podobu jména. Knižní Fischer je správně.

Oba originály poskytuje veřejný projekt J.-J. Lévyho na INRIA:

- https://pauillac.inria.fr/~levy/courses/X/IF/03/pi/levy2/fischer-galler.pdf
- https://pauillac.inria.fr/~levy/courses/X/IF/03/pi/levy2/fischer-galler2.pdf

První PDF má 277502 bytů a SHA-256
729c20b2607860cbb5061b441ae56f4ae1601db1d24fa04858b59b97703696a7.
Druhý má 313685 bytů a SHA-256
eea56d1c0b3d98f7096ad2b0f0773d3ffd8d9842134c4e46cccf8f66a37be2c3.
Obsahuje také nesouvisející 505; zde kontrolujeme příslušný
dopis na 506, nikoli všechny příspěvky obou stran.

Dopis výslovně doplňuje t=t+1 do třetího iteračního rámečku
Fig. 2, opravuje R[t]=a(E[t]), dva vzorce H/H' a kořenový
test S[i]=i ve Fig. 3. Všechny opravy odpovídají viditelné
původní sazbě 302–303. Kniha již správně cituje i stranu 506.

Fig. 1 na 301 má navíc doslovné S[t]=t v místě, kde výstup
k rodiči vyžaduje t=S[t], a obrácené větve T/F u j=1. První
prvek první skupiny by bez inicializace použil t0. Dopis
tyto detaily Fig. 1 neopravuje; Fig. 2 je v těchto místech
správně. Neprohlašujeme všechny externí diagramy za bezchybné.
Jde o kvalifikaci pramene, nikoli o nový nález proti TAOCP.

## Rodičovský les a Algorithm E

Rodičovský les ukládá u každého uzlu jeho rodiče; jeden strom
představuje jednu třídu ekvivalence. Článek 302–303 výslovně
popisuje hledání kořene a spojení dvou tříd připojením jednoho
kořene k druhému. Tím přímo podporuje knižní atribuci na 353.

Článek vkládá jména průběžně a označuje kořen odkazem na sebe;
kniha předem založí n uzlů a označuje kořen nulou. Různé volby
kořene mohou dát jiné rodičovské pole, ale stejnou ekvivalenci.
Důkaz E již byl přijat v notes/other-trees-equivalence.md.
X0288 lze nyní celý převést na checked. Nejde o vyčerpávající
důkaz absolutního historického prvenství ani o ověření
samostatných atribucí McIlroyovi a Tritterovi z odpovědi 10.

## Přesný převod posunů a mezí v odpovědi 11

V knize DELTA(Q)=d na hraně Q→P znamená Q[k]=P[k+d].
Kořenové LBD, UBD jsou nejmenší a největší potřebný index
v souřadnicích kořenového pole.

Článek ukládá pole pozpátku: adresa X[k] je a(X)-k, kde
a(X) označuje adresu nultého prvku. Hrana Q→P má
R(Q)=a(P)-a(Q). Rovnost fyzických adres dává

```
a(Q)-k = a(P)-(k+R(Q)),
tedy Q[k]=P[k+R(Q)] a DELTA=R.
```

Článkové H,H' vymezují fyzický interval
[a(P)-H+1, a(P)+H']; v kořenových indexech je to [-H',H-1].
Proto LBD=-H' a UBD=H-1. Knižní sjednocení s posunem D
se přesně převádí na opravené vzorce z dopisu:

```
H(P)  = max(H(P),  H(Q)+D),
H'(P) = max(H'(P), H'(Q)-D).
```

Sčítání vzdáleností podél cesty, spojení různých kořenů
a rozpor při nenulovém posunu kořene vůči sobě jsou přímo
popsány na 302–303 a odpovídají T1–T3. Stejně je doloženo
rozšíření s předem přidělenými absolutními adresami.

Článek dostává rozměr pole již při jeho zpracování; nepředkládá
gramatiku všech promíchaných ARRAY deklarací. Knižní poznámka
mluví o možnosti rozšíření za vhodných podmínek, nikoli
o doslovné specifikaci původního článku. Pro takové rozšíření
stačí před konečnou rezervací přijímat nové deklarované meze
a posunout je po cestě ke kořeni; udržované minimum/maximum
pak aktualizuje obal deklarovaných buněk. Další vztah mezi
různými kořeny použije stejný posun, ve stejné třídě stejný
test rozporu. Pokud jsou již pevné absolutní adresy, musí se
ověřit také jejich slučitelnost, jak činí článek. Nezavádíme
předpoklad libovolné pozdější změny již přidělené paměti.

Pramenná mezera X0294 je uzavřena. Spolu s dříve přijatým
obecným důkazem a nezávislými kontrolami je celá původní
úloha §2.3.3–11 checked. Žádné staré testy se neopakovaly.

## Salton zůstává samostatně otevřený

Root přímo přečetl NBS Monograph 91, stranu 211, položky
512 a 516. Určují Information Storage and Retrieval,
Scientific Report ISR-1, Harvard Computation Laboratory,
30. listopadu 1961, 152 stran; Saltonův oddíl The Manipulation
of Trees in Information Retrieval je II-1 až II-44,
AFCRL-62-77, a je spojen s CACM 5, 103–114 (1962).

Jde o bibliografický doklad, nikoli vlastní Saltonův text.
Celých 103–114 ani alternativních II-1 až II-44 nemáme.
X0287 proto zůstává partial přesně v pramenné části, bez
znovuotevření prověřené reprezentace a Algorithm F.

Agent prošel všechny čtyři vrstvy errat podle stran i témat
a přímo četl příslušné původní obrazy. Root přečetl výpisy
a kolaci; nevydává to za nové zobrazení všech erratových
obrazů. Žádná příslušná oprava atribuce nebo obou citací
nebyla nalezena. Nový kandidát ani potvrzený nález nevznikl.
