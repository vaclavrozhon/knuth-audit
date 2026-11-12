# Souvislý průchod §2.3.1 — 5. listopadu 2026

Rozsah X0970: první dotisk 1997, tištěné strany 318–334 a odpovědi
564–571 (soubor +15). Originály byly obrazově přečteny v aktuálním
souvislém průchodu, včetně diagramů, četností MIX instrukcí a všech
37 zadání. Na334 je navíc zkontrolován začátek §2.3.2, definice a obě
kresby převodu lesa. Odpovědi §2.3.2 na571 zatím nejsou uzavřeny.

Podrobnými důkazy zůstávají `parallel/tree-traversal/notes/traversal-proofs.md`,
`tary-generalization.md`, `height-erratum-candidate.md` a kořenové revize
`traversal-block-root-review.md`, `traversal-findings-root-review.md`.
Jejich výpočty byly přečteny a porovnány s originály; přijaté konečné
strojové testy se neopakovaly. Tento zápis není tvrzením o celém svazku.

## Průchody a reprezentace

T má silný invariant s libovolným původním prefixem zásobníku, nikoli
jen s prázdným zásobníkem. Levá rekurze jej zachová, následuje vyjmutí,
návštěva a pravá rekurze. S hledá nejlevější uzel pravého podstromu,
nebo použije již hotovou pravou nit. Jeho jednotlivé volání nemusí být
konstantní; součet pro úplný průchod je lineární. Hlavička se účastní
počátečního a závěrečného kroku, včetně prázdného stromu.

Všechny odkazy příkladového stromu a všechny uvedené pořadové posloupnosti
odpovídají A(B(D,∅),C(E(∅,G),F(H,J))). V diagramu322 skutečně chybí
obyčejná šipka E→G; jde o známou opravu z15.7.1997. Rozlišení nitek
porovnáním adres vyžaduje nižší adresu všech předků, včetně hlavičky,
pokud se použije hlavičková reprezentace. Je to podmíněná možnost
reprezentace, nikoli záruka pro libovolné rozmístění uzlů.

Původní definice paměti v MMIX fasciklu, tištěná4/soubor12, přímo
potvrzuje ignorování nejnižších bitů při přístupu k wyde/tetra/octa.
Obraz je uložen jako `sources/sequential-2026-11-05/mmix-addressing-p4.png`.
Tím je ověřena poznámka325 o možnosti využít zarovnané ukazatele pro tag;
nejde o prohlášení, že každá bajtová adresa musí být sudá.

Pro neprázdný strom dávají četnosti Programu T čas15n+a+4, spojová
varianta30n+a+4 a S čas11n−a+7. Z2n slotů a n−1 hran plyne a+b=n+1;
reflexně symetrické rozdělení proto má E(a)=(n+1)/2. Čas nezahrnuje práci
VISIT a jeho návrat, ale zahrnuje volací JMP. Dosavadní kvalifikace
n>0 je nyní samostatně dohledatelná jako C0092 níže.

Vkládání I přesměruje právě jedinou starou předchůdcovskou nit
nejlevějšího uzlu původní pravé větve. Maska(l,r) v preorder jednoznačně
vyplňuje otevřené sloty. Lemma P vyjadřuje jejich kladný počet až do
posledního uzlu; první nulový prefix součtu f odděluje levou větev.
Kopie C vytváří pravou rezervu před levou, ale preorder vyplní levou
dříve. Invariant požaduje prázdné obě větve aktuální rezervy; původní
pravá větev cílového U zůstane zachována. U prázdného zdroje se nic
nekopíruje. Zdroj a nově alokované cílové uzly musejí být disjunktní.

## Cvičení a rozsah přijatých důkazů

1–10: pořadí listů, obrácení postorder, lexikografické adresy, bijekce
zásobníkových permutací a stromů, rekonstrukce z dvojic pořadí, četnosti
T a maximální zásobník jsou doloženy obecnou indukcí. U rekonstrukce
pracujeme s identitami uzlů; pouhá opakující se INFO nestačí. Pozdější
doplnění odlišných značek je výslovná kvalifikace tohoto významu.

