# Souvislý průchod §2.4 — 5. listopadu 2026

X0980. Přímo přečteny všechny původní strany424–434 a příslušné
odpovědi605–607, všech15úloh, obě tabulky a oba diagramy.
Přezkoušeny celý general-proofs.md, algorithms.py a nezávislá
orákula check_algorithms.py. Přijaté úspěšné běhy se neopakovaly.
C0061 je znovu potvrzen na606; nový nález nevznikl.
Úlohy4/12/15 uzavřeny s konkrétními bibliografickými výjimkami.
Historický počet nejméně šesti nezávislých objevitelů na433
zůstává nedoložený: hlavní text má nadále partial.

## Model, tabulky a algoritmy A/B/C

Ověřujeme model výslovně definovaný knihou; nejde o úplný
standard každého dialektu COBOL. Kniha vylučuje formáty a velikosti
dat z této sekce. Pravidlo(a) vyžaduje stejné hladiny sourozenců,
(b) kvalifikaci podposloupností jmen předků a (c) možnost
jednoznačně pojmenovat každý výskyt. Druhé CC příkladu(2)
nelze takto odlišit od vnořeného CC; první CC má kvalifikátor BB.
DAY OF SALES a NAME OF SHIPPER v příkladu(1) jsou jednoznačné.
Přesun odpovídajících dat spojuje stejná jména, nezaměňuje měsíc
za den, přestože fyzické pořadí se liší.

Všech15řádků pětice PREV/PARENT/NAME/CHILD/SIB na428 a všech8
symbolových LINK odpovídají vstupu427. Oba výskyty změny D na
hladinu6 opravdu poruší stejné hladiny sourozenců. Normalizace
prvního stromu na1,2,3,3,2,2,3 zachová celý strom.

A: zásobník obsahuje sentinel(0,NULL) a cestu k poslední položce.
Aktivní SIB jsou nulové. Při růstu hladiny vznikne první dítě;
při poklesu se dokončí vyšší podstromy, rovná hladina je minulý
sourozenec. Přeskočení pod požadovanou hladinu dokazuje porušení(a).
Kladná skutečná hladina neodebere sentinel. PREV a LINK jsou
přesně řetězce předchozích výskytů. Každý vrchol se jednou vloží
a nejvýše jednou odebere: Θ(N+1) času při zadaných symbolových
odkazech a konstantní alokaci. Vstupní pořadí je preorder.

B: po PREV se projdou všichni kandidáti prvního jména, po PARENT
se hledají nejbližší možné kvalifikátory. Nejbližší shoda leží
stejně nízko nebo níže než libovolná jiná úspěšná volba a neztratí
možnost pokračovat výše. Q rozlišuje žádnou/jedinou shodu;
druhá shoda je správně chyba. Nekvalifikované jméno projde B3
ihned. Diagram40 má všechny přechody shodné s textem.
Známá změna rovnítka v B5 na šipku zpřesňuje přiřazovací notaci;
slovo „set“ již záměr určuje.

C: odpovídající položky mají stejnou úplnou relativní cestu jmen
a alespoň jeden konec je list. Je-li list již kořen, cesta má
délku0. Jinak se rekurze rozpadne podle společných jmen přímých
dětí. Jedinečnost jmen sourozenců plyne z platnosti vstupního
modelu; C nemusí napravovat libovolnou tabulku porušující(c).
C2 vstoupí do první dvojice dětí, C3 hledá partnera Q, C4 projde
další P nebo vrátí oba rodiče; C5 vrátí původní kořeny.
C3 má společnou úplnou cestu od rodičů, i když aktuální poslední
jména ještě nesouhlasí. Diagram41 odpovídá každé větvi.
Indukce podle velikostí podstromů dokazuje všechny dvojice jednou.
V příkladu(4) jsou přesně B3→B5 a G4→G8.

## Všechny úlohy a úspory polí

1–2 jsou preorder a amortizovaný lineární čas A výše.
3: A5' odebere vrcholy, dokud zbývající předek nemá menší hladinu.
Poslední odebraný je předchozí sourozenec; nerostoucí hladiny
sourozenců jsou přesně PL/I varianta. Příklad1,3,5,4,2 odpovídá
1,2,3,3,2. Sentinel0 zajišťuje zastavení pro kladné hladiny.

