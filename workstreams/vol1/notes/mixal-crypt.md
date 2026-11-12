# §1.3.2-13: počítání četností znaků

Kontrola1.11.2026. Zobrazeno zadání s.159 a odpověď s.515–516.
Počítají se neprázdné znaky před první hvězdičkou; vstup papírové
pásky20 obsahuje bloky14 slov po pěti znacích. Terminál19 vypisuje
bloky14 slov. Zdroj `mixal_crypt.py` přesně přepisuje program,
`check_mixal_crypt.py` jej porovnává s nezávislou četnostní tabulkou.

## Správnost čítání

TABLE[c] pro kód c obsahuje počet již zpracovaných výskytů. Pro blank0
a hvězdičku46 má zvláštní hodnotu-1. Ostatní položky jsou zpočátku0,
jak předpokládá komentář programu; nevyplněná paměť rovněž obsahuje0.
Pracujeme s platnými MIX znaky a s četnostmi, které se vejdou do
sedmi desetinných míst požadovaného výstupního formátu. Bez této
přirozené kapacitní podmínky kód vypisuje jen posledních sedm číslic;
není to libovolně přesný čítač.

rX obsahuje zbývající znaky současného slova. `SLAX 1` přesune jeho
nejlevější bajt na pravý konec rA. `STA *+1(2:2)` uloží tento bajt
do nižšího adresového bajtu následující `ENT1 0`; vyšší bajt zůstává0.
rI1 je tedy přesně kód dalšího znaku, nezávisle na zbytku a znaménku rA.
Načtená TABLE[c]>=0 se zvětší a uloží. Zápornou hodnotu mají právě
blank a hvězdička: nenulový kód okamžitě zahájí tisk, nulový se přeskočí.
Je-li zbytek rX kladný, pokračuje se posunem; je-li nulový, jsou všechny
zbývající bajty slova blanky a lze rovnou načíst další slovo.

Důležité umístění značky4H: patří k `LDX`, ne k předchozí `INC5`.
Při prvním vstupu do bloku tak program skutečně načte jeho první slovo.
Sentinel za14 vstupními slovy má hodnotu-1 a nemůže se splést s žádným
slovem znakového vstupu, jehož znaménko je vždy+. Když sentinel ukončí
blok, zpracovalo se všech70 znaků, kromě účelně přeskočených blanků.

## Dvojice vstupních pamětí a čekání

BUF1=2000, BUF2=2016. Za každým blokem jsou sentinel a odkaz na druhý
blok. PrvníIN zahájíBUF1, následujícíIN doBUF2 nejprve počká na jeho
úplné dočtení. rI6 se pak přepne odkazem zpět naBUF1 a zpracovává
se hotový blok, zatímcoBUF2 se čte. Opakování střídá obě role.
Žádná operace nečte dosud nedokončený vstup ani nepřepisuje současně
zpracovávaný blok. To je invariant nezávislý na konečné latenci pásky.
Protože před zpracováním bloku se vždy zadá čtení následujícího,
předpoklad jednoho dodatečného bloku po bloku s hvězdičkou je potřebný
a přesně postačuje. Znaky po první hvězdičce se nepočítají.

## Výstup a jeho cena

Smyčka rI1=1..63 přeskočí nulové a záporné položky. CHAR převede
kladný počet na deset číslic, z nichž posledních sedm jde do výstupu:
dvě z konce rA a pět z rX. ST1 dodá znak, dva blanky jej oddělují od
čísel a zbývající paměť je prázdná. Skutečný70znakový blok má deset
úvodních blanků, znak, dva blanky a sedm číslic; následuje50 blanků.
`CMP1 =63=; INC1 1; JL` správně zahrnuje63: změna indexu nemění
příznak dřívějšího porovnání.

JBUS je před všemi třemi zápisy do sdíleného výstupního bloku, takže
pomalý tisk nemůže číst právě přepisovanou zprávu. Převod CHAR se
provádí před čekáním a již se překrývá s předchozím tiskem. Po posledním
zjištění připravenosti zbývá1u za JBUS,6u za tři zápisy a1u za OUT;
předpřipravený druhý blok by mohl zahájit OUT za1u od připravenosti.
Maximální potenciální úspora na takto omezeném řádku je proto7u.
Dodatečná obsluha dvou bloků by z ní ještě ubrala. Originál opravdu
uvádí7u; OCR zde chybně dává1u. Tvrzení „není žádoucí“ je hodnotící
poznámka, nikoli věta o globální optimalitě všech implementací.

## Kontrola, errata a bibliografie

1992 kontrol v498 bězích prošlo napoprvé;2742 výstupních řádků bylo
porovnáno celé. Radixy64/100, latenceI/O0/43/1200, všechny70 pozice
hvězdičky uvnitř bloku, několik hranic mezi bloky, prázdný a čistě
blankový vstup, všechny definované znaky a přednastavené mezní
sedmimístné četnosti. Každý běh navíc ověřil přesně jeden přednačtený
blok navíc a zachování obou záporných položekTABLE.
Tento konečný test doplňuje výše uvedené obecné invarianty.

Vrstvy all1-prepre,all1-pre,all1,err1 a aktuálníTeX byly prohledány
podle s.159,515–516 a tématu; oprava tohoto programu nenalezena.
Relevantní sousední errata patří sedlovým bodům a velikonoční úloze14.
Nový nález v knize není.

Odkaz Bourne–Ford souhlasí s primárním záznamem vydavatele:
[A study of the statistics of letters in English words](https://www.sciencedirect.com/science/article/pii/S0019995861800363),
Information and Control4(1),1961,48–67. Bibliografická data uložena
v `sources/bourne-ford1961-crossref.json` s metadaty. Článek samotný
se zde nepoužívá k numerickému tvrzení a nebyl celý přečten. Kniha na
něj pouze odkazuje pro informace o četnostech; tento omezený rozsah
bibliografické kontroly postačuje pro dané tvrzení.
