# Souvislý průchod MIXALu: úlohy 10–23

5. listopadu 2026 přímo přečteny původní strany 159–163 a 513–522
(soubory 174–178 a 528–537). Spodní část 522 již patří §1.3.3 a její
pokrytí se tímto neuzavírá. Přečteny všechny níže jmenované důkazové
poznámky a porovnány uložené výsledky. Úspěšné výpočty se neopakovaly.
X0952 dokumentuje tento průchod, X0953 doplňuje dříve neevidované známé
erratum. Nová dosud neopravená chyba v tomto bloku nepřibyla.

## Sedlové body, 10–12

Přijaty `mixal-saddle.md` a `mixal-saddle-sources.md` včetně důkazů
všech případů shod. Maximum řádkových minim nepřekračuje minimum
sloupcových maxim; rovnost je právě případ sedlového bodu. Uchovávání
celé množiny kandidátů nevynechává shodná minima. Druhý původní program
vynechává první řádek: jde o opravu ENT3/ENT2 z roku 2013. Protipříklad
má první řádek samé dvojky, každý další jednu nulu a ostatní jedničky.
Přesun ENT1 z roku 1999 pouze šetří čas. Chybějící předpoklad m≥n
u původního odhadu je již opraven; obecný horní odhad porovnání O(m+n)
a pomocné práce O(m log n) je doložen přijatou recenzí Dallant 2024.

Pro náhodné různé prvky je P=(m+n)/binom(m+n,m), pro 9×8 tedy 1/1430.
Pro nezávislé binární prvky je pravděpodobnost sedla
2−(1−2^(−m))^n−(1−2^(−n))^m: nulový sloupec a jedničkový řádek se
navzájem vylučují. Pro 9×8 vychází
924744796234036231/18446744073709551616. Dvoučlenná Bonferroniho mez
opravňuje uvedené přiblížení.

C0023 zůstává potvrzené drobné počítání času na 514: první program
má 1+87+3+45+1=137u před HLT, druhý 432+3+88=523u. Konzistentní pár
je 137/523, případně 138/524 včetně 1u HLT. Vytištěné 137/524 směšuje
konvence. Rozdíl je 386u při obou společných konvencích, takže závěr
nezávisí na otevřeném C0020. UI závažnost snížena na low: výsledek
algoritmu je správný, nesoulad je jedna časová jednotka.

C0024 je **pouze v doplněné odpovědi z 24. dubna 1997**, nikoli
v původním textu 515. Záznam minima stojí 13u proti 6u, proto
E(row)=6n+7H_n−3. Pro B=binom(m+n,m), P=(m+n)/B a n>1 je přesný
očekávaný celkový čas bez HLT

    6mn+7mH_n+6m+6+5(m+1)/(n−1)
    −5(m+n)^2/((n−1)B)−Delta,

kde

    (6n+13)(m−1)P/2 ≤ Delta ≤ (13n+5m+1)(m−1)P/2.

Publikované 5mH_n+8m je tedy chybně, a ani oprava tohoto členu
nepostačuje: při m=n=k má úspora z předčasného zastavení řád k³/B,
nikoli O(k²/B). Druhý vzorec je správný při log(n)/m→0; důkaz používá
momenty maxima exponenciálních veličin. Nejde o vadu hledání sedla.
Závažnost high zachována pro dvě chybné matematické části odhadu.

Staré konečné kontroly (9381, 3118 a 6126 kontrol) a přesné profily
přijaty bez opakování. Vlastní třetí algoritmus ani přibližné historické
náhodné časy nejsou důkazem globální optimality. Původní Bienstock 1991
není dostupný; Hofri–Jacquet preprint není zaměněn s ověřením každého
řádku časopisecké verze. To jsou výslovné bibliografické výjimky.

## Šifrovaný text, 13

`mixal-crypt.md`: kód správně odlišuje konec −1, mezeru 0 a hvězdičku
46. První LDX následuje až po 4H. Dva buffery po 14 slovech, vzdálené
16 slov, se nepřepisují během čtení; jedno přednačtení navíc odpovídá
zadání. CHAR vytváří deset číslic, tisk používá posledních sedm,
a JBUS před zápisy chrání výstupní buffer. Kapacita sedmi číslic
je výslovná podmínka. Na originálu je úspora 7u, nikoli OCR 1u.
1992 uložených kontrol, 498 běhů a 2742 řádků nebylo opakováno.
U Bourne–Ford byla přijata bibliografická metadata; úplný článek
se zde neověřoval, nepřebírá se z něj nový číselný závěr.

## Velikonoce, 14–15

