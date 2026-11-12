# Souvislý průchod §2.3.4.2 — 5. listopadu 2026

X0974. Přímo přečteny originály 372–382 a 580–586 v rozsahu orientovaných
stromů, všech 28 zadání, všechny vytištěné odpovědi, obrázky a tabulky.
Přezkoušeny všechny tři obecné důkazové poznámky v `parallel/oriented-trees/notes/`,
tři samostatné protipříklady a celý `check_exact.py` proti originálu.
Přijaté konečné testy se neopakovaly; nový brute force neběžel.

## Definice, G, E, D a úlohy 1–15

Původní path je neprázdný sled a simple připouští také uzavřený cyklus.
Proto úloha 1 v původní sazbě platí i pro stejné konce; dodatek „or cycle“
je potřeba až s novou terminologií. Délka n≥1 je zde explicitní.
Zapomenutí orientací odstraňuje smyčky a násobné hrany. Proto dva
paralelní oblouky A→R tvoří správný protipříklad k úloze 6.

Orientovaný strom má právě jeden výstup z každého nekořenového vrcholu,
žádný z R a konečnou cestu z každého vrcholu do R. Neorientovaný cyklus
by vynutil uzavřený orientovaný cyklus; orientace volného stromu do R
je naopak jednoznačná. Fig.34 i všechny tři Fig.35 souhlasí. První dvě
Fig.35 se liší pořadím dětí, třetí kořenem; neorientované hrany jsou stejné.
Původní argument na 373 je platný, pozdější přepis výslovně připomíná
V_n=V_0. Není zde nový protipříklad.

V G je konečnost i nepřítomnost izolovaných vrcholů explicitní. Nejdelší
tah ve vyváženém grafu musí končit ve svém začátku. Zbytek je vyvážený;
každý nepoužitý oblouk incidentní s navštíveným vrcholem umožní po rotaci
prodloužit tah. Souvislost tak vynutí použití všech oblouků. V lemmatu E
časy posledních výstupů podél zvolených hran přísně rostou, takže tvoří
strom do R. V D odložené stromové výstupy vedou při předčasném zastavení
ke stále nepoužitému výstupu z R, spor. Kořen stromový výstup nemá;
oprava 2026 výslovně vymezuje V≠R, jak už vyžaduje definice e[V] na 373.

Úlohy 1–7: nejkratší neprázdný sled je cesta nebo cyklus; šest správných
cyklů úlohy 2 má shodná znaménka. A→B,A→C je souvislý graf bez kořene.
Topologické pořadí je ekvivalentní absenci orientovaných cyklů, při
striktním předcházení včetně smyček. Z uzavřeného sledu lze vyjmout
nejkratší cyklus. Podmínky stupňů bez cyklu postačí k existenci stromu
jen v konečném grafu; nekonečný řetězec vedle izolovaného R nestačí.

8 nemá vytištěnou odpověď. Přijaté vlastní řešení má úplný rozklad
Aut(T)=∏_t(Aut(B_t)≀Sym(I_t)) podle izomorfních větví kořene. V konečném
případě dává rekurzivní charakterizaci i součin faktoriálů násobností.
Přímé součiny lze realizovat vzájemně neizomorfními větvemi po přidání
různě dlouhých řetězců. Pro nekonečné stromy se používá kompatibilita
automorfismů ořezů do hloubky h, nikoli neplatná indukce konečnou výškou.

9–13: přesné překořenění Fig.30 do G a všechny jeho hrany souhlasí.
G1/G2 obrací jen cestu do původního kořene, ukládá starého rodiče před
přepsáním a spotřebuje konstantní pomocnou paměť. C1–C6 zachovává
skutečné přijaté hrany a znaménka; C2 má správně S[k]=−s. Nová nestromová
hrana spolu s jedinou cestou v dosavadní komponentě dává fundamentální
cyklus i vzhledem ke konečné kostře. Stupeň stromového uzlu je vstupní
stupeň. Strom v obecném zakořeněném digrafu lze vybrat pomocí klesající
nejkratší vzdálenosti do R, i pro nekonečný graf.

