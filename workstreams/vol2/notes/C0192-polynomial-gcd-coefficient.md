# V2-C0192: chybný koeficient největšího společného dělitele

**dismissed — oprava posouzení 12. listopadu 2026.** Originál i nově
vykreslená strana 672 již mají správně `x³+3x²+4x+6`. Předchozí audit
chybně přečetl koeficient jako 2. Níže zůstává historický argument proti
nesprávně přepsanému polynomu; nedokládá chybu knihy.
Podrobnosti: [nová kontrola](../../../integration/2026-11-12-novelty-review/notes/vol2-c0192-dismissal.md).

Pracuje se modulo 7. Nechť
`u=3x^6+x^5+4x^4+4x^3+3x^2+4x+2` a v je polynom s obrácenými
koeficienty. Odpověď vypisuje správnou poslední nenulovou řádku
`(1,3,4,6)`, ale vzápětí uvede gcd `h=x^3+2x^2+4x+6`.
Správně je `g=x^3+3x^2+4x+6`.

Krátký přesný doklad modulo 7:

```text
u = (3x^3+2x^2+2x+2) h + (5x+4),
u = (3x^3+6x^2+2x+5) g,
v = (2x^3+5x^2+x+4) g,
g = (6x+3)u + 5x*v.
```

První rovnost ukazuje, že h není ani dělitelem u. Další tři společně
dokazují, že monický g je gcd, nezávisle na provedení Eukleidova
algoritmu. Viz `results/polynomial-division.json`.

První kontrolní běh se zastavil právě na nesouhlasu s vytištěným h;
po nahrazení očekávaného výsledku doloženým g byly zbylé bloky
dokončeny s `--resume`, bez opakování již úspěšného základního bloku.

## Podklady a rozsah

Kontrola 4. listopadu 2026. Sazba 3. vydání, 1. dotisku (1997) byla
vizuálně přečtena; strana souboru je tištěná strana plus 12. Všech pět
vrstev errat (`all2-prepre`, `all2-pre`, `all2`, `err2`, `err2.textxt`)
bylo prohledáno podle stránek i matematických výrazů; relevantní oprava
nebyla nalezena. Log je `sources/polynomial-division-basic-errata.txt`.
Nejnovější fyzický dotisk ani historické prvenství nálezu nejsou ověřeny.
Žádné hlášení nebylo odesláno.
