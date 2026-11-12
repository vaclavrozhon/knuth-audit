# V1-X0770–X0771: kumulanty v Thieleho původním tisku

Thieleho rok 1889 a konkrétní matematická atribuce na s. 103 jsou
checked. Přesně citovaný Haldův článek 2000, s. 137–153, zůstává
source-partial. Toto jsou dvě různé otázky; původní definici jsme
ověřili samostatně a nenahrazujeme jí čtení celé historické studie.

Root hashově ověřil všech 63 souborů a 11 vstupů zmrazeného paketu
`parallel/analysis-primary-followup/thiele-hald/MANIFEST.json`, SHA-256
`19d5aff2c628ee21ff3d1916edbdb59b16bc52068f6c78838216f43535ca224a`.
Přečetl HANDOFF, UNIT_STATUS, poznámku a přesný read-log. Přímo
zobrazil titul 1889 (PDF 9), tištěnou 19 s definicí (16), 33
s násobením relativních četností a 35–36 s důkazem aditivity
(PDF 31, 45, 47–48). Agentův širší rozsah 16–22, 26, 33–37
je zaznamenán odděleně. Celá Thieleho kniha nebyla auditována.

Pro pozorování o_1,...,o_n označuje s_j součet jejich j-tých mocnin
a s_0=n. Definice jeho veličin mu_j, nazvaných Halvinvarianter,
má přesně tvar

```text
s_(r+1) = sum_(j=0)^r binom(r,j) s_(r-j) mu_(j+1).
```

Po vydělení n definujme momenty m_j=s_j/n, jejich exponenciální
generující funkci `M(t)=sum m_j t^j/j!` a formální řadu
`K(t)=sum_(j>=1) mu_j t^j/j!`. Rekurence říká M'=K'M;
proto M(0)=1 a K(0)=0 dávají K=log M. V celočíselném případě
M(t)=G(exp(t)), kde G je pravděpodobnostní generující funkce
z TAOCP (23). Tím jsme přímo identifikovali stejnou matematickou
veličinu. Netvrdíme, že Thiele v roce 1889 sám napsal tuto
pozdější logaritmickou definici.

Strana 33 výslovně násobí relativní četnosti volně kombinovaných
pozorování. To je předpoklad odpovídající nezávislosti, potřebný
pro vztah na 35–36: pro u=a o+b o' je jeho r-tý kumulant
`mu_r(u)=a^r mu_r(o)+b^r mu_r(o')`. Původní důkaz používá jednoznačnost
rekurence a binomické koeficienty. Ověření tohoto výsledku není
ověřením všech tabulek ani moderní obecné centrální limitní věty.

Root přímo přečetl TAOCP 103 a all1-prepre 11. Oprava data1903
na1889 a doplnění Halda2000 jsou z4.10.2005; oprava indexu druhého
kumulantu ve(23) z29.7.1997. Jde o známá errata. Prohledání všech
čtyř úplných vrstev je v paketu. Nový nález nevznikl, přijaté
matematické testy se neopakovaly. Absolutní historické prvenství
ani fyzický výtisk TAOCP nejsou touto kontrolou doloženy.

Z Halda2000 máme bibliografii a abstrakt; původní137–153 chybí.
HTTP200 s JSTOR Client Challenge není obsah článku. Starší text
1979/1981 ani částečný přetisk2002 nebyly zaměněny za citaci2000.
Root přímo přečetl archivní soupis IHP na50: BR29-2-1/2 opravdu
eviduje předběžnou a revidovanou verzi1998–1999,56listů, publikovanou
v ISR68(2000),137–153. Čtení soupisu neznamená čtení těchto rukopisů;
je to pouze konkrétní zbývající knihovní cesta.
