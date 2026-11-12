# D173–D174 — celé MPR71–72

7. listopadu 2026. Přímo zobrazeno původní zadání p19/file39
a odpovědi p381/file401; také PS p19/file25 a p38/file44.
Šest vrstev errat a tři TeX zdroje posouzeny včetně známé
opravy72. Žádný numerický běh. Definice X₀=1 a X_j jako
indikátoru j-tého červeného tahu pro j>0 odpovídá již
ověřenému hlavnímu textu v D098; následující důkaz nepoužívá
nezávislost těchto indikátorů.

## 71: každá cesta mezi dvěma uzly

Uzly obrázku P mají kladná celá r,b. Při r′≥r a b′≥b
položme m=r′−r,n=b′−b. Každá cesta do cíle má přesně
m červených a n černých přidání, proto délku m+n.
Volba n pozic černých tahů je bijekce mezi cestami
a podmnožinami velikosti n z m+n pozic. Cest je
binom(m+n,n); neexistuje žádná další překážka dosažitelnosti.

Při červených tazích jsou postupné červené počty před
přidáním r,r+1,…,r′−1; černé tahy je nemění. Obdobně
černé čitatele jsou b,b+1,…,b′−1. Jmenovatele postupují
v každém tahu od r+b po r′+b′−1. Z řetězového pravidla
podmíněných pravděpodobností má každá jednotlivá cesta váhu

    r(r+1)···(r+m−1) · b(b+1)···(b+n−1)
    -------------------------------------------------
              (r+b)(r+b+1)···(r+b+m+n−1)
      = r^overline(m) b^overline(n)/(r+b)^overline(m+n).

Součin závisí na koncovém uzlu, ne na pořadí barev.
Cesty jsou disjunktní a úplné, takže požadovaná
pravděpodobnost je tento součin krát binom(m+n,n).
Všechny jmenovatele jsou kladné. Pro m=0 nebo n=0
prázdný barevný součin znamená1; pro m=n=0 je výsledkem1
a cesta má délku0. Mimo předpoklad r′≥r,b′≥b by byla
pravděpodobnost0, protože počty nikdy neklesají.

Při r=b=1 je součin m!n!/(m+n+1)!. Násobení počtem cest
dává1/(m+n+1)=1/(r′+b′−1), včetně kořene m=n=0.
Tím jsou doloženy všechny vytištěné faktory, horní
indexy rostoucích faktoriálů i poslední zjednodušení.

## 72: úplná konečná záměnnost a každý příklad

Pro libovolné N≥1 má konkrétní bitová historie délky N
s k jedničkami a N−k nulami podle71 pravděpodobnost

    k!(N−k)!/(N+1)!.

Záleží jen na počtu jedniček. Každá permutace N pozic
tedy zachovává pravděpodobnost každého atomu, a proto
i všech událostí. To dokazuje konečnou záměnnost přímo,
bez užití externí reprezentační věty.

Zvolme N=n_m. Existuje permutace prvních N pozic, která
přenese vybrané různé kladné indexy n₁,…,n_m na1,…,m.
Sečtením atomů přes ostatní pozice se zachová i příslušná
marginální událost. Proto

    E(X_{n₁}···X_{n_m})
      =P(X_{n₁}=···=X_{n_m}=1)
      =P(X₁=···=X_m=1)
      =(1/2)(2/3)···(m/(m+1))=1/(m+1).

Součin teleskopuje; při m=1 je výsledek1/2 a prázdný
součin pro m=0 by dal1. Podmínka n_i>0 je podstatná,
protože X₀ je deterministická1 a mezi losované pozice
nepatří. Neprovádíme nesprávnou permutaci včetně X₀.

Každý X_j pro j>0 má střední hodnotu1/2, takže při
nezávislosti by střední hodnota součinu byla2^{-m}.
Pro m≥2 se liší od1/(m+1), neboť 2^m>m+1 (základ m=2
a potom indukce). Kvantitativně pro i≠j je
E(X_iX_j)=1/3, kovariance1/12 a při rozptylu1/4 korelace1/3.
Tištěný dovětek o výrazné závislosti je tedy podložen;
žádné tvrzení o nezávislosti se do důkazu nevloudilo.

Pro tištěný příklad platí bodově
[X₂=1,X₅=0,X₆=1]=X₂(1−X₅)X₆. Linearita a předchozí
momentový vzorec dávají

    E(X₂X₆)−E(X₂X₅X₆)=1/3−1/4=1/12.

Obecně libovolný vzor a jedniček a b nul na různých
kladných pozicích má vahou71 a záměnností pravděpodobnost
a!b!/(a+b+1)!, což kontroluje i tento smíšený příklad.
Všechny veličiny jsou omezené, takže očekávání, konečné
součty i přeskupování atomů jsou bez problému.

## Známá oprava a bibliografie

E126 zaznamenává oficiální změnu z21.6.2022: v odpovědi72
„all paths“→„all paths to (r,b)“ a hodnocení M21→M23.
Přímo prohlédnuty původní errata all4f5 p3 a p10,
TeX bloky4f5.19 a4f5.193, současná4B i historický PS.
PS má původní volnou formulaci a M21; 4B obsahuje přesnější
formulaci i M23. Oprava není novým nálezem, kartou ani
důvodem červené mapy. Přesný důkaz výše používá pouze
cesty se stejným koncovým uzlem a pak permutuje tahy.

[Vydavatelský záznam Kallenbergovy knihy](https://link.springer.com/book/10.1007/0-387-28861-9)
přímo potvrzuje autora, úplný název, první vydání2005
a tematické zaměření na záměnnost a další symetrie.
To je celý bibliografický nárok v odpovědi72; nepřebíráme
žádnou vnější větu ani neprohlašujeme audit celé knihy.
Další bibliografická výjimka v tomto bloku není.

Celé71–72 včetně všech mezikroků, okrajů, smíšeného příkladu
a správně začleněné známé opravy jsou uzavřeny. File39 a401
zůstávají partial pro následující úlohy. Bez nového nálezu,
kandidáta, výpočtu nebo restartu.

