# §7.1.1–6 a 7: asociativita, volný systém a reverzibilita

6. listopadu 2026, X0061. Zadání p80/file97 a odpověď p535/file552
byly čteny z původních images/file097.png a images/proof-file552.png.
Žádný matematický program ani enumerace. Obecný algebraický dodatek
není ověřován jen na booleovských operacích.

## P0562: všechny asociativní booleovské operace, úloha 6(a)

Konstanty 0,1 i projekce x,y jsou asociativní: obě uzávorkování
vrátí tutéž konstantu, první vstup, resp. poslední vstup.
AND,OR,XOR a ekvivalence mají již přesné argumenty P0515/P0517
v proof-028, které se přebírají. To dává osm uvedených operací.

Pro každou ze zbývajících osmi je níže konkrétní svědek. Vpravo
L=f(f(x,y),z) a R=f(x,f(y,z)); vše jsou skutečné bity, nikoli OCR
ztracené komplementy.

| tabulka f | funkce | xyz | L | R |
|---|---|---|---:|---:|
| 0010 | x∧¬y | 101 | 0 | 1 |
| 0100 | ¬x∧y | 101 | 1 | 0 |
| 1000 | NOR | 001 | 0 | 1 |
| 1010 | ¬y | 000 | 1 | 0 |
| 1011 | x∨¬y | 000 | 1 | 0 |
| 1100 | ¬x | 000 | 0 | 1 |
| 1101 | ¬x∨y | 000 | 0 | 1 |
| 1110 | NAND | 001 | 0 | 1 |

Tím je klasifikace úplná; nejde o vzorek pozitivních operací.

## P0563: obecná identita opravdu implikuje asociativitu

Nechť na libovolné množině je definována binární operace ⋆ a platí

    (a⋆b)⋆(b⋆c) = a⋆c                         (E)

pro všechna a,b,c. V této části **asociativitu zatím nepředpokládáme**.
Všechny závorky jsou proto podstatné. Odvodíme tři pomocné rovnosti:

    (a⋆b)⋆((c⋆b)⋆d) = (a⋆c)⋆d              (A)
    (a⋆(b⋆c))⋆(b⋆d) = a⋆(c⋆d)              (B)
    (a⋆b)⋆(c⋆d) = (a⋆c)⋆(b⋆d).             (C)

Pro (A) nahraď a⋆b výrazem (a⋆c)⋆(c⋆b), což je (E) na a,c,b.
Pak použij (E) s trojicí a⋆c, c⋆b, d. Dostaneš pravou stranu (A).

Pro (B) nahraď b⋆d výrazem (b⋆c)⋆(c⋆d), pak použij (E)
s trojicí a, b⋆c, c⋆d. Neproběhla žádná změna závorek navíc.

Pro (C) nahraď c⋆d výrazem (c⋆b)⋆(b⋆d) a použij (A)
s posledním parametrem b⋆d.

Nyní pro libovolná a,c,d:

    (a⋆c)⋆d
      = (a⋆c)⋆((c⋆c)⋆d)                    podle (A), b=c
      = (a⋆(c⋆c))⋆(c⋆d)                    podle (C)
      = a⋆(c⋆d)                            podle (B), b=c.

To je asociativita. Jsou to přesně tři kroky vytištěného důkazu,
s explicitními substitucemi. Platí pro libovolnou kardinalitu a bez
dalších axiomů; konečnost nebo booleovská doména nebyly použity.

## P0564: úloha 6(b), přesně šest booleovských operací

Podle právě dokázaného lemmatu může (E) splňovat pouze některá
z osmi asociativních operací. AND ji nesplní pro xyz=101:
levá strana je 0, pravá 1. OR ji nesplní pro xyz=010:
levá strana 1, pravá 0.

Obě konstanty a obě projekce (E) splňují přímo.
Pro XOR v F₂ je (x+y)+(y+z)=x+z. Pro ekvivalenci je
1+(1+x+y)+(1+y+z)=1+x+z, což je také přesně pravá strana.
Zůstává tedy vytištěných šest: 0, levá/pravá projekce, XOR,
ekvivalence a 1. Osm negativních řádků úlohy (a) se znovu netestuje:
vylučuje je obecná implikace (E)⇒asociativita.

## P0565: normální formy všech slov, nikoli jen horní odhad

Teď už lze závorky vypouštět. (E) a (C) říkají

    a b b c = a c,                 a b c d = a c b d.

U slova délky alespoň 2 zachovej první a poslední písmeno.
Libovolná dvě sousední vnitřní písmena lze vyměnit druhou rovností:
neprázdný prefix je a a neprázdný suffix d. Bublinkovým přesouváním
tak vnitřní písmena uspořádáme podle indexů; počet inverzí klesá.
Dvě sousední stejná vnitřní písmena lze vymazat první rovností,
opět s neprázdným prefixem a suffixem. Délka klesne o 2.
Nakonec zůstanou právě indexy s lichou vnitřní násobností.

