# Stopy, násobení, dělení, determinant a pyramidy

Kontrola 31. 10. 2026, SAT 323–339. Obecné algoritmy a identity níže
prošly nezávislou kontrolou; nový nález F036 se týká konkrétního
ilustračního rozkladu v zadání 339(b).

## Nezávislý model a rozsah

Oracle nepoužívá algoritmus skládání pater. Pro danou délku vypíše
všechna slova a spojí každou dvojici, která se liší jedinou dovolenou
výměnou sousedních komutujících písmen. Union-find dává přesné třídy
equivalence a jejich lexikografická minima.

Druhý model vytváří částečné uspořádání výskytů: dřívější výskyt je
předchůdcem pozdějšího, pokud jde o stejný nebo sousední vrchol grafu.
Patro výskytu je délka nejdelšího řetězce předchůdců. Třetí model
implementuje přímo knižní operace nad patry a bitovými teritorii.
Pro libovolný graf jsou teritoria realizována soukromým bitem vrcholu
 a společným bitem každé jeho hrany.

Na všech grafech na 1..4 písmenech a všech slovech délky 0..5 prošlo
**90 404 slov**, tvořících **39 093 stop**. Patrové reprezentace souhlasí
přesně s třídami sousedních výměn. Algorithm T se shoduje s celým
uspořádaným výstupem oraclu ve všech **450** případech graf/délka.

## 323–326: konkrétní příklad, orientace a obracení

Pro cestu a−b−c je předchůdcem ccb slovo cbc. Dvě topologická
uspořádání stejného částečného uspořádání lze převádět sousedními
výměnami nesrovnatelných prvků; to přesně odpovídá komutujícím písmenům.
V příkladu bcebafdc z (136) přímé procházení všech sousedních výměn
najde **105** různých slov, jak uvádí odpověď 324.

U permutačních stop orientujme každou hranu od dřívějšího vrcholu
k pozdějšímu. Orientace je acyklická a výměny komutujících písmen ji
nemění. Obráceně její topologická uspořádání tvoří jedinou stopu.
Počty prošly pro všech 75 grafů na nejvýše čtyřech vrcholech,
přímým vyzkoušením všech 760 orientací (včetně cyklických).
Obrácení slov v 326 respektuje každou elementární komutaci, protože
graf je neorientovaný; proto respektuje celou ekvivalenci.

## 327–329: správnost patrových operací

Při násobení vkládáme písmena druhé stopy v topologickém pořadí.
Nejvyšší již vložené kolidující písmeno určuje přesně nejnižší možné
patro nového písmene. Sestup shora v odpovědi 327 tedy implementuje
maximální výšku předchůdce plus jednu. Různá písmena téhož vstupního
patra komutují, takže jejich vnitřní pořadí nehraje roli.

Při pravém dělení je poslední odstraňované písmeno b přípustné právě
tehdy, když je maximálním prvkem stejného typu v aktuálním uspořádání.
První kolize při sestupu shora buď najde b, nebo zjistí překážku.
Pokud odstranění b vyprázdní celé patro, toto patro musí být nejvyšší:
jinak by každý řetězec do bezprostředně vyššího patra musel jít přes
jeho jediný prvek b, který by pak nebyl maximální. Proto je knižní
snížení výšky v tomto případě správné. U prázdné stopy implementace
přímo vrací neúspěch, má-li se ještě odstranit neprázdný faktor.

Při levém dělení může být odstraněn jen zdroj, tedy prvek spodního
patra. Odstranění jednoho zdroje zkrátí nejdelší řetězec do libovolného
zbývajícího prvku nejvýše o jednu. Stačí proto postupně přesouvat dolů
písmena, která ztratila poslední podporu v předchozím patře.
Jestliže se patro vyprázdní, všechna vyšší patra lze posunout o jedno;
jestliže se nepohnulo žádné písmeno, další patra se už nezmění.
To přesně odpovídá příznaku c a smyčce v odpovědi 329.

Pro všechny dvojice stop do délky 4 na nejvýše třech písmenech a
do délky 3 na čtyřech písmenech se vytvořila úplná tabulka přípustných
součinů. Obě dělení byla porovnána s touto tabulkou, včetně všech
neúspěchů. Prošlo **18 250 součinů** a **552 064 dělení**.

