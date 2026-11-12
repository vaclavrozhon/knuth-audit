# §4.3.3: paralelní obvody a historický kontext

Kontrola 2. listopadu 2026 uzavírá zbývající text oddílu v níže uvedeném
rozsahu. Matematické jádro a všech 19 cvičení mají samostatné poznámky
`fast-*.md`. Původní stránky knihy 294–318 byly přečteny v předchozích
blocích; zde byla znovu porovnána zejména strana 311. Bibliografické
ověření není tvrzením o nezávislém důkazu celých citovaných článků.

## Hloubka paralelního násobiče, strany 315–316

Hloubkou rozumíme největší počet logických hradel na cestě od vstupu
k výstupu; každé hradlo má omezený počet vstupů a konstantní zpoždění.
Obě n-bitová čísla jsou dostupná najednou. Tvrzení knihy o hloubce
`O(log n)` lze doložit přímo:

1. Vytvoříme `n^2` bitových součinů AND a uspořádáme je do n posunutých
   řádků šířky 2n. Jejich součet je hledaný součin.
2. Pro tři bity stejné váhy platí `x+y+z = s+2c`, kde
   `s = x XOR y XOR z` a `c = (x AND y) OR (x AND z) OR (y AND z)`.
   Současným použitím v každém sloupci tak nahradíme tři řádky dvěma,
   bez šíření přenosu podél řádku. Jedna taková vrstva má konstantní
   hloubku a zachovává součet.
3. Je-li h počet řádků před vrstvou, nový počet je
   `h' = 2 floor(h/3) + (h mod 3) = ceil(2h/3)`.
   Pro `h >= 3` máme `h'-2 <= (2/3)(h-2)`, takže po `O(log n)`
   vrstvách zbývají dva řádky. Celkem použijeme `O(n^2)` hradel.
4. Poslední dvě čísla sečteme pomocí stromu přenosů. Pro bit a,b položme
   `G = a AND b`, `P = a XOR b`: přenos c se zobrazí na `G OR (P AND c)`.
   Dva po sobě jdoucí úseky se tedy skládají předpisem

   ```text
   (G2,P2) o (G1,P1) = (G2 OR (P2 AND G1), P2 AND P1).
   ```

   Skládání je asociativní, protože jde o skládání funkcí přenosu.
   Zdvojováním délky úseků získáme všechny prefixové přenosy v
   `O(log n)` vrstvách. Potom zbývá bitové XOR pro výsledné číslice.

Všechny řádky jsou nezáporné a jejich součet je menší než `2^(2n)`,
takže šířka 2n stačí. I při omezeném počtu výstupních větví hradla
lze vstupy rozkopírovat binárními stromy za dalších `O(log n)` vrstev.
Nejde o odhad fyzického zpoždění konkrétního rozmístění spojů na čipu.

