# §5.2.1: seznamové vkládání95–97,32–33 a seznamová část36

2026-11-07. P0884–0894. Originály96/file107,97/file108,624/file635,
625/file636 a626/file637 zobrazeny. Známé doplnění j v R_j (2015)
a typografické ukončení vět (1998) zohledněny. Nový C0025confirmed/low:
čas358u v odpovědi36 má být433u. Programy jsou správné.
Průběh a náklady se dokazují ručně; žádné simulace ani enumerace.

## Datová struktura a rozsah srovnání — P0884

Ve straight insertion jsou dvě různé práce: najít pozici a fyzicky
vložit záznam. U sekvenčního pole první stojí počet prohlédnutých
prvků a druhá posune stejný prefix/suffix; pro rovnoměrnou relativní
hodnost v seznamu délky n je průměrný počet přesunů n/2. Jde o průměr,
nikoli tvrzení o každém vstupu. V jednosměrném seznamu najdeme pozici
stejným jednosměrným skenem a samotné vložení změní právě dva linky.
Zpětný link není potřeba, protože si držíme předchůdce q.

Výrok o vhodnosti struktury je tím doložen pro tyto dvě operace;
neznamená globální optimalitu mezi všemi třídicími metodami, cache
modely nebo reprezentacemi. Rozdělení místa pro klíč/link do jednoho
MIX slova je explicitní předpoklad ProgramL. Záznamy se zatím fyzicky
nepřerovnávají.

## Celý invariant AlgorithmL — P0885–P0886

Pro N≥1 tvoří před vložením j cesta od L₀ přesně záznamy j+1,…,N
v rostoucím lexikografickém pořadí (K_i,i), každý právě jednou,
a končí0. L1 ji inicializuje singletonem N s L_N=0. Formálně lze
připojit umělý uzel0 s L₀ jako hlavičkou a dostat kruh, ale sken
nikdy neporovnává jeho neurčený klíč:0 je testovaný terminátor.

L2 nastaví p=L₀,q=0,K=K_j. Po celou dobu skenu je p=L_q,
za q leží neprohlédnutý suffix a všechny prošlé skutečné klíče jsou
přísně menší než K. L3 při K≤K_p zastaví před první takovou hodnotou.
Jinak L4 posune q na p a p na jeho následníka. Počet zbývajících uzlů
klesne; test p>0 chrání další čtení K_p. Pokud p=0, všechny klíče
byly menší a nové místo je konec seznamu.

L5 mění jedinou hranu q→p na q→j→p. j dosud v seznamu neležel;
nemůže vzniknout cyklus ani zmizet jiný uzel. Přísně menší prefix
zůstává před j, zbytek s klíčem≥K za ním. Při rovnosti má j menší
původní index než všechny staré uzly, takže nové pořadí je stabilní.
To obnovuje celý invariant a indukcí dává přesně všechny tři vztahy(13).

Krajní polohy q=0,p=0 i jeden starý uzel jsou zahrnuty. Pro N=1 je
výsledek L₀=1,L₁=0 bez vložení. Program není vydáván za variantu pro
N=0: inicializuje konkrétní poslední záznam R_N a předpokládá neprázdný
soubor. Prázdný seznam lze samostatně vrátit s L₀=0.

## Každá instrukce původního ProgramL — P0887

KEY=(0:3),LINK=(4:5) jsou disjunktní pole. Inicializace03–06 nastaví
rI1=N,L₀=N,L_N=0 a skočí na17, takže první zpracované j je N−1.
07 načte hlavu do p=rI2,08 q=rI3=0,09 celý záznam j do A; porovnání10
používá jen KEY, takže starý obsah LINK v A nevadí. JLE11 realizuje
K≤K_p.12 kopíruje p do q,13 načte L_q do p a14 se vrací jen pro p>0.
15–16 zapíší oba nové linky,17–18 sníží j a vrátí se právě pro j>0.
Zápisy LINK nikdy nemění KEY ani ostatní data.

Neplatná adresa p=0 se jako klíč nečte. Před prvním porovnáním každého
vložení je seznam neprázdný; při následném posunu z konce jej14 zachytí.
Všechny linky zůstávají v0,…,N a jejich pole musí tento rozsah pojmout.

## Přesné četnosti a cena — P0888

Označme b_j=#{k>j:K_k<K_j}. Každé takové menší číslo se při vložení j
projde právě jednou, takže B=Σ_j b_j je počet původních inversí.
L4 proběhne B krát. Po skenu se provede ještě jedno neúspěšné
porovnání, kromě případů, kdy j je přísné maximum svého suffixu.
Je-li A počet takových j<N, je A+1 počet pravostranných maxim.
Tedy10–11 mají B+N−1−A průchodů,12–14 B,07–09 a15–16 N−1,
17–18 N. Tyto identity platí i pro rovné klíče při přísné definici maxima.

