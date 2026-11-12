# MMIX-S0006 — Fgetws na prázdném EOF vrací úspěch místo −1

**Confirmed, medium, pouze doprovodný program.** Oba archivované
MMIX-IO vracejí 0, pokud Fgetws požaduje alespoň jeden wyde a soubor
je již na konci před prvním znakem. Správný kontrakt v knize vyžaduje
−1. Volající tak nemůže rozpoznat konec souboru podle deklarovaného
znaménka návratu. Žádná chyba knižní definice se tímto neoznačuje.

## Normativní řetězec a jednoznačně vybraný obor

Fascikl p42/file50 definuje Fgetws jako Fgets nad wyde znaky. Čtení
končí po size−1 znacích nebo po newline, a EOF před dokončením má
vrátit −1. Je-li size=2 a nebyl přečten žádný znak, žádná dokončovací
podmínka nenastala. Výsledek tedy není věcí interpretace.

MMIX-SIM:322–346 uvádí stejný text a také přibližnou C analogii
`fgetws(...)?wcslen(...):-1`. Pro EOF před prvním znakem dává i tato
analogie −1. C11 draft N1570 §7.29.3.2 odst.3, p422/file440, výslovně
vrací null pointer, pokud EOF nastal bez přečteného znaku. Primární
PDF a zobrazená sazba jsou v `sources/c11-n1570.pdf` a
`images/c11-n1570-fgetws-return.png`; výňatek je uložen zvlášť.
Neodvozuji zde MMIX wyde encoding z platformního wchar_t.

U **neprázdného posledního řádku bez newline** knižní/MMIX-SIM text
a C analogie naopak nejsou totožné: C dovoluje úspěšný krátký poslední
řádek. Tato samostatná interpretační povinnost zůstává otevřená.
Zde se nevyužívá ani se nepřekrývá s dokázaným prázdným EOF.

Přípustný stav: handle3 je otevřený BinaryRead stream f≠stdin,
na aktuální pozici není žádný další byte, bez read error. Buffer je
sudý a jeho potřebné byty jsou dostupné. V MMIX $255 ukazuje na dvě
zarovnané octa (buffer,2), rG=32 a rL=0 jsou platné. Instrukce
`TRAP 0,Fgetws,3` má kód #00000503. MMIX-SIM:2399 a :2406 vrátí
výsledek mmix_fgetws přes rBB přímo do $255. Očekávané bity jsou
#ffffffffffffffff, nikoli nula. Handle může pocházet z běžného Fopen;
nevztahuje se na speciální interaktivní stdin adaptér.

## Přesná stopa a celá rodina

MMIX-IO:225–272 má po kontrolách režimu a size:

    size ← S−1;  o ← 0;  eof ← 0.

Pro S=2 je s=min(127,size)=1. Smyčka začne s n=0,p=buf. První
`fread(p,1,2,f)` vrátí 0 a nastaví EOF. Podmínka !eof je nepravdivá,
takže se nevrátí neg_one; provede se break bez zvýšení n. Na buf[0]
a buf[1] se uloží nula. Vnější část je zapíše do MMIX paměti, zachová
o=0 a kvůli eof vrátí o. Skutečný výsledek je **0**.

Stejná stopa platí pro každý požadavek 2≤S<2^63 a každou dostupnou
sudou buffer adresu, protože min(127,S−1)≥1 a hned první hostitelský
pokus končí EOF. Platí i pro TextRead a BinaryReadWrite s odpovídajícím
platným streamem; readwrite pouze zruší oprávnění k dalšímu zápisu
bez Fseek. Pro zvolený prázdný soubor není žádná endian/encoding
konvence schopna vytvořit znak ani newline.

Použití vyššího size.h netvoří velký přenos: stále se provede jediné
fread o 2 bytech a návrat. Žádný velký buffer se v rutině nealokuje.
Pozorovanou malou část MMIX paměti lze doplnit na plný virtuální
buffer; nedotčené byty nejsou vstupem do této stopy.

## Invariant a přesný rozsah opravy

Pro platný požadavek S≥1 označme B počet celých wydes přečtených
dřívějšími plnými bloky. Na vstupu vnější iterace je o=B,
size=S−1−B a buffer=A+2B modulo 2^64. Požadavek každé vnitřní
smyčky je s=min(127,size). Po n úspěšných čteních uvnitř bloku platí
0≤n≤s, p=buf+2n a buf[0..2n−1] jsou právě tyto n celé znaky.
Neúplný fread tento počet nezvýší. Dvojice nul se vejde do buf[256],
protože 2n+2≤256. Po uložení úspěšného bloku se B zvětší o n,
size zmenší o n a adresa o 2n, což invariant zachová. Newline nebo
vyčerpání size či eof ukončí vnější smyčku.

V oboru S<2^63 nemůže B ani B+n přetéct, takže test
`!o.h && !o.l && !n` znamená přesně „zatím žádný celý wyde v tomto
volání“. Nový guard v `sources/audit-fgetws-empty-eof.ch` zní:

    if (eof && !o.h && !o.l && !n) return neg_one;

