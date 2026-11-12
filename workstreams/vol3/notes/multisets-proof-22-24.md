# Multisety: jednotlivé argumenty úloh22–24

Zadání34–35, odpovědi601–602. Použity všechny opravy z let2006/2012,
zejména volba největšího indexu inverze, pravé závorkování a význam
cyklu v zobecněném součinu. Bez nového nálezu. Jeden cílený nice15
průchod scripts/generalized_intercalation.py ověřil tištěný příklad
a zvlášť ručně odvozený svědek neasociativity; neproběhla enumerace.
Historické citace a tvrzení o obsahu externích článků přeskočeny.

## 22(a): rozdělení abecedy

Označme L={1,…,t},H={t+1,…,m}, N_L=Σ_L n_j,N_H=Σ_H n_j.
V původním dvouřádkovém poli je počet přechodů horní L→dolní H
stejný jako H→L; označme jej p. Plyne to z rovnosti obou celkových
četností L v horním a dolním řádku.

Levý útvar l(π) ponechá první N_L sloupců, nahradí jejich dolní H
nulou a z posledních N_H sloupců ponechá pouze p dolních prvků L,
s horní nulou. Má tedy horní blok L a poté p nul; posledních p
dolních prvků je nenulových. Pravý útvar r(π) má nejprve p horních
nul nad nenulovými prvky H a poté původní horní blok H, jehož
dolní L jsou nahrazeny nulami. Je přímo prvkem příslušného P_0.

Obrácení dolního slova l(π) má první p prvků nenulových, jak
uvádí odpověď. Pro práci s vahami je vhodnější ponechat0 poslední
v horním řádku, rovněž podle odpovědi. Přesun celého posledního
bloku p sloupců na začátek jej případně převede do obvyklého P_0
se stejnými sloupci, a tedy i stejnou vahou.

Inverze konstrukce je jednoznačná: sloupce uvnitř L/H ponecháme.
Postupné sloupce L→0 z levého útvaru spárujeme zleva doprava
se sloupci0→H z pravého útvaru; stejně H→0 z pravého se0→L
z levého. Spojením vrátíme původní přechodové sloupce na jejich
původní místa v horních blocích. Tím vznikne každé původní π
právě jednou. Platí i p=0 a prázdný jeden z bloků.

## 22(b): počet a explicitní bijekce odpovědi

Dejme N=Σ_(j=1)^m n_j. Přípustné údaje splňují
Σp_j=Σq_j=n_0,0≤p_j,q_j≤n_j a n_0≤N.
Prvních n_0 nenulových prvků pod horní0 lze umístit n_0!/∏p_j!
způsoby. V každém horním bloku j vybereme q_j nulových míst
a zbylých N−n_0 míst vyplníme nenulovými hodnotami s četnostmi
n_j−p_j. Počet je tedy

n_0!(N−n_0)!/∏n_j! ·∏_j choose(n_j,p_j)choose(n_j,q_j).

Celý P_0 má choose(N,n_0)N!/∏n_j!=N!²/(n_0!(N−n_0)!∏n_j!)
prvků: nuly vybíráme pouze mezi posledními N místy a zbylé pozice
vyplňujeme původními nenulovými písmeny. Dosazením multinomiálních
počtů obou x/y-slov do vytištěného podílu dostaneme právě výše
odvozený počet. Výraz se používá pro přípustné údaje, tedy neprázdný P_0.

Odpovědní bijekce (π,σ)→(λ,ρ) je též úplná. Z λ poznáme nulová
místa v koncovém N-prvkovém bloku σ podle pozic x; všechny ostatní
pozice σ, včetně prvního bloku n_0, vyplníme posloupností indexů
v ρ. Tím je σ obnovena. Počáteční blok π je posloupnost indexů x
v λ. Nulová místa π pod horním j určí typy x/y mezi výskyty indexu
j v ρ; zbývající nenulová místa π vyplní indexy y v λ. To je
jednoznačná inverze všech kroků popsaných v odpovědi.

