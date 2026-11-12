# Přímé vkládání: celý invariant, MIX a úlohy1–5

Zdroj80–82/file91–93, zadání102/file113, odpovědi618–619
a vkládací část odpovědi33 na625/file636. Původní sazba
zobrazena. Pět vrstev errat pokrývá
`sources/insertion-errata-review.json`; opravené znění
směrodatné odchylky B na82 přebíráme, nevytváří nález.
Žádný výpočetní běh. Binární/dvousměrné vkládání
začínající na82 má následný samostatný blok.

## P0685: celý AlgorithmS a jeho invariant s dírou

Na začátku iterace j je prefix1,…,j−1 stabilně
seřazenou permutací původního prefixu. Uložení R_j
do pomocného R vytvoří logickou díru v j; její starou
fyzickou kopii nepočítáme mezi aktuální záznamy.
Před každým S3 je díra v i+1, pozice1,…,i si ponechávají
svůj seřazený prefix a i+2,…,j obsahují právě přesunutý
koncový úsek původního prefixu, ve stejném pořadí.
Všechny jeho klíče jsou přísně větší než K.

Pokud K≥K_i, lze díru vyplnit R: nalevo jsou klíče≤K,
napravo>K. Jinak se R_i přesune do díry a i klesne;
nová díra je zase i+1 a invariant zůstane. Při i=0
už vlevo nic není, takže porovnání s neexistujícím R_0
není třeba. S5 obnoví všechny záznamy, včetně satelitů,
a setřídí celý prefix1,…,j. Klesající i zajišťuje
konečnost vnitřní smyčky; rostoucí j setřídí celý vstup.
Prázdný a jednoprvkový abstraktní vstup mají prázdnou
vnější smyčku. Pomocná paměť je jeden záznam a indexy.
Všechny hrany Fig10 odpovídají právě těmto třem cestám.

## P0686: úlohy1–2, shodné klíče a skutečné zpomalení

S4 přesouvá jen přísně větší klíče. Nový záznam se
tedy vloží až za všechny starší záznamy stejného klíče:
stabilita platí indukcí, nejen pro jeden příklad.

Při náhradě S3 testem K>K_i je koncový přesouvaný úsek
naopak tvořen klíči≥K. Tentýž důkaz dává správné
neklesající pořadí, ale nový záznam se vloží před všechny
dosavadní stejné. Každá skupina stejných klíčů je proto
v přesně opačném původním pořadí.

Nechť E je počet párů shodných klíčů. Nová varianta
provede B′=B+E přesunů. Její počet dosažení i=0 je
A′≥A; nový takový případ potřebuje alespoň jeden
stejný předchozí klíč, takže 0≤A′−A≤E. Z přesného
času P0687 plyne přírůstek9E−3(A′−A)≥6E. Při
jakýchkoli opakovaných klíčích je tedy MIX skutečně
pomalejší; správnost se s cenou nezaměňuje.

## P0687: každá instrukce ProgramS a přesný čas

Předpoklady programu jsou N≥2, platné adresy
INPUT+1,…,INPUT+N a reprezentovatelné indexy bez
přetečení. Nezavádí se nepředepsaný sentinel.
ENT1 nastaví j−N=2−N; LDA pak čte INPUT+j.
ENT2 N−1,1 dává i=j−1. CMPA/JGE je přesně S3.
LDX/STX přenesou celý R_i do R_(i+1); DEC2/J2P
buď vrátí S3 s i>0, nebo bez přístupu na index0
pokračují do STA. STA zapíše nesený R. INC1/J1NP
provedou právě j=2,…,N; rI1 po posledním vzroste na1.

Označme B počet S4 a A počet těchto S4 končících i=0.
Každé vkládání má B_j neúspěšných porovnání a navíc
jedno úspěšné právě tehdy, neskončí-li na0. Proto jsou
četnosti CMPA/JGE B+N−1−A; všechny čtyři instrukce
přesunu mají četnost B; setup a závěr četnost N−1.
Při MIX cenách load/store/CMP=2, index/jump=1 vychází

    1 + 7(N−1) + 3(B+N−1−A) + 6B
      = 9B + 10N − 3A − 9.

Jsou tím prověřeny všechny vytištěné četnosti, nejen
výsledný polynom. Program pro N=0 nebo1 se nepoužívá
bez vstupního testu; kniha N≥2 výslovně uvádí.

