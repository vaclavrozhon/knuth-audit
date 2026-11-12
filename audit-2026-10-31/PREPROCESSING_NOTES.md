# SAT 366–381: předzpracování, rekonstrukce a datové struktury

Kontrola 31. 10. 2026. Dva nové nálezy F049–F050 se týkají
odpovědi 376. Ostatní níže vymezené kontroly prošly.

## F049: při vyjmutí klauzule chybí LINK(c)←0

Odpověď 376, str. 623, definuje `LINK(c)≠0` právě tehdy, když
je klauzule na exploitation stack. Při vyjmutí ale provádí jen
`c←EXP; EXP←LINK(c)` a zapomíná `LINK(c)←0`. Následné zkrácení
ji proto nemůže vrátit do zásobníku: test LINK(c)=0 neprojde.

Malý příklad, bez počátečních jednotek a čistých literálů:

```
C = (a∨b∨c),  E = (a∨b∨d),
N = (¬a∨¬b∨¬d),  D = (a∨¬c).
```

Zvolme počáteční pořadí zásobníku C,E,N,D. První tři klauzule
nic nezmění. D zkrátí C na (a∨b). Nyní je ¬c čistý literál,
takže D zmizí. Tiskovaný postup už C nezařadí a fáze skončí
s C,E,N. Správný postup vrátí C, ta subsumuje E; čistý ¬d pak
odstraní N a čistý a odstraní C. Je hotovo ještě před eliminací
proměnných rezolucí.

Oprava je vložit nulování bezprostředně po `EXP←LINK(c)`, před
dalšími operacemi, které mohou klauzuli znovu změnit. Netvrdíme,
že chyba mění odpověď SAT/UNSAT; brání zamýšlenému opakování
zjednodušení a porušuje výslovný invariant datové struktury.
Přesný průchod obou variant je v `results/preprocessing.json`.

Znění vizuálně souhlasí s autorovým PS, str. 259. Ve veřejných
all4b/all4f6 není odpovídající oprava. Historické opravy této
stránky z července 2022 mění jiné řádky a naše PDF je již má.

## F050: opačný Iversonův test časové značky

Na str. 624, v pokračování 376, má v poslední podmínce být

`EXTRA(c)>>2 = SIZE(c) − [TIME(l)≠T]`,

nikoli `SIZE(c) − [TIME(l)=T]`.

U staré nezměněné klauzule C označuje `EXTRA(c)>>2` počet jejích
literálů s aktuální značkou T. Aby C mohla pomocí l zkrátit novou
klauzuli D, musí být aktuálně označeny všechny literály C\{l}
a také ¬l. Literál l sám může, ale nemusí být označen. Nutný počet
označených literálů v C je proto `|C|−1+[TIME(l)=T]`, což je
právě opravená pravá strana.

Tiskovaný test vynechá **každý** platný případ tohoto typu:
je-li l označen, požaduje o jeden méně než skutečný počet; není-li
označen, požaduje o jeden více. Ostatní okolní filtry tento
rozdíl nenapraví.

Konkrétně C=(a∨b∨c) a nová D=(¬a∨b∨c∨d), při aktuálních
značkách ¬a,b,c,d, dávají SIZE=3 a EXTRA=10. C může odstranit
¬a z D. Tisk ale požaduje 2=3, kdežto oprava požaduje 2=2.
Takové D vznikne eliminací x z (x∨¬a∨b∨d), (¬x∨c).

Pro ověření, že nejde jen o formálně možné značky, skript našel
a uložil úplný příklad na 9 proměnných a 29 klauzulích. Před
eliminací x₉ nemá jednotky, čisté literály, subsumpce ani
self-subsumption. Žádnou z proměnných 1–8 nelze eliminovat
downhill ani pomocí 369, a to ani po odstranění subsumovaných
rezolvent. Po eliminaci 9 existuje právě jedno zkrácení: C
odstraní ¬a z D. Tiskovaný časový filtr je přeskočí. Všechny
klauzule, počty a značky jsou v `results/preprocessing_stamps.json`.

