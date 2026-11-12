# Úlohy1.3.2′–9 až14: úplné číselné a programové doplnění

Zadání file52/p44, odpovědi file107–109/p99–101. Tento blok doplňuje
přesná vedlejší tvrzení, která starý zápis ponechal bez důkazu.
Původní sazby52,108,109 byly zobrazeny. Nikde se z příkladu nebo
správného benchmarkového součtu nevyvozuje obecná korektnost kódu.

## 9. Šest set prvočísel a obě odpovědní číselné meze

Pro L=600 zůstávají všechny výrazy původního programu parametrické:
ptop=D+1200, j0=2−1200=−1198, jj=2(j−600). Výstup má deset
sloupců a60 řádků; inkrement sloupce2L/10=120 i závěrečné srovnání
2(L/10−1)=118 se vejdou do immediate byte. Bázové offsety BUF,Title,
NewLn,Blanks zůstávají malé; početGREG i instrukční tvar se nemění.
Změna title Five→Six má jen délkový důsledek v assemblerových
adresách; symbolické LDA/NewLn/Blanks je přepočítají automaticky.

Uzavřený binomický argument V0086 dává13π(8192)>8178, tedy
π(8192)≥630>600; tytéž čtyři explicitní rozsahy dostupných dělitelů
platí pro všechna n<8192. Generátor tedy dokončí600 prvků, každý
má nejvýše čtyři decimal digits a vejde se do unsigned wyde. Oba
indexové invarianty P1–P8/P9–P11 se přebírají se změněným L; žádný
nový empirický běh Programu P není nutný.

Odpověď navíc tvrdí první potřebu pěti cifer u1230 prvočísel a
6542 prvočísel v jednom wyde. `results/exercise-0132-prime-bounds.json`
uzavírá oba přesné údaje: p1229=9973, p1230=10007,
p6542=65521, p6543=65537. Tedy π(9999)=1229 a π(65535)=6542.
Pouhé ověření prvočíselnosti těchto čtyř čísel by pořadí nedokázalo;
následující certifikát pokrývá i všechna čísla mezi nimi.

**Úplný argument nového malého síta.** Dříve přijatý certifikát
obsahuje všech500 prvočísel do3571 a každý složený vstup v tomto
rozsahu má doložený nejmenší dělitel. Jeho SHA je v novém výsledku.
Nově se zpracuje pouze interval3572..65537. Je-li n z něj složené,
má prvočíselný dělitel≤sqrt(65537)<257; všechna taková prvočísla
jsou již v převzatém seznamu. Pro každé p s p²≤65537 se označí
přesně násobky od max(p²,ceil(3572/p)p) do největšího≤65537.
Každý označený n má2≤p<n a p|n; žádné prvočíslo označeno není.
Naopak nejmenší dělitel libovolného složeného n splňuje n≥p²,
takže je n v jeho aritmetické posloupnosti a označeno bude.

Invariant po i průchodech: označena jsou právě čísla zachycená
prvními i doloženými posloupnostmi; uložený nenulový dělitel je
nejmenší již zpracovaný p. Po posledním průchodu zbydou právě
prvočísla. Připojení k původním500 je disjunktní, zachovává pořadí
a dává kompletní seznam do65537. Výsledek ukládá všechny nové
primes, každou marking progression a hash celého vektoru dělitelů.
Rovnosti výše jsou indexy v tomto úplném seznamu, nikoli odhad.
Práce je O(N Σ1/p) a paměť O(N) pro N=61966 nových celých čísel;
zde trvala celá společná nová kontrola asi0,02s. Staré síto2..3571
se nespouštělo znovu.

## 11. Obě části a skutečně uzavřený Bertrandův předpoklad

Pro složené celé n>1 vyberme faktorizaci n=ab s1<a,b<n. Nemohou
být oba faktory>sqrt(n), jinak ab>n. Menší má prvočíselný dělitel
d ve stejném intervalu1<d≤sqrt(n). Tím je(a) včetně existence
prvočíselného dělitele doloženo bez circularity.

V P7 už byly zamítnuty všechny prvočíselné dělitele≤p a zbytek
je nenulový. q≤p dává n=pq+r<p²+p<(p+1)². Každý další
prvočíselný dělitel je>p+1: p je liché≥3 a p+1 je sudé>2,
tedy není prime. Takový dělitel nemůže být≤sqrt(n), spor s(a).
Odpovědní ostré „greater than p+1“ je tedy správné; stačila by
i slabší celočíselná mez≥p+1, protože sqrt(n)<p+1.

