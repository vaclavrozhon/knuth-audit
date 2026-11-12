# D141–D142 — celé MPR39–40

7. listopadu 2026. Zadání p15/file35, odpověď p377/file397
a autorův Pre-Fascicle5A p33/file39 přímo zobrazeny.
Původní(15) na p4/file24 bylo znovu zobrazeno pro přesné
dosazení; jeho úplný důkaz D095 se přebírá bez opakování.

## D141, 39(a): podmíněný model a všechny okamžiky

Poissonův parametr je konečné μ≥0 a pravděpodobnost
líhnutí je 0≤p≤1. Při daném N=n má n vajec podle zadaného
modelu nezávislé indikátory vylíhnutí s parametrem p.
Proto K podmíněné na N=n je binomické(n,p): pro 0≤k≤n
má každá konkrétní k-prvková množina vylíhnutých vajec
pravděpodobnost pᵏ(1−p)ⁿ⁻ᵏ a takových množin je binom(n,k).
Pro n=0 je součet prázdný a K=0.

Linearita konečného součtu dává E(K|N=n)=np na každém
kladném vlákně. Tedy E(K|N)=pN s pravděpodobností1.
Když μ>0, jsou všechna celočíselná n≥0 kladná vlákna.
Při μ=0 se použije pouze N=0. Kdyby se v prostoru navíc
ponechaly nulové body s N>0, autorova konvence na těchto
vláknech dává EK; netvrdíme další bodovou rovnost pN
na nemožných hodnotách. Jde o tutéž konvenci jako D094/D138.

Ze série přímo, bez odhadu či diferenciace na kraji,

    EN=e^(−μ)∑ₙ≥₁ n μⁿ/n!
      =μ e^(−μ)∑ᵣ≥₀ μʳ/r! = μ.

Při μ=0 je to rovněž0, s obvyklým 0⁰=1 pro atom N=0.
Jelikož 0≤K≤N a EN<∞, obě proměnné jsou integrabilní.
Převzatá věžová identita proto opravňuje každý krok39(b):

    EK=E(E(K|N))=E(pN)=p EN=pμ.

## 39(c): každý faktor společné hmotnosti

Položme q=1−p a λ=qμ. Pro n≥k≥0 je

    pₙₖ=P(N=n,K=k)
        = e^(−μ) μⁿ/n! · n!/(k!(n−k)!) · pᵏqⁿ⁻ᵏ
        = e^(−μ)(μp)ᵏ/k! · f(n−k),
    f(r)=λʳ/r!, r≥0.

Pro n<k nebo záporné indexy je hmotnost0. Tento rozklad
obsahuje všechny faktoriály a mocniny vytištěné v odpovědi.
Při λ=0 se f(0)=1 a f(r)=0 pro r>0, takže zůstává platný
i pro nulový počet nevylíhnutých vajec.

Pro každé k s P(K=k)>0 je společný faktor
Aₖ=e^(−μ)(μp)ᵏ/k! kladný, a proto jej lze z podílu
v odpovědi zkrátit. Máme

    ∑ₙ≥ₖ pₙₖ = Aₖ∑ᵣ≥₀f(r)=Aₖe^λ,
    ∑ₙ≥ₖ n pₙₖ = Aₖ∑ᵣ≥₀(k+r)f(r).

Tištěný mezikrok n f(n−k)=k f(n−k)+(n−k)f(n−k)
je přesně rozklad n=k+r. Pro r≥1 platí

    r f(r)=r λʳ/r!=λ f(r−1).

Pro r=0 je příspěvek r f(r)=0; nevzniká potřeba f(−1).
Proto

    ∑ᵣ≥₀ r f(r)=λ∑ᵣ≥₁f(r−1)=λe^λ,
    E(N|K=k)=(k e^λ+λe^λ)/e^λ=k+λ.

Všechny série jsou nezáporné a uvedené součty konečné,
což opravňuje posuny i podíl. Tím je úplně doložen
vytištěný výsledek E(N|K)=K+(1−p)μ.

Navíc společný zákon (K,R=N−K) lze přímo přepsat jako

    P(K=k,R=r)
      =[e^(−μp)(μp)ᵏ/k!]·[e^(−λ)λʳ/r!].

