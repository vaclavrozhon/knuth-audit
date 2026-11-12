# V2-C0002: chybějící omezení parametrů detektoru cyklů

Stav: **confirmed**, 1. listopadu 2026. V prvním tisku třetího vydání,
§3.1, odpověď 7, str. 540, doplňující odstavec o algoritmu Sedgewicka,
Szymanského a Yaa připouští `m>=2, g>=1`, ale potřebuje také `g<m`.
Bez této podmínky nemusí provést ani jediné hledání v tabulce, a proto
nemusí odhalit ani konstantní posloupnost. To je hlavní potvrzená chyba.

V témže odstavci chybí ošetření počátku běhu ve vzorci pro `b` a při
univerzálním použití meze na počet vyhodnocení. Níže jsou odděleny od
hlavní chyby, aby oprava jedné nezakrývala ostatní.

## Autoritativní místo a značení

Zobrazena [celá str. 540](../images/vol2-p540.png) i
[detail dotčeného odstavce](../images/vol2-p540-ssy.png). Nejde o OCR artefakt.
Zde `m` označuje kapacitu tabulky, `g` celočíselný parametr určující
četnost prohledávání a `n>=1` index právě vypočteného členu `X_n`.
Kniha uvádí

```text
b = 2^ceil(log2(n/m)),
q = ceil(n/b)-1,
table = X_0, X_b, ..., X_(q*b),
search exactly when n mod (g*b) < b.
```

`ceil` je zaokrouhlení nahoru a `log2` logaritmus při základu dvě.
Pro srovnání použijeme smysluplnou počáteční hodnotu
`b=max(1,2^ceil(log2(n/m)))`; hlavní protipříklad pak nezávisí na
necelých indexech v původním vzorci.

## Protipříklad k samotnému ukončení

Zvolme `m=2, g=3`. Pro `n=1` je opravené `b=1`, takže podmínka hledání
`1 mod 3 < 1` neplatí. Pro všechna `n>=2` má celočíselná mocnina dvojky
`b` určující rozestup vlastnost

```text
b < n <= 2*b < 3*b.
```

Tedy `n mod (3*b)=n>b` a hledání se neprovádí nikdy. Můžeme vzít i
`X_n=0` pro všechna `n`; detektor se přesto nezastaví. Je to důkaz
nekonečného běhu pro celý rozsah indexů, nikoli závěr z konečného timeoutu.

Ani slabší oprava `g<=m` nestačí. Pro `m=g=2` se hledá pouze v časech
`n=2^r`, `r>=1`, kdy tabulka obsahuje indexy 0 a `n/2`. V čistém cyklu
délky 3, tedy `X_n=n mod 3`, není `X_n` roven žádnému z těchto dvou
uložených členů: ani `n`, ani `n/2` nejsou dělitelné třemi.
Správná citovaná oblast parametrů je `1<=g<m`.

## Dva související počáteční případy

1. Původní vzorec s `m=2,n=1` dává `b=1/2`, `q=1` a požaduje člen
   `X_(1/2)`. Posloupnost je indexována pouze nezápornými celými čísly.
   Oprava `b=max(1,2^ceil(log2(n/m)))` přesně odpovídá tabulce začínající
   rozestupem 1 a zdvojnásobující ho po zaplnění paměti.
2. Odstavec dále tvrdí, že `X_n` není vypočten, pokud neplatí
   `mu+lambda > m*n/(m+4*g+2)`. Zde `mu` je délka ocasu a `lambda`
   délka konečného cyklu. I po opravě `b` a při legálním `g<m` je třeba
   ošetřit krátké posloupnosti: pro `m=8,g=3,X_n=0` se první hledání
   koná při `n=3`. Tento člen se vypočte, ale `mu+lambda=1`, zatímco
   pravá strana je `24/22=12/11>1`.

Příčinou druhého problému je použití odhadu `b_N<=2*N/m`, kde
`N=mu+lambda` a `b_N` je rozestup v čase `N`. Pro počáteční režim platí
místo něj `b_N<=max(1,2*N/m)`. Z lemmatu 2 citovaného algoritmu plyne
bez této chyby mez

```text
n_stop < N+(2*g+1)*b_N,
b_N=max(1,2^ceil(log2(N/m))).
```

Knižní jednodušší mez tedy platí například za podmínky `N>=m/2`.
Asymptotický výsledek pro dlouhé posloupnosti tímto protipříkladem
zpochybněn není; vadí jeho neomezené použití při bezpečném online výstupu.

## Srovnání s původním článkem

[Sedgewick, Szymanski a Yao, SICOMP 11 (1982), 376–390](https://sedgewick.io/wp-content/themes/sedgewick/papers/1982Cycles.pdf)
na str. 379 výslovně požadují `1<=g<M`, kde jejich `M` je knižní `m`.
Obrázek 4 na str. 380 začíná při `b=1`. Článek byl stažen z autorova webu;
[kopie PDF](../sources/sedgewick-szymanski-yao-1982-cycles.pdf) a
[metadata](../sources/sedgewick-szymanski-yao-1982-cycles.metadata.json).
Jeho neomezeně napsané korolárium 2 také nevyjadřuje počáteční ořezání
mocniny dvojky na 1; vlastní pseudokód ho však provádí.

## Výpočetní kontrola

[verify_cycle_table.py](../verify_cycle_table.py) přepisuje obr. 4
s fyzickým odstraněním položek a nezávisle při každém kroku rekonstruuje
tabulku z jejího vzorce. Pro všech 67 584 kombinací
`2<=m<=12`, `1<=g<m`, `0<=mu<=31`, `1<=lambda<=32` souhlasily tabulky,
detekované kolize a opravená mez. Knižní jednodušší mez byla kontrolována
jen tam, kde `2*(mu+lambda)>=m`.

Skript dále reprodukuje oba neukončující se příklady do indexu 10 000
a konečný protipříklad `m=8,g=3`. Výše uvedené obecné argumenty dokazují
neukončení bez konečného omezení. Výsledek:
[cycle-table.json](../results/cycle-table.json).

## Errata a meze závěru

Prohledány všechny relevantní vrstvy `all2-prepre`, `all2-pre`, `all2`,
`err2` i aktuální `err2.textxt`, originály znovu stažené 1. 11. 2026.
Hledány stránky 539–541 i jména autorů a označení algoritmu. Změny na
str. 540 upravují značení Gosperovy funkce (25. 12. 2002) a formulaci
odpovědi 11 (9. 11. 2002); žádná nalezená položka neopravuje tento odstavec.

Potvrzení znamená chybu v našem zdroji a absenci opravy v kontrolovaných
veřejných erratech. Nový fyzický dotisk ani prvenství hlášení ověřeny nejsou.
[Anglický návrh](../reports/C0002-cycle-table-boundaries-draft.txt) nebyl odeslán.
