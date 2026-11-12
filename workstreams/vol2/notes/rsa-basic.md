# §4.5.4: RSA, Rabin a úlohy 32–35

Audit třetího vydání, prvního dotisku, 3. listopadu 2026. Vizuálně
přečteny strany 403–407, zadání na 415 a odpovědi na 664–665.
Sedm souvisejících zpráv na začátku 405 a úloha 44 jsou uzavřeny
v [rsa-advanced.md](rsa-advanced.md);
historie velkých prvočísel od nadpisu na 407 je samostatný blok.

**Výsledek:** dva nové potvrzené nálezy: [C0166](C0166-rsa-root-density.md)
opravuje pravděpodobnost na 405, [C0167](C0167-rsa-padding-boundary.md)
řeší nechráněné x=floor(cuberoot(N)) v odpovědi 32. Úlohy 32, 34
a 35 mají níže obecné důkazy; úloha 33 je auditována jako otevřený
výzkumný problém, nikoli vyřešena. Pět přesných checkpointů prošlo.

## 1. Modulární inverze a společná zpráva

Modul je N=pq, kde p,q jsou různá lichá prvočísla. **Jednotka**
je zbytek nesoudělný s N. **Čínská věta o zbytcích (CRT)** říká,
že zbytek modulo N je jednoznačně určen zbytky modulo p a q.
Počet jednotek je phi(N)=(p-1)(q-1). Zvolme kladné exponenty
e,d tak, aby ed=1 (mod phi(N)).

Pro každé celé x, včetně nejednotek, platí (x^e)^d=x (mod N).
Modulo p je to při p|x rovnost nul; jinak použijeme Fermatovu
větu a p-1|ed-1. Stejný argument pro q dokončí důkaz pomocí CRT.
Pro e=3 a p mod 3 = q mod 3 = 2 proto existuje právě jedna třetí
odmocnina každého zbytku. Inverzi d lze volit pod phi(N)<N.
Znalost faktorů dává inverzi; znalost d dává vhodné m=3d-1
pro faktorizaci z §3. Z toho neplyne, že každá metoda inverze odhalí d.

Jsou-li N1,N2,N3 po dvou nesoudělné a 0<=x<min(N1,N2,N3),
tři šifrované zbytky určují x^3 modulo jejich součin.
Jelikož x^3<N1*N2*N3, dostaneme přesné celé x^3 a obyčejnou
třetí odmocninou i x. Společný prvočíselný dělitel modulů by
už sám poskytoval faktor přes největší společný dělitel.

Binární umocnění na 3 vyžaduje dvě modulární násobení, na
65537=2^16+1 šestnáct čtverců a jedno násobení. Poměr 17/2=8.5
je přesný počet těchto operací, ne bezpodmínečný poměr skutečných časů.
Prvočíselnost 65537 je součástí konečné kontroly. Knižní odhad jedné
třetiny krátkých prvních bloků vychází z uvedeného logaritmického
modelu vedoucích číslic; neplatí pro každé rozdělení zpráv.

## 2. Úloha 32: malá zpráva a opravené náhodné doplnění

Označme M=floor(cuberoot(N)). Jelikož N=pq není krychle,
platí M^3<N. Knižní větev x>=M proto propustí hodnotu x=M
bez doplnění. Pro N=55, M=3, x=3 odešle 27 a obyčejná
třetí odmocnina zprávu přečte. Hodnota patří do povoleného intervalu
0<=x<M^3-M^2=18. Známé erratum z roku 2004 mění pouze horní
mez náhodného y na ostrou; tento problém neřeší.

Následující vlastní oprava zachová náhodné doplnění pro všechna malá x.
Definujme celá čísla B=ceil(cuberoot(N))=M+1, J=floor(N/B),
H=(J-B)*B. Zprávu omezíme na 0<=x<H. Pro x>=B ponecháme z=x.
Pro x<B zvolíme rovnoměrně jedno z B celých čísel J-B<=y<J
a položíme z=x+yB. Odešleme z^3 mod N. Po modulární inverzi
vrátíme z mod B, jestliže z>=H, a samotné z jinak.

Pro nekrychlové N>=28 máme B>=4 a
N>=(B-1)^3+1>=B(B+1): rozdíl posledních dvou výrazů je
B(B^2-4B+2)>=0. Tedy J>=B+1 a H>=B.
Nedoplněné reprezentanty leží v [B,H), doplněné v [H,JB).
Oba intervaly leží v [B,N), nekolidují a dekodér je správný.
Každé z má z^3>=N. Žádný reprezentant se tedy nevyhne redukci.
Navíc šifrovaný zbytek nemůže být obyčejnou krychlí t^3<N:
jednoznačnost modulární třetí odmocniny by vynutila z=t<B.