Znění je stejné v PDF str. 624 a autorově PS str. 260. Oprava
není v prověřených all4b/all4f6. Kromě obecného argumentu bylo
vyčerpáno 1 280 relevantních kombinací značek pro délky 2–6;
oprava souhlasí přesně s množinovou podmínkou. Všech 40 platných
případů tiskovaný test chybně odmítne.

## Vyvrácené podezření D001: konce seznamu v 374(a)

Při kopírování dvou literálů například vzniknou odkazy
`S(1)=100, S(100)=101, p=101`. Seznam se po S prochází od
S(1) k p. Formulace „from p through S(1)“ však není chyba:
předchozí stránka 621 popisuje interval buněk zleva doprava,
zatímco S jsou levé odkazy. Uvolnění intervalu od p′ k p″ je tam
výslovně `S(p′)←AVAIL; AVAIL←p″`. Dosazení p′=p a p″=S(1)
je přesně správné. Podezření je vyřazeno, nikoli hlášeno.

## 366–370: rezoluce, erp a substituce

Eliminace x nahrazuje všechny dvojice klauzulí s opačnými
polaritami jejich netautologickými rezolventami. Pro každé
ohodnocení ostatních proměnných platí: nelze současně mít
nepravdivý kladný ocas a nepravdivý záporný ocas, protože jejich
rezolventa by byla nepravdivá. Proto fungují obě erp varianty
(161), včetně prázdných součinů u čistých proměnných.

U 368 jednotka subsumuje ostatní výskyty svého literálu; následná
rezoluce s jedinou zbývající kladnou klauzulí je přesně unit
conditioning a je vždy downhill.

V 369 chybějící rezolventy plynou hyperrezolucí z ponechaných
klauzulí. Ještě přímočařeji: dosazení ¬l=(l₁∨…∨lᵣ) splní
definiční klauzuli i všech r obrácených binárních implikací;
ostatní klauzule se změní právě v uvedené dva typy rezolvent.
Počet před vyřazením tautologií a duplicit je
`(q−r)+(p−1)r=(p−2)r+q`. Oprava žádná.

Příklad R v 366 dává přesně čtyři uvedené **nové** klauzule;
dvě nezasažené klauzule přitom zůstávají. Další eliminace dává
{34,¬3 4}; rekonstrukce nastaví x₄=x₂=1, x₁=0 pro obě hodnoty
x₃. První verze našeho testu zaměnila seznam nových klauzulí
za celou formuli; chyba testu byla opravena, není to nález knihy.
Rovnost dvou CNF v 370 platí na všech osmi ohodnoceních.

Známé erratum z 15. 11. 2025 na horním řádku str. 621 nahrazuje
indexy a,b indexy p,q. Je zapracováno a vedeno odděleně jako E005.

## 371–373: konkrétní refutace

V 371 souhlasí všech osm nových klauzulí po eliminaci 1 i osm
po eliminaci 8. Všech 18 vypsaných zkrácení má platného svědka.
Jedno potřebuje později uvedenou ¬3∨¬5, takže seznam zkrácení
čteme jako souhrn, ne jako striktní příkaz provést každé hned
v tiskovém pořadí. Opakovaný průchod seznamem stačí dvakrát.
Obě substituce 369, další rezolventy i závěrečný prázdný člen
souhlasí. To není nový nález.

Příklad 372 má dvě řešení a skutečně nepovoluje žádnou z
transformací 1–4 ani substituci 369. Každá proměnná se vyskytuje
v pěti klauzulích a její eliminace vyrobí šest rezolvent, které
nelze zredukovat subsumpcí. Optimalita velikosti příkladu je
otázka v knize; zde ji netvrdíme.

Pro 373 lze obecný indukční krok rozepsat přesně. Eliminace
x_im pro i<m má jedinou kladnou klauzuli M_im, a proto je
downhill. Vyrobí `M_i,m−1∨¬x_mk` pro k<m. Eliminace x_mm
dá M_m,m−1. Následná eliminace x_m,m−1 vytvoří
`M_i,m−1∨M_m,m−2`. Pomocí předchozích rezolvent z ní postupně
odstraníme všechny x_mk. Zbude M_i,m−1 a ta subsumuje ostatní
nové klauzule. Dostaneme přesně instanci s parametrem m−1.
Výčet m=2,…,15 ověřil 105 těchto kroků, 665 eliminací sloupců
a 3 640 zkrácení; všech 14 instancí skončí prázdnou klauzulí.

