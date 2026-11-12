# Lokální výměny 208–214 a obrázek 73

Kontrola 3. listopadu 2026. Celé zadání a odpovědi 208–214 byly přečteny
v knižním PDF a v PDF odvozeném z autorova PostScriptu. Matematický průchod
je dokončený s výslovným vynecháním úplného výčtu a historických benchmarků.
Nový dosud neopravený nález nepřibyl. Hlavní strana 106 zůstává částečná
kvůli přesné historii Haselgroveové; strana 108 pokračuje úlohou 215 a
preprocessingem. Celý svazek hotový není.

## Přesný rozsah zdrojů

Kniha: hlavní strany 106–108, zadání 150–151, odpovědi 472–473.
Odpovídající autorův draft: 42–44, 86–87, 176–177.
Nové texty a vektorové výpisy jsou v `sources/exchanges208_214/` a
`results/exchanges208_214/`; strany 150/472 a jejich protějšky byly
znovu použity z bloku `focus202_207`. Všechny příslušné stránky byly zobrazeny.
OCR samo není důkaz znění.

Přijatý [zdrojový checker](check_exchanges208_214_sources.py) trval
11,861 s při nice 15. Neprovádí globální výčet pokrytí. Čte oba obrázky,
ověřuje uložené svědky, dva nové malé stromy a dva příklady na třech
vrcholech každé části bipartitního grafu. Výsledek:
[source-checked.json](results/exchanges208_214/source-checked.json).
Starý výčet 17 199 výměn rozkladů ani ostatní přijaté testy se neopakovaly.

## Obrázek 73 a úloha 208

V obou verzích bylo z vektorových obrysů a glyfů získáno všech 45 Y
pentomin a 45 označených buněk. Pokrývají 225 buněk právě jednou.
Podél vyznačené cesty byl v každém kroku ověřen nejmenší počet možností
a pořadí položek při remíze. Pěticestné větvení nastává právě u
8, b, e, g, h, C; větší stupeň se nevyskytuje. Prvních osm dílků leží
u čtyř rohů, jak je přímo vidět v původním obrázku.

Čtyři H tvoří dvojice **8–b, o–p, t–v, F–G**. Dvojice 8–b má přesně
buňky uvedené v opravené nápovědě. Pro každou sjednocenou desetibuněčnou
oblast existují dvě Y dekompozice. Libovolný pevný Y má jediného možného
partnera do H: vedle jeho čtyřbuněčného sloupce musí být druhý rovnoběžný
sloupec a chybějící prostřední buňka. Stejný argument platí po otočení.
Proto se H nemohou překrývat v dílku, jejich převrácení komutují a
nevytvářejí H mimo již přítomné oblasti. Obrázek tak opravdu dává 16
navzájem nekongruentních pokrytí.

Osm množin S0,…,S7 je přesně osm orientací Y. Je 1 344 umístění na
15×15, z toho 40 obsahuje střed. Zachování jediné orientace prostředního
dílku ponechá pět z těchto čtyřiceti možností a 1 309 možností celkem.
Y nemá netriviální symetrii; střední buňka určuje jediný dílek, takže
žádné pokrytí nemůže mít netriviální symetrii celého čtverce. Každá
orbita má osm členů a zvolenou orientaci středu právě jeden.

**Konvence středu:** obrázek má dílek l v orientaci S4 na buňkách
58, 68, 77, 78, 88. Odpověď 208 používá S0. V obrázku sedí cesta MRV
pro S4; nelze ji bez otočení vydávat za cestu instance s S0. Obě jsou
platné volby reprezentanta symetrie. Obrázek nepojmenovává povolenou
orientaci; z tohoto rozdílu nevyvozujeme nové erratum. Zrcadlení řádků
převede střední S4 na S0. U ostatních H lze následně zvolit požadovaný
nepřevrácený rozklad, aniž se dotkneme středu, pokud v něm H není.

