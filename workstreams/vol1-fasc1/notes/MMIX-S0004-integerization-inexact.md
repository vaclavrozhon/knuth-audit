# MMIX-S0004 — FINT, FIX a FIXU ztrácejí příznak inexact

**Confirmed, medium, pouze doprovodný program.** Obě původní verze
MMIX-ARITH (2013-10-17 a 2025-06-20) při zaokrouhlení konečného necelého
vstupu instrukcemi FINT, FIX a FIXU neohlásí X. Číselná hodnota je správná;
nesprávný je pozorovatelný stav rA. Správná definice v knize není nálezem.

## 1. Přesná normativní vazba, zvlášť pro každou instrukci

Použitý standard je **ANSI/IEEE 754-1985**, nikoli pozdější standard
s více variantami round-to-integral. Původní sazba §4, §5.4–5.5 a §7.5
byla zobrazena v souborech `images/ieee754-1985-file011.png`, `013.png`
a `018.png`; jde o tištěné strany 5, 7 a 12. Celý dokument a původ jsou
v `sources/ieee754-1985.pdf` a jeho metadata souboru.

* **FINT:** §5.5 předepisuje převod na celočíselnou hodnotu ve stejném
  floating formátu a výslovně odkazuje na zaokrouhlování §4. §4 zahrnuje
  signalizaci inexact při změně přesné hodnoty; §7.5 výslovně požaduje
  inexact, pokud zaokrouhlený výsledek není přesný. MMIX-doc:1120–1189
  přebírá IEEE/ANSI 754 a vysvětluje vlastní doplnění pro případy, které
  standard plně nedefinuje. Odstavec 1215–1238 výslovně zahrnuje integerizaci
  mezi sedm IEEE operací. Definice FINT:1332–1341 říká zaokrouhlení na
  floating integer a vylučuje O/U; nevylučuje X.
* **FIX:** IEEE §5.4 samostatně odkazuje převod floating→integer na §4,
  a tedy na stejné pravidlo X. MMIX-doc:1543–1555 navíc výslovně stanoví
  převod stejně jako u FINT a následný zbytek modulo 2^64. Pro konečné
  necelé binary64 je |z|<2^52; zaokrouhlené |n|≤2^52 se vejde do signed64.
  Na celém postiženém oboru proto nemůže zasáhnout zvláštní pravidlo W
  ani modular reduction. Speciální MMIX chování pro NaN/∞ je jiná větev.
* **FIXU:** MMIX-doc:1557–1560 stanoví shodu s FIX s jedinou výjimkou,
  potlačením W. Tato výjimka se X netýká. Předchozí argument pro konečné
  necelé vstupy tedy platí zvlášť i pro FIXU.

Další kontrolou je emulační úloha MMIX-doc:1409–1430: žádá ekvivalent FINT
včetně výjimek a její uvedený program pro z=1/2 při nearest vyvolá X při
FADD(2^52,1/2). Půlka leží přesně mezi 2^52 a 2^52+1, vybere se sudé
2^52; následné FSUB vrátí přesně nulu a předchozí X v rA zůstane.
V zadání je však u X napsáno **only if**, nikoli iff. Tento jednostranný
výrok nepřevracím: povinnost vyvolat X opírám o normativní řetězec výše,
emulaci používám jako další kontrolu zamýšlené ekvivalence.

MMIX-doc:1979–2026 definuje event X a čtyři režimy rA. U vypnutého
enable bitu se příslušný event nastaví. Jediná zde výslovná odchylka
O/X při zapnutém overflow tripu se integerizace netýká. Odpověď 54
v §1.3.1′ (file106/p98) upozorňuje, že úplná FP pravidla jsou uvedena
jinde; žádnou výjimku pro FINT/FIX nepřidává. Nepřebírám implicitně
novější IEEE operaci, která by směla inexact potlačit.

