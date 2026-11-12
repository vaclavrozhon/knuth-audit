# V2-C0248 — složené výběrové pravidlo zapomíná první výběr

6. listopadu 2026. **Confirmed / low**, §3.5, odpověď 32,
tištěná strana **597**, souborová **609**. Původní sazba byla nově
zobrazena v `images/vol2-p597.png`. Jde o chybu explicitního předpisu
pro složené pravidlo; správné tvrzení úlohy o uzavřenosti R5 platí.

Pravidlo R má funkce f_n, pravidlo R′ má funkce f′_k. Odpověď definuje
f″_n=1 právě tehdy, když R z minulosti x₀,…,xₙ₋₁ vybere
x_{r₁},…,x_{r_k} a f′_k(x_{r₁},…,x_{r_k})=1. Chybí podmínka,
že **R vůbec vybírá aktuální x_n**, tedy f_n(x₀,…,xₙ₋₁)=1.

## Protipříklad bez výpočtu

Nechť R vybírá právě sudé indexy, tedy f_n=[n je sudé], a R′ vybírá
všechny členy, tedy každé f′_k=1. Obě pravidla jsou totální a
vypočitatelná; R vybírá nekonečnou podposloupnost každého vstupu.

V okamžiku n=1 vybral R z minulosti právě x₀, takže k=1, r₁=0.
Všechny vytištěné podmínky odpovědi jsou splněny a f′_1(x₀)=1.
Tištěný předpis tedy dává **f″_1=1**. Skutečné složení nejprve R,
potom R′ aktuální x₁ nevybírá, neboť **f₁=0**. Rozpor je nezávislý
na hodnotách symbolů, a platí proto i pro vstup splňující R5.
Při tomto R′ tištěný předpis ve skutečnosti vybírá všechny indexy,
ačkoli složení má vybírat pouze sudé.

## Oprava a úplný rozsah důkazu

Správná definice je

```
f″_n(x₀,…,xₙ₋₁)
  = f_n(x₀,…,xₙ₋₁) · f′_k(x_{r₁},…,x_{r_k}).
```

Vybranou minulost vypočteme konečnou simulací R na prefixech délky
0,…,n−1. Pak spočteme obě totální booleovské funkce. Formule platí
i pro k=0 (prázdná vybraná minulost) a n=0; f′_0 je právě konstantní
pravidlo počátečního výběru. Výstup se zařadí právě tehdy, když
projde oběma výběry, takže složení je přesné a totálně vypočitatelné.

Je-li X R5 a XR nekonečné, každý nekonečný R′-výběr z XR je tedy
některý vypočitatelný výběr z X a má rovnoměrné četnosti. To dokazuje
R5 pro XR. Indukce četností slov a nekonečná distribuce pak platí
stejně jako v `selection-randomness.md`, oddíl 3. Ten již obsahoval
správnou podmínku „R a současně R′“, ale dosud ji nesrovnal s vadným
vytištěným předpisem. Nový obnovovací průchod tento rozdíl odkryl.

## Známé opravy

Prohledány a přečteny příslušné rozsahy všech čtyř vrstev
`errata/text/all2-prepre.txt`, `all2-pre.txt`, `all2.txt`, `err2.txt`
a aktuální `errata/originals/err2.textxt`, podle 597/598, odpovědi 32,
skládání a výběrových pravidel. Historická vrstva přechází od oprav
593/596 k 599; další od 591 k 608 a aktuální od 586 k 609. Oprava
tohoto předpisu nenalezena. Změna „answer 32“ na 610 se týká jiné
sekce, a známá oprava n≥k na 162 jen pravidla po slově délky k.

Nízký dopad odpovídá lokální chybě pomocné konstrukce s jednoduchou
opravou; hlavní uzavřenost R5 ani existence náhodných posloupností
nejsou vyvráceny. Poslední fyzický dotisk a prvenství nejsou ověřeny.
Žádný program, census ani email se nevytvářel.
