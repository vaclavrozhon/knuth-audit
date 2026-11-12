# §1.3.2′, úlohy 30–31 — celé harmonické jádro, tisk a asymptotika

Zadání file56–57/p48–49, odpovědi file117–119/p109–111. Originální
file118 byla znovu zobrazena v `images/recovery-harmonic-118.png`;
file56/117 jsou v již zobrazených recovery-magic-josephus-056 a
recovery-fibonacci-117. Tato poznámka doplňuje úplný rozsah dřívějšího
argumentu; žádný starý součet, census ani MMIX program se znovu nespouštěl.

## 1. Definice, všechny poloviny a oba příklady zadání

Položme M=10^n, n≥1, a R(j)=M·r_n(1/j), j kladné celé. Přesná polovina
M/j=q+1/2 znamená j(2q+1)=2M. Lichý dělitel 2q+1 musí být 5^h,
0≤h≤n; naopak každé takové h dává právě jednu celočíselnou pozici
j=2M/5^h. Číslo q=(5^h−1)/2 je sudé, protože 5^h≡1 mod4.
Všech n+1 půlek se tedy zaokrouhluje dolů. Pro ostatní členy rozhoduje
vzdálenost k celému, takže pro tento obor přesně platí

    R(j)=ceil(M/j−1/2)=floor((2M+j−1)/(2j)).             (1)

To není obecná formule pro zaokrouhlování libovolného x k sudému:
například při lichém dolním sousedovi by polovina šla nahoru. Právě tuto
výhradu doplňuje známé erratum p48 z 15.3.2024 (`all1f1`, odstavec p48).
Je aplikováno, nejde o nový nález.

R(j)>0 právě pro 1≤j<2M; všechny další členy jsou nula. Divergence
nezaokrouhlené řady byla přesně dokázána bloky délky 2^k v
`workstreams/vol1/notes/harmonic-finite.md`, oddíl „Definice a růst“.
Zde se sčítají samostatně zaokrouhlené členy; netvrdí se totožnost
s libovolným floating point pořadím průběžného sčítání.

Pro M=10 dává (1) postupně 10,5,3,2,2,2, pak třináct jedniček
pro j=7,…,19 a nuly od20. Součet37 znamená S1=3.7 a ověřuje celý
vytištěný rozpis. Pro každé **kladné** celé R platí

    R(j)=R  iff  2M/(2R+1)≤j<2M/(2R−1).               (2)

Proto je poslední index skupiny floor((2M−1)/(2R−1)). U R=0 se tato
kladná intervalová formule nepoužívá; jeho obor už určila (1).
Pro n5,R1 jsou krajní indexy ceil(200000/3)=66667 a199999,
tedy přesně133333 členů, včetně obou uvedených krajů zadání.

## 2. Algoritmus H a všechny větve tištěného MMIX programu

Před H2 platí: m je poslední započtený index a s=Σ(j=1…m)R(j).
Na začátku m1,s=M, tedy je započten právě první člen. H2 vybere
R(m+1). Je-li nula, monotonie z (1) zaručuje nulový celý ocas.
Je-li kladný, (2) dává mm≥m+1 jako poslední index jeho skupiny.
Přičtení (mm−m)R započte každý její člen jednou, nastaví m=mm
a obnoví invariant. Skupiny jsou souvislé, disjunktní a pokryjí
všechny kladné členy. m ostře roste a nepřesáhne2M−1, takže algoritmus
skončí; žádné spoléhání na numerický příklad zde není.

V MMIX je c=2M, nn=n−MaxN. Před 1H tato rovnost platí díky Main
a pak díky INCL nn,1 / MUL c,c,10. SET m,1 a SR s,c,1 inicializují
právě uvedený invariant. Skok do2H neprovede neplatnou první skupinu.
V2H jsou a=c+m,d=2m+2; signed DIV pro tyto kladné operandy vrací
floor((2M+m)/(2m+2))=R(m+1) podle (1). rR není zde potřebné.

PBNZ r,3B pustí pouze kladné r. Blok3H vytvoří a=2M−1,d=2r−1>0
a DIV mm,a,d vrátí právě poslední index (2). Blok4H vypočte kladný
počet mm−m, jeho součin s r a nový součet; SET m,mm obnoví invariant.
Po poslední skupině r1 máme m=2M−1. Další2H má a=4M−1,d=4M,
tedy r0, a odejde přímo k tisku. Nulový d ani dělení záporným2r−1
se nikdy neprovedou. Po tisku PBNP nn,1B zahrne právě n1…MaxN;
pro nn1 už program skončí.

