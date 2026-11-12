# §1.3.2-21: liché magické čtverce

Originál s.162 a obrázek16 zobrazeny1.listopadu2026. Magický čtverec
řádu n používá každé celé číslo1..n² právě jednou a má stejný součet
v každém řádku, sloupci a obou hlavních diagonálách. Tento součet
musí být n(n²+1)/2: součet všech čísel n²(n²+1)/2 se rozdělí mezi n řádků.

## Obecný důkaz konstrukce

Nechť n=2h+1 je liché kladné číslo. Řádky a sloupce číslujeme od0
shora, respektive zleva. Souřadnice bereme modulo n, což znamená
přechod z posledního řádku/sloupce na první. Počáteční1 leží v
(r,c)=(h+1,h); pro n=1 interpretujeme i tento krok modulo1.

Rozdělme čísla do n bloků po n. Číslo k=nq+s+1, kde0<=q,s<n,
má souřadnice

```
r = h+1+q+s (mod n),     c = h−q+s (mod n).
```

Je-li dvojice souřadnic stejná pro (q,s) a (q',s'), odečtení rovnic
dává2(q−q')=0 modulo n. Protože n je liché, má2 inverzi modulo n;
tedy q=q' a následně s=s'. Všechny n² pozice jsou různé.

Uvnitř bloku odpovídá s→s+1 posunu o jeden řádek dolů a jeden
sloupec vpravo. Na konci bloku by další takový krok vrátil pozici
jeho prvního člena, která už je plná. Posun o dva řádky dolů při
stejném sloupci místo toho přejde z poslední pozice bloku q na první
pozici bloku q+1: řádek začátku se zvýší o1 a sloupec sníží o1.
Bijektivita právě dokázaná zajišťuje, že žádná jiná srážka nenastane.
Vzorec tedy přesně popisuje zadání včetně pravidla pro plné pole.

Pro pevný řádek r je q+s pevné modulo n. Jak s probíhá0..n−1,
probíhá q všechna tato čísla také, takže součet je
n·n(n−1)/2+n(n−1)/2+n=n(n²+1)/2. Pro pevný sloupec c je s−q
pevné modulo n a stejný výpočet platí znovu.

Na hlavní diagonále r=c je2q+1=0 modulo n, tedy q=h; s probíhá
všechna čísla0..n−1. Součet n²h+n(n−1)/2+n je požadovaná konstanta.
Na vedlejší diagonále r+c=n−1 je2s=−1 modulo n, tedy s=h;
q probíhá0..n−1. I zde vyjde n(n²+1)/2. Tím je konstrukce
obecně dokázána, včetně obou diagonál, nikoli jen řádků a sloupců.

## Úplný MIX a tisk

Kniha k úloze21 neposkytuje strojový program; `mixal_magic_square.py`
je naše úplná implementace požadovaného algoritmu. Pole je v paměti
X+nr+c s X=500, výstupní řádek má24 slov od BUF=2000. Program
nejprve celé pole n² slov výslovně nuluje. I1 uchovává násobek řádku
nr, I2 sloupec c, I3 příští číslo k. Kombinace prvních dvou dá adresu.
Před pokusem o diagonální krok se staré souřadnice uloží do I5/I6;
obsazené pole vyvolá návrat ke starému sloupci a posun o dva řádky.
Porovnání a jediné odečtení velikosti řeší přechod přes okraj pro
n>=3. Pro n=1 se po uložení1 rovnou tiskne.

Po vytvoření pole se vynuluje24 výstupních slov. CHAR a STX(3:5)
zapisují trojici desetinných číslic do každého pětiznakového pole;
první dva znaky zůstávají mezery. Každý řádek má tedy pro n=23
115 znaků obsahu a pět koncových mezer. JBUS před přípravou dalšího
řádku čeká na dokončení předchozího OUT, takže se aktivní výstupní
paměť nepřepisuje. Po posledním OUT již program paměť řádku nemění.

Implementace je vymezena na lichá1<=n<=23; právě n=23 zadání žádá.
Všechny indexy jsou nejvýše n²+2n, což je zde575<64²; pole končí
pod1029 a buffer pod2024. Hodnoty1..529 se vejdou do tří desetinných
číslic. Mezivýsledky nenaruší paměť, velikost indexu ani přepínač
přetečení. Obecný matematický důkaz není omezen na tyto strojové meze.

Checker prošel5595 kontrolami: nezávislý souřadnicový vzorec a přímá
chůze souhlasí pro všechny liché řády do101, přičemž byly kontrolovány
všechny součty a všechna čísla. Obrázek16 řádu7 přesně souhlasí.
Celkem47 úplných MIX běhů pokrývá n=23 pro všech37 radixů a menší
řády1,3,5,7,11 pro oba krajní radixy. Celý tisk souhlasí znak po
znaku; počáteční pole i buffer byly úmyslně naplněny nenulovým
odpadem a asynchronní tiskárna měla zpoždění1000u. Pro23 je společný
součet6095. Úspěšný checker neopakovat.

Historie a známá oprava připsání algoritmu jsou v samostatném
`mixal-magic-sources.md`; tento matematický důkaz je uzavřený.