`mixal-easter.md`, `mixal-easter-sources.md` a
`calendar-primary-root-review.md`: matematika i MIX platí v uvedeném
rozsahu 1583≤Y<100000. Násobení floor(aB/d)+1 dává správný podíl za
zdejší meze dV<B. Přičtení 720 odstraňuje záporné epakty ve všech
povolených radixech. Driver tiskne 51 roků 1950–2000. Nedělní posun
odpovídá Y+floor(Y/4)−floor(Y/100)+floor(Y/400)+2; jde o první neděli
striktně po tabulkovém úplňku, nikoli o přesný astronomický model.

První selhání varianty se záporným zbytkem je rok 10317: správně
25. března, vadně 22. dubna. Perioda matematického algoritmu 5700000
má ΔX=42750, ΔZ=18240, Δepact=−24510 a Δweekday=7082250. Minimalitu
vylučují podíly periody prvočísly 2,3,5,19 již s Y=1583. Četnosti
března22, dubna19 a dubna25 jsou 27550, 220400 a 42000; násobnost25
plyne z rozkladu století a CRT. Dva dříve provedené úplné periodické
výpočty (11405398 kontrol) se neopakovaly.

C0025/26 zůstávají drobné historické vady na 518, nikoli chyby programu.
Přímo znovu zobrazen Siglerův překlad Liber abaci, strany438–439:
kapitola12 počítá složené úročení 100(5/4)^18 opakovaným čtvercováním.
Protipříklad vyvrací širokou výlučnost netriviální středověké aritmetiky.
Přímo zobrazeny MGH678–679, kde Victorius sám popisuje dřívější cykly,
a PG10 sloupce879–880 s tabulkou 7×16 let. Tím se dokládá starší
systematický tabulkový postup; nové absolutní prvenství ani nový
filologický přepis všech znaků nápisu se netvrdí. Ostatní primární
strany jsou přijaty z výslovné dřívější kořenové recenze.

Úloha14 se uzavírá s bibliografickými výjimkami: úplné programy
Knuth–Williams1962 a případné proleptické chování před1583, O'Beirne1965
kapitola10, osobní připsání Petolinovi/Wermuthovi/O'Beirnovi/Hillovi,
a Wermuthovy úspory9/10/12 instrukcí bez dostupného programu. Žádná
z těchto položek se neoznačuje za přímo ověřenou ani za důkaz
optimálnosti. Úloha15 již byla uzavřená.

## Zaokrouhlené harmonické součty, 16–17

`mixal-rounded-harmonic.md`: pro M=10^n je R(j)=floor(M/j+1/2), nenulové
právě pro 1≤j≤2M. Skupina r>0 odpovídá
2M/(2r+1)<j≤2M/(2r−1). Poslední skupina pro n=5 má 133334 členů.
Výsledky 6.16, 8.449, 10.7509 a 13.05363 jsou správné. Kód má zastavení
JAP a meze 20M<64^5; vytištěné sumy a všechny radixy byly dříve testovány.
Asymptotika je n ln10+2γ−1+2 ln2+O(10^(−n/2)); opravy H_N a 2H_(2m)
z roku1999 patří do X0176.

**X0953, známé erratum 22. března 2018:** v algoritmu B na161 chybí
zastavení pro r=0. Pak by následující krok požadoval největší index
z nekonečné nulové skupiny, který neexistuje. Oprava je přímo v
all1-pre, strana11; není to nový nález a vytištěný MIX již podmínku má.

C0027 na519 zůstává potvrzené: čas před OUT je
3+4·26+907·43+911·29+4·26=65631u, ne65595u. Včetně OUT/HLT je65633u
bez fyzického čekání tiskárny. Rozdíl36u by vysvětlilo započtení čtyř
CHAR jako1u místo10u, ale to je pouze hypotéza o vzniku chyby.
Numerické součty jsou správné. Dřívější43994+9 kontrol se neopakovalo.

## Fareyovy zlomky, 18–19

`mixal-farey.md`, `mixal-farey-sources.md` a relevantní část
`tree-farey-source-continuation.md`: je-li bc−ad=1 a a/b<p/q<c/d,
pak p=ua+vc, q=ub+vd s kladnými celými u=cq−dp, v=bp−aq; tedy q≥b+d.
Pro h=floor((b+n)/d), X=hc−a, Y=hd−b platí n−d<Y≤n, Xd−cY=1
a d+Y>n. Tyto nerovnosti dokazují, že X/Y je skutečný další člen.
Počet členů je1+sum(phi), s asymptotikou3n²/π²+O(n log n).
Kód výslovně předpokládá n>1 a dvě dostatečně velká disjunktní pole;
na zvoleném rozložení se vejde n=76, nikoli77. Není to obecný slib
neomezené kapacity. Dřívější uložené kontroly přijaty.

