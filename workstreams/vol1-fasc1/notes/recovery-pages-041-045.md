# Obnova úplného rozsahu: souborové strany 41–45 / tištěné 33–37

Celý Program P, diagram 14, všech osm komentářů a začátek souhrnu
MMIXAL jsou porovnány s důkazy a primárními pravidly. Oba nově
odhalené rozpory jsou v samostatných poznámkách C0016/C0017;
zde je přesně rozsah celých stran. Žádný assembler ani MMIX program
se nespouštěl a žádný starý běh nebyl opakován.

## File 41 / p33: diagram, data a všechny instrukce P1–P8

Originální diagram `images/block2-pdf-041.png` zobrazen. Hrany jsou
P1→P2→P3; P3 no→P4→P5→P6; P6 yes→P4, no→P7; P7 yes→P2,
no→P8→P6; P3 yes→P9→P10→P11; P11 no→P10, yes→konec.
Každá přesně odpovídá samostatně dokázanému kroku V0086 na předchozí
straně. Diagram nezavádí jinou pořadovou podmínku ani vynechanou větev.

V0088–V0089 z `independent-arguments-033-040.md` se přebírají v celém
rozsahu. `D=2^61`, PRIME1=D, ptop=BUF=D+1000, j0=−998 modulo 2^64.
Rozsah tabulky je [D,D+999], buffer [D+1000,D+1007]; jsou disjunktní
a správně zarovnané. GREG paměť nevytváří. Nuly dostanou šest různých
registrů 254..249. Čtyři nenulové konstanty ptop, j0, textová báze
a pattern mají navzájem různé hodnoty a dostanou 248..245. rG=245 je
platné a všechny pracovní registry jsou skutečně globální, tedy
nedochází k implicitnímu rozšíření lokálního prefixu nebo spillingu.
Alias mm=kk je použit až po skončení divisorské fáze.

Invariant na P2: uložených j prvočísel, `jj=2(j−500)`, n další správně
přijaté prvočíslo. Adresa ptop+jj=D+2j je přesně PRIME[j+1], nikoli
PRIME[j]. INCL zvýší j a BZ rozpozná 500. Pro divisor platí
`kk=2(k−1−500)`; j0 tedy představuje k=2. DIV má kladné n,pk<8192,
bez přetečení, nulového dělitele nebo jiného aritmetického tripu.
rR=0 vrací na P4; CMP/BNP vrací na P2 právě při q≤pk; jinak kk+=2
a opakuje se P6. Příslušné prime divisory již existují podle úplného
důkazu V0086. Nejvyšší write je PRIME[500]; při j=500 se do P4 ani
na další write nepokračuje. Všechny mezivýsledky i signed offsety
mají přesné bezpečné meze z převzatého důkazu.

## File 42 / p34: všechny instrukce P9–P11 a komentáře 1–3

V0090–V0092 se přebírají včetně decimal invariantu. Buffer je před
každou hodnotou space, čtyři ASCII nuly a tři NUL. Po d iteracích
`pk=floor(N/10^d)` a posledních d digitových pozic obsahuje zbytek
N modulo 10^d. Starý operand DIV při X=Y je zajištěn instrukčním
kontraktem; GET rR přečte zbytek před dalším dělením. `1≤d≤4`
zaručuje, že STBU nezasáhne leading space ani terminátor. Všech 500
kladných hodnot se proto tiskne správně včetně leading zeros.

Pro řádek m a sloupec c je před načtením
`mm=2(m−1)−1000+100c`, adresa `D+2(m−1)+100c`, tedy PRIME[m+50c].
Po c<10 sloupcích zůstává mm záporné; po desátém je `2(m−1)`.
Vnější test proti 98 skončí právě pro m=50. Vnitřní i vnější probable
větve mají právě jednu not-taken událost na příslušný cyklus. Každý
řetězec TRAP dostane čerstvý pointer v t; clobber $255 návratovým
výsledkem Fputs nezničí žádnou dále potřebnou hodnotu.

