# §4.5.4–23: Jacobiho symbol a Solovayův–Strassenův test

Úloha 23 a odpověď na str. 662–663 jsou uzavřeny. Níže jsou vlastní
důkazy všech tří částí, obecného Monierova vzorce i poznámky o chybě
větší než 1/4. Matematické znění souhlasí. Druhý výskyt již evidované bibliografické opravy
**V2-C0129** mění konečnou stránku Lebesgueova článku z 520 na 517.
Známá oprava z 20. 4. 1998 upravuje pouze mezeru před `t` na str. 414.

## 1. Definice a výpočet bez faktorizace

Pro liché prvočíslo `p` značí `J(a,p)` Legendreův symbol: nulu, pokud
`p|a`, jinak znaménko `+1` pro nenulový čtverec modulo `p` a `-1`
pro nečtverec. Ekvivalentně `J(a,p) = a^((p-1)/2) (mod p)`; to plyne
například z cykličnosti násobící grupy konečného tělesa. Pro liché
`n = product p_i^e_i > 1` definujeme **Jacobiho symbol**

```
J(a,n) = product J(a,p_i)^e_i.
```

Prvočísla `p_i` jsou různá a exponenty `e_i` kladné. Pro ukončení
algoritmu přidáváme obvyklou konvenci `J(a,1)=1`, tedy prázdný součin.
Kniha výslovně definuje jmenovatel jen pro `n>1`; tuto konvenci je
třeba doplnit také při použití reciprocity s čitatelem 1. Nejde
o změnu testu, jehož vstup zde vždy splňuje `n>=3`. Záporný čitatel
použitý v historických příkladech rozšiřujeme periodicitou.

Nula, jednička, periodicita a násobnost v čitateli plynou přímo
z definice pro prvočísla a poté ze součinu. Konkrétně `J(a,n)=0`
právě když `gcd(a,n)>1`; jinak je to znaménko. Hodnota `+1` pro
složený jmenovatel **necharakterizuje čtverce**: například `J(2,9)=1`,
ačkoliv 2 není čtverec modulo 9.

Pro pravidlo o dvojce použijeme krátký důkaz Gaussova lemmatu.
Položme `h=(p-1)/2`. Nejmenší absolutní zbytky čísel `a,2a,...,ha`
jsou až na znaménka permutací `1,...,h`. Je-li `v` záporných znamének,
vynásobení a zkrácení `h!` modulo `p` dává `a^h=(-1)^v`.
Pro `a=2` je `v=h-floor(p/4)`, jehož parita je `(p^2-1)/8`.
Na složený lichý jmenovatel pravidlo přejde pomocí identity

```
((uv)^2-1)/8 = (u^2-1)/8 + u^2 (v^2-1)/8.
```

Proto `J(2,n)=(-1)^((n^2-1)/8)`. Obdobně
`J(-1,n)=(-1)^((n-1)/2)` pro periodické rozšíření.

Kvadratickou reciprocitu pro dvě lichá prvočísla bereme jako vstup
výslovně dovolený zadáním, §1.2.4–47(d). Pro nesoudělná lichá
`a,b` násobíme tento zákon přes všechny jejich prvočinitele včetně
násobností. Parita výsledného exponentu je

```
(sum_i (p_i-1)/2) (sum_j (q_j-1)/2)
  = ((a-1)/2) ((b-1)/2)  (mod 2),
```

protože `((uv)-1)/2 = (u-1)/2+(v-1)/2 (mod 2)` pro lichá `u,v`.
Tedy `J(a,b)=(-1)^((a-1)(b-1)/4) J(b,a)`. Pro společný prvočinitel
jsou obě strany nula. Pro jedničku platí doplněná konvence výše.

