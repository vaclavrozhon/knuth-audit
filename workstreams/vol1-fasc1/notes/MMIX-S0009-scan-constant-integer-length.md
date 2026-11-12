# MMIX-S0009 — scan_const ztrácí řád dlouhé celočíselné části

**Confirmed, medium, doprovodný program; nezávislá revize dokončena 12. 11. 2026.**
Původní scan_const v obou distribucích2013/2025 převádí platný floating
řetězec s přesnou hodnotou1 na zaokrouhlené0.1. Po naplnění769místného
bufferu zahazuje další číslice před desetinnou tečkou bez kompenzace
desetinného exponentu. Nález je pouze v software-ledger; správná knižní
definice binary64 ani její stránka nejsou novou knižní chybou.

## 1. Kontrakt a přípustný vstup

MMIX-ARITH §68, zdroj1309–1337, definuje floating magnitude mimo jiné
jako digit string následovaný exponentem. scan_const má vrátit
odpovídající hodnotu v val, typ1 a první nezkonzumovaný znak.
Počet číslic není omezen na velikost interního bufferu. §73 výslovně
motivuje správnost pro dlouhé desetinné řetězce. §77 připouští
nepřesnost při miliardě nebo více leading zeros; zde není žádná
leading zero a první svědek má jen775 ASCII znaků:

    "1" + "0"*769 + "e-769"

Jeho matematická hodnota je10^769·10^−769=1, tedy přesně
#3ff0000000000000. Nejde o decimal integer větev s návratem0
a redukcí modulo2^64, protože řetězec má platný exponent.
Žádná nejasnost režimu, subnormálu, tie nebo exception handleru zde
není. Dokumentovaný nedokonalý výpočet `exceptions` je jiná veličina;
nález nepoužívá jejich hodnotu jako kontrakt.

Přímé volání veřejného scan_const je deklarovaným rozhraním programu.
Není požadováno, aby všechny assemblerové nebo debuggerové vstupní
frontendy přijímaly libovolně dlouhé řádky. Host v reprodukci má
32bitové tetra a ASCII vstupy, takže nedochází k nepovolenému zápornému
argumentu isdigit. Vstup je platný, dostupný a ukončený NUL.

## 2. Přesný průchod a obecná rodina

`buf0=buf+8`, `buf_max=buf+777` dávají kapacitu769 číslic.
Po prvních769 významných celočíselných číslicích je q=buf_max.
Zbytek smyčky udržuje pouze sticky nenulovou poslední číslici;
q se již neposouvá. Po770 číslicích prvního svědka tedy buffer
obsahuje1 a768 nul, nikoli1 a769 nul. Scanned exponent je−769;
větev `if(!dec_pt)` nastaví dec_pt=q a zeros=0.

Při přesunu do bignum je

    x = 341 − (q−buf) − exp = 341 − 777 + 769 = 333.

Zde je důležité odlišit absolutní offset q−buf=777 od počtu číslic769.
Po rozdělení do radixu10^9 vznikne přesně0.1: počátek je ff.a=37,
první blok ff.dat[37]=100000000, všechny další jsou0 a ff.b se
vrátí na37. Původní kód žádný chybějící celočíselný řád nepřičte.

Binary konverzní smyčka tedy zpracuje1/10. Čtyři zdvojení dávají1.6
a exponent1018 v raw konvenci. Finální nearest-even significand je
round(2^55/5)=7205759403792794; celý bitový výsledek je
#3fb999999999999a, nikoli #3ff0000000000000. Funkce přesto vrací
typ1 a spotřebuje všech775 znaků. To přesně souhlasí s uloženým během.

Obecně vezměme `±1`, za ním768+k nul a exponent−(768+k), kde
1≤k≤231. Všechny mají přesnou hodnotu±1. Stejný buffer uchová
jen1 a768 nul a normalizuje±10^−k. Tyto hodnoty leží prokladné
znaménko v(0,0.1]; správné radixové zdvojování a finální pack nemohou
vytvořit1. Případné kolo rounding není zdrojem chybného řádu.
Varianta s explicitní tečkou před exponentem vede na tentýž dec_pt;
znaménko pouze změní sign bit. Nejdelší uvedená varianta se znaménkem
i tečkou má1007 znaků a |exponent|≤999.

## 3. Přesný rozsah opravy a invariant

Auditní `sources/audit-scan-constant-integer-length.ch` přidává čítač
discarded_integer_digits. Každá významná celočíselná číslice, kterou
již buffer nepojme, tento čítač zvýší. Před vstupem do existující
floating normalizace se přičte k exponentu. Původní zdroje se nemění.

Invariant po zpracování D číslic celočíselné části od prvního nenulového
znaku je

    q−buf0 = min(D,769),
    discarded_integer_digits = max(D−769,0),
    (q−buf0)+discarded_integer_digits = D.