Primární [MMIX instrukční popis](https://mmix.cs.hm.edu/doc/instructions/farith.html)
má stejnou vazbu integerizace na sedm IEEE operací. Autorův
[distribuční a opravný přehled](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html)
byl znovu otevřen; tento problém v uvedených opravách není.

## 2. Nejkratší přípustný stav a přesná stopa

Zvolme rG=32, rL=0, rA=0 a globální registr
$254=#3fe0000000000000, tedy +1/2. Všechny arithmetic trips jsou vypnuty,
režim je nearest. Instrukce `FINT $253,0,$254` (#17fd00fe) musí vrátit
+0 a nastavit event X, tedy rA=1. Y=0 je platný a čte režim z rA.

`funpack` nastaví zt=num, zs='+', ze=1021, zf=2^54 a exceptions=0.
V `fintegerize` se posunuje o 1074−1021=53: xf=2. Zpětný posun je
přesný, takže sticky nic nepřidá. Nearest přičte 1, neboť xf&4=0;
vymazání spodních dvou bitů dá nulu. Přímý návrat sestaví +0 a nikde
nenastaví X. Skutečný výsledek má správné bity, **rA však zůstane 0**.

`FIX $253,0,$254` (#05fd00fe) má vrátit integer 0 se stejným eventem X.
`fixit` zavolá stejnou integerizaci a pak `funpack` její nuly. Toto druhé
rozbalení opět vymaže exceptions a vrátí se integer 0. U
`FIXU $253,0,$254` (#07fd00fe) dispatcher pouze odstraní W; X stále chybí.

Skutečný dispatcher `mmix-sim-20250620.w:2017–2033` převezme exceptions
bez dalšího zjišťování ztracených bitů; `2586–2592` při vypnutých tripech
zapisuje `exc>>8` do rA. Interní X_BIT=#100 odpovídá eventu #01.
Oba originály mají stejné relevantní větve. Jsou pokryta i X=Z aliasy:
vstupní z je načten před zápisem výsledku, funkce nemění zdrojový registr.
Pro svědka není potřeba paměť, handler ani další předpoklad OS.

## 3. Celý postižený obor a úplný důkaz auditní opravy

Číselné výsledky, přesné meze posunů, klasifikace všech 64bitových vzorů,
I/W podmínky a ukončení jsou již dokázány v `fp-conversions-recovery.md`,
§1 a §5–6. Zde se přebírá přesně jejich kontrakt
|z|=f·2^(e−1076), 2^54≤f<2^55, f dělitelné 4, se 32bitovými unsigned
tetra a platným režimem. Nejde o převzetí celé knihovny bez důkazu.

Ve FINT je pro e≥1074 každý konečný vstup celý a následné balení přesné.
Pro e≤1020 je 0<|z|<1/2 a xf=1 označuje necelou hodnotu. Ve zbývajícím
intervalu 1021≤e≤1073 je xf=J(4|z|), kde J zachová floor a nastaví
nejnižší bit pro nenulový ztracený zlomek. Při zápisu |z|=q+r, 0≤r<1,
mají dva spodní bity xf tyto disjunktní významy:

| r | xf&3 |
|---|---:|
| 0 | 0 |
| 0<r<1/2 | 1 |
| r=1/2 | 2 |
| 1/2<r<1 | 3 |

Proto test `xf.l&3` **před** zaokrouhlením detekuje právě konečné necelé
vstupy, nezávisle na znaménku a režimu. U každého takového vstupu se
musí číselná hodnota změnit. Původní kód tyto bity později vymaže a
balí již přesný integer; žádná pozdější cesta proto chybějící X nedoplní.

Auditní `sources/audit-integerization-inexact.ch` před switch(r) přidává
`if (xf.l&3) exceptions|=X_BIT;`. Není změněn žádný bit výsledku ani
žádná větev zaokrouhlování. Konečné celočíselné vstupy ponechají X=0;
nuly, infinity a obě NaN třídy se k novému testu vůbec nedostanou.
Jejich dříve dokázané I chování se nemění. Tento důkaz platí pro všechny
čtyři režimy a Y=0, včetně nejmenších subnormálů a záporné nuly vzniklé
zaokrouhlením. Žádný nový posun ani aritmetické přetečení nevzniká.

**Samostatná povinnost FIX:** pouhé doplnění FINT nestačí, protože druhý
funpack exceptions nuluje. Oprava proto nejprve vyhodnotí fintegerize,
uschová jeho exceptions, rozbalí výsledek a obnoví uschované exceptions
**před** testem zt==zro. U konečného vstupu z této části může integerizace
vrátit pouze přesný floating integer, včetně ±0; funpack sám nikdy
nezvedá příznaky. Obnovení tedy nezahodí žádný nový event. Pokryta je
zvlášť časná větev, kdy nenulový vstup zaokrouhlením zanikne na nulu.

Další převod na integer modulo 2^64 mění jen číselnou reprezentaci
dříve vybraného n. Pro původně necelý z máme |n|≤2^52, takže W nenastane
a X zůstane jediným příznakem. Pro původně celé z je uložené X nulové;
všechny původní W větve se chovají shodně. NaN/∞ vracejí původní bity
s I ještě před nově upravenou částí. FIXU pak odstraní pouze W a zachová
právě prokázané X/I. Tím jsou pokryty všechny třídy vstupů, všechny
časné návraty a všechna čtyři zaokrouhlení obou konverzí.

Oprava přidává konečný počet operací, žádnou smyčku. Již prokázané
normalizace a meze zůstávají. Deklarované instrukční náklady jsou 4υ
pro FINT/FIX/FIXU; počet C příkazů se za tento model nevydává.
Závěr o pozorovatelném eventu používá vypnuté trippy. Nedokazuje se
správnost libovolného uživatelského handleru ani celá implementace IEEE.

## 4. Originální sazba, opravy a omezená reprodukce

Originální digitální MMIX-ARITH strany 37 a 38, §§86–88, byly zobrazeny
v `images/mmix-arith-review-file037.png` a `038.png`. Chybějící test X
i druhý funpack souhlasí s oběma archivovanými zdroji. Fyzický výtisk
MMIXware nebyl kontrolován; známá odlišnost sazby s doplňkovým default
návratem se konečné číselné větve ani příznaku netýká.

`results/errata-S0004.json` obsahuje všech osm relevantních vrstev,
jejich hash a význam nalezených řádků. Zmínka o fint/fix v erratu
z 5. srpna 2000 pouze doplňuje instalaci rounding mode do pipeline;
nepřidává X ani jeho zachování. Jde o jinou opravu. Aktuální autorovy
sfpack/fplus opravy také řeší jiné větve. V těchto vrstvách není
nalezena odpovídající oprava; nejde o tvrzení světového prvenství.

Jediný běh `nice -n 15 python3 workstreams/vol1-fasc1/verify_integerization_inexact.py`
provedl 16 vybraných volání v každém ze dvou originálů a v samostatné
auditní opravě: **48 krátkých volání**, žádný simulátor ani enumeraci.
Očekávané hodnoty jsou přesné kódované půlky/celá čísla a přímo odvozené
I/W/X podmínky, bez hostitelského floating-point orákula. Každý originál
má osm shodných selhání pouze v X a osm úspěšných kontrol; auditní oprava
projde všech 16. Kontroly zahrnují všechny čtyři režimy, výběr rA,
zaniknutí na nulu, prostřední i časnou celočíselnou větev, subnormál,
NaN, signed64 hranici a samostatné odstranění W ve FIXU.
Výsledky a build log jsou v `results/integerization-inexact*.json`.
Příklady doplňují důkaz, nenahrazují jej. Staré běhy se neopakovaly.
