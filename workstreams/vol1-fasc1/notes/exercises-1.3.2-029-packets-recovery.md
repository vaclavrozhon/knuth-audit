# §1.3.2′, úloha29 — Ingallsovy pakety bez změny kódu

Tento blok dokončuje poslední konkrétní námět odpovědi file117/p109.
`sources/josephus29-packets.mms` je celý vlastní program pro24,11;
generátor `generate_josephus29_packets.py` dovoluje před sestavením
zvolit1≤N≤219,1≤M<2^64. Po spuštění se žádná instrukce nemění.
Obecný rychlý program pro mnohem větší N a celý význam výstupu jsou
samostatně dokázány v `exercises-1.3.2-029-fenwick-recovery.md`.

## 1. Následníci v registrech a přesné rozhraní GO

Každá osoba i má vlastní globální registr Next_i a tento osmipříkazový
paket s neměnnými instrukcemi:

    Entry_i     SUBU count,count,1
                PBNZ count,Continue_i
                SET successor,Next_i
                SET victim,i
                JMP Remove
    Continue_i  GO prev,Next_i,0
    Update_i    SET Next_i,successor
                JMP Continue_i

Inicializační GETA nastaví Next_i=Entry_(i+1), poslední na Entry_1.
Všechna Next_i jsou deklarovaná **GREG0**. Primární MMIXAL dokumentace
v `sources/mmixal-20250620.w`,559–571, rozlišuje tyto pracovní registry
od shodných nenulových konstantních bází, které může sdílet. Zde jsou
tedy různé měnitelné registry, nikoli aliasy stejné nuly či měněné báze.

Instrukce GO uloží do svého X adresu následující instrukce a přejde
na adresuY+Z. Proto GO v Continue_i nastaví **prev=Update_i** a začne
počítat u živého následníka. Právě umístění Update bezprostředně za
Continue je podstatné: nevkládá se zde PUSH/POP, zásobníkový návrat
ani domnělá vlastnost JMP, který tuto adresu neukládá.

Common Remove zná i ve victim a zachycenou adresu jeho následníka
v successor. Uloží pořadí do Order[i−1], sníží left a při left0 odejde
k tisku. Jinak zvýší step, obnoví count=M a vykoná GO$255,prev,0.
Tento GO nepoškodí prev; jeho nový link v$255 je nepotřebný.
Update předchůdce změní svůj Next registr na successor a přes Continue
přejde k novému prvnímu počítanému člověku. Žádné opkódy či adresní
pole instrukcí nejsou zapsány.

## 2. Celý invariant kruhu a mezní stavy

Mezi živými pakety Next tvoří jediný orientovaný kruh v původním
pořadí. Před každým Entry_i je i živá, prev=Update_p pro jejího
živého předchůdce p a count je počet ještě potřebných návštěv včetně i.
Na začátku i1,prev=Update_N,count=M, takže to platí i pro M1.

Pokud SUBU vytvoří nenulový count, PBNZ přeskočí odstranění a GO
přejde k následníkovi, nastaví jeho správného předchůdce a zachová
počet potřebných návštěv. Pokud vytvoří0, jde přesně o M-tou návštěvu
od posledního zahájení počítání. Zachycený successor je stále živý,
pokud nezbývala jediná osoba. Remove/Update přepojí právě Next_p,
takže odstraní i z jediného kruhu a nic jiného nezmění.

Při více než jedné živé osobě je p≠i. V jednoprvkovém kruhu p=i,
ale právě tehdy left klesne na0 a žádný helper se už nepoužije.
M1 nepotřebuje předchozí normální průchod: počáteční prev je nastaveno
výslovně a helperův Continue vždy zachová správný prev pro následující
okamžité odstranění. Při libovolném M může počítání kruh opakovaně
oběhnout; tento invariant nezávisí na počtu oběhnutí.

SUBU je záměrně unsigned, takže funguje i pro M≥2^63 bez signed
overflow. Z kladného count se vždy odečte1 a při nule se ihned odejde
nebo obnovíM; pod0 se nepočítá. Každé kolo má konečně právěM návštěv
a left klesá N,...,1,0. Výsledkem je každé pořadí1...N jednou na
správné původní pozici. Stará data v Order nejsou před přepisem čtena.

## 3. Registrační, paměťové a adresní meze

Next zabere N registrů, Order/Buf/n/m nejvýše čtyři další globály.
Proto rG≥255−(N+4)=251−N≥32 při N≤219. Všechny pracovní lokály
jsou$0...$16, tedy pod rG; $255 je oddělený scratch/link/I/O registr.
Pokud n=m, případné sdílení jejich nenulové neměněné konstanty je
neškodné a pouze zvýší rG. Mutable Next nemají tuto výjimku.

Order je4N bajtů po tetrabytes, Buf11N+1 bajtů. Mají disjunktní
kladné adresy od Data_Segment, code od#100. Jediné datové zápisy
před formatterem jsou N×STTU do Order; veškeré přepojování používá
SET do registru. Počty a indexy nepřesáhnou219, časy se nedrží v
aritmetickém počítadle, které by mohlo přetéct.