V MIX jednotkách:03–06 stojí6;07–09 mají cenu5;10–11 cenu3;
12–14 cenu4;15–16 cenu4;17–18 cenu2. Proto

    6+5(N−1)+3(B+N−1−A)+4B+4(N−1)+2N
      =7B+14N−3A−6.

Pro N=1 je cena8, což souhlasí se skutečnými inicializačními a koncovými
instrukcemi. Rovnoměrná permutace má E B=N(N−1)/4 a E A=H_N−1;
tyto dříve doložené statistiky se nepřepočítávají. A v ProgramS může
na témže konkrétním vstupu znamenat jiné záznamové extrémy; shodné jsou
rozdělení a dominantní člen, nikoli nutně hodnota na dané permutaci.

## Celá Table8 a32 — P0889

Po inicializaci je řetěz16→0. Vložení15 (765>703) dává
16→15→0, tedy L₀=16,L₁₆=15,L₁₅=0. Vložení14 (677<703) dává
14→16→15→0. To jsou přesně všechny vytištěné řádky Table8.

Úplné vzestupné pořadí indexů je

    4,2,11,6,8,10,1,12,3,13,9,14,16,15,7,5,

s klíči061,087,154,170,275,426,503,509,512,612,653,677,703,765,897,908.
Každý index1,…,16 je přítomen právě jednou a sousední klíče rostou.
Vztah(13) proto dává pro L₀,…,L₁₆

    4,12,11,13,2,0,8,5,10,14,1,6,3,9,16,7,15,

což je přesně odpověď32. Není třeba znovu simulovat16 vložení.

## Procenta a konkrétní cena fyzického přerovnání — P0890

Dominantní průměrné členy původníhoS,L a zlepšenéhoL jsou9E B,7E B,5E B.
Rozdíl2/9≈22.22% původního S platí při každém z obou přechodů ve smyslu
procent původního času. Druhý přechod sám vůči L ušetří2/7≈28.57%;
textové „another22 percent“ je tedy srovnání s původní základnou.
Lineární členy ani dodatečné lineární přerovnání tuto asymptotiku nemění;
nejde o přesné procento pro malé či již seřazené vstupy.

Odkaz5.2-12 má již úplný MacLarenův invariant a A_M=N−C v
`internal-proof-12-list-rearrangement.md`. Pro jednoslovní záznam zde
navíc konkrétní MIX realizace dokládá údaj „about20N“; I1 je absolutní
adresa pozice k, I2 relativní P, I3 pomocný rozdíl nebo Q:

    LD2 INPUT(LINK)       ;2, jednou
    ENT1 INPUT+1          ;1, jednou
    JMP TEST              ;1, jednou
 ADV LD2 INPUT,2(LINK)    ;2, N−C krát
 TEST ENT3 INPUT,2        ;1, 2N−C krát
    DEC3 0,1              ;1, 2N−C krát
    J3N ADV               ;1, 2N−C krát
    LD3 INPUT,2(LINK)     ;2, N krát: Q=LINK(P)
    LDA 0,1               ;2, N krát: původní R_k
    MOVE INPUT,2(1)       ;3, N krát: R_k←R_P, I1 se zvětší
    STA INPUT,2           ;2, N krát: R_P←původní R_k
    ST2 -1,1(LINK)        ;2, N krát: LINK(k)=P
    ENT2 0,3              ;1, N krát: P=Q
    J2P TEST              ;1, N krát

Test skutečně porovnává INPUT+P s INPUT+k. Q se uloží před výměnou;
MOVE funguje i při P=k a zvýší k právě jednou. Uložené A pak přepíše
původní pozici P; poslední ST2 vytváří přesně MacLarenovo přesměrování.
P=0 nastane až po posledním uzlu podle převzatého invariantu.
Cena je4+2(N−C)+3(2N−C)+13N=21N−5C+4, tedy přibližně20N
v uvedeném jednoslovním modelu (a E C=H_N pro rovnoměrnou permutaci).
Nejde o tvrzení přesné nebo univerzální konstanty20 pro dlouhé záznamy.

Závěrečné shrnutí na97 o S a binárním vkládání přebírá přesné důkazy
P0687–0692 a P0701–0703: vedoucí počet přesunů N²/4, resp. porovnání
N log₂N pro binární variantu. Podrobné pokračování shrnutí na98 je další blok.

##33: sentinel a střídání registrů — P0891

