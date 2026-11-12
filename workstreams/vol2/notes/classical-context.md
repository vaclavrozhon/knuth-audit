# §4.3.1: závěr textu a bibliografický kontext

Kontrola 2. listopadu 2026. Původní strany 278–280 a odpovědi 623–630
byly vizuálně přečteny. Matematické a instrukční části mají samostatné
poznámky `classical-*.md`. Tento blok uzavírá zbývající vzorce na279,
kontrolu historického výkladu proti dostupným pramenům a bibliografické
dovětky. **Nejde o nové provedení historických rekordních výpočtů ani
o důkaz absolutního prvenství jednotlivých autorů.** Nedostupné prameny
jsou uvedeny níže; jejich obsah není vydáván za přečtený.

## Reciproční iterace a geometrická řada

Nechť v je nenulové reálné číslo a x aproximuje jeho převrácenou hodnotu.
Zaveďme relativní chybu `e=1-v*x`, tedy `x=(1-e)/v`. Pro celé r>=2 je

```
x_new = x*(1+e+...+e^(r-1)),
v*x_new = (1-e)*(1+e+...+e^(r-1)) = 1-e^r.
```

Nová relativní chyba je **přesně e^r**. Pro r2 dostáváme `2x-v*x^2`;
pro r3 výrazy `x+x*(1-v*x)+x*(1-v*x)^2` a
`x*(1+(1-v*x)*(1+(1-v*x)))`. Oba tištěné zápisy tedy souhlasí.
Při |e_0|<1 je po k krocích chyba `e_0^(r^k)`, a proto x konverguje
k1/v. Podmínku počáteční aproximace nelze vypustit: x0=0 je například
pevný bod. Text mluví o počáteční aproximaci, ne o globální konvergenci
ze všech reálných čísel. Výpočet v konečné přesnosti přidává chybu
zaokrouhlení; tato identita sama ještě není důkazem celé rutiny4.3.3R.
Její algoritmus a složitost zůstávají v pořadí práce u §4.3.3.

Pro druhý vzorec na279 jsou u,v,delta reálná čísla, v!=0,
`|delta/v|<1`. Konečný geometrický součet dává

```
u/(v+delta) = (u/v)*sum_(j=0)^N (-delta/v)^j
              +(u/v)*(-delta/v)^(N+1)/(1+delta/v).
```

Zbytek jde k nule. Po limitním přechodu tedy dostaneme přesně uvedenou
řadu; pro |delta/v|>=1 se tento závěr obecně nedá použít. Dvojitá
přesnost4.2.3 již má vlastní kontrolu. Tato dvě algebraická odvození
nevyžadují numerický test, který by pouze opakoval stejné identity.

## Rané programy, dělení a knihovny