Výpočet nyní střídá zbytek, odstranění mocniny dvojky, případnou
změnu znaménka a záměnu čitatele se jmenovatelem. Invariant je
původní symbol = průběžné znaménko krát aktuální symbol; společný
dělitel se zachovává. Při nulovém čitateli vracíme nulu, zbývá-li
jmenovatel větší než 1, jinak průběžné znaménko. Jmenovatele klesají
jako u Eukleidova algoritmu, takže je `O(log n)` dělení a celkem
`O(log n)` odstraněných binárních míst po počáteční redukci.
Klasická amortizace z §4.5.2 dává kvadratický bitový čas. Faktorizaci
jmenovatele tento algoritmus nepotřebuje.

## 2. Proč je chyba nejvýše poloviční

Zvolme pevné liché složené `n>=9`, `u=(n-1)/2` a grupu
`U=(Z/nZ)^*` nenulových invertibilních zbytků. Její velikost je
Eulerova funkce `phi(n)`. Množina přijímaných zbytků je

```
H = {x in U : x^u = J(x,n) (mod n)}.
```

Obě strany jsou násobné funkce `U -> U`; jejich podíl je tedy
homomorfismus a `H` je jeho jádro, čili podgrupa. Ukážeme, že je
vlastní. Pak její index je alespoň 2 a `|H|<=phi(n)/2`.

Pokud `p^e|n`, `e>=2`, vyberme podle čínské věty zbytek, který je
generátorem modulo `p^e`. Kdyby prošly všechny jednotky, jejich
umocnění na `n-1` by bylo 1. Muselo by tedy platit
`p^(e-1)(p-1) | n-1`, což odporuje `p|n`.

Je-li `n` bez čtvercového dělitele, má alespoň dvě různá prvočísla
`p,q`. Vyberme `x`, které je nečtvercem modulo `p` a je 1 modulo
všech ostatních prvočinitelů. Pak `J(x,n)=-1`, ale `x^u=1 (mod q)`.
Tento zbytek neprojde. Důkaz funguje i v případě, kdy je samotný
Jacobiho charakter triviální, například pro čtverce.

Při rovnoměrném losování `1<=x<n` je chyba
`|H|/(n-1)<=phi(n)/(2(n-1))<1/2`. Prvočíslo test přijme vždy
Eulerovým kritériem. Jde o pravděpodobnost chyby pro pevný vstup,
nikoli o podmíněnou pravděpodobnost prvočíselnosti po přijetí.

## 3. Přesný počet přijímaných základen

Pišme `n-1=2^k q` a `p_i-1=2^s_i d_i`, kde `q,d_i` jsou lichá;
`s=min s_i`, `g_i=gcd(q,d_i)` a

```
P = product gcd((n-1)/2,p_i-1)
  = product (2^min(k-1,s_i) g_i).
```

Vždy `s<=k`, protože každý `p_i` je 1 modulo `2^s`. Jelikož
`p_i` nedělí `u`, má rovnice `x^u=1` modulo `p_i^e_i` přesně
`gcd(u,p_i-1)` řešení. Násobnost `e_i` zde nevytváří další kořeny.
Celkem je podle čínské věty `P` řešení s pravou stranou `+1`.

Na této množině je Jacobiho symbol netriviálním charakterem právě
tehdy, když pro některé **stejné** `i` platí `s_i<k` a `e_i` je liché.
Opravdu: v cyklické grupě modulo `p_i^e_i` jsou kořeny mocninami
generátoru s krokem `p_i^(e_i-1)(p_i-1)/gcd(u,p_i-1)`. Legendreův
symbol na nich střídá znaménko právě při lichém kroku, tj. `s_i<k`;
jeho příspěvek do Jacobiho symbolu zaniká pro sudé `e_i`.
V netriviálním případě projde polovina těchto kořenů, jinak všechny.

Rovnice `x^u=-1` má řešení ve všech komponentách právě když
`k<=s_i` pro všechna `i`, tedy právě když `s=k`. Pak jich je `P`.
Legendreův symbol takového kořene je `-1` pro `s_i=k` a `+1`
pro `s_i>k`. Součet `e_i` přes indexy `s_i=k` je lichý, neboť

