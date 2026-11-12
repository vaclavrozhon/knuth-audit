# MMIX-S0001 — fepscomp ztrácí horní zaokrouhlení při d>54

Stav: **confirmed, companion_program, medium**. Nejde o novou knižní chybu
fasciklu. Doloženo v nezměněném MMIXware 1.0 z 17. 10. 2013 i v autorově
opravované distribuci z 20. 6. 2025. Počty knižních nálezů se nemění.

## Rozpor za platných předpokladů

Zvolme normální konečné hodnoty

```text
y = 1,        bits #3ff0000000000000
z = −2^−55,   bits #bc80000000000000
ε = 1/2,      bits #3fe0000000000000.
```

Architektonická definice v `mmix-doc-20131017.w:1440–1487` dává
poloměry R(y)=1 a R(z)=2^−55. Přesný rozdíl `1+2^−55` překračuje oba,
proto y není podobné z a `FCMPE` má vrátit **+1**. Nejsou přítomny NaN,
nekonečna, nuly, neplatné epsilon ani aritmetické výjimky.

`fepscomp` však při rozbalení získá

```text
yf = zf = ef = 2^54,
ye = 1022, ze = 967, ee = 1021, d = 55.
```

V §53 (řádek 958 obou uložených zdrojů; viz přesná lokace níže) provede
`if(d>54) o=zero_octa,oo=zf;`. Následující test `oo!=zf` je nepravdivý.
Opačná znaménka proto dají `o=yf+0=2^54`, a porovnání s `ef=2^54`
vrátí 1, tj. podobnost. Dispatcher simulátoru, ř. 2049–2055, z této
hodnoty vyrobí **FCMPE=0**. Jde o skutečný jiný výstup instrukce.

Také `FEQLE` je postiženo: při stejných y,z vezměme
ε=2^54, bits #4350000000000000. Menší poloměr je přesně 1, takže
`|y−z|=1+2^−55>1` a výstup musí být 0. Pro test ≈ kód odečte d od
exponentu epsilon; znovu dostane ee=1021 a vrátí **1**.

## Celá rodina, nikoli jen jeden běh

Pro `y=2^a`, `z=−2^b`, kde `−1022≤b<a≤1023` a `d=a−b≥55`, dává
ε=1/2 vždy nesprávnou podobnost. Skutečný rozdíl `2^a+2^b` je větší než
maximální poloměr 2^a. Všechny tři mantisy jsou 2^54 a dlouhý posun
vždy chybně ignoruje nenulový kladný zlomek. Záměna operandů obdobně
dává 0 místo −1. Pro `55≤d≤1024` je i ε=2^(d−1) konečné a tatáž
rodina dává chybný pozitivní výsledek FEQLE, protože minimální poloměr
je opět 2^a. Tato rodina splňuje všechny podmínky normálních operandů.

## Oprava a její dosah

Auditní `sources/audit-fepscomp-ceiling.ch` mění pouze pravou stranu
`oo=zf` na `oo=zero_octa`. Původní soubory zůstávají beze změn.
Pro d>54 a nenulové zf platí 0<zf/2^d<1, takže ztracený zbytek musí
být detekován. Při opačných znaménkách je nutné počítat `ceil(yf+zf/2^d)`
=yf+1; při stejných znaménkách je `ceil(yf−zf/2^d)=yf`.
Obecný invariant a úplný důkaz konečných větví včetně mezí posunů,
subnormálů, nul, výměny operandů a necelé tolerance je v
`notes/fp-comparisons-recovery.md`, oddíl 4. Konečná epsilon s nekonečny
v y,z mají samostatný úplný rozbor v oddílu 3.

## Reprodukce

`nice -n 15 python3 workstreams/vol1-fasc1/verify_fepscomp_boundary.py`
provede pouze osm cílených vstupů proti dvěma původním modulům a jedné
auditní opravě (celkem 24 běhů). CWEB se tangluje beze změn; není sestaven
ani spuštěn celý simulátor. Samostatný oracle používá Python Fraction
a přesné neighborhood poloměry, nikdy hostitelskou floating aritmetiku.

Každý původní modul má čtyři rozpory a čtyři souhlasné kontroly: d=54,
stejné znaménko a nejbližší větší ε hlídají právě určenou hranici. Opravený
modul souhlasí ve všech osmi. Obecnou opravu dokazuje oddíl 4 uvedené
poznámky, nikoli počet testů. Výstupy a příkazy jsou
`results/fepscomp-boundary.json`, `results/fepscomp-boundary-build.json`.

## Originál a všechny relevantní veřejné opravy

- Primární zdroje autora: [zmrazený archiv 2013](https://www-cs-faculty.stanford.edu/~knuth/programs/mmix-20131017.tgz)
  a [opravovaná distribuce 2025](https://www-cs-faculty.stanford.edu/~knuth/programs/mmix.tar.gz).
  Hash obou aritmetických souborů i archivů je v `sources/fp-primary-metadata.json`.
  §50–53 `fepscomp` je v obou beze změny.
- Primární sazba MMIX-ARITH, [p. 22 / §51–53](https://mmix.cs.hm.edu/doc/mmix-arith.pdf#page=22),
  stažena a vizuálně prohlédnuta: `sources/mmix-arith-upstream.pdf`,
  `images/mmix-arith-upstream-p22.png`. Obsahuje přesně `oo=zf`, nikoli
  chybu extrakce či přepisu. Původní fascikl p. 13 je správný kontext
  definice; není označen za chybnou stránku.
- [Historická errata MMIXware 1999–2014](https://www-cs-faculty.stanford.edu/~knuth/mmixware-errata.html)
  obsahují opravu nul v unsubnormalize (15. 3. 2006) a přírůstku
  `−1:1` na `0:1` (21. 6. 2003). Obě jsou v našich zdrojích zahrnuty;
  žádná neopravuje `oo=zf` v dlouhé větvi.
- [Současné opravy na autorově stránce](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html)
  mění mj. `fplus` z d>53 na d>54 a mez tininess v `sfpack`.
  Jde o jiné známé vady, které se jako naše nálezy nezapočítávají.
- [Seznam chyb správce MMIX](https://mmix.cs.hm.edu/bugs/index.html),
  [aritmetická chyba z roku 2015](https://mmix.cs.hm.edu/bugs/bug_rounding.html)
  a [veřejný compiler-warning change file](https://mmix.cs.hm.edu/tools/warn/mmix-arith.ch)
  byly přečteny. Vada z roku 2015 se týká `fplus` §49, nikoli `fepscomp`
  §53, a její oprava je v distribuci 2025. Zdejší rozpor v nich uveden není.
- Fasciklové `errata/originals/err1f1.textxt`, `errata/text/err1f1.txt`
  a `errata/text/all1f1.txt` byly prohledány věcně i podle p. 12–13.
  Relevantní epsilon oprava pro tento kód nalezena nebyla.

Kontrola proběhla 6. 11. 2026. Závěr potvrzuje rozpor v přesně uložených
distribucích; netvrdí historické prvenství a není výsledkem úplného auditu
všech komunitních větví. Fyzický výtisk MMIXware nebyl ověřen. Nic nebylo
odesláno, žádný emailový návrh nevznikl.
