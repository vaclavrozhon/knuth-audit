# V2-C0003: chybějící minus v odpovědi §3.1-19

Stav: **confirmed**, 1. listopadu 2026. Chyba je v publikovaném doplňku
z 8. května 2005, `all2-prepre`, str. 30, nová odpověď ke str. 542.
První dotisk knihy z roku 1997 tuto odpověď ještě neobsahuje.

## Přesné tvrzení a rozpor

V modelu úlohy je `m` počet symbolů, `k>=1` pevný počet předchozích
symbolů určujících další symbol náhodně zvolenou funkcí a `lambda`
délka výsledného cyklu z rovnoměrného počátku. Doplněk tiskne

```text
Pr(lambda=1) = Theta(m^(k/2)).
```

Značení `Theta(h(m))` znamená, že pro všechna dost velká `m` je výraz
mezi dvěma kladnými konstantními násobky `h(m)`; konstanty mohou záviset
na pevném `k`. Proto by pravá strana rostla bez omezení, zatímco
pravděpodobnost je nejvýše 1. Chybí minus v exponentu: má být `-k/2`.

Nezávislá kontrola pro `k=1`: úloha 11 dává přesně
`Pr(lambda=1)=Q(m)/m`, kde `Q(m)` je očekávaný počet různých stavů
před prvním opakováním v rovnoměrném náhodném zobrazení na `m` bodech.
Odvození v [poznámce o náhodných zobrazeních](intro-random-maps.md) dává
`Q(m)~sqrt(pi*m/2)`, tedy řád `m^(-1/2)`.

## Prameny a errata

- [Přímé vykreslení původního PostScriptu, str. 30](../images/all2-prepre-p30-direct.png)
  ukazuje kladný exponent. Stejný výsledek byl předtím zobrazen z archivního
  PDF; nejde pouze o OCR. Originál [all2-prepre.ps.gz](../sources/all2-prepre.ps.gz)
  je zachycen v [manifestu z 1. 11. 2026](../sources/manifest-2026-11-01.json).
- R. Pemantle, [autorův preprint](https://arxiv.org/abs/math/0404103), §4,
  poslední odstavce: pravděpodobnost má řád `m^(-k/2)`. [Lokální PDF](../sources/pemantle-2004-k-ary-maps.pdf).
  Oprava znaménka nevyžaduje důvěru v všechny analytické kroky článku:
  kladný exponent je vyloučen již výše uvedenou elementární mezí.
- Všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a `err2.textxt`
  prohledány podle str. 542, úlohy 19, autora a vzorce dne 1. 11. 2026.
  Pozdější oprava tohoto exponentu nenalezena. Další položka str. 542
  se týká úlohy 21, nikoli tohoto vzorce.

Reprodukce dokladu: rozbalit originální gzip a předat Ghostscriptu
`-sDEVICE=png16m -r200 -dFirstPage=30 -dLastPage=30`.
Uložený obrázek vznikl přímo z tohoto vstupu, ne úpravou matematického textu.

Novější fyzický dotisk ani prvenství nálezu nejsou ověřeny.
[Anglický návrh](../reports/C0003-k-ary-exponent-draft.txt) nebyl odeslán.