Úplný nový Bertrandův důkaz je přesně převzat z
`../../vol1/notes/quality-recovery-bertrand-2026-11-06.md`
(cesta vůči této notes složce) a jeho certifikátu
`../../vol1/results/quality-recovery-bertrand-chain-2026-11-06.json`.
Oba byly celé přečteny. Silná indukce dává P(m)≤4^(m−1);
centrální binomický koeficient a vyloučení p∈(2n/3,n] vedou
při chybění prime v(n,2n) na4^(n/3)≤(2n)^(sqrt(2n)+1).
Od n=512 je to nemožné, protože obě logaritmické funkce klesají
a přesná počáteční mez je(165/256)ln2<(2/3)ln2. Všechny menší
n pokrývá prokázaný řetězec2,3,5,7,13,23,43,83,163,317,631,
každý následující člen<2 předchozího. Nejde o pouhé pojmenování
klasické věty ani nový běh jejího certifikátu.

Před novým prime n tabulka obsahuje předchozí prime p≥3 a věta
se stejnou premisou celé p≥2 dává n<2p<p²+p. Nejpozději u p
proto nastane P7, dříve než by se četlo nevyplněné místo. U
složeného n je jeho nejmenší dělitel<n již v tabulce a nenastane
nesprávné předčasné přijetí podle právě dokázané části(b).
Tím je zobecněné odpovědní tvrzení pokryté; konkrétní MMIX
kapacity do500/600 jsou navíc odůvodněny konečným oborem výše.

## 14. První varianta: funkce, stavy a celý profil

Přípustný stav je původní Program P, L=500, platná paměť a
disjunktní konstantní báze, běžné inicializované NNIX prostředí
s vypnutými floating tripy. Každý kandidát5≤n≤3571 a každý
divisor p je kladné malé celé. FLOT proto dává přesné binary64;
žádný operand není NaN, infinity, subnormal ani záporná nula.
Výsledné FP event bity nejsou kontrolovány programem a nevstupují
do žádné celočíselné větve; enabled trap handlery jsou mimo obor.

Vytištěné dva novéGREG jsou před prvními FLOT/FSQRT; kód FLOT fn,n
a FSQRT sqrtn,fn leží **před6H**. Pro nový kandidát se tedy vykoná
jednou, při návratu33→6B se neopakuje. 6H načtep, převede jej
do t a FREM(r,fn,t) vypočte přesný IEEE remainder. Pro tato
kladná celá čísla je remainder0 právě kdyžp|n. V takovém případě
je n pozitivní, a správné znaménko remainder je+0, takže bitové
BZ opravdu rozpozná nulu. Nenulový remainder smí být záporný,
ale BZ jej pak nepovažuje za nulu.

FCMP porovnává sqrtn s floatingp a původní BNP přijme, jestliže
sqrtn≤p. Pro nesquare n je vzdálenost sqrt(n) od libovolného
celého p alespoň1/(sqrt(n)+p), neboť|n−p²|≥1. V rozhodovacím
rozsahu p,sqrt(n)<64 je tato vzdálenost>1/128, zatímco i directed
binary64 rounding má chybu<2^-46. Znaménko porovnání se nezmění.
Je-li n square, přesný dělitel byl zachycen FREM před FCMP. Tím
má program ve všech čtyřech rounding režimech tytéž větve jako
matematický test p²≥n, s vypnutými tripy.

Pokud jsou dosavadní remainder nenulové a p≥sqrt(n), n nemá
žádný prvočíselný dělitel≤sqrt(n), takže je prime. Dostupnost
takového známého p je dána konečným původním důkazem (nebo
Bertrandem); počty a tabulkový invariant zůstávají stejné.

**Úplné testové počty.** Z původního certifikátu jsou převzaty
C=1784 lichých kandidátů, K=1286 kompozitů, A=498 nových primes
(2 a3 se nevykonávají jako testovaní kandidáti). U složeného n
se zastaví vždy na jeho nejmenším prime d; dřívější p<d nemůže
splnit p≥sqrt(n), neboť n≥d². U prime n se zastaví na prvním
lichém prime p s p²≥n. V obou případech je přesný počet testů
π(p)−1, protože2 se nezkouší. Suma těchto uzavřených počtů je
T1=9597, zatímco už doložené T0=9538. Pro každý kandidát je
uložen jeho stop a počet; neproběhla simulace programu.

