# SAT 387–390: vložení grafu, cesty a souvislost

Kontrola 31. 10. 2026. Nálezy F051–F052 se týkají odpovědi 390.
Konstrukce 387 a zbývající části 390 jsou správné v níže uvedeném
rozsahu. Příklad s nápisem v úloze 389 zde zatím není ověřen.

## F051: procházka přesné délky místo cesty délky nejvýše k

V odpovědi 390(d), str. 627, jsou počáteční jednotka (s₀),
implikace `v_j→w_(j+1)` pro každou orientaci hrany a závěrečná
jednotka (¬t_k). To vynucuje vrcholy dosažitelné procházkou
**přesně** j kroků. Kniha ale tvrdí dolní mez pro vzdálenost ≤j.

Stačí jediná hrana s—t a k=2. Vzdálenost je 1, takže podle
zadání má být formule nesplnitelná. Ve skutečnosti ji splňuje

| vrstva j | s_j | t_j |
|---|---|---|
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |

Všechny čtyři implikace i obě jednotky jsou splněny. Problém
se projevuje zvlášť v bipartitních grafech jako chyba parity.

Jednoduchá oprava je nahradit (s₀) součinem všech jednotek
`(s₀)∧(s₁)∧…∧(s_k)`. Cesta délky d≤k pak může začít ve
vrstvě k−d a vynutí t_k. Naopak při d(s,t)>k je modelem
`v_j=[d(s,v)≤j]`. Tím je oprava dokázána pro libovolný graf,
včetně s=t a k=0. Přibude jen k jednotek; pro graf s alespoň
jednou hranou zůstává počet klauzulí O(km), bezhranové případy
jsou rozhodnutelné přímo.

Nejde o přehlédnutí známé opravy: celý text 390 byl nahrazen
v erratu k Fascicle 6 z 9. 2. 2016. **Tatáž chyba je i v této
náhradě**, na str. 16 současného all4f6, a přešla do našeho 4B.
Starší autorský PS str. 263 má vedle toho starý indexový překlep;
náhrada opravila index na j, ale tento problém neodstranila.
V all4b nebyla další oprava nalezena. Vykresleny a přečteny byly
PDF str. 627, původní PS a oficiální náhradní odpověď.

## F052: v části (b) jsou potřeba i pomocné proměnné

Úvod odpovědi 390 na str. 626 tvrdí, že části (b),(e),(f) používají
jen n proměnných v=[v∈H]. Část (b) však pro omezení stupně
výslovně používá Sinzovy klauzule (18),(19). Ty zavádějí
`(d−r)r` pomocných proměnných pro d vstupů a horní mez r.
Pro vnitřní vrchol stupně d≥3 a r=2 jich je 2(d−2); například
stupni 4 odpovídají čtyři pomocné proměnné navíc.

Oprava: ve větě o „just n variables“ ponechat pouze (e),(f),
případně u (b) výslovně připustit O(m) pomocných proměnných.
Lineární počet klauzulí se tím nemění a samotná myšlenka (b)
je správná. Nejde o tvrzení, že by bez pomocných proměnných
nešlo jiným způsobem rozhodnout existenci cesty; nález se týká
počtu proměnných v konkrétně uvedené konstrukci.

Stejná věta je v autorském PS str. 262 i v náhradě odpovědi
z roku 2016. Sinzova konstrukce pro r=2 byla nezávisle ověřena
na všech 508 ohodnoceních vstupů velikosti 2–8, včetně počtu
pomocných proměnných.

## 387: injektivní vložení

Binární záporné klauzule zajišťují, že každý zdrojový vrchol
dostane nejvýše jeden obraz a dva zdrojové vrcholy nemají stejný
obraz. Pro každou zdrojovou hranu vybere dlouhá klauzule alespoň
jednu pomocnou proměnnou; ta vynutí odpovídající dvojici obrazů
spojených hranou. Bez izolovaných zdrojových vrcholů tak má každý
vrchol alespoň jeden obraz. Injektivní vložení naopak dává model
tím, že vybere odpovídající hranu pro každou zdrojovou hranu.
Omezení podle stupňů je nutnou podmínkou vložení a neztrácí řešení.