14: všech osm vytištěných tahů obsahuje všech devět oblouků právě jednou,
začíná e12, respektuje poslední e01/e21 a končí v 1. Úplnost plyne
ze tří nezávislých pořadí dvojic, 2³=8. Použity správné směry Fig.36
podle errata. 15 je v originálu nesprávně bez omezení na konečné grafy:
oboustranný řetězec i→i+1 je souvislý a vyvážený, ale není silně souvislý.
To je zveřejněná oprava z roku 2004.

## C0051: cena skutečně vypsaných cyklů

Na 581 je potvrzená chyba časových mezí, nikoli správnosti C.
Vstupní cesta (1,2),…,(n−1,n) a potom (1,3),…,(1,n) má m=2n−3 hran.
C přijme cestu a vytiskne cykly délek 3,…,n, tedy n(n+1)/2−3 hran.
To vylučuje O(m log n) bez ohledu na rychlejší testy souvislosti.

Ani navržená DFS varianta nezaručí lineární **výpis**: ve vějíři má
vrchol 1 v každé DFS kostře nejvýše tři sousedy. Po jeho odstranění
zbývají nejvýše tři cesty velikostí s_i. Součet vzdáleností do 1 je
alespoň ∑s_i²/4≥(n−1)²/12. Všechny kromě nejvýše tří hran (1,v)
jsou nestromové, takže součet délek jejich cyklů je Ω(n²).
Hvězdová kostra by dala krátké trojúhelníky, ale není DFS kostrou
tohoto grafu. Správná obecná mez je O(n+m+L), kde L je délka výstupu.
Tarjanův citovaný text uchovává cykly kompaktně, a jeho vlastní
lineární tvrzení tím není vyvráceno. C0051 zůstává confirmed.

## Hodiny a Markovovy procesy

16: každá karta je jeden rozlišitelný oblouk z hromádky do své hodnoty;
vstupní i výstupní stupně jsou čtyři. Hra končí při čtvrtém králi.
Výhra je ekvivalentní Eulerovu tahu, poslední výstupy z 1,…,12 jsou
spodní karty a podle E/D tvoří strom právě při výhře. Původní odůvodnění
na 581 mylně říká, že poslední karta musí pocházet ze středu; správně
se posledním králem do středu vracíme. Známá oprava toto nahrazuje.

17: adaptivní odhalování nezávisí na dosud skryté kartě zvolené pozice.
Úplné pořadí odkrytí po povolených nucených přesunech je tedy rovnoměrná
permutace. Karet zůstane k právě tehdy, je-li poslední král na 52−k:
P(K=k)=C(51−k,3)/C(52,4), 0≤k≤48. Výhra má pravděpodobnost 1/13.
Pět mezer mezi králi má společnou střední délku 48/5, takže průměrně
odkryjeme 212/5=42.4 karet. Po uzavřené fázi je zbytek vyvážený;
počet dalších nucených přesunů je počet rekordů v pořadí posledních
výskytů L13,L1,…,L12 minus jedna. Symetrie hodnot a rekurence rekordů
dávají přesně Stirlingovo rozdělení [13,k+1]/13!, nikoli jen heuristiku.

26 nemá vytištěnou odpověď. Ze všech vrcholů vede kladně pravděpodobná
cesta do Stop; konečnost dá společnou δ>0 pro dokončení do n kroků.
Proto ||A^(kn+r)||∞≤(1−δ)^k a N=∑A^k=(I−A)^−1 existuje. Stop má
nulový řádek: po návštěvě proces zanikne, nečeká v absorpční smyčce.
Součet indikátorů návštěv dává N_ij. Silná Markovova vlastnost při
zásahu j dává a_j=N_1j/N_jj a b_j=1/N_jj, tedy správné kofaktory
s transponovanými indexy j1. Rozdělení kladného počtu návštěv je
a_j(1−b_j)^(k−1)b_j; pro n=1 a b_j=1 platí příslušné okrajové hodnoty.
Konkrétní matice, 3/128 a očekávání 13/6,7/3,7/3,5/3 souhlasí
s přijatou přesnou racionální kontrolou.