[Wallaceův původní článek](https://www.ece.ucdavis.edu/~vojin/CLASSES/EEC280/Web-page/papers/Arithmetic/Wallace_mult.pdf)
byl získán jako přetisk. Vizuálně byly přečteny PDF strany 1–2
(přetisk 114–115, původní článek 14–15). Popisuje právě redukci tří
sčítanců na dva a strom s logaritmickým počtem vrstev. Titulní údaj
potvrzuje *IEEE Transactions on Electronic Computers* EC-13 (1964),
14–17. Jeho historické časy jednotlivých obvodů zde znovu neměříme.
Samostatný program pro uvedenou jednoduchou algebraickou identitu
by nepřidal nezávislý důkaz, proto nebyl psán.

## Little Fermat, strana 311

Matematický základ popsaného konvolučního jádra je správný i bez
předpokladu, že `m = 2^256+1` je prvočíslo. Pracujeme v okruhu zbytků
modulo m a volíme délku transformace `K = 256` a kořen `omega = 4`.
Platí `omega^128 = -1` a `omega^256 = 1` modulo m. Pro
`0 < j < 256`, `j = 2^s t` s lichým t, se členy součtu
`sum_(r=0)^255 omega^(jr)` vyruší v párech vzdálených
`2^(7-s)` uvnitř bloků délky `2^(8-s)`. Součet je tedy nula.
Číslo 256 má modulo m inverzi, neboť m je liché. Tím jsou doloženy
ortogonalita transformace, její inverze i konvoluční věta.

Dvě dopředné a jedna zpětná transformace proto potřebují 256
bodových násobení. Ostatní násobitele jsou mocniny dvou a realizují
se posuny a znaménky modulo m; totéž platí pro dělení 256.
Kanonické zbytky `0,...,2^256` skutečně vyžadují 257 bitů.
Toto dokazuje konvoluci modulo m, nikoli bez dalšího libovolně
dlouhý celočíselný součin: při převodu je nutné omezit koeficienty,
doplnit nuly a zpracovat přenosy, případně použít více konvolucí.

Časy pod 0,1 s pro milion bitů a přibližně 60 ns na cyklus nebyly
nezávisle reprodukovány ani ověřeny z technické dokumentace stroje.
Citované strany sborníku 1988 a *Contemporary Mathematics* 143
(1993), 136, nebyly získány. Dobová reportáž
[Richarda Prestona](https://www.newyorker.com/magazine/1992/03/02/the-mountains-of-pi)
potvrzuje existenci stroje a jeho konstruktéry; neověřuje uvedené
technické parametry. Toto omezení není důvod označit časový údaj
za chybný. Překlep `than` místo `then` již opravuje erratum
29. prosince 1997; upřesnění vydavatele sborníku je z 2. března 2011.

## Brentova mez pro elementární funkce, strana 313

[Původní Brentův článek](https://maths-people.anu.edu.au/~brent/pd/rpb034.pdf)
byl získán z autorova archivu. Vizuálně byly přečteny tištěné strany
242–243, tedy abstrakt a úvod s přesnými předpoklady. Citace
*JACM* 23 (1976), 242–251 souhlasí. `M(n)` značí cenu násobení
n-bitových čísel. Článek předpokládá cenu sčítání `O(M(n))` a slabou
regularitu `M(alpha n) <= beta M(n)` pro vhodné pevné
`0 < alpha,beta < 1`. Na vhodném pevném konečném intervalu argumentů
pak uvádí cenu `O(M(n) log n)` při relativní chybě `O(2^-n)`.
Výsledek platí také pro vícepáskový Turingův stroj.

Stručný odkaz v knize tak odpovídá citovanému výsledku při jeho
standardních doménových a nákladových předpokladech. Nevykládáme
jej jako uniformní odhad pro neomezeně rostoucí exponent argumentu
nebo jako relativní přesnost v nule funkce. Celý důkaz využívající
eliptické integrály zde nebyl znovu auditován. Algoritmus R a redukce
dělení na násobení mají vlastní nezávislý důkaz v `fast-reciprocal.md`.

## Historie a bibliografie

- **Karatsuba, 295:** opravy z 15. listopadu 2016 a 12. listopadu 2018
  oddělují odkaz na publikaci 1962 od objevu 1960. Tikhomirovův
  [dopis z roku 2013](https://www.mathnet.ru/rus/rm9547) obsahuje
  svědectví o podzimu 1960; jeho anglický text byl dostupný ve webovém
  vyhledávání, přímé stažení skončilo 403. Nevydáváme jej za lokálně
  přečtený sken ani za důkaz absolutního historického prvenství.
- **Toom a Cook, 296–297:** [Toomův autorský seznam](https://cs-web.bu.edu/faculty/gacs/toomandre-com-backup/my-articles/rusmat/index.html)
  potvrzuje ruský článek 150(3), 496–498 (1963).
  [Cookova stránka](https://www.cs.toronto.edu/~sacook/) potvrzuje
  disertaci uvedeného názvu z roku 1966 a nabízí její kapitolu III;
  následný odkaz skončil chybou 502. Přesné stránky disertace 51–77
  a anglický Toomův překlad nebyly z vlastních skenů zkontrolovány.
  Důkazy algoritmu v knize byly provedeny samostatně.
- **Schönhage, 305–311:** [autorův seznam](https://pages.iai.uni-bonn.de/schoenhage_arnold/publis.html)
  potvrzuje *Computing* 1 (1966), 182–196, a společnou práci se
  Strassenem, *Computing* 7 (1971), 281–292. Zároveň rozlišuje
  krátký text o pointer machines z 1979 od časopisové práce 1980.
  Kompletní externí konstrukce páskového algoritmu není součástí
  tohoto bloku. Novější mez Harvey–van der Hoeven je popsána v
  `fast-online.md`; není zde tvrzena její současná optimalita.
- **Pollard, 306:** dostupný [původní článek](https://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/2004932.pdf)
  ve webové textové vrstvě potvrzuje transformaci nad konečným tělesem
  a aplikaci na konvoluce. Bibliografický rozsah 365–374 potvrzuje
  obsah časopisu. Celý důkaz článku nebyl čten; knižní transformace
  je nezávisle doložena v `fast-fft.md`.
- **Atrubin, 315:** dobová bibliografie NBS i bibliografické záznamy
  uvádějí EC-14 (1965), 394–399. [Stránka vydavatele](https://ieeexplore.ieee.org/document/4038457/)
  vyžádala kontrolu prohlížeče; původní článek nebyl získán a jeho
  detaily zde nepovažujeme za ověřené. Knižní automat byl ověřen
  vlastním invariantem a přesnou simulací v `fast-automata.md`.
- **Winograd, Yao, Mansour–Nisan–Tiwari, 316:**
  [ACM](https://doi.org/10.1145/321420.321438) potvrzuje Winogradovu
  studii času násobení a stránky 793–802. [Yaoův seznam](https://iiis.tsinghua.edu.cn/rydw/qzjs/yaoqizhi.htm)
  potvrzuje *The Entropic Limitations on VLSI Computations*, STOC
  1981, 308–311. [ACM](https://doi.org/10.1145/100216.100246)
  potvrzuje STOC 1990, 235–243. Abstrakt
  [souvisejícího konferenčního sdělení stejných autorů](https://ieeexplore.ieee.org/document/113957/)
  výslovně zahrnuje `a+b*c` při libovolném kódování prvků tělesa.
  Jde o kontrolu relevance odkazů, nikoli o nové ověření všech dolních mezí.
- **Maeder, odpověď 18:** [vydavatel](https://link.springer.com/chapter/10.1007/BFb0013168)
  potvrzuje LNCS 722 (1993), 59–65 a obsah práce o pomocné paměti.
  Plný text je za předplatným a nebyl čten. Naše konstrukce paměti
  v `fast-late.md` na něm nezávisí.
- **GraphBase a Halliwell, 316:** uvedené stránky knihy *The Stanford
  GraphBase* ani původní rukopis říkanky nebyly získány. Přesný
  literární přepis a datování kolem 1570 zůstávají neověřené; různé
  pozdější verze říkanky samy nedokazují chybu této citace.

## Závěr evidence

Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
byly znovu prohledány podle stran, jmen a témat. Kontext nepřidal
nový kandidát. §4.3.3 je uzavřena jako audit vlastního matematického
textu, všech 19 úloh a citací v popsaném rozsahu; nezískané historické
podklady a neauditované externí důkazy jsou výše výslovně odděleny.
Potvrzené nálezy oddílu C0103, C0104, C0106 a kandidáti C0105, C0107
zůstávají ve vlastních záznamech. Nejnovější fyzický dotisk ani
prvenství hlášení nejsou ověřeny.