## P0688: význam A,B a nezávislost prefixových pořadí

Pro původní vstup polož b_j=# {i<j:K_i>K_j}.
Vkládání j přesune právě tyto záznamy, takže B=∑b_j.
Přitom i=0 nastane právě pro b_j=j−1, tedy pro nové
striktní minimum prefixu, j≥2. To dokazuje oba knižní
výklady bez zaměnění původních a průběžných klíčů.

Pro náhodnou permutaci různých klíčů mají b_j nezávislá
rovnoměrná rozdělení na0,…,j−1. Přebíráme konkrétní
bijektivní rekonstrukci prefixových pořadí z úlohy
5.1.1–7 v `notes/inversions-proof-01-13.md` (P0114):
nový prefixový rank je j−b_j; starší ranky alespoň tak
velké se zvýší a nový se připojí. Každý přípustný vektor
má právě jednu permutaci, tedy pravděpodobnost1/N!.

## P0689: všechny momenty na82

I_j=[b_j=j−1] jsou nezávislé Bernoulliho proměnné1/j.
Proto pro A=∑_(j=2)^N I_j platí

    min A=0, max A=N−1,
    E A=H_N−1,
    Var A=∑(1/j−1/j²)=H_N−H_N^(2).

Pro B přebíráme uzavřené P0088–P0089 v
`notes/inversions-proof-main.md`:
E B=N(N−1)/4, Var B=N(N−1)(2N+5)/72,
minimum0, maximum N(N−1)/2. Směrodatná odchylka
je sqrt(N(N−1)(N+2.5))/6, s6 **mimo** odmocninu.
Dosazení do P0687 dává přesně

    E T = 2.25N²+7.75N−3H_N−6.

Nezávislost A a B se netvrdí: ve skutečnosti spolu
korelují, což je podstatné v úloze5.

## P0690: všechny skutečně vytištěné řádky Table1

Prvních šest vkládání má nové klíče87,512,61,908,170,897
a přesuny1,0,3,0,3,1. Výsledné prefixy jsou

    87 503;
    87 503 512;
    61 87 503 512;
    61 87 503 512 908;
    61 87 170 503 512 908;
    61 87 170 503 512 897 908.

Tak odpovídají i všechny značky místa vložení v tabulce.
Před posledním klíčem703 je prefix
61,87,154,170,275,426,503,509,512,612,653,677,765,897,908;
přesunou se poslední tři a703 přijde mezi677 a765,
jak uvádějí obě poslední řádky.

Celý dříve doložený vektor b_j je
0,1,0,3,0,3,1,4,2,5,8,4,3,2,2,3 (P0651).
Přebíráme jeho součet41 bez opakování běhu. Nová minima
jsou pouze87 a61, tedy A=2. Výpočet9·41+160−6−9=514
potvrzuje uvedený čas. Vynechané řádky tabulky se
nevydávají za další vytištěné příklady.

## P0691: úloha4, simultánní extrémy

Část času náležející b_j je f_j(b)=9b−3[b=j−1].
Její hodnoty jsou0,9,…,9j−18,9j−12: přísně rostou,
v posledním kroku o6. Všechny nezávisle přípustné
souřadnice tedy dosáhnou minima při b_j=0 a maxima
při b_j=j−1. To jsou vzestupná a sestupná permutace.

Minimum je10N−9; maximum je
9N(N−1)/2+10N−3(N−1)−9=4.5N²+2.5N−6.
Knižní rozklad6B+3(B−A) je také platný, neboť obě
části jsou v každé souřadnici neklesající. Nejde jen
o dosazení nezávislých mezí s neověřenou dosažitelností.

## P0692: úloha5, celá generující funkce

Z P0688 a přesného příspěvku f_j plyne pravděpodobnostní GF

    E z^T = z^(10N−9) ∏_(j=2)^N
            ( ∑_(b=0)^(j−2) z^(9b) + z^(9j−12) )/j.

Jde o konečný součin s nezápornými celočíselnými
exponenty; v z=1 má hodnotu1. Součin nevyžaduje
nepravdivou nezávislost A a B, pouze nezávislost b_j.
Při j=2 je faktor(1+z^6)/2, takže krajní případ
zápisu s tečkami je jednoznačný.

## P0693: úloha5, rozptyl se správnou kovariancí