K₀ v horním KEY poli je největší reprezentovatelná hodnota. Zápisy L₀
jej nenarušují. K_j≤K₀ vždy, včetně rovnosti, takže přísné JG zastaví
na p=0 a nemusíme testovat nulový link. Průchod nikdy nemine sentinel.
Stabilita zůstává: nový, původně dřívější prvek jde před rovný suffix.

Druhá optimalizace střídá význam I2 a I3. Při vstupu na13/4H je q=I3
(na začátku0), LD2 načte p=L_q. Úspěšné JG15 přejde na07/8H, kde
q je nyní I2 a LD3 načte jeho následníka p. Úspěšné JG09 se vrací na13.
Tím se q←p realizuje změnou rolí, bez kopírovací instrukce. Každý
neúspěch jde na správné dvě ukládací instrukce10–11 nebo16–17.

18–21 zmenší j, nastaví q=0, načte další K a vrátí se na13 jen při j>0.
Poslední LDA při j=0 je čtení povoleného umělého záznamu, nikoli mimo
pole. Inicializace03–06 je původní včetně skoku na nový6H na18.
Celý program tedy uskutečňuje původní invariant s testovaným sentinelem.

##33: všechny četnosti a cena — P0892

B'+B''=B+N−1, protože každý prohlédnutý menší klíč dává jeden úspěch
a každé vložení má jedno závěrečné porovnání, nyní i když jde za maximum.
N'+N''=N−1 jsou oba typy ukončení. Výchozí porovnání je vždy v druhé
bance13–15; první banka07–09 ukončuje právě po lichém počtu b_j úspěchů.
Tedy N'=#{j<N:b_j je liché}.

Obě porovnávací banky LD/CMP/JG stojí5u, oba páry zápisů4u, jen první
ukončení má JMP navíc1u. Každá z N návštěv18–21 stojí5u. S iniciálními6u
proto přesně

    T=6+5(B+N−1)+4(N−1)+N'+5N
     =5B+14N+N'−3.                                        (A)

To nezapomíná závěrečná porovnání ani poslední čtení INPUT. Pro singleton
vychází11u a odpovídá skutečnému inicializačnímu/koncovému průchodu.
Část33 o ProgramS, ceně6B+11N−10 a zdvojení se přebírá z P0698–0700;
jejich důkaz má přesně stejnou sentinelovou a stabilní konvenci.

##33: všechny statistiky N' — P0893

Min0 dosáhne rostoucí permutace. MaxN−1 dosáhne2,3,…,N,1,
kde každé b_j pro j<N je1. Pro rovnoměrnou permutaci je b_j rovnoměrné
na0,…,N−j (volba relativní hodnosti daného prvku v jeho suffixu).
Pro m=N−j+1 je pravděpodobnost lichého b_j rovna floor(m/2)/m.
Linearita tedy dává

    E N'=Σ_(m=2)^N floor(m/2)/m
         =(N−1)/2−(1/2)Σ_(3≤m≤N, m liché)1/m
         =N/2+(1/4)H_floor(N/2)−(1/2)H_N.

Tím je doložena celá vytištěná trojice(min,ave,max), včetně N=1.
Nezávislost jednotlivých b_j pro tento první moment vůbec není potřeba.

##36: přesná data pro L a nový číselný nález — P0894

Pro Table8 jsou b₁,…,b₁₆ ručně

    6,1,6,0,11,1,9,1,4,1,0,0,0,0,1,0.

Jde o počty menších hodnot napravo; například503 má087,061,170,275,426,154,
908 má všech11 pozdějších hodnot a897 všech9 pozdějších hodnot.
Součet je B=41. Pravostranná maxima jsou703,765,897,908, tedy A=3.
Liché b_j leží na j=2,5,6,7,8,10,15, tedy N'=7. N=16.
Vynásobení všech klíčů1000 (zadání36) zachová všechna porovnání,
KEY o třech bytech základ100 je bezpečně obsáhne, LINK pojme0,…,16.

Původní cena7·41+14·16−3·3−6=496u je správná.
Vylepšená cena z(A) je5·41+14·16+7−3=**433u**, nikoli358u.
Dokonce bez znalosti N' musí být≥5·41+14·16−3=426u>358u.
Rozdíl75u se přesně rovná5(N−1): těm15 závěrečným porovnávacím bankám,
které jsou v kódu nezbytné. To vysvětluje možnou aritmetickou příčinu,
nikoli prokázanou autorovu historii chyby.

C0025 jeconfirmed/low po kontrole originálu a všech vrstev;
`notes/V3-C0025-list-insertion-example-time.md` má stručný důkaz.
Odpověď36 pro ProgramM a spojení seznamů se zde ještě neuzavírá.
