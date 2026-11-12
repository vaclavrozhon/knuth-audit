# Nejkratší polynomiální řetězce malých stupňů

V2-X0079, 4. listopadu 2026. Úlohy §4.6.4–32 až 36,
zadání518 a odpovědi703–704. Výsledky všech pěti úloh platí.
V odpovědi35 je chybný index posledního parametru, C0239;
odpověď34 používáme se známou opravou z 20. 4. 2000.

**Řetězcový krok** používá dva dříve vypočtené výrazy;
**parametrický krok** kombinuje jeden takový výraz s novým
reálným parametrem. Povolené operace jsou sčítání, odčítání
a násobení, v řetězcovém kroku i znaménko před prvním operandem.
Proměnná x je jediným počátečním výrazem. Přesné definice
stupňů volnosti a jejich důkazy jsou v oddílech1–3 poznámky
[polyeval-chains.md](polyeval-chains.md).

Používáme zejména dva již dokázané fakty: pro obecný polynom
stupně n je třeba alespoň n+1 parametrických kroků; při m_c
řetězcových a m_p parametrických násobeních je počet stupňů
volnosti nejvýše `2m_c+m_p+[m_c=0]`. Hranatá závorka je 1,
pokud podmínka platí, jinak 0. Monický znamená vedoucí
koeficient rovný 1.

## 1. Úloha32: řídký kvartický polynom

Pět kroků knihy dává

```
t=x*x,
u=alpha1*t,
v=alpha2+u,
w=v*t,
result=alpha3+w.
```

Výstup je `alpha1*x^4+alpha2*x^2+alpha3`, tedy požadovaná
rodina, se třemi násobeními a dvěma sčítáními.
Tři volné koeficienty potřebují alespoň tři stupně volnosti;
věta A proto vyžaduje nejméně dvě sčítání či odčítání.

Dvě násobení nemohou stačit. Pro dosažení stupně4 musejí obě
být řetězcová a vytvářet postupně stupeň2 a4. Před prvním
násobením mají všechny výrazy tvar `k*x+b` s celým k. Výsledný
kvadratický člen má tedy celočíselný koeficient. Před druhým
násobením se k dispozici pouze sčítají či odčítají takové výrazy,
takže i kvadratické koeficienty jeho operandů jsou celé.
Výsledný koeficient x^4 je opět celý; následující sčítání
a odčítání to nemohou změnit. Rodina ale obsahuje například
`sqrt(2)*x^4`. Nejméně tři násobení jsou nutná i při neomezeném
počtu sčítání. Minimální délka je proto přesně5.

## 2. Úloha33: lichý stupeň

Nechť n≥3 je liché a `m=(n+1)/2`. Parametrické násobení nemůže
zvyšovat stupeň v x, takže m_c>0. Z obecné meze dostáváme

```
n+1 <= 2m_c+m_p = 2m-m_p = n+1-m_p.
```

Tedy m_p=0. Všechny parametry musejí přijít prostřednictvím
sčítání či odčítání; takových kroků je alespoň n+1.

Zbývá ukázat, že je nutný ještě nejméně jeden řetězcový
sčítací či odčítací krok. Kdyby žádný nebyl, indukcí by každý
výraz měl kladný stupeň a vedoucí koeficient +1 nebo −1:
parametrické přičtení či odečtení mění pouze konstantu a
znaménko, řetězcové násobení násobí vedoucí koeficienty.
Takto nelze získat všechny vedoucí koeficienty výsledku.
Celkem je tedy potřeba alespoň n+2 sčítání či odčítání.

Tato formulace indukce se vyhýbá nejasnostem s konstantními
mezivýsledky: bez řetězcového sčítání a parametrického násobení
žádný takový mezivýsledek nevzniká. Není nutné klasifikovat
první necelý vedoucí koeficient v řetězci, který již řetězcová
sčítání obsahuje.

## 3. Úloha34: normalizace bez řetězcových sčítání

Odstraníme kroky, které se nepodílejí na konečném výsledku.
Každému zbývajícímu výrazu lambda_i přiřadíme formální stupeň
d_i a obsah c_i, tedy koeficient x^d_i. Začneme d0=1,c0=1.
Parametrické sčítání, odčítání a násobení stupeň zachovávají;
řetězcové násobení stupně sčítá. Proto jsou všechny d_i kladné.
Nové parametry jsou formálně nezávislé, takže nevznikne
identicky nulový c_i a tato rekurze dává maximální stupeň.

Obsahy se přenášejí takto:

| Původní krok | Nový obsah c_i | Normalizovaný krok pro nu_i=lambda_i/c_i |
|---|---|---|
| alpha+lambda_k | c_k | alpha/c_k+nu_k |
| alpha−lambda_k | −c_k | −alpha/c_k+nu_k |
| alpha*lambda_k | alpha*c_k | nu_k, kopie k odstranění |
| s*lambda_j*lambda_k, s=±1 | s*c_j*c_k | nu_j*nu_k |

Každý původní sčítací krok tedy zůstane jedním parametrickým
sčítáním, všechny záporné znaky se absorbují do parametrů a
obsahů. Každé parametrické násobení se odstraní. Nakonec
přidáme jediné parametrické násobení `c_r*nu_r`. Protože
původně bylo alespoň jedno, počet násobení nevzroste.

**Nulové obsahy.** Z rekurzí je c_r, až na znaménko, součinem
parametrů těch násobení, jejichž výsledky se podílejí na
výstupu, s kladnými celočíselnými exponenty. Pokud kterýkoli
obsah v této části řetězce je nulový, je nulový i c_r.
Naopak požadavek nenulového koeficientu x^n dává c_r≠0 a
všechny použité obsahy nenulové. Uvedené podíly jsou proto
oprávněné na celém požadovaném rozsahu; ztráta stupně je
výslovně vyloučena zadáním. Zbytečné kroky jsme odstranili
ještě před dělením.

Známá oprava z 20. 4. 2000 mění v odpovědi703 při nahrazování
kopií „that uses lambda_j“ na „that uses lambda_i“.
Zahrnutí znaménka s výše rovněž výslovně pokrývá všechny
případy obecné definice řetězce.

## 4. Úloha35: obecný polynom stupně4

Předpokládejme tři násobení a nejvýše čtyři sčítání/odčítání.
Pět nezávislých koeficientů vyžaduje pět parametrů. Alespoň
jedno násobení proto musí být parametrické. Stupeň4 zároveň
vyžaduje dvě řetězcová násobení, takže právě jedno násobení
je parametrické a všechna čtyři sčítání jsou parametrická.
Úloha34 převede řetězec na dvě řetězcová násobení, parametrická
sčítání a jedno závěrečné násobení vedoucím koeficientem.

Pro monický výstup můžeme toto poslední násobení vynechat.
První násobení vytvoří kvadratický výraz Q. Druhé musí násobit
dva výrazy stupně2. Mezi násobeními se pouze přičítají
konstanty, takže tyto dva výrazy jsou Q+b a Q+c. Libovolný
počet postupných parametrických sčítání můžeme sloučit do
jediného posunu. Výsledkem je podrodina

```
(x^2+A*x+B)(x^2+A*x+C)+D
  = x^4+2A*x^3+(E+A^2)*x^2+EA*x+F,
E=B+C, F=BC+D.
```

Tato zastřešující rodina má jen tři volné parametry A,E,F.
Úplnost rozboru nezávisí na sdílení posunů či opakovaném
použití stejného operandu: dovolíme nezávislé posuny, a tím
množinu výsledků jen zvětšíme. Žádná dřívější násobení nelze
vynechat při dosažení stupně4.

Označíme-li koeficient x^i jako c_i, každý výstup splňuje

```
8c1−4c3*c2+c3^3=0.
```

Například x^4+x do této rodiny nepatří. Čtyři sčítání tedy
nemohou stačit pro obecný polynom; nejméně pět je nutných.

**C0239 confirmed.** V odpovědi35 na straně704 je `D=alpha6`.
Řetězec na703 má ale pouze alpha1,…,alpha5 a jeho poslední
krok je `lambda7=alpha5+lambda6`. Správně tedy `D=alpha5`.
Při alpha1=…=alpha4=0 a alpha5=1 dostáváme x^4+1, takže
poslední aditivní konstanta je skutečně1. Alpha6 zde není
definováno. Ostatní definice A,B,C,E,F i výsledná dolní mez
zůstávají správné.

## 5. Úloha36: obecný polynom stupně6

Při čtyřech násobeních a nejvýše šesti sčítáních je třeba
sedm parametrů, tedy nejméně jedno parametrické násobení.
Stupeň6 potřebuje alespoň tři řetězcová násobení, protože
dvě mohou vytvořit nejvýše stupeň4. Proto jde právě o tři
řetězcová násobení, jedno parametrické a šest parametrických
sčítání. Použijeme opět úlohu34 a monický výstup.