Pro b rovnoměrné0,…,j−1 a I=[b=j−1] máme

    Var b=(j²−1)/12,
    Var I=(j−1)/j²,
    Cov(b,I)=(j−1)/(2j).

Poslední rovnost plyne z E(bI)=(j−1)/j a
E b·E I=(j−1)/(2j). Tedy

    Var(9b−3I)
      =81(j²−1)/12+9(j−1)/j²−27(j−1)/j
      =27j²/4−135/4+36/j−9/j².

Sečtením pro j=2,…,N a použitím ∑j²=N(N+1)(2N+1)/6
vyjde přesně

    Var T=2.25N³+3.375N²−32.625N+36H_N−9H_N^(2).

Požadovaná směrodatná odchylka je odmocnina tohoto
nezáporného součtu dílčích rozptylů. Pro N=2 jsou
časy11 a17, takže rozptyl9 souhlasí i přímo.

## P0694: úloha3, správnost všech osmi instrukcí

Pozor na význam MOVE: kopíruje jeden word ze zdroje
rI1+1 na adresu rI1 a pak zvýší rI1 o1. LDA drží
původní levý prvek, takže následné STA 0,1 uloží
tento prvek napravo. Dvojice se opravdu vymění,
nikoli duplikuje. JLE ponechá správně uspořádaný pár
včetně rovnosti. Po výměně následuje ENT1 N a sken
se spustí znovu od N−1; při nevýměně DEC1 jde doleva.

Každá výměna obrátí jednu sousední striktní inverzi,
a tím zmenší celkový počet inverzí přesně o1.
Výměn je proto přesně A=inv(vstup). Mezi nimi sken
trvá nejvýše N−1 porovnání. Konec nastane po celém
skenu bez výměny, kdy jsou všechny sousední páry
neklesající, tedy i celé pole. Satelity při slovních
klíčích nejsou samostatným předpokladem tohoto kódu.
Rovné prvky nepřekročí jeden druhý, postup je stabilní.
N=1 se po ENT1/DEC1/J1P ihned ukončí, bez čtení0.

Pro INPUT≠0 lze uvedené tvrzení o jedné další řádce
realizovat konkrétně: LDA/CMPA používají INPUT+0,1
a INPUT+1,1; mezi JLE a MOVE vložíme INC1 INPUT.
MOVE/STA už mají absolutní rI1 a poté ENT1 N zase
obnoví relativní index. To nevyžaduje další záznam.

## P0695: úloha3, přesný počet porovnání a jeho GF

Každý restart má sken z N−1. Výměna na sousedních
pozicích i,i+1 tedy spotřebuje N−i porovnání od
předchozího restartu; poslední sken spotřebuje N−1.

Posloupnost výměn je stejná jako při vkládání zprava:
jakmile se vyřeší suffix i+1,…,N, původní prvek v i
postupně překročí všechny menší prvky tohoto suffixu.
Po výměně je jediná možná nová inverze v suffixu
o místo vpravo; restart ji tedy najde před návratem
na menší index. Indukce na i dokazuje toto tvrzení
i přes zbytečné opakované skeny.

Je-li k=N−i+1 a c_i počet menších původních následníků,
jsou místa těchto výměn i,…,i+c_i−1. Jejich příspěvek je

    w_k(c_i)=(k−1)+(k−2)+…+(k−c_i)
             =c_i(2k−c_i−1)/2.

Suffixové pořadové kódy c_i jsou nezávislé rovnoměrné
na0,…,k−1, symetrickou rekonstrukcí z P0688. Proto

    B=N−1+∑_(k=2)^N w_k(c_(N−k+1)),
    E z^B=z^(N−1) ∏_(k=2)^N
       (1+z^(k−1)+z^(2k−3)+…+z^(k(k−1)/2))/k.

To jsou přesně všechny faktory vytištěné odpovědi.

## P0696: úloha3, každý náklad a kubický průměr

Přírůstek k−s se započte právě při c_i≥s,
s pravděpodobností(k−s)/k. Odtud

    E w_k=(1/k)∑_(t=1)^(k−1)t²=(k−1)(2k−1)/6,
    E B=N−1+∑E w_k=(N−1)(4N²+N+36)/36.

