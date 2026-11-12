# D147–D151 — celé MPR45–49

7. listopadu 2026. Původní zadání p16/file36 a celá
odpovědní p377/file397 byly zobrazeny, stejně jako
autorův PS p16/file22 a p34/file40. D095–D096 už
dokázaly(15),(16),(21)–(23) a konkrétní kvadratickou
část47; přebíráme jejich důkazy, nikoli pouze status.
Níže jsou doplněny všechny tištěné odpovědi a okraje.

## D147, 45: každý předpoklad Markovova dosazení

První momentový princip(21) se vztahuje na nezáporné
celočíselné X. Právě tato dvě omezení dávají ekvivalenci
{X>0}={|X|≥1} a rovnost E|X|=EX. Pro práh m=1>0
v(16), což je dokázaná instance(15), proto dostaneme

    P(X>0)=P(|X|≥1)≤E|X|/1=EX.

Tím je odvození z(15) i celý mezikrok odpovědi doložen.
Pro X=0 skoro jistě jsou obě strany0. Při konečném EX
jsou splněny momentové podmínky; s povoleným EX=+∞
je odhad pouze triviální. Nezávislost není potřebná.
Nevydáváme výsledek za odhad pro libovolné kladné
reálné X; celočíselnost je součást původního(21).

## D148, 46: Jensen i přímý rozklad rozptylu

Pro reálné U s E U²<∞ existuje také E|U|, například
z 2|U|≤1+U². Je-li m=EU, pak

    E(U−m)²=E U²−2m EU+m²=E U²−(EU)²≥0.

Všechny členy jsou integrabilní, takže je rozvinutí
oprávněné. To dokazuje vytištěnou obecnou nerovnost
E U²≥(EU)² a přesnou identitu. Alternativně je to
D095/Jensen pro konvexní funkci u², jejíž druhá
derivace je2; oba tištěné důkazy jsou tím ověřeny.

V(23) jde o podmíněný prostor A={X>0} s q=P(A)>0.
Jeho druhý moment je nejvýše E X²/q<∞, takže stejný
důkaz dává přesně

    E(X²|A)≥(E(X|A))².

Podmíněná rovnost nastane právě tehdy, je-li X na A
konstantní skoro jistě: nezáporný podmíněný součet
čtverců musí být0. Pro q=1 jde o původní prostor.
Kdybychom izolovanou nerovnost četli pro q=0, autorova
konvence ji převádí na E X²≥(EX)², takže je také
pravdivá; samotné dělení v(23) se tam nepoužívá.
Původní strana5 už výslovně předpokládá, že X není
skoro jistě0. Žádná nulová podmínka není zatajena.

## D149, 47: obě dominance i celý zlomkový dovětek

Pro Y=max(0,X) máme bodově Y≥X a Y²≤X²:
na X≥0 jsou rovnosti, na X<0 je Y=0. Očekávání
dává obě požadované nerovnosti. Konečný druhý moment
X stačí také na konečnost všech zde použitých prvních
momentů. Při nekonečném druhém momentu je druhá
dominance stále pravdivá v rozšířeném smyslu,
ale níže používáme konečné podíly.

Nechť μ=EX≥0 a 0<ν=E X²<∞. Potom EY≥μ≥0.
Navíc E Y²>0: kdyby E Y²=0, měli bychom X≤0 skoro
jistě; μ≥0 by pak vynutilo X=0 skoro jistě, protiν>0.
Z(EY)²≤E Y² a pozitivního EY je užitečný podíl definován.
Přesněji EY>0 plyne z P(Y>0)>0 a nezápornosti Y.
D096/(22) tedy dává

    P(X>0)=P(Y>0)≥(EY)²/E Y²
                           ≥μ²/E Y²≥μ²/ν.

První z posledních dvou kroků využívá právě μ≥0,
druhý E Y²≤ν a kladnost jmenovatelů. Pro μ=0 je
konečná pravá strana0 a všechny kroky zůstávají platné.
Pro ν=0 je X=Y=0 skoro jistě a P(X>0)=0 přímo;
nevyhodnocuje se0/0. Podmínka μ≥0 je podstatná pro
dovětek, například X=−1 by bez ní dal nesprávné0≥1.
Samotné dvě dominance v zadání platí i pro zápornéμ.

## D150, 48: součet, každá kovariance a Chebyshev

Položme S=∑ⱼ₌₁ⁿXⱼ a V=∑ⱼ₌₁ⁿσⱼ². Předpoklady
dávají EXⱼ=0, E Xⱼ²=σⱼ²<∞. Pro i≠j je z nezávislosti
E|XᵢXⱼ|=E|Xᵢ|E|Xⱼ|<∞ a E(XᵢXⱼ)=EXᵢEXⱼ=0.
Rozvinutím konečného čtverce tedy dostáváme

    ES=0,    E S²=V.

