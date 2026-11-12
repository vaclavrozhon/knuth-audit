# Individuální audit: str.3–8, §7–8 až19

6. listopadu2026. Původní strany20–25,53–55 a532–535; nově celé přečteny
odpovědi515–517, na518 rozšířeno původní cílené čtení. Čtení a důkazové
pokrytí jsou oddělené. Žádný nový matematický program ani census.

## Langford: přesně uzavřená a otevřená tvrzení

Na p3 se přebírají pevní svědci(2),(3), vážený součet5268, balance a šířka7.
**Maximum5268, počet12016 maximálních řešení a lexikografické extrémy n24
zůstávají partial.** Pro(4) platí známá oprava15.5.2020, nikoli vlastní nález.
V předchozí poznámce bylo opraveno pouze naše shrnutí:12016 jsou maximální
řešení; známá změna historického benchmarku je3200→3500, ne opačně.

§7–8: n1,2,5,6 odpadají již dokázanou kongruencí. n3 má jediné řešení
a jeho křížení lze rozdělit na dvě strany. Pro n4 je jediné řešení41312432;
intervaly párů4=(1,6),3=(3,7),2=(5,8) se navzájem kříží. Tři vzájemně
se křížící oblouky nelze dát na dvě strany, takže planarita je nemožná.
Čtyři vytištěné svědky n8 ověřuje tabulka intervalů; v každé barvě jsou
intervaly disjunktní nebo vnořené, takže se nekříží:

|řetězec|intervaly párů1..8|první barva|
|---|---|---|
|1317538642572468|(1,3),(10,13),(2,6),(9,14),(5,11),(8,15),(4,12),(7,16)|{1,5,7}|
|1418634753268257|(1,3),(11,14),(6,10),(2,7),(9,15),(5,12),(8,16),(4,13)|{1,3,6,8}|
|4275248635713168|(12,14),(2,5),(9,13),(1,6),(4,10),(8,15),(3,11),(7,16)|{1,5,7}|
|5286235743681417|(13,15),(2,5),(6,10),(9,14),(1,7),(4,11),(8,16),(3,12)|{1,3,6,8}|

Každý interval má rozdíl k+1. Druhá barva je doplněk první.
Neexistence n7 a úplnost seznamu n8 se bez censu neuzavřely.

§7–9: ve třech vytištěných řetězcích jsou počáteční pozice trojic1..9
postupně (1,7,19,16,6,8,9,2,4), (1,4,17,8,14,9,11,6,2),
(1,7,19,16,8,4,9,6,2). Další dvě pozice jsou vždy p+k+1,p+2(k+1).
Tím jsou všichni tři svědci přímo ověřeni. Úplnost tří tříd a360 uzlů
vyhledávání zůstávají partial. Neomezený exact-cover model má135 možností;
132 lze získat vynecháním tří zrcadlových poloh páru největších rozestupů
(trojice9). Implementační normalizace knihy se tím nereprodukuje a rozdíl
není označen za chybu. Známá terminologická oprava2022 je rows→options.

## Hlavní text: latinské čtverce

Pevné čtverce(5),(7) a jejich ortogonalita se přebírají z uzavřeného sanity
výsledku. Přejmenování symbolů zachovává Latin i ortogonalitu; proto první
sloupec M lze normalizovat na0..9. Řád2 je nemožný: po přejmenování má
jediný latinský čtverec tvar součtové tabulky mod2 a §7–12 níže vylučuje
jeho transverzálu. Historická klasifikace řádu6 na17 rodin je externí vstup.

Pro liché n dává dvojice i+j,i−j ortogonální čtverce. Pro q=2^e≥4 dává
nad GF(q) dvojice i+j,ai+j s a∉{0,1} totéž. Existence konečného tělesa
je zde standardní externí algebraický vstup. Součin dvojic ortogonálních
čtverců řádůu,v dává dvojici řáduuv: symboly, indexy i jednoznačnost
dvojic se posuzují po obou složkách. To dokazuje existenční část pro
všechna n≢2 mod4; historické autorství konstrukcí se tím neověřuje.

