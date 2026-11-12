# §4.5.2: přesné délkové třídy, úlohy20–22

Originály zadání354–355 a odpovědí642–643 byly zobrazeny. Předpoklad
o počtu posunů je zkontrolován také proti programuB a jeho definici D
na339–340. Čtyři vrstvy errat prohledány2026-11-02; u20–22 nebyla
nalezena změna. Nový nálezC0123 se týká přesného průměruD v odpovědi22.

## Úloha20: obecný přesný počet jednoho kroku

Třída A_m obsahuje kladná lichá u s floor(lg u)=m; lg je logaritmus
o základu2. A_0={1}, jinak A_m={2^m+1,2^m+3,...,2^(m+1)-1}.
Počet jejích členů je1 pro m=0 a2^(m-1) pro m>=1.
Cyklus pro u>v nahradí u lichou částí u-v, druhý argument ponechá.
Při u=v algoritmus skončí; tento stav je třeba počítat samostatně.

Nechť nejprve m>=n>=1 a M=2^(m-1), N=2^(n-1). Pišme
`u=2M+2a+1`, `v=2N+2c+1`, kde0<=a<M,0<=c<N. Pro kladný rozdíl
u-v=2s je počet uspořádaných dvojic přesně

```text
K(s) = (s-M+2N)_+ - (s-M+N)_+
       - (s-2M+2N)_+ + (s-2M+N)_+,
y_+ = max(y,0).
```

Vzorec plyne spočtením průniku intervalů pro a-c=s-M+N, nebo
konvolucí dvou konečných posloupností jedniček. Má trojúhelníkový
nebo lichoběžníkový průběh. Pro m=n je K(s)=M-s pro1<=s<M;
negativní rozdíly mají symetrické počty a s=0 má M dvojic.

Každé kladné s má jediný zápis s=2^h*w s h>=0 a lichým w.
Počet přechodů z(m,n) do(r,n) tedy je

```text
sum_{h=0}^m sum_{w in A_r} K(2^h*w).
```

Vyšší h již nemohou přispět, protože K(s)=0 pro s>=2M-N.
Pro m=n se přidá symetrická možnost(n,r) a pravděpodobnost zastavení1/M.
Pro m>n jsou všechny původní rozdíly kladné.

Následující uzavřený výpočet vnitřního součtu dovoluje vyhodnotit
vzorec pro libovolné m,n bez výčtu jednotlivých vstupů. Pro r=0 položme
L=R=0; pro r>=1 položme L=2^(r-1),R=2^r-1, takže w=2a+1.
Pro libovolný celočíselný práh c a h>=0 definujme

```text
l = max(L, floor((c-2^h)/2^(h+1))+1),
J = max(0,R-l+1),
F(r,h,c) = J*(2^h*(l+R+1)-c).
```

Potom F je přesně součet `(2^h*w-c)_+` přes A_r: je to aritmetická
řada od prvního kladného členu. Do počtu přechodů tedy dosadíme
F pro čtyři prahy M-2N, M-N,2M-2N,2M-N se znaménky+,-,-,+.
Zbývají konečné geometrické řady v h. Vyhodnocení dává tyto
pravděpodobnosti, shodné s tištěnou odpovědí:

| Případ | Výstup | Pravděpodobnost |
|---|---|---|
| m=n>0 | (n-t,n),2<=t<n; také symetricky | t/2^t-5/2^(t+1)+3/2^(2t) |
| m=n>0 | (0,n); také symetricky | n/2^(n-1)-1/2^(n-2)+1/2^(2n-2) |
| m=n>0 | stop | 1/2^(n-1) |
| m=n+1,n>1 | (n,n) | 1/8 |
| m=n+1 | (n-t,n),1<=t<n-1 | 11/2^(t+3)-3/2^(2t+1) |
| m=n+1,n>1 | (1,n) | 5/2^(n+1)-3/2^(2n-1) |
| m=n+1 | (0,n) | 3/2^n-1/2^(2n-1) |
| m>=n+2,n>=1 | (m-1,n) | 1/2-3/2^(m-n+2)-[n=1]/2^(m+1) |
| m>=n+2 | (m-t,n),1<t<n | 1/2^t+3/2^(m-n+t+1) |
| m>=n+2,n>1 | (m-n,n) | 1/2^n+1/2^m |
| m>=n+2 | (m-n-1,n) | 1/2^(n+1)+1/2^(m-1) |
| m>=n+2 | (m-n-t,n),1<t<m-n | 1/2^(n+t) |
| m>=n+2 | (0,n) | 1/2^(m-1) |

