# Souvislá revize §3.4.2: S, R, P a základní úlohy

6. listopadu 2026, X0125/X0126. Přímo přečteny původní 142–148
a 590–592. Tento blok přijímá algoritmy S/R/P a úlohy 1–13, 15, 17;
karetní kontext na 145, úloha 14, konstanta úlohy 16 a dodatky 18/19
pokračují zvlášť. Nový nález nepřibyl. X0126 odděluje známé opravy.

Přečteny celé `sampling.md`, `sampling-extensions.md`, oba verifiery
a všechny jejich výsledky; šest archivovaných bloků rozšíření má PASS.
Výpočty nebyly opakovány. Ideální nezávislé uniformní vstupy jsou
předpoklad důkazů; konečná mřížka ani libovolný pseudonáhodný generátor
tím nedostávají certifikát přesné rovnoměrnosti.

## Rovnoměrnost podmnožin a momenty

V S je podmíněná pravděpodobnost přijetí (n−m)/(N−t), přičemž
0<n−m≤N−t až do ukončení. Na hranici rovnosti je přijetí jisté.
Proto algoritmus nikdy nepřejde konec souboru a vybere přesně n
prvků. Pro libovolnou pevnou podmnožinu součin pravděpodobností
její historie dává n!(N−n)!/N!. To je rovnoměrnost celých vzorků,
silnější než rovnost jednotlivých inkluzních pravděpodobností.
Nezávislá původní metoda Bernoulliho výběrů má správně střed n
a směrodatnou odchylku √(n(1−n/N)); velikost vzorku není pevná.

Hypergeometrický prefix p(m,t) splňuje uvedenou dvouvětvovou
rekurenci. E(m)=tn/N vysvětluje nepodmíněnou pravděpodobnost n/N.
Po ukončení pouze pro účely tohoto rozdělení doplníme odmítnutí
zbývajících pozic. Poslední přijatá pozice T má hmotnost
C(k−1,n−1)/C(N,n) pro n≤k≤N. Součtové identity dávají

```
E(T)=n(N+1)/(n+1),
E(T(T+1))=n(N+1)(N+2)/(n+2),
Var(T)=n(N+1)(N−n)/((n+1)²(n+2)).
```

Vzorce platí včetně n=N. Pro n=0 algoritmy S/R zadány nejsou;
obě podmínky n>0 jsou na původních stránkách výslovné.

U R indukce pro cílové podmnožiny s novým prvkem i bez něj dává
1/C(t+1,n). Různost odkazů a pořadí fyzického rezervoáru dokazují
správnost R6. Indikátor vložení záznamu t závisí jen na čerstvé
náhodné volbě a má pravděpodobnost n/t, proto jsou tyto indikátory
nezávislé. Součinová PGF, střed n(1+H_N−H_n) a rozptyl
n(H_N−H_n)−n²(H_N^(2)−H_n^(2)) v odpovědi 11 souhlasí.
Odpověď 10 je dereference téže tabulky do n paměťových buněk.
Pokud je požadováno původní pořadí, přidají se vstupní indexy.

Příklad 9 znovu porovnán se zadáním i uloženým výstupem:
rezervoár 1,2,3,5,9,13,16; výsledný vzorek 2,5,16. Pro N/n=1000
je uvedené přibližné 1/125 hrubým zaokrouhlením harmonického odhadu,
nikoli tvrzením přesné konstanty. Různý seed v poznámce na 143
je praktické rozlišení běhů; sám nedokazuje jejich nezávislost.
Vzorkování více kategorií vyžaduje samostatné stavy počítadel
a pro nezávislé vzorky také nezávislé náhodné vstupy.

## Přeskakování a očekávaná konstantní cena

Pro počet přeskočených záznamů X platí
T(k)=C(N−k,n)/C(N,n) a f(k)=C(N−k−1,n−1)/C(N,n)
na příslušné podpoře. Inverzní smyčka 8(b) i minimum nezávislých
diskrétních veličin 8(c) mají tento zákon. Za podporou bereme
pravděpodobnosti jako nulu; nepoužíváme záporné pravděpodobnostní
faktory. O(X) v odpovědi znamená počet iterací po konstantní
inicializaci, tedy celkově O(X+1).

Znovu přezkoumán úplný důkaz odmítací varianty ve starších poznámkách.
Pro 2≤n≤N/2 je kandidát Z=N(1−U^(1/n)), K=floor(Z),
g(z)=(n/N)(1−z/N)^(n−1) a obálka c=N/(N−n+1)<2.
Přijetí f(K)/(c g(Z)) je správné: součinové srovnání a Bernoulliho
nerovnost dávají f(K)≤c g(Z) na celém jednotkovém intervalu,
nikoli jen v bodech testované sítě. Přijetí má pravděpodobnost 1/c.

