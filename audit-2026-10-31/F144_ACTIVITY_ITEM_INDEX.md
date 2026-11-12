# F144: čtyřcestná větev je 03 nebo 05, nikoli 04

3. listopadu 2026; confirmed, nízká závažnost. Odpověď §7.2.2.1–207(c),
str.472, druhý odstavec; autorský Fascicle 5c, str.176. Fyzický výtisk
ani prvenství neověřeny.

Po volbě ‘00 01’ v problému (92) zůstává v první komponentě právě
těchto šest možností; první nulu pro čitelnost vynecháváme:

    234, 2345, 245, 34, 35, 45.

Stupně položek 02,03,04,05 jsou tedy **3,4,5,4**. Odpověď přesto
uvádí čtyřcestnou větev na04 (nebo05). Správně má být **03 (nebo05)**.
Všechny tři položky03,04,05 mají v tomto okamžiku aktivitu1.

Chyba ovlivňuje i uvedenou nerovnost: pro μ=5/4 a např.ρ=1/2 je

    score(04)=1+5/(1+5/4)=29/9 > 3,
    score(03)=score(05)=1+4/(1+5/4)=25/9 < 3.

Nedotčená dvoucestná komponenta má skóre3. Položka04 tedy nesplňuje
tvrzenou preferenci pro všechna μ>1; potřebuje μ>3/2. Oprava04→03
zachovává uvedenou podmínku μ>1 i smysl odstavce. Samotná heuristika
definovaná v zadání se nemění.

Zdroje byly zobrazeny přímo:
[možnosti v knize](images/focus202-207-original-124.png),
[odpověď v knize](images/focus202-207-original-492.png),
[možnosti v draftu](images/focus202-207-draft-46.png),
[odpověď v draftu](images/focus202-207-draft-182.png).
Obě verze mají04. Přesný seznam zbylých možností a zlomky jsou v
[nové kontrole](results/focus202_207/source-checked.json).
Šest vrstev errat bez odpovídající opravy. Známá změna207(d) z roku2020
se týká výkonnostních čísel a je oddělená jako E094.

[Úplné poznámky](FOCUS202_207_SOURCE_NOTES.md).
