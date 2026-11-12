# §1.2.6-10–12: kongruence a přenosy v číselných soustavách

Značení C(n,k) je definováno v [binomial-identities.md](binomial-identities.md).
Pro celé n,k je toto číslo celé: pro n>=0 jde o počítání podmnožin,
pro n<0 použijeme C(n,k)=(−1)^k C(k−n−1,k), pro k<0 je 0.
Kongruence modulo prvočíslo p znamená rovnost po odečtení násobku p.
Těleso zbytků modulo p značíme F_p.

## Lucasův vzorec, včetně záporných horních indexů

Formální mocninná řada nad F_p je posloupnost koeficientů
se sčítáním po složkách a s konečnou konvolucí pro každý
koeficient součinu. Konvergence reálných řad se zde nepožaduje.
Řada s nenulovým konstantním členem má jednoznačný inverzní
prvek: koeficienty inverze se postupně vyřeší ze součinu 1.

Pro 1<=j<=p−1 je p dělitelem C(p,j), protože j je invertibilní
modulo p a j C(p,j)=p C(p−1,j−1). Proto
`(1+x)^p=1+x^p` v F_p[x]. Pro libovolné celé n napišme
n=pq+a, 0<=a<p, kde q=floor(n/p), a=n mod p. Potom v F_p[[x]]

```text
(1+x)^n = (1+x^p)^q (1+x)^a.                         (L1)
```

Při q<0 používáme právě definovanou inverzní řadu; celočíselné
binomické koeficienty této řady vyplývají z Pascalovy identity
nebo z předchozího důkazu binomické věty. V koeficientu x^k,
k=pj+b>=0, 0<=b<p, může z druhého faktoru přispět pouze x^b.
Porovnání koeficientů dává

```text
C(n,k) = C(floor(n/p),floor(k/p)) C(n mod p,k mod p)  (mod p).  (L2)
```

Pro k<0 jsou obě strany 0, protože floor(k/p)<0.
To dokazuje úlohu 10(e) pro všechna celá n,k, včetně n<0.
Omezení n na celé číslo bylo přidáno v erratech 4. října 2021.
Část (f) získáme opakováním (L2) pro konečné p-ární rozvoje
nezáporných n,k; součin jde přes všechny jejich číslice,
po doplnění nul na začátku kratšího rozvoje.

V (a) dosadíme k=p do (L2): C(n,p)≡floor(n/p).
Část (b) byla dokázána před (L1). Pro (c) ve zlomku C(p−1,k)
jsou j=1,...,k invertibilní modulo p, takže každý faktor
(p−j)/j přispěje −1. Pro (d) Pascalovo pravidlo dává
C(p+1,k)=C(p,k)+C(p,k−1)≡0 v požadovaném rozsahu 2<=k<=p−1.
Při p=2 je tento rozsah prázdný.

Knižní důkaz pomocí bloků p činitelů v odpovědi 10 také funguje.
Po odstranění prvních b=k mod p činitelů mají celé bloky stejný
součin jednotek modulo p; násobky p po dělení p vytvářejí
C(floor((n−b)/p),floor(k/p)). Tento podíl je celé číslo i
pro záporné n. Při b>a má první blok nulový zbytek, jinak
floor((n−b)/p)=floor(n/p). Krácení se týká jen jednotek,
tedy činitelů nedělitelných p, nikoli libovolných nulových zbytků.

## Úloha 11: Kummerovo počítání přenosů

Pro nezáporné celé N označuje s_p(N) součet číslic N v soustavě
o základu p a v_p(N!) násobnost prvočísla p. Již dokázaný
Legendreův vzorec je v_p(N!)=(N−s_p(N))/(p−1).
Pro nezáporná celá a,b proto

```text
v_p(C(a+b,a)) = [s_p(a)+s_p(b)−s_p(a+b)]/(p−1).       (K1)
```

Při sloupcovém sčítání označme číslice a_i,b_i,c_i a přenos
do sloupce i jako epsilon_i; epsilon_0=0. Platí
`a_i+b_i+epsilon_i=c_i+p epsilon_(i+1)`.
Každý přenos je 0 nebo 1, protože součet dvou číslic a
předchozího přenosu je nejvýše 2p−1. Sečteme rovnosti přes
všechny sloupce, včetně konečného vedoucího sloupce. Přenosy
se vykrátí kromě faktoru p−1; čitatel (K1) je tedy (p−1)
krát počet přenosů. To zahrnuje i řetězce přenosů a nulové vstupy.

## Úloha 12 a její zobecnění v odpovědi

Z (L2) je C(n,k) nedělitelné p právě tehdy, když každá číslice
k je nejvýše odpovídající číslice n. Všechny koeficienty řádku
0<=k<=n jsou tedy nedělitelné p právě tehdy, když všechny
číslice pod vedoucí číslicí n jsou p−1. Kdyby nižší číslice
byla menší, lze zvolit k s touto jedinou číslicí o 1 větší;
vyšší vedoucí číslice n zaručuje k<=n a vznikne nulový faktor.
Obráceně, při všech nižších číslicích p−1 nemůže žádné k<=n
porušit číslicové nerovnosti.

Ekvivalentní popis je `n=a p^m−1`, 1<=a<p, m>=0, jak uvádí
odpověď. Pro p=2 a kladné n jde přesně o n=2^m−1, m>=1.
Nultý řádek by také vyhověl, ale zadání se ptá na kladné n.

## Pramenný rozsah

Matematika všech částí je dokázána výše. Dne 2. listopadu byly
přímo přečteny původní Kummerova pasáž 1852 a celý citovaný
článek Knuth–Wilf 1989; přesný rozsah a meze dokumentuje
[knuth-wilf-primary.md](knuth-wilf-primary.md), X0693–X0694.
Úloha 11 je tím uzavřena i pramenně. Lucas1877/1878 a Fine1947
byli následně přímo přečteni, viz X0701 a
[kořenovou revizi](binomial-primary-root-review.md). U úlohy10
zbývají původní Dicksonovy strany383–384 z1902. Nový výpočet
nenahradí četbu této citace.