Ztráta kapacity je přesně N-H=B^2+(N mod B), tedy O(N^(2/3))
z N možných symbolů. Pro velká N jde o zanedbatelnou relativní
ztrátu; délka zpráv se podstatně nezvětší. Jde o odstranění
konkrétního úniku z této úlohy, nikoli o důkaz obecné bezpečnosti.

První checkpoint také zkoušel minimální aritmetickou opravu
x=M -> z=M^3 s výjimkou v dekodéru. Ta sice zabrání obyčejnému
odmocnění, ale dává této zprávě jeden veřejný kód. Doporučujeme
proto jednotnou náhodnou variantu; má samostatný pátý checkpoint.
Úspěšné první čtyři kontroly se při jejím přidání neopakovaly.

## 3. Úloha 34 a chybný součin na straně 405

Pro kladné m označme P=gcd(m,p-1)/p a Q=gcd(m,q-1)/q.
To jsou přesné pravděpodobnosti x^m=1 modulo příslušné prvočíslo,
když je x rovnoměrný zbytek. Nenulové zbytky tvoří cyklickou grupu;
rovnice mt=0 (mod p-1) má právě gcd(m,p-1) řešení.
CRT dává pravděpodobnost PQ modulo N. Pravděpodobnost,
že gcd(x^m-1,N) poskytne právě jeden faktor, je

    S = P(1-Q)+Q(1-P) = P+Q-2PQ.                 (1)

Položme delta=10^(-12) a předpokládejme PQ>=delta.
Je-li P<=1/2, výraz (1) s Q neklesá, a proto

    S >= P+delta/P-2delta >= 2sqrt(delta)-2delta.

Stejně postupujeme pro Q<=1/2. Očekávaný počet pokusů je menší
než 500001; každý potřebuje O(log m) modulárních operací.
To odpovídá řádu 10^6 log m v odpovědi.

Jsou-li obě pravděpodobnosti větší než polovina, musí být
p-1|m a q-1|m: vlastní dělitel p-1 je nejvýše (p-1)/2.
Pišme m=2^k r, kde r je liché. Nejprve zkusíme gcd(x,N);
vlastní dělitel už řeší úlohu, x=0 znovu vylosujeme. Zbývá
rovnoměrná jednotka. Umocnění na r odstraní liché části jejích
řádů modulo p a q. Pokud se mocniny dvou v těchto řádech
liší, při opakovaném čtvercování dostaneme před první jedničkou
netriviální odmocninu jedničky a gcd oddělí faktory.

Označme a=v2(p-1), b=v2(q-1), kde v2(t) je exponent
nejvyšší mocniny dvou dělící t. V cyklické grupě řádu 2^a
je jeden prvek řádu 1 a 2^(j-1) prvků řádu 2^j, 1<=j<=a.
Pravděpodobnost shodného řádu obou nezávislých složek je

    (1 + sum_{j=1}^{min(a,b)} 4^(j-1)) / 2^(a+b)
        = (4^min(a,b)+2) / (3*2^(a+b)) <= 1/2.

Poslední poloviční mez v odpovědi je tím přesně zdůvodněna pro
jednotky, s běžným gcd předtestem pro ostatní vstupy.

Jsou-li p1|p-1 a q1|q-1 prvočísla, pak p1∤m dává P<1/p1,
zatímco q1∤m dává Q<1/q1. Součin mezí smíme použít, když chybí
**oba** dělitelé. Chybí-li jen jeden, obecně máme pouze
PQ<1/min(p1,q1). Nález C0166 má p=23,q=47,p1=11,q1=23,m=22:
přesně 44 z 1081 zbytků splňuje kongruenci, ačkoli 253 nedělí 22.
Tím vyvrací knižní mez 1/253. Při případné rovnosti p1=q1 je
nutné formulovat větev dělitelnosti pomocí lcm(p1,q1), ne součinu.

## 4. Rabinova odmocnina a Williamsova úloha 35

Definujme f=(p^(q-1)-q^(p-1)) mod N. Fermatova věta dává
f=-1 (mod p), f=1 (mod q). Kořeny čtverce x^2 jsou
x,-x,fx,-fx modulo N. Jsou čtyři různé právě pro jednotku;
pro násobek jediného faktoru dva a pro nulu jeden. Knižní popis
čtyř kořenů na 406 používáme s touto kvalifikací, kterou známá
oprava odpovědi 35 výslovně zohledňuje.