Opravené sekundární položky S4→Vij, S5→H(i+1)j,
S6→Vi(j+1), S7→Hij zakazují právě současné použití převrácených
polovin H. Například vertikální H má levou polovinu S6 s kotvou
(i,j−1) a pravou S4 s kotvou (i,j); obě dostanou Vij. Nepřevrácené
poloviny S2 a S0 zůstávají povolené. Horizontální případ je otočení.
Po omezení středu má model 292 dvojic sdílejících sekundární položku;
všechny odpovídají takovému H. Dalších 68 položek má jediný výskyt.
Z nich 48 vzniká na okraji mimo deklarovaný rozsah; jejich vynechání
nebo ponechání nemění přípustná pokrytí. Zbývajících 20 osiřelo
omezením středu. To je implementační konvence, nikoli nový nález.

Jediný [SAT pokus](check_y208_bounded.py), Glucose4 s limitem 20 s
a nice 15, nalezl 16 redukovaných pokrytí. Skončil **timeoutem** po
20,258 s, nikoli UNSAT. Modely jsou zachované v
[y-bounded.json](results/exchanges208_214/y-bounded.json).
Každý svědek byl geometricky validován; následná kontrola všech H
a symetrií je samostatná od SAT kódování.

Počty H v těchto 16 svědcích mají histogram 2:5, 3:4, 4:4, 5:3.
V žádném H není střed. Všechna jejich lokální převrácení dávají
5·4 + 4·8 + 4·16 + 3·32 = **212** navzájem nekongruentních platných
pokrytí, s osmi různými symetriemi každého. Souhlasí i multiset
exponentů v odpovědi. To je **nezávislá dolní mez 212**, nikoli důkaz,
že další řešení neexistují. Žádné nové dlouhé hledání ani restart
se kvůli horní mezi nespouští.

Výslovně vynecháno podle pokynu uživatele: úplnost 16/212, tvrzení
o alespoň dvou H u všech řešení, že vytištěné pokrytí je skutečně
první nalezené celou implementací, a historické hodnoty 92/26 Gμ.
Přesná geometrie, odvození modelu a lokální výměny jsou ověřené.
Registr vynechání je označen `verified:false`; starý záznam pro
benchmarky 207 zůstává beze změny a tento výsledek jej jen doplňuje.

## Malé příklady, Theorem S a 209

Zachování sjednocení u bipáru dává obousměrnou výměnu řešení.
Sdílená sekundární položka zakazuje přesně společný výběr příslušných
dvou možností. Příklad (99) zmenší strom (91) na přesně vytištěný
14uzlový strom (100). Úloha 209 používá správné bipáry a přidává
A k 01,234 a B k 02,145; dostane přesně vytištěný vyvážený strom
o sedmi uzlech s jedním řešením. V každé zdrojové verzi tak bylo
zkontrolováno 21 uzlů a 19 hran dvou nových stromů.

V příkladu (101) bylo přepsáno všech devět možností a přiřazení
sekundárních A,…,F k šesti uvedeným bipárům. Každé ze šesti
perfektních párování poruší nejméně jednu sekundární položku.
Příklad tedy opravdu zničí všechna řešení.

Theorem S tomu zabrání pevným pořadím možností: redukce nahradí
nepreferovanou dvojici preferovanou a na prvním změněném místě
vektoru volby zapíše 1 místo 0. Vektor striktně roste v konečné
množině řešení, proto proces skončí v silném řešení. Původní
možnosti preferované dvojice nemohou být již zvolené, protože
jejich neprázdné množiny primárních položek překrývají nahrazované
pokrytí. Příklad (99) dovoluje požadované pevné pořadí.

## Celé 210–214

Obecné důkazy v [FOCUS_THEORY_NOTES.md](FOCUS_THEORY_NOTES.md)
zůstávají přijaté; byl doplněn průchod celým původním zněním.

- **210:** primární položka #A s násobností 0 až 2, vložená do tří
  nepreferovaných možností, zakáže právě jejich současný výběr.
  Neostrá preference Algorithm M je správná.
