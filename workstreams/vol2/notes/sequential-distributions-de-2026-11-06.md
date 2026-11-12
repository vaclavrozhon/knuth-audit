# Souvislá revize §3.4.1 D/E: další spojitá rozdělení

6. listopadu 2026, X0119 a X0120. Znovu přečteny původní strany
132–136, zadání16 na140 a odpověď586–587. Rovnice, algoritmy a
úloha16 obstály po známé opravě Studentova jmenovatele. Nový nález
nepřibyl. Celá §3.4.1 zůstává partial; tento blok neuzavírá její
dřívější mezery ani nově výslovně vymezené historické srovnání rychlosti
na134. Stránky souboru mají číslo o12 vyšší než tištěné.

Úplné důkazy jsou v [původním zápisu](distributions-other.md), jehož
rovnice byly nyní znovu přezkoumány proti sazbě. Přečten byl také celý
`verify_distributions_other.py`, všechny tři bloky protokolu PASS a
relevantní výsledky. Dřívější výpočet nebyl znovu spuštěn. Hashovaný
manifest je `results/sequential-distributions-de-review.json`.

## Matematický rozsah

- Exponenciální zákon a transformace −μ ln U: μ>0; radioaktivní příklad
  čteme jako obvyklý homogenní Poissonův model. Samotný průměr obecné
  posloupnosti příchodů by exponenciální čekací dobu neurčoval.
- Algoritmus S: pro L=ln2 mají směšovací váhy L^k/k! součet1.
  Hustota minima po škálování je 2 exp(−z), 0<z<L. Nezávislý počet
  úvodních jedniček má hmotnost2^(−j−1), takže spojený výstup je
  exponenciální. Větev k=1 správně recykluje podmíněně rovnoměrné U.
  Celková ideální střední spotřeba celých vstupů je1+ln2; počet
  odstraněných bitů má střed2. U konečného slova doplněného nulami
  je konečný ocas a atomy, nikoli přesný spojitý zákon. Mez tabulky
  Q[k]>1−2^(−t) stačí i pro původní samé jedničky. Sedm uložených
  minimálních délek tabulky bylo přijato bez opakování výpočtu.
- Gamma zákon: případy a=1 a1/2, součet nezávislých gamma veličin,
  součin uniformních čísel a riziko podtečení souhlasí. Jacobián
  substituce (X,Y)=(RT,R(1−T)) má absolutní hodnotu R a dokazuje
  zároveň beta poměr i nezávislost poměru a součtu.
- Odmítací algoritmus A: pro k=a−1, b²=2k+1 platí na y>−k/b
  `(ln r)'=−y(by−1)²/((1+y²)(k+by))`. Tím je dokázána globální
  obálka r≤1, i když symbolický verifier deklaruje y kladné:
  jeho nulový polynomiální zbytek dokazuje identitu i pro záporné y.
  Cena C(k)=π√(2k+1)k^k exp(−k)/Γ(k+1) klesá pro k≥2 podle
  uvedeného integrálního odhadu digamma. Maximum při a=3 je
  1.90141058262025…<1.902. Nejde pouze o kontrolu vzorku parametrů.
- Úloha16: obě části obálky, jejich normalizace, p=e/(a+e),
  recyklace U v obou větvích i okamžité přijetí U<p/e jsou správné.
  Pravděpodobnost posledního případu je1/(a+e), tedy přibližně
  27–37 procent pro0<a≤1; formulace „asi30 procent“ je přiměřená.
  Celou mez c<1.4 pokrývá200 uložených intervalů, nejvyšší horní
  mez je menší než1.391632. Numerická poloha maxima a≈.799069
  slouží pouze jako orientace; není náhradou důkazu. Bod a=0 je
  použit jen jako spojitá limita ceny, nikoli povolený parametr.
- Beta: gamma poměr, Jöhnkovo podmínění na Y1+Y2≤1 a pořadová
  statistika souhlasí. b-tá největší z a+b−1 je a-tá nejmenší.
  Uložených576 přesných momentů potvrzuje zvolenou parametrizaci.
- Chi-square a F: škála2 gamma(ν/2), poměr nezávislých chi-square
  a transformace ν2*T/(ν1*(1−T)) dávají přesně hustotu(36).
