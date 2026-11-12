# MMIX-S0002 — directed overflow vrací nekonečno místo konečné meze

Stav: **confirmed, companion_program, medium**. Jde o původní
`fpack`/`sfpack` v MMIXware 1.0 (17. 10. 2013) a v autorově opravené
distribuci z 20. 6. 2025. Není to nová chyba souhrnné knižní definice
ani tvrzení o libovolném zapnutém handleru.

## Platný kontrakt, nikoli samotná citace IEEE

Před reprodukcí byla uložena `notes/fp-overflow-contract.md`. Dokument
MMIX přímo přenáší standardní rounding konvence na STSF (ř. 1517–1527),
určuje OFF jako směr k nule a vymezuje enable/event chování rA.
Při vypnutých tripech specifikace neudává jinou defaultní číselnou
hodnotu O než převzatý IEEE/ANSI 754-1985 §7.3. Výslovná MMIX odchylka
O+X i při zapnutém O mění příznaky, nikoli OFF na NEAR.

Tento normativní řetězec má výslovnou externí IEEE závislost. Jeho
předpoklad je **všech osm enable bitů vypnuto**, platné rA, přístupná
paměť, běžná uživatelská instrukce. Při zapnutém O/X může handler
výsledek změnit; tento případ není svědkem ani oborem zdejší opravy.

## Přesný svědek STSF

Nechť rG=32 a globální $253 obsahuje `#47f0000000000000` = 2^128;
$254=#1000 je povolená zarovnaná adresa. rA=#10000 znamená ROUND_OFF,
bez zapnutých tripů a bez předchozích eventů. Instrukce

```text
STSF $253,$254,0
```

musí uložit `#7f7fffff`, tj. 2^128−2^104, největší konečný binary32,
a nastavit O|X, takže rA=#10009. Kladné nekonečno by neleželo ve směru
k nule od konečného 2^128.

Původní program ale provede přesně:

```text
funpack:  f=2^54, e=1150 (#47e), s='+'
sfpack:   e>#47d, proto e=#47f a o=0
OFF:      o se nemění
packing:  o = (#47f−#380)<<23 = #7f800000
flags:    O_BIT|X_BIT = #900
return:   +infinity
```

Dispatcher STSF tento tetrabyte přímo uloží. Krok logování výjimek
jen zapíše #09 do eventů rA, žádné další zaokrouhlení ani saturace
nenásleduje. Výstupní paměťové slovo je tedy skutečně jiné, při stejných
správně rozpoznaných příznacích.

## Celá rodina a druhá přesnost

Stejný průchod platí pro každý binary64 vstup ±2^k, 128≤k≤1023, uložený
jako short. Pro OFF obou znamének, UP záporných a DOWN kladných musí
nastat konečná saturace; starý packer dá infinity. Ostatní dvě směrové
kombinace i NEAR dávají infinity správně.

fpack má totožný problém s mezí #7fd. Pro FMUL(2^1023,2) je přesný
výsledek 2^1024. Oba vstupy jsou normální konečná čísla. Rozbalené
mantisy jsou 2^54, exponenty 2045 a 1023. Násobení v §43 dá horní
polovinu 2^53 a nulovou dolní polovinu, tedy normalizací xf=2^54,
xe=2046. fpack pak nastaví e=2047,o=0 a vždy vrátí
`#7ff0000000000000`, zatímco OFF musí dát `#7fefffffffffffff`.
Záporný první operand s UP analogicky vyžaduje
`#ffefffffffffffff`, ale dostane −∞. Obecně tatáž větev postihuje
součiny mocnin 2^a·2^b pro normální konečné vstupy a a+b≥1024.

Pro tento svědek není zapotřebí předpokládat správnost všech vstupů
omult: konkrétní součin 2^54·2^63=2^117 má přesně uvedené dvě poloviny.
Úplný FMUL důkaz zůstává samostatnou povinností.

## Auditní oprava a úplný omezený důkaz

