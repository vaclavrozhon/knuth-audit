# §1.3.1-22: třináct míst mezi programy s časem nejvýše4u

**Výsledek:** při přenositelném kontraktu a čase nejvýše4u před
HLT stačí a v nejhorším radixu je nutných13 dodatečných paměťových
míst. Vstupní buňka2000 se do tohoto počtu nepřičítá; všechny
instrukce, připravené konstanty a pomocná místa ano. Stejná
konvence v knize počítá sedmislovnou smyčku jako7, nikoli8 včetně
vstupu. Výsledek není důkazem globálního prostorového minima7,
pokud je dovolena libovolně dlouhá doba běhu.

Označme b radix bajtu, 64<=b<=100; B=b^5 je mez velikosti slova
a D=b^2−1 největší velikost indexu nebo platné efektivní adresy.
Čas u je jednotka z tabulky138. S jednotkovým časem závěrečného
HLT mají všechny níže míněné nejrychlejší programy nejvýše5u.
Nepředepsané registry a paměť jsou libovolné; program nespoléhá
na nepředepsané periferní zařízení, viz výslovná konvence136.

## Nová konstrukce: nulová položka tabulky je samotný vstup

```
3000  LD1 2000
3001  LDA 2000,1
3002  HLT 0

2000+k  CON k^13       pro každé přípustné nenulové k
2000    [daný vstup X; není zde připravená konstanta]
```

Přípustné hodnoty jsou |X|<=4 pro b=64,65 a |X|<=5 pro b>=66.
Přesné hranice jsou

```
4^13 = 67108864 < 64^5 = 1073741824,
65^5 = 1160290625 < 5^13 = 1220703125 < 66^5 = 1252332576,
6^13 = 13060694016 > 100^5 = 10000000000.
```

Po LD1 je rI1 rovno vstupu, včetně případného znaménka nuly;
velikost nejvýše5 se vždy vejde do dvou bajtů. Pro X!=0 druhý
příkaz načte předepsanou konstantu X^13 na adrese2000+X. Pro
X=0 adresuje právě2000 a načte původní nulový vstup. Žádné slovo
paměti se nepřepisuje. Záporná nula se tak vrátí jako záporná
nula a kladná jako kladná, ačkoli původní číselné zadání tuto
silnější vlastnost nevyžaduje. Nezávisí se na žádném jiném
počátečním registru ani příznaku.

Instrukce jsou stejné pro všech37 radixů. Data tabulky obsahují
právě přípustné celé mocniny; nepoužité krajní buňky pro b<=65
nemusejí být předepsány. To je tatáž přenositelnost číselné
tabulky, kterou používá oprava17.11.2007: nepožaduje se uložit
5^13 do slova na stroji, kde se tato hodnota nevejde a vstup5
není přípustný.

Počet dodatečných míst je3+8=11 pro b=64,65 a3+10=13 pro b>=66.
Maximum přes všechny radixy je13. Nejde o přepsání vstupu na
předem známou nulu: veškeré vstupy zůstávají původní a střed
tabulky se použije jen tehdy, když jeho skutečný obsah je nula.

## Úplná redukce programů s nejhorším časem4u

Pro dolní mez stačí povolený radix100. Zde je D=9999 a vstup+3
vyžaduje A=1594323. Jeho pět bajtů je(0,1,59,43,23). Ostatní
počáteční registry můžeme nejprve zvolit nulové a držet je
stejné pro všechny vstupy. Připravené konstanty programu jsou
nadále libovolné; důkaz je neomezuje.

Jednotkové adresové příkazy mění A o velikost nejvýše D nebo
nastavují velikost nejvýše D. Jediná běžná instrukce čtoucí
vstup stojí2u. Pokud vedle ní zbudou jen dvě jednotkové operace,
velikost A při daném počátečním stavu nemůže přesáhnout2D+3,
pokud vstupní čtení vůbec mění A; to je méně než1594323.
Skok či změna jiného registru tuto mez nezvětší. Totéž platí,
je-li jedna jednotková operace před čtením a druhá po něm.

