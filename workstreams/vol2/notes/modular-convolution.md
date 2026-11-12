# §4.3.2-14: vážená konvoluce modulo 2^q−1

Kontrola 2. listopadu 2026. Zadání294, odpověď632 a oprava31.7.2020
na straně14 souboru `all2-pre.pdf` byly vizuálně přečteny. Starý text
bez faktoru2 má známou chybu; oprava zaručuje celočíselné zaokrouhlované
koeficienty. Závěrečné dělení dvěma však musí být modulární. Doslovná
reálná interpretace opraveného součtu není správná; otázku, zda toto
text již implicitně předpokládá, vedeme zvlášť jako **V2-C0102 candidate**.
Matematika úlohy je níže uzavřena, nejde o otevřený algoritmický problém.

## Rozklad a váhy

Nechť q,n jsou kladná celá čísla a M=2^q−1. Vstupy U,V jsou celá čísla
z[0,2^q), rozdělená do n sousedních bloků. Definujme

```
e_k = floor(kq/n),    r_k = kq mod n,    f_k = r_k/n,
a_k = 2^(-f_k) = 2^(e_k-kq/n),           0 <= k < n.
```

Platí1/2<a_k<=1. Číslice u_k,v_k mají šířku e_(k+1)−e_k bitů, kde
e_n=q; tedy `U=sum u_k 2^e_k`, obdobně V. Je-li n>q, některé bloky
mají šířku0 a číslici0. Ani tento okraj není překážkou správnosti.

Cyklická konvoluce vážených bloků znamená

```
z_k = sum_(i+j≡k mod n) a_i a_j u_i v_j.
```

Součet indexů se redukuje modulo n, ale hodnoty jsou zatím skutečná
reálná čísla. Píšeme `i+j=k+hn`, kde h je0 nebo1. Potom

```
f_i+f_j-f_k = hq-e_i-e_j+e_k ∈ {0,1}.
```

Je to celé číslo a součet dvou zlomkových částí po odečtení jejich
zlomkové části. Proto `2*a_i*a_j/a_k` je buď2, nebo1. Číslo

```
t_k = 2*z_k/a_k
    = sum_(i+j≡k) u_i v_j * 2^(1-f_i-f_j+f_k)             (1)
```

je **přesně celé**. Při numerickém výpočtu stačí absolutní chyba pod1/2,
aby zaokrouhlení na nejbližší celé číslo vrátilo t_k. Bez faktoru2 může
být výsledek půlčíselný, což je obsah opravy2020.

## Obecný důkaz rekonstrukce

Vytvořme celé nezáporné číslo `S=sum t_k 2^e_k`. Příspěvek páru i,j
do S má exponent

```
1-f_i-f_j+f_k+e_k = 1+e_i+e_j-hq.
```

Ten je nezáporný, protože pochází z celočíselného násobku2^e_k.
Jeho rozdíl od exponentu odpovídajícího členu2UV je hq. Jelikož
2^q≡1 modulo M, dostáváme

```
S ≡ 2UV (mod M).                                         (2)
```

Pro q>=2 je2 invertibilní modulo M a inverze je2^(q−1).
Nejprve sečteme překrývající se bloky v S a zredukujeme `R=S mod M`.
Správný kanonický výsledek je

```
w = (R + M*(R mod 2))/2.                                 (3)
```

Čitatel je sudý. Když je R sudé, výsledek leží v[0,M); když je liché,
platí R<=M−2, takže opět0<=w<M. Rovnice2 a jednoznačnost zbytku
potvrzují w=(UV) mod M. Pro q1 je M1,R0,w0 a tentýž algoritmus funguje.
Ekvivalentní zápis, vhodný pro vysvětlení půlbitu, je

```
w = (floor(S/2) + 2^(q−1)*(S mod 2)) mod M.               (4)
```

Bit původně na pozici−1 se tedy přesune na pozici q−1. Jde o cyklický
posun doprava; není přípustné jej zahodit nebo počítat běžný reálný
zbytek půlčíselného S/2. Pro n>q může být e_k0 u více k; společné S
řeší všechny tyto příspěvky současně. Výsledné bloky w_k se z w opět
vyberou na pozicích e_k..e_(k+1)−1.

## Přesnost s ověřitelnými intervaly

