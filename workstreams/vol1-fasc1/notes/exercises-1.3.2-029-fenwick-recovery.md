# §1.3.2′, úloha29 — celý rychlý MMIX s tiskem

Zadání file56/p48, odpověď file117/p109. Obě originální stránky byly
zobrazeny (`images/recovery-magic-josephus-056.png`,
`images/recovery-fibonacci-117.png`). Celý uzavřený
`workstreams/vol1/notes/mixal-josephus.md` byl přečten; jeho staré běhy
ani enumerace se neopakovaly. Zde je nový celý program
`sources/josephus29-fenwick.mms`, který volí živou pozici ve stromu četností.

## 1. Význam výstupu a přesné převzetí matematiky

Na původní pozici p se tiskne její pořadí odstranění, nikoli seznam
postupně odstraněných pozic. Pro n8,m4 obrázek v pořadí od START ve
směru šipek obsahuje54613872. Odpovídající odstraněné pozice jsou
4,8,5,2,1,3,7,6; po každém odstranění se počítá od následníka.
Tak je první původní člověk pátý a druhý čtvrtý, přesně jako v textu.

Přečtený dřívější úplný argument i uložený `vol1/results/josephus.json`
pro n24,m11 dávají

    15 12 22 08 16 11 23 21 03 05 01 17 10 07 24 19 20 18 09 14 04 02 13 06

Poslední je pozice15, protože tam je24. Tento vektor byl převzat,
nikoli znovu spočten jiným Josephusovým censem.

Základní rekurence je rovněž přesně převzata: při L živých osobách
a počátečním ordinalu r je vybraná osoba na ordinalu(r+m−1) modL.
Po odstranění má její následník tentýž ordinal, případně0 po wrapu.
Převzatá recenze originálů5.1.1–2,5 dokazuje tento význam inverzní
tabulky, asociativní vkládání mezer i O(n log n) vyvážené skládání.
To je přesná opora knižního křížového odkazu; náš MMIX níže používá
jiný konkrétní datový strom se stejným asymptotickým řádem.

## 2. Datový kontrakt a stromový invariant

Program je sestaven pro N24,M11, ale celé tělo i formatter mají
prokázaný obor1≤N<2^32,1≤M<2^64, pokud jsou přidělené oblasti dostupné.
Tree obsahuje N+1 octabytes, Order obsahuje N tetrabytes a Buf11N+1bajtů.
Báze jsou od Data_Segment, všechny součty délek jsou<2^37 a nedojdou
k signed adresní hranici. Tree je zarovnané po8, Order po4; Buf jen po1.
Kód od#100 je disjunktní. Obsah těchto dat nemusí být počátečně nulový.

Pět GREG obsadí globální báze a n,m; lokální$0...$22 jsou pracovní,
$255 se použije až pro Fputs/Halt. PUT rD,0 před prvním DIVU vymezuje
přesně64bitový čitatel. Není později změněn. Předpokládáme běžné
dokumentované I/O rozhraní; chyba výstupu vede k Halt1, úspěch k Halt0.

Definujme low(j)=j & (−j), pro j>0. Stromová buňka Tree[j] je počet
živých pozic v intervalu I_j=(j−low(j),j]. Init nastaví Tree[j]=low(j),
tedy správně všechny původně živé pozice. Tree[0] není čteno. NEG
vypočte signed−j bez overflow, AND poskytne nejnižší nastavený bit.
Init pokryje právě j1...N. Pozdější Order bude před tiskem zapsáno
právě jednou na každé pozici, Buf se také vyplní před prvním čtením I/O.

## 3. Výběr ordinalu bez overflow pro libovolné M

Na vstupu Kill je left=L>0 počet živých, rank je ordinal prvního
počítaného člověka mezi živými v původním lineárním pořadí,0≤rank<L,
a step je další pořadí odstranění. mm=M−1 je unsigned slovo.

DIVU s rD=0 a divisor L≥1 je přípustné; GET rR získá zbytek mm modL.
Součet rank+zbytek je<2L≤2^33. Proto signed ADD/SUB nepřetečou a
jediné podmíněné odečtení L pomocí CSNN vytvoří přesně nový target rank.
Přímé64bitové sčítání M s rank by mohlo přetéct; kód je nedělá.
Případ M1 funguje s mm0, poslední případ L1 s divisor1.

