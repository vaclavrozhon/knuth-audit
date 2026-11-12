# Úvodní modelové mezery: s. 5 a dopředná úloha 5.2.1–38

6. listopadu 2026. Nové doplnění P0010/P0011, nikoli opakování jejich
již doloženého obsazovacího součtu. Originál s. 5/file16 a úloha105/file116
s odpovědí626/file637 byly prohlédnuty. Kontext je na99–102 a176–177.
Pravidlo z důkladných vzorů: oddělit správný podmíněný výsledek od
nevyřčených předpokladů a od případného neplatného univerzálního závěru.
Žádný nový nález. P0010/P0011 zůstávají partial z přesně uvedeného důvodu.

## P0378: počet bitů není automaticky čas každého třídění

Pro N různých binárně kódovaných klíčů stejné šířky w platí 2^w≥N,
tedy w≥ceil(lg N). Ani proměnná šířka neodstraní lineárně-logaritmický
objem dat: řetězců délky menší než l, včetně prázdného, je2^l−1.
Pro L=floor(lg N) proto součet délek splňuje

    Σ_i |K_i| ≥ Σ_(l=1)^L (N−2^l+1)
              = NL−2^(L+1)+2+L = N lg N−O(N).

Jde pouze o počet bitů. Násobení dalšími lg N vyžaduje, aby se tento
objem skutečně četl/přesouval v každém z tolika kol. Konkrétní svědek
pro knižní heuristiku: bufferový mergesort s N=2^k a klíči šířky w,
který v každé z k hladin fyzicky přepíše všechny klíče, vykoná přesně
Nwk bitových zápisů a O(Nwk) bitových operací při přímých porovnáních.
Pro w=Θ(lg N) tedy Θ(N(lg N)^2). Obecná šířka dává Θ(Nw lg N).

Kniha na s. 5 mluví o lepším časovém odhadu, nikoli o specifikaci
bitového stroje, reprezentace klíčů a práce s prefixy či ukazateli.
Právě tento rozdíl ponechává P0010 partial. Uvedený dolní odhad délky
ani cenu konkrétního mergesortu nevydávám za univerzální bitovou dolní
mez. Žádný nesouvisející radixový algoritmus nepoužívám jako nález.

## P0379: spojitá distribuční transformace, včetně plochých intervalů

Nechť F je spojitá CDF na reálné ose a X má toto rozdělení. Pro0<u<1
je q=sup{x:F(x)≤u} konečné: limity CDF jsou0 a1. Spojitost dává
F(q)=u a monotonie dává ekvivalenci F(x)≤u právě když x≤q. Tedy

    Pr(F(X)≤u)=Pr(X≤q)=F(q)=u.

Koncové hodnoty plynou limitou. Striktní růst F není potřebný;
případné ploché intervaly mají nulovou pravděpodobnost. Deterministické
transformace nezávislých X_i zůstávají nezávislé. F(X_i) jsou tedy iid
rovnoměrné na[0,1]. Důkaz nepotřebuje existenci hustoty.

## P0380: správnost košů a přesná nezakrytá cena

Pro N≥1 zvolme b_N(x)=min(N−1,floor(N F(x))). Je to neklesající funkce
do{0,…,N−1}, takže všechny klíče v nižším koši jsou nejvýše všechny
klíče ve vyšším koši. Proto seřazení podle původních klíčů uvnitř košů
a následné spojení košů vždy správně třídí, i pro rovnosti a ploché
úseky. Stabilitu lze zachovat pořadím vstupu. N=0 se vrací ihned.

Obsazovací výsledek EΣ_j n_j²=2N−1 z P0011 přebírám: transformace
výše doplnila chybějící obecný předpoklad jeho použití. Založení košů,
jejich spojení a vstup/výstup stojí O(N); přímé vkládání uvnitř koše
potřebuje O(n_j+n_j²) porovnání/přesunů. Je-li c_N(x) skutečná cena
určení b_N(x), při jednotkové ceně odkazu a porovnání klíčů je

    E T_N = O(N + Σ_(i=1)^N E c_N(X_i)).

Očekávaný lineární čas tak vyplývá při sup_N E c_N(X)<∞. To zahrnuje
jednotkově dostupnou přesnou transformaci a určení koše. Pouhá znalost
spojitého rozdělení nedodává algoritmus, jeho přesnost ani cenu; právě
tento předpoklad zůstává v P0011 partial. Pro obecné reálné klíče se
zvlášť předpokládá dostupné porovnání; bitový model není RAM.

