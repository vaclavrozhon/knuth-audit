# MMIX-C0003 — chybný popis rY při tripu NEG

**Confirmed, medium**, uzavřeno 6. 11. 2026 krátkou primární kontrolou
zmrazené specifikace/implementace MMIXware 1.0. Nejde o chybu architektury
nebo běžného výpočtu NEG; chybná je věta popisující stav viditelný handleru.

Tištěná p. 18 / file 26, §1.3.1′, odstavec „Whenever a trip occurs“.
Sazba `images/file-026-p018.png` říká pro nestorovací instrukci rY←$Y;
výjimku okamžité konstanty uvádí pouze u rZ. NEG $X,Y,$Z však jako první
operand používá konstantu Y, nikoli registr $Y.

Vezměme $1=123, s($2)=−2^63, rA=#4000 (enable V), a instrukci
`NEG $3,1,$2`. Matematický výsledek je 2^63+1, tedy přetečení signed64.
Doslovná věta knihy předpovídá rY=123, skutečný výsledek je **rY=1**.

## Rozhodný primární zdroj

[Knuthova stránka MMIXware](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html)
výslovně identifikuje zmrazenou verzi 1.0 s master software 17. 10. 2013.
Z jejího [oficiálního archivu](https://www-cs-faculty.stanford.edu/~knuth/programs/mmix-20131017.tgz)
jsou uloženy pouze mmix-sim.w a mmix-doc.w, nikoli sestavený simulátor.
Hash a datum v `sources/mmix-20131017-metadata.json`.

Krátký sémantický řetězec v `sources/mmix-sim-20131017.w`:

1. Řádek 1520 dává NEG flags #26, tedy bit #4 pro immediate Y.
2. Řádky 1738–1749 instalují `y.l=yy` při tomto bitu; ostatní části
   octabyte byly předtím nulovány v hlavní smyčce na řádku 1364.
3. Řádky 1930–1933 provedou `x=ominus(y,z)`, nastaví V při přetečení,
   ale operand y nemění.
4. Řádky 2602–2603 pro nestorovací instrukci nastaví `g[rY]=y`.

Proto konkrétní NEG jednoznačně uloží konstantu 1. Obecná dokumentace
`mmix-doc-20131017.w`, řádky 2090–2096, také mluví o skutečných operandech.
Nebyl sestaven ani spuštěn simulátor; přímá deterministická větev stačí.

Vlastní implementace v auditované knize s tím souhlasí: p. 83 řádky
198–200 nastavují y←Y, tabulka p. 88 dává NEG #26 a p. 122 řádek 533
ukládá y do rY. Tyto stránky byly již přečteny a příslušná sazba ověřena;
tentokrát se neopakoval celý průchod. Oprava má rozlišit skutečný operand
od číslem Y vybraného registru, zejména uvést immediate případ NEG.

Relevantní původní/historické i současné místní errata již prověřena
v `results/errata-first-32.json`; nové cílené doplnění a zdrojový rozsah
jsou v `results/errata-C0003-C0013.json`. Odpovídající oprava nenalezena.
