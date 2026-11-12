# §2.3.1-11: generující funkce a kandidát proti erratu z roku 1999

Kořenový stav při předání: **V1-C0050, confirmed**. Globální ID přidělil koordinátor; lokální dočasné označení a níže zachovaná historie revize slouží návaznosti evidence.
Dočasné označení `height-asymptotic-erratum`; kořenově potvrzeno jako V1-C0050. Důležitý rozdíl: původní asymptotika na straně 565 je podle následujícího výpočtu správná. Podezření se týká publikované opravy z 13. listopadu 1999 v all1-prepre, strana PDF 42. Oba originály byly přímo prohlédnuty (`images/p565.png`, `images/all1-prepre-42.png`); není to záměna znaménka z OCR.

## Přesná veličina a konečné koeficienty

Pro binární strom T definujme h(T) jako největší počet prvků na zásobníku během Algorithm T. Pro prázdný strom je h=0; pro neprázdný s levým podstromem L a pravým R platí

```text
h(T) = max(1+h(L), h(R)).
```

Při průchodu L je kořen stále na zásobníku, při průchodu R již nikoli. Označme a[n,k] počet n-uzlových binárních tvarů s h≤k a `g_k(z)=sum_n a[n,k] z^n`. Rekurence rozkladu kořene dává

```text
g_0=1,
g_k=1+z*g_(k-1)*g_k = 1/(1-z*g_(k-1)).
```

Odtud přesně plyne tištěná rekurence pro q_k a uzavřený vzorec s kořeny `f_1,f_2=(1±sqrt(1-4z))/2`. Položme `u=z(1+u)^2`, tedy `z=u/(1+u)^2`. Pak

```text
g_k(z) = (1+u)*(1-u^(k+1))/(1-u^(k+2)),
C(z)   = sum_n C_n z^n = 1+u,
C_n    = binom(2n,n)/(n+1).
```

C_n je celkový počet n-uzlových binárních stromů. Vždy používáme jedinou analytickou větev `u(0)=0`, tedy `u(z)=(1-sqrt(1-4z))/(1+sqrt(1-4z))`, s odmocninou rovnou 1 v nule. Druhý algebraický kořen sem nepatří. Změna proměnné v koeficientovém integrálu má Jacobián `(1-u)/(1+u)^3`, a proto pro celá n,k≥0 přímo dává tištěný vzorec

```text
a[n,k] = [u^n] (1-u)*(1+u)^(2n)*(1-u^(k+1))/(1-u^(k+2)).
```

Nechť s_n je součet h přes všechny n-uzlové tvary. Součet pravděpodobnostních ocasů (zde konečný součet počtů) dává `s_n=sum_(k>=1)(C_n-a[n,k-1])`. Označme Lambertovu řadu `D(u)=sum_(j>=1)u^j/(1-u^j)`. Algebraicky pak

```text
S(z) := sum_n s_n z^n
     = (1/u-u)*D(u) - (1+u).
```

Stejná změna proměnné potvrzuje i druhý tištěný koeficientový vzorec:

```text
s_n = [u^(n+1)] (1-u)^2*(1+u)^(2n)*D(u) - C_n.
```

Tím je ověřena celá přesná část odpovědi, nezávisle na následné asymptotice.

## Asymptotický výpočet s kontrolou koeficientů

Položme `u=exp(-t)` a nechť γ je Eulerova konstanta. Mellinova transformace Lambertovy řady je `Gamma(s)*zeta(s)^2`: vychází z absolutně konvergentního dvojného součtu pro Re(s)>1. Posunutím integrační přímky dostaneme

```text
D(exp(-t)) = (γ-log(t))/t + 1/4 - t/144 + O(t^3).
```

Dvojný pól v s=1 má reziduum `(γ-log(t))/t`; pól v s=0 dává 1/4 a pól v s=-1 dává -t/144. Posun lze provést dále do libovolného pevného záporného řádu. Odhady platí stejnoměrně pro `|arg(t)|≤pi/2-epsilon`, protože Gamma(s) exponenciálně klesá na svislých přímkách. To zajišťuje potřebnou komplexní oblast pro přenos koeficientů; nejde pouze o rozvoj na reálné ose.

Dosadíme do S:

```text
S(z) = 2*(sinh(t)/t)*(γ-log(t))
       + (3/2)*sinh(t) - cosh(t) - 1 - t*sinh(t)/72 + ... .
```

Nyní nechť `w=1-4z`, `x=sqrt(w)`, takže `t=2*atanh(x)` a

```text
sinh(t)/t = 1 + (2/3)*w + O(w^2),
sinh(t)   = 2*sqrt(w)/(1-w).
```

Vynecháme-li členy analytické ve w v okolí nuly, dostáváme relevantní singulární část