11: h(T)=max(1+h(L),h(R)), g0=1, gk=1/(1−z*g(k−1)). Substituce
u=z(1+u)^2 a Lambertova řada dávají přesný koeficientový vzorec.
Mellinovy rezidua, přenos v komplexní oblasti a dělení Catalanovým
číslem dávají +11/24*sqrt(pi/n); člen1/n se vyruší. **C0050 se týká
chybného errata1999, nikoli správné původní asymptotiky na565.**
Převod z lesní výšky h na výšku stromu h+1 s n+1 uzly tuto opravu
nezachrání. Dřívější přesné hodnoty ani obecný důkaz se nyní nerozšiřují
na celý obsah všech citovaných článků.

12–18: preorder mění místo návštěvy, postorder13 sleduje poslední
navštívený kořen pravé větve. Každý uzel se uloží nejvýše dvakrát.
Počet nulových odkazů zahrnující vnější T je n+1 i pro n=0.
Double order a všechny jeho čtyři kombinace fáze a tagu fungují i na
hlavičce. Soukromé připsání řešení13 Araújovi1976 se výslovně přeskakuje;
matematická úloha13 je uzavřena.

19: obecný důkaz hledání rodiče F i amortizace je přijat. **C0049 zůstává
candidate**, protože prozaický návod pro postorder následníka neříká,
zda kořenový konec ošetří volající. Singleton při doslovném použití
vrací sebe místo HEAD. Doplnění Q=HEAD je jednoznačná funkční oprava.

20: **C0048 confirmed**, singleton stojí12u, nikoli11u. Obecné opravené
součty jsou7n+11a−6 a7n+26a−21 pro n>0. Rozdíl n−a+1 je právě počet
nulových levých odkazů. Nejde o výsledek drahého hledání.

21: U dočasně propojí pravý kraj levé větve s rodičem a při druhém
setkání nit odstraní; R rozezná tento návrat. W rotačně projde levou
a pravou část a obnoví všechny původní odkazy. Silný invariant začíná
s P=T,Q=X a končí s P=X,Q=T. Každý ze tří výskytů uzlu leží v jiném
zbytku modulo3; každá třetí návštěva proto pokryje všechny uzly a
vzdálenost sousedů takového průchodu je≤3. Drobné chybné zdůvodnění
parent/child je odděleno jako C0093. Matematická úloha21 je uzavřena;
nepřečtené části historických článků a rozporné datum C0090 jsou
samostatně evidovány a nezastavují tuto matematickou kontrolu.

22: **C0047 confirmed**, CMP5 v poli(1:2) porovnává nulové bajty
indexu s RLINK(Q), nikoli P s RLINK(Q). Dvouuzlový strom přeskočí levý
list. Ruční důkaz platí pro každý MIX radix64–100. Přijatá oprava přes
I4 zachovává A,X,I1–I3;1454 skutečných MIX běhů bylo dříve provedeno,
nikoli v tomto průchodu znovu spuštěno.

23–31: ověřeny obě orientace vložení, nejmenší tříuzlový protipříklad
inorder masek, úplné uspořádání tříd ekvivalentních stromů, double-order
stopa délky2n, invariant R, kopie, vytváření nitek a bezpečné uvolňování
uzlů. U L musí být další uzel spočten před přepsáním starého nulového
odkazu. Morrisova dočasná nit je nejprve odstraněna a teprve potom
obnovena jako trvalá. U X se S(P) spočte před vrácením P do AVAIL.

32: **C0046 zůstává candidate**. Pokud „single node“ znamená již
inicializovaný izolovaný list, LLINK(Q)=null a postup funguje; jinak
stará hodnota LLINK(Q)=P vytvoří cyklus. Nelze bez rozhodnutí o kontraktu
označit prokázanou vadu libovolně inicializovaného vstupu za potvrzenou
vadu zadání s inicializovaným listem.

33–37: alternativní L vždy obsahuje preorder následníka. Při kopii
stačí dva přímé přechody; obecné pravé vložení musí hledat konec levé
větve. Oddělení podstromu mění jen jeho koncovou pravou nit a původní
rodičovský slot. Vlastní t-ární zobecnění obsahuje indukční algoritmy,
gk=1/(1−z*g(k−1)^(t−1)), G=1+zG^t a slotový počet(t−1)n+1.
Není tvrzeno, že na širokou průzkumnou úlohu35 existuje jediný konečný
seznam všech možných zobecnění. Uspořádání není dobré již pro jednu INFO:
B>F(B)>F²(B)>..., kde B má levý list a F připojí argument jako pravou
větev nového kořene. Sousední bloky potomků potřebují1+2(n1+n2)=n+n1
slov, tedy n..2n−1 pro n>0; příklad má11 místo18, prázdný strom0.

