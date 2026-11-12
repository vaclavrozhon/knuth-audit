# Zbývající původní prameny k Eulerově sumaci

Stav 2026-11-02. Tento samostatný dodatek navazuje na zmrazené pakety
`robson`, `algorithms` a `constants`; jejich soubory nemění. Výsledkem je
uzavření konkrétního obsahu de Bruijnova §3.7 a Steffensenova §14. U Sekiho
je přímo doložen příslušný tisk z roku 1712, ale citované strany vydání 1974
zůstávají nečtené. Nejde o nové ověření již hotových obecných důkazů.

Před hledáním byly přečteny kořenové záznamy
`notes/euler-errata-and-scope.md`, `sources/euler-primary-limits.json`
a oba starší katalogové záznamy Sekiho. Starý neúspěšný NDL obrazový odkaz
ani starý katalogový Google Books odkaz nebyly opakovány bez nové stopy.
Konkrétní nové cesty zachycuje `results/euler-primary-searches.json`;
stažení včetně chyb jsou v `sources/retrievals-euler-gaps.jsonl`.

## De Bruijn, §3.7: obsahově i obrazově ověřeno

Rice University zveřejňuje na [stránce kurzu](https://www.cmor-faculty.rice.edu/~strings/)
odkazy na [kapitoly 1–2](https://www.cmor-faculty.rice.edu/~strings/debruijnCh1a2.pdf)
a [kapitolu 3](https://www.cmor-faculty.rice.edu/~strings/debruijnCh3.pdf).
První sken obsahuje titul s rokem **1958**, North-Holland, Amsterdam /
P. Noordhoff, Groningen. Druhý obsahuje původní sazbu kapitoly 3.
Přímo byly přečteny titul, relevantní obsah a tištěné strany **40–42**;
celý §3.7 je na s. 42. Pozdější vydání tím není kolacionováno.
Další uložené stránky kapitoly nejsou vydávány za audit jejich obsahu.

`C(z)` je zde konstanta v asymptotickém rozvoji součtu
`sum(k^(-z) log(k), k=1..n)`. De Bruijn uvádí
`C(z)=-(1-z)^(-2)-zeta'(z)`. Pro `z=-1` dostaneme
`C(-1)=-1/4-zeta'(-1)`. Integrál od 1 do n přidá konstantu `1/4`
a člen s `B_2` přidá `1/12`; tedy konstanta v normalizaci knihy je
`log(A)=1/12-zeta'(-1)`. Odkaz v odpovědi 7 na s. 504 je věcně přesný.
§3.7 neuvádí druhý knižní tvar s `zeta'(2)/zeta(2)` doslova;
ten je důsledkem funkční rovnice, již samostatně dokázaným v kořenové
poznámce `euler-products.md`, P5. P4 se zde neopakuje.

Technická poznámka k původu: obvyklí klienti nedokázali ověřit řetězec
certifikátu Rice. Získání těchto veřejných statických souborů proto
použilo pro dané požadavky vypnuté ověřování TLS. Log to výslovně uvádí.
Soubory byly získány přímo z uvedené institucionální domény; žádné
přihlášení, proxy kopie ani přístupový token nebyly použity.

## Steffensen, Interpolation, §14: obsahově i obrazově ověřeno

Veřejná [kopie University of Arizona v Internet Archive](https://archive.org/details/interpolation0000jfst)
obsahuje původní titul **Baltimore, The Williams & Wilkins Company, 1927**
a rub s vydáním v lednu 1927. Přímá obrazová četba zahrnuje titul a rub
(PDF 7–8) a **celý §14**, od dolní části s. 129 do horní části s. 138
(PDF 143–152). Údaj „129–137“ by opomíjel závěr §14 na s. 138.

`B_m` označuje sudé Bernoulliho číslo, `P_m(x)` Bernoulliho polynom,
`R_m` knižní zbytek po korekčním členu řádu m a
`C_m=B_m/m! [f^(m-1)(b)-f^(m-1)(a)]` tento korekční člen na intervalu
`[a,b]` s celočíselnými konci. Přesné návaznosti jsou:

| Steffensen | Knižní tvrzení / již přijatý důkaz |
|---|---|
| s. 129–131, č. 144–146, (1)–(7) | Periodické Bernoulliho polynomy a integrální zbytek Eulerovy–Maclaurinovy formule. |
| s. 132–133, č. 148–149, (9)–(12) | Jádro `B_m-P_m({x})` má pevné znaménko. Při pevném znaménku `f^(m)` vede (12) přes `R_(m-2)=C_m+R_m` k intervalu mezi `-C_m` a `(1-2^(1-m))*C_m`. To je kořenové E10. |
| s. 133, č. 149 | Dvě sudé derivace s odstupem 2 mají stejné pevné znaménko: zbytek má znaménko prvního nenulového vynechaného členu a menší absolutní hodnotu. Dosazením `2r=m+2` odpovídá Steffensenův zbytek v (9) knižnímu `R_m`; jde přesně o podmínku E11. |
| s. 134–138, č. 150–154 | Přečtený zbytek §14: posunutá sumace, změna kroku, numerický příklad a opakovaná integrace. Není potřebný k nahrazení chybějícího důkazu v knize. |

Steffensen užívá staré `B_1=-1/2`. Přechod TAOCP na `B_1=+1/2` z roku
2021 ponechal Bernoulliho polynomy a sudé koeficienty těchto odhadů stejné.
Žádný nesoulad znamének nevzniká. Již známá oprava roku **1937 → 1927**
z 5. března 2013 je přímo potvrzena oběma titulními stranami originálu.

## Seki: oddělení původního tisku 1712 a sborníku 1974

[Kyoto University RB00000159](https://rmda.kulib.kyoto-u.ac.jp/item/rb00000159)
zpřístupňuje *Katsuyō sanpō*, 括要筭法, ve 112 obrazech. Novou cestou byl
[veřejný IIIF manifest](https://rmda.kulib.kyoto-u.ac.jp/iiif/metadata_manifest/RB00000159/manifest.json),
nikoli dříve neúspěšný NDL prohlížeč. Uložené obrazy jsou původní snímky
instituce; jejich čísla označují pořadí v manifestu, nikoli stránky vydání 1974.

Přímá četba rozhodných míst:

* **Obraz 7 vlevo:** začátek první knihy, 巻元, a jména Araki Murahide
  a Ōtaka Yoshimasa jako Sekiho žáků. Obraz 33 potvrzuje konec 巻元 a
  začátek 巻亨. Tabulka níže tedy patří do první knihy.
* **Obraz 26, listy 19 verso a 20 recto:** původní trojúhelníková tabulka.
  Ve sloupci pokynů pro úrovně 2–12 jsou výslovně předepsány násobky
  `+1/2, +1/6, 0, -1/30, 0, +1/42, 0, -1/30, 0, +5/66, 0`.
  Nula zde přepisuje znak 空, prázdné místo. Jde o dnešní koeficienty
  `B_1,...,B_11`; první úroveň se tímto přepisem neoznačuje za `B_0=0`.
  Obraz 25 obsahuje předcházející výpočty koeficientů, obrazy 27–29
  navazující tabulky součtů mocnin. Pro historický závěr je rozhodná
  přímo čitelná tabulka, nikoli domnělý úplný překlad všech operací.
* **Obraz 110 vlevo:** úvod doslovu výslovně zmiňuje Sekiho úmrtí a
  zbylé rukopisy; dále uvádí Ōtaku a vznik knihy. **Obraz 111 vpravo:**
  tiráž má 正徳二壬辰年正月上旬, druhý rok Shōtoku, tedy 1712.

To je přímý doklad publikace uvedených čísel roku 1712 a posmrtného
charakteru vydání. Kladné `B_1` rovněž souhlasí s dodatkem Knuthových
errat z 21. března 2021. Samotný tisk není důkazem univerzální historické
priority před všemi možnými staršími rukopisy; takový dodatečný nárok
z tohoto dílčího čtení nevyvozujeme.

K orientaci posloužil [odborný text Tsukane Ogawy (2012)](https://www.mathsoc.jp/publication/tushin/1702/1702ogawa.pdf),
přímo obrazově přečtené s. 13–14. Jeho obr. 9 reprodukuje **tentýž
kjótský list** a rozlišuje původní a pozdější podobu autorské hlavičky.
Pomáhá tak s identifikací, ale není vydáván za sborník z roku 1974.
Četba starého textu byla omezená na titulní identifikaci, číselné údaje,
vybrané pokyny, úvod doslovu a tiráž; nebyl přeložen celý japonský spis.

Přesný [NDL záznam vydání 1974](https://ndlsearch.ndl.go.jp/books/R100000002-I000001126639)
identifikuje editory Hirayama, Shimodaira a Hirose, nakladatele Osaka
Kyōiku Tosho a digitální PID **12608851**, ale digitální obsah je omezen
na službu pro knihovny a registrované čtenáře. Žádné stránky tohoto
svazku nebyly získány. **Strany 39–42, jejich vztah k původnímu tisku
a přesné znění moderního komentáře zůstávají source-partial.**
Katalog uvádí místo Tokyo, zatímco Knuth píše Osaka; bez přečtené
tiráže vydání 1974 to zde není hodnoceno jako potvrzená chyba knihy.

## Errata a meze předání

Prohledány všechny čtyři vrstvy `all1-prepre`, `all1-pre`, `all1`, `err1`;
konkrétní výsledky a SHA-256 textových vstupů jsou v
`results/errata-euler-gaps.json`. Přímo obrazově zkontrolována změna
Bernoulliho jména/atribuce (2006), konvence a historické poznámky (2021)
a roku Steffensenova vydání (2013). Vrstvy 2023/2024 obsahují místní
formulační úpravy, které žádný z těchto tří pramenných závěrů nemění.
Nový matematický ani bibliografický nález se tímto paketem nehlásí.

Concrete Mathematics zůstává výhradně v kořenovém úkolu X0689. Dřívější
důkazy E8–E11 a P4–P5 ani jejich testy se neopakovaly. Nové obrazy a
reprodukční logy mají vlastní manifest; starší zmrazené pakety zůstávají
beze změny.