Všechny pracovní GREG0 jsou samostatné měnitelné registry; nenulová
báze dec je zvlášť a kód od#100 se s daty od Data_Segment nepřekrývá.
Předpokládá se obvyklé spuštění MMIXAL/MMIX-SIM a úspěšný standardní
výstup. Registry a buffer nesmí asynchronně přepsat cizí handler.
Kód nemá obsluhu selhání Fputs; číselný výsledek na takovém zařízení
není slib úspěšně vytištěného souboru.

## 3. Celočíselné meze až do n=17

Zde MaxN smí být libovolné celé1…17, ne pouze původních10. Proto
M≤10^17 a2M<2^58. Dyadická mez H_(2^58)≤59 z citovaného konečného
důkazu dává H_(2M−1)<59. Součet absolutních zaokrouhlovacích chyb
je menší než1, takže 1≤S_n<60 a0<s=M S_n<60M≤6·10^18<2^63.
Každý mezisoučet i každý kladný skupinový příspěvek je nejvýše s.

V jádře platí 1≤m≤2M−1, a=c+m≤4M−1, d=2m+2≤4M,
mm≤2M−1 a při r>0 rovněž2r−1<2M. Všechna ADD/SUB/SL/MUL
tedy mají přesný signed64 výsledek, nikoli pouze správné spodní bity.
Konečné MUL c,c,10 po n17 ještě vytvoří2·10^18<2^63, ačkoli se tento
výsledek už nepoužije. nn leží mezi−16 a1; všechny jeho immediates
jsou přípustné. DIV má vždy kladný nenulový d a nevzniká výjimka.
Záruka n≤17 je tak prokázaná pro celý kód včetně poslední aktualizace.

## 4. Úplný formatter a nulový konec

V sazbě BYTE obsahuje **tři mezery a tečku**, takže dec=@+3 ukazuje
na tečku. OCR se čtyřmi mezerami není program. Nezapsaná paměť
standardního MMIX-SIM je nulová: `sources/mmix-sim-20250620.w`,
new_mem744–751, používá calloc pro celý datový uzel a mem_find
přiděluje stejné uzly také pro dosud neexistující adresy. Právě toto je
konkrétní počáteční předpoklad nulového bajtu za formátovaným řádkem;
pro libovolnou nenulovou holou RAM jej kód neposkytuje.

V5H se nastaví a=n+1,d=LF. První7H uloží newline na dec+n+1,
sníží a na n a začne dělit kladné s deseti. Každý6H vrátí v rR
číslici0…9 a v s zbývající prefix; INCL přidá ASCII '0'. Po vytištění
j-té cifry zprava obsahují navštívené pozice posledních j cifer
původního M S_n a s=floor(M S_n/10^j). Žádná cifra se nepřeskakuje.

Po poslední desetinné cifře SUB sníží a na0. BZ a,@−4 jde zpět
právě na SUB, nikoli na STB; druhé SUB dá−1, další BZ neodbočí.
Tečka na dec tedy zůstane a další cifra jde na dec−1. Protože S_n≥1,
má s alespoň n+1 cifer a tato větev nastane právě jednou. Poslední
DIV dá s0 a jeho cifra se ještě uloží; teprve PBNZ s pak skončí.
Z S_n<60 plyne nejvýše n+2 cifer, takže se vlevo zapisuje nejvýše
na dec−2 a před řetězcem zůstane aspoň jedna z původních mezer.

Ani při obecném MaxN17 není třeba mazat starou širší celou část:
|S_n−H_(2M−1)|<1 a
H_(20M−1)−H_(2M−1)≥ln10>2 dávají S_(n+1)>S_n. Počet cifer celé
části tedy neklesá. Pravý okraj se v každém kole posune o1; předchozí
newline přepíše cifra, nový newline leží v dosud nulové paměti a bajt
za ním zůstává0. Fputs od dec−3 dostane právě mezery, celou část,
tečku, přesně n desetinných cifer, LF a NUL. Pro n1 jsou to dvě mezery
a `3.7\n`; od n4 je jedna mezera. Globální dec/s/nn/c přežijí Fputs;
jeho návrat v$255 se před následujícím voláním znovu přepíše adresou.

## 5. Přesně převzaté výsledky a všechna časová znaménka

Celý uzavřený `workstreams/vol1/notes/mixal-rounded-harmonic.md`
byl přečten, včetně nezávislého sčítání po hladinách a jeho rozsahu.
Jeho starý výsledek `vol1/results/rounded-harmonic.json` je pro poloviny
nahoru. Od něj (1) odečítá přesně n+1 jednotek v měřítku M.
`verify_harmonic30_transfer.py` a uložený výsledek byly celé přečteny:
kontrolují jen65 změněných půlek pro n1…10, nikoli nově miliony členů.

