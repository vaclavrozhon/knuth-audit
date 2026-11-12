# V2-C0190: exponent při dělení zprava doleva

**candidate**, odpověď na §4.6.1–6, strana 673.

Kniha píše `u=v*q+x^(m−n)*r`, `deg(r)<n`, a popisuje souvislost
s Eukleidovým algoritmem nad obrácenými polynomy. Pro obvyklé dělení
zprava doleva, které postupně ruší m−n+1 nejnižších koeficientů, je
správný exponent m−n+1. Přesné odvození obrácením běžného dělení je
v `polynomial-division-basic.md`; 100 obecných případů prošlo validací.

Například u=1+x, v=1+2x má m=n=1. Obrácené polynomy x+1 a x+2
dávají podíl 1 a zbytek −1. Původní identita je tedy
`1+x=(1+2x)*1+x*(-1)`. S vytištěným exponentem nula neplatí.

Důvod ponechání kandidáta: vytištěnou rovnici samotnou lze splnit
jiným podílem; v uvedeném příkladu q=1/2,r=1/2. Obecně lze zrušit
m−n dolních koeficientů a zvlášť nejvyšší koeficient. To dává jinou
platnou redukci gcd, protože x je nesoudělné s v při v(0)≠0.
Proto zde netvrdíme, že rovnice nemá řešení nebo že každý algoritmus
podle ní selže. Podezření se týká její identifikace s obvyklým
obráceným Eukleidovým dělením. Bez upřesnění zamýšlené varianty není
zařazeno mezi potvrzené chyby a není připraveno hlášení.

## Podklady a rozsah

Kontrola 4. listopadu 2026. Sazba 3. vydání, 1. dotisku (1997) byla
vizuálně přečtena; strana souboru je tištěná strana plus 12. Všech pět
vrstev errat (`all2-prepre`, `all2-pre`, `all2`, `err2`, `err2.textxt`)
bylo prohledáno podle stránek i matematických výrazů; relevantní oprava
nebyla nalezena. Log je `sources/polynomial-division-basic-errata.txt`.
Nejnovější fyzický dotisk ani historické prvenství nálezu nejsou ověřeny.
Žádné hlášení nebylo odesláno.
