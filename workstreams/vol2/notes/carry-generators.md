# §3.2.1.1-12 až 14: generátory s přenosem nebo výpůjčkou

Kontrola 1. listopadu 2026. Zadání str. 16, odpovědi str. 545–547,
všechny historické vrstvy errat. **V2-C0005** je neplatné mezitvrzení
v 12(d); hlavní radixová identita má níže nezávislý důkaz.
Ostatní kontrolované formule po známých opravách souhlasí.

## Společný model a hlavní identita

Nechť `b>=2` je základ číselné soustavy, `k>=1` počet uchovávaných cifer,
`a_1,...,a_k` celočíselné koeficienty, `x_n` cifry v `0,...,b-1`
a `c_n` celočíselný přenos. Při záporných `c_n` jde o výpůjčku.
Z počátečních `x_-1,...,x_-k,c_0` se pro `n>=0` počítá

```text
u_n = sum_(j=1)^k a_j*x_(n-j) + c_n,
x_n = u_n mod b,     c_(n+1) = floor(u_n/b).                (1)
```

Zápis `(d_1...d_j)_b` znamená `sum_(i=1)^j d_i*b^(j-i)`.
Položme `H_j(n)=(x_(n-1)...x_(n-j))_b`,
`m=sum_(j=1)^k a_j*b^j-1` a `M=abs(m)`. Číslo `m` je nenulové,
protože `m=-1 (mod b)`; zároveň `gcd(b,M)=1`.
Znaménko `s=sign(m)` je 1 při kladném `m`, jinak -1. Definujme

```text
X_n = s*(sum_(j=1)^k a_j*H_j(n) + c_n).                   (2)
```

To je opravený vzorec z úlohy 14: délka bloku je `j`, nikoli `k`.
Pro přechod platí `b*H_j(n+1)=H_j(n)+b^j*x_n-x_(n-j)`.
Sečtením a použitím (1) dostáváme přesnou celočíselnou identitu

```text
b*X_(n+1) = X_n + M*x_n.                                 (3)
```

Jestliže `0<=X_0<M`, indukce z (3) dává `0<=X_n<M` a
`X_(n+1)=b^(-1)*X_n mod M`; inverze existuje díky nesoudělnosti.
V každém kroku je na pravé straně (3) nezáporné číslo menší než `b*M`.
Tento důkaz nepotřebuje předpokládat periodickou inicializaci cifer.

Přenosy mají též přesnou invariantní mez. Označme
`C_-=sum_j min(0,a_j)`, `C_+=sum_j max(0,a_j)`. Je-li
`C_-<=c_n<C_+`, pak `b*C_-<=u_n<b*C_+`, tedy po podlaze
`C_-<=c_(n+1)<C_+`. Tím je dokázána mez uvedená v odpovědi 14.
Případ všech nulových koeficientů má prázdný interval pro tuto
podmíněnou mez; hlavní identita (3) nadále platí a `M=1` je triviální.

## Radixový rozvoj bez sporného prodloužení výpůjček

Kongruenční stavy `X_n` lze jednoznačně prodloužit na všechna celá `n`,
protože násobení `b` modulo `M` je permutace. Pro záporná `n` definujme
výstupní cifru vztahem `x_n=(b*X_(n+1)-X_n)/M`; je to celé číslo
v `0,...,b-1`. Pro nezáporná `n` je shodné s (1), jak už dokazuje (3).
Opakováním rovnosti (3) zpět dostaneme pro každé `h>=1`

```text
X_n/M = sum_(i=1)^h x_(n-i)/b^i + X_(n-h)/(M*b^h).        (4)
```

Poslední člen leží v `[0,b^(-h))`, takže v limitě jde přesně
o rozvoj `(.x_(n-1)x_(n-2)...)_b`. Při nulovém stavu volíme nulové
cifry, nikoli alternativní rozvoj končící nekonečnými ciframi `b-1`.

Tento postup dokazuje konečný závěr 12(d) i obecnou verzi v 14.
Původní dodané záporné cifry se nemusejí rovnat periodicky prodlouženým
výstupům. Zvláště nelze bez další podmínky periodicky předefinovat pouze
záporné indexy a tvrdit zachování všech původních výpůjček včetně `c_0`:
[V2-C0005](C0005-borrow-periodic-extension.md) dává přesný protipříklad
pro desetinný počátek `X_0=1`. Důkaz (4) nevyžaduje
žádnou takovou vlastnost počáteční reprezentace.

## Úloha 12: odečítání starší a novější cifry

Zvolme `0<l<k`, koeficienty `a_k=1`, `a_l=-1` a ostatní nulové.
Pro `c_n=-b_n` je přenos reprezentován bitem `b_n` v `{0,1}` a (1) dává