Počet skupin je počet nerovností sousedních R(j). Jedna změněná
hodnota ovlivní pouze hrany(j−1,j) a(j,j+1); tie indexy se liší
faktorem5 a nejmenší je2^(n+1)≥4, takže tyto dvojice hran různých
změn nemají průnik. Uložené dva nové indikátory minus dva staré dávají
u všech65 položek nulu. Proto se přesně přebírají i počty skupin po
první: 4,18,61,198,630,1998,6323,19998,63244,199998, součet292472.

Deset výsledků v `results/harmonic30-transfer.json` je přesně
3.7,6.13,8.445,10.7504,13.05357,15.356255,17.6588268,19.96140681,
22.263991769,24.5665766342. Celkem mají72 cifer. Nejde o nový běh.

V modelu knižní tabulky má DIV60υ,MUL10υ,TRAP5υ, běžné zdejší
instrukce1υ a chybně predikovaný podmíněný skok navíc2υ.
STB má navíc μ; načítání instrukcí se jako datové mem nepočítá.
Jeden běžný průchod 3H/4H/2H stojí63+13+63=139υ. Pro jedno n
se k jeho g skupinám po první přidá inicializace1H3υ, první2H63υ
a poslední neúspěšný PBNZ navíc2υ: celkem139g+68.

Formatter má3υ přípravy5H a4υ za newline. Každá z d cifer stojí
66υ; poslední PBNZ s navíc2υ a jediný přeskok tečky navíc4υ.
8H stojí6υ,9H běžně12υ. To dává za jedno n139g+66d+99υ.
Main stojí2υ, poslední PBNP navíc2υ a závěrečný Halt5υ.
Paměť jsou pouze d+1 zápisů. Celý tištěný čas proto přesně je

    82μ+[139·292472+66·72+99·10+9]υ =82μ+40659359υ.      (3)

Hostitelská latence I/O v tomto nominálním modelu není. Smlouva
modelu se nezaměňuje za stopky konkrétní pipeline.

## 6. Řád času a uskutečnitelnost „asi poloviny“

Pro q=floor√M jsou hodnoty R(1)…R(q) navzájem různé, neboť
M/(j(j+1))>1 pro j<q. Za q+1 je rozdíl sousedních přesných hodnot
menší než1, takže ceil v (1) může klesnout nanejvýš o1. Odtud až
k nule jsou dosaženy všechny hodnoty od R(q+1)=√M+O(1) dolů.
Počet skupin je tedy2√M+O(1), a nejen horní O(√M). Formatter je
O(n), takže celkový řád je Θ(10^(n/2)).

Známé erratum p110 z29.3.2023 nahrazuje poslední chybný vzorec
správným R_n(1/m_(k+1))=R_n(1/m_k)−1. Jeho obor je právě druhá
oblast; ve skupinových koncích se hodnoty postupně snižují o1.
Nejde o stejnou vlastnost pro malé indexy ani o nový nález.

Konkrétní dosažitelná úprava počítá první q členů přímo a pak
přechází na skupiny. q není nutno předem znát: udržujeme j,2j,j²
a2j+1; j² se po kroku zvětší o2j+1 a tento rozdíl o2. Přímé tělo je

    SUB a,c,1; ADD a,a,j; DIV r,a,twice_j; ADD s,s,r
    ADD square,square,odd; ADD odd,odd,2
    ADD j,j,1; ADD twice_j,twice_j,2
    CMP a,square,M; PBNP a,Direct

s počátkem s0,j1,twice_j2,square1,odd3. Má69υ na běžný člen
a2υ navíc při odchodu. Před první skupinou se jednou vypočte R(j)
podle (1), nastaví m=j−1 a převezme3H/4H; místo celého2H pak stačí
SUB r,r,1 / PBNZ r,3B. To je78υ na skupinu a2υ navíc při konci.
Oba invarianty jsou přesně ty z§2, split nevynechá ani nezdvojí člen
a při q/q+1 ve stejné skupině se její zbytek prostě přičte zvlášť.
Čtverec do odchodu je≤(√M+1)²<2M pro zdejší M≥10; všechny další
meze z§3 platí. Nové pomocné GREG0 a inicializace přidají O(1).

Hlavní cena je proto147√M+O(n) proti278√M+O(n) původně, poměr
147/278≈0.529. To konkrétně odůvodňuje „asi polovinu“ v knižním
modelu. Netvrdí se globální optimum ani měřený čas všech procesorů;
tato malá odvozená varianta nebyla znovu spuštěna.

## 7. Celý asymptotický argument31 včetně celých částí

