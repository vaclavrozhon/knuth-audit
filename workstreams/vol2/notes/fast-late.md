# §4.3.3: chirp transformace, počty součinů a paměť (16–18)

Kontrola 2.11.2026. Zadání318 a odpovědi634–635 byly vizuálně
přečteny, stejně jako relevantní erratum21.11.2020. Všechny tři
úlohy mají obecný důkaz níže a přesné kontrolní výpočty. Žádný
nový nález z tohoto bloku.

## Úloha16: libovolná délka transformace

Nechť K>=1 je délka, u_0,...,u_(K−1) vstupní komplexní čísla
a omega nenulový komplexní parametr. Transformovaný člen je
`hat_u_s=sum_(t=0..K−1) omega^(st) u_t`. Pro běžnou diskrétní
Fourierovu transformaci je omega=exp(2*pi*i/K), ale následující
identita nevyžaduje kořen jednotky.

Zvolme rho s rho^2=omega. Pak
`omega^(st)=rho^((s+t)^2−s^2−t^2)`. Znaménko odmocniny výsledek
nemění, protože celkový exponent je2st. Nechť L je nejmenší
mocnina2 větší než2K, takže L<=4K. Položme

```
a_t = rho^(−t^2) u_t          (0<=t<K), jinak0,
b_t = rho^((2K−2−t)^2)        (0<=t<L).
```

Cyklická konvoluce délky L je c_r=sum_(j=0..L−1) a_j b_((r−j)modL).
Potřebujeme pouze r=2K−2−s, tedy K−1<=r<=2K−2. Každý nenulový
člen má j<K, a proto0<=r−j<L. V požadovaných pozicích tedy
cyklická konvoluce přesně souhlasí s obyčejnou; přehnutí indexů
nepřidá žádný člen. Dostáváme

```
hat_u_s = rho^(−s^2) c_(2K−2−s).
```

Tři FFT délky L spočtou konvoluci v O(L log L)=O(K log K)
aritmetických operacích; pro K=1 stačí přímá odpověď. Mocniny
kvadratických exponentů se připraví v O(K) násobeních, protože
(t+1)^2−t^2=2t+1 a násobitel se dále mění konstantním faktorem
rho^2. Tato příprava se nesmí počítat jako K nezávislých mocnění.

Odmocninu lze zcela obejít, pokud má být omega proměnným vstupem
a počítáme jen sčítání,násobení,dělení. Pro trojúhelníkové číslo
B(t)=t(t−1)/2 totiž platí B(s+t)−B(s)−B(t)=st. Stejný důkaz
funguje s a_t=omega^(−B(t))u_t, b_t=omega^B(2K−2−t) a závěrečným
faktorem omega^(−B(s)). Postupné mocniny opět stojí O(K).

Případ omega=0 se řeší přímo: s konvencí polynomiálního vyhodnocení
0^0=1 je hat_u_0=sum u_t a hat_u_s=u_0 pro s>0. Záporné mocniny
z hintu se pro tento případ nepoužívají. Nejde o překážku tvrzení
pro libovolný komplexní parametr. Časová mez počítá operace nad
komplexními čísly; sama nedává bitovou přesnost ani numerickou
stabilitu při |omega| výrazně odlišném od1.

## Úloha17: přesný počet listových násobení

Označme K_n počet jednobitových, resp.jednociferných součinů
v doslovné Karatsubově rekurzi bez vynechávání nulových větví.
Platí K_1=1,K_(2n)=3K_n,K_(2n+1)=2K_(n+1)+K_n. Nechť
D_n=K_(n+1)−K_n. Odečtení sousedních rekurencí dává
D_1=2,D_(2n)=2D_n,D_(2n+1)=D_n.