Po uložení vybraného pořadí se left sníží. Při left0 program ihned
přejde k tisku, takže již neprovede žádné modulo0. Jinak rank≤left;
rovnost znamená odstranění poslední lineární pozice, takže CSZ nastaví
rank0. Při ostré nerovnosti zůstane správný ordinal následníka. Step
se zvětší právě pro další skutečné odstranění a nikdy se neukládá N+1.

## 4. Celý binary-lifting výběr a všechny větve

Grow najde top=2^K, K=floor(log₂N). Při posledním testu je tmp≤2^32,
tedy bez overflow. Find začíná idx0,bit=top,remain=rank.
Označme S(j) počet živých pozic≤j a p hledanou živou pozici, takže
S(p)=rank+1. Invariant při bit=b>0:

    idx je násobek2b, S(idx)≤rank, remain=rank−S(idx),
    idx < p ≤ idx+2b.

Kandidát c=idx+b má low(c)=b. Je-li c≤N, Tree[c] je proto přesně
S(c)−S(idx). Je≤remain iff c<p: pro c≥p už prefix obsahuje hledanou
živou osobu, pro c<p nikoli. V prvním případě SUB/SET přeskočí celý
levý blok a upraví remaining ordinal; ve druhém se idx nemění.
Je-li c>N, pak p≤N<c a musí se také ponechat levý blok bez čtení paměti.
To jsou všechny dvě BP větve, včetně nulových počtů v prázdném bloku.

Po SRU bit o1 je zachována dělitelnost idx i poloviční interval pro p.
Po posledním bit1 interval obsahuje jedinou celočíselnou možnost p=idx+1.
ADD pos a STTU step,Order,4(pos−1) tedy uloží správné pořadí původní
pozice. Počet Find kroků je přesně K+1 na každého člověka; žádná větev
nečte Tree za N. Při N1 je tentýž důkaz jeden krok bit1.

## 5. Celá aktualizace stromu a ukončení

Delete začne j=p. Právě ty intervaly I_j, které obsahují p, ztratí
jednoho živého. Kód je navštíví posloupností j←j+low(j).
Pro důkaz úplnosti: má-li I_j délku l a obsahuje p, pak
low(j+l)≥2l a (j+l)−low(j+l)≤j−l<p. Další interval tedy p obsahuje.
Pro j<k<j+l naopak low(k)=low(k−j)≤k−j, tedy k−low(k)≥j≥p;
takový mezilehlý interval p neobsahuje. Posloupnost proto nevynechá
žádný správný endpoint. První endpoint p je zjevně nejmenší možný.

Každé navštívené value je≥1, protože p je právě živé, takže SUB1
je nezáporné. STO obnoví invariant Tree. J roste a jeho lowbit alespoň
zdvojnásobuje, takže nejvýše K+1 aktualizací skončí za N. Jejich adresy
jsou uvnitř Tree a všechna j,idx/cand i8j jsou malá signed slova.

Počet živých po celém Delete klesne přesně o1. Indukce dokazuje N
odstranění, každou původní pozici právě jednou a celý Order v rozsahu
1...N. N<2^32 opravňuje všechny STTU bez ztráty. InicializaceO(N),
výběr/aktualizace O(log N) na osobu dávají **O(N log N)** slovních
operací a **O(N)** prostoru, bez lineární závislosti na M. Pro neomezené
víceslovné M by bylo třeba započíst jiné dělení; to se netvrdí.

## 6. Úplné formátování všech přípustných N

Width opakovaným kladným DIV10 najde d, počet desetinných cifer N;
1≤d≤10. Pro každou původní pozici se načte její rank a d opakování
DIV/GET vypíše zprava všechny cifry, včetně úvodních nul. Každý
zbytek je0...9, přičtení'0' dá správný ASCII bajt. Po poslední cifře
prvního pole může end=−1, ale již se na této adrese neukládá.