Přebírá se uzavřený důkaz v `vol1/notes/mixal-rounded-harmonic.md`,
oddíl „Úloha17“, a jeho předpoklad H_t=ln t+γ+O(1/t) pro t→∞.
Tento odhad je doložen v `vol1/notes/harmonic-analytic.md`,(A6);
existence γ a divergence jsou v harmonic-finite. Pro poloviny nahoru
bylo dokázáno S_n^+=n ln10+2γ−1+2ln2+O(M^−1/2). Rozdíl
S_n^+−S_n=(n+1)/M=o(M^−1/2) z§1 přenáší celý výsledek, ne jen limitu.

Navíc lze přímo ověřit všechny zobrazené kroky MMIX odpovědi.
Od začátku zvolme m=floor√M a N=floor(2M/(2m+1)). Počet indexů
s R(j)>m je A=ceil(2M/(2m+1))−1, tedy A=N nebo N−1. Počty
jednotlivých hladin k≤m jsou přesně

    ceil(2M/(2k−1))−ceil(2M/(2k+1)).

Nahrazení prvních A zaokrouhlených členů H_A stojí O(A/M).
Přechod k H_N při A=N−1 stojí1/N=O(m/M). Pro zvolenou m≈√M
je to rovněž O(N/M), takže první tištěná rovnost s H_N platí
i při přesné půlce na hranici. Bez této volby by obecná mez měla
explicitně také O(m/M); neprohlašujeme uniformní první O(N/M)
pro všechna libovolná m<M.

Označíme-li C_k=ceil(2M/(2k−1)), sumace po částech dává přesně
Σ(k=1…m)k(C_k−C_(k+1))=Σ(k=1…m)C_k−mC_(m+1).
Nahrazení stropů reálnými hodnotami stojí po dělení M pouze O(m/M).
Platí2Σ1/(2k−1)=2H_(2m)−H_m a mC_(m+1)/M=1+O(1/m)+O(m/M).
Proto další tištěný řádek je

    S_n=H_N+2H_(2m)−H_m−1+O(1/m)+O(m/M).

Harmonický odhad a ln N+ln m=ln M+O(M^−1/2) dávají požadovaný
hlavní člen. Odečtením dvou sousedních n dostáváme limitu ln10;
obě chybové funkce jdou k0, není potřeba předpokládat jejich monotonii.
Převzatý certifikovaný hlavní člen pro n10 je24.56657662086342,
tedy údaj24.5665766209 na začátku file119 je správně zaokrouhlený.
Jeho chyba vůči24.5665766342 je mnohem menší než samotná řádová
mez10^−5; slovní „closer than predicted“ netvrdí chybnou ostrou
univerzální konstantu.

## 8. Celostránková mapa a použití vzorů

File56: všechny49 buněk obrázku16, obecný lichý postup,19×19 program
a formátování, Ibn al-Haythamův postup i uvedené životopisné údaje
jsou v028-recovery a přesně převzatém mixal-magic-sources. Bibliografický
výrok Ball/Coxeter1939,kapitola7 má primární dobové recenze; čtení celé
doporučené knihy není dodatečná podmínka tohoto výroku. Obrázek17,
pořadí8/4,celý24/11 program, rychlý obecný algoritmus a odkaz Ahrens
1918,kapitola15 pokrývají029-fenwick/packets a převzatý mixal-josephus.
Všechna tvrzení harmonického zadání od divergence po konkrétní požadavek
na1≤n≤10 pokrývají§1–5 této poznámky. File56 má úplný rozsah.

File117: obě úplné Fibonacci rutiny, jejich nejmenší selhání a typy
přetečení jsou v027-recovery. Všechny věty odpovědi29, oba žádoucí
programy, čas před výstupem, Ingalls bez změn kódu i odkaz5.1.1–5
mají029-fenwick/packets. Kladný obor (2) a všechny deklarace začátku
odpovědi30 mají§1–3 zde. File117 má úplný rozsah.

File118: všechny pokračující deklarace, každá instrukce, deset hodnot,
přesný čas, n17, asymptotický čas, opravený rychlejší postup a všechny
rovnosti odpovědi31 mají§2–7. Známé dvě opravy zůstávají jen v evidenci.
File118 má úplný rozsah. File57 a119 zde mají jen příslušné části30/31;
jejich další kalendářní či historické výroky se tím neuzavírají.

Binomický vzor je použit na přesný obor reciprokých půlek a signed64
meze, Algorithm R na úplný profil se všemi posledními predikcemi,
kografový vzor na rozdíl mezi opravovanou pomocnou formulí a správným
výsledkem. Zejména (1) není rozšířena na všechna x a první O v31
není rozšířeno na všechny m. Úlohy30 i31 zůstávají argument_recorded,
nyní s úplným znovu vymezeným důkazem a bez nového výpočtu či nálezu.
