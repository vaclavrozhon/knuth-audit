# Algoritmus H a jediná vstupní váha

Přečteny původní zadání 405 a odpověď 596; obrazy v `images/p405.png` a `p596.png`. Čtyři vrstvy errat jsou doloženy v `inventory-and-errata.md`. Žádná příslušná oprava H nebyla nalezena.

## Invariant pro m>=2

A[m]..A[2m-1] jsou pevné seřazené vstupní váhy, A[2m]=infinity je pracovní sentinel. Nevyužité listy jsou v neklesající frontě od i; nevyužité vnitřní kořeny v neklesající frontě A[j],A[j-1],...,A[k]. Na vstupu H2 je x už odstraněný nejmenší kořen. H2 odstraní nejmenší ze zbývajících kořenů, H3 vytvoří jejich rodiče k-1. Potom zbývá k kořenů. Každé dítě má větší index než rodič; po m-1 sloučeních je kořen 1 a vznikne úplný strom na všech listech.

Je nutné vysvětlit záporné váhy, nikoli předpokládat monotónní slučovací součty. Pokud druhá vybraná váha A[y]<0, nově vytvořený součet je přísně menší než A[y] a než všechny zbývající listy. Žádný jiný vnitřní kořen v této fázi nezůstává: předchozí záporný agregát byl jako nejmenší vybrán na pozici x. Proto j=k, i=y+1 a A[i]>A[j], přesně jak tvrdí H5. Nový agregát se hned zase odebere. Fronta vnitřních vah má v této fázi nejvýše jeden prvek.

Jakmile jsou druhé vybírané váhy nezáporné, slučovací součty neklesají. Je-li předchozí součet s=a+b, a<=b a b>=0, další dvojice buď obsahuje s, takže nový součet je aspoň s, nebo obsahuje dva původně nevybrané kořeny oba alespoň b, takže jejich součet je aspoň 2b>=a+b. Pozdější výběry z front jsou tedy platné. Obě fáze se překrývají na případné záporné první váze x; právě proto nestačí naivně předpokládat všechny váhy nezáporné.

První H2 vůbec neporovnává váhy, protože vnitřní fronta je prázdná. Dalších H2 je m-2 a H5 je m-2. Je tedy nejvýše 2m-4 skutečných porovnání vah, což splňuje požadavek méně než 2m. Čas i pracovní paměť jsou O(m).

`huffman.py` obsahuje celý doslovný algoritmus včetně ověření uvedených invariantů. `check_huffman.py` jej porovnává s nezávislou enumerací všech profilů binárních tvarů, nikoli pouze s jinou implementací H. Všech 6427 neklesajících seznamů vah z {-3,...,3} délky 2..8 prošlo; výsledky v `results/huffman.json`.

## Kandidát: v zadání chybí omezení m>=2 nebo základ m=1

Zadání 405 neuvádí m>=2. Jediná váha je smysluplný vstup: požadovaný strom má jeden vnější kořen 1, A[1]=w1, žádné vnitřní uzly a prázdné L,R. Hlavní indukční důkaz zvlášť pracuje s m>=2, což tento základ nevylučuje.

Vezměme m=1,w1=1. Doslovný průběh je:

```text
H1: A[1]=1, A[2]=infinity, x=1, i=2, j=0, k=1.
H2: j<k, tedy y=2, i=3.
H3: k=0; požaduje zápis L[0]=1, R[0]=2, A[0]=infinity.
```

To je mimo požadované pole L[1]..L[m-1], R[1]..R[m-1] i A[1]..A[2m-1]. Ani volné pole místo kontroly indexu nepomůže: H4 test k=1 už neprojde. Nejmenší lokální oprava je po zkopírování vstupních vah v H1 vrátit výsledek, pokud m=1. Alternativně je třeba výslovně omezit zadání na m>=2 a triviální případ vyřešit předem. `singleton_guard=True` realizuje první opravu bez změn pro m>=2.

Stav je zatím **candidate** kvůli možné zamýšlené, ale nevypsané doméně m>=2. Numerický a indexový rozpor pro doslovně dovolené m=1 je přímý. Netvrdím prvenství a nebyl prověřen pozdější tištěný dotisk.
