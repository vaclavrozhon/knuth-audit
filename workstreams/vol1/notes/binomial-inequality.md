# §1.2.6-66: binomická nerovnost a okrajový případ

Audit 1. listopadu 2026. Zobrazeno původní zadání s. 74,
odpověď s. 491, náhrada z 8. listopadu 2005 v `all1-prepre`
s. 9 a 33 a následná změna z 17. dubna 2015 v `all1-pre`
s. 15. Zde se dokazuje rozšířené zadání z roku 2005.

Pro celé k>=0 je `C(t,k)=t(t−1)...(t−k+1)/k!` polynom.
Fixujeme celé n>=2 a reálné y>=n−1. Pro každé z>n−2
určuje rovnice

```text
C(x,n)=C(y,n)+C(z,n−1),       x>=n−1,                     (I1)
```

právě jedno x. Funkce C(t,n) je totiž na [n−1,infinity)
spojitá a ostře rostoucí od 0 do infinity; na otevřeném
intervalu je součinem kladných ostře rostoucích činitelů.
Protože C(z,n−1)>0, máme x>y a x>n−1.

## Druhá nerovnost

Zaveďme kladné X=C(x,n), Z=C(z,n−1) a nezáporné
Y=C(y,n). Označme

```text
F(z)=C(x,n+1)−C(y,n+1)−C(z,n),
alpha=(x−n)/(n+1), beta=(y−n)/(n+1), gamma=(z−n+1)/n.
```

Pak F=alpha X−beta Y−gamma Z a X=Y+Z. V každém kořeni
F(z)=0 proto platí

```text
(alpha−gamma)Z = −(x−y)Y/(n+1) <= 0,
tedy alpha <= gamma.                                    (I2)
```

Rovnost v (I2) může nastat při y=n−1; tuto možnost
nesmíme vypustit. Označme X_x=dC(x,n)/dx a Z_z=dC(z,n−1)/dz.
Logaritmické derivace součinů dávají

```text
X_x/X = 1/x+1/(x−1)+...+1/(x−n+1),
Z_z/Z = 1/z+1/(z−1)+...+1/(z−n+2).
```

Z (I2), po přičtení j/(n+1)<j/n pro j=1,...,n−1,
plyne `(x−n+j)/(n+1)<(z−n+1+j)/n`.
Všechny porovnávané jmenovatele jsou kladné. Převrácením
a sečtením n−1 nerovností, s dalším kladným členem 1/x,
dostaneme

```text
X_x/X > n/(n+1) * Z_z/Z,
x'(z)=Z_z/X_x < (n+1)/n * Z/X.                           (I3)
```

Proto v každém kořeni F

```text
F'(z)=X x'(z)/(n+1)−Z/n+(alpha−gamma)Z_z < 0.             (I4)
```

První dva členy mají ostře záporný součet podle (I3)
a poslední je nekladný podle (I2). Tento důkaz platí
také pro Y=0, nikoli jen vnitřní případ Y>0.

Pascalovo pravidlo dává x=y+1 při z=y, a tedy F(y)=0.
Všechny kořeny spojitě diferencovatelné F jsou podle (I4)
ostré přechody z kladných do záporných hodnot. Dva různé
takové kořeny by vyžadovaly mezi nimi kořen bez tohoto
směru přechodu, což je spor. Proto z=y je jediný kořen,
F>0 pro z<y a F<0 pro z>y. Dokázali jsme

```text
C(x,n+1) <= C(y,n+1)+C(z,n)  právě když  y<=z,             (I5)
```

s rovností právě při y=z.

## První nerovnost

Položme `G(z)=C(x,n−1)−C(y,n−1)−C(z,n−2)`.
Při n=2 je G=x−y−1; podle (I1) a monotonie C(t,2)
platí G<=0 právě tehdy, když z<=y.

Pro n>2 by každý kořen G spolu s (I1) byl případem
**rovnosti** v (I5), aplikované na řád n−1. Jeho podmínky
platí: x,y>=n−1>n−2 a z>n−2>n−3. Právě dokázaná
charakterizace rovnosti proto vynutí z=y. Tento kořen
opět existuje podle Pascalova pravidla.

Pro z↓n−2 máme Z→0, x→y, a tedy G(z)→−1.
Pro z→infinity vyplývá z vedoucích členů polynomů v (I1)
`x ~ n^(1/n) z^((n−1)/n)`. Proto C(x,n−1) roste jako
kladná konstanta krát z^(n−2+1/n), zatímco C(z,n−2)
roste jen jako z^(n−2). G je tedy nakonec kladná.
Spojitost a jediný kořen nyní dokazují

```text
C(x,n−1) <= C(y,n−1)+C(z,n−2)  právě když  y>=z,           (I6)
```

opět s rovností právě při y=z.

## Původní zadání z roku 1997

Původní verze má řád n+1, y>=n, y<=x<=y+1 a
C(x,n+1)=C(y,n+1)+C(z,n), n−1<=z<=y.
Při x=y je z=n−1 a výsledek je přímo rovnost.
Jinak z>n−1 a (I6) pro řád n+1 dává požadovanou nerovnost.
Tím jsou ověřeny oba matematické výroky, starý i rozšířený.

## Přesnost opraveného důkazu na hranici

Náhrada odpovědi z roku 2005 pracovala s y>n−1.
Oprava 2015 mění tento předpoklad na y>=n−1, avšak
pozdější věta stále používá Y,Z>0 a odvozuje alpha<gamma.
Na hranici to není pravda: n=2,y=z=1,x=2 splňuje
všechny předpoklady, ale Y=C(1,2)=0 a alpha=gamma=0.
Jde pouze o krok důkazu; (I5),(I6) zůstávají správné.
Stačí v uvedeném kroku použít Y>=0 a alpha<=gamma,
a závěrečnou ostrost získat z (I3), přesně jako výše.
Tento lokální nesoulad je potvrzen jako **V1-C0008**, s návrhem
zprávy `reports/V1-C0008.txt`. Není protipříkladem zadání.
Pět vrstev errat dostupných 1. listopadu 2026 neobsahuje
další změnu tohoto kroku. Jde o vadu kombinovaného znění
oprav 2005 a 2015; novější fyzický dotisk nebyl ověřen.
Samotný faktor (n+1)/n v (I3) je v obrazu errat správně,
i když pořadí při extrakci textu může klamat.