U vytištěného příkladu n_0=6,n_1=5,n_2=4,n_3=5 má π první
blok231313 a jeho nenulový zbytek23112321. Nulové vzory bloků
1/2/3 jsou xyyyx,yxyx,yyxyx. Koncový vzor σ je
xyyxyyxyyxxyxy. Tyto čtyři posloupnosti dávají přesně
λ=x2,y2,y3,x3,y1,y1,x1,y2,y3,x3,x1,y2,x3,y1
aρ=y3,y2,y3,x1,x3,x2,y1,y1,y3,y2,y1,x3,x2,x1.
Kontrola příkladu byla ruční, bez dalšího běhu.

## 22(c): vážená identita a přísná kladnost

Vnitřní sloupec j→k ponechá váhu w_j/w_k. Přechodový sloupec
se rozdělí na j→0 a0→k; jejich váhy z_j/z_0 a z_0/z_k se
vynásobí na z_j/z_k. Proto w(π)=w(l(π))w(r(π)).

V jednom bloku s p_j sloupci0→j a q_j sloupci j→0 se všechny
ostatní výskyty w_j vyruší na váhu
∏_j(w_j/z_j)^(p_j−q_j). Pomocné z_0 se vyruší díkyΣp_j=Σq_j=p.
Položme u_j=w_j/z_j, tedy |u_j|=1. Počet z(b) a sečtení přes
oba vektory p_j,q_j dává vážený součet levého bloku

p!(N_L−p)!/∏_(j∈L)n_j!
 · |Σ_(Σ_L p_j=p) ∏_(j∈L) choose(n_j,p_j)u_j^p_j|².

Komplexní sdružení je oprávněné, protože u_j^−1=conjugate(u_j).
Stejně pro H. Vynásobení obou čtverců a součet přes společné p
dávají přesně vzorec zadání s koeficientem
p!²(N_L−p)!(N_H−p)!/∏n_j! a s vnitřními podmínkami
Σ_L p_j=Σ_H p_j=p. Všechna sčítání jsou konečná. Člen p=0
má vnitřní součet1 a kladný faktoriálový koeficient; celý součet
je tedy reálný a přísně kladný, nejen nezáporný.

## 23: DNA a pětipísmenná výjimka

Stejné přeuspořádání pozic původního i nového slova zachová počet
rozdílů a permutuje množinu možných nových slov. Původní slovo
lze proto předpokládat seřazené. Náhodná permutace označených bází
dává každému neoznačenému slovu stejných∏n_j! označení, tedy uniformitu.

Pro t=2,m=4 zvolme w_1=w_3=z_1=z_2=1 a
w_2=w_4=z_3=z_4=−1. V obou blocích má rozdílná dvojice poměr w
rovný−1; mezi bloky je poměr z rovněž−1; shodná dvojice má váhu1.
Proto w(π)=(−1)^d. Kladnost z22(c) říká počet sudých d minus
počet lichých d>0, což dokazuje přesně požadovanou přísnou převahu.

U pěti různých písmen je počet slov s d změněnými pozicemi
choose(5,d)D_d, kde D_d jsou derangements. Rekurence
D_d=(d−1)(D_(d−1)+D_(d−2)), D_0=1,D_1=0, plyne rozlišením,
zda prvek poslaný na místo1 tvoří s1 dvojcyklus nebo delší cyklus.
Dává D_2=1,D_3=2,D_4=9,D_5=44, tedy přesně tištěné počty
1,0,10,20,45,44. Sudých je56, lichých64, skutečný protipříklad.

Explicitní Laguerreův polynom v historické poznámce souhlasí s
Rodriguesovým výrazem e^x x^−α/n! ·(d/dx)^n(e^−x x^(n+α)):
Leibnizovo pravidlo dává koeficient choose(n+α,n−k)(−x)^k/k!.
Historické tvrzení o obsahu citovaných článků nebylo ověřeno;
žádná konkrétní integrální identita v tomto odstavci formulována není.
Parita je nezávisle dokázána výše.

## 24(a): zobecněné třídění a jednoznačné vytažení sloupce