Úloha19 uzavřena s výjimkami: původní Haros1802, strany364–368,
zůstává nedostupný (starší pokusy403/429), stejně jako úplná historie
prvenství a Cauchyho připsání. Obsah přijatých přetisků a důkaz
Hardy–Wright není zaměněn s přímým čtením původního Harose.
Pravopisné opravy X0179 patří přímo na520.

## Semafory, 20 — dosud částečné

`mixal-traffic.md`: DELAY dává přesně max(n,7)u a FLASH16 přechodů
po půlsekundě s dalšími4s dává12s. Celý cyklus má přechody0,18,30,38,
46,58,63 sekund. Známé LDA *= na521 je opraveno na LDA * (2008).
Časování a všechny radixy pokrývá15125 dřívějších kontrol.

Otevřené je pořadí shodného hardwarového okamžiku: požadavek přesně
na přechodu Berkeley zelená→oranžová může být při jedné interpretaci
smazán následujícím JOV. Specifikace říká, kdy se mění X při LDA/INCX,
nikoli přesný okamžik vzorkování JOV. Nelze zvolit chybovou interpretaci
bez dalšího předpokladu. Úloha zůstává partial, nikoli confirmed.
Částečné jsou strany161–162 a521; samotný DELAY na520 je prokázán.

## Magické čtverce, Josephus a křížovka, 21–23

`mixal-magic-square.md`, `mixal-magic-sources.md`: pro n=2h+1 a
k=nq+s+1 má pole souřadnice r=h+1+q+s, c=h−q+s modulo n.
Invertibilita2 dokazuje bijekci; řádky, sloupce a obě diagonály mají
součet n(n²+1)/2. Fig16 má součet175, n=23 součet6095. Kolize nastává
po každých n krocích a opravuje se posunem o2 dolů. Vlastní MIX
splňuje kapacity1≤n≤23; 5595 starých kontrol/47 běhů se neopakovalo.
Oprava Moschopoulos→Ibn al-Haytham X0183 je doložena konstrukcí
otočenou o90°. Přijaty dřívější recenze Berggren/Sabra/Tannery; původní
arabské a řecké rukopisy ani celý Ball1939 se znovu nekontrolovaly.

`mixal-josephus.md`: fig17 vypisuje pořadí odstranění po pozicích,
pro8,4 tedy54613872, nikoli posloupnost odstraňovaných pozic.
Pro24,11 zůstává původní pozice15. Kruhové ukazatele, CHAR/NUM,
výslovné m>2 a dvouciferný rozsah splňují kód. Čas před OUT je
16+(n−1)(4m+30)=1718u. Vlastní Ingallsova varianta není slib globální
optimality. Vyvážené skládání map vynechaných pozic dává O(n log n)
slovních operací; ne stejný počet bitových operací s neomezenými čísly.
153742 starých kontrol/598 běhů přijato; Ahrensovy relevantní stránky
a odkaz§5.1.1–5 jsou přijaty z předchozího přímého ověření, nikoli
z nového čtení celého třetího svazku či celé Ahrensovy kapitoly.

`mixal-crossword.md`: flood fill mění1→−1 a používá pouze stranovou
sousednost. Začátek slova vyžaduje bílé následující a nebílé předchozí
pole; sjednocení obou směrů čísluje křížení jen jednou. Fig18 má14
čísel. Zápis nn není výslovným omezením na99: pro23×23 může být192
začátků a tři číslice se vejdou do čtyř sloupců dlaždice. Všechny
vzory hran5×3, pravý/dolní/diagonální soused i120 sloupců výstupu
souhlasí. Opravy what→white a popisu horní vstupní karty jsou X0187.
4212 kontrol/601 běhů nepřepočítáváno. Úlohy21/23 nemají v knize
vzorový kód: vlastní programy jsou pouze důkazové konstrukce.

## Errata a mapa

Čtyři erratové vrstvy jsou totožné s listopadovým obnovením podle
`sources/sequential-2026-11-05/errata-refresh.json`. Přečten celý
MIXAL výtah a přímo zobrazeny relevantní all1-prepre13,14,37,38
a all1-pre11,16. Dříve přímo ověřené aktuální dodatky jsou rozlišeny
od prvního dotisku. C0024 je pouze související místo515; červeně je
nebarví samo erratum. Červené původní vady C0023/25/26/27 a známé
opravy mají konkrétní stránky, ne všechny stránky příslušné úlohy.

Výsledný stav: úlohy14/19 nově checked s výše uvedenými výjimkami;
úloha20 stále partial. Staré částečné pramenné záznamy zůstávají
archivem se svým přesným rozsahem. Další kurzor je§1.3.3, strana164
(soubor179), odpovědi od522.
