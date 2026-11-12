# Souvislý průchod §3.3 a §3.3.1 — 6. listopadu 2026

Podklad: třetí vydání, první tisk, září 1997. Obrazově přečteny celé
strany 41–60 a odpovědi 559–562; z 562 zatím pouze odpovědi §3.3.1.
Všech 25 původních úloh bylo porovnáno s důkazy, kódem a uloženými
výsledky. Nová matematická chyba v tomto bloku nepotvrzena.
C0015 a C0016 obstály; C0017 zůstává kandidát. Historické grafy mají
níže uvedené mezery. Tento průchod neprohlašuje celou sekci za dokončenou.

## Matematika textu a úloh

- **41–43, úlohy 1–4.** Machinova identita a racionální interval
  potvrzují 30 číslic π a první opakovanou dvojici 26 na pozicích 6 a 21.
  Nejde o důkaz normality π. Pravděpodobnost sousední shody je v modelu
  nezávislých desetinných číslic 1/10. Sčítání dvou kostek dává trojúhelné
  rozdělení; součet tabulkových počtů je 144. Rozvinutí čtverců převádí
  Pearsonovu statistiku na `sum(Y_s^2/p_s)/n-n`. Čtyři příklady mají
  hodnoty `343/48`, `3539/120`, `137/120`, `1853/240`; odpověď 4 má `33/2`.
  Předpoklady: kladná p, součet 1, nezávislá pozorování. Nulové kategorie
  se odstraní, pozorování v nich okamžitě odporuje nulové hypotéze.
- **44–46.** Všech 112 položek tabulky 1 porovnáno s přepisem v programu;
  přijat historický test kvantilů neúplné gama funkce a nezávislé rekurence.
  Kniha výslovně označuje rozdělení za limitní. Binomický příklad má
  `V=(Y-n/4)^2/(3n/16)`; 28 diskrétních kvantilů a hranice `64/15`
  odpovídají uložené kontrole. Práh zaokrouhlený na 4.27 mění zahrnutí
  hraničního atomu — známá oprava z roku 2017. Doporučení očekávaných
  četností nejméně 5 není rigorózní univerzální mez chyby aproximace.
- **48–51, úlohy 5–9,13,18.** Empirická CDF má po skoku hodnotu j/n,
  před ním (j−1)/n. Proto supremální odchylky dávají přesně (13), i při
  shodách. Reflexe `u_j -> 1-u_(n+1-j)` prohodí obě znaménka, ale
  nečiní je nezávislými; pro n=1 je jejich součet 1. Rozsah je [0,√n].
  Druhá úroveň testu má počet 20, nikoli vnitřní počet 10. Všech 105
  konečných kvantilů tabulky 2 a 7 limitních hodnot odpovídá přepisu,
  odvození a uloženým kontrolám. C0015: `D-=6/125`, percentil je přesně
  `(6/125)(131/125)^19 ≈ 11.6978 %`, nikoli 86 %. Závěr testu se nemění.
- **51–54, úlohy 9–12.** Vícestupňový test je správně kalibrovatelný
  na disjunktních nezávislých blocích; spojitost přesné vnitřní CDF je
  podstatná. Použití limitní CDF chí-kvadrát přidává její aproximaci.
  Tvrzení o lepším rozpoznání místních odchylek není univerzální
  nerovnost síly testů. Duplikace dat násobí V dvěma a K odmocninou ze 2.
  Při pevné alternativě q≠p platí skoro jistě
  `V/n -> sum((q_s-p_s)^2/p_s)>0`; tento důkaz pokrývá i q_s=0,
  kde pomocné Z v tištěné odpovědi 12 není definováno. Pro KS stačí
  zákon velkých čísel v jediném bodě s G(x)≠F(x).
- **55–56, úlohy 14–16,25.** Poissonovy počty podmíněné na součet n
  dávají přesně multinomické pravděpodobnosti. Pro normalizovaný vektor
  je kovariance `I-uu^T`, u_s=√p_s; na kolmém podprostoru má normální
  limita k−1 nezávislých souřadnic. Radiální integrace a substituce
  t=r²/2 dávají (22). Lokální Stirlingův odhad v úloze 14 má absolutní
  zbytek `O(n^(-k/2))` pro pevná kladná p a omezená Z, nikoli uniformně
  pro p→0 či rostoucí k. Kolmé sloupce polárního Jacobiánu dávají
  uvedený součin sinusů. Gama rozvoj dává kvantil
  `ν+sqrt(2ν)x_p+2x_p²/3-2/3+O(ν^(-1/2))`.
  Pro úlohu 25 z `C=AA^T`, `CGC=C` a levé inverze L matice A vyjde
  `A^TGA=I`; tvrzení platí i pro nesymetrickou G. Normální rozdělení je
  potřeba až pro závěr o rozdělení součtu čtverců.