Při D<769 další číslice posune q a čítač zůstane0. Při D≥769 se q
nemění a čítač roste o1. Sticky pravidlo se zachovává; před prvním
nenulovým znakem zůstává q=buf0 a leading integer zeros nepřidávají
žádnou pozici do obou členů. Tím jsou všechny větve celočíselné
smyčky pokryté. Fractional část čítač nemění, protože její zahozené
číslice nemění polohu tečky.

Je-li K=(dec_pt−buf0) a δ počet vynechaných integer pozic, logická
poloha tečky je K+δ. Normalizace po opravě používá E+δ, což je
algebraicky totéž jako nahradit K skutečnou polohou K+δ. Pro první
svědek je δ=1, E+δ=−768, x=332 a ff.dat[36]=1: jádro nyní
obdrží přesně1. Pro celou rodinu je δ=k a E+δ=−768, tedy také1.

Obor důkazu **nové integer aritmetiky** je vstup kratší než10^9 bytů
a literal exponent s absolutní hodnotou nejvýše999999999. Pak
0≤δ<10^9 a −999999999≤E≤999999999, takže součet je v rozsahu
signed32. Jestliže δ>0, je zeros=0; dlouhé leading fractional zeros
mohou nastat pouze při δ=0. Tím se nespojí dva současně obrovské
pozitivní posuny. Žádné nové paměťové pole ani pointer neposouváme.
Širší zacházení s exponenciální saturací a původními C pointerovými
výrazy tím není prohlášeno za plně ověřené.

Větve bez ztracené integer číslice mají δ=0 a floating normalizaci
beze změny. Pure decimal integer návrat0 proběhne před novým přičtením;
jeho celý modulo akumulátor zůstává stejný. Inf, běžné NaN a neplatný
prefix nevstupují do upravené floating normalizace. U NaN s fraction
je celočíselná smyčka prázdná a δ=0. Syntax a next_char se nemění.

Přidává se jeden int, jedno počáteční nulování, jedno přičtení na
floating cestě a přesněδ inkrementů při již existující O(n) vstupní
smyčce. Počet přečtených znaků a bufferová kapacita se nemění. Nová smyčka
v multiprecizní konverzi nevzniká; její počet zdvojení samozřejmě
odpovídá opravenému exponentu.
Celý decoder ani jeho globální IEEE rozhraní zde nedostává nový
univerzální důkaz. Dokázaná oprava obnovuje ztracenou **polohu tečky**
v uvedeném oboru; ostatní konverzní povinnosti zůstávají samostatné.

## 4. Originál, errata a jediná malá reprodukce

Celý input-conversion oddíl2013/2025 je byteově stejný. Přímé zdroje,
archivní hashe a původní [sazba MMIX-ARITH §68–78](https://mmix.cs.hm.edu/doc/mmix-arith.pdf#page=30)
jsou v evidenci. Strany30/31/32 byly zobrazeny, včetně příslušné
smyčky, bufferu a výslovné leading-zeros výjimky. Veřejná sazba
přidává závorky a inicializaci zeros=0; obojí ponechává stejnou chybu
ztraceného celočíselného řádu. Fyzický výtisk nebyl kontrolován.

`results/errata-S0009.json` obsahuje13 vrstev, jejich hashe a kontexty.
Známé opravy input části:1999 inicializace standardního NaN;
2002 disclaimer pro exceptions;2009 inicializace exp/NaN guard
a zvýšení exponentového limitu. Všechny jsou už zohledněny a žádná
nepočítá zahozené integer pozice. Warning change přidává pouze
závorky. Veřejný rounding report2015 je fplus alignment; debugger
buffer overrun2025 je parser příkazu b. Nejde o tento kontrakt.
Aktuální primární stránky errat i seznamu bugů byly znovu otevřeny;
žádná odpovídající oprava nebyla nalezena. Netvrdí se světové prvenství.

Jediné první spuštění `verify_scan_constant_integer_length.py` s nice15
trvalo **1.335681968s**, šest build kroků a36 přímých volání scan_const.
Dvanáct vstupů proběhlo na2013,2025 a auditní opravě. Každý originál
má sedm přesných hodnotových rozporů; opravená varianta souhlasí ve
všech12. Všech36 spotřebuje celý řetězec a vrátí správný druh.
Kontroly zahrnují poslední naplněnou pozici, obě znaménka, explicitní
tečku, dvě a231 vynechaných pozic, vícemístný prefix, fractional
sticky po plném integer bufferu, pure integer modulo, leading zero,
fraction-only a běžné0.1. Oracle používá jen celá čísla a Fraction
s vlastním nearest-even packingem; nepoužívá hostitelský float parser.

Uložené výsledky a build logy jsou přímou evidencí. Verifikátor odmítne
znovu přepsat úspěšný výsledek; žádný starý test ani úspěšný nový test
se neopakuje. Reprodukce podporuje přesný obecný invariant výše,
nenahrazuje jej ani nepokrývá zbytek decimal konverzního programu.