Píšeme-li n=sum_(i=1..t) 2^e_i, kde e_1>...>e_t>=0 jsou pozice
jedniček v binárním zápisu, dostáváme
`D_n=2^(e_1−t+2)`: za každý bit0 po nejvyšší jedničce se D zdvojí,
za bit1 zůstává. Dále K_(2^e)=3^e. Pro0<=j<2^e je
D_(2^e+j)=2^(e+1−popcount(j)), kde popcount počítá jedničky.

Sečtěme D od2^e_1 do n−1. Interval zbytku po nejvyšší jedničce
rozdělíme podle dalších jedniček n na bloky délek2^e_i. V i-tém
bloku je i−2 pevně daných jedniček a e_i libovolných bitů; součet
2^(−popcount(j)) je proto2^(−(i−2))*(3/2)^e_i. Výsledkem je

```
K_n = 3^e_1 + sum_(i=2..t) 3^e_i 2^(e_1−e_i−i+3).
```

To je přesně tištěná odpověď. Lichost všech K_n plyne z rekurence.
Pro obdélníkový součin n-ciferného a(n+1)-ciferného operandu
stačí R_1=2,R_(2h)=2R_h+K_h,R_(2h+1)=R_h+2K_(h+1) součinů:
rozdělíme oba operandy po h cifrách v sudém případě, po h+1
v lichém. Vztah R_n=(K_n+K_(n+1))/2 potom plyne indukcí.

Pro formální mocninnou řadu K(z)=sum_(n>=1)K_n z^n oddělení
sudých a lichých indexů dává
`z K(z)+z^2=K(z^2)(z+1)(z+2)`. Formální zde znamená identitu
jednotlivých koeficientů, bez nutnosti dosadit konkrétní z.

Indukcí n<=K_n<=n^2, takže poloměr konvergence je1. V bodech
z=−1,1,−2 členy řady nejdou k nule a řada diverguje. Hodnoty2,1,1/5
v známém erratu21.11.2020 vznikají pouze algebraickým dosazením
do funkcionální rovnice, nikoli součtem řady. Výslovná poznámka
o lehkomyslnosti vůči konvergenci tento problém již přiznává.
Erratum je podle obsahu k odpovědi17, ačkoli lokátor říká16;
nezavádíme pro tuto drobnost samostatný nález.

## Úloha18: počet pracovních cifer

Nechť S_1=0,S_(2n)=S_n,S_(2n−1)=S_n+1 pro argument>1.
Je-li h=ceil(lg N), pak

```
S_N = popcount(2^h−N) = h−popcount(N−1).
```

První identita plyne z dělení deficitu dvěma: lichý argument
přidává právě jednu jedničku. Druhá je bitový doplněk v h bitech.
V notaci úlohy17 dostáváme S_N=e_1−e_t−t+2−[t=1]. Hranatá
závorka je1, když t=1, jinak0. Zejména S_N=O(log N).
Dále S_(n−1)<=S_n+1: při zvětšení deficitu o1 naroste jeho počet
jedniček nejvýše o1; případ přechodu přes mocninu2 mez nezhorší.

Níže jsou adresy relativní k začátku pracovní oblasti; operandy
leží mimo ni. Pišme N=2n−e,e v{0,1},B=2^n a
U=B U1+U0,V=B V1+V0. Dolní části mají n bitů, horní n−e.
Velikost pracovní oblasti je přesně3N+S_N datových bitů.

1. Rozdíly |U0−U1| a|V0−V1| uložíme do úseků[0,n),[n,2n).
   Jejich rekurzivní součin použije pracovní oblast začínající
   na2n, délky3n+S_n. Po návratu přesuneme jeho2n výsledných bitů
   z pozice2n na3n+S_n; při překryvu kopírujeme odzadu.
   Platí5n+S_n<=3N+S_N: v lichém případě n>=2.
2. Spočteme H=U1V1 rekurzivně od pozice0. Potřebuje
   3(n−e)+S_(n−e)<=3n+S_n bitů, takže uložený rozdílový součin
   nepoškodí. U lichého N stačí již S_(n−1)<=S_n+1.
