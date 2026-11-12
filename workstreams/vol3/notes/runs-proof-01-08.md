# Runs: úlohy1–8, zadání44–45, odpovědi602–603

Sazba: `images/runs-file-055.png`, `runs-file-056.png`,
`multisets-file-613.png`, `multisets-file-614.png`. Pět vrstev errat
již obsahuje `sources/runs-errata-review.json`. Bez nového nálezu a běhu.

1. Eulerův vzorec je převzat z V3-P0254, neopakuje se. Tištěná odpověď
   navíc správně obrací konečnou konvoluci: po s=r−j zbývá pro s<k
   součet `(−1)^j choose(n+1,j) choose(n+k−s−j,n)`. Doplněné členy
   jsou nulové a úplný součet je(n+1). diference polynomu stupně n,
   tedy0. Pro s=k zbývá jediný člen1, takže výsledek je k^n.
   Kontext rovnice11 má n≥1; nultý Eulerův řádek je definován zvlášť.
2. (a) Surjektivních slov délky n nad1..q je q!S(n,q): třídy shodných
   hodnot tvoří rozklad na q neprázdných bloků, jejichž hodnoty lze
   přiřadit q! způsoby. Pro pevné indexové pořadí s r běhy je dovoleno
   n−r nepřísných hran. Musíme zvolit n−q z nich jako rovnosti; zbylé
   hrany jsou přísné a hodnoty pak určeny1..q. Po symetrii k=n−r vzniká
   `Σ_k A(n,k) choose(k,n−q)=q!S(n,q)` pro celočíselné q≥0.
   Prázdné slovo a q=0 se vyřídí přímo konvencí S(0,0)=1.
   (b) Pascalova identita pro choose(k+1,m) sčítá výsledky pro
   q=n−m a q=n−m+1. Dostaneme
   `(n−m)![S(n,n−m)+(n−m+1)S(n,n−m+1)]
   =(n−m)!S(n+1,n−m+1)`.
   Opravené indexy v poslední větě odpovědi2 jsou známé erratum2006.
3. Z již dokázané20 je EGF podepsaného součtu přesně
   `E(x)=2/(1+e^(−2x))=1+tanh x`.
   V původní konvenci `t/(e^t−1)=Σ B_j^- t^j/j!` platí
   `E(x)=[B^-(−4x)−B^-(−2x)]/x`, takže
   `E_n=(−1)^(n+1) B_(n+1)^- 2^(n+1)(2^(n+1)−1)/(n+1)`.
   Tím je původní odpověď602 ověřena včetně n0. Pro liché n převod
   `tanh x=tan(ix)/i` dává `(−1)^((n−1)/2)T_n`; kladné sudé n dávají0.
   Z18 zároveň
   `Σ_k S(n,k)k!/(−2)^k=E_n/(−2)^n
   =2B_(n+1)^-(1−2^(n+1))/(n+1)`.

   Erratum22.3.2021 mění použité Bernoulliho značení spolu s výslovnou
   změnou definice v `errata/text/all1-pre.txt`, strana112,
   21.3.2021: `B^+(t)=t/(1−e^(−t))=B^-(−t)`, tedy B_1^+=+1/2.
   Původní `text/vol1.txt`,§1.2.11.2,112 má B_1^−=−1/2.
   Dosazení B_j^+=(−1)^jB_j^− dává přesně obě opravené odpovědi.
   Jde o známou změnu konvence, nikoli nový nález ani nejasný kandidát.
4. V prvním tvaru18 vybereme koeficient z^m v g_n(z)/z:
   `A(n,m)=Σ_k S(n,k)k!choose(n−k,m)(−1)^(n−k−m)`.
   Po vynásobení(−1)^(n+m) dostaneme požadovaný součet.
   Pro n0 se totéž ověří jediným nenulovým členem přímo.