Paketů je8N instrukcí, inicializace a společné tělo přidají méně než
N+100. I při219 je celá code oblast menší než2100tetrabytes. Všechny
GETA/relativní větve jsou proto ve svém rozsahu a GO vždy míří na
zarovnaný doložený Entry nebo Update. Starý problém sestavovače při
přechodu bit63 se zde nemůže objevit.

## 4. Formatter je převzatý s úplně shodnými předpoklady

Tělo od Done až po OutputFailure je bajtově shodný text již uzavřeného
formatteru z Fenwick programu; ověřen hash
7dfa1745c79fcc1fc8f07054f24c545ba75b20555ec46f4825573809855d14d9.
Všechny jeho symbolické registry mají zde vlastní deklarace, stejné
obory, stejné n, hotovou permutaci Order a dostatečný Buf. Předchozí
důkaz všech d cifer, mezery/newline, koncového NUL a obou I/O návratů
se tedy přebírá přesně; není pouze převzatý vzhled výstupu.

Při prvním sestavení vlastního nového programu chyběla deklarace t
pro tento formatter. Assembler správně odmítl tři operandy a žádný
MMIX příkaz ještě neběžel. Deklarace t=$16 byla doplněna; původní
diagnostika je v `results/josephus29-packets-initial-assembly.json`.
To je vlastní oprava rozhraní, nikoli nález v knize nebo její assembleru.

## 5. Úplná cena a srovnání dvou skutečných MMIX programů

Inicializace má N GETA a šest dalších instrukcí, tedy(N+6)υ.
V každém zN kol je M−1 normálních návštěv, každá SUBU/PBNZ/GO
za1+1+3=5υ a bez mem. Každá skutečná odstraněná Entry stojí7υ:
SUBU1,PBNZ3,dva SET2,JMP1.

Společná Remove s helperem při nezávěrečném odstranění stojí15υ+μ:
SUB,SLU,STTU,SUB,BZ za5υ, INCL/SET/GO za5υ a helper SET/JMP/GO
za5υ. Závěrečná Remove stojí7υ+μ a žádný helper se neprovede.
Před formatterem je proto přesně

    Nμ+[N+6+5N(M−1)+22(N−1)+14]υ
     = Nμ+(5NM+18N−2)υ.                                (1)

Žádná cena vytvoření propojení nebo posledního helperu se nezamlčela.
Pro24,11 je(1) **24μ+1750υ**. Převzatý formatter má97μ+3698υ,
tedy celý úspěšný program **121μ+5448υ**. Těsně před vlastním TRAP Fputs,
po vytvoření a adresování celého řetězce, je to121μ+5436υ.

Fenwick program měl před formatterem304μ+4101υ a celkem401μ+7799υ;
těsně před Fputs tedy401μ+7787υ. Oba konkrétní vyplňují chybějící
časové místo odpovědi podle jasně určeného programu a okamžiku.
Nejde o porovnání MMIX jednotek s nesrovnatelnými MIX časy.

Pro N24 a libovolné M mají dva celé programy ceny

    packets: 121μ+(120M+4128)υ,
    Fenwick: 401μ+7799υ.

Packet varianta je levnější iff120M<280(μ/υ)+3671. Například pro μ=υ
je levnější pro M≤32 a Fenwick pro M≥33. Toto plyne z přesných profilů,
ne z nového spuštění těchto hodnot. Packet postup je O(NM) a je omezen
počtem globálních registrů; Fenwick O(N log N) pokrývá velké N i M.
Není tvrzeno globální optimum ani objektivně „nejhezčí“ ze všech programů.

## 6. Jediný nový úspěšný běh a uzavření29

Po opravě chybějícího aliasu proběhlo jediné nové nice15 sestavení a
jediné spuštění packet programu24,11. První neúspěšná assembly výše
nic nespustila. Uložený accepted rank vektor se pouze přečetl; starý
Josephus/MIX test ani nový Fenwick běh se neopakovaly.

Všech72 výstupních bajtů souhlasí; native profil1816instrukcí,
121mem,5448oops přesně potvrzuje(1) a celý převzatý formatter.
Úspěšný build-and-run trval1.454s. Evidence:
`results/josephus29-packets.json`, `josephus29-packets-build-and-run.json`,
`josephus29-packets-listing.txt`, `josephus29-packets-profile.txt`.
Výstup je shodný s již uloženým `josephus29-output.txt`.
Tento úspěšný běh se neopakuje.

Spolu s úplným Fenwick blokem jsou nyní pokryty celé zadání29, příklad
a obrázek8/4, konkrétní24/11, poslední pozice15, oba celé MMIX návrhy,
jejich ceny, explicitní Ingallsův námět bez změny kódu, asymptotické
zrychlení i přesný rozsah historického/křížového odkazu. **E29 je
argument_recorded.** Výzva k hledání dalších elegantních řešení zůstává
výzvou, ne neověřeným tvrzením o jednom globálně nejlepším programu.

Vzor stavového důkazu vyžaduje skutečný link GO, inicializovaný prev
pro M1 a nepoužití helperu po poslední osobě. Nákladový vzor zahrnuje
každé přepojení i inicializaci registrů. Převzatý formatter má shodné
tělo a výslovně zkontrolované rozhraní, ne pouhý odkaz na jiný stroj.