27: součet a_ij t_i i t_j∑a_jk počítá stejnou váhu funkcionálních
digrafů s jediným cyklem obsahujícím j. Odstraníme buď vstup do j
na cyklu, nebo výstup z j. Tím je stacionarita obecně dokázána,
včetně smyček. Nevyžaduje aperiodicitu ani konvergenci rozdělení v čase.

## Determinanty, počítání stromů a C0054

18: incidenční minor stromu je po uspořádání trojúhelníkový s diagonálou
±1. Cyklus dává závislost řádků. Cauchy–Binet tak sčítá indikátory
všech koster; zahrnuje i prázdný minor determinantem 1.

19: rozvoj řádkového Laplaciánu podle jedné zvolené výstupní hrany
každého nekořene dává nulu pro každou volbu s cyklem, jinak přesně +1
krát součin vah. To dokazuje váženou orientovanou větu i všechny
hlavní minory s předepsanou množinou kořenů. Smyčky nevstupují,
paralelní oblouky jsou různé volby. V 20 je neorientovaná matice
A0ᵀA0 správně; det B=11. Vzorové A a A* na 378/583 a všech 27
oblouků Fig.37 odpovídají koncům a směru opravené Fig.36.

21: při n vrcholech a stupni m má G* q=nm vrcholů. Incidenční
obdélníkové X,Y dávají XY=N,YX=N* a
det(λI_q+L*)=(λ+m)^(n(m−1))det(λI_n+L). Koeficient λ je **součet**
počtů stromů přes všechny kořeny. Proto t(G*)=m^(n(m−1))t(G).
Původní značení n+1 na 379 má shodný správný výsledek s exponentem
(n+1)(m−1); samotná změna počtu vrcholů není chyba zadání. Dlouhý
původní determinantový argument 583–584 má známou chybu odstraněnou
náhradou z roku 2001. Výše uvedený obecný důkaz nepoužívá jeho
problematické mocniny a perturbaci jediného diagonálního prvku.

22: pevný první rozlišitelný oblouk spolu s posledními výstupy
dává T_r∏(σ_v−1)! možností. Cyklický tah má jedinou rotaci začínající
daným obloukem. Počet všech lineárních tahů je proto M krát větší.
Současně T_r nezávisí na kořeni. Nedochází k míchání normalizací.

23: správná korespondence potřebuje f(x_k,…,x_1)=x_(k+1).
**C0054 confirmed:** pro m=k=2 a f(u,v)=1−v má zadání maximální
periodu 0011; doslovná odpověď na 584 místo toho dává
00→01→10→01 a vynechá 11. Otočení argumentů je bijekce všech
funkcí, takže konečný počet m^(−k)(m!)^(m^(k−1)) zůstává správný.
Vzorec zahrnuje k=1 a m=1. Rekurence počtů stromů v G_k a dělení
počtem kořenů dávají tentýž výsledek.

24: nahrazení e_j E_j kopiemi dává vyvážený souvislý digraf; vyjmeme
jedinou kopii e0 z Eulerova tahu. Případ pouhé smyčky e0 potřebuje
prázdný výsledný sled. Tuto již evidovanou okrajovou konvenci nelze
zaměnit za důkaz, že tištěná definice na 372 dovoluje nulovou délku;
neděláme z ní nový algoritmický nález.

28: negování prvních m řádků i sloupců vytvoří Laplacián bipartitního
grafu s kořenem 0. Nezávislé proměnné identifikují každou volbu hran,
takže každý necyklický monom má koeficient +1, cyklický nulu.
Dosazení jedniček a rozklad na nulové součty v obou skupinách dává
(n+1)^(m−1)(m+1)^(n−1)(m+n+1). Pro m=2,n=3 je to 216.
Sylvesterova specializace na 586 dává n^n(n+1)^(n−1); kontrakce
nucených hran dá Cayleyho (n+1)^(n−1). Všechny uvedené matice
a elementární úpravy v opravené odpovědi odpovídají tomuto důkazu.

## Reprezentace 25 a C0055