`sources/audit-directed-overflow.ch` ponechá O|X a při detekci O
nahradí neznaménkovou infinity největším konečným vzorem právě tehdy,
když r=OFF, nebo r=UP a s='−', nebo r=DOWN a s není '−'. Znaménko se
připojí původním kódem. Stejná volba je provedena pro obě přesnosti.

`notes/fp-conversions-recovery.md`, oddíly 1–2, dokazují všechny větve
packerů: guard/sticky invariant, ties-to-even, malé subnormály, posuny
a jejich meze, carry mantisy i velký exponent. Při O má původní
neznaménkový výstup vždy přesně vzor infinity. Tři uvedené podmínky
jsou přesně všechny případy vyžadující konečnou mez; jejich komplement
vyžaduje infinity. Proto je volba úplná. Ne-overflow větve se vůbec
nemění; příznaky O|X a podpis nuly/NaN cest se nepřepisují.

Důkaz neopravuje hypoteticky jiné chyby volajících aritmetických rutin
ani předávání výsledku při enabled traps. Původní zdroje zůstaly beze
změny; change file je samostatný auditní artefakt.

## Reprodukce a kontrolní případy

`nice -n 15 python3 workstreams/vol1-fasc1/verify_fp_conversion_boundary.py`
provedl 12 zvolených případů ve dvou původních modulech a v jedné
auditní opravě, celkem 36 krátkých volání. Pět svědků se neshoduje
v každém originálu: tři STSF a dva FMUL. Sedm kontrol souhlasí:
opačné directed směry, NEAR, největší konečný short a tři hranice
celočíselných/short konverzí. Auditní oprava souhlasí ve všech 12.
Žádný simulátor nebo plošný test nebyl spuštěn. Očekávané bity jsou
odvozeny přesnými mocninami dvou; nepoužívá se hostitelský float.

Výstupy: `results/fp-conversion-boundary.json` a build log stejného
jména s příponou `-build.json`. Obecný závěr stojí na důkazu, ne na
počtu úspěšných kontrol. Dřívější fepscomp běhy se neopakovaly.

## Originál a vrstvy veřejných oprav

- Autorské zdroje 2013 a 2025: hash a URL v
  `sources/fp-primary-metadata.json`; příslušné větve fpack/sfpack mají
  stejný overflow mechanismus. Architektonický dokument je bytově
  totožný v obou archivech.
- Původní elektronická sazba [MMIX-ARITH p. 12–14](https://mmix.cs.hm.edu/doc/mmix-arith.pdf#page=12)
  byla prohlédnuta: `images/mmix-arith-review-file012.png`, `...013.png`,
  `...014.png`. Obsahuje přímo uvedené clampy a samotné přidání O|X,
  nikoli saturaci. Není to extrakční chyba.
- [Historická errata MMIXware](https://www-cs-faculty.stanford.edu/~knuth/mmixware-errata.html)
  včetně všech aritmetických oprav a změn normativních FP/trip odstavců
  tuto větev neopravují. [Současná autorova stránka](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html)
  opravuje short tininess a fplus guard; obě známé opravy jsou odlišné.
- [Veřejný seznam chyb správce MMIX](https://mmix.cs.hm.edu/bugs/index.html),
  [podrobný rounding report](https://mmix.cs.hm.edu/bugs/bug_rounding.html)
  a compiler-warning change file neobsahují odpovídající saturaci.
  Report roku 2015 řeší odečítání s rozdílem exponentů 54.
- Všechny tři relevantní fasciklové vrstvy (původní err1f1 text,
  err1f1 a kumulativní all1f1) byly porovnány; výsledek s hashi je
  `results/errata-S0002.json`. Kniha nemá novou kartu ani error lokaci.

Kontrola 6. 11. 2026. Bez tvrzení historického prvenství, bez úplného
auditu všech komunitních větví a bez fyzického výtisku MMIXware.
Autorova politika zmrazené verze se respektuje uchováním originálů;
zde se eviduje rozpor programu s dokumentovaným kontraktem.