4: jednoznačné pojmenování je ekvivalentní jednoznačné úplné
kvalifikaci. Při minimální hloubce nejednoznačné položky má
rodič už jednoznačnou kvalifikaci, takže jiný stejnojmenný
kandidát je pod týmž rodičem. Proto stačí pro nový výskyt
ověřit oba směry „rodič jednoho je předkem druhého“.
Virtuální rodič NULL je předkem všech. PARENT a aktivní zásobník
obě podmínky zjistí; staré dvojice se nezmění. Poznámka, že B
nepojmenovatelný výskyt odmítne při použití, je správná.

5: místo čítače k jde K po RLINK neprázdného seznamu
kvalifikátorů; K=T při každém kandidátovi, poslední je rozpoznán
RLINK(K)=NULL a jméno je INFO(K). Všech pět záměn605 úplných.
6: první průchod vyžaduje bezprostřední rodiče a nejvyšší jméno
bez rodiče, druhý původní B se použije jen při absenci úplné shody.
Při odlišných jménech sourozenců je úplná shoda jednoznačná.
A,A.A,A.A.A u řetězce tří A jsou správné PL/I odkazy.

7: všech sedm MOVE je správně podle jmen: MONTH/DAY/YEAR,
ITEM/QUANTITY/PRICE/TAX. NAME/ADDRESS se nepřenesou, protože
jejich bezprostřední skupiny BUYER a SHIPPER nesouhlasí.
8: rovnost expanze s jediným MOVE kořenů nastane právě při
alespoň jednom listovém kořeni; nejde o náhodnou rovnost
bajtového účinku dvou různých příkazů. Zadání výslovně odkazuje
na definici knihy. IBM COBOL1964 má další syntaktická omezení.
9: úplný indukční důkaz C je výše, s navrácením P=P0,Q=Q0.

10: odstraněné NAME se rozpozná členstvím v PREV řetězci jména,
nebo rovností prvních výskytů obou řetězců. Při rostoucích adresách
stačí sestupovat větším ukazatelem; stejné jméno nemůže minout
menší výskyt. NULL není shoda dvou jmen.
11: SIB1 zrychlí jedinou dereferenci. Seřazení každé rodiny
podle NAME a slučovací průchod zlepší párování z d1*d2 na d1+d2.
Součet přes dosažené dvojice je O(Nu+Nv). Přestavba rodin se
provede při konstrukci; ostatní fyzické pořadí dat je samostatné.
Nejde o doklad univerzálního praktického časového poměru.

12: každý podstrom je souvislý preorder interval a jeho poslední
vrchol je list. Proto SCOPE(P)=P právě u listu a
Q<P≤SCOPE(Q) přesně charakterizuje striktního potomka.
Všech15hodnot tabulky434 souhlasí. B'' vyhledá po PREV první
interval obsahující S, tedy nejbližšího předka daného jména.
Přenáší se hladový důkaz B; používají se jen PREV a SCOPE.
Křížový odkaz350 má výlučný konec místo zahrnutého, rozdíl je
jedna velikost záznamu c. Obě definice jsou výslovné.
Poznámka o PL/I říká, že jednoduchá změna testů B se nepřenese
beze změny; netvrdí nemožnost získat rodiče z celé tabulky.
Např. rodič P je největší Q<P se SCOPE(Q)≥P.

13: běžné uzavření zásobníkové položky nastaví SCOPE=Q−1 správně.
EOF ovšem posílá L=0 až do A7 přes nebezpečnou A5; viz C0061 níže.
14: zásobník párů nahrazuje PARENT, první dítě je P+1,
další sourozenec SCOPE(P)+1 pouze uvnitř intervalu rodiče.
Test jména je přes PREV. V C3'/C4' je rodič vždy již na zásobníku;
samotný listový kořen jde přímo přes C2' do C5', bez čtení vrcholu.
Indukce C tedy platí i s pouhými dvěma poli.

15: vytištěná odpověď není. Přijaté úplné vlastní řešení ukládá
hladinu do zatím nulového SIB aktivního vrcholu, PARENT je
předchozí zásobníková položka. Odstranění vyšší hladiny obnoví
SIB=0, nalezenému sourozenci nastaví SIB na novou položku.
EOF vynuluje zbývající aktivní SIB. Indukcí je cesta TOP přesně
původní zásobník, všechna konečná pole shodná s A.
Lineární čas, konstantní pomocná paměť mimo výslednou tabulku.

