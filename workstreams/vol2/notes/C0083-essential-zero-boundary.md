# V2-C0083: nulový argument v (36)

**Confirmed v dostupných podkladech.** §4.2.2, str.234, implikace(36).
Původní sazba233–234 a definice normalizace215 vizuálně přečteny.
Neověřen nový fyzický dotisk ani prvenství; hlášení neodesláno.

Značení: b je základ, p počet cifer, q exces exponentu. Dvojice(e,f)
znamená hodnotu f*b^(e−q), kde zlomek f má p míst. Definice na215
výslovně zahrnuje do normalizovaných čísel také nulu s nejmenším
povoleným exponentem. Relace „essentially equal“, zde u≈v(ε), znamená

```text
|u−v| <= ε min(b^(e_u−q), b^(e_v−q)).
```

Podle(36) pro normalizovaná u,v a ε<1 plyne mimo jiné
`|u−v| <= b ε |u|`. To selhává při u=0.

## Přesný protipříklad

Vezměme b=10, p=8, q=0 a povolené exponenty0..99. Potom

```text
u=(0,.00000000)=0,
v=(0,.10000000)=1/10,
ε=1/10 < 1.
```

Obě čísla jsou normalizovaná. Podmínka u≈v(ε) je `1/10<=1/10`.
První závěr(36) je však `1/10<=0`. Žádná plovoucí operace se zde
neprovádí, takže vysvětlení pomocí přetečení nebo podtečení nepřichází
v úvahu. Stejný příklad funguje s libovolným excesem, se všemi hodnotami
vynásobenými b^(−q); lze jej tedy použít i přímo pro MIX.

## Oprava a její přesný rozsah

Stačí u(36) doplnit u,v≠0. Pro každý nenulový normalizovaný argument
platí b^(e−q)<=b|u|, což dává oba závěry přímo, dokonce bez ε<1.

Alternativou je změnit společný předpoklad ε<1 na **ε<1/b**.
Pokud u=0,v≠0 a u≈v(ε), normalizace v dává

```text
b^(e_v−q)/b <= |v|
             <= ε min(b^(e_u−q),b^(e_v−q))
             <= ε b^(e_v−q),
```

tedy ε>=1/b. Při ε<1/b je proto nulový jen jeden argument nemožný;
jsou-li oba nulové, závěr platí. Práh1/b je ostrý, jak ukazuje příklad.
Implikace(37) s alternativou „nebo“ tento problém nemá: exponent nuly
je minimální, takže větší exponent patří nenulovému argumentu.

## Errata a reprodukce

Dne2.11.2026 zkontrolovány všechny čtyři řady all2-prepre, all2-pre,
all2, err2 podle str.215,233,234, čísel vztahů a slov o normalizaci,
nule a aproximaci. Oprava(36) nenalezena. Poznámka16.4.1999 oznamuje
budoucí změnu konvence pro čtvrté vydání; nemění zde auditované třetí
vydání. Oprava15.5.2026 na234 mění až dvě řádky **za(37)**, zejména
ostrou nerovnost chyby zaokrouhlení na neostrou. Nulový případ(36)
neřeší; originál této opravy viz images/accuracy-errata-all2-5.png.

Přesné zlomky ověřuje blok zero_boundary v verify_accuracy_basic.py,
včetně základů2,3,10,64,100. Všechny protipříklady prošly. Program je
doplňkem uvedeného elementárního důkazu, nikoli jeho náhradou.