Pozor na OCR: smyčka v 329 skutečně používá `U_(j−1)≠0` a `c≠0`,
nikoli rovnosti, které vypadly z textového přepisu. V 336(b) jsou
podmínky `β=ε` a `α=ε`. Originální stránky 613–614 je potvrzují;
nejde o chyby knihy.

## 330–334: teritoria a kanonický výčet

Konstrukce T(v)={v}∪{incidentní hrany} dává neprázdná teritoria se
správnými průniky. Dvouprvková teritoria jsou právě hrany nějakého
multigrafu, jehož hranový graf je původní graf. Jednoprvková teritoria
lze doplnit vlastním soukromým bodem. Nezávislé množiny pak odpovídají
párováním; reálnost příslušných kořenů plyne z váženého involučního
polynomu 341 po limitním přechodu k nulovým vahám chybějících hran.

V 331 se každý výskyt ac může rozdělit na dvě písmena nebo brát jako
jeden faktor. Výskyty ac se nepřekrývají, takže pro k>0 dostaneme
2^k rozkladů se stejně mnoha kladnými a zápornými znaménky.
V 332 slovo cab ukazuje, proč nestačí zakázat pouze lokální inverze.

Pro nekomutativní identitu 333 zafixujme slovo délky n>0. Nechť s
je poslední pozice sousední dvojice, která patří do D (nebo 0),
a r první pozice dvojice, která do D nepatří (nebo n). Přípustné
místo řezu k musí splňovat s≤k≤r. Buď žádné není, nebo má slovo
všechny D-dvojice před všemi ne-D-dvojicemi a r=s+1. V tom případě
jsou přesně dva řezy s opačným znaménkem. To dokazuje identitu
koeficient po koeficientu. Přímá kontrola prošla **186 858 slov**
pro všechny digrafy včetně smyček na nejvýše třech písmenech.

Kritérium v 334 říká, že menší pozdější písmeno nesmí projít vlevo
přes celý blok komutujících písmen a vytvořit menší slovo.
V T5 se proto jde zpět přes menší komutující písmena, až se najde
blokující kolize nebo nepřípustné větší písmeno. T3–T5 najdou nejpravější
možné zvýšení platného prefixu. T6 doplní nejmenší suffix: nově volené
písmeno je nejvýše tak velké jako předchozí a musí s ním kolidovat,
čímž se zablokují případné překážky ještě více vlevo. Každý krok tedy
dává bezprostředně další kanonické slovo, bez opakování a vynechání.
Úplné porovnání s oraclem je popsáno výše.

## 335: krátký nezávislý důkaz determinantového vzorce

Nechť `B_uv=[u≥v nebo u sousedí s v]` a `A=B diag(a_v)`.
V rozvoji det(I−A) je koeficient monomu `Π_(v∈S) a_v` roven
`(−1)^|S| det(B_S)`. Stačí tedy dokázat, že tento hlavní minor je
1 pro nezávislou množinu S a 0 jinak.

Pro nezávislou S je B_S dolní trojúhelníková s diagonálou 1.
Obecně napišme B_S=J−C, kde J má samé jedničky a C je přísně horní
 trojúhelníková matice nehran. Kdyby všechna políčka C bezprostředně
nad diagonálou byla 1, tranzitivita nehran z předpokladu úlohy by
vynutila, že S je nezávislá. Pro závislou S proto některé z těchto
políček chybí. Jediný možný nenulový minor C řádu |S|−1 (první
|S|−1 řádků, poslední |S|−1 sloupců) má determinant roven součinu
právě těchto políček. Je tedy nula; hodnost C je nejvýše |S|−2.
Proto hodnost J−C je nejvýše |S|−1 a det(B_S)=0, jak bylo potřeba.

Důkaz platí symbolicky pro libovolný počet vrcholů a všechna vážení.
Kontrola přesnou celočíselnou eliminací prošla **12 130 hlavních
minorů** všech **407** vhodně uspořádaných grafů na nejvýše pěti vrcholech.