ALINK/ATAG propojuje výstupy a přechází na vstupy stejného vrcholu,
BLINK/BTAG symetricky opačně. Obrácení všech oblouků tedy vymění
obě dvojice polí. Obě tabulky 584 souhlasí s pořadím a konci hran.
Pro strom po přidání R→H dostaneme první dítě / pravého sourozence;
ATAG není zadáním ztotožněn s LTAG. Izolované vrcholy vyžadují
vnější počet nebo jména; zadání taková metadata nezakazuje.

**C0055 confirmed:** přidejme smyčku h:H→H poslední do F_H=(r,h).
Pak h má ALINK=r,BLINK=h,BTAG=1. Standardní hlavička na 324 však
vyžaduje RTAG=0. Vedle v poznámce přiznané výjimky RTAG kořene
chybí i výjimka RTAG hlavičky. Už strom s jediným R stačí. Vlastní
obecná reprezentace je správná; chybná je přesná shoda v poznámce 585.

## Pramenné výjimky a přesná mapa

Převzata obsahová kolace zdrojů v `notes/sources.md` s jejími přesnými
omezeními. Není tím tvrzeno nové čtení celých historických publikací.
Pozdější zápisy X0698, X0829, X0823 a X0837 mají přednost před
starším seznamem neúspěšných přístupů. Přeskočeno:

- Good: první původní 167 přečtena již v X0698; chybí pokračování
  168–169. Metadata první řady 21(1946),167–169 jsou ověřena, nově
  shodně potvrzena nakladatelem Wiley; chybné 1947 na 374 je známé erratum.
- 16: Jonesové skutečná kap. VII je přečtena, chybí pouze jisté datování
  exempláře [1900?]. Cheney 1870 je doložena dobovým katalogem;
  pravidla známe z rozšířené edice, původní 62–65 nejsou kolacionovány.
- 17: Staver 1946 má přesný knihovní ročník, ale neveřejné 88–89
  ani titul článku nebyly obsahově přečteny.
- 18: Okada–Onodera 1952,89–117 chybí; pozdější citace nenahrazuje originál.
- 21: úplné Dawson–Good 1957, Knuth 1967 a Orlin 1978 chybí.
  Metadata a abstrakty jsou doloženy; X0837 čte jen část Orlinovy
  bibliografie na 198, nikoli 187–197. Nepravidelná generalizace není
  matematickým předpokladem zde dokázané pravidelné úlohy.
- 25: původní osobní komunikace W. C. Lynche není dostupná.
- 28: přesná kapitola 9 Hageman–Young 1981 nebyla získána. Zvlášť
  se nepovažuje za ověřenou její formulace „Property A“ a aplikace.
  Krátká nová rešerše našla blokovou charakterizaci v pozdějších textech;
  cílený primární Young 1954 na AMS vrátil 403, nikoli PDF. Další
  přístupové cesty se neopakovaly. Samotná bipartitní struktura matice
  je přímo ověřena důkazem, nezávisle na názvu a citaci.

Čtyři dnešní vrstvy errat: 36 stránkových bloků, 104 tematických
výskytů, SHA-256 v `oriented-trees-errata-extract.json`. Nově přímo
zobrazeny zejména all1-prepre 25/43/44 a all1 10. Tři potvrzené
nálezy nejsou opraveny. Fyzický výtisk a prvenství neověřeny.

X0447 mapuje věcné opravy původního tisku na 374,375,377,581,583–585.
Přepisy důkazu 373, terminologie, explicitní kořenové omezení v D,
indexové rozepsání na 381 a samotné přeznačení n+1→n na 379 se
nepočítají jako nové matematické vady. Přesné lokace C0051/C0054/C0055
jsou 581/584/585, nikoli jejich správná zadání.

Všech 28 úloh a hlavní text se uzavírají s uvedenými bibliografickými
výjimkami. Celé stránky 372–381 a 580–585 jsou pokryty; 382 a 586
zůstávají částečné pro začátek následujícího oddílu. Další kurzor je
§2.3.4.3, tištěná 382 / soubor 397.
