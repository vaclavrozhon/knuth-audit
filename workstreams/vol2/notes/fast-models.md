# §4.3.3: výpočetní modely a úlohy 12–13

Kontrola 2.11.2026. Původní strany311,317 a634 vizuálně přečteny.
Doplňujeme konstrukční detaily horních mezí, nikoli důkaz optimality.
Historické zdroje jsou dále součástí kontextu oddílu.

## Velikosti a rekurze na str.311

Píšeme lg pro logaritmus o základu2, K=2^k pro délku transformace,
l pro počet vstupních bitů v bloku a m pro zlomkovou přesnost.
Vezměme l=k, m=6k a nejmenší k s 2n<=k2^k. Potom kK=Theta(n)
a k=Theta(lg n). Kvůli celočíselnému k nemusí vždy platit pomocná
mez kK<4n z předchozího rozboru; platí však kK<4kn/(k−1)<=8n
pro k>=2, což zde stačí. Malé délky se násobí přímo.

Celý algoritmus má O(Kk) operací s m-bitovými čísly, takže
T(n)=O(n T(lg n)). Konstantu6 a pomocné bity lze absorbovat
rozdělením operandů na konstantně mnoho bloků. T zde znamená cenu
zvoleného multiplikátoru včetně takového rozdělení; netvrdíme,
že libovolná monotónní funkce splňuje T(6x)=O(T(x)).

Opakované dosazení dává knižní součin
`C n (C lg n)(C lg lg n)...`. Zaokrouhlení logaritmických délek
se absorbují v konstantě pro každý stupeň. Rekurze končí při
argumentu nejvýše2. Známé erratum29.1.1998 mění původní mez1
na2; erratum8.11.1997 přečísluje rovnici52 na53. Dříve ověřený
chybový odhad FFT dovoluje m=6k pro dostatečně velká k.

## Náhodný přístup s logaritmickou cenou adresy

Nechť B=2^ceil(m/12). Tabulka součinů dvou B-cifer má B^2=2^k
nebo2^(k+1) položek. Každý následující součin v řádku vznikne
přičtením prvního operandu. Výpočet i uložení položky stojí O(k),
včetně adresy a délky výsledku. Celá tabulka stojí O(kK)=O(n).

Aritmetika s dvanácti ciframi používá konstantní počet tabulkových
násobení a operací s O(k) bity. Jedna operace tedy stojí O(k),
celá FFT O(Kk^2)=O(n log n). Nepředpokládáme jednotkovou cenu
pro libovolně dlouhé adresy nebo celá čísla.

## Uzly a aritmetika ukazatelového stroje

Ukazatelový stroj znamená přesně sedm druhů operací ze zadání12.
Uzel je záznam s pevným počtem odkazů na další uzly; adresa uzlu
nemá aritmetický význam. Změna nebo sledování odkazu stojí jeden
krok. Počet příchozích odkazů na jeden uzel není omezen.

Vytvoříme řetězec N uzlů, pro účely důkazu označených0,...,N−1.
Při průchodu pomocný ukazatel postoupí jednou za dva hlavní kroky;
tím zapíšeme floor(p/2) a paritu p. Pomocný ukazatel postupující
dvakrát rychleji vytvoří odkazy na2p. Cena je O(N). Odkazy mimo
rozsah lze označit koncovým uzlem; v simulaci jsou následník
a dvojnásobek cyklické modulo N. Jde jen o konvenci pro okraj,
který stručný hint nerozepisuje.

Dělení dvěma a parita převedou p na binární seznam v O(log N)
krocích. Opačný převod používá dvojnásobek a následníka. Bitové
sčítání je konečný automat s přenosem, školní násobení má
O(log^2 N) kroků. Dostaneme součet modulo N a přenos nebo obě
cifry součinu. Pro obecné N lze po binárním součtu odečíst N;
v aplikaci je N mocninou2 a hranice cifer je hranicí seznamu.

## Seskupení operací

Vezměme N=2^ceil(m/13). Číslo pevné přesnosti zabírá13 cifer
a znaménko. Větší dočasné součiny potřebují stále konstantně mnoho
cifer. Motýlek FFT se přeloží na pevně omezený počet instrukcí
s nejvýše dvěma N-ciframi; přenosy a znaménka mají konstantně mnoho
stavů. Celá třinácticiferná čísla se nesmějí považovat za dva klíče
s N možnostmi: operace se rozloží na jednotlivé cifry.