```text
x_n = (x_(n-k)-x_(n-l)-b_n) mod b,
b_(n+1) = [x_(n-k)-x_(n-l)-b_n<0],
M=b^k-b^l-1,    X_n=H_k(n)-H_l(n)-b_n.                   (5)
```

Hranaté závorky jsou indikátor podmínky. Identita
`b*(b^(k-1)-b^(l-1))=M+1` dokazuje, že násobitel je
`b^(k-1)-b^(l-1)`. Pro `b=10,k=10,l=3` je to **999999900**.
Nadbytečná nula ve starém vystaveném mocněnci byla opravena roku 2010;
plus před `b_n` v obecné verzi (5) bylo opraveno na minus roku 2007.

Pro papírové násobení deseti použijme `10^10=10^3+1 (mod M)`.
Cyklická rotace cifer a přičtení `x_9*10^3` tedy zachovávají správný
zbytek. Přenos přes nejvyšší pozici se znovu nahradí hodnotou `10^3+1`.
Každé takové převedení zmenší celé číslo o kladný násobek `M`, proto
proces skončí. Výsledek může být v `[M,10^10)`, jak kniha připouští.
Oba uvedené příklady dávají přesně `M+1` a pak `M+10`.

Při dělení deseti napišme vstup `X=10*q+r`, `0<=r<10`.
Opačná rotace a odečtení odpovídají číslu
`q+r*10^9-r*10^2=(X+r*M)/10`. Pro `0<=X<M` je tento výraz opět
v `[0,M)`, kongruentní s `10^(-1)*X`; záporná výpůjčka tedy nepřeteče
přes nejvyšší cifru. Uchovávání výpůjčky místo jejího okamžitého
šíření vede přesně k rekurenci (5).

Pro kontrolu druhé reprezentace v odpovědi 12(c) sečtěme tři po sobě
jdoucí rekurence s vahami `1,10,100`. Členy výpůjčky se teleskopicky
zruší, kromě `-b_n+1000*b_(n+3)`. Dostaneme

```text
X_n = 1000*(x_(n-1)...x_(n-7))_10
      + (x_(n+2)x_(n+1)x_n)_10 - 1000*b_(n+3),
```

což souhlasí s prvním vystaveným výrazem. Obvyklé dělení `U/M` deseti
dává další cifru `floor(10*U/M)` a nový zbytek `10*U mod M`.
Identita (4) proto také dokazuje jejich opačné pořadí při generování
inverzními mocninami deseti, bez výpočtu celé periody.

## Úloha 13: obrácené pořadí odečítání

Nyní `a_l=1`, `a_k=-1`, ostatní koeficienty nula. Podepsaný modul
obecné formule je záporný: `m=-(b^k-b^l+1)`. Pro `c_n=-b_n` vyjde

```text
x_n = (x_(n-l)-x_(n-k)-b_n) mod b,
M=b^k-b^l+1,    X_n=H_k(n)-H_l(n)+b_n.                   (6)
```

Násobitel je `M-(b^(k-1)-b^(l-1))`; v desetinném příkladu tedy
8999999101. Obecná identita (3) potvrzuje i znaménko plus v (6).
Sčítání tří rekurencí dává alternativní výraz
`1000*(x_(n-1)...x_(n-7))_10-(x_(n+2)x_(n+1)x_n)_10+1000*b_(n+3)`.
To odpovídá sazbě po opravách indexů 1999 a 2007.

Zápis se třemi negovanými posledními ciframi znamená, že se jejich
obvyklá hodnota odečítá od horního bloku. Příklad
`9876544000-790=9876543210` souhlasí. Násobení deseti s využitím
`10^10=10^3-1 (mod M)` přesune nejvyšší cifru `x_9` na negované místo
jednotek a novou cifru na místě tisíců udělá `x_9-x_2`.
Opačná operace udělá `x_0-x_3` na negovaném místě stovek. Dosazením
vážených ciferných součtů se oba uvedené předpisy ověří přímo;
normální přenosy mohou upravit reprezentaci, nikoli zbytek.

## Úloha 14: obecná verze a konkrétní prvočíslo

Mírné zobecnění na libovolný základ nejvýše velikosti slova plyne
z (5) a (6); dělení základem na dvě části lze nahradit porovnáním
a případnou opravou, protože součet/rozdíl cifer má omezený rozsah.
Obecnou verzi dokazují (1)–(4). Pro dva kladné jednotkové koeficienty
na pozicích `l,k` je `M=b^k+b^l-1`, přenos v `{0,1}` a vznikne
generátor s přičítáním a přenosem uvedený v odpovědi.

V konkrétním příkladu `b=2^31`, `D=65430` je

```text
M=D*b^2+b-1=301742616185706138042367,
M-1=2*3^2*13*583537*12321391*179346397.
```

