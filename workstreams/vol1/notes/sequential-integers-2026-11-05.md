# Souvislý průchod §1.2.4: celé části a elementární teorie čísel

5. listopadu 2026. Přímo přečteny původní strany 39–45 a odpovědi
476–480. Porovnány celé důkazy `integer-functions.md`,
`replicative-functions.md`, `floor-sums.md`, dále přijatá pramenná
revize `floor-sources-root-review.md` a přesný zbytek
`integer-final-root-status.md`. Dřívější výpočty se neopakovaly.

Celých 49 původních úloh a přidaná 50 jsou matematicky uzavřeny.
Úlohy 40 a 49 přecházejí z partial do checked s explicitně přeskočenou
bibliografií: Mordellovy s. 372–375 a Eiseleho–Hadelerovy s. 475–477
nebyly přečteny. Jejich pramenné záznamy X0055/X0727/X0765 zůstávají
partial. Přijaté původní pasáže Yodera, Hamela, Buscheho, Hermita,
Iversona a Fermatovy korespondence se tím nemění. Soukromé atribuce
McEliece/de Bruijn se samostatně nedokládají; jejich matematická
tvrzení mají vlastní důkazy.

## Co bylo porovnáno

Definice podlahy/stropu a modula zahrnují záporná čísla a smluvené
x mod 0=x. Ekvivalence kongruence s celočíselným násobkem rozdílu
platí také při modulu 0. Násobení obou argumentů modula je správné
i při nulovém násobiteli, ale tento případ vyžaduje samostatnou větev.
Zákony A–D pro celá čísla vycházejí z Bézoutovy identity; jejich
odvození není kruhové. Rozšíření na reálné argumenty v úloze 24
nepovoluje libovolné krácení ani libovolné reálné moduly v zákoně D.

Fermatův důkaz permutací zbytků je správný včetně p=2 a násobků p.
Eulerova věta má zvláštní triviální větev m=1; použitá konvence 0^0=1
je stanovena už dříve. Multiplikativita phi a dělitelových součtů
využívá jednoznačnou faktorizaci a konečné množiny kladných dělitelů.
Tvrzení úlohy 32 nebylo rozšířeno na n=0 a neurčité nekonečné sumy.

U kompozic podlah/stropů byly zkontrolovány přesné otevřené a uzavřené
meze. McElieceova charakterizace využívá spojitost a přísnou monotonii;
nelze ji nahradit výčtem náhodných vstupů. Součty v 37–38 mají obecné
důkazy pomocí zbytkových tříd a překročených prahů, platné pro záporné
x a v 37 také záporné m. Známá oprava symetrie stropového součtu mění
dolní mez na 0<k≤n; obě hlavní formule odpovědi 37 jsou správné.

U replikativních funkcí 39 byla znovu prověřena jednoznačnost rozkladu
rπ+m, nuly sinusového součinu a periodizace f(x mod 1). Závěr 40
o lokálně Riemannovsky integrovatelných funkcích má úplný důkaz:
h(x)=f(x+1)−f(x) je konstantní zvlášť na každé poloose; Fourierovy
koeficienty periodizace mají vztah c_(nj)=c_j/n. Omezenost Fejérových
průměrů vyloučí kosinovou složku s harmonickým růstem. Jednoznačnost
koeficientů dává pilu skoro všude a posuny doplní obě části podlahy.
Nezaměňujeme shodu skoro všude za shodu v každém bodě. U spojité f
se shoda rozšíří na všechny body a výsledkem je a(x−1/2).

Bernoulliho, cot, csc², Hurwitzovy zeta a psi příklady mají násobicí
vzorce na svých definičních oborech; póly a parametr s=1 se nedoplňují
neurčitými hodnotami. Chybějící i v odpovědi 40 je již veřejné erratum.

Obecná reciprocita 45–46 má důkaz počítáním velikosti jednotlivých
bloků, včetně posledního zkráceného bloku a neceločíselného konce αn.
V 47 je Legendreův symbol 0 pro násobky p a paritní substituce vyžaduje
výslovnou známou výjimku v části (c). Mřížový argument pro kvadratickou
reciprocitu a znaménka symbolu (2/p) souhlasí.

V 49 je nezbytné, aby f byla celočíselná; bez toho funguje protipříklad
f(x)=x. Po zveřejněné opravě dává indukce podlahu nebo strop na Q.
Hamelova báze poskytuje protipříklad k rozšíření na celé R a hustota
grafu vysvětluje neomezenost na každém intervalu. Přidaná úloha 50
obsahuje správný protipříklad 3143 a oba jednostranné závěry pro α≥1
a 0<α≤1; ty jsou dokázány intervaly, ne zaokrouhleným dělením π.

## Stránky a errata

Čtyři vrstvy errat porovnány podle stran 39–45 a 476–480 i podle témat;
aktuální originály mají stejné hashe jako dnešní obnovený archiv.
Změny 1997–2005, pozdější kladnost/celočíselnost a opravy 2020–2026
zůstávají X0005, X0049–X0054 a X0058, bez nových duplicitních karet.
Původní s. 479 má správné označení Mordellova ročníku 33. Později
vzniklá chyba označení řady (2), opravovaná v roce 2026, proto není
červeným defektem této stránky našeho prvního dotisku.

Celá s. 45 a s. 480 prozatím zůstávají částečné: pokračuje na nich
§1.2.5. Ostatní stránky tohoto bloku jsou zkontrolované v popsaném
rozsahu; známé opravy zůstávají červené i na dokončené stránce.
Žádný nový dosud nepublikovaný nález nevznikl.