Bose–Shrikhande–Parkerův výsledek pro všechna n>6 je přijat jako externí
vstup, ne jako zde rekonstruovaný důkaz. Primární článek obsahuje Theorem10
s tímto rozsahem: [CJM1960, indexovaný primární PDF](https://www.math.uci.edu/~brusso/%5B14%5DBosShrParCJM1960.pdf).
Přímé načtení PDF skončilo502; celý článek nebyl přečten. Metadata prvního
článku1959 odpovídají citaci: [PNAS45,734–737](https://pmc.ncbi.nlm.nih.gov/articles/PMC222625/).

Transverzála0859734216 v L(6) volí v postupných sloupcích řádky
0,1,2,3,5,6,9,8,4,7; jsou různé a uvedené hodnoty také. Každá hodnota k
v ortogonálním M označuje jednu transverzálu L; rozklad L na n disjunktních
transverzál naopak vyplní M a zaručí všechny tři podmínky. Tím je přesný
převod na pokrytí dokázán. Součet uvedených dílčích počtů je808, ale tyto
počty, jedinečnost M a prohledávací stromy jsou partial. Ruční backtracking
celého p6 se nereprodukoval. Aritmetika výkonových odhadů sedí:
75·2.5·10^18≈2·10^20; poměr k(1.7·10^8+5·10^6) přesahuje10^12;
1.3·10^11/(1.75·10^8)≈743 odpovídá slovnímu řádu tisíc. Samotné mems
nejsou nezávisle změřené.

Experimentální příklad p8:4³=64 plných kombinací, latinský plán má4²=16
a každá dvojice faktorů je vyvážena. Ortogonalita přidá čtvrtý faktor se
stejnou párovou vlastností. Není tím tvrzena ekvivalence informací o všech
interakcích. Historické údaje Ozanam/Euler/Clausen/Tarry, benchmarky,
ovce1788 a aplikace Skolem/Groth jsou bibliograficky přeskočené; známá
oprava Ozanam1725→1723 se zohledňuje.

## §7–10 až13

10: k hodnotám A,K,Q,J přiřaď12,8,4,0 a barvám4,3,2,1. Součty jsou
všechna čísla1..16 právě jednou. Každý řádek/sloupec/diagonála obsahuje
všechny hodnosti i barvy, takže součet je24+10=34. Vlastnost obrázku(5)
již byla ověřena. Historie magických čtverců se znovu nezkoumala.

11: hebrejská vrstva je H=(0123;1032;2301;3210), tedy H(i,j)=i XOR j.
Pro dvoubitové hodnoty definuj A=(0,1,3,2), B=(0,3,2,1); jde o invertibilní
lineární mapy a C=A XOR B=(0,2,1,3) je také invertibilní. Vytištěné vrstvy
jsou L=3 XOR A(i) XOR B(j), M=2 XOR B(i) XOR A(j).
Z (H,L) nebo(H,M) jednoznačně dostaneme i,j díky C. Z (L,M) nejprve
H=C^−1(L XOR M XOR1), pak i,j. Každá dvojice vrstev je tedy ortogonální;
Latin plyne z invertibility A,B,I. Tím je ověřena celá uvedená konstrukce.

12: pro liché n je M=i−j modn latinský a z (L,M) rekonstruujeme i,j
dělením2. Pro sudé n by transverzála L měla hodnoty permutace0..n−1,
avšak jejich součet modulo n by byl2Σi=0, zatímco Σi≡n/2≠0. Spor.

13: po převodu hodnot na0/1 mají čtvrtiny A,D po k jedničkách a B,C
po k nulách. Při k≤2 je dohromady≤8 výjimečných buněk; mezi10 disjunktními
transverzálami alespoň dvě žádnou neobsahují. Každá transverzála protne A,D
stejně často (vyplývá z počtu horních řádků a levých sloupců). Bez výjimek
proto obsahuje sudý počet nul, ale musí obsahovat právě5. Spor.
Obecně pro řád4m+2 a k≤m je4k<4m+2 a počet nul má být lichý2m+1;
tentýž argument dokazuje i dodatek v odpovědi. Známá bibliografická oprava
Mann2024 odstraňuje(2) před50; vlastní důkaz na citaci nezávisí.

## §7–14 až16: přesná omezení

14(a–e): čtení zadání/odpovědí není důkaz úplnosti censů2,0,6,0,12265168.
Tyto censy, lexikografická krajnost,5504 transverzál a jednotlivé šestice
vytištěných partnerských čtverců zatím partial. Program se nespouštěl.

15: samotné nalezení trojice řádu10 zůstává otevřenou výzkumnou úlohou.
Konkrétní čtverec L v odpovědi517 však byl nyní ručně ověřen. Řádky L a
jeho vytištěné transpozice jsou permutace0..9, diagonála je0..9. Pro i<j
se v dvojicích {Lij,Lji} postupně po řádcích objevují:

    23 36 48 15 46 57 89 79 12
    59 27 67 09 08 45 34 68
    58 18 37 49 14 06 07
    29 04 17 69 16 05
    78 39 03 02 56
    28 26 19 13
    01 35 24
    25 38
    47

To jsou všechna45 neuspořádaných dvojic různých číslic; diagonála dává
zbylých10 stejných dvojic. Tedy L je ortogonální ke své transpozici.
Pět uvedených permutací p je involutivních a jejich vybrané L-hodnoty jsou
0185369247,3267451089,4958236701,5479128630,7026495813; každá je permutace.
Transverzály jsou diagonálně symetrické a jediný opakovaný průsečík je(4,4)
ve druhé a páté, takže sjednocení má49 buněk. To neřeší úlohu15.

Externí omezení McKay–Meynert–Myrvold je výslovně potvrzeno abstraktem
[primárního univerzitního záznamu](https://researchportalplus.anu.edu.au/en/publications/small-latin-squares-quasigroups-and-loops/):
případná trojice má jen čtverce s triviální symetrií. Jejich rozsáhlý
výpočet se nepřebírá jako vlastní reprodukce. Existence trojic pro n>10
zůstává externím vstupem; citace Wang–Wilson/Todorov se rychle neověřovaly.

16: Ryserova otázka se neprohlašuje za vyřešenou. Primární práce
[Montgomery2023](https://arxiv.org/abs/2310.19779) a
[Tang–Zhao2026](https://arxiv.org/abs/2609.11006) uvádějí pro velké n
částečné transverzály délky n−1; to není požadovaná plná transverzála
lichého řádu. Ověřeny abstrakty, nikoli jejich dlouhé důkazy.

## §7–17 až19

17(a): možnost buňky(i,j) pokryje právě řádek i, sloupec j a hodnotu Lij.
Přesné pokrytí3n položek je tedy právě transverzála. 17(b): možnost(i,j,k)
pokryje čtyři podmínky r_ik,c_jk,x_ij,y_(Lij)k. Všechny dohromady říkají,
že M je latinský, každá buňka obsazená a každá dvojice(Lij,Mij) právě jednou.
Omezení j>0 neboi=k normalizuje první sloupec; počet možností je
n²(n−1)+n=n³−n²+n. Obrácené zobrazení je jednoznačné. Terminologické
erratum2017 mění columns/rows na vertices/hyperedges, argument zůstává.

18: pro hloubku m≥2 dvě indexové řádky OA určují jednoznačně každou
buňku(i,j). Každý další řádek je Latin, protože jeho dvojice s indexovými
řádky jsou unikátní; dvě další řádky dávají ortogonální čtverce. Obráceně
připojení indexů ke každé buňce dává OA. Sloupcová permutace nic nemění.
Příklad OA v odpovědi je přesně konstrukce úlohy11 výše. Dodatečné
kritérium L ortogonální ke konstantním řádkům/sloupcům platí s podmínkou
hodnot1..n doplněnou známým erratem23.5.2011.

19: přejmenuj symboly tak, aby první sloupec OA obsahoval jen0. Každý řádek
má mimo něj n−1 dalších nul, a dvě řádky se tam na0 neshodnou. Proto
m(n−1)≤n²−1, tedy m≤n+1 pro n>1. (Při m1 je mez triviální.)
Pro prvočíslo p vezmi sloupce(i,j)∈F_p² a řádky i a j+ai pro a∈F_p.
Libovolné dvě složky určují i,j, protože rozdíl různých a je invertibilní.
Vytištěný příklad p5 má po blocích:

    00000 11111 22222 33333 44444
    01234 01234 01234 01234 01234
    01234 12340 23401 34012 40123
    01234 23401 40123 12340 34012
    01234 34012 12340 40123 23401
    01234 40123 34012 23401 12340

Tytéž lineární vztahy fungují v GF(p^e); existence tělesa je externí vstup.
Souvislost maximální hloubky n+1 s projektivními rovinami je doplněna
v proof-004, bez rekonstrukce citované historie Moore/Hall.

Pozdější doplnění6.11: proof-005 přebírá uzavřené4B důkazy pro5268/12016,
planární n7/n8 a část tabulkyLn; příslušné zdejší partial závěry jsou tím nahrazeny.

Doplnění X0051/X0052 po obnově: celý lokální greedy odstavec p6 je nyní
v proof-019 doložen, bez benchmarků a censusů. Proof-020 ověřuje všech
pět zadaných Latin a všech šest vytištěných mate úlohy 14. Starší partial
u těchto konkrétních svědků je tím nahrazeno; všechny horní počty,
absence mate a extremality zůstávají partial.