Originál `images/block2-pdf-042.png` zobrazen: Blanks opravdu obsahují
tři mezery, ne počet mezer odhadnutý z OCR. Title má 25 znaků;
NewLn je LF+NUL a následuje přímo za ním; Blanks mají tři mezery+NUL.
Po 15 instrukcích první fáze je báze na #13c. Title, NewLn, Blanks
jsou od báze posunuté o 0,25,27; další LDA je zarovnaná na #15c.
Před data se nikdy nepropadne: první fáze buď opakuje explicitní
JMP, nebo BZ skočí přímo k řádku 38. Žádné datum není vykonáno jako
instrukce. Výstupní řádek má 3+10·5=53 znaků a LF.

Komentář 1: `%` na začátku a prázdný řádek parser přeskočí
(`mmixal-20250620.w` 2598–2626); ostatní řádky jsou LABEL/OP/EXPR,
výrazy odděluje comma, zbytek je komentář. Pozdější explicitně
uvedené semicolon rozšíření nepovažuji za nemožné tímto úvodním popisem.
Komentář 2 rozlišuje pure octabyte a register number 0..255, nikoli
obsah registru. Jména t a L jsou konkrétně $255 a 500. Konvence
velkých/malých písmen je doporučení; parser dovoluje obojí.
Začátek komentáře 3 odpovídá GREG alokaci, dopovězené na další straně.

## File 43 / p35: GREG, base address, globální a lokální symboly

Konkrétní alokace 254..249 a alias mm jsou doloženy V0088. Nenulové
GREG se mají zachovat jako konstanty; nulové jsou proměnné. Není
tvrzeno, že hardware fyzicky znemožní přepsání nenulového GREG.
Skutečná primární definice `mmixal` 558–570 říká přesně tento kontrakt,
implementace 2694–2707 sdílí stejnou nenulovou hodnotu a pro nulu vždy
alokuje nový registr. Pro Program P jsou všechny čtyři hodnoty různé.

Dvouoperandové LDA vybere dostupnou bázi a byteový offset podle
`mmixal` 3006–3018. Všechny případy na stránce jsou konkrétně:
BUF+4=ptop+4; Title=base+0; Blanks=base+27; NewLn=base+25.
Tyto překlady nepotřebují −x a každá LDA je jedna ADDU immediate.
Všechny báze se za běhu Programu P zachovávají.

Normativní rozlišení jediného globálního významu a opakovaně
definovaných místních značek je správné. **Samostatně znovu otevřená
a rozhodnutá věta:** opakovaný globální LABEL nemusí vyvolat chybu,
zachová-li hodnotu i typ. To starý V0093 vůbec nedokládal.
`MMIX-C0017-identical-global-definition.md` dává čtyřřádkový
protipříklad a úplný guard pro oba originály 2013/2025; příslušné
bloky jsou byte-identical. Nezaměňuje se definice povoleného stylu
za pravdivé tvrzení o existujícím chybovém hlášení.

V0093 přesně dokazuje všechny tři skutečné cíle 2B/2F a trojici
`IS $10; BZ 2B,2F; IS 2B−4`: výsledkem je BZ $10,@−4. Při výpočtu
operandů ještě není aktuální label instalován, takže vlastní řádek
se nezapočítává; následná instalace mění backward symbol. F/B jsou
jen v operandu, H jen v LABEL, počáteční B má hodnotu 0; pravidlo
platí pro každou z deseti číslic. Primární definice `mmixal` 201–222
i pořadí `Scan operand` před `Define label` 2612–2615 to přímo potvrzují.

