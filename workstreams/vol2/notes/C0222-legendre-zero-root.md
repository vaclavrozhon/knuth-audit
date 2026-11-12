# V2-C0222: historický popis vynechává faktor x

Stav: **confirmed**. §4.6.2, strana 449, první historický odstavec.
Původní sazba znovu zobrazena v `images/vol2-p449.png`.

Popis slibuje všechny lineární faktory beznásobného f modulo p,
začíná však `g=gcd(x^(p-1)-1,f)`. Pro p=3 a f=x dostáváme g=1.
Žádný další gcd s g nemůže najít faktor x. Pro netriviální vstup
f=x(x−1) je g=x−1 a ztrácí se stejný faktor.

Obecně 0 nikdy není kořenem x^(p−1)−1. Správně tedy jde o všechny
lineární faktory s nenulovým kořenem, nebo je třeba nejdříve odebrat x.
Algoritmus D používající x^p−x touto drobností netrpí. Tvrzení o tom,
co napsal sám Legendre, zde nevznášíme: originál nebyl přečten.

Všech šest vrstev errat prohledáno 4. listopadu 2026, včetně posunutých
stran druhého vydání a jmen. Log: `sources/factorization-history-errata.txt`.
Oprava pařížské citace na 449 je známá, doplnění nenulovosti nenalezeno.
Fyzický poslední dotisk a prvenství nejsou ověřeny. Nic neodesláno.
