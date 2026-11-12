# V0054–V0055: přesné zbývající smluvní hranice

6. listopadu 2026. Tato poznámka zužuje staré neadresné „IEEE partial“
na konkrétní tvrzení a odděluje je od hotových důkazů. Není novým nálezem
a nepožaduje dokazovat správnost libovolného hardware nebo uživatelských
handlerů.

## 1. Celý skutečný výsledek epsilon okrajů

Primární definice MMIX-doc:1440–1487 pracuje s nezáporným epsilon;
invalid vyjmenovává pro NaN v rE/Y/Z nebo záporné rE. Kód
`fepscomp` začíná testem znaménka rE a pak rozlišuje jeho třídu.
Skutečné chování je úplně určeno, nikoli ověřeno jen několika příklady:

* Nastavený sign bit rE, včetně −0 a −∞, ihned vrací 2.
* Každé NaN rE rovněž vrací 2. U přípustného epsilon vrací 2 také
  každá ze sedmi dvojic operandových tříd s alespoň jedním NaN.
* Dispatcher z hodnoty 2 udělá výsledek 0 a event I pro FCMPE/FEQLE;
  FUNE vrátí 1 a žádný event, i pro signaling NaN. Toto je vlastní
  výslovná MMIX konvence.

Pro **rE=+∞** je ee=10000. Po případném odečtení d je exponent
nejméně 10000−2045=7955, neboť po unsubnormalizaci mají konečné
nenulové operandy exponenty 0..2045; nula je při testu podobnosti
přesunuta na stejný exponent. Proto konečná porovnávací větev vrátí 1
ještě před dalšími posuny. Nedochází k posunu o 10000 ani k chybě S0001.
Úplná tabulka pro dva nenanové operandy, se všemi znaménky, je:

| Typy y,z | FCMPE | FEQLE | FUNE |
|---|---:|---:|---:|
| dvě nuly | 0 | 1 | 0 |
| dva konečné nenulové | 0 | 1 | 0 |
| dvě infinity | 0 | 1 | 0 |
| právě jedna nula, druhý nenulový | 0 | 0 | 0 |
| konečný nenulový a infinity | 0 | 0 | 0 |

Třídy partitionují všechny takové vstupy. Obě infinity mají při
ee≥1023 shodu bez ohledu na znaménko. Mixed infinity větev vrací
pouze similarity, nikoli equivalence. Nulové větve jsou odděleny
před numerickým invariantem. Pro žádný řádek nevzniká event.

## 2. Dvě přesné nevyřešené interpretační otázky

**rE=−0.** „Negative“ může v tomto kontextu označovat sign bit, anebo
matematický vztah ε<0. V druhém výkladu by −0 bylo přípustné a mělo
stejné okolí jako +0, zatímco první výklad přesně odpovídá kódu.
MMIX výslovně rozlišuje signed nuly, ale běžné FEQL je ztotožňuje;
z toho samotného nelze vybrat význam tohoto slova u epsilon. Nevyvozuji
nový programový rozpor bez dalšího jednoznačného kontraktu.

**rE=+∞ a FEQLE(konečný nenulový, infinity).** Pokud jsou x v okolí
konečného u rozšířená reálná čísla a nekonečné epsilon se dosadí
doslovně, pak N∞(1) obsahuje +∞, protože |∞−1|≤2·∞. Zároveň N∞(+∞)
obsahuje 1 podle výslovného pravidla pro ε≥2. Doslovně by FEQLE dalo 1.
Pokud však x v konečném okolí zůstává reálné nebo se N∞(u) chápe jako
sjednocení okolí přes konečné epsilon, toto okolí infinity neobsahuje
a FEQLE dává 0, stejně jako kód. Dokument neupřesňuje tento přechod
domény. Podobnost a nula s Nε(0)={0} nemají stejnou nejasnost.

