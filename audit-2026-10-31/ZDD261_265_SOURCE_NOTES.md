# Úplné zdroje ZDD: hlavní strana 123 a úlohy 261–265

Kontrola 3. listopadu 2026. Sekce 7.2.2.1. Kniha: druhý digitální
dotisk 2022; hlavní str. 123, zadání 155, odpovědi 482–484. Autorův
draft: str. 59,91,186–188. Celé stránky v obou verzích byly vykresleny
a prohlédnuty, včetně dvou detailů Randallova obrázku. Seznam a otisky
27 prohlédnutých obrazů jsou v `sources/zdd261_264/source-observations.json`.
Adresář výsledků si ponechává počáteční název `zdd261_264`, ale blok
zahrnuje také 265. Texty zadání následujících úloh 156/92 jsou jen náhled.

## Výsledek a rozsah

- F154: posunutý parametr produktu a P₁₆ v 261(c); střední závažnost.
- F155: jeden modrý ohyb Randallovy cesty, 262(a); nízká závažnost.
- F156: čtyři číslice tabulky neodpovídají obrázku, 262(b); nízká.
- F157: jednotka MB místo KB ve dvou řádcích 263(g); nízká.
- C043/C044: dvě oddělené interpretační otázky konstrukce 261.
- E110/E111: známé opravy endpointového indexu a bibliografie.
- X251: celý zdrojový průchod 264–265 uzavřen. X250: 261–263 partial.
- D086: hlavní strana 123 partial, kvůli přesně vyjmenovaným historickým
  mezerám níže. Zbývající matematické a zdrojové mezery se neskrývají
  pod povolené vynechání drahých výpočtů.

Staré X262, F058 a F059 zůstávají beze změny. X262 ověřilo konkrétní
matematické výpočty a obecné lineární vzorce; neznamenalo prohlédnutí
každého nového obrázku, všech historických atribucí a celé odpovědi.
Nový úplný registr proto označuje 262 partial a starou přijatou evidenci
zachovává. Fyzický exemplář ani prvenství nálezů nejsou potvrzeny.

## 261 — cesty a jejich kanonické číslování

V části (a) položky v− a v+ vynucují buď jednu vstupní/výstupní
hranu, nebo nulovou možnost nepoužitého vrcholu. Shoda barvy vynucuje
stejné číslo cesty na obou stranách použitého vrcholu. DAG vylučuje
odpojené orientované cykly. Číslovací řetěz x_k,y_k vynucuje počet
vybraných zdrojů v prefixu a očísluje je v rostoucím pořadí. Každá
rodina m cest tak má právě jeden očíslovaný model; koncové y_p=m
vynucuje přesně m cest. Meze j<k jsou správné.

Část (b) funguje při zachování nulových možností, s omezením barev
na předepsané koncové dvojice. Slovo „main“ ponecháno jako C043.
Pět malých variant sítě včetně m=0, m=1, m=2 a obou párování má
počty 1,12,4,2,2. Přímé množiny cest se shodují s modely původního
DLX6 až na každou konkrétní hranu, nikoli jen v počtu.

Část (c): každý monotónní úsek prochází právě jedním diagonálním
vrcholem; n−1 disjunktních cest tedy použije všech n−1 takových
vrcholů. Obě trojúhelníkové rodiny lze nezávisle slepit, čímž vzniká
P_n² čtvercových rodin. Vytištěný čtvercový obrázek má 15 platných
disjunktních cest a právě jeden diagonální vrchol na každé. Všechna
pozadí a všechny cesty obou verzí se vektorově shodují.

Součin a velká hodnota mají F154; význam zdrojových okrajových hran
C044. Přesné počítání terminálů složeného ZDD souvisí s C041.
Knuthova třístránková poznámka `noncr-conj.pdf` z 6. února 2019
s dodatkem 8. února uvádí Beluhovovu bijekci; všechny tři stránky
byly přímo prohlédnuty. Samostatný Beluhovův publikovaný článek
jsme nezískali, kniha sama uvádí „to appear“.

Část (d): všech 64 číslic obou jezdcových obrázků se shoduje.
Osm vyznačených cest tvoří platné sestupné tahy jezdce, jsou disjunktní
a vedou do obráceného pořadí konců. Úplný počet 47356 a historické
náklady se nově nereprodukují, viz přesná vynechání.

## 262 — pokrytí, geometrie a primární články

Bez opakování přijímáme `TILING_ZDD_NOTES.md` a jeho otiskem chráněné
výsledky: 80 malých aztéckých a 15 malých šestiúhelníkových případů,
determinanty S₁₆/S₃₂, obecné konečné důkazy obou lineárních velikostí
ZDD, obě velká MacMahonova čísla a 16 přesných obdélníkových kontrol.
F058 (mez souřadnic) a F059 (koeficient asymptotiky) platí beze změny.