První násobicí výstup má stupeň2. Druhý musí mít stupeň3
nebo4: při stupni nejvýše2 by třetí nedosáhl6. Dostáváme
přesně dvě možnosti:

1. Stupně2,3,6: třetí násobení použije dvě posunuté kopie
   stejného kubického výrazu.
2. Stupně2,4,6: druhé násobení použije dvě posunuté kopie
   prvního kvadratického výrazu, třetí použije posunutý
   kvadratický a posunutý kvartický výstup.

Po sloučení všech posunů jsou výsledky podrodinami právě
těchto dvou rodin z odpovědi704:

```
I:  (x^3+A*x^2+B*x+C)(x^3+A*x^2+B*x+D)+E,
II: (x^4+2A*x^3+(E+A^2)*x^2+EA*x+F)(x^2+A*x+G)+H.
```

Každá má nejvýše pět parametrů. První má dokonce jen čtyři
účinné parametry A,B,C+D,CD+E; toto zpřesnění není pro důkaz
potřeba. Konečná unie obou rodin má tedy nejvýše pět stupňů
volnosti, zatímco obecný monický sextický polynom potřebuje
šest. Při čtyřech násobeních je tedy pro obecný stupeň6
nutných nejméně sedm sčítání či odčítání.

Konkrétní společný chybějící polynom je x^6+x. V rodiněI
je c5=2A, c4=A^2+2B. Jejich nulovost vynutí A=B=0 a pak
je c1=B(C+D)=0. V rodiněII je c5=3A; jeho nulovost
vynutí A=0, a celý výstup je sudý. Ani zde tedy c1=1 nelze.
Tento svědek se týká zastřešujících rodin pro obecný řetězec;
netvrdíme, že konkrétní x^6+x samo potřebuje sedm sčítání.

## 6. Evidence a hranice

Sazba518,703,704 prohlédnuta. Všech šest vrstev errat
prohledáno podle stránek i obsahu; C0239 nenalezeno.
Jediná relevantní nalezená oprava pro32–36 je známý index
v odpovědi34. Obecné minimální počty dokazujeme výše,
symbolická kontrola pouze doplňuje tento důkaz.

Skript verify_polyeval_small_bounds.py kontroluje řídký
kvartický řetězec, šest mezikroků normalizace včetně záporného
součinu, všechny kostry dvou a tří násobení po dokázané
normalizaci, tři obecné parametrické identity a tři koeficientové
relace. Nezaměňujeme vyčerpání těchto malých koster za
vyčerpání všech původních aritmetických řetězců.

Pozdější fyzický dotisk a prvenství C0239 neověřeny.
Návrh hlášení nebyl odeslán.

Skript prošel jednou, PID1599332,0.313364954s;
obalPID1599331,1.056868677s,limit120s,exit0. Žádná chyba ani
opakování úspěšné kontroly.

## 7. Doplnění primárních zdrojů k předchozím blokům

Dokončeno stažení celého svazku Problemy Kibernetiki5.
Titulní strana a tiráž byly přečteny vizuálně: Moskva1961,
předáno do sazby1.12.1960, schváleno k tisku2.3.1961.
Rok1961 v Knuthově odkazu na Panův článek je tedy správný.
Eveův odlišný rok1959 není údajem tohoto vydání. Panův
článek byl přijat28.11.1958 a sám odkazuje na jiný svůj
článek v DAN127(2),266–269(1959); toto rozlišení je doloženo
na straně29.

Belaga: strany7,11,15 prohlédnuty vizuálně;11–13 přečteny
také v textové vrstvě. Úvod a věta2 výslovně obsahují
dolní mez n aditivních operací, závěr uvádí přijetí30.5.1958.
Tím je ověřen obsah citace k větě A, nikoli celý článek.

Pan: vizuálně přečteny17,18,28,29; textově také19.
Strana28 výslovně rozlišuje nulový jmenovatel s nenulovým
čitatelem a současné vymizení obou. Ve druhém případě
dovoluje volný parametr. To nezávisle podporuje výpočet
D=N=0 v C0236. Status ponecháváme candidate, protože
Knuthovo „this method“ lze stále číst úzce jako doslovný
postup dělení. Neprověřovali jsme zde všechny Panovy
konstrukce stupňů8–12 ani jejich tabulku počtů.

Tento dodatek aktualizuje historické mezery X0077/X0078;
jejich starší manifesty zachycují stav v okamžiku příslušných
checkpointů. Motzkinův původní abstrakt zůstává nepřečtený.