Zbývající položka tedy není „neověřený IEEE detail“: epsilon je vlastní
MMIX rozšíření. Je to konkrétní hranice matematické domény převzatého
popisu pro dvě hodnoty rE. V0055 a jeho epsilon leaf zůstávají partial,
s úplně doloženým chováním programu. Bez nové karty, opravy či běhu.

## 3. Co přesně ještě znamená široké IEEE tvrzení

Na file20/p12 stojí, že MMIX zahrnuje plnou implementaci IEEE/ANSI 754,
a podrobnosti deleguje na §4.2 a MMIXware. Z tohoto širokého výroku
nelze udělat důkaz pouhou shodou tabulky formátů. Současně není
důvod otevírat uzavřené jednotlivé operace znovu. Rozsah je nyní:

| Konkrétní závazek | Stav a důkaz |
|---|---|
| binary32/binary64 formát (§3.1–3.2) | Vlastní rozklad polí a hodnot, shoda s primárním IEEE §3; `fp-comparisons-recovery.md` §1. |
| Čtyři směry, všechny sedm aritmetických operací, signed nuly, NaN a infinity | Úplné vlastní větve a invarianty v příslušných čtyřech aritmetických poznámkách. Originální S0002/S0003/S0004 a auditní opravy jsou oddělené. |
| Integer/float a short konverze (§5.3–5.5) | `fp-conversions-recovery.md` plus samostatný S0004 event důkaz; všechny vstupy a režimy. |
| Porovnání (§5.7) | Vlastní MMIX FCMP/FEQL/FUN jsou uzavřené; případná odchylka FEQL pro sNaN je v MMIX-doc výslovně přiznána. Není tiše vydávána za obecné pravidlo IEEE. |
| Short vstupy → jedna operace → STSF | Celý důkaz hodnot i disabled-trip eventů v `fp-short-arithmetic-recovery.md`, včetně falešného dopadu na subnormál. |
| Decimal↔binary (§5.6) | Přesná zbývající matematická/implementační povinnost pro obecné tvrzení: MMIXware `print_float`/`scan_const`, požadované rozsahy, monotonicita a správné decimal rounding. Výše uvedené binární důkazy tyto funkce neověřily. |
| Precision control (§4.3) pro obecné double operandy a širší exponentový rozsah | Tvrzení o short vstupních operandech dokazuje jen svůj přesný obor; nesmí se zaměnit za obecné rozhraní single-precision rounding každého double mezivýsledku. Konkrétní realizace či přesné omezení převzaté shody zbývá doložit. |
| Trapping interface (§7.3–7.4 a §8) | Zbývá přesné přiřazení IEEE upraveného exponentu/předaného výsledku k MMIX trip protokolu a případné deklarované odchylce. To není požadavek dokazovat libovolný handler. Skutečná implementace vstupu do trip/RESUME je vedena u pozdějších vlastních stránek a úloh, bez jejich duplikování zde. |

IEEE extended formáty podle §3.3–3.4 nejsou automaticky dalším povinným
formátem MMIX: zdejší „should“ pro extended rozšíření se nesmí číst
jako „shall“. Připouštěné MMIX odchylky (například O/X při zapnuté
overflow výjimce) nejsou samy novými nálezy; případná hranice obecného
slova „full“ se musí posoudit v kontextu celé deklarované architektury.

V0054 tedy zůstává partial kvůli konkrétním posledním třem řádkům,
nikoli kvůli znovu požadovanému důkazu FREM, FSQRT nebo FINT. Provedené
programové kontroly se nezapočítávají jako další knižní chyby a plná
stránka se nezelení jen proto, že zmizela většina starých dílčích mezer.


Aktualizace7.listopadu: precision-control řádek výše byl přesně uzavřen
v `notes/fp-precision-control-scope.md`; nepodmíněná širší povinnost
neplyne z IEEE4.3. Decimal helper má samostatný hodnotový rozporS0009;
celý decimal a trapping interface nadále zůstávají partial.