U cílové hrany se musí použít obě orientace. Kniha na rozdíl od
zdrojových hran neukládá u′<v′, takže její zápis tomuto použití
odpovídá. Není to další nález.

Větu „můžeme předpokládat, že nejsou izolované vrcholy“ lze
realizovat takto: nejprve odmítnout |V(G)|>|V(G′)|; pak odstranit
izolované vrcholy obou grafů a testovat vložení zbylých částí.
Obrazy neizolovaných zdrojových vrcholů nemohou být izolované;
odstraněné zdrojové vrcholy lze nakonec umístit do libovolných
volných cílových vrcholů, protože byl zachován původní početní
test. Pouhé zapomenutí obou množin izolátů bez tohoto testu by
nebylo správné; zde je to explicitní součást redukce.

Bylo vygenerováno SAT kódování pro všech 5 776 dvojic grafů
do čtyř vrcholů a výsledek porovnán s přímým výčtem injekcí.
V 1 954 případech byla navíc nezávisle ověřena varianta bez
filtru podle stupňů. Vše souhlasí.

## 388: tři redukce

K-klika je právě vložení K_k. K-obarvení dává vložení do úplného
k-partitního grafu s n vrcholy v každé části: vrcholy stejné
barvy umístíme injektivně do jedné části. Naopak části určují
obarvení. Hamiltonovská kružnice je vložení C_n při n=|V(G)|.
Poslední určení n doplňuje známé erratum z 15. 11. 2025.
U kružnic se používá obvyklá konvence jednoduchých grafů n≥3.

## 390(a),(b),(c),(e),(f)

V (a) implikace z v_(j+1) do některého souseda v předchozí
vrstvě při v≠s a počáteční zákazy nesprávných vrcholů dávají
indukcí `v_j≤[d(s,v)≤j]`. Proměnné s_j pro j>0 nejsou zakázány;
přiřazení podle vzdáleností splní všechny klauzule. Na rozdíl
od (d) je tato konstrukce správná. Část (c) jen vyžaduje všechny
vrcholy ve vrstvě n−1 a je proto ekvivalentní souvislosti.

V (b) tvoří nejkratší cesta indukovanou cestu, takže její množina
vrcholů H má předepsané stupně. Naopak komponenta H obsahující
s musí obsahovat i t, protože jsou to jediné dva vrcholy lichého
stupně. Při s=t stačí H={s}. Přídavné kružnicové komponenty
nevadí. Stupňové omezení je správné; F052 se týká jen počtu
pomocných proměnných v lineárním kódování.

Implikace (e) propagují pravdu ze s do celé jeho komponenty,
takže (¬t) způsobí spor právě při dosažitelnosti. V (f) záporná
dlouhá klauzule požaduje vrchol mimo tuto komponentu. Je tedy
splnitelná právě pro nesouvislý graf. Pro n=1 je dlouhá klauzule
prázdná a správně způsobí spor.

## Rozsah kontroly

`check_graph_encodings.py` obsahuje obecný SAT rozhodovač,
nezávisle porovnaný s úplnými pravdivostními tabulkami všech
512 dvouproměnných CNF. Grafový oracle používá BFS, úplný výčet
injekcí a explicitní množiny vrcholů dosažitelných přesným
počtem kroků. Pro všechny jednoduché grafy na 1–5 vrcholech,
všechny dvojice konců a limity 0,…,n+1 bylo provedeno:

- 557 217 kontrol kódování omezené cesty (a), tiskovaného (d)
  a opraveného (d);
- 53 410 kontrol neomezené cesty (b),(e);
- 10 810 kontrol souvislosti (c),(f).

Všechna opravená tvrzení prošla. Tiskované (d) dává 27 929
nesprávných odpovědí pro podmínku vzdálenosti ≤k, ale vždy
přesně souhlasí s podmínkou procházky délky k. Výsledky jsou
v `results/graph_encodings.json`. Vyčerpání malých grafů
doplňuje výše uvedené obecné důkazy, nenahrazuje je.