První pozorování vstupu nemusí být předpokládáno jako LOAD:

- Vykonání nezměněného vstupního slova+3 by bylo MUL za10u.
  Přepis jiného bajtu ponechá opcode3. Přepsání posledního
  bajtu před prvním pozorováním ztratí jediný rozdíl mezi+2
  a+3. Nemůže tedy poskytnout správný vstupně závislý výsledek.
- Kladné MOVE stojí nejméně3u, samo nemění A a zbývající1u
  nedá do A požadovanou velikost. MOVE s F=0 nic nepřenáší.
- FLOT/FIX za3u jsou operace v A a vstup z paměti nečtou;
  zbývající1u běžné čtení nedovolí. FADD/FSUB za4u nemohou
  samy řešit úlohu: pro X=0 ponechají vhodné původní nenulové
  normalizované A nenulové. FCMP A nemění. MUL, DIV, NUM a CHAR
  se do rozpočtu nevejdou.
- IN není na přenositelné instalaci zaručeno. Ostatní I/O
  neposkytne bez něj v tomto čase velký vstupně závislý A.

Při vstupu+3 se tedy musejí vykonat právě dvě instrukce za2u.
Jejich úplný celočíselný seznam tvoří LOAD/STORE, ADD/SUB, CMP
a šest posunů; MOVE má lichou cenu a ostatní operace byly
vyřízeny. Následující rozbor zahrnuje také pozorování vstupu
teprve druhou instrukcí.

Pokud první instrukce vstup nečte, nastaví jen stav nezávislý
na X nebo jej přepíše bez zachování informace. Druhá instrukce
může číst X do A pouze pomocí LDA/LDAN nebo ADD/SUB. Pro kladné
X v rozsahu0,...,5 je výběr pole buď0, nebo X. Výsledkem je
tedy nanejvýš pevná konstanta plus0, X či−X (případně s obvyklým
zkrácením při přetečení). To nedá současně1^13=1 a2^13=8192.
LOAD do jiného registru a CMP výsledný A nenastaví. STORE před
čtením může při nulových počátečních registrech jen vymazat
některé vstupní bajty; velký nový výsledek tím nevytvoří.

Čte-li první instrukce X do A nebo X, zvolené nulové ostatní
registry dávají pouze jeden nenulový bajt3. Jediný následující
posun z něj nevytvoří čtyři různé nenulové bajty požadovaného
3^13. Ostatní indexy se nezměnily, takže další paměťový operand
má pevnou adresu: načtení je konstantní nebo vrací X, a ADD/SUB
dává na kladných vstupech jen afinní funkci se sklonem nejvýše2
v absolutní hodnotě, nikoli třináctou mocninu. CMP jen mění
příznak; žádný skok se už do této dvojice nevejde.

Ani přetečení v posledních dvou odstavcích nezpůsobí výjimku:
číselný výsledek ADD/SUB je modulo B shodný s přesným součtem.
Rozdíl výsledků pro vstupy1 a2 je proto modulo B jeden z
−2,−1,0,1,2, zatímco požadovaný rozdíl je8191.

Zbývá první LOAD vstupu do indexového registru rIi. Následující
posun nulových A/X dá opět nulu. ADD/SUB by sice mohl číst
tabulku indexovanou X, ale první LOAD ponechává původní A:
změna původního A o1 by změnila i výsledek. Tím je porušena
správnost pro libovolný počáteční A. Jediná možnost je proto
LDA nebo LDAN z adresy indexované právě nově načteným rIi.

První LOAD musí rozlišovat velikost i znaménko vstupu. Pole
neobsahující poslední bajt ztratí velikost; pole vynechávající
znaménko nerozliší X a−X. Jde tedy o LD_i nebo LD_iN celého
vstupního slova. Původní index pro jeho adresování nemůže být
nepředepsaný: změna tohoto indexu by odvedla čtení od vstupu
do nezávislé buňky. První LOAD je proto neindexovaný. Druhý
LOAD musí použít právě rIi, nikoli jiný libovolný index.

