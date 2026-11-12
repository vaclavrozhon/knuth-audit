# Úlohy53–54 a celý původní obrázekA–13

Zadání p118/file133 a odpovědi s celým obr.A–13 na p170/file185
byly zobrazeny. Nativní vektorové cesty byly získány přímo ze
sazby, včetně černých čar skrytých pod bílými kroužky jmen.
`check_hc_examples53_54.py` a `results/hc-examples53-54.json`
uchovávají všechny body, pořadí, relace, průchody stěnami,
pět obvodových možností54 a všech20 původních značek.
Krátký cílený běh nice15 nepoužívá všeobecný census labelings.

## E53-1 — obě úplné nativní geometrie

Pozitivní afinní normalizace cest18–19 dává souřadnice

    a(16,0), b(13,3), c(12,6), d(13,9), e(16,12),
    f(8,8), g(0,6), h(8,4), i(10,6).

Cesty38–39 druhého obrázku dávají

    a(7,1), b(8,0), c(0,3), d(8,6), e(7,5),
    f(7,4), g(6,3), h(7,2), i(8,3).

Odchylka každého nativního bodu je menší než0.01pt. V obou
obrázcích jsou přesně hrany ab,ah,bc,cd,de,ef,fg,fi,gh,hi.
Úplné rozdělení segmentů na průsečíky žádný další bod nepřidá;
obě geometrie mají9junctions,10čar a3stěny včetně vnější.
Všechny determinantové podmínky47 byly ověřeny v přesných
celočíselných souřadnicích. Oba obrázky jsou realizovatelné:
mají7V,2Y a žádné T s dodatečnou podmínkou.

## E53-2 — stejná HC síť včetně všech pořadí

U obou realizací vychází přesně

    a=V(b,h), b=V(a,c), c=V(b,d), d=V(c,e), e=V(f,d),
    f=Y(e,g,i), g=V(h,f), h=Y(a,i,g), i=V(f,h).

U Y je dovolena pouze cyklická rotace, která zachovává tutéž
relaci Tabulky1; zrcadlové obrácení se nepoužilo. Shoda
abstraktního grafu tedy není zaměněna za shodu uspořádané
HC sítě. Výše je zkontrolován každý její junction.

## E53-3 — biconnected, dva různé obvody a nutný další vstup

Graf tvoří tři vnitřně disjunktní cesty z f do h:

    f g h,    f i h,    f e d c b a h.

Po smazání f či h zůstávají všechny tři zbytky připojeny
k druhému konci. Po smazání vnitřního bodu jedné cesty
dvě celé zbývající cesty stále spojují f,h a oba zbytky
porušené cesty jsou připojeny k jednomu z nich. Žádný bod
tedy není artikulace: graf je biconnected. To je i přímo
zaznamenáno pro všech devět jednotlivých smazání, ale důkaz
nezávisí na algoritmickém testu.

První vnější průchod je g,h,a,b,c,d,e,f,g. Druhý je
c,b,a,h,i,f,e,d,c. Jsou jednoduché a liší se již množinou
bodů: první obsahuje g a ne i, druhý i a ne g. Nejde tedy
o cyklický posun ani obrácení stejného obvodu. Tím je
odpověď53 úplným protipříkladem i s biconnected předpokladem.
HC síť sama nerozhoduje, který z těchto geometricky možných
obvodů zadavatel míní. Postup50, jenž má analyzovat skutečný
obvod konkrétního obrázku, proto potřebuje také jeho zadání.
Netvrdí se, že dvě geometrie musí vždy dát různé booleovské
výsledky libovolného konkrétního testu.

## E54-1 — celá síť a platnost obvodového modelu

Nativní cesty58–60 dávají po afinní normalizaci

    a(0,0), b(2,1), c(4,1), d(6,0), e(6,4),
    f(3,5), g(0,4), h(3,2), i(2,3), j(4,3).

Obvod je a,b,c,d,e,f,g,a; uvnitř jsou dvě disjunktní cesty
b–h–c a g–i–j–e. Celkem10junctions a12čar, typy6V,2W,2Y.
Přesné determinanty všech junctions a žádné nežádoucí
průsečíky zajišťují realizovatelnost. Žádné T zde není.
Pořadí případů50 je přesně VYYVWVW, vnitřní větve v jeho
pořadí jsou bh,ch,ej,gi. Všechny čtyři jsou různé fyzické
čáry a obvod je jednoduchý. Všechny předpoklady korektního
podmíněného maticového důkazu50 zde proto skutečně platí.

## E54-2 — všech pět obvodových řešení a tištěná stopa

Pišme x pro štítek de=ef a y pro fg=ga, oba ve směru
obvodového průchodu. W v e,g nutí tyto rovnosti a dovoluje
jen stavy>,−,+. V v f má v tomto omezení právě dvojice
(x,y)=(>,>),(>,−),(−,>). Tím oba W nutí své vnitřní větve+.

Pro horní úsek a,b,c,d se vynásobí pouze VYYV. V relevantních
vstupních/výstupních stavech má tento součin:

    Q_(>,>) = 2mm+gl,  Q_(>,−)=mm,  Q_(−,>)=mm.

Přímé odvození po přechodech dává pro (x,y)=(>,>) horní
trojice (ab,bc,cd) přesně `>>>`, `---`, `-<-`; pro zbývající
dvě dvojice je horní trojice pouze `>>>`. Tím je vyčerpání
úplné a nevyžaduje zkoušet obecná přiřazení všech čar.
Celých sedm obvodových štítků a odpovídající vnitřní slovo
jsou tedy právě

| ab,bc,cd,de,ef,fg,ga | bh,ch,ej,gi |
|---|---|
| `>>>>>>>` | mmpp |
| `>>>-->>` | mmpp |
| `--->>>>` | mmpp |
| `>>>>>--` | mmpp |
| `-<->>>>` | glpp |

Každý řádek přímo vyhovuje svým sedmi obvodovým relacím;
čtyři m a jedno gl dávají přesně tištěnou stopu4mmpp+glpp.
Celý16prvkový maticový součin je navíc uložen v certifikátu,
nikoli odvozen pouze ze správného celkového počtu5.

## E54-3 — jediné rozšíření, neexistence standardního a všechny značky

Každé ze čtyř slov mmpp dává na obě čáry u vnitřního h
znaménko−. To V nepřipouští. Nezávisí to na ostatních
vnitřních čarách, takže všechny čtyři možnosti jsou vyloučeny.
Pátý řádek glpp dává bh>,ch<,ej+,gi+. Junction h tyto dvě
šipky přijímá. V v i s gi+ nutí ij< a V v j s ej+ přijímá
právě tutéž čáru; zbývá jediná úplná možnost. V orientaci
od menšího písmene k většímu je to

    ab−, ag<, bc<, bh>, cd−, ch<, de>, ef>,
    ej+, fg>, gi+, ij<.

Je ověřeno všech10relací tohoto svědka. Standardní obvod
je první tabulkový řádek, již vyloučený v h. Jediný labeling
je tedy skutečně nestandardní a žádný standardní neexistuje.

Každá z20 původních značek byla spárována s konkrétní čárou:
čtyři bílé výřezy61,62,64,65 představují−; čtyři červené
příčné tahy76,77,79,80 představují+; dvanáct dalších cest
jsou šipky. U šipky je prostřední bod hrot a směr se počítá
od středu dvou koncových bodů k hrotu, nikoli z vizuálního
odhadu. Každá značka souhlasí s uvedeným jediným labelingem.
Více značek na jedné čáře je kontrolováno jednotlivě. Tím
je ověřen i celý konkrétní obrázekA–13(c), nejen jeho existence.
