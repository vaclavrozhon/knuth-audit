# §1.2.11.3: rozsah, errata, přepis a prameny

Kontrola 1. listopadu 2026. Originály s. 116–123 a odpovědí 504–507
v prvním dotisku třetího vydání byly zobrazeny; mapování na strany souboru
je +15. Ve skenu je přesně 20 původních úloh. Jejich hodnocení jsou

`1:HM20, 2:HM20, 3:M20, 4:HM10, 5:HM24, 6:HM20, 7:HM30, 8:HM30,`
`9:HM36, 10:HM34, 11:HM35, 12:HM20, 13:HM42, 14:HM39, 15:HM20,`
`16:M24, 17:HM29, 18:M25, 19:HM30, 20:HM30`.

Nová cvičení k této sekci v dostupných vrstvách errat nenalezena.
U úlohy 14 chybí samostatný odstavec v odpovědích záměrně: zadání je
rozvedeno do pěti návodných částí; všechny byly prověřeny.

## Matematické pokrytí

| Rozsah | Doklad a výsledek |
|---|---|
| Hlavní (4)–(19), úlohy 1–10,12,19–20 | [asymptotic-gamma.md](asymptotic-gamma.md): Taylorův zbytek, gama řady, Theorem A, obě znaménka horních mezí, obecné Watsonovo lemma i při podmíněné konvergenci |
| Úloha 11 | [asymptotic-parameters.md](asymptotic-parameters.md): všechny reálné větve, koeficienty a rovnoměrnost zbytků pro záporné parametry; oprava Q_x |
| Úloha 13 | [ramanujan-bound.md](ramanujan-bound.md): úplný důkaz všech n, včetně nezávislé kontroly obrysu, konstant, polynomů a konečných případů |
| Hlavní (20)–(26), úlohy 14–18 | [asymptotic-sums.md](asymptotic-sums.md): diskrétní rozvoj s obecným zbytkem, P a S, přesné kombinační identity |
| Nové opravy | [asymptotic-findings.md](asymptotic-findings.md), V1-C0016–19: limita 1 místo 0; absolutní hodnota u v symetrickém integrálu; chybějící exponenciální člen; sgn(x) u normálního integrálu |
| Přesné výpočty | `check_asymptotic_calculations.py`: 51 úspěšných kontrol; `check_ramanujan.py`: 147 úspěšných kontrol, z toho 127 úplných intervalových případů |

Pro Ramanujanovu nerovnost není konečný výpočet vydáván za důkaz
nekonečně mnoha případů: pro všechna n≥128 je zvlášť ověřen obecný
analytický zbytek a kladnost dvou polynomů po posunu n=t+128.
První běh certifikátu zachytil chybný koeficient n^(−4) v citovaném
článku; po přesném odvození a výslovném zaznamenání opravy prošel celý
certifikát. Úspěšné běhy se neopakovaly bez nové změny.

Matematika všech 20 úloh je uzavřena. V celkové mapě zůstávají úlohy
8,11,18,19,20 `partial` pouze pro níže konkretizované primární citace;
ostatních 15 je `checked`. Hlavní text je `partial` kvůli historii.
Nové nálezy jsou doložené našimi zdroji, nikoli potvrzením prvenství,
autorovým přijetím nebo kontrolou fyzického exempláře.

## Relevantní opravy ve všech časových vrstvách

Prohledány řady `all1-prepre`, `all1-pre`, `all1`, `err1` a zdrojový
`err1.textxt`, podle stran i obsahu. Výpis
`sources/asymptotic-calculations-errata-extract.json` obsahuje i sousední
Eulerovy úlohy na s. 116 a 504; ty nejsou zaměněny s novou sekcí.
Čerstvé stažení všech řad z 1.11.2026 je evidováno samostatně.

- 27.3.1998: úloha 17, index sumy k≥0; hodnota se nemění.
- 8.2.2000: s. 121, koeficient 1/8505→16/8505 v Ramanujanově řadě.
- 1.1.2006: odpověď 20, doplnit faktor k při derivování inverzní řady.
- 17.10.2007: odpověď 9, x^z→x^x.
- 10.8.2008: v obou dvojitých sumách odpovědi 11 doplnit k,m≥0;
  dále uzávorkovat exp(n)n^n ve jmenovateli zvláštního případu x=−1.
- 29.3.2023: s. 118, opravit odkaz na §1.2.11.1-(13).
- 2.5.2024 a 30.12.2024: s. 118–119, u,v,w≥0 v první substituci;
  y a u mohou být záporné v druhém integrálu, použít |y| při omezení.
  Pro zápornou úsečku jsme výslovně odvodili rovnoměrnost na |u|≤|y|.

Relevantní originální sazba historických oprav je na obrazu
`errata-all1-prepre-file036.png`, nových oprav na
`errata-all1-file007.png`; obojí bylo zobrazeno. Čtyři nové opravy
V1-C0016–19 v těchto zdrojích ani při hledání mimo příslušné strany nalezeny nebyly.

## Nespolehlivost pomocného Markdownu

Soubor `md/vol1/16-1.2.11.3-asymptotic-calculations.md` není použitelný
jako matematický přepis této sekce. Pro koordinátora, bez změny sdíleného souboru:

- Definice P je nahrazena 1+Q; skutečné P obsahuje k^(n−k)k!/n!.
- U P je chybně −1/3 místo −2/3; u R chybně −1/3 místo +1/3.
  Všechny vyšší koeficienty a velká část důkazu byly vypuštěny.
- Úloha 1 žádá Taylorův vzorec, nikoli obecnou identitu exponenciálních sum.
  Úloha 3 žádá řadu exp(x)γ(a,x), nikoli doprovodný rozvoj horní gama funkce.
- Úloha 6 má skutečný koeficient α(β−α/2); přepis uvádí jiný polynom.
- V úloze 7 chybí pohyblivá horní mez y x^(1/4).
- Úloha 8 je nahrazena jiným integrálem; originál připouští také r=0.
- V úloze 10 má posun hodnotu py/(p−1), nikoli p sqrt(p−1).
- Zadání 12–20 byla nahrazena jinými otázkami. Skutečná úloha 12 je
  převod normálního integrálu, 13 Ramanujanova nerovnost, 14 pětikrokový
  diskrétní rozvoj, 15 integrální identita Q+1, 16 alternující konečná
  identita, 17 součet S, 18 dvě binomické sumy, 19 Watsonovo lemma,
  20 inverzní řada pro Q+1. Hodnocení v této části jsou také chybná.

Tyto vady přepisu nejsou připsány Knuthovi a nejsou počítány jako
nálezy v knize. Soupis ve `scope.json` byl opraven podle originálu.

## Přečtené primární prameny a zbývající mezery

- Flajolet–Grabner–Kirschenhofer–Prodinger 1995: kompletní argument
  k Ramanujanově nerovnosti přečten a rekonstruován; viz samostatná
  poznámka. Zdrojové tiskové chyby nejsou zaměněny s chybami knihy.
- Temme 1975, [CWI sken](https://ir.cwi.nl/pub/10709/10709D.pdf):
  přečteny s. 1109–1112, zejména (1.4) a §2. Obsahuje rovnoměrné
  aproximace pro reálné parametry a sám rozlišuje Tricomiho výsledek.
  Citace roku, svazku a stran souhlasí. Sken s. 1112 má uříznutý pravý
  okraj; neprohlašujeme kontrolu každého slova ani beta části článku.
- Temme 1979, [CWI sken](https://ir.cwi.nl/pub/10713/10713D.pdf):
  s. 757–758 a 764–766, definice, rekurence a celé §5 o komplexních
  parametrech skutečně přečteny. Rozlišeny větve odmocniny a oblasti
  |arg a|≤π−ε_1, |arg(x/a)|≤2π−ε_2. Citace odpovídá obsahu; tabulky
  numerických zbytků uprostřed článku nebyly samostatně certifikovány.
- Odlyzko, [autorský text](https://www-users.cse.umn.edu/~odlyzko/doc/asymptotic.enum.pdf):
  úvod a bibliografický průvodce přečteny; skutečně **65 různých
  číslovaných příkladů**, se seznamem a stranami v
  `results/odlyzko-example-inventory.json`. Tento 192stránkový autorský
  text má jiné stránkování než knižní kapitola 1063–1229. Nepovažujeme
  ho za kontrolu sazby všech stran vydané kapitoly ani důkazů 65 příkladů.
- Helen Keller: originální sken *The Story of My Life*, s. 242,
  strana PDF 288. Dopis paní Laurence Huttonové je datován **29.5.1898**
  a obsahuje zkrácený výrok použitý na s. 123 TAOCP; znění i rok souhlasí.
  Uložen obraz `keller1903-story-of-my-life-file288.png`.
- Rousseau 1989: registr Crossref s metadaty vloženými vydavatelem
  potvrzuje název *A simply obtained asymptotic expansion for the
  probability that a random mapping is connected*, AML 2(2),159–161,
  DOI 10.1016/0893-9659(89)90012-8. Konkrétní třístránkový důkaz zatím
  nezískán; ScienceDirect odmítl přístup. Náš důkaz úlohy 20 je úplný.
- Carlitz 1965: titul, svazek a strany 248–252 potvrzeny záznamem
  vydavatele/JSTOR; AMS PDF odmítnuto 403. Konkrétní článek dosud
  nepřečten, vztah polynomů je nezávisle dokázán rekurencí.
- Dosud nepřečteny konkrétní citované pasáže: Demuthova disertace
  (Stanford 1956), s. 67–68; Ramanujanovy původní texty 1911/1912;
  Furch 1939, s. 92–95; Tricomi 1950, s. 136–148; Gould AMM 1968,
  s. 1019–1021; Cauchy *Oeuvres* (2)6, s. 62–73; Barnes 1906,
  s. 249–297; Watson 1918, s. 116–148; příslušná místa de Bruijna.
  Pozdější citace nejsou vydávány za přečtení těchto originálů.
- Knuthova osobní vzpomínka na výpočet z roku 1963 je přímo jeho
  vlastní primární svědectví. Nenahrazujeme ji domnělým nezávislým
  dokladem; matematická část a uváděný desetinný koeficient souhlasí.

Uložená metadata každého staženého souboru zaznamenávají URL, čas,
otisk a skutečný rozsah čtení. Nedostupnost zdroje je oddělena od
matematické platnosti příslušné identity. Tyto konkrétní bibliografické
mezery zůstávají ve frontě pro návrat před uzavřením celého svazku.
