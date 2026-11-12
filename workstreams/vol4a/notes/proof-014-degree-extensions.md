# Doplňování stupňů: §7–108 až 111

6. listopadu 2026. Původní zadání file060.png, odpovědi proof-file545.png.
Samostatné argumenty bez programu. Nový F0003 je vyčleněn; známá errata
odpovědi 108 a d=2k>0 v odpovědi 110 se nepovažují za nové nálezy.

## 108: orientované jednoduché grafy s povolenými smyčkami

Jde o 0/1 matici s předepsanými řádkovými a sloupcovými součty.
Pro další sloupec požadované váhy r vyber r největších kladných zbytkových
řádkových součtů a sniž je o 1. Je-li r větší než počet kladných součtů
nebo některý řádkový součet větší než počet zbývajících sloupců,
realizace neexistuje. Předem lze ověřit rovnost celkových součtů;
všechny nulové zbytky se přímo dokončí nulami.

Greedy krok zachovává možnost realizace. V libovolné realizaci
předpokládejme, že poslední sloupec obsahuje 1 v nevybraném řádku j,
ale 0 ve vybraném řádku i s x_i≥x_j.
Mimo tento sloupec má i celkem x_i jedniček a j jen x_j−1;
existuje proto jiný sloupec k s a_ik=1,a_jk=0.
Přepni obdélník řádky i,j / sloupce poslední,k z 01/10 na 10/01.
Všechny řádkové i sloupcové součty zůstanou a poslední sloupec se
přiblíží greedy volbě. Opakováním dosáhneš celé greedy množiny,
potom sloupec smaž a použij indukci. Smyčky jsou přípustné,
takže žádná diagonální buňka není zakázaná.

To ověřuje matematickou konstrukci odpovědi a výměnový argument
analogický Corollary H. Uvedené změny H dávají tuto konstrukci
v pozitivních stavech: n je nyní počet zbývajících sloupců, nikoli
počet kladných řádků; zdrojové řádky se při smazání cílového sloupce
neodstraňují. Známá oprava z 23. 5. 2011 přidává guard j>0 před
čtení m=c_t a vytvoření oblouku. Doslovná inicializační substituce H1
a nevyužité čtení c_0 ve stavu d_1=0<n nejsou zde plně formalizovány;
tato implementační mezera zůstává partial, není vydávána za nový nález.
Správná výše uvedená konstrukce tyto nulové stavy řeší přímo.

## 108: konjugovaná majorizační charakterizace

Nutná rovnost součtů je jasná. Pro k největších sloupcových součtů
máme Σ_(j≤k)s_j≤Σ_i min(k,r_i)=Σ_(j≤k)c_j,
kde c je konjugát řádkových stupňů r.
Naopak začni Ferrersovou 0/1 maticí s r_i jedničkami na začátku
každého řádku. Její sloupcové součty jsou právě c.
Jestliže c majorizuje požadované seřazené s, rozlož přechod c→s
na jednotkové přesuny podle již dokázaného rozkladu v proof013.
Pro přesun z většího sloupce i do menšího j existuje řádek
s hodnotami 1,0 v těchto sloupcích; přesuň tuto jedničku.
Řádkové součty zůstanou, sloupcové se změní přesně požadovaným způsobem.
Nakonec permutuj sloupce do původního pořadí vstupních stupňů.
To je úplný důkaz tištěné charakterizace; odkaz na budoucí úlohu
7.2.1.4–57 zde nemusí být přijímán jako neověřený vstup.
Historický Fulkersonův výsledek pro zakázané smyčky nebyl rozebírán.

## 109: bipartitní varianta

Na levé části dej požadované out-degree a nulové in-degree, na pravé
požadované in-degree a nulové out-degree. Maticová konstrukce 108 pak
může vytvořit oblouk jen zleva doprava. Smyčky jsou automaticky nemožné
a zapomenutí orientace dává požadovaný jednoduchý bipartitní graf.
Všechny potřeby částí i případná nerovnost součtů jsou kontrolovány
stejným řádkově-sloupcovým argumentem.

## 110: správné části a oprava F0003