**Všechny ceny ve smyčce.** Při obecném T má LDWU T mems aTυ;
FLOT/FREM každý4Tυ; BZ stojí T+2K; FCMP T−K;
BNP T−K+2A; INCLkk a JMP každý T−K−A. Součet je
Tμ+(14T−2K)υ. Původní DIV/GET varianta měla
T0μ+(67T0−2K)υ. Přidaná příprava stojí(4+40)Cυ,
ostatní řádky obou programů jsou totožné. Úspora celé změny je

    (T0−T1)μ + (67T0−14T1−44C)υ
    = −59μ + (53·9538−14·59−44·1784)υ
    = 426192υ−59μ.

Zahrnuty jsou všechny taken/not-taken předpovědi, poslední test
každého kandidáta i oba přechody ven. Nejde o empirickou pipeline
rychlost; jde přesně o deklarovaný μ/υ model, bez TRAP handlerů.
Změna je rychlejší právě při μ/υ<426192/59≈7223,59, stejná
na rovnosti a pomalejší nad ní. Vytištěné „unless μ/υ>7000“ je
platná slabší nutná podmínka výjimky, nikoli tvrzení, že už každé
μ/υ>7000 obrátí výhodu; implikace se nesmí otočit.

## 14. Short-float tabulka: konkrétní změny a38169υ

Pouhé nahrazení load/store typů by38169 nedokázalo. Následující
úplný seznam změn první FP varianty dává přesně tvrzenou úsporu:

* Uchovávej i kandidát n jako floating. Main používá `FLOT n,3`
  místo `SET n,3`; přidej konstantní `two GREG #4000000000000000`
  a nahraď P4 `INCL n,2` instrukcí `FADD n,n,two`. fn se stane
  aliasem n a původní FLOT fn,n úplně odpadne. FSQRT zůstává.
* PRIME1 je `TETRA #40000000`, tedy short2.0. Všechny prime
  položky mají4 byty: LOC PRIME1+4*L, j0=PRIME1+4−@,
  INCLjj/INCLkk po4 a `STSF n,ptop,jj`. P6 načte
  `LDSF pk,ptop,kk`, vynechá FLOTt a provede
  `FREM r,n,pk; BZ r,4B; FCMP t,sqrtn,pk`.
* Při tisku načti `LDSF pk,ptop,mm; FIXU pk,pk`. Zbytek
  decimal conversion zůstane celočíselný. Počáteční mm je−4,
  sloupcový krok4L/10=200 a závěrečná mez4(L/10−1)=196.
  Všechny ostatní tiskové instrukce a řetězce jsou beze změny.

Poslední mez je **196**, protože L/10−1=49; sloupcová báze po
prvním řádku je0, po posledním196. Všechny nové immediate hodnoty
3,4,200,196 jsou≤255. Ptop=D+2000, j0=−1996; původní důkaz
indexace se přebírá s měřítkem4. Short2.0 je na4 zarovnáno a
každé nové STSF/LDSF má stejně zarovnaný index. ConstantGREG pro
two ani alias fn nemají runtime náklad; lze ponechat nepoužitý q.
Počet globálních registrů zůstává daleko od hranice rG=32.

Všechna celá čísla≤3571 jsou přesná i v binary32. Inicializace3.0,
přičítání2.0, STSF a rozšíření LDSF jsou proto přesné; n má při
každém kandidátu tutéž matematickou hodnotu a všechny testové
větve jsou stejné. FIXU každého tiskového p je přesný a jeho
výsledek se vejde do unsigned i signed64. Není třeba spoléhat na
obecně neplatnou ekvivalenci úzké/široké FP aritmetiky.

Odstraněný FLOT v P6 ušetří4T1=38388υ. U každého kandidáta se
ušetří4υ za FLOTfn, ale FADD místo INCL stojí o3υ více, čistá
úspora+C=1784υ. Tiskový FIXU stojí navíc4·500=2000υ a úvodní
FLOT místo SET navíc3υ. Load/store mají stejné μ+υ ceny a
žádná další instrukce se nevykonává navíc. Proto dodatečná úspora je

    4·9597 +1784 −4·500 −3 = 38169υ.