Při rovnoměrné jednotce x jsou čtyři kořeny jejího čtverce
stejně pravděpodobné. Libovolný pevný výstup odmocňovacího
algoritmu se s poloviční pravděpodobností liší od ±x;
pak gcd(x-y,N) poskytne faktor. Náhodný algoritmus posoudíme
podmíněně jeho náhodnými volbami. Pro nejednotku pomůže gcd
předem. Toto je redukce faktorizace na odmocňování, nikoli
řešení obdobné otázky pro RSA.

Nyní p=3 (mod 8), q=7 (mod 8). **Jacobiho symbol**
J(t)=(t/p)(t/q) je součin dvou Legendreových symbolů.
Legendreův symbol je 0 pro násobek prvočísla, +1 pro nenulový
čtverec a -1 pro ostatní zbytky. Jacobiho symbol proto
má hodnoty -1,0,1, přičemž nula znamená nejednotku.
Z jeho násobnosti a doplňkových zákonů plyne

    J(-1)=1, J(2)=-1, J(f)=-1,
    J(-x)=J(x)=-J(2x), J(fx)=-J(x).

Zpráva má rozsah 0<=x<=(N-5)/8. Zvolíme z=4x+2 nebo
z=8x+4, aby J(z)>=0, a odešleme z^2 mod N.
Je-li symbol nula, fungují obě volby. Vždy 0<z<N a z je sudé.
Pro jednotkový čtverec mají právě dva kořeny kladný symbol;
jsou navzájem opačné a právě jeden je sudý. Pro nenulový
nejednotkový čtverec jsou dva opačné kořeny se symbolem nula,
opět právě jeden sudý. Dekodér tedy jednoznačně vybere y=z.
Když y mod 4=2, vrátí floor(y/4); jinak floor(y/8).
Obě možnosti vracejí původní x.

Známá oprava z 18. února 2004 je nutná: pro N=21, x=1
mají obě možnosti 6 a 12 nulový symbol. Původní podmínka J=1
nevybere ani jednu. Opravená podmínka i důkaz pokrývají nejednotky.

Je-li falešný vstup t jednotka s J(t)=-1, dekodér čtverce
vrací kořen y s J(y)=1; nutně y=±ft, a gcd s t faktorizuje.
Vrací-li zařízení jen dekódovanou zprávu w, zkusíme kandidáty
4w+2,8w,8w+4 a otestujeme jejich čtverec. Pravý y je mezi nimi.

Ani příslib dekódování jen platných šifer tuto redukci neodstraňuje.
Pišme p=8a+3, q=8b+7. Z (N+3)/8 zpráv má 4x+2
násobek p v b+1 případech a násobek q v a případech;
průnik je prázdný, protože 0<4x+2<N/2. První počet plyne
z lichých násobků p pro 2x+1 v intervalu [1,(N-1)/4]:
jsou to násobky 1,3,...,2b+1; pro q obdobně 1,3,...,2a-1.
Počet jednotkových zpráv je tedy

    V = (N+3)/8-(a+b+1) = (phi(N)+4)/8.

Díky jednoznačnému dekódování mají různé zprávy různé šifry.
Rovnoměrné t se symbolem -1 dává rovnoměrný jednotkový čtverec;
ze phi(N)/4 takových čtverců je V platných šifer. Podíl
1/2+2/phi(N)>1/2 tak stačí i pro tento užší příslib zařízení.

## 5. Úloha 33 a vymezený kontext

