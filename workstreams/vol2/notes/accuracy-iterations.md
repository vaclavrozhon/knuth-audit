# §4.2.2: stabilita násobení a převracení, kladné součty, Pellův příklad

Audit úloh22,26,27,29,31. Původní strany244–245,616–617 i relevantní
čtyři vrstvy errat byly vizuálně přečteny. V27 se používá opravené
uzávorkování z1998. Nikde se nepřipouští přetečení/podtečení;
R značí zaokrouhlení na nejbližší reprezentovatelné číslo v základu b
s p ciframi. Poloviny se rozhodují konzistentně a invariantně vůči
násobení mocninou b, jako v AlgoritmuN. Důkazy22 a27 nepotřebují
konkrétní volbu sudé/liché poloviny.

## 1. Úloha22: poslední možná změna má index1

Posloupnost je x0=u, x_(2n+1)=R(x_(2n)v),
x_(2n+2)=R(x_(2n+1)/v), kde v≠0. Pro u=0 je tvrzení okamžité.
Znaménka a mocniny b se vytknou; stačí u,v celá v intervalu[B,N),
kde B=b^(p−1), N=b^p. Dokážeme x4=x2. To samo z determinismu
implikuje x_(k+2)=x_k pro všechna k>=2.

**uv<=BN.** Zaokrouhlený součin je x1=uv−r, |r|<=B/2.
Proto |r/v|<=B/(2v)<=1/2; rovnost by vyžadovala v=B,
ale pak je součin přesný a r=0. Pro u>B je okolní síť celočíselná,
takže R(u−r/v)=u. Pro u=B je součin rovněž přesný. Vždy x2=u.

**uv>BN.** Nyní je x1 násobkem N, včetně možnosti x1=BN.
Protože uv/N<v a v je celé, zaokrouhlení uv/N na nejbližší celé
nemůže přesáhnout v. Odtud x1<=vN, x1/v<=N a x2<=N.
Také x1/v>B, takže x2>=B.

- Je-li x2=N, pak x1/v>=N−1/2, tedy
  x1>=vN−v/2>vN−N/2. Protože x1 je násobekN a x1<=vN,
  musí x1=vN. Následující součin dává x3=x1 přesně a x4=x2.
- Je-li x2<N a x1>BN, pišme x2=x1/v+q s |q|<=1/2.
  Pak |qv|<N/2. V okolí x1 mají sousední čísla odstupN,
  tedy x3=R(x1+qv)=x1 a opět x4=x2.
- Zbývá x2<N a x1=BN. Jestliže x3>=BN, tentýž odhad
  |qv|<N/2 dává x3=BN=x1. Jestliže x3<BN, je x2v<BN,
  takže na dvojici x2,v platí již první případ; x4=x2.

Možnost změny x1≠x3 realizuje tištěný příklad b10,p2,u19,v55:

```text
19, 1000, 18, 990, 18, 990, 18, ...
```

Největší možný index k s x_k≠x_(k+2) je tedy1. Primární autorská
poznámka Kahan, `Div754.pdf`, příloha na stranách6–7, byla také
vizuálně přečtena: dokazuje stabilitu dělení–násobení–dělení
pro p>1. Zdejší samostatný důkaz pokrývá rovněž p1; netvrdí se,
že tuto krajní situaci zahrnuje Kahanova příloha.

## 2. Úloha27: nejprve čistě celočíselné lemma

Nechť T zaokrouhluje kladná reálná čísla na nejbližší celé číslo.
Přesné poloviny mohou být rozhodovány libovolně, ale stejné číslo musí
mít vždy stejný výsledek. Taková funkce T je neklesající. Pro K>0
položme n=T(K/m), l=T(K/n), r=T(K/l), kde m,n,l jsou kladná celá.
Tvrdíme **r=n**.

Kdyby r<n, monotonicita dává m<l, tedy m<=l−1. Z jednotlivých
zaokrouhlení získáme