Četnosti jsou B pro LDA,CMPA,JLE; A pro MOVE,STA;
A+1 pro ENT1; B+1 pro DEC1,J1P. MOVE jednoho slova
stojí3u, takže T=7B+6A+3. Dosazení E A=N(N−1)/4
dává vedoucí člen(7/9)N³u, jak tvrdí odpověď.
Není ztotožněn počet inverzí A s porovnáními B.

## P0697: otevřená domněnka o minimální délce

Osm řádek je konkrétně kratších než dvanáct ProgramS,
takže zadání úlohy3 má konstruktivní odpověď. Navazující
domněnku, že žádný ještě kratší MIX program nemůže
třídit, tento důkaz neřeší. Kniha ji výslovně označuje
conjectured; zůstává partial výzkumnou položkou, nikoli
chybným tvrzením nebo novým nálezem. Výraz „shortest
decent“ na81 je neformální charakteristika kompromisu
délky/rychlosti; neexistuje zde definice decent ani
matematický důkaz optimálnosti mezi všemi programy.

## P0698: úloha33, úplný sentinelový ProgramS

Zde se ověřuje jen vkládací část úlohy33; část ProgramL
má vlastní pozdější blok. Sazba625 předpokládá sentinel
v INPUT+N+1 s největší možnou jednoslovní hodnotou.
Program zpracovává j=N−1,…,1 a udržuje setříděný suffix.
R_j se drží v A, rI1 je absolutní adresa aktuální díry.
CMPA 1,1 porovnává s pravým sousedem. Je-li menší než
A, MOVE jej posune doleva do díry a rI1 zvýší, takže
díra jde doprava. Jinak STA uzavře vkládání.

Sentinel zajišťuje zastavení, protože ani největší
platná hodnota není **větší** než on; nesmí se změnit
JG na JGE. MOVE se proto nikdy netýká sentinelu ani
nepřekročí pole. Nový, původně dřívější záznam se při
rovnosti vloží před rovný suffix, takže stabilita platí.
ENT2/DEC2/J2P zajistí všechny vnější iterace. Předpoklad
N≥2 původního ProgramS se zachovává.

## P0699: úloha33, přesný čas a rozsah zlepšení

Každá původní inverze se odstraní právě jedním MOVE,
tedy B je zase počet inverzí. CMPA/JG proběhnou
B+N−1 krát. Setup LDA/ENT1/JMP stojí4(N−1),
závěr STA/DEC2/J2P také4(N−1), iniciální ENT2 stojí1.
Proto čas je

    1+8(N−1)+3(B+N−1)+3B=6B+11N−10.

Rozdíl proti starému programu je3(B−A)−N+1. Zlepšení
se tedy netvrdí pro každý vstup: již seřazený vstup
je o N−1 pomalejší. Pro rovnoměrné různé klíče je
nový průměr1.5N²+9.5N−10 a vedoucí člen skutečně klesá.

## P0700: úloha33, konkrétní zdvojení vnitřní smyčky

Knižní „B/2 or so“ lze doložit bez měření. Po setupu
jednou porovnej A s prvním sousedem; pokud není větší,
skonči. Jinak lze použít následující logickou smyčku:

    porovnej A s druhým sousedem;
    pokud A≤druhý, proveď MOVE1 a jdi na konečné STA;
    proveď MOVE2 z následujících dvou míst do díry;
    porovnej A s novým prvním sousedem;
    je-li A větší, vrať se na začátek smyčky;
    jinak proveď konečné STA.

MOVE2 má cenu5u místo dvou MOVE1 za6u. Kopírování
zleva doprava při posunu doleva je bezpečné i s překryvem.
Druhého souseda lze číst: předtím bylo A>první, takže
první určitě není sentinel a druhý nepřesáhne N+1.

Každá dvojice přesunů stojí2+1+5+2+1=11u místo12u.
Úvodní porovnání je3u; liché dokončení lze realizovat
za7u (CMP/JLE/MOVE/JMP) místo původních6u pro poslední
přesun. Pro b přesunů jednoho vložení se tak ušetří
floor(b/2)−[b liché] jednotek, tedy celkově B/2+O(N).
To přesně podkládá uvedený dominantní přírůstek úspory,
bez tvrzení úspory pro každé malé b.

Domněnka P0697 je jedinou novou otevřenou položkou
tohoto bloku. Autorství a priority nejsou nově
bibliograficky reprodukovány. Žádný nový nález;
odpověď33 se neuzavírá mimo výslovně prověřenou část S.