Historie byla cíleně doplněna: původní [Knuthův CASE SOAP III, 1958](https://archive.computerhistory.org/resources/access/text/2018/07/102784981-05-01-acc.pdf)
na file 3 děkuje Conwayovi za koncept program points, je datován
31. ledna 1958 a uvádí kompatibilitu s připravovaným UNISAP pro Univac.
Tištěná strana 4 / file 7 obsahuje týchž deset B/F program points.
PDF, text, SHA256 metadata a zobrazené acknowledgments jsou uloženy.
Tím je dobová existence a osobní atribuce skutečně podložena.
**Výslovná bibliografická výjimka:** originální UNISAP report No. 1009
z roku 1958 nebyl získán; přesné tvrzení o prvním zavedení v UNIVAC I
assembleru neuzavírám pouze ze sekundární bibliografie a kompatibility.

## File 44 / p36: segmenty, loader, výrazy, negativní počítadla

Pokračování o výhodě místních jmen je programátorská motivace, nikoli
nevyřčená empirická míra jejich používání. V0094 dokazuje všechny
intervaly: user/kernel po 2^63 bytech, user čtyři segmenty po 2^61,
počátky 0,#2000…,#4000…,#6000…. Žádná překrývající se adresa.
Primární doc 2789–2817 má privileged negative addresses a zbytek
popisuje jako právě tuto **konvenci**, nikoli vynucený obsah segmentů.
Předdefinované konstanty jsou přímo v `mmixal` 2015–2019.

Možnost pomalejšího přístupu k vyšším adresám je doložena konkrétní
adresní cestou, ne paušálním výkonovým tvrzením. Při page size 2^13,
b1=5,b2=6,b3=7,b4=8 a přípustných PTE/PTP vyžaduje poslední byte
text segmentu page index 2^48−1, tedy radix-1024 číslo s pěti číslicemi
a nenulovou nejvyšší. Čtyři PTP a jeden PTE jsou pět tabulkových čtení.
První byte data segmentu má page index 0, tedy přímý jeden PTE.
Takové přípustné tabulky a prázdná translation cache dovolují, aby
první cesta byla pomalejší; při cache hitu závěr vynucen není. To je
přesný rozsah slova „might“ (`mmix-doc` 2886–2910, 2960 a dále).

Zákaz assemble do Pool/Stack je deklarovaná načítací konvence kvůli
datům OS a register stack. Read-only text je zvolená konvence těchto
programů; P ji konkrétně splňuje, všechny jeho stores jsou v Data.
Nejde o zákaz veškerého self-modifying kódu v architektuře.

V0095 dříve pouze předpokládal loader kontrakt. Nyní je doplněna
skutečná implementace: nový paměťový chunk je calloc-nulovaný
(`mmix-sim` 747), každý obyčejný objektový tetrabyte se načítá přes
`mmo_load(loc,val): ll->tet ^= val` (940–951). Tím každý příslušný
byte dostane XOR všech příspěvků a nenahraná místa zůstanou nula.
Normativní definice `mmixal` 676–689 přesně souhlasí; runtime OS data
v Pool/Stack jsou výslovná výjimka již popsaná knihou. Nejde o tvrzení,
že by po zahájení programu samotné stores byly také XOR operace.

Oba aritmetické výrazy mají přesnou hodnotu D+1000 a 98, všechny
typy a konstanty jsou pure. Smysl negativních jj/mm byl dokázán
samostatnými stavovými invarianty V0089/V0091; nelze jej nahradit
jen komentářem, že se nula snadno testuje.

## File 45 / p37: rychlejší konverze, profil a začátek jazykového souhrnu

Výrok „division-by-10 není nejrychlejší“ nyní má vlastní svědectví pro
celý dosažitelný rozsah, nikoli jen odkaz na jinou kapitolu. Po ukončení
generování je n volné: jednou nastavíme `SET n,52429`. Namísto
řádků 48–49 (DIV+GET) lze v každé decimal iteraci použít:

```
        MUL     q,pk,n
        SRU     q,q,19
        4ADDU   r,q,q
        2ADDU   r,r,0
        SUB     r,pk,r
        SET     pk,q
```

Nechť staré pk=N, 0≤N<8192. `10·52429=2^19+2`, takže
`N·52429/2^19 = N/10 + 2N/(10·2^19)`. Dodatek je nezáporný a <1/10;
zlomková část N/10 je některá z 0,1/10,…,9/10. Proto přesně
`floor(N·52429/2^19)=floor(N/10)`. Součin je <2^29, tedy signed MUL
bez overflow. Dvě ADDU vytvoří 5q a 10q, SUB zbytek 0..9, SET nový
quotient. Stejný decimal invariant i všechny koncové testy zůstávají
platné; rR se dále nepoužívá, q a n jsou po generování volné.
Cena je 15υ místo 61υ za původní DIV+GET, jednorázově navíc 1υ.
Pro alespoň jednu cifru jde o přísnou úsporu. **Globální optimum se
netvrdí.** Odkaz §4.4 míří skutečně na Radix Conversion ve svazku 2;
zde žádný konkrétní nečtený algoritmus odtud nepřebírám.

V0096 je nově uzavřen přes `MMIX-C0016-program-p-mems.md` a úplný
uložený profil. T=9538, D=1803, všechny větve a υ součty souhlasí;
koeficienty μ musí být 10037 a 2803. Historický fyzický běh autora
se nedokazuje, ale všechny konkrétní numerické údaje jsou nyní
samostatně rozhodnuty. Pouhý správný součet dříve chybu dělení mezi
fázemi skrýval. Jediný nový malý součet použil existující prime
certifikát; žádný simulator a žádné opakované síto.

Jazyková pravidla 1–3 jsou normativní definice MMIXAL. Každý příklad
PRIME1, Data_Segment, Main, __, pâté začíná dovoleným písmenem;
„code value>126“ zde definuje syntaktickou třídu, nikoli Unicode
alphabetic category. Číslice na začátku dH/dF/dB jsou explicitní
výjimka pro lokální symboly, ne protiargument k definici globálního
symbolu. Full Unicode je v knize jazyková specifikace; samotná
referenční implementace `mmixal` 117–127 výslovně omezuje vstup na
bytes. Neprohlašuji, že by její parser uměl číst všechny Unicode
znaky, ani na něj nevznáším požadavek dodatečně implementovat tuto
deklarovanou širší jazykovou třídu.

V0097 dokazuje 65=#41='A', 39=#27=apostrophe a 31639=#7b97='算';
poslední Unicode přiřazení je již dříve doloženo primární tabulkou.
Tři apostrofy jsou otevření, znak apostrophe, uzavření. Decimal a hex
zápis reprezentují unsigned octabyte, nikoli signed decimal hodnotu.
String je seznam alespoň jednoho znaku bez newline/double quote;
všechny uvedené strings podmínku splňují. Rozdělení na již definovaný
symbol a future reference je rozdělení podle dřívějších definic v LABEL;
predefined rR, ROUND_NEAR, V_BIT, W_Handler a Fputs jsou výslovná
počáteční výjimka, tabulky `mmixal` 1990–2084 je obsahují s odpovídajícími
hodnotami. Pokračování pravidla je až na další straně, která zůstává
samostatným budoucím blokem.

## Výsledek rozsahu

File 41,42,44,45 mají úplné substantivní argumentové pokrytí,
včetně rozhodnutého rozporu C0016 na 45. File 43 má všechny technické
výroky rozhodnuté včetně C0017, ale zachovává výše přesně pojmenovanou
historickou bibliografickou výjimku. Staré checked V0093 nezakrylo
nově nalezenou chybnou větu o globálních symbolech; tato dodatečná
položka je evidována jako R0005 s přímou vazbou na C0017.

Žádný z těchto výsledků neuzavírá zbylé IEEE či cvičební mezery jinde
v knize. Další celý rozsah je file 46/p38, zbytek jazykového souhrnu.
