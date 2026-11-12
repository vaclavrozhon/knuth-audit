# V2-C0013: dva chybné indexy v odpovědi §3.2.2-36

**Confirmed, 1. listopadu 2026.** První tisk třetího vydání 1997,
str. 558, řádky 3–4 odpovědi 36. Obecný důkaz periody je správný po
opravě indexu v mezikroku; nejde o protipříklad hlavní věty.

Zde q_0=0, q_1=1, q_(n+1)=c*q_n+a*q_(n-1). Kniha tiskne

```
q_(2n+1)-a*q_(2n-1)
 = (q_(n+1)-a*q_(n-1))*(q_(n+1)+a*q_(n+1)).
```

Poslední q_(n+1) má být q_(n-1). Totéž chybné druhé q_(n+1)
je zopakováno v následující větě začínající „Since“.

Nejkratší příklad: a=1,c=2, tedy všechny předpoklady úlohy platí,
a q=(0,1,2,5,...). Pro n=1 je levá strana 5-1=4, zatímco tištěná
pravá strana (2-0)*(2+2)=8. Rozdíl přetrvá i modulo 8. Opravený
součin dává (2-0)*(2+0)=4.

Správná identita je rozklad rozdílu čtverců:
q_(2n+1)=q_(n+1)^2+a*q_n^2 a
q_(2n-1)=a*q_(n-1)^2+q_n^2. Odečtením dostaneme
q_(n+1)^2-a^2*q_(n-1)^2. Navazující dvouadický důkaz pak funguje;
[úplná kontrola](inversive-generators.md) jej uvádí včetně kratšího
vztahu A-B=(a+c-1)*q_n.

Sazba je jednoznačná v `images/vol2-p558.png` a věrném výřezu
`images/vol2-p558-inversive-detail.png`, oba vizuálně přečteny.
Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální TeX,
stažené 1. 11. 2026: podle str. 558, odpovědi 36 a inverzních generátorů.
Jediná relevantní změna na této straně je oprava jiného důkazu37
z 3. 2. 2005. Oprava tohoto indexu nenalezena.

`verify_inversive.py`, `results/inversive.json`: přesný protipříklad,
38400 obecných identit pro 25 dvojic koeficientů a n=1,...,512,
plus přímé periody a nezávislé maticové výpočty. Vše prošlo.
Poznámka: následující kongruence „Since“ je při vytištěném indexu
číselně také pravdivá; oprava druhého výskytu obnovuje zamýšlené
použití správného faktoru v indukci, nikoli nový nezávislý protipříklad.

Fyzický novější dotisk neověřen; dostupný digitální náhled nemá str. 558.
Návrh `reports/C0013-inversive-doubling-index-draft.txt` neodeslán.
Prvenství ani odměna se netvrdí.
