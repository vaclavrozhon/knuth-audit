# Program A: kapacita odpovědi a prázdná identita

Kontrola 1. listopadu 2026. První dotisk třetího vydání, tištěné s.164,
167–169; originální obrazy přečteny. Tištěný exemplář nebyl kontrolován.
`MAXWDS=1200` je mez délky vstupu ve slovech; jedno slovo představuje
jeden pětiznakový symbol nebo závorku. Výstupní pole `ANS` má stejnou
velikost. `OUTBUF` za ním má24 slov, pak začíná kód.

## C0029: potvrzená nedostatečná kapacita

Použijme2t různých jmen a_i,b_i, kde1<=i<=t. První vstupní cyklus
je `(a_1 ... a_t)`, druhý `(a_1 b_t a_t ... b_2 a_2 b_1)`.
Součin se jako v knize aplikuje zleva doprava. Druhý cyklus posílá
b_i na a_i a a_i na b_(i−1), přičemž index0 znamená t. Součin tedy
vymění a_i s b_i pro každé i: výsledek je t disjunktních transpozic,
tj. cyklů délky2. Vstup má3t+4 slov, výstup4t slov. Už t=5 ukazuje,
že výstup nemusí být kratší:19 versus20 slov.

Pro skutečné selhání původní alokace bereme t=320. Jména `A0001` až
`A0320` a `B0001` až `B0320` jsou přípustná pětiznaková pole; žádné
není závorka, prázdné pole ani ukončovací znak. Každý cyklus má různá
jména.964 neprázdných slov s výplní a koncovým znakem zabere61 karet,
976 slov. To je uvnitř vstupní kapacity. Výsledek má1280 slov.

`check_permutation_a_capacity.py` nejprve nezávisle složí tabulky
obou permutací a ověří všech640 obrazů. Potom běží přesný tištěný
program, nikoli pseudokód. První zápis mimo `ANS[1200..2399]` nastane
na řádku64 po2938338 instrukcích, na adresu2400. Program dále
přepíše své instrukce; na `OPEN=2458` leží jméno `B0315`. Při návratu
na OPEN po315. transpozici se tato data vykonají jako neplatná I/O
instrukce. Model skončí výjimkou po3083245 instrukcích. Záznam
`results/permutation-a-capacity.json` uchovává konec stopy. Vytištěno
je61 kopií karet a žádná odpověď. Selhání není důsledkem timeoutu.
Obecný počet slov sám dokazuje nedostatečnou alokaci, nezávisle na
konkrétním chování modelu po přepsání kódu.

Oprava pouze alokace zavede `MAXANS EQU 2*MAXWDS+23` a
`ANS ORIG *+MAXANS`. Její dostatečnost: označme N počet různých jmen.
Každé patří právě jednomu výslednému cyklu. Cyklus délky k>=2 potřebuje
k+2<=2k slov; singletony se mažou. Finální délka nepřekročí2N<=2400.
Dočasně zapsaný singleton má3 slova; jestliže byl právě zpracován
některý z V>=1 pevných bodů, délka nejvýše2(N−V)+3<=2N+1.
To se do pole2423 slov vejde. Při nulovém výsledku se doplní `()`.
Nakonec řádky51–52 napíší23 nul pro zarážku a tiskovou výplň, takže
alokace2MAXWDS+23 postačuje i v krajních případech.

V MIXAL se výrazy vyhodnocují zleva doprava; pomocné EQU je záměrné.
Zápis `*+2*MAXWDS` by nebyl ekvivalentní požadované opravě.
S opravenou alokací je `OUTBUF=3623`; celý kód i literály jsou pod4000,
adresy ve dvoubajtových registrech pod4096. Sestavení ověřeno pro všech
37 radixů64–100. `check_permutation_a_capacity_fix.py` ověřil úplný
stejný vstup v radixech64 a100 s asynchronním I/O o zpoždění1000u:
3197486 instrukcí,4509819u CPU,61 kopií vstupu a54 řádků přesně
správné odpovědi. Výsledky uloženy, úspěšné běhy neopakovat.

Prohledány všechny4 vrstvy errat podle s.168–169 i MAXWDS, ANS,
OUTBUF a vstupní/výstupní kapacity. Relevantní oprava nenalezena;
kontrola webu rovněž žádnou konkrétní dřívější zprávu neodhalila.
To není tvrzení o prvenství. Návrh zprávy je `reports/V1-C0029.txt`.

## C0028: kandidát pro vstup `()`

Kniha na s.164 užívá `()` pro identitu a Program A ji také tiskne,
avšak výslovně neříká, zda se smí objevit jako vstupní cyklus.
Proto je následující problém pouze kandidát k vyjasnění domény.
Jedna karta obsahuje levou závorku, pravou závorku,13 prázdných polí
a koncový znak. Řádky30–32 načtou pravou závorku jako první jméno,
ale A stále obsahuje levou závorku; řádek33 tedy nedetekuje zavírací
symbol. Při další fázi je pravá závorka pokládána za jméno a následný
průchod najde koncový znak. Ten se pak opakovaně vypisuje, protože
nesouhlasí se START a ve vlastním vstupním rozsahu se nevyskytuje.

`check_permutation_a_edgecases.py` zastaví přesný běh před prvním
zápisem mimo ANS: řádek72, registrI1=2400,96058 instrukcí,134513u.
Ve všech třech radixech64,65,100 leží v ANS po závorkách1198 kopií
koncového znaku. Fáze DONE nebyla dosažena. Jde o doložený konečný
prefix, nikoli tvrzení o nekonečném běhu po přepsání paměti. Čtyři
vrstvy errat neobsahují nalezené vyjasnění ani opravu. Oprava kapacity
C0029 tento doménový problém neřeší.