```text
n(l−1/2) <= K <= l(n−1/2),
K <= m(n+1/2) <= (l−1)(n+1/2).
```

První řádek implikuje l<=n, zatímco dolní mez prvního a horní mez
druhého dávají n<=l−1. To je spor.

Kdyby r>n, monotonicita dává m>l, tedy m>=l+1. Nyní

```text
l(n+1/2) <= K <= n(l+1/2),
K >= m(n−1/2) >= (l+1)(n−1/2).
```

Odtud l<=n<=l+1. Pro n=l se ale l i r získávají shodným výpočtem
T(K/n), takže r=l=n. Pro n=l+1 se poslední dolní mez a první horní
mez rovnají n(n−1/2); musí K=n(n−1/2) a m=n. Potom se n i l
získávají shodným výpočtem T(K/n), opět spor. Lemma je dokázáno.

Navíc, pokud m²<=K, je n>=m. Pro n>m máme
|K/n−m|<=m/(2n)<1/2, takže l=m. Pro n=m je l=T(K/n)=n=m.
Tato jednodušší část ověřuje i pomocné tvrzení tištěné odpovědi27.

## 3. Přenos lemmatu na plovoucí aritmetiku

Škálováním kladného u můžeme psát u=m/N s B<=m<=N,
B=b^(p−1), N=b^p. Položme K=BN. Potom

```text
R(1/u)       = n/B,  n=T(K/m),
R(1/R(1/u))  = l/N,  l=T(K/n),
R(1/R(1/R(1/u))) = r/B, r=T(K/l).
```

Všechna nezaokrouhlená celá měřítka K/m,K/n,K/l leží v[B,N],
a všechny jejich výsledky také. V tomto uzavřeném intervalu je
zaokrouhlení opravdu totéž co na jednotkovou síť; krajní mocniny b
jsou reprezentovatelné a jiné exponenty nic nemění. Pravidlo poloviny
je ve všech třech měřítkách stejné. Předchozí lemma dává r=n,
tedy požadovanou identitu. Záporné u řeší symetrie znamének.

Podmínka f_u<=b^(−1/2) v pomocném tvrzení odpovědi je právě m²<=K.
Tím je prověřena také struktura původního argumentu, nejen hlavní
identita. Důkaz platí včetně jednobitové a jednociferné ternární soustavy.

## 4. Úloha26: stabilita kladného součtu