Úloha 33 žádá obecnou účinnou redukci faktorizace na inverzi RSA.
[Dachman-Soled, Loss a O'Neill, ITC 2024](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITC.2024.8),
úvod 8:1–8:3 (8:2 také vizuálně), výslovně odlišují tento obecný
otevřený problém od svého výsledku pro generický okruhový model
s předzpracováním. V tomto modelu algoritmus používá předepsané
okruhové operace a testy rovnosti; nedostává neomezený přístup
k bitové reprezentaci jako obecný algoritmus. Nález obecného
řešení při rešerši 3. listopadu 2026 nemáme. Dřívější stav checked znamenal pouze
ověřené zadání a výzkumný status. Od 6. listopadu 2026 je celá
úloha partial: vyžádanou obecnou redukci nemáme dokázanou.

Rivestův [autorský přepis původního článku](https://people.csail.mit.edu/rivest/Rsapaper.pdf)
byl čten v úvodu, §§II–VI a na začátku VII; strany 5–7 také vizuálně.
Potvrzuje obecný exponent i inverzi včetně nejednotek. Přepis má
jiné stránkování než původní CACM 21 (1978), 120–126.
Podpisy a důvěryhodný adresář na 406 odpovídají této původní
motivační konstrukci. Při skládání operací různých uživatelů je
zprávu třeba reprezentovat v přípustných blocích příslušného modulu;
jediný zbytek pod jedním modulem nemusí být pod jiným.
Tento odstavec není důkazem obecné nepadělatelnosti protokolu.

[Rabinův původní TR-212](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-212.pdf)
má titulní datum leden 1979; přečtena titulní strana a celý abstrakt
na tištěných 1–2 (PDF 5–6). Plný externí důkaz nebyl přeauditován;
potřebná elementární redukce je nezávisle dokázána v §4.
[Williamsův autorský záznam s původním textem](https://www.researchgate.net/publication/3083444_A_modification_of_the_RSA_public-key_encryption_procedure_Corresp)
uvádí IT-26 (1980), 726–729 a přijetí rukopisu 17. července 1979.
Původní OCR 726–728 bylo čteno ve vybraných pasážích včetně
konstrukce a podmínek; přímé stažení PDF vrátilo 403 a webový
snímek timeout. Vizuální četbu článku netvrdíme. Rok 1979
v zadání není v rozporu s publikací roku 1980.

Konstrukce prvočísel na 405: pro p=kp1+1, sudé k a
k=p1 (mod 3) platí p=2 (mod 3). Odhady přibližně 90 pokusů
jsou heuristikou hustoty prvočísel (ln(p0)/2, resp. ln(p1*p2)/3),
nikoli jednotnou mezí mezer mezi prvočísly. Počet mikrosekund
za rok odpovídá 365.2425 dnům. 10^25 mikrosekund je přibližně
3.1688*10^11 let; dělení 10^10 dává 31.688 let. Jde o
podmíněný dobový ilustrativní výpočet, nikoli současný odhad bezpečnosti.
Přesný originál X.509 1989 (74–76), přepis Cocksovy zprávy 1973
a archivní oznámení CESG nyní uzavírá [rsa-history.md](rsa-history.md). Bezpečnostní hodnocení roku 1997 se neaktualizuje
na dnešní doporučení pouhým přepočtem těchto čísel.

## 6. Reprodukce a errata

[Program](../verify_rsa_basic.py) a [výsledek](../results/rsa-basic.json)
obsahují pět oddělených checkpointů. Enumerace zbytků kontroluje
uzavřené vzorce, přímá modulární inverze rekonstrukci CRT,
tabulka všech čtverců klasifikaci kořenů a přesná celočíselná
odmocnina hranice doplnění. Nejde o dvě spuštění stejného modelu.

| Kontrola | Rozsah | Sekundy |
|---|---|---:|
| RSA | 66 modulů, 123474 všech zbytků, 55 společných zpráv | 1.574 |
| Řády | 4992 instancí, 2226816 zbytků, 31524 jednotkových posloupností | 3.090 |
| Doplnění, původní a první oprava | 102338 zpráv, 110040 reprezentantů | 0.519 |
| Williams | 144 modulů, 1200784 vstupů, 153416 kódování, 587264 falešných jednotek | 39.141 |
| Jednotná náhodná oprava | 113277 zpráv, 122377 reprezentantů | 0.137 |

První běh PID 1298581, obal 1298580, session 97744, limit 180 s,
exit 0. Pátý checkpoint PID 1298834, obal 1298833, limit 60 s,
exit 0. Vše prošlo; úspěšné checkpointy se neopakovaly.

Prohledány celé all2-prepre, all2-pre, all2, err2 i TeX err2
podle stran a výrazů RSA, Rabin, Williams, cube, probability,
Jacobi, 32, 34, 35. Známé opravy: 404 rozsah/indexy z roku 2011,
404 slovo quickly z roku 2000, 406 published z roku 1999,
407 Cocksův dodatek 2010, 664 horní mez y a 664–665 nulové
Jacobiho symboly z 18. února 2004. Strany 41–42 historických
errat byly také vizuálně přečteny. Oprava součinu na 405 ani
prahu x=M v odpovědi 32 nalezena nebyla.

Zdroje, hashe a přesné limity jsou v [metadatech](../sources/rsa-basic.json).
Pozdější fyzický dotisk a prvenství nových nálezů nejsou ověřeny.
Hlášení nebyla odeslána; celý svazek zůstává rozpracovaný.