K připravených instrukcí stabilně setřídíme podle druhé cifry,
první cifry a kódu operace. Každý hodnotový uzel má dva pomocné
odkazy pro začátek a konec zásobníku. Vložení používá přímo
ukazatel položky a stojí O(1), bez hledání adresy. Průchod řetězcem
N hodnot spojí zásobníky a vymaže pomocné odkazy. Cena je O(K+N).

Po setřídění je nejvýše O(N^2) skupin. Aritmetiku spočteme pro
skupinu jednou za O(log^2 N) a výsledek rozešleme jejím položkám.
Cena společného kroku je O(K+N^2 log^2 N). Počet společných kroků
na motýlek je konstanta. Z m=6k máme N^2<=4*2^(12k/13), tedy
N^2 log^2 N=O(2^k)=O(K). Konstanta může být velká. Jeden průchod
FFT stojí O(K), všech k průchodů O(Kk)=O(n).

Do této meze se vejde také příprava. Základní kořeny spočteme
polynomiálně v k bitových operací, což je O(n). Jejich K mocnin
vznikne v k vrstvách zdvojování, opět s uvedeným seskupením.
Seznamy motýlků, propojení vrstev a obrácení bitů lze vytvořit
průchody binárního stromu v O(Kk) uzlech a krocích. Čtení, balení
vstupu, přenosy a zápis výsledku stojí O(n). Tím je dokázána mez
pro celý algoritmus, nikoli jen jednu vrstvu FFT.

[Primární abstrakt Schönhage1980](https://epubs.siam.org/doi/abs/10.1137/0209036?journalCode=smjcat)
potvrzuje název *Storage Modification Machines*, SICOMP9(3),490–508
a větu o lineárním násobení. Vyhledávač poskytl vydavatelský abstrakt;
přímé otevření skončilo timeoutem. Úplný článek nebyl přečten.
Výše uvedený konstrukční důkaz je samostatný rozbor úlohy.

## Úloha13: rozdílné délky

Nechť 1<=m<=n, U<2^m, V<2^n a B=2^m. Rozepišme V=sum v_i B^i
do h=ceil(n/m) bloků. Spočteme h součinů P_i=Uv_i. Pro skládání
stačí přenos c_0=0 a kroky

```
w_i = (P_i+c_i) mod B,   c_(i+1)=floor((P_i+c_i)/B).
```

Indukčně c_i<B, protože P_i<=(B−1)^2. Každý krok pracuje s O(m)
bity a celkem stojí O(hm)=O(n+m), bez opakovaného sčítání celého
rostoucího výsledku. Cena je ceil(n/m) T(m)+O(n+m).

Dosazení tří tehdejších mezí dává přesně odpověď13:
O(n log m log log m) pro páskový Turingův stroj, O(n log m) pro
popsaný náhodný přístup a O(n) pro ukazatelový stroj. Z doplněného
výsledku Harvey–van der Hoeven2021 plyne i O(n log m) na Turingově
stroji. Jde o platnou horní mez, nikoli tvrzení o nejlepším výsledku
k dnešnímu dni. Pro malé m nahradíme logaritmické výrazy konstantou.

## Reprodukovatelné kontroly a errata

`verify_fast_models.py` je referenční simulace uzlů, nikoli překlad
do sedmi strojových instrukcí. Přístupy k zásobníkům používají
odkazy; číselné popisky uzlů slouží pouze nezávislému orákulu.
Běh skončil exit0:10920 operací pro všechny dvojice cifer v bázích
2,4,...,64;1140 seskupených instrukcí včetně duplikátů;480
nesymetrických násobení do103425bitů. Oba checkpointy prošly.
Tyto konečné kontroly doplňují obecné důkazy výše.

Prohledány všechny čtyři vrstvy errat podle stran311,317,634,
ukazatelových strojů, logaritmů a čísel úloh. Změny12/13 nenalezeny;
relevantní jsou uvedená oprava ukončení logaritmů, doplnění
výsledku2019/2021 a následná oprava jeho svazku193.
