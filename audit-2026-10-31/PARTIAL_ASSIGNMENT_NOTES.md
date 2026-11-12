# Stabilní částečná ohodnocení a jednotkové klauzule: SAT 362–365

Kontrola 31. 10. 2026. F046 se týká ochrany před nedefinovaným polem
v Algorithm S; F047 konstrukce Hornových klauzulí; F048 chybějící
hvězdičky. Hlavní věty o stabilních ohodnoceních a vahách platí.

## F046: kontrolu nulových flexibilit lze přeskočit

Algorithm S na str. 277 (autorův PS str. 93) dovoluje libovolné
neprázdné klauzule. Vezměme `(x)∧(¬x)` a počáteční obě zprávy 1/2,
výchozí N₀=5 a ε=0.01. Posilující zprávy zůstávají nula.

| Průchod | i | π_x,π_(¬x) v S5 | Nové jednotkové zprávy v S6 | δ | Další krok |
|---|---|---|---|---|---|
| první | 0 | 1/2,1/2 | 1,1 | 1/2 | návrat do S2 s i=1 |
| druhý | 1 | 0,0 | 1,1 | 0 | S8 |

S3, kde je jediná kontrola π_l=π_(¬l)=0, se v obou průchodech
přeskočí kvůli i<N₀. V S8 je pole podle (155) nedefinované: všechny
jeho složky mají tvar 0/0. Jednotkové zprávy v S6 jsou prázdné
součiny rovné 1 i při správném použití konvencí z359.

Tento jev není omezen na jediný náhodný bod: pokud alespoň jedna
počáteční zpráva nepřevyšuje 0.99, první δ≥0.01 a následující
průchod skončí přesně takto. Kontrola 400 počátečních dvojic
potvrzuje tutéž větev; obecný argument pokrývá celý uvedený obor.

Oprava je přidat kontrolu obou nulových flexibilit ihned po S5,
před S6 a případným přechodem do S8. Jinou možností je výslovně
předzpracovat jednotkové klauzule před spuštěním Algorithm S.

Související popis odpovědi362 na str.619 také nekontroluje rozpor
v počátečním seznamu L a při zkrácení klauzule kontroluje pouze
délku 1. Pro L=[x,¬x] nechá vzniklou prázdnou klauzuli bez
ohlášeného rozporu. Zde je vhodné doplnit kontrolu počátečních
protikladů a prázdných klauzulí. Nevedeme to jako druhý nález
na témže jednotkovém protipříkladu.

## F047: konstrukce363(g) vytváří samé tautologie

Odpověď363(g), str.620 (PS256), uvažuje `L=L′\{l}`,
L′∈ℒ a L∉ℒ, ale vytváří klauzuli

`x_l ∨ ⋁_(k∈L′) ¬x_k`.

Protože l∈L′, obsahuje zároveň x_l i ¬x_l. Správně musí negativní
část běžet přes **L**, tedy přes L′\{l}.

Například rodina `ℒ={∅,{1},{1,2}}` splňuje všechny podmínky.
Jediný zakázaný krok z rodiny je `{1,2}→{2}`. Tisk vytvoří
`x₁∨¬x₁∨¬x₂`, což nic nevylučuje. Po vypuštění tautologie je
i {2} dosažitelné pod {1,2}, v rozporu se zadáním. Opravená
klauzule `x₁∨¬x₂` dává přesně požadovanou rodinu.

Známé erratum z 10. 2. 2024 mění v **zadání** „strict Horn clauses“
na „definite Horn clauses“. Index v odpovědi neopravuje. Tuto
známou změnu vedeme samostatně jako E004, ne jako nový nález.

## Proč opravená Hornova konstrukce funguje

Vytvořme opravenou klauzuli pro každý krok z člena L′ rodiny do
nečlena L=L′\{l}. Každý člen S rodiny je stabilní: jediná možnost
nepravdivé jednotkové klauzule při pozitivním částečném ohodnocení
by vyžadovala L⊆S a l∉S. Potom by ale S∩L′=L patřilo do rodiny
uzavřené na průnik, spor. Úplně nepravdivá klauzule nevznikne,
protože její pozitivní literál může být jen pravdivý nebo neurčený.

Všechny členy rodiny lze spojit s plnou množinou povolenou cestou
ze zadání, takže jsou dosažitelné přes stabilní stavy. Naopak první
krok cesty, který by opustil rodinu, má právě svou zakazující
klauzuli a vytvořil by jednotku. Dosažitelná rodina je tedy přesně ℒ.
Úplný výčet ověřil všechny takové rodiny do čtyř prvků: počty
**2, 6, 35, 596**.

## F048: prázdné ohodnocení364(c) má čtyři pozice

Odpověď364(c) na str.620 (PS256) píše `***`, ale soustava R′ z(7)
má čtyři proměnné. Má být `****`. Úplný výčet všech 81 částečných
ohodnocení potvrzuje, že právě toto je jediný covering i jediný core.
Obě řešení 0101 a 0111 mají váhu q₃, jak uvádí kniha správně.
Jde pouze o počet znaků v zápisu, ne o chybu klasifikace.

##363(a–f): základní definice a příklady