Hranatá závorka je indikátor uvedené podmínky. Neuvedené přechody mají
pravděpodobnost0. Pro m=n=0 je zastavení jisté. Pro m>n=0 dává
u-v=u-1 dvojice(m-t,0) s pravděpodobností2^-t pro1<=t<m a(0,0)
s pravděpodobností2^(1-m). Zvláštní případ m=2,n=1 z druhé skupiny
dává výstup(0,1) jistě; řádek s1/8 se zde nepoužívá.

Pro kontrolu algebraického zjednodušení tabulky lze použít rekurzi
K_(2M,2N)(2s)=2K_(M,N)(s). Příspěvek sudých s po zdvojení obou
intervalů je polovinou staré pravděpodobnosti, lichá s přidají
`sum_{w in A_r}K_(2M,2N)(w)/(4MN)`, počitatelný stejným F.
Například na diagonále a při pevném r>=1, t=n-r>=2, vychází
`p_t=p_(t-1)/2+2^-t-3*4^-t`, p_1=0. Sečtením získáme
`p_t=2^-t*(t-5/2+3*2^-t)`, první řádek tabulky. Ostatní řádky
vznikají stejným součtem čtyř aritmetických řad, s mezemi určenými
čtyřmi uvedenými prahy. Tato přesná konstrukce nevyžaduje žádný
předpoklad náhodnosti mezivýsledků při více cyklech.

## Úloha21: pevný menší argument

Nechť v je pevné kladné liché číslo a u je rovnoměrně vybrané z A_m.
Nejprve zkoumejme redukci, dokud aktuální hodnota x nepoklesne na x<=v.
Jeden elementární krok je

```text
epsilon_j = x_j mod2,
x_(j+1) = (x_j-v*epsilon_j)/2.
```

Tento krok provede jeden posun a právě při lichém x také jedno
odečtení. Seskupením po sobě jdoucích posunů dostaneme původní
subtract-and-shift cykly; přerušení skupiny na hranici x<=v může
změnit zbývající práci jen o konstantu závislou na v.

Po r krocích platí přesná identita

```text
u = 2^r*x_r + v*sum_{j=0}^{r-1} 2^j*epsilon_j,
u/2^r-v < x_r <= u/2^r.
```

Počet kroků T do dosažení x<=v je proto m+O_v(1), kde index v
označuje, že konstanta může záviset na v. Zbytek gcd pracuje se dvěma
čísly nejvýše v a stojí dalších O_v(1) odečtení i posunů. Počet
posunů je tak m+O_v(1) dokonce pro každý jednotlivý vstup.

Pro odečtení pokračujme pomocnou rekurzi formálně i za okamžik T,
případně do záporných čísel. Modulo2^m je posloupnost prvních m parit
v bijekci s u: `u = v*sum 2^j*epsilon_j modulo2^m`. Protože v je liché,
má modulo2^m inverzi. U rovnoměrných lichých reziduí u je epsilon_0=1
a zbývajících m-1 bitů jsou nezávislé rovnoměrné bity. Očekávaný
počet jedniček je1+(m-1)/2. Skutečný počet odečtení se od této pomocné
sumy liší o O_v(1), protože |T-m|=O_v(1) a závěrečná práce je omezená.
Tedy průměr odečtení je m/2+O_v(1).

Pro pevné n tvoří A_n konečnou množinu v; konstanty lze nahradit
jejich maximem. Dostáváme přesně `C_mn=m/2+O_n(1)` a
`D_mn=m+O_n(1)`. Důkaz nezaměňuje paritu na náhodně zastavené
trajektorii s nezávislými hody mincí: nezávislost byla použita na
pevně dlouhé pomocné trajektorii a rozdíl délek byl omezen samostatně.

## Úloha22: váhy a vedoucí koeficienty

Nyní N značí délku celkového vstupního intervalu1..2^N-1. Každé liché
číslo t z A_m má v tomto intervalu právě N-m předobrazů t,2t,4t,... .
Váha třídy je proto `(N-m)*2^(m-1)` pro m>=1 a N pro m=0.
Počet odečtení C závisí jen na lichých částech obou vstupů. Z těchto
vah a symetrie vznikne přesně tištěná identita na642.

