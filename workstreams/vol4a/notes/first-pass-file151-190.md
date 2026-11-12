# První průchod: file 151–190 / tištěné 134–173

6. listopadu 2026. Celý rozsah §7.1.3 přečten v OCR i původní sazbě,
včetně tabulek, algoritmů a obrázků. Žádný nový nález ani kandidát.
Neběžel matematický program, census ani simulace. Následuje str.174.

## Konkrétní kontroly a meze

- Str.134–139: bitové operace, nekonečné dvojkové doplňky, identity(4–21),
  posuny, balení dat a endianita. Původní negace v(18) souhlasí; date packing
  512y+32m+d a masky správně zachovávají pořadí platných dat. Prvočíselné
  konstanty a quilt přečteny, nikoli všechny bity přepočítány. MMIX LDOU
  při indexu k>>3 zarovná adresu na správný osmibajt; emulátor nespouštěn.
- Str.140–145: pravá/levá krajní jednička, ruler, de Bruijn, popcount,
  reverzace a delta swap. Formule32–43 odpovídají tvaru a01…10…0; u(58)
  sazba obsahuje ≤. Popcount sčítá dvojice/nybbly/bajty bez přetečení
  dílčích součtů. XOR rozdílu v(69) prohazuje obě pozice. Všech64 položek
  de Bruijn tabulky a exotická reverzace(70) nebyly zvlášť reprodukovány.
- Str.146–151: Benešova síť, transpose, shuffle/compress, gather-flip,
  podmnožiny a rozptýlená aritmetika. Důkaz sítě používá sudé cykly
  bipartitního 2-regulárního multigrafu, včetně dvojitých hran. Formule86
  propouští carry přes nemaskované bity; bajtové sčítání87 odděluje horní
  bity a průměr88 maskuje mezibajtový posun. Plné routování neimplementováno.
- Str.152–155: Mycroftův nulový bajt, přesné flagy91, byte compare93,
  broadword logaritmus95/Algorithm B a pattern01^r. Přečteny i původní
  negace a omezení n,r. Pravá versus levá nulová pozice je správně rozlišena.
  Důkazy dlouhých formulí95/98 a úplná optimalita počtů kroků jsou odloženy
  do odpovědí106/111; rychlé přečtení je nenahrazuje.
- Str.155–159: definice chain, shift sets, Lemma A/B, Theorems R/P/R'/P'.
  Prošel jsem předpoklady, dependency/carry argument a návaznost mezí.
  Corollary I má v sazbě monus, nikoli obyčejné x−1. Známou opravu důkazu R
  uplatňuji. Úplné odvození externích RAM mezí z úloh124/125 ani současný
  stav otevřených otázek neověřen.
- Str.159–163: Algorithm/Program R, 3hodnotové kódování a Łukasiewiczovy
  tabulky. R udržuje X⊆R, proto r−x skutečně kóduje R\X. Příklady násobení
  a max souhlasí s významem bitů; redundantní nula v(120) umožňuje dvě
  operace(122). Třídám odpovídá 24 jednoznačných +36 nejednoznačných kódů.
  Minimální náklady obvodů nebyly znovu syntetizovány.
- Str.164–167: heaps, sideways heap, rodiče/potomci, NCA a Algorithm V.
  Přečteny obě tabulky v(141–143), inkluzivní význam předků/potomků a
  součet přes množinu v(140), který neopakuje stejné mocniny. Malý příklad
  souhlasí s obrázkem; univerzální důkaz V a navigation-pile bound zůstává
  v příslušných dosud nečtených odpovědích. Žádná generace stromů.
- Str.167–171: hyperbolická geometrie, pentagrid, negaFibonacci kódy,
  sousedé a druhá souřadnice. Přečteny vzdálenost i tabulka kódů a orientace
  obrázků. V(149) je doplněk μ0; OCR jej ztrácí. Nekonečné pokrytí pravidly
  a globální jednoznačnost souřadnic nebyly znovu dokázány.
- Str.171–173: bitmapy, custering, 3×3 automata a první část thinning.
  De Morganův přepis157 a počet2^512 pravidel souhlasí. Přečteno37
  konfigurací a čtyři doplňky; simulace Guo–Hallova automatu a reprodukce
 25krokového řetězce se nedělala. Zachování topologie pokračuje na174.

## Errata a výjimky

Prohledány `all4a-pre`, `all4a`, `err4a`, `all4f1`, `err4f1`.
§7.1.3 odpovídá fasciklu4F1, jeho strany1–41 jsou zde133–173 (offset132).
Fasciklové doplňky Benešovy sítě, gather-flip a inkluzivních předků již
jsou v tomto dotisku. Známé pozdější opravy: str.134 mature trick;
140 replace by zero a proměnnáy v44; 142 truncated shifts (2022);
153 šestikrokový compare; 157 průnik s V je prázdný; 169 doplněná citace;
171 odkaz naFig15b; 172 begin with; 173 one, two, or three místo at least two.
Vše je pouze zohledněno, bez vlastních karet či nálezových lokací.

Bibliografie, autorství a historické priority včetně strojové historie,
výkonnostních anekdot, externích publikací a nynější otevřenosti problémů
neověřeny. Čtení odkazů na cvičení neznamená jejich vyřešení. Reviewed zde
znamená celou přečtenou stránku s těmito výjimkami, ne certifikaci všech vět.

Doklady: `sources/file151-190-ocr.txt`, `sources/file151-190.pdf`,
`images/file151.png` až `images/file190.png`. Offset file=printed+17.
Další kurzor **file191 / tištěná174**, pokračování bitmapové topologie.