Obě skutečné instrukce jsou nyní paměťová čtení bez skoku
a bez zápisu. Jejich opcode se proto pro ostatní vstupy ani
počáteční A nemůže změnit; rozbor bodu+3 se vztahuje na tentýž
průběh všech vstupů. Není zde nezdůvodněné přenesení jediné
testované posloupnosti instrukcí na libovolný program.

## Počet tabulkových a kódových buněk

Při b=100 je přípustných jedenáct čísel−5,...,5. První LOAD
vytváří rIi=X nebo−X, takže druhý čte jedenáct různých adres
`a+X` nebo `a−X`. Každá z nich musí obsahovat odpovídající
třináctou mocninu nebo její zápornou hodnotu, podle volby
LDA/LDAN. Tyto hodnoty jsou navzájem různé; obě znaménka
nuly mají stejný operační bajt0.

Na radixu100 mají velikosti k^13 tyto operační bajty, tedy
zbytky modulo100:

| k | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| k^13 mod100 | 0 | 1 | 92 | 23 | 64 | 25 |

Žádná tato hodnota není opcode9,...,14 nebo17,...,22 prvního
indexového LOAD, opcode8 či16 druhého LOAD do A, ani opcode5
závěrečného HLT. Znaménko slova opcode nemění. Tabulková buňka
proto nemůže současně být jednou ze tří vykonaných instrukcí.
Ty leží na třech různých adresách: bez skoku a samomodifikace
po sobě následují dvě čtení a HLT.

Z jedenácti tabulkových adres může nejvýše jedna být danou
vstupní buňkou2000. Ostatních nejméně deset musí být připravené
konstanty: bez předchozího zápisu nemůže libovolná nepředepsaná
paměť zaručovat jejich hodnoty. Tím je nutných nejméně3+10=13
dodatečných míst. Nová konstrukce této meze dosahuje.

Použití jediného radixu100 je platná dolní mez pro přenositelný
program nebo rodinu programů fungující ve všech radixech. Výsledek
říká, že maximální potřebný prostor mezi všemi radixy nelze
snížit pod13 při zachování času nejvýše4u. Netvrdíme zvláštní
minimum13 pro každý jednotlivý radix66,...,99; shoda datových
slov s instrukcemi by tam vyžadovala samostatný rozbor.

## Evidence a přesně zachované otevřené části

Originály143 a509 byly znovu přímo zobrazeny. Časy a instrukční
sémantika138/139, znaménka131/134/135 a volitelnost I/O136 jsou
již přímo přečtené; floating224 ve svazku2 byl přímo ověřen
v důkazu24(b). Čtyři vrstvy errat včetně opravy krajních tabulkových
hodnot17.11.2007 byly přečteny po stranách i věcně. Nová konstrukce
nemění žádný frozen podklad.

Původní tabulka na509 skutečně používá14 míst; její uvedený
počet ani minimální čas nejsou tímto zlepšením vyvráceny. Není
založen nový nález chyby pouze proto, že jsme tabulku zmenšili.
Zůstává otevřena globální prostorová dolní mez7 pro programy
s libovolnou dobou běhu. Nový program zároveň uzavírá čas4u
i pro silnější požadavek zachovat znaménko nuly: dolní mez
číselného zadání se na silnější kontrakt vztahuje automaticky.

Nový cílený checker `check_power_fast_space.py` ověřil všech440
přípustných vstupních slov přes37 radixů, včetně obou nul:
2*10 případů pro b=64,65 a35*12 případů pro ostatní radixy.
Ostatní registry i paměť byly předem nenulové, indexy záporné,
příznak přetečení zapnutý. Všechny případy mají čas5u s HLT,
přesný znaménkový výsledek a nezměněnou paměť. Výsledky jsou
v `results/power-fast-space.json`. Jde o kontrolu nového programu;
starší úspěšné testy nebyly spuštěny znovu. Obecná správnost
i dolní mez jsou dokázány výše nezávisle na tomto výčtu.