Předpokládejme jako v zadání `C_mn=alpha*m+beta*n+gamma` pro m>=n>=1.
Po substituci a=N-m,b=N-n a vydělení4^N je vedoucí koeficient
z mimodiagonálních tříd

```text
(alpha+beta)*N * (1/4)*sum_{0<=a<b} a*b/2^(a+b).
```

Z geometrické řady a jejího derivování plyne
`sum a/2^a=2`, `sum a²/4^a=20/27`. Proto je poslední váha
`(4-20/27)/8=11/27`. Diagonální váha je `(20/27)/4=5/27`.
Členy s alpha*a,beta*b,gamma mají omezené součty, protože všechny
potřebné geometrické momenty konvergují. Ocas za a nebo b>=N je
exponenciálně malý i po násobení N. To dokazuje oba odhady v zadání
včetně O(1), nikoli pouze numerickou shodu koeficientů.

Po započtení symetrické poloviny je celková váha
`2*(11/27)+5/27=1`. Třídy m=0 nebo n=0 přispívají po normalizaci
jen O(N²*2^-N), neboť C_m0=O(m+1). Průměr je tedy
`(alpha+beta)*N+O(1)`. Tento závěr používá společný předpoklad
zadání22; uniformní dvouparametrový odhad neplyne sám z úlohy21,
kde n bylo pevné.

## C0123: pro D chybí počáteční posuny

První věta odpovědi22 na643 tvrdí stejnou přesnou identitu pro D.
To není pravda. Pišme původní vstupy jako2^a*u a2^b*v s lichými u,v.
B1 odstraní společnou mocninu2^min(a,b), ale B3 musí před první
subtrakcí odstranit ještě |a-b| faktorů2 z jediného sudého argumentu.
Tyto posuny jsou součástí D podle výslovné definice na340.
Správná bodová identita je

```text
D(2^a*u,2^b*v) = D(u,v)+|a-b|.
```

Pro N=2 jsou všechny vstupy1,2,3 a správný součet D přes devět dvojic
je8. Tištěné vážení lichých tříd dává4; chybí po jednom posunu pro
(1,2),(2,1),(2,3),(3,2). Průměr má být8/9, nikoli4/9.

Obecně označme M=2^N-1 a a,b exponenty2 náhodných vstupů.
Z počtu násobků2^k dostaneme

```text
E[a] = 1-N/M,
E[min(a,b)] = M^-2 * sum_{k=1}^{N-1}(2^(N-k)-1)^2,
E[|a-b|] = 4/3 + (8/3-2N)/M - 2N/M².
```

Poslední hodnota se musí přičíst k tištěnému váženému průměru.
Ekvivalentní chybějící člen v nenormalizované identitě je
`(4M²+(8-6N)M-6N)/3`. V limitě jde o4/3, tedy pouze O(1):
vedoucí asymptotické koeficienty zůstávají správné. Empirické konstanty
celého textu tím automaticky neopravujeme; jejich test je jiná otázka.

## Výpočty a rozsah

`verify_gcd_bins.py --resume`, relace52259, exit0; všechny tři
checkpointy prošly. `results/gcd-bins.json` a `.log`:

- 699051 přímých dvojic v66 třídách do m=10 ověřuje tabulku20.
  Dalších1176 tříd do m=48 je ověřeno nezávislým mřížkovým součtem F,
  bez výčtu exponenciálně mnoha vstupů.
- 16352 vstupů pro sedm pevných v ověřuje přesnou rovnoměrnost bitů
  pomocné trajektorie a její vztah ke skutečným počtům.
- 10923 lichých dvojic dává třídní průměry. Jejich vážení se porovnává
  s již dříve dokončeným nezávislým celkovým sčítáním pro N=1..8
  v `results/gcd-basic.json`; původní sčítání se neopakovalo.
  Identita pro C i opravená identita pro D platí přesně ve všech osmi
  případech. Generující funkce ověřuje samostatně váhy11/27 a5/27.

Obecné důkazy jsou výše. Konečné testy slouží jako kontrola přepisů,
okrajů a nezávislé aritmetiky, nikoli jako důkaz neomezených tvrzení.