Oddělovač je mezera kromě poslední pozice, kde CMP/CSZ zvolí LF.
Outoff roste po d+1; poslední PBN skončí a STB0 vytvoří terminátor na
offsetu N(d+1)≤11N. Všechna čtená a vydaná data jsou inicializovaná.
Fputs a obě větve Halt jsou stejné explicitní návratové rozhraní jako
u úplného magic28; žádné I/O registry se po volání nepoužijí k dalšímu
počítání. Pro24je d2 a text má72bajtů včetně posledního newline.

## 7. Přesné náklady, včetně zpracování všech větví

Nechť T=Σ_(j=1)^N low(j), O počet Find kandidátů>N za celý běh.
T je přesný počet aktualizovaných uzlů: každá původní pozice se jednou
odstraní a uzel j se zmenší právě pro|I_j|=low(j) pozic. O závisí jen
na tvaru stromu N, protože každé cílové p1...N je jednou vybráno.

Init/Grow/příprava stojí Nμ+(7N+5K+15)υ. Předvýběr DIVU/GET/ADD/
SUB/CSNN má64υ, příprava Find3υ, uložení pos4υ+μ a SET j1υ.
Jeden přípustný Find krok stojí11υ+μ: při přeskočení je BP za1 a
SUB/SET za2, při nepřeskočení BP za3. Krok s c>N stojí7υ bez mem.
Poslední PBNZ každého hledání přidá2υ. Delete stojí2Tμ+(9T+2N)υ.
Zakončení všech kol je(6N−2)υ, včetně posledního vykonaného BZ.
Celkem před formatterem:

    [N(K+3)−O+2T]μ
    +[(11K+100)N+9T−4O+5K+13]υ.                        (2)

Formatter včetně width, terminátoru a úspěšných Fputs/Halt má

    [N(d+2)+1]μ+[(66d+16)N+62d+22]υ.                    (3)

Zde každý digitový průchod stojí66υ, poslední PBNZ další2υ; zahrnuta
jsou všechna opakovaná dělení i poslední špatná predikce vnější smyčky.
Při I/O chybě přibudou2υ za BN. Jde o nominální instrukce tabulky1,
nikoli wall-clock práci hostitelského I/O.

Pro N24 je K4,T68. Hodnoty lowbit dávají12+12+12+16+16=68;
všech120 Find kandidátů je≤24, tedy O0. Počty přijetí jednotlivých
bitů jsou8,8,12,12,12, celkem52, jejich součet není nahrazen náhodným
odhadem. (2) je304μ+4101υ a(3)97μ+3698υ; celý program tedy
**401μ+7799υ**.

## 8. Jediný nový krátký native běh a otevřený další námět

`verify_josephus29_program.py` jednou pod nice15 sestavil a spustil
pouze tento nový program24,11. Výsledek porovnal bajt po bajtu se
starým přijatým `requested_ranks`, nikoli novým přepočtem Josephusovy
rekurence. Navíc malý součet tvaru nového stromu ověřil120/52/0/68;
nejde o opakování starého stromového testu do10000.

Výstup všech72bajtů souhlasí. Native profil je3135 instrukcí,
401mem a7799oops, přesně(2)+(3). Celý krok včetně sestavení nástrojů
trval1.436s. Evidence je v `results/josephus29-program.json`,
`josephus29-build-and-run.json`, `josephus29-listing.txt`,
`josephus29-simulator-profile.txt` a `josephus29-output.txt`.
Tento úspěšný běh se nebude opakovat.

Původní historický odkaz Ahrens1918, kapitolaXV, je přesně převzatý
v přečteném rozsahu titulního listu,118–120 a154–155; celý52stránkový
text není vydáván za auditovaný. Samotný konkrétní odkaz je doložený.

Požadovaný celý MMIX program, tisk i obecné zrychlení jsou uzavřené.
Původně oddělený další Ingallsův námět nyní dokončuje
`exercises-1.3.2-029-packets-recovery.md`: celé pakety bez změny kódu
a přesná cena. **E29 je po obou blocích argument_recorded.** Rétorické
„neatest“ není tvrzení, že zde byl dokázán globální optimum přes všechny
programy. Tento stromový program se za takový důkaz nevydává.

Vzor stavového důkazu zde vyžaduje invariant všech stromových intervalů
a modulo bez64bitového overflow; nákladový vzor započítává vytvoření
stromu a formatter; převzetí uzavřených výsledků uchovává původní
rank vektor bez dalšího censu.