## 336–338: operace s grafy a omezené zdroje

Nezávislá množina v disjunktním sjednocení je nezávislá volba v obou
grafech, proto M se násobí. V úplném spojení leží neprázdná nezávislá
množina jen na jedné straně, proto `M=M_G+M_H−1`.
Při nahrazení vrcholu klikou lze zvolit nejvýše jeden klon; nahrazení
jeho proměnné součtem proměnných klonů tedy dává správný polynom.

V součinu `M_(G\A) M_G^(-1)` může nezávislý levý faktor dané stopy
obsahovat libovolnou podmnožinu jejích zdrojů mimo A. Koeficient je
součet znamének těchto podmnožin, tedy 0, pokud existuje zdroj mimo A,
a 1 jinak. Tím je dokázána identita 338 i správné pořadí faktorů.
Obrácení slov dává analogii pro pravé faktory a koncové prvky.

## 339: faktorizační věta a F036

Pyramidou s vrcholem na konkrétním výskytu je množina všech jeho
předchůdců včetně jeho samotného. Jde o ideál, tedy levý faktor,
a je to jediný levý faktor s tímto jediným maximálním prvkem.
Osm takových pyramid v 339(a) souhlasí s přímým výpočtem.

Pro označenou stopu vezměme nejmenší zbývající označení a odstraňme
jeho pyramidu. Vrchol má nejmenší označení v této pyramidě a další
vybrané vrcholy mají rostoucí označení. Každý rozklad předepsaného
typu musí začít právě touto pyramidou, proto je rozklad jednoznačný.

### F036: prostřední faktor příkladu není pyramida

V zadání na str. 346 je vytištěno

`b₆c₂e₄b₇a₈f₅d₁c₃ = b₆c₂e₄d₁ · b₇a₈c₃ · f₅`.

Graf kolizí je cesta a−b−c−d−e−f. V prostředním faktoru b₇a₈c₃
komutují a₈ a c₃, ale oba kolidují s b₇. Má tedy **dva maximální
prvky**, a₈ a c₃, a není pyramidou. Správný rozklad je

`b₆c₂e₄d₁ · b₇c₃ · f₅ · a₈`.

Vrcholová označení jsou 1,3,5,8 a všechny čtyři faktory jsou pyramidy.
Chyba se týká pouze příkladu; obecná věta i odpověď 339(b) jsou správné.
Stejné znění je v autorově Pre-Fascicle 6A na str. 162. Obě stránky
byly vizuálně zkontrolovány; odpovídající oprava není v úplných erratech
4B ani Fascicle 6. Fyzický výtisk dosud neověřen.

### Počítání a logaritmus

Po rozdělení n označení do l skupin a volbě pyramid v jednotlivých
skupinách je pořadí jednoznačně určeno rostoucími minimy skupin.
Proto počet rozkladů s l faktory je `n![z^n]P(z)^l/l!`, kde
`P(z)=Σp_n z^n/n`. Sečtením dostáváme T=exp(P), a jelikož T=1/M,
platí `−ln M=Σp_n z^n/n` v komutativní algebře.

Výčet prošel **121 017 označených stop** a 165 koeficientů rozdělení
podle počtu faktorů. Neoznačené i vážené generující funkce stop a
pyramid prošly dalších **1500** přesných kontrol na výše uvedených
grafech. Váhy písmen byly 1 a nezávisle 2,3,4,5.

Upozornění v odpovědi 339(e) je správné: v nekomutativní algebře má
bac v příkladu cesty a−b−c koeficient `2/3−1/2=1/6` v −ln M,
ale bac má dva koncové prvky a není pyramidou. Komutativní interpretace
je tedy podstatná, nikoli jen formalita.

## Soubory

`check_traces.py`, `results/traces.json`, `check_trace_examples.py`,
`results/trace_examples.json`. Originální znění algoritmů:
`images/local-lemma-632.png`, `images/traces-633.png`,
`images/traces-634.png`. Doklad F036: `images/vol4b-p346.png`,
`images/fasc6a-p162.png`. Žádné hlášení nebylo odesláno.
