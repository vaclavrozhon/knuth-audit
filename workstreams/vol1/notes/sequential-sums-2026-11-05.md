# Souvislý průchod §1.2.3: součty, součiny a matice

5. listopadu 2026. Přečteny originály s. 27–39 a odpovědi 471–475,
porovnány celé důkazy `sums-and-products.md`, `matrices.md` a závěrečná
recenze `sums-final-root-review.md`. Přijata dříve dokončená pramenná
revize; historický závěr C0088 znovu porovnán s
`kronecker-date-root-review.md`. Dřívější výpočty se neopakovaly.
Strana 39 zůstává jako celek částečná, protože začíná následující oddíl.

Matematika hlavního textu a všech 47 původních úloh je uzavřena včetně
doložených oprav. Doporučená kapitola 12 prvního vydání Apostolovy
Mathematical Analysis (1957) nebyla dostupná a nyní je podle nového
zadání výslovně přeskočena. X0764 zůstává pramenně partial: změna
pracovního rozsahu není důkazem přečtení knihy. Hlavní text §1.2.3 tak
může být checked s bibliografickou výjimkou.

## Přímá matematická revize

- Součet přes množinu indexů a orientovaný intervalový součet mají
  odlišné chování při obrácených mezích. Model z X0762 je konzistentní;
  původní C0004 zůstává dismissed. Dodatky 2010/2022 neprokazují rozpor.
- Oboustranné nekonečné součty se definují oddělenými jednostrannými
  limitami. Známá oprava (3) odstraní dvojí započtení indexu 0.
  Libovolné přeuspořádání se používá při absolutní konvergenci;
  konečné posuny/reverze mají vlastní jednodušší zdůvodnění.
- Součin dvou součtů, záměna konečných sumací, Iversonovy závorky,
  aritmetické a geometrické řady i trojúhelníková identita jsou správné
  po započtení zveřejněné opravy indexu na s. 33.
- Příklad dvou nekonečných pořadí součtu v úloze 8 se neopírá
  o neplatné použití absolutní konvergence. Diagonály +1 a −1 mají
  odlišné iterované součty. Úloha 18 používá kladné celé n;
  projekce indexů v novém zadání/odpovědi 2019 byla porovnána.
- Teleskopování v 19 obsahuje indikátor m≤n v množinové konvenci.
  V 26 se každý faktor a_r vyskytne n+2krát, a to i pro záporné a_r
  nebo nulu. Trojitý symetrický součet v 29 dává
  (S1³+3 S1 S2+2 S3)/6 rozdělením podle shod indexů.
- Binetova identita a komplexní Cauchyho–Schwarzova nerovnost byly
  porovnány včetně všech konjugací. Lagrangeova interpolace v 33/34
  vyžaduje různé uzly; koeficient nejvyšší mocniny dává uvedené sumy.
  Reziduová varianta používá R větší než všechny |x_j|, takže lze
  integrovat rovnoměrně konvergentní Laurentovu řadu po členech.
- Pravidla pro supremum platí tam, kde jsou příslušné rozšířené
  operace definované. Nevyvozujeme hodnotu z výrazů ∞−∞ nebo 0·∞.
  Zápis maxima dvou suprem opravuje zveřejněná změna z roku 2024.
- Determinanty a inverze kombinatorické, Vandermondovy a Cauchyho
  matice byly porovnány s obecnými důkazy, včetně znamének a transpozice
  kofaktorů. Inverze vyžadují příslušnou nesingularitu a nenulové
  jmenovatele; odmítnuté chyby pomocného OCR se nevracejí jako nálezy.
- U Hilbertovy matice jsou správné faktoriálové i binomické tvary
  inverze, celočíselnost, vypsané dělitelnosti a součet n². Její špatná
  podmíněnost je doložena obecným Rayleighovým odhadem v původní
  poznámce, nikoli jen několika zaokrouhlenými numerickými experimenty.
- Binetova–Cauchyho formule zahrnuje i m>n: výběr různých indexů je
  prázdný a součin má nedostatečnou hodnost. Krattenthalerův determinant
  má správné znaménko a normalizaci; počet přidaných nezávislých
  parametrů opravuje známé erratum na n−2.

## Znovu posouzený skalární okraj úlohy 39

Pro n≥2 je x(x+ny)≠0 ekvivalentní invertibilitě xI+yJ.
Pro n=1, x=0, y=1 je matice [1] invertibilní, ale dosazení do
nezkráceného racionálního výrazu v zadání dává 0/0. Po symbolickém
zkrácení je b11=1/(x+y), tedy správně 1. Tuto výjimku už původní
`matrices.md` výslovně zachycuje. Nejde o nový protiargument vůči
polynomické rovnosti v odpovědi 39 ani vůči racionální identitě na
jejím definičním oboru. Nepřidáváme potvrzenou chybu z obecně užívané
konvence, že se racionalní vzorce vyhodnocují tam, kde jsou definované.
Při případné implementaci je však nutné n=1 ošetřit nebo výraz nejprve
zkrátit; tvrzení, že nezkrácený vzorec je definován pro každou
invertibilní reprezentaci xI+yJ, by bylo nepravdivé. Tato hranice je
součástí přijatého rozsahu kontroly, ne zamlčené numerické selhání.

## Nálezy a známé opravy

C0003 zůstává potvrzená chyba **doplněné odpovědi v erratech 2020**.
Rovnost P1=√(P1P2) ztrácí znaménko už pro n=1, a0=−1, a1=1.
Původní odpověď z roku 1997 tuto rovnost neobsahuje a její konečný
vzorec je správný. UI proto používá druh `errata` a původní s. 472
je pouze související stránka, ne místo této nové chyby v knize.

C0088 je již doložené nesprávné datování Kroneckerovy delty na s. 33.
Nejde o novou chybu nalezenou dnes. Matematická definice je správná;
původní zpráva 1866 byla prokazatelně vytištěna nejpozději v roce 1867.

X0937 doplňuje do mapy dosud neseskupené drobné zveřejněné opravy:
chybějící a_j na s. 27 (16. 7. 1997), nesprávný odkaz zadání 21
na s. 35 (7. 2. 2004), sup→max na s. 473 (7. 2. 2024) a rozlišení
kofaktoru od matice na s. 475 (15. 10. 2007). Významnější již
evidované X0037–X0042 a X0045 nejsou duplikovány dalšími kartami.
Změna vysvětlující věty úlohy 40 z roku 2020 se týká později přidané
věty, kterou náš první dotisk ještě nemá; nebarvíme kvůli ní s. 38
červeně. Doplnění kofaktoru pro n=1 a svislých teček je upřesnění.

Čtyři vrstvy all1-prepre/all1-pre/all1/err1 prohledány podle stran
i témat. Jejich originály jsou dnešní obnovené, se shodnými hashi
v `sources/sequential-2026-11-05/errata-refresh.json`. Rozhodující
erratové obrazy 6, 31, 14 a 11 byly přímo přečteny. Žádný nový
dosud nepublikovaný nález se tímto blokem nepotvrzuje.