- **Goldstine–von Neumann1947:** veřejný [sken IAS](https://www.ias.edu/sites/default/files/library/pdfs/ecp/planningcodingof0103inst.pdf)
  má194 stran souboru a zahrnuje více dílů. Webová textová vrstva
  prvního dílu obsahuje §9.8–9.10, tištěné61–69: dvouslové sčítání,
  odčítání a násobení, přenosy a časové odhady. To podporuje věcný
  obsah odkazu na rané programování. Přímé stažení vrátilo403;
  nástroj pro webové snímky vrátil jen odkazy, nikoli dostupný obraz.
  **Tento pramen nebyl vizuálně přečten** a číslování jeho přetisku
  v Collected Works5,142–151 nebylo přímo porovnáno. Bibliografický
  katalog Netlib sloužil pouze k nalezení originálu. Slovo „first“
  není tímto postupem nezávisle prokázáno.
- **Pope–Stein a varianty D:** správnost vlastních větA/B a programuD
  je doložena v `division.md` a `classical-division-*.md`. Aktuální
  oprava z14.5.2026 oslabuje přesnou atribuci na tvrzení, že Pope
  a Stein dokázali *varianty* větA/B. Kniha po této opravě nepřipisuje
  obě zdejší formulace doslova článku1960. Úplné texty Cox–Luther1961,
  Stein1964, Krishnamurthy1965, Krishnamurthy–Nandi1967 a
  Collins–Musser1977 nebyly v tomto kontextovém bloku znovu získány.
- **Fourierovo dělení:** popis postupně zvětšované přesnosti není
  algoritmem s úplně předepsaným zaokrouhlováním. Autorova poznámka
  o vlastních rozsáhlých testech neudává vstupy ani měření; její
  rychlostní srovnání nebylo reprodukováno. Rabinowitz1961,
  Krishnamurthy1970 a Laughlin1930 jsou odkazy na související metody;
  zde byly ověřeny právě vytištěné identity, nikoli všechny výsledky
  těchto článků.
- **Brent1978:** autorův [článek](https://maths-people.anu.edu.au/~brent/pd/rpb042.pdf)
  byl stažen; první tištěná strana57 vizuálně přečtena. Popis MP,
  proměnné přesnosti a elementárních i speciálních funkcí souhlasí.
  Rozsah57–81 v knize spojuje vysvětlující článek57–70 a navazující
  [Algorithm524](https://maths-people.anu.edu.au/~brent/pub/pub043.html),
  71–81. Není to chybné stránkování jediného článku. Celý balík
  Fortran nebyl spuštěn ani auditován.
- **Smith1991/1998:** [autorova stránka](https://myweb.lmu.edu/dmsmith/FMLIB.html)
  byla stažena a přečtena. Potvrzuje oba názvy a rozsahy17(1991),273–283
  a24(1998),359–367. Druhý článek přidává známé erratum z28.10.2000.
  Aktuální vlastnosti FM nelze automaticky připsat verzi1991;
  současný web nebyl použit k takovému závěru. Stroud–Secrest1963,
  Blum1965, Tienari–Suokonautio1966 a Collins1966 zůstávají v tomto
  bloku bibliografickými odkazy, nikoli znovu auditovanými knihovnami.
- **Möller–Granlund:** dodatek z2.5.2021 je věcně podpořen prvním
  dvoustránkovým úvodem [autorského preprintu](https://gmplib.org/~tege/division-paper.pdf),
  získaného z veřejného [zrcadla](https://ftp.libre-soc.org/division-paper.pdf)
  a vizuálně přečteného. Týká se dělení pomocí předpočítané aproximace
  převrácené hodnoty a levnějších násobicích instrukcí. PDF má vlastní
  číslování1–10; nejde o časopiseckou sazbu165–175. Pro normalizované
  slovo d je jeho definice `v=floor((beta^2-1)/d)-beta` konzistentní
  i při d=beta/2. Uváděná zrychlení na konkrétním hardwaru nebyla
  nezávisle změřena.

## Rekordy čísla pi

Následující srovnání se týká tvrzení historického textu, nikoli současného
světového rekordu. Pozdější rekord sám o sobě nedělá staré datované
sdělení chybným.

| Tvrzení knihy | Doložený rozsah |
|---|---|
| ENIAC1949,2037 desetinných míst,70h | Tabulka v Shanks–Wrench1962,76 souhlasí. Shelburneův vlastní popis archivní rekonstrukce z2013 potvrzuje Labor Day weekend a70h; původní Reitwiesner1950 nebyl celý získán. |
| Genuys1958,10000 míst,100min | Shanks–Wrench1962,76 tuto kombinaci uvádějí; původní článek Genuys1958 nebyl celý přečten. |
| Shanks–Wrench1961/1962,100000 míst | Původní článek76–79 byl vizuálně přečten. Počítání a kontrola trvaly8h1min a4h22min, převod navíc42min. Zaokrouhlení knihy na8h a4.5h není chyba. Rozpor po70695 místech zmizel po přepočtu chybného členu; souhlas byl nakonec100265 míst, zveřejněno100000. |
| Guilloud–Bouyer1973, milion míst za necelý den | Podpůrná tabulka v dohledaném článku Takahashi–Kanada1998 uvádí1001250 a23h18min. Dostupný byl jen indexovaný text; primární zpráva1973 ani Shibata1982 nebyly obrazově přečteny. |
| Chudnovští1991, přes2 miliardy míst a250h | Dobová reportáž Richarda Prestona uvádí2260321336 míst a přibližně250h včetně kontrol na domácím paralelním stroji. Údaj odpovídá knize. Číslice nebyly přepočteny. |
| Kanada–Takahashi1997,51.5 miliardy míst | Dobový přetisk jejich oznámení uvádí51539600000. Abstrakt jejich článku1998 uvádíSR2201,1024 procesorů a66h11min včetně ověření; to odpovídá zaokrouhlenému součtu29.0+37.1h. Původní PDF vrátilo503/429, takže přesné rozdělení obou časů a měsíc nebyly obrazově ověřeny. |

Prameny tabulky: [Shanks–Wrench1962](https://www.ed-thelen.org/Shanks-Wrench-Pi.pdf),
[Shelburne2013](https://www.wittenberg.edu/news/2013/03-14-pi),
[Preston1992](https://www.newyorker.com/magazine/1992/03/02/the-mountains-of-pi),
[archiv přetisku oznámení](https://groups.google.com/g/alt.math.recreational/c/nf13A0i14NM),
[Takahashi–Kanada1998](https://tsukuba.repo.nii.ac.jp/record/37234/files/IPSJ-JNL3907005.pdf).
Datum webu Prestona24.2.1992 a datum časopiseckého čísla2.3.1992 se
nesměšují. První čtyři stránky Shanks–Wrench byly čteny, nikoli dalších
20 stran vytištěných desetinných číslic. OCR na79 chybně čte rok
poznámky jako1981; původní obraz má1961. Nejde o chybu Knuthovy knihy.

Starší údaje de Lagny1719, Dase1844, Shanks1853/1873 a Ferguson1945/1946
byly obsahově porovnány s nalezenými historickými výklady, ale všechny
původní tisky nebyly získány. Neoznačujeme jejich přesné stránkové odkazy,
prvenství nebo délku ručních výpočtů za nově nezávisle potvrzené.
Známá poznámka v erratech vysvětluje, proč se ponechává jméno
„J. C. V. Hoffmann“, i když autorovo křestní jméno bylo Immanuel.

**Gardnerův miliontý digit:** vlastní pozdější kniha Gardnera
[*The Magic Numbers of Dr. Matrix*](https://www.scribd.com/doc/57110566/The-Magic-Numbers-of-Dr-Matrix), kapitola8, znovu otiskuje předpověď
z1966 a výslovně započítává počáteční3. Jde tedy o999999. desetinné
místo, nikoli o1000000. místo za tečkou. Dostupná webová textová vrstva
byla použita jen k vyjasnění formulace; první vydání dodatku1966
nebylo vizuálně ověřeno. [API pi.delivery](https://pi.delivery/),
které počítá index0 jako3, vrátilo pro index999995 deset znaků
`4581513092`: index999999 je5, index1000000 je1. Odpověď je uložena
v `sources/pi-millionth-google.json`. Jde o porovnání s publikovanými
daty, nikoli o náš vlastní certifikovaný milionimístný výpočet.
Tištěné slovo „digit“ proto nedává důvod k novému nálezu.

## Doplněk o rekordu2019

[Iwaové původní zpráva](https://cloud.google.com/blog/products/compute/calculating-31-4-trillion-digits-of-archimedes-constant-on-google-cloud)
a obě připojená schémata byly získány; schémata vizuálně přečtena.
Počet31415926535897 desetinných míst, program y-cruncher a nezávislá
kontrola Yeeho pomocí Bellardovy a BBP formule souhlasí s erratem
z14.3.2019. Tabulka rozlišuje111.8 dne výpočtu a121.1 dne od začátku
do konce; dále240TB přiděleného úložiště a170TB nejvyššího využití.
[Zpráva Yeeho](https://www.numberworld.org/blogs/2019_3_14_pi_record/)
a [veřejný protokol](https://www.numberworld.org/y-cruncher/records/2019_1_21_pi.txt)
byly čteny webovým nástrojem. Protokol uvádí9661293.745s výpočtu
oproti10464677.977s celkového času. Rozdílná čísla nejsou rozporem.
Výsledek ani platnost podpisu validačního souboru jsme nepřepočítali.

## Hardware a dovětky odpovědí

Edelmanův [původní článek](https://math.mit.edu/~edelman/homepage/papers/pentiumbug.pdf),
první dvě tištěné strany54–55, byl vizuálně přečten. Téma Pentium1994,
název a SIAM Review39(1997),54–67 souhlasí; nejde o naše nové ověření
chování fyzického procesoru. Starší přehledové články Reitwiesnera,
MacSorleyho, Metzeho a Garnera nebyly všechny nově získány. Dolní meze
hardwarového času Winograd/Brent/Floyd jsou dopředným odkazem na4.3.3E;
jeho matematická kontrola zůstává otevřena v příslušné sekci.

U42 byl nyní Holte1997 vizuálně přečten na tištěných138–142 (PDF2–6).
Věta1 na140 po dosazení počátečního přenosu0 a základuN=b^n dává
přesný počet použitý v `classical-carries.md`. Eulerova formule(6)
na142 potvrzuje střídavé znaménko, doplněné známým erratem2024.
Vlastní obecný důkaz úlohy již byl hotov; celá Holteho spektrální
analýza matice nebyla nezávisle auditována.

U43 [autorův seznam Blinnových publikací](https://www.jimblinn.com/publications/)
potvrzuje sloupek o praktickém skládání obrázků v14(6), listopad1994.
Pozdější *Three Wrongs Make a Right* je jiný článek z1995. Plný text
prvního článku nebyl získán, takže se netvrdí řádková shoda jeho vzorce
s Knuthem. Vlastní důkaz a všech65536 párů úlohy43 jsou ověřeny.
U15 byl nalezen původní konferenční záznam Krandick–Johnson1993
na [ARITH11](https://www.acsel-lab.com/arithmetic/arith11/arith11.html);
PDF přímým stažením vrátilo403 a jeho obraz nebyl přečten. Větu o chybě
zkráceného součinu dokládá náš vlastní důkaz, nikoli domnělá četba článku.
Ostatní dovětky31–41 mají rozsah zdrojů uveden ve vlastních poznámkách.

## Errata a závěr bloku

Znovu prohledány všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`,
`err2`, včetně současného TeXu. Relevantní obrazové strany již byly
přečteny při předchozích blocích: Smithův dodatek2000, Paris2002,
Hoffmann2010, millennium1998, rekord2019, Möller–Granlund2021 a
oslabení atribuce Pope–Stein2026. Zde se nepotvrdila nová chyba.

Text sekce lze uzavřít v uvedeném rozsahu matematické kontroly a
kritického porovnání dostupných pramenů. **Celá §4.3.1 stále není hotová:**
úloha40 má otevřený uniformní zbytek O(n) pro malý pevný základ.
Neověřené podrobnosti starších tisků a absolutní historická prvenství
nejsou bez důkazu překlasifikována na potvrzená fakta.
