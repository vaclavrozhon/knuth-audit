# V2-C0167: vynechané x=M v odpovědi 4.5.4-32

**Stav: confirmed.** Odpověď 4.5.4-32, strana 664,
první dva řádky. [Detail původní sazby](../images/vol2-p664-answer32-detail.png)
potvrzuje dolní celou část M=floor(cuberoot(N)) a nedoplněnou
větev x>=M. Zadání na [415](../images/vol2-p415.png) požaduje
odstranit problém zpráv menších než třetí odmocnina N.

Pro RSA modul N=pq nemůže být N krychle. Tedy M^3<N,
a právě hodnota x=M zůstává nechráněná. Konkrétně N=55=5*11,
M=3 a x=3 splňují všechny podmínky: obě prvočísla jsou 2 modulo 3
a 0<=3<M^3-M^2=18. Kniha odešle 3^3 mod 55=27.
Obyčejná celočíselná třetí odmocnina okamžitě vrátí zprávu.

Známé erratum z 18. února 2004 mění pouze horní mez náhodného
y z y<=M^2 na y<M^2. Je nutné kvůli jinému selhání, například
N=517,M=8,x=5,y=64 dá reprezentant 517 a dekóduje nulu.
Ani po této známé opravě se x=M nezačne náhodně doplňovat.

Vlastní jednotná oprava v [RSA §2](rsa-basic.md#2-úloha-32-malá-zpráva-a-opravené-náhodné-doplnění)
používá B=ceil(cuberoot(N)), J=floor(N/B), H=(J-B)B.
Pro 0<=x<H nechá x>=B beze změny; každé x<B doplní na
z=x+yB s rovnoměrným J-B<=y<J. Po modulárním odmocnění
použije z mod B právě pro z>=H. Je dokázána jednoznačnost,
z^3>=N i ztráta kapacity pouze O(N^(2/3)). Platí pro N>=28,
tedy zejména pro všechny zde uvažované liché RSA moduly.

Dne 3. listopadu 2026 prohledány celé vrstvy all2-prepre,
all2-pre, all2, err2 a zdrojový TeX err2 podle 32, 664,
cube, RSA a hraničních výrazů. Známá oprava y byla přečtena
i vizuálně; oprava prahu x=M nalezena nebyla.

[Přesná kontrola](../results/rsa-basic.json) našla tuto jednu
hraniční hodnotu u všech 66 zkoušených modulů. Doporučená
náhodná oprava prošla na 113277 zprávách a 122377 reprezentantech.
Obecný důkaz je nezávislý na tomto konečném rozsahu.
[Metadata](../sources/rsa-basic.json) uvádějí zdroje a hashe.
Pozdější fyzický dotisk a prvenství nebyly ověřeny.
[Návrh hlášení](../reports/C0167-rsa-padding-boundary-draft.txt) nebyl odeslán.
