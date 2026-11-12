# Runs: střídavé běhy, úlohy15–16

Zadání46/file57; odpovědi604–605/files615–616. Sazba v
`images/runs-file-057.png`, `multisets-file-615.png`, `multisets-file-616.png`.
Známé opravy v `sources/runs-errata-review.json`. C0004 převzat beze změny
z `notes/V3-C0004-alternating-run-variance.md`; žádný nový nález ani běh.

## 15. Definice, příklad a průměr

Pro n≥2 určuje střídavé běhy posloupnost znamének sousedních rozdílů;
počet běhů je1 plus počet změn znaménka, tedy počet vnitřních vrcholů
a údolí plus1. Obrácení slova obrátí i neguje posloupnost znamének,
komplement hodnot ji neguje; obě operace počet změn zachovají.
Příklad53247618 má znaménka−−++−−+, tedy čtyři uvedené úseky.
Maximálně se mění každé sousední znaménko: n−1 běhů, dosažených např.
slovem1,n,2,n−1,... . Pro jednu hodnotu se v úloze16 používá konvence0.

Ze šesti pořadí trojice mají čtyři prostřední prvek největší nebo
nejmenší. Každá vnitřní pozice tedy přispívá pravděpodobností2/3 a
průměr je `1+2(n−2)/3=(2n−1)/3`, n≥2.

## 16. Vložení maxima a generující funkce

Vkládejme n do slova délky n−1 se k střídavými běhy. Vnitřní mezera
mění původní znaménko na dvojici+−. Obě mezery vedle každého vrcholu
počet zachovají; rovněž přední mezera při počátečním poklesu a zadní
mezera při koncovém vzestupu. Je-li p počet vrcholů, těchto mezer je
`2p+[první znaménko−]+[poslední znaménko+]=k`.

U předního okraje je právě jedno ze dvou míst (před první hodnotou,
nebo po ní), které přidá jeden běh; totéž u zadního okraje.
Tyto dvě mezery jsou různé i pro délku2. Ostatní vnitřní mezery
přidají dvě změny znaménka. Všech n mezer se tedy rozpadá na
k s přírůstkem0, dvě s přírůstkem1 a n−k−2 s přírůstkem2.
Při délce1 dávají obě vložení jeden běh a souhlasí s konvencí k0.
Smazání maxima je inverze, takže tištěná rekurence počtů je úplná.

Po součtu a dělení n! dostáváme přesně
`n G_n=z(1−z²)G'_(n−1)+[2z+(n−2)z²]G_(n−1)`, G_1=1.
První další členy jsou `G_2=z`, `G_3=(z+2z²)/3`;
rovněž G_n(1)=1 indukcí.

## Derivace a parita

Označme x_n=G_n'(1), y_n=G_n''(1). První derivace rekurence dává
`n x_n=(n−2)x_(n−1)+2n−2`; počáteční x_2=1 a již dokázaný
výraz(2n−1)/3 souhlasí pro všechna n≥2.

Druhá derivace dává nejprve
`n y_n=(n−4)y_(n−1)+(4n−10)x_(n−1)+2n−4`.
Pro n≥3 dosazení střední hodnoty mění poslední členy na
`8n²/3−26n/3+6`, přesně jak stojí v odpovědi.
Při n4 vymizí závislost na y_3 a vyjde y_4=7/2.
Dosazení polynomu `y_n=4n²/9−14n/15+11/90` ověří rekurenci
i tuto počáteční hodnotu; tudíž platí pro n≥4.
Algebra rozptylu y_n+x_n−x_n² a chyba symbolu g_n místo G_n jsou
již uzavřený C0004 a neopakují se.

V bodě−1 platí `G_n(−1)=(n−4)G_(n−1)(−1)/n`, tedy od n4 je
hodnota0. Proto je sudých a lichých počtů střídavých běhů právě n!/2.
Oprava malého g na velké G v tomto pozdějším řádku je známé erratum2006.

## Závěrečný vztah s Eulerovou GF

Z Eulerovy vkládací rekurence plyne
`n g_n(t)=n t g_(n−1)(t)+t(1−t)g'_(n−1)(t)`.
Položme `t=(1−w)/(1+w)`, takže `z=2t/(1+t²)`.
Pravá strana posledního vzorce odpovědi16 pak je
`B_n(t)g_n(t)`, kde `B_n=4(1+t)^(n−3)/(1+t²)^(n−1)`.
Pro n2 dostaneme z, tedy G_2.

Ověření rekurence je krátké: pišme R=B_n/B_(n−1)=(1+t)/(1+t²).
Pak
`z(1−z²)/(dz/dt)=R t(1−t)` a
`B'_(n−1)/B_(n−1)=(n−4)/(1+t)−2(n−2)t/(1+t²)`.
Koeficient g'_(n−1) po substituci do rekurence pro G je R t(1−t),
a koeficient g_(n−1) je
`R t(1−t) B'_(n−1)/B_(n−1)+z(2+(n−2)z)=nRt`.
Jsou to právě R-násobky Eulerovy rekurence. Indukce dokazuje vztah
pro všechna n≥2. Změna větve odmocniny mění t na1/t a známá symetrie
`g_n(t)=t^(n+1)g_n(1/t)` zachová celý výraz, takže vztah je jednoznačný;
výjimečné body se doplní polynomickou kontinuitou.

Historické atribuce a obsah citací nebyly ověřeny. Odkaz na maximální
počty v§5.1.4-23 neobsahuje zde žádný další číselný vzorec; tato úloha
zůstává v přirozené frontě Tableaux.