## P0381: §5.2.1–38, průměrný čas pro hladkou hustotu

Použita známá oprava all3-prepre z22.5.2000: na105 jde o **průměrný**
čas, na626 o **asymptotickou ekvivalenci**, nikoli doslovnou konvergenci
rostoucího výrazu. Nejsou to naše nálezy. Pět vrstev errat je již
shromážděno v sources/insertion-errata-review.json; příslušné záznamy
byly znovu přiřazeny k tomuto argumentu.

Nechť F(x)=∫_0^x f(t)dt, f≥0, ∫_0^1 f=1, a f∈L²[0,1]. Pro M košů
stejné šířky položme p_j=∫_((j−1)/M)^(j/M) f. Počet neuspořádaných
dvojic uvnitř košů má střední hodnotu

    E Σ_j binom(n_j,2) = binom(N,2) Σ_j p_j².

To je součet indikátorů po dvojicích vstupních pozic: každá dvojice
je v témže koši s pravděpodobností Σp_j². Ekvivalentně dává binomické
rozdělení každého n_j přesně vytištěný levý součet odpovědi38.
Podmíněně na koši jsou dva iid spojité klíče v inverzi s pravděpodobností
1/2. Proto knižní počet inverzí B má

    E B = (1/2) binom(N,2) Σ_j p_j².

Cauchyova–Schwarzova nerovnost na každé buňce délky1/M dává
p_j²≤(1/M)∫_cell f²; po součtu Σp_j²≤||f||²_2/M. Při M=cN,
resp. celočíselném M s M/N→c>0, tedy E B=O(N). V přímém vkládání
je každý přeskočený uzel účtován k jedné inverzi a každé vložení má
nejvýše jeden závěrečný neúspěšný test. Správa seznamů a výpočet koše
floor(MK) stojí v modelu Programu M O(N+M). To samo dokazuje očekávaný
O(N) čas, aniž bych předbíhal detailní pozdější kontrolu každé MIX
instrukce. Také vytištěný součet7B+31N−3A+4M+2 s0≤A≤N je s tím
slučitelný; přesné koeficienty zatím nepovyšuji na nově ověřené.

Pro asymptotiku v odpovědi stačí ještě konkrétnější předpoklad:
f je spojitá na[0,1]. Označme f_M buněčný průměr M p_j. Uniformní
spojitost dává sup|f_M−f|→0, proto

    M Σ_j p_j² = ∫_0^1 f_M² → ∫_0^1 f².

Pravá konstanta je kladná (nejméně1), takže skutečně dostáváme
asymptotickou ekvivalenci v opravené odpovědi. Dokázaná podmínka
pro samotné O(N) je slabší L²; asymptotiku tu nezobecňuji bez důkazu
na libovolnou hustotu. N=0,1 má B=0 a nečiní problém.

Odkaz odpovědi na Theorem5.2.5T tvrdí jiný, silnější jednotný odhad
pro upravený dvouúrovňový algoritmus při omezené Riemannovsky
integrovatelné hustotě. Tento dopředný výrok na177 zde není dokázán
a je výslovně P0383 partial; uzavřena je výše uvedená část úlohy38,
nikoli všechny výroky celé odpovědní stránky nebo celého Programu M.

## P0382: proč samotná spojitost nestačí tomuto rozdělení do košů

Nejde o protipříklad obecného výroku s. 5, pouze o hranici konkrétního
algoritmu bez distribuční transformace. Pro F(x)=sqrt(x) na[0,1] je

    p_j=(sqrt(j)−sqrt(j−1))/sqrt(M),
    M Σ_j p_j² = Σ_(j=1)^M 1/(sqrt(j)+sqrt(j−1))².

Pro j≥2 je příslušný sčítanec mezi1/(4j) a1/(4(j−1)). Odtud
MΣp_j²=(1/4)ln M+O(1). Při M/N→c>0 dostáváme
E B~N ln N/(16c), nikoli O(N). F je spojitá, ale její hustota
1/(2sqrt(x)) není L². Znalost tohoto F a dostupná transformace
z předchozího oddílu stále mohou dát lineární algoritmus; žádný
neplatný přesun kvantifikátorů se proto neoznačuje jako knižní chyba.

Historické atribuce Karp/MacLaren/Tamminen nebyly znovu rešeršovány.
Žádný početní běh; staré úspěšné výpočty se neopakovaly.