Každé slovo je proto rovno buď jedinému x_i, nebo právě některému
kandidátu na normální tvar

    x_i x_j1 … x_jr x_k,
    r≥0, 1≤i,k≤n, 1≤j1<…<jr≤n.

Vnitřní index smí být stejný jako i nebo k; jejich násobnost se
nesmí zahodit spolu s chráněným prvním/posledním písmenem.
Prázdný vnitřek dává slovo délky 2, ne jediný generátor.
Tím je počet tříd nejvýše n+n²2ⁿ. K rovnosti je třeba následující
oddělující model; samotná redukce nestačí.

## P0566: explicitní model odlišuje všechny normální tvary

Pro n≥1 vytvoř množinu tvořenou dvěma disjunktními druhy prvků:

- jednotlivé atomy A_i pro 1≤i≤n;
- trojice (i,P,k), kde 1≤i,k≤n a P je libovolná podmnožina {1,…,n}.

Každému prvku v přiřaď první index l(v), poslední r(v) a paritní
množinu p(v). Pro atom A_i jsou l=r=i a p={i}; pro trojici
(i,P,k) jsou l=i, r=k a p=P. Definuj pro všechny prvky

    u⋆v = (l(u), p(u) △ p(v), r(v)),

kde △ je symetrický rozdíl. Výsledkem je vždy trojice, nikdy atom.

Tato operace je asociativní: obě uzávorkování mají první index
l(u), poslední r(w) a paritu p(u)△p(v)△p(w).
Také

    (u⋆v)⋆(v⋆w)
      = (l(u), p(u)△p(v)△p(v)△p(w), r(w))
      = u⋆w.

Model tedy splňuje původní (E). Vyhodnocení normálního slova
x_i x_j1…x_jr x_k v něm je

    (i, {i} △ {j1,…,jr} △ {k}, k).

Pro pevné i,k určuje paritní složka jednoznačně vnitřní množinu;
různé i,k se liší koncovými složkami. Každý jednopísmenný term
zůstává odlišným atomem. Všechny vypsané normální formy jsou tudíž
navzájem různé alespoň v tomto modelu a žádná další rovnost mezi
nimi nemůže být důsledkem (E).

Naopak každá trojice modelu je generovaná atomy: pro (i,P,k)
vezmi vnitřní množinu P△{i}△{k} a její indexy ve vzestupném pořadí.
Tím je přesně n+n²2ⁿ prvků. Redukce P0565 a rozlišení modelem
navíc dávají univerzální vlastnost volného systému: libovolné
přiřazení generátorů v jiné algebře splňující (E) se rozšíří
vyhodnocováním slov; všechny zde použité redukce jsou její platné
identity a žádné další ztotožnění nebylo vnuceno.

Pro n=1 tedy vzniknou tři odlišné prvky x,xx,xxx, s pravidlem
x⁴=x². Pro n=2 je počet 18; není to spor s šestnácti booleovskými
funkcemi, protože volný systém je v celé třídě algeber (E), nikoli
pouze v jedné dvouprvkové booleovské algebře. Při n=0 nejsou žádné
neprázdné termy; nulový počet odpovídá prázdnému systému, pokud
jej příslušná konvence dovoluje. Knižní netriviální konstrukce
používá n≥1.

## P0567: úloha 7, obě implikace a úplnost seznamu

Požadavek je f(x,y)=z právě tehdy, když f(y,z)=x.
Dosazením z=f(x,y) plyne nutná identita f(y,f(x,y))=x.
Pro každé pevné y je proto zobrazení x↦f(x,y) injektivní:
rovné výstupy by po aplikaci f(y,·) daly rovné vstupy.
Na B jsou jen dvě permutace, tedy f(x,y)=x⊕a_y pro nějaká a₀,a₁.

Kdyby a₀=a₁=a, byla by f(y,f(x,y))=y⊕a nezávislá na x,
což není možné. Musí proto a₁=1−a₀ a
f(x,y)=x⊕y⊕c pro c∈{0,1}: právě XOR a ekvivalence.

U obou funkcí platí i celá požadovaná ekvivalence:
x⊕y⊕c=z právě tehdy, když y⊕z⊕c=x, prostým vyrušením
dvou kopií y a c. Tím je doložena i opačná implikace, nikoli
pouze nutná identita z odpovědi. Tvrzení o ekvivalentním testu
zde patří ke klasifikaci dvouprvkových operací; není neoprávněně
rozšířeno na libovolné nekonečné systémy.

## Meze a pokračování

Schröderova a Jevonsova historická atribuce se samostatně
neověřovala. V pěti relevantních vrstvách errat je u odpovědi 7
známá změna následného odkazu §7.2.3 na §7.2.2.1 (19. 4. 2020);
nejde o nový nález ani o změnu právě dokázané algebry.
Všechny matematické dodatky odpovědí 6–7 jsou nyní doloženy.
P80 i p535 zůstávají neuzavřené kvůli úlohám 8 a dalším.
Další úloha 8: kompletní klasifikace levé distributivity a číslo 92.