Rekurzivní Lucasův certifikát (kritérium vysvětlené v
[poznámce k tabulce](modulus-arithmetic.md)) dokazuje prvočíselnost `M`
i potřebných faktorů. Přesné mocnění dává `b^((M-1)/2)=1 (mod M)`
a nenulovou odchylku od 1 pro exponent `((M-1)/2)/q` při každém
prvočíselném faktoru `q` čísla `(M-1)/2`. Řád `b` i jeho inverze je
tedy přesně `(M-1)/2`; to je perioda všech **nenulových** počátků.
Nulový počátek je samozřejmě pevný bod.

Pro kontrolu spektrálního komentáře definujme `v_t` jako nejmenší
eukleidovskou délku nenulového celočíselného vektoru
`h=(h_0,...,h_(t-1))` s `sum_i h_i*a^i=0 (mod M)`, kde `a=b^(-1) mod M`.
Takový vektor určuje rovnoběžné nadroviny obsahující normalizované
t-tice generátoru; jejich rozestup je `1/||h||`. Nejkratší vektor tedy
odpovídá největší mezeře. To je přesná veličina používaná později v §3.3.4.

Zde je přesně `v_2=sqrt(b^2+1)`: vektor `(1,-b)` vztah splňuje.
Kratší vektor by měl `|h_i|<=b` a `b*h_0+h_1` absolutně menší než `M`,
tedy nulový. Jeho nejmenší nenulové řešení má právě uvedenou délku.
Obdobně `v_3=sqrt(D^2+2)`, dosažené vektorem `(D,1,-1)`.
Pro kratší vektor by `|h_i|<=D`; pokud `|h_0|<D`, je
`h_0*b^2+h_1*b+h_2` menší než `M` v absolutní hodnotě, a musí být 0.
Protože `b>D+1`, omezené koeficienty pak musejí být všechny nulové.
Pokud `|h_0|=D`, zbývá pro součet čtverců ostatních složek nejvýše 1,
což nestačí k doplnění na `±M`: potřebovali bychom složky `(±1,∓1)`.

Hodnoty přibližně `2.15*10^9` a `65430` vysvětlují malé absolutní
rozestupy v prvních dvou netriviálních dimenzích. Současně ukazují,
proč nejde o dobrý násobitel vzhledem k obrovskému modulu: pro jiný
násobitel `q=floor(sqrt(M))=549311037742` je už `v_2>=q/2`.
Kratší vektor by totiž měl `|h_0+q*h_1|<q*(q+1)/2<M` a rovnost
`h_0=-q*h_1` by byla při této délce nemožná. Dolní mez je více než
stokrát větší než `v_2` původního násobitele. Není tím tvrzena
optimalita `q`, jeho maximální perioda ani prověření celého §3.3.4.

## Errata a reprodukce

K těmto odpovědím byly zapracovány změny:

- str. 546, 3. 7. 2010: mocněnec 999999900;
- str. 546, 28. 9. 2002: odstraněné zdvojené slovo;
- str. 546, 24. 11. 2007: minus před výpůjčkou v 12(e), správné indexy
  výpůjček v rekurenci 13;
- str. 546, 19. 2. 1999: prostřední negovaná budoucí cifra má index `n+1`;
- str. 547, 1. 12. 2007: v součtu úlohy 14 končí j-tý blok cifrou `x_(n-j)`;
- str. 547, 13. 5. 2016: `lambda` definována jako nejmenší kladný exponent.

Relevantní sazba historických errat byla zobrazena; všechny pozdější vrstvy
včetně aktuálního TeXu prohledány. Nový problém v 12(d) se těmito změnami
neodstraňuje. Dřívější tvrzení v 12(e) s plus místo minus má přesný
protipříklad při `b=3,k=2,l=1`, počátečních cifrách `(0,2)` a výpůjčce 1.
Modul je 5, násobitel 2; správný stav je 1 a další stav 2.
Chybný výraz s plus dává počáteční stav 3 a další stav opět 2,
ale kongruenční přechod by z 3 dal 1. Obecné odvození (5) dokazuje
správné znaménko pro všechny přípustné parametry.

[Validátor](../verify_carry_generators.py) a [výsledky](../results/carry-generators.json):
101 497 stavů obecné formule, 104 124 kontrol mezí přenosu, 84 324 stavů
obou výpůjčkových variant, 1000 desetinných stavů s oběma reprezentacemi
a kontrolou rozvoje, 10 005 vstupů rotace; navíc certifikát prvočíselnosti
a přesného řádu velkého příkladu. Zvláštní nezávislý malý skript
ověřuje [C0005](../results/borrow-extension.json). Obecné důkazy výše
platí i mimo konečné testovací rozsahy.

```sh
python3 workstreams/vol2/verify_carry_generators.py
python3 workstreams/vol2/verify_borrow_extension.py
```