Nově přečteny všechny tři aztécké ilustrace: 72,136,200 domin,
vždy úplné disjunktní pokrytí. Tři šestiúhelníky mají 192,256,320
kosočtverců, rovněž úplná pokrytí. Každý má 64 svislých kosočtverců
v řádcích s počty 1,2,…,8,7,…,1. V obou verzích stejné vektorové
hrany a stejné pokrytí. Randallův diagram má F155; konkrétní
reverzní rovinný rozklad prostředního obrázku má F156.

Rovnoměrné vzorkování hotového ZDD: při rozvětvení vybírat každou
větev s pravděpodobností úměrnou počtu jejích dokončení. Rodiny L/H
jsou disjunktní podle přítomnosti aktuální možnosti, takže indukčně
má každé řešení stejnou pravděpodobnost. Platí i pro free ZDD,
jsou-li počty přesné. Není třeba náhodně přegenerovat ilustrace.

Obdélníkové inkluze pro pevné m dávají stejné exponenciální tempo:
rozdílové sloupce lze párovat svisle, pro n≥2m vložíme vnitřní
obdélník a rozšíříme do vnějšího. Jejich délky se liší od n pouze
o konstantu, takže po F059 stále platí Θ(μ_(2m)^n).
Konvexní rovnost počtů obou orientací trojúhelníků dává protilehlé
stejně dlouhé strany; takové hexagony mají explicitní pokrytí
odpovídající prázdnému krabicovému rozkladu. Nulové délky dovolují
degenerace. MacMahonův produkt a fixované řádkové počty zůstávají
podloženy starým důkazem a novou celou geometrií.

Primární zdroje byly získány a rozhodující stránky prohlédnuty:

- [Jockusch–Propp–Shor, verze v3](https://arxiv.org/pdf/math/9801068v3):
  věta 1 pro arktický kruh a příslušný obrázek. Tato stažená verze
  má 38 stran; nezaměňovat s v2 uvedenou v erratech E111.
- [Cohn–Elkies–Propp](https://arxiv.org/pdf/math/0008243), Proposition 13:
  mimo zvětšený kruh je pravděpodobnost nesprávné orientace
  exponenciálně malá. Unie přes O(n²) pozic zachovává rychlejší než
  polynomiální pokles, tedy knižní „q.s.“ s odstupem od hranice.
- [Cohn–Larsen–Propp](https://nyjm.albany.edu/j/1998/4-10.pdf), str. 141–142
  a Conjecture 6.2 na str. 162: krabicové rozklady a odpovídající
  domněnka exponenciální koncentrace mimo vepsanou elipsu.
- [Boutillier](https://arxiv.org/pdf/math/0607162): ověřena bibliografie
  a rozsah obecného bead modelu. Tento článek zde neoznačujeme za
  důkaz konečné hexagonální arktické elipsy.

Otevřeno: původní Grensing–Carlsen–Zapp 1980 nebyl získán;
nepublikované atribuce Ciucu/Randall/Klarner nejsou nezávisle uzavřené.
Přesný obecný dolní odhad Θ(n²) pro čas konkrétní implementace a
obecný důkaz exponenciálního růstu při řádkovém pořadí nejsou hotové.
Tyto mezery nejsou povoleným vynecháním dlouhého brute force.

## 263 — co tabulka dokládá a co zůstává otevřené

Všech 15 řádků bylo přečteno v obou zdrojích. Nová F157 dokládá
chybnou jednotku v neprovedeném a změněném kakuro, bez nového řešení
úlohy 431. Počty primárních/sekundárních položek v její horní mezi
jsou ty, které tabulka sama deklaruje; není to kontrola celého vstupu.

Bez opakování přijímáme dřívější počty 14772512 pro 16 dam,
987816 pro ukotvené MacMahonovy trojúhelníky a 137216/41280 pro
univerzální cykly, viz `QUEEN230_236_SOURCE_NOTES.md`,
`TRIANGLES124_126_NOTES.md`, `UNIVERSAL_CYCLES_NOTES.md`.
Staré kakuro 432 není totožné s kakuro 431 v tabulce. Počty 18/1
se proto nepovažují za již potvrzené starým `KAKURO_NOTES.md`.

Zbývá kontrola přesných vstupů tabulky a návazných úloh 271/274/431;
část (e) navazuje na dosud otevřené slovní úlohy. Část (f) vyžaduje
rozlišení degenerovaných řešení, která se dotýkají všech buněk.
Povolení vynechat náročné cenzy tyto zdrojové mezery neuzavírá.

## 264–265 — pořadí a duplicity

264: každé možnosti přiřadíme r(o), nejmenší její primární položku.
Podél H se r přísně zvětšuje, protože r(o) i menší položky jsou
pokryté. Podél L zůstává r stejné a klesá vstupní pořadí možnosti.
Pár (r(o),−index(o)) tedy přísně roste na každé neterminální hraně.
To dokazuje existenci společného pořadí i při sekundárních barvách.
Předčasný neúspěch pro prázdný sloupec pouze vrátí terminál 0.

265: každý uzel představuje neprázdnou rodinu dokončení pokrývajících
stejnou množinu primárních položek. Dvě stejné instrukce by tedy
vyžadovaly stejný primární zbytek, a bez sekundárních položek stejnou
signaturu. Cache má pro tuto signaturu jediný viditelný uzel; v jeho
řetězu se jednotlivé možnosti neopakují. Sekundární informace může
signaturu odlišit, aniž by změnila rodinu, a duplicity pak možné jsou.

Oba vytištěné protipříklady se sekundární položkou byly nové malé
testy. Pět možností má tři řešení; nezávislý model s první primární
položkou přesně reprodukuje všech šest vytištěných instrukcí a jejich
duplicitu. Původní DLX6 běží s MRV, proto jeho odlišný tvar u tohoto
příkladu není chyba. Druhý, 23možnostní příklad má 57 řešení a
duplicity i při MRV; rodiny původního DLX6 a deklarativního modelu
se shodují. Všechna dokončení jsou nezávisle validována.

[Nishino et al., AAAI 2017](https://ojs.aaai.org/index.php/AAAI/article/download/10662/10521)
byl archivován a přečten včetně Proposition 3/4 na str. 872.
Potvrzuje původní memoizační konstrukci a pevné pořadí. Rozsah
článku je str. 868–874; nevyvozujeme z něj atribuci Huangova
nezávislého objevu.

## Historie na hlavní straně 123

Shrnutí C/M/C$/Z odpovídá předchozím ověřeným algoritmům.
Knuthův archivovaný `dancing.tex` přímo připisuje ranou undo
konstrukci Hitotumatuovi a Noshitovi; Crossref potvrzuje metadata
jejich článku, ale původní plný text nebyl získán. `dlx2.w` dokládá
GDANCE z listopadu 2000, `dlx3.w` MDANCE ze srpna 2004.
[Autorův obsah Fascicle/Fun knihy](https://www-cs-faculty.stanford.edu/~knuth/fg.html)
potvrzuje kapitolu 38 Dancing Links. Nishinův plný článek ověřen.

Otevřené zůstávají přesné originály Rohl 1983, Hitotumatu–Noshita
1979 a podrobný algoritmus Pierce 1968/Garfinkel–Nemhauser 1969;
samotná vydavatelská metadata nepotvrzují všechny knižní podrobnosti
o pevném pořadí, bitových vektorech a odstraňování možností.
Rovněž Huangova časová osa 2007/leden 2017 není uzavřena.

## Errata, náklady a zachování evidence

Šest vrstev v `errata-search.json` a `errata-supplement.json` bylo
prohledáno podle obou číslování, témat i konkrétních čísel. Obě
relevantní stránky publikovaných errat byly přímo prohlédnuty.
E110 je známé k→m v 261(b), 11. července 2022: kniha opravená,
draft ne. E111 je bibliografická aktualizace arktického kruhu ze
7. dubna 2026 na v2, 42 stran. Naše oba zdroje uvádějí 44 stran;
starší errata hovoří o 46. Nyní získaná v3 má 38 stran; tyto verze
se neslévají. Aktuální PDF errat obsahuje položku, kterou dostupný
TeX ještě nemá. F154–F157 ani C043/C044 v prohledaných vrstvách nejsou.

Nové výpočty: 11 drobných nativních případů s nezávislým modelem
za 0,315 s; obě kompletní sady obrázků 1,157 s; doplňující tvrzení
a ověření otisků 0,060 s. Vše s nice 15. První pokus o model 261
již dokončil n=2, pak odhalil nepřístupné okrajové položky n=3;
přijatý n=2 byl při opravě znovu použit. Při vývoji geometrie byla
opravena parita barevných cest, offset draftu a projekce i−j.
Doplňující kontrola znovu použila již hotové doslovné malé cesty
po opravě normalizace kolineárních bodů. Úspěšné cenzy se neopakovaly.

Výslovná náročná vynechání, všechna `verified:false`:

1. 261(c): M₁₆ = 3803972 a 7 Gμ. P₁₆ je naopak nově přesně
   ověřené maticí; starý velký ZDD se nestaví.
2. 261(d): úplný počet 47356, C 278 Gμ / 760 Mμ po P,
   Z 92 Gμ / 7 GB a po P 940 Mμ / 90 MB. Obrázkový svědek ověřen.
3. 262: 2,2 Gμ pro n=32, empirický přechod výhodnosti MRV od n=18
   a velké řádkové běhy. Přijaté obecné lineární počty uzlů se nemění.
4. 263: historické C/Z memy, paměť a velikosti ZDD všech 15 řádků;
   nové úplné cenzy pentomin 2339/16146/24600/23619/60608/25943
   a kakuro 18/1. Dříve ověřené počty jsou výslovně oddělené výše.
   Přesná čísla jsou v obou archivovaných zdrojových stránkách
   `original-503.txt`, `original-504.txt` a jejich obrazech.

815 starých programů zůstává shodných s výchozími otisky. Tři nové
úspěšné checkery jsou dále zmrazené. Žádná nová dlouhá fronta.
Snímek vlastních zachovaných procesů má 17 procesů, všechny nice 15;
žádná priorita se nemusela měnit. Pokračování: 266 a generátory pokrytí;
zároveň převzít případné nově dokončené staré úlohy bez jejich restartu.