```
n = 1 + 2^k sum_{s_i=k} e_i  (mod 2^(k+1)).
```

Všech těchto `P` kořenů má proto Jacobiho symbol `-1` a projde.
Dostáváme přesně tištěný Monierův vzorec

```
b_E(n) = delta P,
delta = 2     pokud min s_i = k,
        1/2   pokud existuje i se s_i<k a lichým e_i,
        1     jinak.
```

Značení `b_E` zde znamená počet přijímaných základen `1<=x<n`,
v knize `b'_n`; ani pro prvočíslo nejde o počet skutečných chyb.
Sousední vzorec pro silný test je geometrický součet již dokázaný
v [primality-probabilistic.md](primality-probabilistic.md), §2.

Pro kontrolu větví: `n=45=3^2*5` má `k=2`, `delta=1` a `b_E=4`.
Lichý exponent u prvočísla 5 neaktivuje větev `1/2`, protože právě
u tohoto prvočísla není `s_i<k`. Pro `n=9` je `b_E=2` a chyba 1/4.

## 4. Kdy může chyba překročit 1/4

Má-li `n` opakovaný prvočinitel `p`, vzorec z §3 dává
`b_E<=product(p_i-1)`: pro `delta=2` každá komponenta ztrácí
alespoň faktor 2, ostatní větve jsou okamžité. Proto

```
b_E/n <= (p-1)/p^2 <= 2/9.
```

Pro `n>=9` z toho plyne `4b_E<=n-1`. Zbývá bezčtvercové `n`
s alespoň dvěma prvočiniteli. Je-li `min s_i=k`, faktor
`delta=2` spolu s alespoň třemi komponentami dává `b_E<=phi(n)/4`.
U dvou komponent musí mít jedna `s_i>k`, jinak by součin byl
1 modulo `2^(k+1)`; její další faktor 2 dává stejnou mez.

Je-li `min s_i<k`, máme `delta=1/2`. Existuje-li také `s_i>=k`,
opět dostáváme `b_E<=phi(n)/4`. Jinak všechna `s_i<k` a
`b_E/phi(n)=(1/2) product(g_i/d_i)`. Některý vlastní lichý dělitel
`g_i<d_i` sníží tuto hodnotu nejvýše na 1/6. Jediný zbývající
případ má všechna `g_i=d_i`, tedy `p_i-1 | n-1`: podle již
dokázaného Korseltova kritéria jde o Carmichaelovo číslo.

Nutná podmínka v knize je tedy správná: chyba větší než 1/4 může
nastat pouze pro Carmichaelovo `n` s `max s_i<k`. V takovém případě
`b_E=phi(n)/2`; netvrdíme, že každé takové číslo má chybu >1/4.
U příkladu `1729=7*13*19` je `k=6`, `(s_i)=(1,2,1)`,
`phi=1296`, `b_E=648` a chyba přesně `3/8`.

## 5. Každé přijetí silným testem splňuje Jacobiho test

Pokud `x^q=1`, násobnost symbolu a lichost `q` dávají
`J(x,n)^q=1`, tedy `J(x,n)=1=x^((n-1)/2)`.

Jinak silný test přijal `x^(2^j q)=-1`, kde `0<=j<k`.
Pro každý prvočinitel `p_i` má řád `x` modulo `p_i` právě
`j+1` faktorů 2. Pišme `p_i=1+2^(j+1)c_i`, přičemž `c_i`
nemusí být liché. Z cyklické grupy plyne
`J(x,p_i)=(-1)^c_i`: lichá část řádu dělí `q` a její odstranění
nemění paritu potřebného exponentu. Proto
`J(x,n)=(-1)^(sum e_i c_i)`. Současně

```
n = 1 + 2^(j+1) sum e_i c_i  (mod 2^(j+2)),
```

takže součet je lichý právě když `j+1=k`. To přesně odpovídá
hodnotě `x^((n-1)/2)=(-1)^(2^(k-j-1))`.