```text
S(z) = -(1+(2/3)*w+O(w^2))*log(w)
       + 3*w^(1/2) + 3*w^(3/2) + O(w^(5/2)).
```

Analytické části a zbytky jsou kontrolovatelné do vyššího řádu předchozím posunem Mellinovy přímky. Z přesných koeficientů logaritmu a standardního binomického rozvoje tedy plyne

```text
s_n/4^n = 1/n
          - 3/(2*sqrt(pi))*n^(-3/2)
          - (2/3)*n^(-2)
          + 27/(16*sqrt(pi))*n^(-5/2)
          + O(n^(-3)).

C_n/4^n = 1/(sqrt(pi)*n^(3/2))
          *(1-9/(8n)+O(n^(-2))).
```

Po vydělení je koeficient u `sqrt(pi/n)` roven `9/8-2/3=11/24`. Člen řádu 1/n se ruší: `27/16-(3/2)*(9/8)=0`. Proto

```text
s_n/C_n = sqrt(pi*n) - 3/2 + (11/24)*sqrt(pi/n)
          + O(n^(-3/2)).
```

Celé původní znění je tedy

```text
s_n/a[n,n] = sqrt(pi*n) - 3/2 + (11/24)*sqrt(pi/n)
             + O(n^(-3/2)).
```

Celé znění po jediné změně z errata je

```text
s_n/a[n,n] = sqrt(pi*n) - 3/2 - (13/24)*sqrt(pi/n) + 1/(2*n)
             + O(n^(-3/2)).
```

V obou případech `a[n,n]=C_n`; průměruje se přes všechny C_n binární tvary s přesně n uzly, každý se stejnou váhou. Žádné pravděpodobnosti vyvolané náhodným pořadím vkládání do vyhledávacího stromu se nepoužívají. Rozdíl mezi dvěma výrazy je `sqrt(pi/n)-1/(2n)`, který nelze pohltit zbytkem `O(n^(-3/2))`.

Posun oproti článku z roku 1972 je explicitní. Převod binárního stromu s n uzly na uspořádaný les ponechá n uzlů i maximální výšku h v konvenci kořenové úrovně 1. Přidáním společného kořene vznikne obecný uspořádaný strom s `N=n+1` uzly a výškou `H=h+1`, kde článek výšku počítá počtem uzlů cesty. Jeho omezené počty proto splňují `A[N,H]=a[N-1,H-1]`. Pro průměry platí přesně `E(H_N)=1+s_(N-1)/C_(N-1)`. Výše dokázaná binární formule by po důsledném přepisu dávala `E(H_N)=sqrt(pi*N)-1/2-(1/24)*sqrt(pi/N)+O(N^(-3/2))`. Vyšší člen z errata nelze vysvětlit pouhým přejmenováním N na n. Samotný článek uvádí jen první dva členy, se zbytkem dovolujícím řád N^(-1/2), a proto s naším výpočtem není v rozporu.

## Nezávislé konečné kontroly a pramenná mez

`check_height.py` porovnává rekurzivní výčet všech tvarů pro n≤8 s rekurencí g_k a přesným Lambertovým koeficientem. Rekurence a koeficientový vzorec souhlasí pro všechna n≤30. Přesné celočíselné součty a Catalanova čísla jsou uloženy pro n=10,100,1000,10000 v `results/height.json`. Normalizovaný rozdíl `(s_n/C_n-sqrt(pi*n)+3/2)*sqrt(n/pi)` postupně dává přibližně 0.44630, 0.45706, 0.458205, 0.458321 a směřuje k 11/24≈0.458333, nikoli k -13/24. Numerika pouze doplňuje uvedený obecný důkaz.

Citovaný původní článek de Bruijn–Knuth–Rice (1972), strany 15–22, byl získán z univerzitního repozitáře spoluautora; neuvádí tento vyšší člen v konečné větě (34), ale potvrzuje použité přesné řady, metodu a možnost pokračovat v rozvoji. Jeho pojem je výška obecného uspořádaného stromu, zatímco h zde je výška reprezentovaného lesa; je nutný přechod přidáním jednoho kořene, nikoli záměna n bez posunu. U dalších dvou citací byly přečteny původní definice a zobecňující věty; přesný rozsah je v `sources.md`. Tyto články potvrzují uvedené zobecnění a rozdělení výšek, ale nejsou nezávislou revizí sporného vyššího členu.

Všechny čtyři erratové vrstvy byly prohledány podle 565 a témat height, stack, asymptotic, 11/24 a 13/24. Nebyla nalezena pozdější změna této opravy ani změna definic a[n,k], s_n či g_k, která by výše uvedenou veličinu nahradila jinou.