Úspory v hlavním textu: rodiče lze najít po rodině až k označenému
poslednímu SIB; při monotónních adresách pozná nit pokles adresy.
CHILD stačí jako bit, případně sousední PARENT s obvyklým testem
konce tabulky. NAME je nahraditelné podle10. Jednotlivé úspory
nelze bez další konstrukce libovolně složit; úplný příklad dávají
12–14. Formulace „virtually minimum“ je hned kvalifikována úlohou11,
nikoli tvrzení dokázané absolutní optimality.

## C0061 a známé opravy

Na legálním vstupu1A je po skončení zásobník(0,NULL),(1,1).
I když dáme EOF správné Q=2 a přeskočíme nežádoucí A3,
A5 odstraní skutečný uzel a nastaví SCOPE(1)=1. Pak při L1=L=0
odstraní také sentinel, vyžádá SCOPE(NULL)=1 a vrchol prázdného
zásobníku. Pozdní test A7 to nezachrání. Stejný problém nastane
po každém konečném neprázdném platném vstupu.
Oprava přímo na EOF: bez alokace odebrat pouze kladné hladiny,
nastavit jejich SCOPE na poslední skutečnou adresu a skončit.
Starý build_scope tuto opravu výslovně obsahuje.
Přesná chybová lokace je606; správný původní A na428–429 se
neznačí červeně kvůli chybné pozdější úpravě.

Čerstvé čtyři vrstvy potvrzují15různých oprav. Původní obsahové
vady X0546 mapujeme pouze na426(zaměněné pořadí cílových jmen),
430(index j<n vede k nedefinovanému A_n) a433(index i místo j).
Doplnění „complete“ na431 zesiluje pravdivý původní invariant,
„or both“ na430 vyjasňuje již inkluzivní C2; nejde o další vadný
výpočet. Typografie432, terminologie428 a doplnění Lawsonových
stran433 se oddělují od matematických vad.
Přejmenování B'/B''/C' a později ztracené čárky neopravují
původní chybné instrukce odpovědi13. Záznam607-6 je už §2.5.
C0061 mezi současnými opravami nalezen nebyl.

## Historické meze a další stav

Převzaty přesné přímé kontroly PL/I1965:25–27,39,63–64;
COBOL1964:14,32–33,85–86; Conway1963:402–404 včetně diagramů.
Netvrdíme nové úplné čtení celých manuálů. Conwayův dodatek
dokládá jeho pozdější seznámení s Lawsonovou podobnou prací,
ne počet šesti nezávislých objevitelů.

Rychlé nové hledání přesné fráze a Dahma nedalo doklad pro šest
osob ani datovaný Dahmův přínos1965. Autorův Lawsonův OCR upload
a Conwayova kopie pouze potvrzují již uložené zdroje.
Nově získán archivní text M. E. D'Imperio, Data Structures and
Their Representation in Storage, CHM102734157:81skenovaných stran.
Přímo přečten jen titul, bez data; PDF nemá použitelnou textovou
vrstvu. Celou obtížně čitelnou bibliografickou odbočku nyní
přeskakujeme, není důkazem uvedeného počtu ani Dahmova roku.
URL a SHA256 v chm-data-structures-retrieval.json; záznam hledání
v multilinked-history-search.json.

Výslovně přeskočeno: přesná facsimilní kolace Lawsonových dvou
stran a jeho globální prvenství; Dahmova osobní atribuce a rok;
Wiseovy osobní příspěvky4/15; úplný standard COBOL1961 oproti
přijatému omezenému srovnání IBM1964.
Počet nejméně šesti nezávislých autorů je samostatné kvantifikované
faktické tvrzení bez identifikovaných šesti osob. Ponecháno partial
v hlavním textu a pokrytí433, nikoli prohlášeno za ověřenou citaci.

Všech15úloh je checked s výjimkami; C0061 má samostatnou kartu.
Celé424–432,434,605–606 jsou pokryty;433 má výše uvedenou faktickou
mezeru a607 má dosud neprošlý obsah následujícího §2.5.
Pokračuje dynamická správa paměti na435.