Pro a>0 je Chebyshevova mez zadaná v úvodu přesně
Markov pro nezáporné S² a kladný práh a²:
P(|S|≥a)≤V/a². Tato věta nevyžaduje nezávislost po
výpočtu V; nezávislost byla použita pro nulové křížové
členy. Při a=0 se tento úvodní podíl nepoužívá.

## 48: celý jednostranný krok a všechny okraje

Pro a≥0 vezměme T=a−S. Má ET=a≥0 a

    E T²=a²−2a ES+E S²=a²+V.

Je-li a²+V>0, úloha47 dává přesně tištěný mezikrok

    P(a−S>0)≥a²/(a²+V).

Komplementem je {S≥a}, nikoli {S>a}. Proto

    P(S≥a)≤1−a²/(a²+V)=V/(a²+V).

Pro a=0,V>0 je pravá strana1 a důkaz stále platí.
Pro a>0,V=0 je S=0 skoro jistě a obě strany jsou0.
Ve společném degenerovaném případě a=V=0 je S=0
skoro jistě a P(S≥0)=1; podíl0/0 se nepočítá. Chceme-li
jeden všude definovaný horní odhad, položíme jej pro
a=0 roven1 a pro a>0 použijeme vytištěný zlomek.
Jde o explicitní doménu podílu a přímé vyřešení
degenerovaného zákona, nikoli o nový kandidát.

Pro a>0,V>0 je zlepšení proti V/a² přesně

    V/a²−V/(a²+V)=V²/(a²(a²+V))>0.

Nová mez je navíc menší než1. Pro V=0 jsou obě meze0.
To odůvodňuje tištěné „somewhat better“ v celé
netriviální doméně, včetně případů, kdy stará mez
byla větší než1.

Pro n=1 a obecnou proměnnou Z s konečným druhým
momentem aplikujeme výsledek na X₁=Z−EZ. Dostaneme

    P(Z≥EZ+a)≤var(Z)/(var(Z)+a²),

přesně Cantelliho formulaci odpovědi. Naopak její
aplikace na S vrací celý n-proměnný výsledek. U n=1
je nezávislost prázdná podmínka. Nulové okraje jsou
tytéž jako výše; a ani variance nejsou tiše děleny0.

## D151, 49: každý zlomek a přesný význam slabší meze

Pro X≥0, μ=EX>0 a ν=E X²<∞ máme ν≥μ²>0
podle46. Druhý momentový princip a komplement dávají

    P(X=0)=1−P(X>0)
      ≤1−μ²/ν=(ν−μ²)/ν
      ≤(ν−μ²)/μ²=ν/μ²−1.

Čitatel ν−μ² je nezáporný a jmenovatel ν≥μ²>0,
což přesně opravňuje jedinou srovnávací nerovnost
mezi oběma zlomky. Tím jsou doloženy všechny
rovnosti i nerovnosti tištěného řetězu.

Rozdíl slabšího a silnějšího horního odhadu je

    (ν−μ²)/μ²−(ν−μ²)/ν=(ν−μ²)²/(νμ²)≥0.

Je striktně kladný právě pro kladný rozptyl; pro
kladnou konstantu X jsou obě meze0. Označení
„strictly weaker“ tedy popisuje skutečně slabší
obecné tvrzení, nikoli falešnou přísnost v každém
jednotlivém konstantním zákoně. Například férové
X∈{0,1} dává silnější mez1/2 a slabší1.

Při μ=0 nezápornost nutí X=0 skoro jistě, a tedy
P(X=0)=1; vytištěný podíl není definován. Jako u
(22) se tato nulová distribuce vyřeší přímo a
není jí přisouzena hodnota0/0. Pokud by se dovolilo
ν=+∞ při konečném kladnémμ, poslední mez je
triviální+∞, ale původní knižní konvence očekávání
pracuje s konečnými momenty.

## Zdrojové a bibliografické vymezení

PDF+PS a všech6vrstev errat+3TeX: žádná použitelná
oprava45–49. Shodná čísla v odpovědích jiných sekcí
byla odlišena. Žádný nový nález, kandidát nebo běh.

[Primární katalog Numdam](https://www.numdam.org/item/JMPA_1874_2_19__157_0/)
potvrzuje autora, rok1874, sérii2, svazek19 a rozsah157–160
citovaného článku „Sur les valeurs limites des intégrales“.
Samotný obsah článku a historická věta, že již obsahoval
tento odhad, se neprohlašují za přečtené či ověřené.

Přesné Cantelliho stránky v ICM1928, svazek6,47–59 a66–67
zůstávají bibliografickou výjimkou. Odkaz na primární
ICM PDF byl nalezen, ale nástroj jej odmítl pro velikost
57,796,301bytů; celý svazek se kvůli tomuto údaji
nestahoval. Katalogové a druhotné odlišnosti stránkování
nejsou samy považovány za nový nález.

Celé45–49 jsou reviewed v uvedené momentové doméně
a s explicitně vyřešenými nulovými distribucemi.
File36 zůstává partial pro50–57; file397 pouze pro50(a),
jehož odpověď pokračuje na další straně. Starší P050
a jeho všechny výpočty zůstávají beze změny.