Transpozice vždy prohodí horní hodnoty w,x; dolní y,z buď ponechá,
nebo prohodí podle R. Po opakování se nezmění žádná z neuspořádaných
dvojic, tedy ani rozhodnutí R; operace je involuce, i v případech
shodných horních či dolních hodnot. Každá třídicí transpozice
zmenší počet horních inverzí o1, takže algoritmus skončí.

Opravené pravidlo bere nejpravější inverzi, nikoli největší x_j.
Má-li vstup první sloupec x/y, nejprve se úplně setřídí jeho suffix:
každá inverze uvnitř suffixu má větší index než hranice s prvním
sloupcem. Poté se x posune doprava přes právě ty horní hodnoty,
které jsou menší než x. Stane se tak nejlevějším x v hotovém horním řádku.

Proto lze z výsledku jednoznačně obnovit y i setříděný suffix:
vezmeme nejlevější horní x a inverzními transpozicemi jej přesuneme
zcela doleva. Zbývající horní řádek zůstane seřazený. Tento postup
je současně existence i jednoznačnost požadovaná v(a), pro libovolné R.

## 24(b): cykly v opravené konvenci a pravé závorkování

Podle opravy2006 cyklus(c_1…c_s) odpovídá nesetříděnému
dvouřádkovému poli s horním řádkem c_s,c_1,…,c_(s−1)
a dolním c_1,…,c_s. Toto pole vstupuje do operace sort v součinu;
není dovoleno jej předem samostatně setřídit a tím změnit závorkování.
Právě toto odpovídá poli11, jemuž je přiřazen cyklus(x_2…x_n x_1).

Začneme v nejmenší horní hodnotě y a vytáhneme ji postupem(a).
Je-li emitovaný dolní prvek c≠y, vytáhneme dále horní c atd.,
až se poprvé emituje y. Po každém neuzavřeném kroku je rozdíl
četností horního a dolního zbytku e_c−e_y, takže požadovaný
další horní c určitě existuje. Konečný počet sloupců vynutí uzavření.
Všechny mezilehlé emitované prvky jsou>y a každý krok odstraňuje
jeden sloupec. Po uzavření jsou četnosti opět vyrovnané; pokračujeme
nejmenším zbývajícím y. Koncová minima proto neklesají.

Zpětné operace(a) rekonstruují přesně sort zřetězených syrových
cyklových polí. Protože nejpravější pravidlo vždy nejprve setřídí
pravý suffix, platí sort(A,B)=sort(A,sort(B)). Rekonstrukce je tedy
právě pravostranně závorkovaný součin v opraveném zadání.
V libovolném přípustném rozkladu je první minimum celkovým minimem;
jednoznačné vytažení(a) určí všechny prvky až do jeho prvního
návratu, tedy první cyklus i zbytek. Indukce dokazuje úplnou jednoznačnost.

Je-li R vždy nepravdivé, přesouvají se vždy celé sloupce a dostáváme
obyčejnou interkalaci. Je-li R vždy pravdivé, dolní řádek zůstane
beze změny: pouze se setřídí horní řádek. To je přesné znění známé
opravy dřívějšího příliš stručného „juxtaposition“.

Pro relaci „všechna čtyři písmena jsou různá“ dal jediný cílený
běh na poli12 cykly(ddbca),(cbba),(cdb),(db),(d), přesně tištěný
příklad; pravostranná rekonstrukce vrátila původní celé pole.
Záznam results/generalized-intercalation-example.json.

Neasociativitu lze doložit bez hledání: nechť R platí právě když
se horní a dolní neuspořádaná dvojice liší. Vezměme A s horním13
a dolním31, B=2/2,C=1/1. Přímé nejpravější transpozice dávají
(A⊗B)⊗C s horním1123 a dolním3211, ale A⊗(B⊗C) má dolní3112.
Rozdíl způsobí kroky s páry{1,3}/{1,2}, {2,3}/{1,2}, které dolní
řádek zachovají, oproti páru{1,2}/{1,2}, který jej prohodí.
Tentýž malý svědek byl součástí jediného cíleného běhu, nikoli enumerace.