Počet mems se nezmění, jen paměť tabulky vzroste z1000 na2000
bytů. Kompletní explicitní variantu lze z tohoto seznamu získat
beze skrytého výběru; žádné tvrzení o optimálnosti se nepřidává.

## 14. Posunutá odmocnina: korektnost,9357 a podmínka ceny

Pro přesný matematický bias b=19999/10000=1.9999 použijeme
threshold sqrt(n)−b. Pokud po nenulových remainder přijmeme u
lichého prime p, pak p≥sqrt(n)−b, takže p+2>sqrt(n).
Jakýkoli zbývající prime divisor by byl≥p+2 (p+1 je sudé>2),
což podle části11(a) u kompozita není možné. Test tedy může
přijmout dříve, ale nikdy nesprávný prime. Před prvním divisor d
složeného n nemůže nastat p≥sqrt(n)−b, protože p≤d−2 a
sqrt(n)≥d; rozdíl je nejméně2>b. Dostupnost testového p je
slabší než u původní sqrt varianty, proto rovněž zajištěna.

Pro MMIX přidej `bias GREG #3fffff972474538f` a za FSQRT jedinou
`FSUB sqrtn,sqrtn,bias`. Uvedené bity jsou nearest binary64 pro
19999/10000. Jejich výpočet je samostatné integer zaokrouhlení
(19999·2^52)/10000: zbytek9504 vyvolá zaokrouhlení nahoru.
Chyba konstanty je<2^-53. Při libovolném ze čtyř režimů má FSQRT
i FSUB v našem rozsahu chybu<2^-46, takže celková chyba threshold
je<2^-44.

Pro každé relevantní celé n,p má přesný rozdíl

    n−(p+b)² = [10^8 n−(10000p+19999)²]/10^8.

Čitatel nemůže být0, neboť druhý člen je1 modulo10000 a první0.
Jeho absolutní hodnota je≥1. Proto
|sqrt(n)−(p+b)|≥1/[10^8(sqrt(n)+p+b)]>1/(128·10^8),
jelikož n≤3571 a rozhodovací p≤61. Tato mez je>2^-44.
Floating chyba tudíž nikdy nezmění stranu porovnání. Žádná
neověřená desetinná aproximace se zde nepoužila jako oracle.

Nový stop pro prime je proto přesně první p splňující
10^8n≤(10000p+19999)². Pro composite zůstane nejmenší dělitel.
Úplný součet π(p)−1 ve stejném uloženém seznamu kandidátů je
T2=9357. Proti první FP variantě odpadne240 testů, každý v
celkovém profilu zaμ+14υ, ale přibude4Cυ za FSUB. Rozdíl ceny je

    4·1784υ−240(14υ+μ) = 3776υ−240μ.

Posunutá varianta je rychlejší právě při μ/υ>3776/240=236/15,
na rovnosti stejně rychlá a pod ní pomalejší. Vytištěné „unless
μ/υ>15“ je opět platná slabší nutná podmínka, ne přesná prahová
ekvivalence. Srovnání se týká první FP varianty; při současném
použití short tabulky mají odstraněné testy jinou υ cenu a nelze
tento práh bez přepočtu přenášet.

## Evidence a stav

Jeden nový `nice -n 15` běh `verify_exercise_0132_counts.py` vytvořil
oba výsledky. Pro nové FP varianty použil již uložené prime/composite
certifikáty a uzavřené stopping vzorce; nespustil MMIX, assembler,
starý profiler ani staré síto. Uloženo všech1784 rozhodovacích řádků,
jejich zdrojové hashe, všechny count součty i integer původ biasu.
Případně drahé souborové či pipeline experimenty nebyly potřeba.

Tím jsou všechny numerické a implementační části úlohy14 a všechny
její vytištěné časové věty uzavřeny v deklarovaném μ/υ modelu.
Úloha14 se může změnit zpartial naargument_recorded. U úlohy13
zůstává samostatná jazyková/bibliografická výhrada, kterou tento
výpočet nijak neřeší; úplná mapa strany52 bude uvedena zvlášť.