- **211:** zachování poloh a předepsaných vzdáleností vylučuje
  Langfordovy bipáry; výměna rohů obdélníku nezachová diagonály dam;
  sudoku by při výměně dvou číslic vyžadovalo shodný řádek i sloupec.
  Dřívější konkrétní bitriple a biquadruple svědci zůstávají platní.
- **212:** nejmenší položka je v α a α′; pořadí podle minima a pak
  lexikograficky je pevné pořadí požadované větou. Knižní příklad
  1<2 a 1<4<0<5 funguje; doplnění 1<2<4<0<5<3 preferuje 14 v prvním
  bipáru a 01 ve druhém. Tím zakáže právě dvojice (99).
- **213:** vlastní prefix musí být větší, jak odpověď výslovně
  stanoví. První změněná položka při obvyklém neprefixovém porovnání
  opouští dřívější blok a vstupuje do pozdějšího. Opačný případ
  nastane právě při vyčerpání α jako prefixu α′; zvolená konvence
  jej správně obrátí. Původních 17 199 malých výměn se neopakovalo.
- **214:** konečný orientovaný graf redukcí je acyklický, proto
  obrácená dosažitelnost ze všech silných řešení najde všechna řešení.
  Duplicity je potřeba sjednocovat. Konkrétní sedmimožnostní příklad
  má tři řešení; první dvě orientace bipárů dávají dva silné vrcholy
  se společným nesilným předchůdcem. Alternativní orientace dává
  jediný silný vrchol. Obě sady mají explicitně nalezené pevné pořadí
  možností splňující všechny podmínky kanonického bipáru.

## Publikované opravy a historické zdroje

Prohledány všechny čtyři PDF/textové vrstvy 4B/Fascicle 5 a oba
primární TeXy. Hashované výsledky a kontexty jsou v
[errata-check.json](results/exchanges208_214/errata-check.json).
Relevantní původní stránky úplných errat 6, 7, 15 byly zobrazeny.

- **E095:** 10. 7. 2021, Fascicle 5 str. 102, `evenually` →
  `eventually`; drobný historický doplněk k již uzavřenému bloku 202–207.
- **E096:** 17. 11. 2021, str. 280, odpověď 208: první V má být Vij
  a na konci chybělo Hij. Naše kniha už obsahuje správné přiřazení.
- **E097:** 19. 12. 2021, str. 148, zadání 208: pořadí dvou možností
  v nápovědě prohozeno tak, aby odpovídalo pořadí označení 8,b.

Všechny tři změny chybí v draftu 2019 a jsou zapracované v knize.
Nejde o nové nálezy.

Knuthův primární [Dancing Links](https://www-cs-faculty.stanford.edu/~knuth/papers/dancing.tex.gz)
je už uložen v `sources/pentomino_main/dancing.tex`. Relevantní odstavec
a reference 20 potvrzují, že autor sám publikoval počet 212 a odkaz
na Haselgroveovou, JRM 7 (1974), 229. Nejde o další nezávislý výčet.
[Reidův přehled](https://sicherman.net/mikereid/y5_rect.html)
uvádí 15×15 jako nejmenší lichý obdélník; uložená stránka je podpůrný
pramen, nikoli Haselgroveové původní článek. Její textový číselný odkaz
u této věty navíc nesouhlasí s bibliografickým pořadím; toto není
nález v TAOCP. [Historie Multumu](https://www.ourcomputerheritage.org/Minicomp/ICS_Multum_for_OCH_V1.pdf)
potvrzuje využití tohoto počítače pro hledání daného pokrytí.
Původní jednostránkový článek z roku 1974 se nepodařilo získat.
Přesné pořadí hledání v roce 1973 a vyloučení menších obdélníků/9×25
v jejím programu proto zůstávají zdrojovou mezerou strany 106.

Vývojové opravy před přijetím checkeru: skutečná orientace středu
v obrázku je S4; obě volby symetrie jsou nyní výslovné. Byly upraveny
hranice ořezu stromu 209 a porovnání správných polovin příkladu 212.
První render errat mířil do `originals/`, kde je PostScript; správné
PDF je v `errata/pdf/`. Úspěšné kontroly se po přijetí neopakovaly.