Pro kladná normalizovaná u,u',v,v' nechť e=max(e_u,e_u'),
f=max(e_v,e_v') a E=max(e_R(u+v),e_R(u'+v')). Posun exponentů
q nastavíme škálováním na0. Relace a~c(ε) znamená
|a−c|<=ε b^max(e_a,e_c). Z předpokladů tedy
|u−u'|<=εb^e a |v−v'|<=εb^f.

Monotonicita zaokrouhlení a kladnost dávají E>=max(e,f).
Každý součet má absolutní chybu nejvýše b^(E−p)/2, takže

```text
|R(u+v)−R(u'+v')| <= ε(b^e+b^f)+b^(E−p)
                         <= (2ε+b^(−p))b^E.
```

To je první odpověď. Pro b2 a opačná znaménka rozdílů u−u',v−v'
je jejich součet v absolutní hodnotě nejvýše větší z obou hodnot,
a tedy stačí ε+b^(−p). Pro shodná znaménka můžeme bez újmy
předpokládat u>=u',v>=v'. Pak e=e_u,f=e_v. Nemůže platit e=f=E:
v takovém případě u,v>=2^(E−1), a tedy R(u+v)>=2^E, což by
vyžadovalo exponent aspoň E+1. Alespoň jeden exponent je proto
<=E−1 a výsledná mez je **1.5ε+2^(−p)**, jak uvádí kniha.

## 5. Úloha29: proč nelze vynechat podmínku velikosti formátu

Pro b2,p1 a doporučené sudé poloviny je pro x>0
R(x)=2^floor(log2(4x/3)); hranice mezi 2^(k−1) a2^k je3·2^(k−2).
Vezměme f(x)=x^(99/100) na kladných číslech, g(y)=y^(100/99)
a h=R∘g∘R∘f. Funkce f je ryze rostoucí a ryze konkávní.
Pro všechny celé e od42 do58 včetně vychází h(2^e)=2^(e−1).

Tyto hodnoty neověřujeme přibližným logaritmem. Pro exponent k
prvního výsledku se obě meze testují po umocnění na100:

```text
(3/4)^100 · 2^(100k) < 2^(99e)
                    < (3/4)^100 · 2^(100(k+1)).
```

Druhý krok se ověří stejně s exponenty99 a100 zaměněnými.
Všechny nerovnosti jsou ostré a přesně racionální. Volba x=2^44
dává exponenty44,43,42,41; tudíž h³(x)≠h²(x). Potvrzuje tištěný
protipříklad. Obecný Diamondův výsledek28 tím není dokázán a zůstává
samostatně otevřeným kontrolním blokem.

## 6. Úloha31: Pellovy rovnice a ztráta malé celočíselné reziduální hodnoty

Nechť p_n/q_n je n-tý konvergent řetězového zlomku sqrt(3),
s indexem0 pro1/1. Částečné podíly jsou1,1,2,1,2,... .
Dvojice čitatel/jmenovatel splňují obvyklou rekurzi
p_n=a_n p_(n−1)+p_(n−2), q_n=a_n q_(n−1)+q_(n−2),
s p_(-2)=0,p_(-1)=1,q_(-2)=1,q_(-1)=0. Po dvojicích vychází

```text
p_(2j+1)+q_(2j+1)sqrt(3) = (2+sqrt(3))^(j+1),
p_(2j)+q_(2j)sqrt(3) = (1+sqrt(3))(2+sqrt(3))^j.
```

Násobením sdruženým výrazem se znaménkem minus před sqrt(3)
dostaneme 3q_n²−p_n²=2−3(n mod2). Pro liché n tedy

```text
2p_n²+9q_n^4−p_n^4
= 2p_n²+(3q_n²−p_n²)(3q_n²+p_n²)
= p_n²−3q_n² = 1.
```

Rekurze dává p31=708158977,q31=408855776. V binary53 jsou již
zaokrouhlené hodnoty 3q31² a p31² shodné, takže rozložený výraz
ztratí člen, který má téměř přesně vyrušit2p31². Přímé čtvrté
mocniny naproti tomu nesou absolutní chyby mnohem větší nežp31².
Přesný model oddělených zaokrouhlených operací dává hodnoty
−36893488147419103232 a1002978273411373056; nezávislá hostitelská
binary64 aritmetika při stejném pořadí operací souhlasí.
To reprodukuje oba přibližné výsledky knihy. Jiné pořadí násobení
nebo slučování operací může dát jinou chybu, proto je pořadí uvedeno
v reprodukčním programu. Konvergenty jiných algebraických čísel
poskytují podobné téměř rušící velké celočíselné výrazy.

## 7. Reprodukce

`verify_accuracy_iterations.py` používá pouze přesné zlomky, s výjimkou
výslovně oddělené nezávislé binary64 kontroly úlohy31. Každý formát
má vlastní uložený výsledek v `results/accuracy-iterations.json`.
Dokončeno98 304 celočíselných případů převracení,20 784 dvojic násobení
a8 136 případů plovoucího převracení v51 formátech/pravidlech. Dále
17 přesných exponentových případů29 a40 konvergentů31. Všech55 bloků
prošlo. První běh skončil kvůli vlastnímu přepisu41<e jako41<=e;
původní obraz potvrdil správný otevřený kraj, úspěšné bloky zachovány
a obnoveny jen poslední dvě kontroly. Žádná chyba knihy v tomto bloku.