D=0 dává prázdný graf. Nechť p vrcholů má stupeň d a q vrcholů d−1,
p+q=n. Relabeling konečné konstrukce dovolí dát vyšší stupně na
prvních p požadovaných jmen.

Pro liché d=2k+1 je p sudé. Pokud n≥d+2, tištěné posuny
±{2,...,k+1} jsou různé, nenulové a vynechají ±1.
Základ má stupeň 2k=d−1; matching na p vrcholech přidá právě
po jedné hraně těmto vrcholům a není v základu.
Hraniční n=d+1 je chybný pro k≥1: viz samostatný F0003,
kde 3333 vytvoří jen C4. Tuto hranici opraví K_n minus matching
na q nízkostupňových vrcholech; q je sudé. Případ d=1,n=2
je rovněž pokryt touto opravou.

Pro sudé d=2k>0 je q sudé. Posuny ±{2,...,k} jsou díky
n≥2k+1 různé a základ má stupeň 2k−2.
Pro q=0 přidá obvodový cyklus dva sousedy všem.
Pro q>0 přidej matching 1–2,...,(q−1)–q a cestu q–(q+1)–...–n.
Vrcholům 1,...,q−1 a n přibude po jednom sousedu (celkem q nízkých);
vrcholům q,...,n−1 po dvou (celkem p vysokých).
Žádné přidané hrany nejsou v základu, protože mají posun ±1.
Po přeznačení je tedy požadovaná seřazená posloupnost realizována.
Známé omezení d>0 pro Case 2 je přesně potřebné kvůli nulové větvi.

Obecná poznámka o vysoké souvislosti a citace Wang–Kleitman jsou
externí vstup s bibliografickou výjimkou; nejsou potřeba pro tento
samostatný existenční důkaz.

## 111: minimální regulární rozšíření

Je-li G už d-regulární, vezmi N=n. Jinak potřebujeme n′>0 nových vrcholů.
Deficity původních vrcholů jsou e_k=d−d_k≥0 a s=Σe_k.
Pro každé n′ jsou nutné:
(i) n′≥max e_k; (ii) n′d≥s;
(iii) n′d≤s+n′(n′−1); (iv) (n+n′)d sudé.
První dvě meze jsou kapacitní, třetí říká, že zbývající nové stupně
lze nejvýše doplnit kompletním grafem na nových vrcholech, čtvrtá je parita.

Postačitelnost: přiřazuj e_k po sobě jdoucích nových vrcholů cyklicky.
Díky (i) se v jednom původním řádku žádný cílový vrchol neopakuje.
Celková zátěž každého nového vrcholu je floor(s/n′) nebo ceil(s/n′).
Z (ii) plyne nezápornost zbytků d−load; z (iii) jejich maximum
d−floor(s/n′)≤n′−1. Zbytkové stupně se liší nejvýše o 1.
Jejich součet n′d−s je sudý, protože s=nd−2|E(G)| a platí (iv).
Správný existenční důkaz 110 výše tedy doplní hrany mezi novými vrcholy.
Na původních vrcholech se nic nepřidává, takže G zůstane indukovaný podgraf.
Použití 110 zde vyžaduje opravenou hraniční konstrukci F0003;
samotná věta o existenci regulárního rozšíření je správná.

Vždy funguje n′=n: max e_k≤d≤n−1,
s=nd−2|E|≤nd a 2|E|≤n(n−1), parita 2nd je automatická.
Pro minimum N stačí vzít nejmenší n′ z 0,...,n splňující čtyři
nutné a postačující číselné podmínky, s přímou větví n′=0 pro regulární G.
Jde o nejvýše n jednoduchých testů, nikoli enumeraci grafů.

Ostrost 2n: pro G=K_n bez hrany 12 a n≥4 máme d=n−1 a s=2.
Podmínka (iii) je n′(n−n′)≤2. Pro 1≤n′<n je levá strana
nejméně n−1≥3 a n′=0 odporuje (i). Je tedy nutné n′≥n.

Další kurzor: sítě od druhé části str. 31/file48 a §7–112.
Nálezy: 3 confirmed, 3 candidate. F0003 nevyvrací žádnou existenční
větu; jde o selhání tištěné konkrétní konstrukce na doloženém vstupu.