Dolní rychlý test L(K) ze `sampling-extensions.md` je platný podle
součinové nerovnosti ∏(1−a_j)≥1−∑a_j. Jen při jeho neúspěchu se
vyhodnotí součin délky K. Beta integrály E(Z)=N/(n+1) a
E(Z²/(N−Z))=2N/(n(n−1)) omezují očekávanou práci součinů
na méně než 2 za jeden pokus, tedy méně než 4 celkem. Přitom
E(cena do přijetí)=E(cena jednoho pokusu)/Pr(přijetí);
nezávislost ceny téhož pokusu na jeho přijetí není potřeba.
Pro n=1 stačí uniformní celé číslo; pro n>N/2 má přímá inverze
E(X)<1. Důkaz O(1) je tedy uniformní v parametrech.
Jde o model jednotkové reálné aritmetiky a mocnin; fyzické čtení
souboru ani bitová složitost nejsou zahrnuty. Není to audit celého
optimalizovaného Vitterova programu.

## Permutace, malé reprezentace a známé opravy

P má bijekci mezi historiemi voleb k_j∈{1,…,j} a označenými
permutacemi, tedy hmotnost 1/t!. Duplicitní hodnoty mají po odstranění
značek všechny stejnou násobnost. Rostoucí varianta je vkládání
nového prvku na uniformní pozici; při k=j stačí zapsat j bez čtení
dosud nezadané buňky. Pracujeme s neprázdnou vstupní posloupností;
prázdný případ se v implementaci obslouží před vstupem do P.

Úloha 12 má obecný dvouprůchodový invariant inverzní permutace;
přiřazení b_(a_j)←b_j obnovuje správný prefix a ponechává hotové b_j.
Oba průchody jsou lineární. V 13 je předpoklad n>1 výslovně uveden
v zadání. Grupa všech map x↦2^a x+b modulo m=2n−1 má přesně
m·ord_m(2) prvků, nejvýše m(m−1). Kladný a záporný jednotkový
řez generují stejnou grupu, ale správný směr zadaného řezu je x−1.

Dahlova úloha 15 zachovává invariant, že změněná aktivní malá pozice
má hodnotu větší než aktuální j; jediný odkaz v již hotovém X
ukazuje do odpovídající buňky Y. Tři větve proto přesně simulují
plné pole. Jde o O(n) paměti; zadání neslibuje čas konkrétní
neimplementované symbolové tabulky. Floydova 17 dává pro každý
cílový r-vzorek přesně r možností poslední volby, a tedy
r/[j C(j−1,r−1)]=1/C(j,r). Kolize přidává dosud nepoužité j.

Omezení na m seedů dává nejvýše m výstupních permutací.
13!/2³²=6081075/4194304 správně zaokrouhluje na 1.45.
Velký počet seedů je nutný předpoklad, nikoli důkaz rovnoměrnosti.

X0126 zachycuje zveřejněné opravy: na 145 zbytek modulo místo
nejednoznačného dělení (2001), na 146 P místo S (2001), na 591
N←N−X−1 místo N←N−1 (1999) a závorky kolem celého součinového
faktoru (2011), na 592 směr řezu x−1 (2008).
Chyba aktualizace N je věcná: pro N=3,n=2 první X=1 vybere
záznam 2, ale nesprávně ponechá N=2. Další X=1 pak žádá záznam 4.
V ideálním modelu má tato konkrétní cesta pravděpodobnost 1/6.
Opravené N=1 ji znemožní. Není to nový nález. Změna set→sequence
(2012), doplnění členu v zadání 14 a duplikace řádku jen v dotiscích
5–14 jsou redakční změny, poslední se netýká naší první sazby.

## Evidence a pokračování

Přijaty archivované přesné výsledky: 8178 koncových vzorků S,
2654 stavů R a 502 jeho vzorků; 163064 prefixových pravděpodobností,
11480 mezer, 1128 modelů a 73696 sond rychlých mezí, 46233 úplných
permutačních historií, 21753 Dahlových historií a 115137 invariantů,
15 malých grup s 3237 uspořádáními a 16278 Floydových mezistavů.
Číslo 1 421 542 628 u Floyda je počet implicitně sloučených historií,
nikoli počet jednotlivě provedených běhů. Každý obecný závěr má
samostatný důkaz; konečné testy jej nenahrazují.

Durstenfeldův Algorithm 235 a Pikeova poznámka v primárním přetisku
znovu celé vizuálně přečteny; sestupný cyklus, výměna a částečný
výstup souhlasí. Přetisk také uvádí CACM 7 (1964), 420. Samotná
časopisecká sazba této stránky nebyla přečtena. Starší autorova
metadata Vitterových článků zůstávají přijata; plné programy nebyly
auditovány. Přesné pinpoints Fisher–Yates Example 12, GraphBase 104,
Salfi 28–35, Hoyleova pravidla a historické priority osobních atribucí
zůstávají bibliografickými výjimkami. Totéž platí pro nepřečtené
původní Fan–Muller–Rezucha/Jones a Floydův časopisecký text.

Všechny čtyři vrstvy errat a aktuální TeX znovu prohledány podle
142–148/590–592 i tematických názvů. Errata all2-prepre 8/33
a all2-pre 13 přímo porovnána v obrazu. Karetní míšení na 145,
úlohy 14/16 a doplněné 18/19 budou mít vlastní navazující záznam.
Strana 592 také obsahuje začátek odpovědí §3.5 a zatím není celá
uzavřená. Žádný starý výpočet se nerestartuje.