Je umístěn hned za čtením bloku, před zápisem do MMIX paměti. EOF
bez jediného znaku vrátí správně −1; žádná úspěšná dokončovací podmínka
v této větvi není možná. Paměť smí být při chybě podle MMIX kontraktu
nedefinovaná, takže její ponechání beze změny je přípustné. Nebyla
přidána žádná práce s hostitelskými ukazateli, posun ani aritmetika.

Všechny ostatní větve jsou zachovány:

* špatný read mode a S=0 vracejí původní −1 před smyčkou;
* S=1 má s=0, nečte hosta, eof zůstane 0 a vrací původní úspěšnou
  nulu s terminátorem; tento výsledek není zaměněn s požadavkem S≥2;
* plná quota a newline mají n>0 nebo eof=0, takže guard nezasáhne;
* embedded #0000 je běžný přečtený znak, zvyšuje n a sám neukončí
  čtení; podmínkou newline zůstává #000a;
* ne-EOF read error již vrací −1 z vnitřní větve;
* EOF po neprázdném prefixu má B+n>0 a zůstává beze změny, protože
  právě jeho normativní výklad zde nebyl uzavřen;
* interaktivní stdin větev nenastavuje eof a guard se jí nedotkne.

Pro všechny pokračující iterace s>0 musí být n=s≥1: jinak by musel
nastat newline, EOF nebo error, které už vedou k návratu. Zbývající
size je tedy klesající nezáporná varianta. Nulová quota končí ihned.
Čtení provede nejvýše S−1 úplných znakových pokusů a nejvýše jeden
neúplný koncový pokus; počet vnějších bloků je nejvýše
floor((S−1)/127)+1. Oprava přidává jeden konstantní test na blok,
žádnou smyčku. Tyto náklady nejsou architektonický čas TRAP, který
samotnou službu OS nezahrnuje.

Tento argument dokazuje zamýšlenou malou změnu a zachování ostatních
cest. Není to blanket důkaz Fgetws: odd buffer convention, neprázdný
unterminated EOF, stav s oběma sticky EOF/error flags a platformní
wyde soubory mají vlastní povinnosti v `io-recovery-open-obligations.md`.
Pro potvrzený svědek jsou buffer sudý, stream bez read error a soubor
prázdný; žádný z těchto otevřených bodů ho nemůže změnit.

## Originální sazba, známé opravy a cílený běh

MMIX-IO 2013 a 2025 jsou celé byte-identické, hash
`d6732108356986956f4e4a5a883d210a1e4e69216e1f8d614c456fd3126496e5`.
Veřejný originál [MMIX-IO §§16–17](https://mmix.cs.hm.edu/doc/mmix-io.pdf#page=6)
byl zobrazen v `images/mmix-io-upstream-file006.png`. Má unsigned
declaration handle a tetra n,s, kde archivované zdroje mají unsigned
char a int; n=s=0/1 pro witness a stejná EOF větev dávají identický
výsledek. Rozdíl deklarací je výslovný, PDF se nevydává za stejný
byteový soubor. Knižní p42 byla znovu zobrazena u S0005.

Deset veřejných opravných vrstev je v `results/errata-S0006.json`.
Oprava MMIXware p143 z 21. března 2009 inicializuje eof=0 a v obou
ověřovaných verzích již je. Neřeší chybějící záporný návrat při
skutečně zjištěném EOF. Opravy stdin/-f výslovně řeší jiný interaktivní
adaptér. Další nalezené EOF zmínky patří ke čtení zdrojového souboru
assembleru. Všechny kontexty byly přečteny, odpovídající oprava zde
nenalezena. Fyzický MMIXware výtisk ani světové prvenství se netvrdí.

Jeden nový `nice -n 15` běh `verify_fgetws_empty_eof.py` provedl
**18 volání**, devět pro společný originál a devět pro samostatnou
opravu, čtyři úspěšné build kroky. Všechny streamy jsou skutečné C
tmpfile s nejvýše čtyřmi uloženými byty; žádný mock fread ani wchar_t
orákulum. Tři prázdné vstupy mají S=2,128,2^32+2. Ve všech je
fread EOF, host_error=false, pozice0; originál vrátí0 a oprava−1.
Šest kontrol je newline před dalšími daty, celá dvouznaková quota,
vložený NUL před newline, S=1, S=0 a špatný mode. Všechny mají stejné
správné návraty i očekávané uložené prefixy v obou verzích.

`results/fgetws-empty-eof.json` obsahuje všechna pozorování a obsah
paměti, build log je zvlášť. Vysoké S nevyvolalo velkou alokaci ani
dlouhý přenos. Žádný dřívější verifier se neopakoval. Malé příklady
potvrzují konkrétní C cestu; obecný důkaz celé zvolené rodiny je výše.
