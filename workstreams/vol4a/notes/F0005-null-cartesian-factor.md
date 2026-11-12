# V4A-F0005 — nulový faktor v chromatickém čísle Cartesian součinu

6. listopadu 2026. **Confirmed, low.** Odpověď §7–128, tištěná strana
530, souborová 547. Jde pouze o chybějící okrajovou podmínku; standardní
výsledek pro dva grafy s alespoň jedním vrcholem a jeho barevná konstrukce
jsou správné. Žádný výpočet ani nový census.

## Přesná doména ze sazby

* P13/file030 definuje graf pomocí konečné množiny vrcholů V; není zde
  podmínka V≠∅. Nejde pouze o použití symbolu n bez určeného oboru:
  odpověď 41(b), p521/file538, výslovně zahrnuje K₀=C₀, a odpověď 78(a),
  p524/file541, zahrnuje K₀ mezi samodoplňkové grafy.
* P17/file034 definuje k-barvitelnost jako obarvení vrcholů nejvýše k
  barvami se zákazem stejné barvy na sousedních vrcholech.
* P27/file044 definuje vrcholy součinu jako U×V. Definice nevyřazuje
  prázdnou množinu faktorových vrcholů.
* P35/file052, (64), definuje χ jako minimum k, pro které je graf
  k-barvitelný, a výslovně vztahuje definici i na obyčejné grafy.
* Zadání 128 na p44/file061 říká pouze, že G a H jsou grafy. Odpověď
  p530/file547 uvádí χ(G □ H)=max(χ(G),χ(H)) bez dalšího omezení.

Všechny rozhodující formule a domény byly porovnány s původními obrázky;
OCR sloužilo jen k navigaci. Odpověď 80 má ve známých erratech nově
omezení alespoň dvou vrcholů, ale to je lokální oprava jiného zadání,
nikoli globální změna definice grafu nebo předpoklad úlohy 128.

## Protipříklad nezávislý na konvenci χ(K₀)

Zvol G=K₀ a H=K₂. Součin má množinu vrcholů ∅×{0,1}=∅, tedy je K₀.
Prázdné přiřazení barev je platné obarvení nejvýše jednou barvou:
neexistuje vrchol ani hrana, na které by mohlo porušit definici.
Proto χ(K₀)≤1. K₂ má dva sousední vrcholy, takže χ(K₂)=2. Dostáváme

    χ(K₀ □ K₂)=χ(K₀)≤1 < 2=max(χ(K₀),χ(K₂)).

Není třeba rozhodnout, zda se minimum v (64) bere od k=0 nebo od k=1.
Obě běžné konvence dávají rozpor. Chybná je zde i věta odpovědi, že
maximum je nutné: kopie faktoru H v součinu vyžaduje zvolený vrchol G,
který v tomto případu neexistuje.

## Oprava a rozsah starého důkazu

Stačí doplnit V(G)≠∅ a V(H)≠∅. Pak zafixovaný vrchol každého faktoru
skutečně dává v součinu kopii druhého faktoru a dolní mez max platí.
Pro k=max(χ(G),χ(H))≥1 vezmi vlastní barvení a,b hodnotami 0,…,k−1.
Barva (a(u)+b(v)) mod k se při změně po hraně v právě jedné souřadnici
změní, protože rozdíl dvou různých barev má absolutní hodnotu <k.
Tím je dokázána i horní mez; není nutná žádná jiná změna argumentu.

Chce-li se zachovat celé původní zadání, doplní se větev: je-li jeden
faktor bez vrcholů, výsledek je χ(K₀); jinak uvedené maximum. Dosavadní
`proof-016-colorings-cliques.md` obsahoval právě důkaz pro neprázdný
součin, ale stav P0419 byl širší než jeho předpoklady. Obnova jej nejprve
vrátila na partial a nyní přesně odděluje správný nenulový případ od této
okrajové chyby. Nejde o chybu obecné barevné konstrukce.

## Errata — všechny relevantní vrstvy

Kontrola 6. 11. 2026 nad uloženými historickými a současnými vrstvami:
`errata/text/all4a-pre.txt`, `all4a.txt`, `err4a.txt`, `all4f0.txt`,
`err4f0.txt`. Prohlédnuty oblasti zadání 36–46 a odpovědí 514–534,
v původním Fascicle 0 odpovídající odpovědi 134–154, a výskyty 128,
530/150, null/empty/nonempty a chromatic/Cartesian. Žádná z těchto
vrstev neopravuje úlohu 128 ani nepřidává její chybějící předpoklad.

Historické opravy u p530 se týkají citace 126 a odkazu 131; známá oprava
zadání 80 z roku 2024 nemění doménu 128. Bibliografická kontrola není
tvrzením o prvenství. Fyzický exemplář prvního dotisku nebyl ověřen.

## Doklady

* `images/file030.png`, `images/file034.png`, `images/file044.png`,
  `images/file052.png`, `images/file061.png`: definice a zadání.
* `images/proof-file538.png`, `images/proof-file541.png`: explicitní K₀.
* `images/proof-file547.png`: samotná chybná neomezená odpověď.

V UI patří červená lokace pouze odpovědi p530/file547; zadání žádá určit
hodnotu a samo neobsahuje nepravdivý vzorec. Závažnost je low vzhledem
k čistě nulovému faktoru a snadnému doplnění podmínky.