3. V úseku od3n+S_n délky3n−2e vytvoříme
   F=(B+1)H−(U0−U1)(V0−V1). Součin rozdílů tam již je;
   použijeme jeho znaménko a dvakrát přičteme H, jednou s posunem n.
4. Součin P=U0V0 rekurzivně spočteme od0, se3n+S_n bity.
   F zůstane nedotčen. Od pozice d=2n+S_n vynulujeme n bitů
   před F a přičteme P od d a od d+n. Výsledná hodnota je
   B F+(B+1)P = U V.
5. Součin délky2N přesuneme z d na0, tentokrát od nejnižší pozice.

Poslední použitá adresa je d+2N−1, protože
`d+2N=6n−2e+S_n=3N+S_N`. Všechny tři rekurzivní oblasti
jsou oddělené od aktuálních vstupů a od dat, která musí přežít.
Tím je paměťová indukce uzavřena, včetně N=2 a N=3.

## Záporný mezivýsledek a řízení rekurze

F může být záporné: například N=3,U=V=3 dává F=−9. Není správné
předpokládat, že všechny pomocné celočíselné hodnoty jsou nezáporné.
F uložíme modulo2^(3n−2e), tedy se zápornými hodnotami v doplňkovém
kódu. Po posunu n bitů a obou sčítáních stačí ignorovat přenos mimo
celou2N-bitovou oblast. Dostaneme UV modulo2^(2N), a protože
0<=UV<2^(2N), je to přesně požadovaný součin. Tento postup nevyžaduje
samostatnou znaménkovou cifru pro celé F. Znaménka rozdílů jsou
konstantně velká řídicí informace na jednu úroveň.

Přesný vzorec3N+S_N počítá aritmetická data, nikoli programové
ukazatele a záznamy rekurze. Běžná implementace potřebuje navíc
O(log N) řídicích záznamů. Pokud vyžadujeme i jejich cenu v bitech,
lze uchovat jen cestu v ternárním stromu volání, fázi a znaménka,
celkem O(log N) bitů, a adresy na návratu znovu odvodit z kořenového
N a této cesty pomocí konstantního počtu O(log N)-bitových registrů.
To zachová prostor3N+O(log N) bitů, za cenu další práce při řízení.
Referenční Python používá běžné zásobníkové rámce; netvrdíme,
že celé jeho runtime používá přesně tolik paměti.

Knižní poznámka o další zhruba N-ciferné oblasti, pokud výstup
nesmí sousedit s pomocnou pamětí, je popisem varianty rozvrhu,
nikoli dokázanou dolní mezí pro všechny algoritmy. Citace Maeder1993
patří do navazující kontroly historického kontextu.

## Přesné kontroly a errata

`verify_fast_late.py`,běh58963,exit0,všechny tři checkpointy:
60 přesných komplexně racionálních chirp příkladů,532 výsledných
buněk transformace;100000 hodnot rekurencí a10001 formálních
koeficientů;5604 paměťových násobení, z toho všechny dvojice do
6bitů a144 větších případů do257bitů. Vzniklo15101 záporných F.

Paměťový násobič skutečně sčítá,odčítá,přenáší a přesouvá jednotlivé
bity v předepsaných úsecích. Nezávislé celočíselné násobení je pouze
orákulem; kontrolní kopie paměti ověřují, že okolní data každého
rekurzivního volání zůstala nedotčena. Počet jednobitových součinů
souhlasí s nezávislou rekurencí K_N. Přesná FFT konvoluční identita
byla ověřena v předchozím bloku; zde znovu netestujeme stejné FFT.

Čtyři vrstvy errat prohledány podle318,634,635,čísel úloh,chirp,
Karatsuba a paměti. Jediná zde relevantní oprava je uvedené
upřesnění konvergence2020. Žádná nová chyba16–18 nepotvrzena.
