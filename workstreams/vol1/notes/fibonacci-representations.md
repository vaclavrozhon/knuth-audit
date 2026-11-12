# §1.2.8-34,41–42: Fibonacciho reprezentace a posuny

Audit 1. listopadu 2026. Zobrazeny s. 86,495–496.
F_n,phi,psi jsou definovány v `fibonacci-basic.md`.
Značka k >> j v knize znamená **k>=j+2**, nikoli k>j+2.
Reprezentace má sestupné indexy s tímto rozestupem.

## Úloha 34: existence a jednoznačnost

Povolíme indexy 2,...,K, žádné dva sousední. Jejich
součty tvoří každé celé číslo od 0 do F_(K+1)−1
právě jednou. Důkaz indukcí: bez F_K získáme
[0,F_K−1], s F_K získáme
F_K+[0,F_(K−1)−1]=[F_K,F_(K+1)−1]. Intervaly jsou
souvislé a disjunktní. Základy K=1,2 jsou přímé.
To současně dokazuje maximum součtu, existenci,
jednoznačnost a hladový postup: odečíst největší
F_K<=n a opakovat na zbytku <F_(K−1).

Pro n=0 je reprezentace prázdná. Pro n>0 jde přesně
o zadání s k_r>>0, které vylučuje duplicitní F_1=F_2.
Budeme jí říkat Zeckendorfova reprezentace; tento název
není sám o sobě tvrzením o historickém prvenství.

## Úloha 41: přesné zaokrouhlení po posunu

Nechť n=sum_j F_(k_j) je tato reprezentace a
D=sum_j psi^(k_j). Z identity F_(k+1)−phi F_k=psi^k
plyne, že A=sum_j F_(k_j+1)=phi n+D je celé číslo.
Protože k_j>=2 a rozestupy jsou aspoň 2, dostáváme

```text
−phi^(−2) < D < phi^(−1).                              (Z1)
```

Dolní mez je součet všech lichých mocnin psi^3,psi^5,...,
horní všech sudých psi²,psi⁴,... . Obě nerovnosti jsou
ostré, protože reprezentace je konečná. Platí i pro
prázdný součet. Definujme f(x)=floor(x+phi^(−1)).
Pak 0<phi^(−1)−D<1, a tedy

```text
sum_j F_(k_j+1)=f(phi n),
sum_j F_(k_j−1)=f(phi^(−1)n)=f(phi n)−n.                (Z2)
```

Druhá rovnost používá F_(k+1)−F_k=F_(k−1) a celočíselné n.
Není to odhad typu „asi zaokrouhlení“: otevřený interval
(Z1) vylučuje obě sporné hraniční hodnoty.

## Úloha 42: společná reprezentace dvou celých čísel

Chceme indexy s rozestupy >=2, tentokrát libovolně
záporné, tak aby m=sum F_k a n=sum F_(k+1).
Taková reprezentace existuje právě když m+phi n>=0.
Při rovnosti jsou m=n=0 díky iracionalitě phi a jedinou
možností je prázdný součet. Nutnost pro neprázdnou
reprezentaci plyne z

```text
m+phi n=sum_j phi^(k_j+1)>0.                           (Z3)
```

Pro dostatečnost při m+phi n>0 položme
A_N=mF_(N−1)+nF_N a B_N=mF_N+nF_(N+1).
Uzavřený vzorec ukazuje A_N→+infinity a

```text
B_N−phi A_N=m psi^(N−1)+n psi^N → 0.                   (Z4)
```

Zvolíme N tak velké, že A_N>=0 a absolutní hodnota
pravé strany (Z4) je menší než phi^(−2).
Proto B_N=f(phi A_N). Zeckendorfova reprezentace
A_N=sum F_(ell_j) tedy podle (Z2) současně dává
B_N=sum F_(ell_j+1). Matice
[[F_(N−1),F_N],[F_N,F_(N+1)]] má determinant (−1)^N,
takže je invertibilní. Z (F2) proto dostáváme
m=sum F_(ell_j−N), n=sum F_(ell_j−N+1).
To je hledaná reprezentace, se zachovanými rozestupy.

Při dvou různých reprezentacích zvolíme společné N,
které posune všechny indexy nejméně na 2. Obě pak
reprezentují stejné nezáporné A_N v soustavě úlohy 34,
což odporuje již dokázané jednoznačnosti.

Původní sazba odpovědi 42 má **m+phi n>=0**.
OCR mění tuto nerovnost na >0; případ prázdné
reprezentace není nová chyba knihy. Dokázán je také
silnější obor se zápornými m,n, přesně jak uvádí odpověď.

Doklad pramene Klarner 1968 je veden samostatně;
jeho úplná bibliografická kontrola není nahrazena tímto důkazem.