## Dvě nyní samostatně evidované drobnosti

**C0092 — candidate, nízká závažnost:** samotná doba pro prázdný vstup
je určitá. Program T provede pouze LD5(2u), J5Z(1u), potom dosáhne DONE.
ENT6 na325 má četnost0, nikoli vytištěnou1. Pro n=a=0 tedy T i spojový
T trvají3u místo4u. Stejně program U na568 skončí po LD5/J5Z za3u,
zatímco jeho polynom21n+6a−3−14b dává−3u. Optimalizované formule na567
také předpokládají n>0, nezávisle na C0048.

Na324 kniha výslovně požaduje zpracování prázdných stromů. Na326 ale
o něco později výslovně říká „assuming that n≠0“ u spodní meze a.
Není rozhodnuto, zda má čtenář tuto kvalifikaci vztáhnout i na celý
časový rozbor. Proto jde o kandidáta na doplnění domény, nikoli chybu
funkce algoritmu. Přesné řešení je formulovat všechny tyto polynomy
pro n>0 a zvlášť uvést3u pro n=0. Hlavní text zůstává partial pro tuto
jedinou konkrétní nejistotu, nikoli kvůli nedostupným citacím.

**C0093 — confirmed, nízká závažnost:** věta na568 tvrdí, že po sobě
jdoucí x_j,x_(j+1) v triple order jsou vždy rodič a dítě. Singleton
má posloupnost(P,P,P). P není vlastním rodičem ani dítětem. Přesně
platí: oba výskyty označují stejný uzel, nebo sousední uzly stromu.
Oprava přidáním možnosti rovnosti zachovává závěr o vzdálenosti≤3
i celý algoritmus W. Jde pouze o chybu jedné věty důkazu, ne o vadný
průchod ani nový závažný algoritmický nález.

Obě původní pozorování již byla v `traversal-proofs.md`; nyní dostávají
samostatné karty, aby nebyla ztracena v prose. Čtyři čerstvé vrstvy errat
z5.11.2026 prohledány po stránkách i podle15n,30n,21n,empty,nonempty,
parent/child a triple. Výpis a hashe jsou v `traversal-errata-extract.json`.
Relevantní oprava žádné z obou vět nenalezena. Tištěný exemplář ani
prvenství nejsou doloženy. Žádné hlášení se nepřipravovalo ani neposílalo.

## Bibliografické výjimky a mapa

Výslovně se přeskakují plné Perlis–Thornton1960,CACM3,195–204,
a Blikle1966,Bulletin14,203–208, včetně přesného připsání a tvrzení
o šesti addressless pořadích. Převzaté X0814 dokládá první strany
Morris1979:197, Robson1973:12, Lindstrom1973:47, Dwyer:143. Ty přímo
dokládají uvedené jádro metod; Morris198–200, Robson13–14,
Lindstrom48–51 a Dwyer144–145 se nedávají za přečtené.

C0090 zůstává bibliografický candidate: Dwyerova hlavička a údaje
vydavatele podporují1974, ale pozdější původní rejstřík uvádí1973 pro
celé číslo2(5). Chybí obálka/tiráž, datum přijetí nic nerozhoduje.
Připsání Araújovi1976 a Fergusonovi se přeskakuje. Swainsonova
citace byla dříve ověřena na původních193–195; mluví o zoologickém
třídění. Úprava slovosledu2024 je skutečná známá nepřesnost citace330.

Společná X0415 má nyní přesné obsahové lokace310,322,328,329,330,562,
565,568,569. Nezahrnuje pouhou sazbu, doplnění zřejmé identity uzlů331,
LOC(T)=HEAD ani nesprávnou náhradu asymptotiky C0050. Nové karty C0092
mapují325,326,567,568; C0093 pouze568. C0046 pouze570,C0047 pouze568,
C0048 pouze567,C0049 pouze566,C0090 pouze567. C0050 má565 jako související
správnou původní stránku, ne jako místo chyby v knize.

Celé stránky319–324,327–331,334,564–565,569 jsou doloženy s uvedenými
nálezy a bibliografickými výjimkami. 325–326 zůstávají partial kvůli
C0092;332–333 kvůli dosud otevřenému významu odpovědí19/32;566 kvůli
C0049,567 kvůli C0090/C0092,568 kvůli C0092 a570 kvůli C0046. 571 čeká na následující
část odpovědí. Technické úlohy13 a21 lze uzavřít;19 a32 zůstávají partial.
