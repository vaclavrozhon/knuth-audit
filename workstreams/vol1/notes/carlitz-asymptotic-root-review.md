# §1.2.11.3–11: Carlitz a Concrete Mathematics

**Celá úloha 11 je checked, se zachováním potvrzeného V1-C0018.**
Pramenná kontrola doplňuje již přijatý samostatný důkaz všech reálných
větví v `asymptotic-parameters.md`. Neopakuje jeho výpočty.

Koordinátor ověřil 27 členů zmrazeného
`parallel/asymptotic-primary-followup/results/carlitz-ex11-manifest.json`
a všech 15 přímých závislostí. Devět společných vstupů knihy a errat
bylo ověřeno v témže převzetí X0756. SHA-256 manifestu je
`8bd4a00716ef81796ee2eb22fd9919911472660e596cef3474607c916d1b8a52`.

Agent i koordinátor přímo přečetli celý Carlitzův článek 248–252,
na s. 252 pouze jeho bibliografii před dalším článkem. Jde o
*The Coefficients in an Asymptotic Expansion*, Proc. AMS 16 (1965),
248–252, zachovaný veřejný archivní snímek původního AMS PDF;
SHA-256 PDF je
`536e173d72f5da886b4ad6cb1d0859a93d8c27cd1a80cd84a84655c1fca81b6e`.
Záhlaví dokládají duben 1965. Koordinátor také přímo přečetl
Concrete Mathematics, 2. vydání, §6.2, s. 270–271 (PDF 283–284),
a TAOCP 122/505–506. Identita vydání CMath byla doložena v dřívějším
převzetí; soubor byl nyní hashově ověřen a neměnil se.

Pro celé n>=1 a komplexní z je Carlitzova S_n určena oddělením
prvních n+1 členů exponenciální řady. Proto přesně
`S_n(z)=R_z(n)-1`, kde knižní
`R_z(n)=sum_(k>=0) n! n^k z^k/(n+k)!`.
V nule se zdánlivá singularita odstraňuje analytickým prodloužením.
Jeho polynom Q_m nazveme P_m, aby se nepletl s knižní funkcí Q_z.
Rovnice (13)–(14) na s. 251 dávají

```text
P_(m+1)(z) = (2m+1)zP_m(z) + z(1-z)P'_m(z),
P_m(z) = sum_(h=1)^m a_(m,h) z^h,
a_(m,h) = h a_(m-1,h) + (2m-h)a_(m-1,h-1).
```

Eulerova čísla druhého řádu A(m,j) definuje CMath (6.41)
rekurencí `A(m,j)=(j+1)A(m-1,j)+(2m-j-1)A(m-1,j-1)`.
Počáteční hodnoty jsou `A(1,0)=a_(1,1)=1`; mimo trojúhelník
0<=j<m, respektive 1<=h<=m, jsou hodnoty nulové. Posun h=j+1
tedy indukcí pro každý řád dokazuje `a_(m,j+1)=A(m,j)`.
Odtud P_m přesně odpovídá knižnímu r_m. Již přijatý reciproký
převod dává `q_m(z)=z^(2m)r_m(1/z)`, tedy správné obrácené pořadí
exponentů v odpovědi. Poslední rovnost určuje polynom i v nule.

Carlitzova (1) také souhlasí se znaménkem koeficientu
`(-1)^m r_m(z)/(1-z)^(2m+1)`. Jeho převzatou větu od Buckholtze
o oblasti a rovnoměrnosti rozvoje zde nerozšiřujeme na další
komplexní oblasti; konkrétní knižní citace se týká koeficientů.
Všechny potřebné reálné zbytky pokrývá samostatný důkaz.

Čtyři úplné vrstvy errat jsou prohledány ve společném a doplňkovém
tematickém záznamu agenta. Koordinátor přímo četl obě opravy
z 10.8.2008 na all1-prepre PDF 36: nezáporné indexy dvojitého součtu
a závorky ve jmenovateli. Citace ani indexování polynomů nemění.
Chybějící exponenciální člen pro některé záporné parametry zůstává
samostatným potvrzeným V1-C0018. Nový nález nevznikl.
