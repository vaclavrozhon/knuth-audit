# V2-C0188: úloha 4.6.1–8 musí vyloučit konstantní polynomy

**confirmed**, zadání na straně 435, odpověď 673, definice 421–422.

Kniha definuje ireducibilní polynom jako prvočinitel v okruhu polynomů,
tedy zejména jako nejednotku. Výslovně počítá konstanty 2 a 3 mezi
ireducibilní faktory nad celými čísly, ale nikoli nad racionálními.
Úloha 8 přesto tvrdí přenos ireducibility ze Z[x] do Q[x] bez omezení.

Protipříklad je konstantní polynom u(x)=2. V Z[x] je ireducibilní:
ze součinu dvou nenulových polynomů stupně nula vyplývá, že oba jsou
konstantní, a celočíselný rozklad čísla 2 má faktor ±1. V Q[x] je však
2 jednotkou, protože má inverzi 1/2, a tedy není ireducibilní.
Stačí doplnit „nonconstant polynomial“.

Odpověď začíná tvrzením, že u je primitivní; to platí pro ireducibilní
nekonstantní u, nikoli pro konstantní prvočíslo. Její zobrazená rovnost
navíc musí respektovat znaménko: při konvenci kladného vedoucího
koeficientu primitivní části z 423 máme obecně
`u = ±pp((m*v)(n*w))`, nikoli vždy rovnost s kladným znaménkem.
Například u=−x−1, v=u, w=1, m=n=1 dává na pravé straně x+1.
To je vedlejší zpřesnění stejné odpovědi; není počítáno jako další nález.

Důkaz opraveného tvrzení je v `polynomial-division-basic.md`, úloha 8.
Pro tento konstantní protipříklad není potřebný výpočet.

## Podklady a rozsah

Kontrola 4. listopadu 2026. Sazba 3. vydání, 1. dotisku (1997) byla
vizuálně přečtena; strana souboru je tištěná strana plus 12. Všech pět
vrstev errat (`all2-prepre`, `all2-pre`, `all2`, `err2`, `err2.textxt`)
bylo prohledáno podle stránek i matematických výrazů; relevantní oprava
nebyla nalezena. Log je `sources/polynomial-division-basic-errata.txt`.
Nejnovější fyzický dotisk ani historické prvenství nálezu nejsou ověřeny.
Žádné hlášení nebylo odesláno.
