# §1.2.6-42: bilaterální rozvoje a V1-C0007

Audit 1. listopadu 2026. Zobrazen původní text s. 487
v měřítkách 150 a 300; zadání na s. 72. Bilaterální řada
je součet přes všechna celá k. Níže konvergence znamená
konvergenci obou jednostranných ocasů; symetrická hlavní
hodnota není automaticky konvergencí takové řady.

## Konvence pro zobecněný koeficient

Odpověď definuje C(z,w) jako limitu Gamma podílu, nejprve
v dolním indexu w a poté v horním indexu z. To je popsáno
v `binomial-exercises.md`, (E2). Zvláště `C(z,k)=0`
pro každý záporný celý dolní index k, včetně záporných
celých horních indexů. Právě proto sama odpověď upozorňuje
na výjimky ze symetrie C(z,w)=C(z,z−w).

## Přesný protipříklad bilaterální konvoluce

V poslední identitě odpovědi 42 položme
`r=s=alpha=beta=−1/2`. Pro celé k je první faktor

```text
C(−1/2,−1/2+k)
 = Gamma(1/2)/(Gamma(k+1/2)Gamma(1−k)).                    (B2)
```

Pro k>=1 je tento koeficient 0: 1/Gamma(1−k)=0,
zatímco ostatní dva Gamma faktory jsou konečné a nenulové.
Druhý koeficient se získá náhradou k→−k a je konečný.
Pro k<=−1 je naopak druhý koeficient 0 a první konečný.
Při k=0 jsou oba koeficienty přesně 1. Proto

```text
sum_{k in Z} C(−1/2,−1/2+k) C(−1/2,−1/2−k) = 1.          (B3)
```

Pravá strana tvrzené konvoluce je ale `C(−1,−1)=0`.
Pro každé nesingulární z blízko −1 je totiž vnitřní
limita při w→−1 rovna 0, díky jednoduché nule 1/Gamma(w+1).
Vnější limita z→−1 proto také dává 0. V (B3) tedy
není problém konvergence ani neurčitosti 0*infinity:
všechny jednotlivé koeficienty jsou konečné a pouze jediný
součin je nenulový. Nejsou přítomny žádné komplexní mocniny.

Kdyby se na pravé straně místo předepsaného pořadí limit
pokračovalo podél z=w, dostali bychom 1, ale to je
**jiná definice** a není slučitelná s nulovou konvencí
negativních dolních indexů používanou v knize.

Zvětšený sken potvrzuje obecné tvrzení pro všechny komplexní
parametry, pokud řady konvergují. V `all1-prepre`, `all1-pre`,
`all1`, `err1` a `err1.textxt`, ověřených 1. listopadu 2026,
není k tomuto tvrzení nalezena oprava. Jediná historická
změna výslovně označená s. 487 doplňuje Ramusův odkaz
do odpovědi 38. Nález **V1-C0007** je proto potvrzený
v kontrolovaných zdrojích. Prvenství, obsah citovaného
Ramshawova článku a fyzický exemplář nejsou doloženy.

## První, binomický bilaterální rozvoj: kontrolní důkaz

První rozvoj na téže stránce je jiný výrok. Pro Re(r)>−1
a libovolné komplexní w platí Fourierův koeficient

```text
(1/(2pi)) integral_{−pi}^pi
        (1+exp(it))^r exp(−iwt) dt = C(r,w).               (B4)
```

Uvnitř intervalu používáme
`(1+exp(it))^r=(2cos(t/2))^r exp(irt/2)` s kladným
kosinem. Konce jsou integrovatelné díky Re(r)>−1.
Pro Re(w)<0 lze (B4) přímo odvodit substitucí u=exp(it)
a deformací kružnice na oba břehy úseku (−1,0), kde
u^(−w−1) má zvolený řez. Příspěvek malé kružnice kolem
0 mizí, a příspěvek u=−1 má integrabilní řád Re(r)>−1.
Rozdíl obou větví dává

```text
−sin(pi w)/pi * B(−w,r+1)
 = Gamma(r+1)/(Gamma(w+1)Gamma(r−w+1)).
```

Poslední rovnost je reflexní formule Gamma. Obě strany
(B4) jsou celistvé ve w, takže shoda pokračuje na všechna w.

Funkce `exp(−i alpha t)(1+exp(it))^r` na (−pi,pi)
má tedy Fourierovy koeficienty C(r,alpha+k). Je hladká
v každém vnitřním podintervalu a integrovatelná na celém
intervalu; lokalizace Fourierovy řady, nebo přímo Dirichletovo
kritérium s Gamma asymptotikou koeficientů, dává její hodnotu
v každém vnitřním bodě. Po vynásobení exp(i alpha t)
získáme požadovanou binomickou identitu pro z=exp(it),
−pi<t<pi, Re(r)>−1. Oba ocasy konvergují samostatně:
jejich vedoucí člen je konstanta krát
`(−exp(±it))^k k^(−r−1)` a má derivaci amplitudy
O(k^(−Re(r)−2)), což ospravedlňuje Abelovu sumaci.

Pro Re(r)>0 lze dojít i k z=−1 absolutní konvergencí;
součet je 0. Pro obecné neterminující koeficienty mimo
jednotkovou kružnici nemohou konvergovat oba ocasy,
protože jeden obsahuje exponenciálně rostoucí |z|^k.
Výjimky s jednostrannou podporou se redukují na obyčejnou
binomickou větu: při celém alpha na rozvoj v z, při
celém r−alpha a nesingulárním r na rozvoj v 1/z.
Nezáporné celé r s celočíselným posunem dává konečnou větu.
Záporné celé r s necelým alpha dávají póly jednotlivých
koeficientů a nejsou konvergentními číselnými řadami.

## Proč obecná konvoluce potřebuje samostatné podmínky

V bezpečném oboru Re(r),Re(s)>−1/2 jsou obě funkce
z (B4), s posuny alpha,beta, v prostoru L²(−pi,pi).
Parsevalova rovnost pro jejich bilineární součin dává
`sum_k C(r,alpha+k)C(s,beta−k)=C(r+s,alpha+beta)`;
součet je absolutně konvergentní podle Cauchyho–Schwarzovy
nerovnosti. To nezahrnuje (B3), kde r+s=−1. Přechod
na další singulární parametry není dovolen pouhým tvrzením,
že konkrétní řada náhodou konverguje. Příklad (B3) ukazuje
právě selhání takového přechodu při iterovaném limitování.
Úplná maximalizace opraveného oboru není pro vyvrácení
otištěného tvrzení potřeba a zde se neprohlašuje za hotovou.
