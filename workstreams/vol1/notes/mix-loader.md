# §1.3.1-26: dvoukartový zaváděcí program

Program na s.510 načte další program z děrných štítků. Pracuje pro
všechna b=64,...,100, kde b je počet hodnot jednoho MIX bajtu.
Kód znaku je číslo bajtu v tabulce1; číslice mají kódy30–39,
poslední číslice záporného slova se čte jako10–19. Vstupní slovo
se vždy načte se znaménkem +. Registry a paměť před GO mohou být
libovolné, kromě právě zavedených prvních16 slov.

Použity známé opravy: GO vynuluje overflow (29.11.2011);
první cílová adresa může být0100 (3.11.2022); znak na řádku03
je O, nikoli0 (21.11.1998); řádek27 má adresový znak J
(30.12.1997). Originály errat byly zobrazeny. Tyto dvě znakové
opravy jsou nutné pro souhlas děrných štítků se symbolickým kódem.

## Synchronizace dvou karet a vstupu

GO načte první kartu do0–15 a spustí adresu0. IN16(16) zahájí
načítání druhé karty do16–31. Následující IN29(16) nejprve počká
na dokončení **téže čtečky**, takže celý kód16–28 už je bezpečně
v paměti. Nová vstupní karta přepisuje pouze29–44, tedy vyrovnávací
oblast BUFF. LD1 0(0:0) nastaví rI1=+0; znaménko v0 je kladné.
JBUS3(16) pak počká na celý datový blok. Následující čtení bufferu
je proto správné bez jakékoli pevné představy o rychlosti čtečky.

## Zpracování hlavičky

LDA30 načte sloupce6–10, tedy počet a čtyřcifernou adresu.
SLA1 odstraní počet a SRAX6 posune zbylé čtyři znaky na správné
pozice desetibajtového AX; původní X je přitom zcela vytlačeno.
NUM převede adresu a STA0 ji uloží do LOC. LDA30(1:1) čte kód
počtu, SUB adresové pole instrukce NUM30 odečte30: výsledkem
je k=0,...,7. LD3 LOC nastaví cílový index. Když k=0, JAZ0,3
přejde přímo na startovní adresu z transferové karty.
Sloupce1–5 se nepoužívají; text TRANS je konvence formátu.

## Invariant vnitřní smyčky

Před zpracováním j-tého slova karty (j=0,...,k−1) platí:

```
rI1 = 2j
LOC = původní_cílová_adresa + j
rI3 = LOC
rA  = k-j
```

STA29 uloží zbývající počet. LOC se zvýší o1 pomocí adresového
pole instrukce SLA1, ale rI3 stále ukazuje aktuální cíl.
LDA32,1(5:5) vezme poslední znak aktuálního desetiznakového slova.
Po odečtení25 je A záporné pro kódy10–19 a kladné pro30–39;
STA0,3(0:0) uloží jen toto znaménko do cíle.

LDA31,1 a LDX32,1 načtou celé desetiznakové slovo. NUM bere každý
kód modulo10, takže přetisk znaménka nemění číselnou velikost.
STA0,3(1:5) uloží pouze velikost a zachová připravené znaménko.
Takto se zachová i **záporná nula**, což by prostý zápis A nezajistil.
Předpokladem je jako vždy reprezentovatelnost vstupní velikosti v pěti
bajtech; při b=64 nejde libovolné desetinné desetimístné číslo uložit.

MOVE0,1(2) má zdroj i cíl rI1. Kopíruje dvě slova na sebe, tedy
nic v paměti nemění, a přitom zvýší rI1 o2. LDA29 a SUB adresového
pole SLA1 sníží zbývající počet. JAP11 se vrátí na LD3 LOC, pokud
zbývá další slovo; jinak JMP1 čte další kartu. Invariant se obnoví.
Nejvýše sedm slov odpovídá dostupným14 slovům dat za hlavičkou.

Program používá jen adresy do32, kódy operací do47 a povolené
znaky; zakázané bajty20,21,48,... se v obou kartách nevyskytují.
Všechny adresové konstanty jsou menší64, takže stejné **znaky karet**
mají stejnou číselnou hodnotu při každém radixu. Náhrada pole(2:5)
posuny obchází jeho zakázaný kód21. Konstanty1,30,25 jsou adresy
už existujících instrukcí, není potřeba další konstantové slovo.
29instrukcí se vejde do dvou karet po16 slovech; zbylá tři slova
jsou volná a později mohou být přepsána bufferem.

## Reprodukce a její rozsah

`check_mix_description.py` porovnává ručně přepsané znakové řádky
se samostatným číselným sestavením symbolických instrukcí. Shoda
byla ověřena pro všech37 radixů. Dále pro každý radix běží úplné
zavedení s prodlevami čtečky0,17,100 jednotek, adresami100,1000,3999,
počty1,3,7, kladnou i zápornou nulou a maximální reprezentovatelnou
velikostí obou znamének. Model zakazuje čtení/zápis nedokončeného
vstupního bloku. Všechny případy prošly; konečný transfer nastává
po řádku12 s J=13 a prázdnou vstupní frontou.

Tři zvolené prodlevy samy nejsou důkazem všech rychlostí zařízení.
Ten dává výše uvedená závislost IN na předchozím IN a čekací JBUS,
za předpokladu, že každé čtení nakonec skončí. Při poruše čtečky
specifikace dovoluje čekat trvale. Původní chybné znakové řádky
nejsou vydávány za funkční program ani za nové nálezy.
