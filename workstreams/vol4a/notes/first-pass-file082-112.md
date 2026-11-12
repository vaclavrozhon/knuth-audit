# První průchod: file 82–112 / tištěné 65–95

6. listopadu 2026. Celý rozsah přečten v OCR i původní sazbě. Hlavní text
§7.1.1 dokončen; přečtena zadání úloh 1–131 (132–133 jsou až na str.96). Zadání nejsou vyřešené
úlohy a jejich odpovědi zatím nejsou auditované. Žádný nový nález ani kandidát.
V tomto bloku neběžel matematický program, enumerace ani optimalizace.

## Konkrétní obsah a krátké sanity argumenty

- Str. 65–68: mediánové axiomy, intervaly, Lemma M, Theorem G, projekce
  a Theorem C. Přečteny důkazy v textu. V obrázku 7 souřadnicový medián
  bodů (0,2,1), (3,3,3), (2,0,0) skutečně vychází (2,2,1). Ve stromu (63)
  bitové štítky souhlasí s hranami; medián štítků b,g,h je štítek d.
  Úplné odvození distributivity odkazované do úloh nereprodukováno.
- Str. 69–74: Algorithm H a Subroutine I, tabulka 2, median sets, důkaz
  Theorem S a konstrukce Theorem F. Podmínka I4 v prvním tisku je známé
  erratum, viz níže. H není implementován ani znovu formálně dokazován.
  Důkaz S má správný spor: medián tří svědků minimality klauzule délky
  alespoň 3 nesplňuje žádný její literál. Komparátor i invertor zachovávají
  sousednost vstupů lišících se jediným bitem. Dokončení důkazu F odkazované
  do úlohy 89 zůstává ke čtení s odpověďmi; celá síť (74) nebyla simulována.
- Str. 75–78: threshold, majority, Chow parameters, symmetric a canalizing
  functions. U (81)–(84) součet násobností je 2(b+t)−1; převod záporné váhy
  přes negaci proměnné posune práh o její absolutní hodnotu. Důkaz T funguje
  porovnáním součtů vah na rozdílu supportů f a g. U (91) počty jedniček jsou
  v+11 pro v≤3, v+7 pro 4≤v≤6, v+5 pro 7≤v≤9 a v pro 10≤v≤12, jak uvádí text.
  Původní negace v (91)–(94) a canalizing příkladu přečteny; OCR je vynechává.
  Minimality vah v (88)/(89) a velké klasifikace se neověřovaly.
- Str. 78–79: přečteny definice ekvivalencí a tabulky 3–5. Elementární řádky
  arbitrary/self-dual/symmetric odpovídají počtu pravdivostních tabulek,
  komplementárních dvojic a možných Hammingových vah. Ostatní censy ani
  ekvivalenční třídy se nepřepočítávaly.
- Str. 79–95: přečtena všechna zadání 1–131, obrázky, definice a algoritmy
  obsažené v zadáních. Jde o kontrolu formulace a návaznosti, nikoli řešení.
  Příklad úlohy 35 opravdu rozděluje 8 bodů do disjunktních podkrychlí
  11**, 011*, *011 velikostí 4,2,2. Původní zápis shadow používá saturující
  odčítání; není to obyčejné záporné číslo z OCR. U úlohy 39 známá podmínka
  N>0. U úloh 67 a 110(d) zohledněny známé změny. Náročné asymptotické
  odhady, optimální konstrukce, Y konfigurace, censy a otevřené problémy
  zůstávají bez nezávislého řešení či ověřování současného stavu.

## Známá errata a výjimky

Relevantní vrstvy `errata/text/all4a-pre.txt`, `all4a.txt`, `err4a.txt`,
`all4f0.txt`, `err4f0.txt` prohledány podle stran a témat. All4a-pre obsahuje:
str. 68 seven→eight-bit labels (2018) a změnu substituce x=y na y=x (2011);
str. 70 krok I4 doplňuje `or RANK(u) ≠ 1` (2011); str. 73 zápis vektoru x
(2018); str. 74 relaci místo nerovnosti (2011); str. 81 úloha 26 doplňuje
efficiently (2011); str. 84 upřesnění pořadí (2019); str. 85 úloha 39 N>0
(2013); str. 89 prohození částí 67(a)/(b) (2011); str. 93 náhradu 110(d)
(2011); str. 94 index m místo n (2012). Nejde o nové nálezy ani vlastní karty.
Historické F0 opravy jsou přebírány jako historie, nikoli znovu hlášeny.

Bibliografické údaje, autorství a historické priority, odkazy na externí
články/knihy a současný stav otevřených problémů byly výslovně přeskočeny.
Stránkové záznamy v UI používají „First-pass review“; reviewed zde znamená
celou přečtenou stránku, ne certifikaci všech jejích tvrzení.

Doklady: `sources/file082-112-ocr.txt`, `sources/file082-112.pdf` a původní
stránky `images/file082.png` až `images/file112.png`. Offset stále +17.
Další kurzor **file 113 / tištěná 96**, §7.1.2 Boolean Evaluation.
