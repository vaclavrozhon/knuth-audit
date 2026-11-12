# V2-C0189: prohozené koeficienty při přesné dělitelnosti

**confirmed**, odpověď na §4.6.1–3, strana 672; zadání 435.

Zadání požaduje `u(x)*V(x)+U(x)*v(x)=gcd(u,v)`. Odpověď v případě
`d=min(m,n)=n`, kde m,n jsou stupně vstupů a d stupeň jejich gcd,
uvádí U=0, V=1. Toto dosadí na levou stranu u, ačkoli gcd je v
(až na normalizaci jednotkou).

Stačí u=x², v=x. Všechny polynomy jsou monické a m=2,n=d=1.
Vytištěné koeficienty dávají x², ale požadovaný výsledek je x.
Správně jsou U=1, V=0. Obecně pro monický gcd je U=1/leading(v),
V=0. Pokud se vrací libovolný nenormalizovaný gcd reprezentovaný
polynomem v, stačí U=1.

Při přenosu algoritmu 4.5.2X na obecné těleso je třeba také normalizovat
poslední nenulový zbytek a oba Bézoutovy koeficienty stejnou inverzí
vedoucího koeficientu, má-li být gcd monický podle konvence strany 425.
Samotná změna normalizace však prohození U,V neopraví; náš protipříklad
je už monický. Přesná validace je v `results/polynomial-division.json`.

## Podklady a rozsah

Kontrola 4. listopadu 2026. Sazba 3. vydání, 1. dotisku (1997) byla
vizuálně přečtena; strana souboru je tištěná strana plus 12. Všech pět
vrstev errat (`all2-prepre`, `all2-pre`, `all2`, `err2`, `err2.textxt`)
bylo prohledáno podle stránek i matematických výrazů; relevantní oprava
nebyla nalezena. Log je `sources/polynomial-division-basic-errata.txt`.
Nejnovější fyzický dotisk ani historické prvenství nálezu nejsou ověřeny.
Žádné hlášení nebylo odesláno.
