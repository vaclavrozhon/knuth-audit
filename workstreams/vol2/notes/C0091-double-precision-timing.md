# V2-C0091: změny času v odpovědích4.2.3-4/5

**Stav: confirmed, neodesláno.** Třetí vydání, první dotisk1997, str.618,
odpovědi4 a5. Programy a jejich přesnější varianty počítají zamýšlené hodnoty;
problém je v nepodmíněných údajích o změně celkového času.

Všechny relevantní původní strany248–252 a618 byly vizuálně přečteny.
Dne2.11.2026 prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` podle
stran246–253/617–619 a výrazů4.2.3/normalization/running time. Erratum
24.11.2012 správně mění v odpovědi5 řádek22 na23; tuto opravu používáme.
Údaje o čase se tam neopravují. Obě historické stránky errat byly zobrazeny.
Poslední fyzický dotisk, prvenství ani odměna ověřeny nejsou.

## Nejkratší protipříklad: přesný nulový součet

Při `u=-v != 0` se obě sčítání shodnou na přesné nule. Neproběhne přetečení
zlomkové části ani jediný normalizační posun. Přesnější varianta přidá
`JOV OFLO`, `DEC2 1`, `JNOV DNORM`, každý za1 jednotku času; ostatní změněné
instrukce mají stejné ceny. Rozdíl je tedy **+3**, kde odpověď5 uvádí **-3**.

Konkrétně pro `b=64` nebo100 a `Q=b^2/2` použijeme dvě normalizovaná čísla
s exponentemQ a zlomkem `+1/b`, resp. `-1/b`. Přímé počítání vykonaných
instrukcí dává60 a63 jednotek. Čas se měří v MIX jednotkách `u` z knihy;
symbolem `u` v předchozí větě o operandech bylo označeno vstupní číslo.

Není to pouze nulová výjimka. Pro velký operand `(Q,+.10000000)_b` a menší
`(Q-1,-.(b-1)(b-1)...(b-1))_b` vyjde původně nenulový zlomek s chybou
`b-1`, zatímco vylepšení zachová další číslici. Oba běhy mají8 posunů a časy
120 a123. Při jiné nenulové redukci, kdy se významný byte přesune přes hranici
rA/rX, je rozdíl-4: přestane se vykonávat i `JXNZ` na řádku42.

## Násobení může být celkově rychlejší

V odpovědi4 údaj1/2/3 jednotky správně popisuje změnu **před normalizací**.
Přesnější hodnota ale může potřebovat o jeden normalizační posun méně.

Například `b=100`, oba exponentyQ=5000, kladné zlomkové celočíselné části

```
U = 909090909090910,
V = 1099999999999999,
f_u = U/b^8, f_v = V/b^8.
```

Původní program vrátí `(Q-1,(b^8-1)/b^8)`; vylepšený `(Q,1/b)`.
Před vstupem do DNORM stojí vylepšení o2 jednotky více. Jeho normalizace však
vynechá jeden průchod řádky45–48, jehož cena je `2+1+2+1=6`.
Celkové časy jsou112 a108, tedy **-4**, místo kladného1/2/3.

## Doklady a oprava formulace

- [Původní odpovědi](../images/vol2-p618.png).
- [Přepis programů](../sources/double-precision.mix) a generátor variant
  v [ověřovači](../verify_double_precision.py).
- [Cílená kontrola](../verify_double_precision_edges.py) a
  [výstup](../results/double-precision-edges.json): registry před DNORM,
  úplné trasy a nezávislé sečtení cen podle četností typů instrukcí.
- [Nezávislý celočíselný model](../double_precision_model.py) ověřuje hodnoty
  výsledků bez simulace MIXu.

Navržená úprava: u odpovědi4 omezit časový údaj na fázi před DNORM. U odpovědi5
uvést, že před DNORM přibudou3 jednotky bez přetečení a7 při přetečení;
potom připočítat skutečnou změnu času normalizace. Typický ušetřený posun
stojí6, ale nulové výsledky a změna vstupní větve DNORM vyžadují zvláštní zacházení.