- **57–58, úloha 17.** Transformace F(X) je rovnoměrná pro spojitou F;
  ploché úseky mají nulovou hmotnost, krajní hodnoty 0 a 1 se ošetří
  limitou. Uspořádaný simplex má objem n^n/n!. Vnořené integrály,
  posun o t, indukce pro P_n0 a teleskopování přes k dokazují oba
  distribuční součty (25),(26). V algebraických krajních případech
  nejprve krátíme odstranitelné singularity; pro t≤0 je CDF 0, pro
  t≥n je 1. Součet v (25) numericky ruší velké členy. Nezápornost
  členů v (26) neodstraňuje ztrátu relativní přesnosti při odečítání
  výsledku blízkého 1.
- **Úloha 20.** Znovu porovnány Lauwerierovy (1.4),(2.5),(2.6),(3.9)–(3.14)
  v reportu TW90/62 a vlastní algebra v `kolmogorov-smirnov.md`.
  Koeficient `1/n` je `(3-He_4(2s))/36=2s²/3-4s⁴/9`, přesně kniha.
  Deformace kontury a odhad vzdálených částí jsou převzaté z primárního
  důkazu; nejde o nové úplné analytické odvození. Vyšší chybný index
  He_4 místo He_5 v reportu není chyba Knuthovy odpovědi. Režim je
  pevné s>0; s=0 má přesnou CDF 0. Numerický zbytek sám asymptotiku nedokazuje.
- **Úlohy 19,21,22.** Znovu přečteny vlastní konečné konstrukce v
  `ks-generalizations.md`. Vícerozměrná distribuce není univerzální
  (FGM příklad má E D+=3/4−θ/18); kvantilová mřížka, Bernoulliho
  exponenciální odhad a sjednocení dávají platnou konzistentní kontrolu.
  Pro diskrétní F se supremum bere v kumulativních atomech, nikoli
  spojitým vzorcem (13); randomizace uvnitř atomů dokazuje konzervativnost
  pouze horního spojitého prahu. Přesná srovnání síly jsou kalibrována
  randomizací na hraničním atomu. Vážená statistika odpovědi 6 vyžaduje
  `0<F(x)<1` a vlastní kalibraci: pro n=1 má CDF s²/(1+s²), nikoli
  tabulku 2. Odvození monotónnosti, kvadratické hranice a dvou výpočtů
  objemu simplexu souhlasí. Tyto výzkumné úlohy nepožadují ani náš audit
  netvrdí globální optimalitu všech zobecnění.
- **Úlohy 23–24.** Při m≥n rozdíl pořadových indexů převáží šířku
  přihrádky; stačí její počet, minimum a maximum. Knižní předpoklad
  F(X_j)<1 je výslovný. Čas je O(n+m); nahrazení středy posune každé
  pořadové pozorování nejvýše o 1/(2m), a tedy K nejvýše o √n/(2m).
  Přijaty dva přesné modely tříkategoriálních experimentů; jejich
  výsledek ukazuje i nemonotónnost konečné chyby kalibrace.

## Historické obrázky a mezery

Pro B/C/D/F je potvrzeno 60 prvních klasifikací obrázků 2 a 5 z
uložených výstupů. Kód, přepis všech použitých symbolů, vstupní parametry
a souhrny byly znovu přečteny; žádný proud se znovu negeneroval.
Další sloupce závisí na neúplně popsaném výběru bloků, A/E nebyly
zrekonstruovány. Číselné statistiky obrázku 4 a vnějšího testu (12)
nejsou přesně reprodukovány. C0017 má silné, ale podmíněné vodítko:
první tisícovky B/F dávají čtyři hodnoty (16) s obrácenými znaménky
a současně V=9.4 a 39.3; historický seed/začátek tohoto experimentu
není doložen. Strany **47,49,50,52,54** proto zůstávají částečné.
Nesoulad není omluven drahým výpočtem a není potvrzenou chybou.