- Student: běžný poměr normálního a odmocniny chi-square dává(37).
  U alternativy ν>2 položme k=ν−2. Přijaté Y má hustotu úměrnou
  `(1−y²/k)^(k/2)` na |y|<√k. Po opravené transformaci
  `X=√ν*Y/√(k−Y²)` dává inverze a její Jacobián exponent
  −(ν+1)/2, přesně podle(37).
- Náhodné body: radiální symetrie normálního vektoru dává rovnoměrný
  povrch; nezávislé U^(1/n) dává objemovou radiální CDF r^n.
  Ve3D je diskový čtverec poloměru S uniformní, Z=2S−1 uniformní
  na[−1,1] a plošný element je dθ dZ. Úspora součtu čtverců
  pomocí −2 ln S souhlasí s polárním generátorem. Nulový vektor
  je nulová událost ideálního modelu, nikoli nově nalezená chyba.
- Wilsonova–Hilfertyové aproximace je v knize výslovně přibližná.
  Gamma momentový poměr pro mocniny1/3 a2/3 dává střed
  1−1/(9a)+O(a^−2) a rozptyl1/(9a)+O(a^−2). Nejde o tvrzení
  přesného generátoru ani o rovnost přesných momentů.

## Errata, prameny a otevřený rozsah

Všechny čtyři vrstvy all2-prepre/all2-pre/all2/err2 i aktuální TeX
byly prohledány podle stran132–136,140,586–587 a pojmů exponenciální,
gamma, Student,1.902 a koule. Čerstvé kopie z6. listopadu05:47UTC
jsou shodné se zachovanými soubory; další stahování nebylo potřeba.

X0120 je **známá oprava z23. března1999**, původní135:
`1−2ν` se mění na `1−2/ν`. Pro ν>2 je starý faktor záporný,
takže při přijetí není odmocnina reálná. Závažnost high odpovídá
rozbití alternativního generátoru, nikoli novosti nálezu.
Originál i oprava na all2-prepre8 byly přímo vizuálně porovnány.
Terminologii sphere/ball z29. dubna2014 potvrzuje all2-pre5;
nepřidáváme kvůli ní další matematickou chybu ani červenou stránku.

Z primárních zdrojů byly nyní znovu přímo přečteny Sibuya231–233
(minimum, Poissonova konstrukce a volba ln2) a Wilson–Hilferty686,688
(kubická transformace, momenty a výslovná omezení normality).
Starší vizuální přečtení celého Sibuya231–237 zachováváme jako
archivní doklad, nikoli jako sedm nově přečtených stran. Sibuya OCR
neobsahuje text; dokladem jsou původní obrázky. Staré zdrojové tabulky
jsme znovu nepočítali. Rok1962 podle původního obsahu vydavatele
se neopravuje na rok přijetí rukopisu1961.

Bibliografické výjimky: plné články Ahrens–Dieter1972/1982,
Jöhnk1964, Cheng1978, Marsaglia1980, Kinderman–Monahan–Ramage1977,
Brown1956 a Knop1970 nyní nebyly přečteny. Priority Brown/Ahrens
a osobní atribuce Brent nejsou nezávisle potvrzené. Přímý detail
znaménka v Marsagliově externím článku1977 byl již nedostupný403
a neopakujeme pokus; není to nepřečtený vzorec v naší knize.

Samostatná faktická mezera: tvrzení na134, že metoda Ahrens–Dieter1982
generuje gamma veličinu přibližně za dvojnásobek doby normálního
generátoru, není doložené původním měřením. Je to dobové srovnání,
ne univerzální složitostní věta; stránka134 proto zůstává partial.
Neověřenou rychlost neskrýváme mezi ověřenou matematikou.

Strana133 a odpověď586 jsou nyní celé pokryté v uvedeném rozsahu.
Na135 je matematika pokrytá a známá chyba; bibliografické výjimky
zůstávají viditelné. Strany132,136,140,587 zůstávají partial kvůli
dalším oddílům nebo dřívějším mezerám. Pokračuje §3.4.1 F od136,
úlohy17–19,22,25–30 a následně zbytek sekce. Žádný proces ani
korespondence nebyly spuštěny.