5. Pro0≤k<p se v Eulerově vzorci modulo p zachovají jen j0,1,
   protože choose(p+1,j) je pro2≤j≤p−1 dělitelné p.
   Malá Fermatova věta pak dává `(k+1)^p−k^p≡1`.
   Mimo nosič0≤k<p jsou Eulerova čísla0; odpověď tento nosič výslovně uvádí.
6. Původní pořadí má vnější součet n!, ale v opačném pořadí je
   každý vnitřní binomický součet(1−1)^(n+1)=0. Absolutní součet
   diverguje již na diagonále k=j, kde má člen velikost(j+1)^n;
   výměna nekonečných součtů proto není přípustná.
   V pomocném příkladu a_jk=(k−j)[|j−k|=1] má řádek0 součet1,
   ostatní řádky0; sloupec0 má−1, ostatní0. Obě tištěné iterace sedí.
7. Vlastní důkaz asymptotické normality: reprezentujme permutaci pomocí
   nezávislých U_i∼Uniform(0,1) a sestupy D_i=[U_i>U_(i+1)].
   Jde o1-závislé indikátory se známými momenty z V3-P0259.
   Zvolme b=floor(n^(1/4)); skupiny b sousedních D_i oddělme vždy
   jedním vynechaným D_i. Skupinové centrované součty jsou nezávislé,
   každý má absolutní hodnotu≤b a rozptyl(b+2)/12.
   Jejich celkový rozptyl σ²∼n/12. Vynechané členy a koncový zbytek
   mají rozptyl O(n/b+b)=o(n), neboť závislost má dosah1.

   Pro centrovaný blok B rozvoj charakteristické funkce dává
   `E exp(itB/σ)=1−t²Var(B)/(2σ²)+O(|t|³E|B|³/σ³)`.
   Součet chyb je nejvýše O(b/σ)=o(1), protože E|B|³≤b E B².
   Největší jednotlivý kvadratický člen také jde k0, takže logaritmus
   součinu jde k−t²/2. Spojitostní věta pro charakteristické funkce
   dává normální limit; zanedbatelný zbytek jej nemění.
   Tedy `(R_n−(n+1)/2)/sqrt((n+1)/12)` konverguje k N(0,1).
   Bibliografická citace v odpovědi není nutným předpokladem tohoto důkazu.
8. Pro kladné l_i a N=Σl_i musí být každý ze zadaných souvislých bloků
   rostoucí a na prvních k−1 hranicích musí být pokles. Inkluze–exkluze
   nad zakázanými vzestupy na hranicích slučuje sousední bloky;
   každá sloučená skupina přispívá převráceným faktoriálem součtu délek
   a každá sloučená hranice znaménkem−. U disjunktních bloků jsou
   relativní pořadí nezávislá. Tím sedí i konkrétní součin v odpovědi.

   Rozvoj tištěného horního Hessenbergova determinantu podle prvního
   řádku má přesně rekurenci
   `D(l_1,..,l_k)=Σ_{j=1}^k(−1)^(j−1)
   D(l_(j+1),..,l_k)/(l_1+...+l_j)!`, s D(prázdné)=1.
   Stejná rekurence třídí členy inkluze–exkluze podle první sloučené
   skupiny. Poslední blok nemusí končit v N, proto je poslední délka≥l_k.

   Také tvrzení o kvadratickém algoritmu má přímý argument nezávislý
   na citaci: c_j(r) počítá permutace prvních j pozic se správným
   vzorem nerovností a poslední hodnotou relativního pořadí r.
   Při vzestupu je `c_j(r)=Σ_{s<r}c_(j−1)(s)`, při poklesu
   `c_j(r)=Σ_{s≥r}c_(j−1)(s)`. Prefixové či suffixové součty počítají
   řádek v O(j) aritmetických operacích, tedy celek v O(N²).
   Začátek c_1(1)=1 a konečný součet přes r dávají přesný počet.
   Historické autorství a obsah citovaného článku zůstávají přeskočeny.
