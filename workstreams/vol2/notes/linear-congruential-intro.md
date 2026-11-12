# §3.2.1: lineární kongruenční generátory

Kontrola 1. listopadu 2026. Text [str. 10](../images/vol2-p010.png) a
[11](../images/vol2-p011.png), všech pět úloh a [odpovědi str. 543](../images/vol2-p543.png).
Text §3.2 je krátký úvod na str. 10 a je zahrnut zde.

## Definice a textové vzorce

Nechť `m>=1` je celočíselný modul, `0<=a,c,X_0<m`; `a` je násobitel,
`c` přírůstek a `X_0` počátek. Zbytek `z mod m` volíme v `{0,...,m-1}`.
Generátor je `X_(n+1)=(a*X_n+c) mod m`. Příklad `m=10,a=7,c=7,X_0=7`
dává `7,6,9,0,7,...`; všechny čtyři přechody byly ověřeny.
Případy `a=0` a `a=1` jsou po řadě konstantní od prvního kroku a
`X_n=(X_0+n*c) mod m`. Při další práci kniha předpokládá `a>=2`
a zavádí `b=a-1`.

Označme `S_k=1+a+...+a^(k-1)` pro `k>=1` a `S_0=0`.
Indukce pomocí `S_(k+1)=a*S_k+1` dává

```text
X_(n+k) = (a^k*X_n+c*S_k) mod m.
```

Pro `a>=2` je `S_k=(a^k-1)/b` celé číslo. Dělení se provádí před
redukcí modulo `m`, ne inverzí `b` modulo `m`. Tím je dokázána rovnice (6)
i odpověď 4. Každý k-tý člen je tedy nový kongruenční generátor
s násobitelem `a^k mod m` a přírůstkem `c*S_k mod m`.

Pomocná posloupnost `Y_0=0, Y_(n+1)=(a*Y_n+1) mod m` splňuje
`Y_n=S_n (mod m)`. Protože `a^n=1+b*S_n`, dostáváme rovnici (8),
`X_n=(A*Y_n+X_0) mod m`, kde `A=(X_0*b+c) mod m`.
Nejde o tvrzení, že transformace pomocí `A` je nutně prostá.

Historické odkazy na Lehmera, Thomsona a Rotenberga jsou připsání
publikovaných návrhů, nikoli matematické tvrzení o první myslitelné
konstrukci. Bibliografické položky zkontrolovány v textu; priorita
nebyla nezávisle znovu historicky dokazována.

## Úlohy 1–3 a 5

1. Pro `m=10`, sudé `a,X_0` a liché `c` jsou všechny další členy liché;
   počáteční sudý stav se tedy nevrátí. Redukce modulo sudého `m`
   zachovává paritu.
2. Je-li `gcd(a,m)=1`, násobení `a` i přičítání `c` permutují zbytky.
   Každá trajektorie permutace konečné množiny je cyklická od počátku:
   z prvního opakování lze pomocí jednoznačné inverze odstranit stejně
   dlouhé počáteční úseky. První opakovaný stav proto musí být `X_0`.
3. Položme `d=gcd(a,m)`. Obraz přechodu je přesně množina zbytků
   kongruentních s `c` modulo `d`, velikosti `m/d`; po prvním kroku
   se jiné stavy nevyskytují. Pro `m=2^e`, `e>=1`, a sudé `a` je
   `a-1` liché a existuje jediný pevný bod `r=-c/(a-1) (mod 2^e)`.
   Zde zápis dělení značí násobení existující modulární inverzí.
   Rozdíl `X_n-r=a^n*(X_0-r) (mod 2^e)` je od `n=e` nulový.
   Posloupnost je tedy nakonec konstantní, jak tvrdí odpověď.
5. Pro jednotkové `a` zvolme celé `a'` s `a*a'=1 (mod m)`.
   Inverzní krok je `(a'*X_n-a'*c) mod m`; jeho opakování dává
   správný první řádek odpovědi. **Druhý řádek je chybný**, pokud
   není volba `a'` zpřísněna: [V2-C0004](C0004-inverse-lcg.md).
   Při `d>1` má každý dosažitelný stav přesně `d` předchůdců,
   lišících se o násobky `m/d`, a samotný stav předchůdce neurčuje.
   Jde o inverzi z hodnoty stavu, nikoli o nemožnost znovu vypočítat
   známou posloupnost od jejího zadaného počátku.

## Errata a kontroly

Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2`, `err2.textxt`
podle str. 10–11 a 543 a příslušných vzorců/úloh. Pět původních úloh,
žádná přidaná úloha v této sekci. Dodatek z 24. 1. 2003 doplňuje
`b=a-1` do odpovědi 5; doložen přímo [na str. 30 historických errat](../images/all2-prepre-p30-direct.png).
Upřesnění odpovědi 3 z 23. 12. 2024 přidává „modulo m“; výše je zapracováno.

[Validátor](../verify_lcg_intro.py) používá přímou iteraci a přesnou
celočíselnou/racionální aritmetiku. Pro `m<=20` projde všechny `a,c,X_0`,
dopředné skoky `0<=k<=6`, obrazy přechodu, cykličnost jednotkových
násobitelů a obě správné inverzní formulace. Pro `m=2^e`, `1<=e<=7`,
navíc všechny sudé násobitele a přírůstky, čtyři reprezentativní počátky.
Výpočty doplňují obecné důkazy; [výsledky](../results/lcg-intro.json).
