# V2-C0119 — znaménko rozdílu v trojkovém gcd

Stav: **confirmed**. §4.5.2-5, odpověď na str. 640; zadání na 353.
Zobrazeny oba originály. Popis nastaví t na u+v nebo u-v podle dělitelnosti
třemi, odstraní z t faktory 3 a výsledkem nahradí max(u,v).

Pro kladné vstupy (1,7), již bez faktorů 3, dává doslovný postup:

```text
(u,v)=(1,7):  t=1-7=-6 -> -2; nahrazení max dává (1,-2).
(u,v)=(1,-2): t=1-(-2)=3 -> 1; nahrazení max ponechá (1,-2).
```

Druhý krok se opakuje bez konce. Chyba tedy není pouze v závěrečném znaménku.
Stačí nahradit u-v výrazem |u-v|, případně výslovně zajistit u>=v před
každým odečtením. Vytištěná tabulka toto zjevně zamýšlí: při
u=13634,v=24140 píše kladné t=10506, opačné k doslovnému u-v.

S absolutní hodnotou zůstávají vstupy kladné, gcd se zachovává a maximum
při nahrazení klesá. Úplný důkaz i kontrola příkladu jsou v `gcd-basic.md`;
samostatný záznam cyklu je v `results/gcd-basic.json`.

Čtyři vrstvy errat (`all2-prepre`, `all2-pre`, `all2`, `err2`) prohledány
2026-11-02 podle stran, úlohy a obsahu; odpovídající oprava nenalezena.
Aktuální fyzický dotisk a prvenství neověřeny, návrh neodeslán.