Jde o inkluzi množin přijímaných základen, ne o tvrzení, že jsou
vždy různé. U složeného čísla je při knižních intervalech losování
chyba P dokonce menší: `(b_P-1)/(n-2) <= (b_E-1)/(n-2)
< b_E/(n-1)`. Silný test pracuje s touž posloupností umocnění
od `x^q` a může skončit před jejím koncem; nepotřebuje výpočet
Jacobiho symbolu. Zde netvrdíme konkrétní měřenou rychlost programu.

## 6. Nezávislé konečné ověření

[Program](../verify_primality_jacobi.py) porovnává algoritmus reciprocity
s explicitními množinami čtverců modulo prvočísla certifikovaná
zkušebním dělením. Přímé umocnění testuje kritérium nezávisle na
počítacím vzorci; samostatný algoritmus P kontroluje inkluzi z §5.

Pro všech 2047 lichých `n` od 3 do 4095 a všech `0<=x<n` prošlo
**4 194 303 dvojic**. Bylo 563 prvočísel a 1484 složených čísel,
větve `delta=2,1,1/2` nastaly 1398, 98, 551krát. Každé z
1 083 506 přijetí silným testem splnilo Jacobiho test; dalších
6182 dvojic prošlo jen Jacobiho testem. Všechny přesné počty
souhlasily. Největší chyba **v tomto konečném rozsahu** je 3/8
pro 1729. Zvláštní Carmichaelova rodina v rozsahu obsahuje
1729 a 2465. Kontrolovány také oba Lebesgueovy příklady.

[Výsledek](../results/primality-jacobi.json),
[úplná tabulka](../results/primality-jacobi-counts.csv).
Běh PID 1276958, session 14735, limit 120 s, exit 0,
44.817267559 s. Obecné důkazy na konečném experimentu nezávisí.

## 7. Primární zdroje a meze historického ověření

Původní strany knihy 413, 414, 662, 663 byly přečteny vizuálně.
Prohledány všechny čtyři vrstvy errat i `err2.textxt`; známá
typografická oprava na PDF straně 24 byla také zobrazena.

[Solovay–Strassen, 1977](https://epubs.siam.org/doi/10.1137/0206006):
ověřen vydavatelský abstrakt a metadata, včetně podání 12. 6. 1974.
Plný původní článek nebyl získán. [Oprava z roku 1978](https://epubs.siam.org/doi/pdf/10.1137/0207009?download=true)
byla přečtena celá v textové extrakci vydavatelského PDF, nikoli
vizuálně: opravuje přehlédnutý případ čtvercového `n`. Vlastní
důkaz §2 tuto mezeru nemá. Přímé lokální stažení opravy vrátilo 403.

[Monier, 1980](https://www.sciencedirect.com/science/article/pii/0304397580900079):
ověřena vydavatelská metadata a indexovaný autorský abstrakt,
Theoretical Computer Science 12(1), 97–108, DOI
10.1016/0304-3975(80)90007-9. Celý originál nebyl získán; vlastní
důkazy §3–5 nezávisí na předpokladu jeho správnosti.

[Lebesgue, 1847](https://www.numdam.org/item/JMPA_1847_1_12__497_0/):
originál uložen, vizuálně přečteny 497, 503–507 a závěrečná 517.
Na str. 497 výslovně připisuje součinovou definici Jacobimu;
§III, 503–507, uvádí algoritmy a porovnává délku výpočtu.
Další aplikace 508–517 nebyly auditovány. Odkaz na 520 je
**C0129**; metadata i ukončená sazba článku dávají 517.
Jacobiho původní sdělení z roku 1837 nebylo přímo získáno
(odkaz na přetisk 1846 v DigiZeitschriften vrací 404).
Historické prvenství tímto neprohlašujeme za nezávisle prokázané.

Podrobné rozsahy a kontrolní součty jsou v
[metadatech](../sources/primality-jacobi.json). Novější fyzický dotisk
ani prvenství nálezu nebyly ověřeny; žádná zpráva nebyla odeslána.
