# §3.2.2: dokončení textu na str. 32–36

Stav: **checked v níže vymezeném rozsahu**. Uzavírá zbývající text
sekce; důkazy úloh jsou v samostatných poznámkách. Nejde o nový nález.
Původní stránky `images/vol2-p032.png` až `vol2-p036.png` prohlédnuty;
kontrola všech čtyř vrstev errat k 1. listopadu 2026.

## Lewis–Payne a bitové sloupce

**Bitový sloupec** znamená jednu pevnou bitovou pozici ve všech slovech
uloženého stavu. Operace XOR provádí součet modulo 2 nezávisle v každém
sloupci. Primitivita polynomu stupně 55, již ověřená v
[primitivních polynomech](primitive-polynomials.md), znamená, že přechod
má jediný cyklus na všech `2^55-1` nenulových binárních stavech.
Každý nenulový sloupec proto dává posun téže binární posloupnosti;
nulový sloupec zůstává nulový. Celé slovo má periodu `2^55-1`, jestliže
je alespoň jeden sloupec nenulový: jeho perioda dělí tuto délku a zároveň
musí být násobkem periody nenulové projekce.

Doslovně pro libovolnou inicializaci by věta o **každém** sloupci
potřebovala nenulovost každého sloupce. Kniha však odkazuje na konkrétní
metodu Lewis–Payne, nikoli na libovolně inicializované XOR.
Primární Payneova zpráva
[Calculation of GFSR Pseudorandom Number Binary Starting Matrix](https://archive.org/details/calculationofgfs567payn),
UIUCDCS-R-73-567, březen 1973, popisuje inicializaci právě pomocí sloupců
`V_0,V_d,V_(2d),...`, kde `V_0` je vektor samých jedniček a
`V_j=A^j V_0` pro matici binární rekurence `A`. Všechny jsou nenulové.
Zpráva používá stupeň 98, lag 27 a odkazuje na tehdy připravovaný článek
Lewis–Payne v JACM; není zdrojem konkrétního stupně 55 z knihy.
Vizuálně přečteny str. 2, 7 a 8 (PDF 11,21,23),
`images/payne-1973-p02.png`, `p07.png`, `p08.png`. Soubor a hash
v `sources/payne-1973-starting-matrix.*`.

To dostatečně vysvětluje implicitní inicializační konvenci. **Nulový
sloupec nehlásíme jako chybu této pasáže.** Celá číselná tabulka zprávy
ani její zdrojový FORTRAN nebyly auditem tohoto odstavce ověřeny.
Původní JACM článek, DOI 10.1145/321765.321777, zůstává nedostupný
přes ACM (403); jeho úplné přečtení se netvrdí. Výrok, že sčítací
varianta měla v praxi lepší výsledky, je zpráva o zkušenosti, ne obecná
věta o všech testech a všech inicializacích.

## Úplné a inverzní posloupnosti

Přechod řádu `k` nad `m` symboly má nejvýše `m^k` stavů, a tedy nejvýše
tak dlouhý cyklus. Konstrukce Martina a Reese a přesný význam všech
`k`-oken jsou rozebrány v [úplných posloupnostech](complete-sequences.md).
Pomalá změna součtu sousedních hodnot v Martinově konstrukci je
strukturální omezení, nikoli rozpor s tím, že se všechna okna vyskytnou.

Projektivní inverzní přechod, který připouští také symbol nekonečna,
byl úplně prověřen v [inverzních generátorech](inversive-generators.md).
Vypuštění kroku přes nekonečno vede k implementační konvenci `inverse(0)=0`:
úsek `0,infinity,c` se změní na `0,c`. Proto se liší délka pozorovaného
cyklu; text tuto implementaci nezaměňuje s projektivním důkazem periody
`p+1`. Výroky o celočíselných nadrovinách mají přesný obsah v úloze 37.

## Míchání a součet dvou generátorů

Algoritmy M/B a jejich MIX programy již pokrývá
[první poznámka](other-algorithms.md). Prohlášení, že B nezhorší
náhodnost, nelze číst jako uspořádání všech deterministických posloupností
podle všech myslitelných testů. Má však přesný základ v ideálním modelu:
pokud jsou vstupy nezávislé se stejným rozdělením `Q`, výstupy mají
rovněž nezávislé rozdělení `Q`.

Důkaz: podmíněně na dosavadní výstupy zůstávají položky tabulky nezávislé
s rozdělením `Q`. Zvolený index je funkcí minulého výstupu, a tedy
v dané podmínce pevný. Čtená položka má rozdělení `Q` nezávisle na
minulosti; po jejím zveřejnění ji nahradí nový nezávislý vstup, čímž se
invariant obnoví. Inicializační pomocná hodnota je nezávislá na tabulce,
takže platí i první krok. Konečné pseudonáhodné posloupnosti se tím
neprohlašují za nezávislé.

Je také přesné, v jakém smyslu se při míchání mění pouze pořadí.
Po `N` výstupech platí rovnost multisetů

```text
initial_table + N_consumed_inputs = N_outputs + final_table.
```

Multiset eviduje i násobnost každé hodnoty. Pro libovolnou množinu
hodnot se její počet v `N` vstupech a výstupech liší nejvýše o velikost
tabulky `k`. Pro váhu každého prvku v `[0,1]` platí stejná mez pro
součty. Trvalou vadu četností proto konečná tabulka neodstraní. Z toho
samotného ještě neplyne přesná p-hodnota testu narozeninových rozestupů;
konkrétní testy a odkaz na náhodnou procházku zbývají pro §3.3.2.

Při kombinaci `Z=X-Y mod m` zůstávají důkazy period úloh 13–14 platné,
protože `-Y` má stejnou periodu jako `Y`. Pro nezávisle zvolené seedy
jsou celé bloky X a Y nezávislé. Na konečné grupě bloků
`G=(Z/mZ)^d` má rozdělení Z tvar konvoluce `P*Q_minus`.
Je-li `U` rovnoměrné rozdělení, trojúhelníková nerovnost dává

```text
sum_z |(P*Q_minus)(z)-U(z)| <= sum_x |P(x)-U(x)|.
```

Počítá se přes všechny možné bloky, nikoli po jedné pevné trajektorii.
Tím je přesně vyjádřen jeden smysl zlepšení rovnoměrnosti; nevzniká
záruka pro závislé seedy ani pro každý konkrétní statistický výsledek.
Detaily úlohy §3.3.2-23 zůstávají samostatnou položkou auditu.

## Lüscherovo prořezávání

Primární preprint Martina Lüschera
[A Portable High-Quality Random Number Generator for Lattice Field Theory Simulations](https://arxiv.org/abs/hep-lat/9309020)
je uložen v `sources/luscher-1993-ranlux.*`. Přečten úvod, §2.1–2.4,
§3, §4 a relevantní §5; vizuálně také věta 2.2 na str. 4/PDF5.
Studuje odečítání s výpůjčkou s bází `b=2^24` a lagy `r=24,s=10`.
§3 vysvětluje korelace tím, že blízké počáteční vektory zůstávají
blízké po jednom bloku. §4 pracuje se spojitým limitním modelem na
jednotkové krychli s protilehlými stěnami ztotožněnými. §5 ponechává
`r` hodnot z bloku délky `p`, používá kongruenční násobitel `a^p`
a porovnává konkrétní spektrální testy. Článek výslovně odlišuje konečný
stavový prostor od skutečné statistické nezávislosti.

Vlastní algebraická kontrola vztahu citovaného knihou: z identity
`b*y_(n+1)-y_n=m*x_n` plyne modulo `m`
`y_(n+1)=b^(-1)*y_n`, a indukcí po `t` krocích násobitel `b^(-t)`.
Inverze existuje, neboť `m=b^r-b^s+1` je nesoudělné s `b`.
Přenosové invarianty a radixový výklad již byly odvozeny v
[generátorech s přenosem](carry-generators.md).

Knižní příklad `55` uchovaných hodnot z každých přibližně `500`
přenáší myšlenku na jinou, sčítací rekurenci. Není totožný s parametry
preprintu. Přesné koeficienty `X_500` a polynomiální přechod ověřují
[identity úloh 32–33](lagged-identities.md). Formulace o „blízkých“
vektorech a téměř nulové korelaci je kvalitativní motivace, bez určené
metriky a meze. Nevydáváme ji za větu o všech dvojicích seedů, ani
za přesnou nezávislost konečných stavů. Kompletní spektrální teorie
v §3.3.4 a konkrétní kód §3.6 zůstávají otevřeny.

## Úvod k Blum–Blum–Shub a muddle-square

Vzorce (16) a (17) na str. 35–36 jsou aritmeticky správné:
`X'=X^2 mod M`; první výstup je nejnižší bit a druhý parita součinu
odpovídajících bitů X a pevné masky Z. Maska `Z=1` dává první variantu.
Je-li `M=P*Q` pro **různá** prvočísla `P,Q=3 mod 4`, grupa nenulových
kvadratických zbytků má řád `(P-1)(Q-1)/4`, který je lichý. Umocnění
na druhou je na ní permutací: v každé složce modulo P,Q má mocnění
exponentem 2 inverzi modulo lichý řád podgrupy. Rovnoměrný nesoudělný
seed se po jednom umocnění stane rovnoměrným kvadratickým zbytkem,
protože každý takový zbytek má čtyři odmocniny mezi jednotkami.

Bezpečnostní tvrzení je **podmíněné** obtížností faktorizace náhodného
modulu a náhodným výběrem seedu/masky. Pevný seed 1 ani maska 0 proto
nejsou vyvrácením formulované distribuční záruky. Časový příměr „100
let“ navíc výslovně závisí na dostatečně velkém M a nepředstavuje
samostatný údaj o hardwaru v roce 2026.

Zkontrolováno umístění navazujícího výkladu §3.5F, str. 174–176:
Blumovy moduly mají různě vymezené intervaly pro oba faktory, definice
zahrnuje rovnoměrný stav a věta P uvádí explicitní převod statistického
rozlišování na faktorizaci s délkou výstupu N, bitovou délkou modulu R a rozlišovací odchylkou epsilon. Jde zde o
kontrolu významu a odkazu, **ne dokončený audit kryptografické redukce**.
Její důkaz a slabší redukce pro variantu bez masky v §4.5.4-43 zůstávají
v evidenci otevřené. Str. 36 sama neslibuje záruku pro každý pevný seed.

## Errata a rozsah uzavření

Relevantní známé opravy: str. 33 odkaz (12)→(13), 29. 12. 1997;
Greenwoodovy stránky 222→222–227, 8. 12. 2009; str. 34 přidané
„additional“, 16. 9. 2014; velikost modulu pro MIX, 18. 6. 2024;
pořadí a jména O. Taussky a J. Todd, 23. 12. 2024. Žádná další oprava
výše prověřovaných matematických vztahů nalezena nebyla.

Po spojení s ostatními poznámkami jsou text a **všech 38 úloh §3.2.2**
uzavřeny jako audit jejich tvrzení, odpovědí, oprav a zdrojového rozsahu.
Neznamená to vyřešení otevřené Reiserovy domněnky ani provedení všech
historických experimentů. Osm potvrzených nálezů této sekce je
C0007–C0014; kvalifikace jejich závažnosti jsou v jednotlivých záznamech.