Mechanismus Fibonacciho vady je doložen samostatně: pro rovnoměrný
počáteční pár zachovává zobrazení (u,v)→(v,u+v mod 1) plochu, ale pro
0<x≤1/2 má maximum pěti členů CDF x²/12, zatímco nezávislý model má x⁵.
Nejde o rekonstrukci seedů historického E. Mocnina 23^k vysvětluje
přeskakování stavů ENIACu, neprokazuje však nezávislost. Osobní historii
odběru hodnot jsme nepřevzali jako ověřenou událost.

## Prameny a errata

Čtyři vrstvy errat stažené 6. listopadu jsou shodné s dřívější kopií;
relevantní výřezy jsou v `sources/sequential-2026-11-06/general-tests-errata.json`.
X0094 eviduje původní strany **41,46,48,50,54,56,57,559,560**: doplnění
autorství příkladu π, přesný diskrétní práh, `fracton`, supremum,
milisekundy, kouli místo vnitřku hypersféry a Smirnovovy strany.
Oprava uvedená v nových erratech na 57 ř.3 patří v našem prvním tisku
na **56, rovnici (23)** — pozdější odstavec Valiantových změnil zalomení.
Původní odpověď 13 vědomě vysvětluje užití „max“ místo „sup“; nové erratum
tuto historickou poznámku maže. Úpravy stylu na 43, vysvětlení osy na 49
a přemístění vysvětlivky v odpovědi 16 na 561 nejsou nové početní chyby.

Pearsonovy původní strany 1897/45,54 a 1900/169 znovu vizuálně porovnány:
4274 sérií má stejnou tabulku, zdrojem byly publikované záznamy Le Monaco.
C0016 se týká tohoto původu, nikoli tvrzení, že Pearson nikdy nebyl
v Monte Carlu. V našem starém textu opravena iniciála de Whalleyho na L. G.;
to není chyba TAOCP. Historický řád 10²⁹ odpovídá Pearsonovu uvedenému
14.5/10³⁰; kalibraci tohoto extrémního historického odhadu zde neobnovujeme.

Metadata [archivu Smirnovova článku](https://www.mathnet.ru/eng/rm8798)
potvrzují známou opravu 179–206. [Sahniho autorský seznam](https://www.cise.ufl.edu/~sahni/s.htm)
potvrzuje 1977, sv.3, 60–64; odkaz na PDF znovu vrací 404.
Lauwerierův report má ověřenou matematickou souvislost, nikoli přesnou
časopiseckou sazbu 1963. Valiantův doplněk byl porovnán s autorským
manuskriptem, algoritmem a momenty: „superior“ se vztahuje k počtu vzorků
v testování známého rozdělení a vyžaduje oddělení lehkého ocasu i
největšího atomu. Nelze jen zaměnit statistiku a ponechat starou tabulku.
Hluboký optimalitní důkaz nebyl celý nově auditován.

Přeskočeno: plná Gardnerova citace a Huffova kniha, přesná zdrojová
tabulka Abramowitz–Stegun 26.8, primární priority Kolmogorova/Smirnova,
plné články Cochran/Doob/Donsker/Birnbaum–Tingey, celá Durbinova monografie,
časopisecký Lauwerier 1963, původní Gonzalez et al. 1977 a citovaná sekce
Golub–Van Loan. Vlastní matematické důkazy tím nejsou nahrazeny pouhými citacemi.

## Přijetí starých výpočtů a pokračování

Přečteno všech sedm kontrolních programů, výsledky a dokončovací logy.
První chí-kvadrát běh skončil až po úspěšných tabulkách a 16 experimentech
na chybě API SymPy; podrobné prefixové hodnoty se neuložily. Přijímáme
přesně rozsah dokládaný logem, nikoli údajný kompletní úspěšný první běh.
Obnovení dopočítalo 60 matic a 80 gama případů. KS první běh uložil
265 racionálních kontrol a 36 polynomů před chybou API; obnovení dokončilo
105 kvantilů, 3760 multisouborů a 25355 přihrádkových porovnání.
Ostatní výsledky mají dokončovací záznamy. Nic z toho nebylo restartováno.
Hash přijatých artefaktů obsahuje `results/sequential-general-tests-review.json`.

Další kurzor: **§3.3.2, strana 61, odpovědi 562**. Strana 559 je nyní
pročtena celá, 562 zůstává sdílená a částečná. Otevřené historické
experimenty a C0017 jsou vedeny zvlášť; nejde o záminku zastavit další průchod.
