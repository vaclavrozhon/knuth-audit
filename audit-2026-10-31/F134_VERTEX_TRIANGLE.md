# F134: pootočená dlaždice v třetím tetrahexu

**4B, strana 454, odpověď 7.2.2.1–140(c), třetí obrázek zleva.**
Stav: doloženo v našem PDF i původním autorově PostScriptu. Nízká závažnost.

Vpravo je trojúhelník směřující dolů, který má jeden bílý a dva růžové
vrcholy. V tisku je bílý vrchol napravo. Tam sousedí s růžovým vrcholem
jednobarevné dlaždice; dole se naopak jeho růžová dotýká bílé.

**Oprava: otočit tento dílek o 120° po směru hodinových ručiček.**
Bílý vrchol se přesune dolů a oba nesoulady zmizí. Všechny ostatní
dlaždice zůstávají na svém místě.

![Původní a opravený obrázek](images/vertices140-c3-repair.png)

[Zvětšený originál](images/vol4b-p454-c3-detail.png) ·
[celá původní stránka](images/vol4b-p454-vertices140.png) ·
[autorův draft, strana 158](images/fasc5c-p158-vertices140.png).

K rychlému ověření stačí Python 3 a standardní knihovna:

```bash
cd .
python3 audit-2026-10-31/verify_f134.py
```

Program má přímo v sobě přepis všech 24 dlaždic. Nečte výsledky hledání
ani jiné datové soubory. Kontroluje všech 24 typů, nesoulad na právě
dvou vrcholech a všech 48 možností otočení jediného dílku. Právě jedna
taková oprava funguje. Všech 72 přepsaných rohů bylo zvlášť porovnáno
s vektorovou kresbou PDF.

V souřadnicích certifikátu má chybný dílek buňku `(6,1,1)` a vrcholy
`(7,2), (6,2), (7,1)` v pořadí proti směru hodinových ručiček.
Barevné slovo `abb` se mění na `bba`, kde `a` je bílá a `b` růžová.
Nesoulady byly na `(7,2)` a `(7,1)`. Množina použitých dílků se nemění.

Původní PostScript `fasc5c.ps.gz` ze září 2019 obsahuje stejnou chybu.
Porovnání zahrnuje všech 504 rohů všech sedmi tetrahexů, ne pouze tento
výřez. Dva úplné nezávislé výčty potvrzují, že opravená kresba patří
mezi 48 podstatně různých řešení této desky. **Knižní počet 48 je správně.**

Čtyři oficiální soubory errat byly znovu staženy 2. listopadu 2026
v 19:14 UTC a shodují se s archivem. V šesti aktuálních a historických
vrstvách pro 4B a Fascicle 5 nebyla nalezena odpovídající oprava.
Nejde o potvrzení prvenství ani příslib odměny; fyzický výtisk nebyl ověřen.

Důkazy: [samostatný certifikát](results/vertices140/standalone-f134-checked.json),
[oprava a autorův originál](results/vertices140/repair-checked.json),
[úplné výčty](results/vertices140/counts-checked.json),
[kontrola errat](results/vertices140/errata-check.json).
