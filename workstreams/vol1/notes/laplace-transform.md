# §1.2.9-13: obor Laplaceovy transformace a V1-C0011

Audit 1. listopadu 2026. Zadání s. 94 (strana souboru 109),
odpověď s. 497 (512) a originální stránka 6 obou errat `all1`
a `err1` byly zobrazeny. Konvergentní generující funkce v definici
na s. 87 znamená mocninnou řadu s kladným poloměrem konvergence;
neznamená konvergenci na celém jednotkovém kruhu.

Pro koeficienty a_k zadání definuje kumulativní funkci
`f(t)=sum_{0<=k<=t} a_k` a její Laplaceovu transformaci
`Lf(s)=integral_0^infinity exp(-st) f(t) dt`. Odpověď je

```text
Lf(s)=G(exp(-s))/s,    G(z)=sum_{k>=0} a_k z^k.          (L1)
```

Dodatek z 1. ledna 2024 předpokládá kladnou reálnou část s
a tvrdí, že tím je zajištěna existence integrálu. To neplatí.

## Přesný protipříklad

Položme `a_k=2^k`. Pak `G(z)=1/(1-2z)` jako mocninná řada
pro |z|<1/2; například z=1/4 splňuje knižní definici konvergence.
Vezměme reálné `s=ln 2>0`. Pro celé n>=0 a n<=t<n+1 platí
`f(t)=2^(n+1)-1`, takže

```text
integral_n^(n+1) 2^(-t) f(t) dt
   = (1-2^(-n-1))/ln 2 >= 1/(2 ln 2).                  (L2)

integral_0^N 2^(-t) f(t) dt
   = (N-1+2^(-N))/ln 2 -> infinity.                   (L3)
```

Přidaná podmínka tedy nezaručuje existenci integrálu. Ani
pravá strana (L1) není v tomto bodě definována: exp(-s)=1/2
leží na pólu G. Nejde o jemnost podmíněné konvergence.

## Dostačující oprava a obecný důkaz

Nechť R>0 je poloměr konvergence G, tedy mez otevřeného kruhu,
v němž řada konverguje absolutně. Stačí předpokládat

```text
sigma=Re(s)>0,    exp(-sigma)<R.                       (L4)
```

Jednoduché slovní znění je „Re(s) sufficiently large“.
Pro R=infinity druhá podmínka neomezuje sigma. Za (L4) je

```text
sum_{k>=0} integral_k^infinity |a_k exp(-st)| dt
 = (1/sigma) sum_{k>=0} |a_k| exp(-sigma k) < infinity.
```

Absolutní integrabilita dovoluje zaměnit integrál a součet
indikátorů [t>=k]. Každý jednotlivý integrál je exp(-sk)/s,
čímž vznikne (L1). Podmínka je dostačující; netvrdíme její
nutnost pro každý zvláštní výběr koeficientů.

## Errata a rozsah nálezu

Prohledány byly `all1-prepre`, `all1-pre`, `all1`, `err1`
a zdroj `err1.textxt` podle strany, Laplaceova názvu a znění
podmínky. Zdrojový TeX obsahuje dodatek na řádcích 458–459.
Aktuální PDF i jejich původní obrazy potvrzují stejné znění;
další podmínka růstu nebo poloměru konvergence nalezena nebyla.
Čerstvost a shodu všech pěti zdrojů dokládá
`sources/errata-refresh-2026-11-01.json`.

**V1-C0011 je confirmed:** doložený nedostatek podmínky
v publikovaném dodatku. Jeho prvenství není stanoveno,
tištěný exemplář nebyl ověřen a nic nebylo odesláno.
Výpočet (L2)–(L3) je přesný důkaz; numerický test není potřebný.