Oba faktory se sečtou na1 a určují nezávislé Poissonovy
proměnné. Je to další přímá interpretace výsledku:
znalost K ponechává průměr λ nevylíhnutých vajec.
Nezávislost zde plyne z přesné faktorizace, není dodatečně
předpokládaná.

## 39: všechny degenerované parametry a nulová vlákna

Pro p=0 je K=0 jistě a E(N|K)=EN=μ, souhlasně s výsledkem.
Pro p=1 je K=N jistě, λ=0 a E(N|K)=K. Pro μ=0 jsou N=K=0,
ať je p jakékoli. Tyto případy nevyžadují krácení nulového Aₖ.
Když μp>0, má každé k≥0 kladnou hmotnost. Když μp=0,
jediná kladná hodnota K je0; pro nulové události K=k>0
autor stanoví E(N|K=k)=EN=μ. Výraz k+λ se na takových
událostech neprohlašuje za povinný bodový reprezentant.
Výsledná identita náhodných proměnných platí s pravděpodobností1,
jak je pro toto podmínění zamýšleno. Žádný nový kandidát
kvůli standardnímu nulovému reprezentantu nevzniká.

## D142, 40: každý krok přímé nerovnosti

Nechť m<M jsou konečná reálná čísla a X≤M. V souladu
s definicí očekávání pracujeme nejprve s konečným EX.
Označme A={X>m} a p=P(A). Bodově platí

    X≤m[¬A]+M[A].

Na ¬A je to předpoklad X≤m; na A je to zadané X≤M.
Očekávání a rozklad P(¬A)=1−p dávají přesně tištěný krok

    EX≤(1−p)m+pM=m+p(M−m).

Protože M−m>0, lze odečíst m a dělit bez obrácení znaménka:

    P(X>m)≥(EX−m)/(M−m).

Případ EX≤m dává nekladnou pravou stranu a je dovolený.
Pravá strana nikdy nepřesáhne1, protože EX≤M. Pro p=0
má X≤m skoro jistě a nerovnost zůstává platná; pro p=1
je přímý mezikrok prostě EX≤M. Při X=M skoro jistě je
rovnost1=1. Obecně ji dosahuje každý zákon soustředěný
na {m,M}, včetně obou jednobodových krajů. Pokud bychom
připustili EX=−∞, horní omezení X vylučuje +∞ a mez je
jen triviální; kniha takový rozšířený moment nevyžaduje.

## 40: přesné dosazení do(15)

Na oboru možných hodnot X, tedy (−∞,M], je funkce
f(x)=M−x nezáporná. Pro S={x:x≤m} a s=M−m>0 máme
f(x)≥s na S. Pokud chceme f definovat nezáporně na celé
reálné ose, použijeme max(0,M−x); na žádné možné hodnotě
X se tím f(X) nemění. To je pouhé rozšíření oboru
tištěné funkce, nikoli nová matematická oprava.

D095/(15) se všemi předpoklady dává

    P(X≤m)≤E(M−X)/(M−m)=(M−EX)/(M−m).

Odečtením od1 získáme

    P(X>m)≥1−(M−EX)/(M−m)=(EX−m)/(M−m).

Také zvolená ostrá nerovnost X>m a neostrá v S přesně
odpovídají komplementu. Oba tištěné důkazy jsou platné.

## Rozsah a výjimky

Celé39(a–c) i40 jsou checked/reviewed, každý tištěný
mezikrok je odůvodněn. PDF+PS, všech6lokálních vrstev
errat a3TeX bez použitelné opravy; hashe a nalezené
nesouvisející kontexty jsou uložené v JSON. Žádný nález,
kandidát, numerický běh ani restart.

Bibliografická výjimka: přesná citace G. Grimmett,
D. Stirzaker, Probability and Random Processes
(Oxford:1982), §3.7, nebyla ověřena z daného vydání.
Žádný důkaz se z ní nepřebírá; všechny výpočty39 jsou výše.

Původní file35/p15 je nyní celý posouzen v D129–D142,
včetně dřívějších výzkumných dovětků30 a všech uvedených
bibliografických výjimek. File397/p377 má tímto pokryté
pouze39–40; odpovědi41–50 zůstávají otevřené.
