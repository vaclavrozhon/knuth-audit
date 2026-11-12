# V2-C0120 — znaménko jediného vstupu algoritmu C

Stav: **candidate**. §4.5.2, str. 341, C1 a obor algoritmu C.

Algoritmus uvádí celá čísla u_i a n>=1. Pro n=1,u_1=-1 nastaví d=-1,
k=0 a skončí s d=-1. Největší společný dělitel jediného čísla je jeho
absolutní hodnota, zde 1. Pro n>=2 s rutinou gcd nad celými čísly první
volání znaménko normalizuje. Změna C1 na d=|u_n| pokryje celý uvedený obor.

Materiální nejistota: předchozí odstavec výslovně zavedl nezáporné vstupy
pro jinou redukci n-argumentového gcd. Může být míněn jako společný
předpoklad i zde, ačkoli C jej neopakuje. Proto nejde o potvrzený nález.

Originál `images/vol2-p341.png` zobrazen. Čtyři vrstvy errat prohledány
2026-11-02 bez nalezené opravy. Přesný výpočet je v
`results/gcd-basic.json`, část counterexamples. Fyzický dotisk a priorita
neověřeny; hlášení nebylo napsáno ani odesláno.