Odpověď neudává pevný strojový formát; říká, že se má zachovat dostatečná
přesnost. Následující konstrukce dokazuje, že to lze provést certifikovaně.
Není to předstíraná analýza chyby libovolné implementace FFT.

Pro počet pomocných bitů p>=1 a B=2^p spočteme celé číslo

```
A_k = floor((2^(pn-r_k))^(1/n)).
```

Jeho správnost ověří dvě celočíselná porovnání
`A_k^n <= 2^(pn-r_k) < (A_k+1)^n`. Dostaneme interval
`a_k∈[A_k/B,H_k/B]`, kde H_k=A_k při přesné odmocnině a jinak A_k+1.
Protože číslice jsou nezáporné, přesná celočíselná přímá konvoluce dává

```
L_k = sum_(i+j≡k) u_i v_j A_i A_j,
H'_k = sum_(i+j≡k) u_i v_j H_i H_j,

2*z_k/a_k ∈ [2*L_k/(B*H_k), 2*H'_k/(B*A_k)].              (5)
```

Vypočteme nejmenší a největší celé číslo v tomto racionálním intervalu.
Pokud souhlasí, je t_k určeno přesně. Jinak zdvojnásobíme p. Intervaly
se smršťují k t_k; protože t_k je celé a počet souřadnic konečný,
postup skončí. Volba délky intervalu menší než1 sama o sobě nestačí
bez znalosti celočíselnosti; zde ji zaručuje1. Program výslovně
ověřuje, že interval obsahuje právě jedno celé číslo.

Tato metoda kontroluje numerický princip pomocí přímé konvoluce.
Rychlé provedení konvoluce a jeho složitost patří do§4.3.3/§4.6.4.
Odhad libovolného hardwarového FFT nelze odvozovat pouze z testování
náhodných vstupů. Podrobné meze v citovaném Percivalově článku nejsou
v tomto bloku celé znovu auditovány.

## Vztah k pramenům a známým opravám

[Percivalův autorský PDF](https://www.daemonology.net/papers/fft.pdf),
strany387 a389, byly vizuálně přečteny; strana388 čtena v extrahovaném
textu. Rovnice3.3/3.4 na389 používají **horní** celou část, zatímco
Knuthovo zadání používá dolní. Proto není přípustné bez změny vah
přenášet tvrzení o celočíselnosti přímo z této verze. Rozšíření na
moduly k*2^n±1 odpovídá dodatku2003. Datum2002 v erratu není tímto
auditem odmítnuto: první strana výslovně uvádí elektronické vydání
5.3.2002. Úplné ověření všech vět článku nebylo cílem.

Článek Crandall–Fagin1994 byl bibliograficky nalezen jako autorský
upload Barryho Fagina; původní časopisové PDF zde získáno nebylo
(AMS403 z dřívějšího bloku; autorský web selhal při TLS handshake).
Nespojujeme tuto nedostupnost s důkazem nesprávnosti jejich algoritmu.

Zkontrolovány `all2-prepre` (dodatek7.4.2003), `all2-pre`
(oprava31.7.2020), `all2`, `err2` a aktuální `sources/err2.textxt`.
Poslední tři nemají další relevantní opravu632/konvoluce.
Právě problém formulace závěrečného půlení řeší C0102; nejde o nové
ohlášení již známého chybějícího faktoru2.

## Reprodukce

`verify_modular_convolution.py`, běh96963, exit0. Výsledky jsou v
`results/modular-convolution.json` a `.log`; checkpointy se neopakují.

- 189324 všech párů pro q1..7,n1..q+2, včetně nulových bloků a obou
 reprezentací nuly0 a2^q−1.59270 případů má liché S, takže obyčejné
 půlení vede na půlčíslo;100214 případů má necelé původní z_k/a_k.
- 720 dalších případů do16384 bitů, včetně maximálních vstupů.
- 416 intervalových kontrol do4096 bitů;126 si vynutilo zvýšení
 přesnosti, celkem222 zdvojení. Nejvyšší p bylo256.
- Orákulum je přímý celočíselný součin U*V a jeho zbytek. Intervalový
 výpočet nečte vzorec1; teprve jeho výstup se porovnává s přesnými
 koeficienty a nakonec s nezávislým součinem.

Úloha14 je vyřešena včetně známé opravy. Kandidát C0102 zachovává
nejistotu o zamýšlené interpretaci, nikoli nejistotu matematického výsledku.