## 374–375: seznamy, signatury a časové značky

Přímý překlad merge a podmnožinového testu byl porovnán
s množinovým oraclem na všech 242 neprázdných netautologických
klauzulích do pěti proměnných. Prošlo 58 564 dvojic subsumpce,
196 020 dvojic s obráceným literálem a 65 610 rezolvent.
Při obrácení literálu v 374(c) zůstává seznam setříděn:
kódy opačných literálů jsou sousední a oba nemohou být v klauzuli.

Bloomův filtr nemůže odmítnout skutečnou podmnožinu. Modifikace
signatury v 374(c) může smazat i bity společné jiným literálům,
ale tím pouze zeslabí filtr; přesný test následuje. Známá oprava
374(c) z roku 2022 je v našem PDF již obsažena.

Detekce definice v 375 souhlasí s přímým hledáním všech potřebných
binárních klauzulí na 37 712 testech literálů. Záměrně byly použity
jen osmibitové signatury s častými kolizemi; správnost detekce na
jejich řídkosti nezávisí.

## 377–381: trojúhelníky a blokované klauzule

Konstrukce 377 dává pro každou hranu přesně šest klauzulí.
V implikačním grafu jsou nejdelší cesty délky tři, z úrovně 1
přes úrovně 2,3 do záporné úrovně 1, případně přes záporné
úrovně 3,2. Cesta z v₁ do ¬v₁ odpovídá uzavřené trojkrokové
procházce v jednoduchém grafu, tedy trojúhelníku. Jiné literály
se ke svému opaku nedostanou. Všech 1 099 grafů do pěti vrcholů
souhlasí s přímým hledáním trojúhelníků.

Erp v 378 mění l z nepravdy na pravdu jen tehdy, když všechny
ostatní literály odstraněné klauzule jsou nepravdivé. Každá
klauzule s ¬l pak obsahuje jejich pravdivý opak, takže zůstane
splněna. Ověřeno 197 523 rekonstrukcí pro 26 760 blokovaných
eliminací.

V 379 zkrácená formule implikuje původní, proto zpětná erp
není třeba. Pro opačný směr lze při a=b=c=0,d=1 nastavit a=1:
každá klauzule s ¬a má ¬b, ¬c nebo d a zůstane pravdivá.
Všech 882 přípustných kombinací doplňkové klauzule a modelu
souhlasí. Historické PS zde má starší chybnou erp větu, ale
známé erratum ze září 2022 a naše PDF už ji opravují.

V 380(a) ostatní klauzule skutečně implikují odstraňovanou
klauzuli. V (b) funguje `c←c∨(¬a∧¬b)`, ověřeno na všech 21
modelech zbývajících klauzulí; další klauzule bez ¬c změna
0→1 neporuší. U 381 zpětně provedené erp převedou každý řetězec
0…01…1 na konstantní řešení. Ověřeno všech 42 řetězců délky
2–8; obecně se postupně přepnou právě nuly před první jedničkou.

## Rozsah a reprodukce

`check_preprocessing.py` prověřil 4 952 formulí: všechny formule
do tří klauzulí na třech proměnných a 2 000 reprodukovatelných
pětiproměnných příkladů včetně vložených definic. Celkem 18 856
eliminací, 323 220 rekonstrukcí (161), 2 857 substitucí a
25 936 jejich erp rekonstrukcí. Všechny aserce prošly po opravě
výše přiznané chyby testu 366.

`check_preprocessing_traces.py` ověřuje 371 a 373;
`check_preprocessing_stamps.py` filtr F050 a celý dosažitelný
příklad jednoho eliminačního kola. Odpověď 376 obsahuje i další
implementační pokyny; celý preprocessor včetně všech možných
propletení zásobníků a recyklace buněk zde nebyl implementován.
Proto má 376 stav partial, ne úplnou certifikaci algoritmu.