V C5 je trail stabilní: C2 do něj přejde až při G=F, kdy byly
zpracovány všechny vynucené literály; C4 by případný rozpor odvedl
do C7. C1 navíc výslovně odmítá protikladné jednotky.

Proměnná v pravdivém literálu je omezená právě tehdy, když jejím
překlopením vznikne nepravdivá klauzule, nebo jejím odznačením
vznikne jednotka. To dokazuje 363(c)(i),(iii). Varianta (ii) neplatí:
pro klauzuli123 je10* stabilní a první proměnná neomezená, ale00*
je jednotkový stav. Příklady 363(b),(d),(f) souhlasí s výčtem.
Konkrétně F z(1) má jen dva stabilní stavy,001 a***. Příklad(f)
dává všech 12 požadovaných dosažitelných množin; {3} je stabilní,
ale z plného pozitivního ohodnocení není dosažitelné.

##363(h–j),364: průniky, jádra a váhy

Neomezená přiřazená proměnná zůstává neomezená po jakémkoli
dalším odznačení jiných proměnných: odznačení nemůže změnit neurčený
nebo pravdivý literál na nepravdivý. Proto dvě povolená odznačení
komutují, což dokazuje(h).

Máme-li cesty z L do S a T, projděme nejprve cestu do S a pak
cestu do T s vynecháním již odznačených literálů. Každý další krok
zůstává povolený v menším stavu. Dojdeme do S∩T, takže tato množina
je dosažitelná a stabilní. To dokazuje(i) i existenci jediného
nejmenšího stavu, jehož všechny přiřazené proměnné jsou omezené.
Je to jediné jádro pod daným úplným řešením. Sousední úplná
řešení mají společného stabilního předchůdce, tedy stejné jádro;
tím i každý souvislý cluster má jediné společné jádro.

Obrácený směr364(f)neplatí. Šest uvedených klauzulí zakazuje
právě šest čtyřbitových řetězců s váhou2. Zbylá řešení mají váhy
0,1,3,4 a tvoří dva clustery po pěti vrcholech. Všechna mají
prázdné jádro. To souhlasí s knihou.

Pro identitu vah363(j) lze dát nezávislý pravděpodobnostní důkaz.
Nejprve uvažujme úplné stabilní L. Každému přiřazenému literálu
předem dejme nezávislou minci: odstranění s pravděpodobností p_i,
ponechání s q_i. Opakovaně odstraňujme neomezené literály, jejichž
mince dovoluje odstranění. Komutace odznačení zaručuje, že konečný
stav nezávisí na pořadí. Dosažitelný stav S vznikne právě když:

- všechny odstraněné literály mají minci p_i;
- všechny neomezené ponechané literály mají minci q_i;
- mince omezených ponechaných literálů jsou libovolné.

Pravděpodobnost výsledku S je proto přesně W(S), takže součet
vah je 1. U původně částečného L mají již neurčené proměnné společný
faktor Πp_i; klauzule s takovými neurčenými proměnnými neomezují
žádné další odznačování pod stabilním L. Dostáváme celý vzorec(j).

##365: škálované covering assignments

Všech šest řešení waerden(3,3;8) má každou proměnnou omezenou.
Pro liché q a posun d zachovejme jejich hodnoty na pozicích
q,2q,…,8q minus d, ostatní nechme neurčené. Obsahuje-li trojčlenná
aritmetická posloupnost dvě přiřazené pozice, obsahuje i třetí:
u krajních pozic používáme lichost q, tedy q|2s⇒q|s. Rozsah
8q−d≤n<9q−d vylučuje další přiřazené pozice0 a9 mimo základní
osmici. Žádná jednotka ani nepravdivá klauzule proto nevznikne.
Klauzule omezující jednotlivé proměnné se přenesou ze základní
osmice, takže jde opravdu o covering, ne pouze stabilní stav.

Pro pevné liché q sjednocení rozsahů přes d pokrývá
[7q+1,9q−1]. Od q=9 se intervaly pro následující liché q překrývají,
takže pokryjí všechna n≥64. Tvrzení knihy n>63 je správné.
Přímý test zahrnul **1716** škálovaných ohodnocení pro q≤11.

## Rozsah a doklady

`check_partial_assignments.py` prověřil 4215 formulí, 163485 částečných
ohodnocení, 43525 symbolických identit vah, 560908 průniků, 36935
lokálních dvojic odznačení a 13202 dvojic sousedních řešení.
Váhy se porovnávají jako celé polynomy, ne jen pro několik čísel p_i.
Výčet všech rodin pro Hornovu konstrukci je samostatný.
`check_survey_guard.py` reprodukuje oba průchody Algorithm S a
prázdnou klauzuli z popisu362. Výsledky jsou v `results/`.

F046–F048 byly vizuálně porovnány s PDF i autorovým PS. Odpovídající
veřejné opravy nebyly nalezeny; známé přejmenování363(g) je odděleno.
Fyzický exemplář dosud nebyl ověřen. Samostatný `check_partial_table.py` porovnal všech 27 tištěných buněk
tabulky 363(e) s definicí vah; všechny souhlasí (`results/partial_table.json`).
