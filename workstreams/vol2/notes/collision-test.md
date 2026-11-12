# §3.3.2 I: kolizní test a algoritmus S

Uzavřeno1.11.2026. Str.70–71 přečteny v původní sazbě. Hlavní
distribuce, střední hodnota a sedm tabulkových hodnot jsou správné.
Numerickou ochranu ukončení řeší samostatně
[C0021](C0021-collision-sentinel.md).

## Distribuce a rekurence

Rozhazujeme n nezávislých míčků do m stejně pravděpodobných uren.
J je počet obsazených uren; počet kolizí je C=n−J, protože každá
obsazená urna má právě jeden první zásah. Zápis {n\j} označuje
Stirlingovo číslo druhého druhu, počet rozkladů n označených míčků
do j neprázdných neoznačených skupin. Přiřazením skupin různým
urnám dostáváme

```text
Pr(J=j) = m(m−1)...(m−j+1) {n\j} / m^n.
```

Každá urna zůstane prázdná s pravděpodobností(1−1/m)^n, a tedy
E C=n−m+m(1−1/m)^n. Po i míčcích označme a_i(j)=Pr(J_i=j).
Další míček buď zasáhne některou z j obsazených uren, nebo přidá
novou urnu k dosavadním j−1. Proto

```text
a_(i+1)(j) = (j/m)a_i(j) + (1−(j−1)/m)a_i(j−1).
```

Aktualizace v sestupném pořadí zachová obě staré hodnoty; to je S2.
Pro p=Pr(J<=j) je 1−p=Pr(J>j)=Pr(C<=n−j−1), takže index n−j−1
v S3 je správný. Nulování malých položek je numerická aproximace,
nikoli přesná rovnost distribucí.

## Nezávislý certifikát tabulky

Pro výpočet použijeme místo J počet kolizí. Označme b_i(c)=Pr(C_i=c).
Jeho rekurence je

```text
b_(i+1)(c) = ((m−i+c)/m)b_i(c) + ((i−c+1)/m)b_i(c−1).
```

Kolize nemohou ubývat. Vynechání stavů c>153 tudíž neovlivní
žádnou z požadovaných distribučních funkcí. Ve výpočtu se každá
položka ukládá jako celé číslo krát2^(-160) a zaokrouhluje dolů.
Přechod má nezáporné koeficienty na dosažitelných stavech a
nezvětšuje součet absolutních chyb. Každý krok zavede nejvýše
154 jednotek chyby. Celková chyba libovolné dolní kumulativní
pravděpodobnosti je proto nejvýše

```text
(n−1)154 / 2^160 < 1.73 * 10^(-42).
```

Pro m=2^20,n=2^14 leží celé certifikované intervaly uvnitř
příslušných intervalů zaokrouhlení na tři desetinná místa:

| Nejvýše kolizí | Pravděpodobnost, informativně | Kniha |
|---:|---:|---:|
|101|0.008611382310478|.009|
|108|0.043194299802245|.043|
|119|0.243920037030565|.244|
|126|0.476115952769318|.476|
|134|0.742362296913647|.742|
|145|0.945803107494083|.946|
|153|0.988842904440608|.989|

Očekávaný počet kolizí127.328237999849... má zvláštní racionální
certifikát: sousední částečné součty alternujícího binomického
rozvoje, jehož členy zde klesají. Zaokrouhlení127.33 souhlasí.
Doslovný float model S reprodukoval všech sedm prahů. Jeho
shoda není použita jako důkaz přesnosti tabulky.

Bitové pole pro2^20 možných dvacetibitových slov má2^20 bitů,
tedy2^15 dvaatřicetibitových slov, jak uvádí text. Nezávislá
distribuce předpokládá nepřekrývající se dvacetice nezávislých bitů.

## Paměťový odhad má omezený obsah

Kniha uvádí šířku aktivního intervalu j1−j0 nejvýše řádu log(n).
Pro pevný poměr m/n=64 a práh10^(-20) experiment dal:

|n|256|1024|4096|16384|65536|
|---:|---:|---:|---:|---:|---:|
|největší j1−j0|24|43|92|196|390|

V tomto rozsahu šířka připomíná sqrt(n). Z konečných dat ale
neplyne vyvrácení asymptotického tvrzení. Při pevném absolutním
prahu má rozdělení o hmotnosti nejvýše1 nejvýše10^20 položek
nad prahem, což v přesné aritmetice s ořezáváním dává i triviální
konstantní mez; pro extrémní n může ovšem zaniknout použitelná
aproximace. Bez určení vztahu n,m, přesnosti a povolené chyby
proto tato věta neposkytuje užitečný rovnoměrný odhad. Samostatný
nový matematický nález z ní nevyvozujeme.

## Rozsah kontroly

`verify_collision_test.py` a `results/collision-test.json` obsahují
42 modelů m=1..6,n=1..7, celkem458961 úplně enumerovaných slov,
porovnaných s přesnou racionální rekurencí a střední hodnotou;
dále certifikát tabulky, dva přesné modely binary64 a uvedený
experiment šířky. Všech pět bloků prošlo. Původní čtyři dokončené
bloky se při doplnění řidšího protipříkladu neopakovaly.

Všechny čtyři vrstvy errat a aktuální TeX prohledány1.11.2026.
Oprava této části nenalezena. Tento blok uzavírá I, nikoli J
nebo celou §3.3.2; nové úlohy se jím neuzavírají.
