# Tableaux39: dopředný algoritmus, všechny malé části a příklady

Zadání70–71/file81–82, odpovědi613–614/file624–625; původní sazba
všech čtyř stran zobrazená. Dopředně se používá oprava C0006:
po vodorovném přesunu se vrací do S2′. Inverzní hranice má samostatný
C0020. Protipříklady se neopakují. Původně otevřený geometrický invariant P0594 je nyní úplně doložen
v tableaux-proof-39-inverse-invariant.md. Níže uvedená historie mezery
zůstává pro dohledatelnost; dnešní stav je checked a zahrnuje jednoznačnost(e).

## P0583: invariant opraveného S′ na skutečné aktivní oblasti

Před zpracováním u=(i,j) jsou uspořádané všechny buňky za u
v řádkovém lexikografickém pořadí: nižší řádky a buňky napravo
v řádku i. Oblast je uzavřená vůči pohybu doprava/dolů.
Vyjměme K=P_ij a sledujme díru. Při nesplněném testu K<oba
sousedé přesuneme do díry menšího souseda napravo/dole;
chybějící soused je∞.

Přesouvané hodnoty podél cesty striktně rostou: následující sousedé
ještě nebyli na cestě a v původní uspořádané oblasti jsou větší
než právě přesunutá hodnota. Přesun menšího zachovává vztah proti
druhému sousedu. Horní a levý soused nové díry, pokud jsou aktivní,
mají nejvýše právě přesunutou hodnotu: buď leží na cestě a nesou
dřívější hodnoty, nebo původně předcházeli právě uvolněné buňce.
Každá další přesouvaná hodnota je tedy větší než oba tito sousedé.
Relace mezi označenými buňkami mimo díru zůstávají platné.

Počáteční u nemá horní/levý soused v aktivní oblasti. Každá
skutečně přesunutá hodnota je<K, protože přesun nastane jen při
nesplněném S2′. Když test uspěje, vložení K zachová menší horní/
levé i větší pravé/dolní sousedy. Uspořádaná oblast se rozšířila
o u. Čísla se zachovávají: jen se posunou po jednoduché cestě
a K se vloží na její konec.

## P0584: celý průchod, hranice a dopředný náklad

P1 zpracovává buňky v opačném pořadí; indukce P0583 začíná prázdnou
oblastí a končí standardním tableau stejného tvaru. Cesta je konečná,
protože souřadnice jen rostou. V koncové buňce jsou vnější sousedé∞
a konečné K zastaví; návrat do S2′ je zde nezbytný.

Ze startu(i,j) do(r,s) je r−i+s−j přesunů, nejvýše H_ij−1.
Změn Q v P3 je s−j+1, tedy nejvýše počet přesunů+1. Celý průchod
má O(N+Σ(H_ij−1)) aritmetických operací/porovnání a O(N) buněk
pro P,Q. Součet H−1 je Σ_i binom(λ_i,2)+Σ_j binom(λ′_j,2):
počítá dvojice ve stejném řádku nebo sloupci, nejvýše binom(N,2).
O(N²) je ostré na jediném klesajícím řádku s binom(N,2) přesuny.
Prázdný tvar znamená prázdný průchod; singleton se nezamění.

P3 čte pouze Q napravo v témže řádku, které už byly stanoveny.
Ještě nenavštívené Q tedy nemusí mít známé hodnoty; lze je pro
jednotný popis inicializovat nulami bez změny výsledku.

## P0585: část(c), obě meze a počet možností

Pišme b_ik=λ′_k−i a r_ik=λ_i−k. Pro j≤k<s:

    Q′_ik=Q_i(k+1)+1≤λ_i−(k+1)+1=r_ik,
    Q′_ik≥−(λ′_(k+1)−i)+1≥−(λ′_k−i)=−b_ik.

Terminální Q′_is=i−r je nekladné a r≤λ′_s, tedy
−b_is≤Q′_is≤0≤r_is. Ostatní hodnoty se nemění. Nově zavedená
buňka má tytéž meze, takže indukcí platí všude.
Interval celých čísel[−b_ij,r_ij] má přesně b_ij+r_ij+1=H_ij
možností. To samo ještě nedokazuje vznik všech jejich společných
voleb; tento silnější bod patří do39(f).

## P0586: část(a), jediný řádek a hodnotově indexované b

Jde o vkládání klíčů zprava do setříděného pravého úseku.
Každá menší hodnota z úseku se při vložení K posune doleva;
P3 s ní přenese její Q a zvýší je o1. Přibyla jí právě jedna
větší hodnota původně vlevo, totiž K. Nové K dostane Q=0,
protože všechny zpracované klíče původně ležely vpravo.

Indukcí Q připojené k hodnotě v udává počet větších původních
předchůdců v dosud zpracovaném suffixu. Po dokončení P=(1,…,N)
proto Q=(b_1,…,b_N) v definici§5.1.1. Nejde o tabulku
indexovanou původními pozicemi.

## P0587: část(b), jediný sloupec a pozičně indexované C

Před krokem v řádku i se původní a_i ještě nezměnilo; nižší
suffix je setříděn. Svislé vkládání posune K=a_i o počet menších
původních následníků C_i=c_(a_i) z§5.1.1–7. Konec je r=i+C_i.
P3 se s=1 nemá žádný posun Q, jen Q_i1=i−r=−C_i.
Pozdější kroky v horních řádcích tento Q_i1 nemění.
Odpověď správně používá velká C_1,…,C_N; sazba613 potvrzuje
odlišnost od malých hodnotově indexovaných c.

## P0588: všech osm kroků obrázku70 a konečný pár71

Počáteční pole je[7 8 5;1 6 4;3 2]. D je dolů, R doprava,
„–“ prázdná cesta. Každý následující vytištěný mezistav vzniká
posunem uvedeného K po zapsané cestě; tabulka uvádí i všechny změny Q.

| Start | K | Cesta | Konec | Nové položky Q |
|---|---:|---|---|---|
| (3,2) | 2 | – | (3,2) | Q32=0 |
| (3,1) | 3 | R | (3,2) | Q31=1,Q32=0 |
| (2,3) | 4 | – | (2,3) | Q23=0 |
| (2,2) | 6 | D | (3,2) | Q22=−1 |
| (2,1) | 1 | – | (2,1) | Q21=0 |
| (1,3) | 5 | D | (2,3) | Q13=−1 |
| (1,2) | 8 | DR | (2,3) | Q12=0,Q13=−1 |
| (1,1) | 7 | DDR | (3,2) | Q11=1,Q12=−2 |

Při K=8 se porovnají pravá4 a dolní3, potom pravá5 a dolní6;
přenesou se3 a5. Při K=7 se přenesou1,2,6. Konečný pár je

    P=[1 3 4;2 5 8;6 7], Q=[1 −2 −1;0 −1 0;1 0].

Jde o kontrolu konkrétního příkladu; obecnou bijektivitu
nenahrazuje několik úspěšných průchodů.

## P0589: část(d), právě dva vstupy bez enumerace permutací

Pišme původní pole[a b;c d] a požadované Q=[0 −1;0 0].
Q21=0 nutí c<d. Po kroku(1,2) je Q12 buď0, nebo−1;
druhá možnost nastane právě při b>d. Poslední krok má dvě možnosti:

- Konec ve sloupci1 vyžaduje z Q11=0 řádek1, tedy žádný přesun.
  Q12 zůstává−1, proto b>d a a<c<d<b. Vyjde[1 4;2 3].
- Konec ve sloupci2 vyžaduje z Q12=−1 řádek2. Z Q11=0 plyne
  dřívější Q12=−1, tedy b>d. Pole před posledním krokem je
  [a d;c b] s c<d<b. Sift začne dolů přes c a do(2,2) dojde
  právě při a>b. Tedy c<d<b<a a vstup je[4 3;1 2].

Ostatní koncové souřadnice nesplní požadované Q. Výsledná P jsou
[1 3;2 4] a[1 2;3 4], se stejným Q. To dokazuje úplnost
odpovědi i skutečnost, že samotné Q nestačí k inverzi.

## P0590: část(e), celý šestnáctikrokový dopředný doklad

Vytištěný návrh původního pole je

    [12 10 8 14 15 11;9 13 7 1;6 4 5;16 3;2].

Každý dopředný krok je níže; Q se mění podle ověřeného P3
a uvedených koncových souřadnic.

| Start | K | Cesta | Konec |
|---|---:|---|---|
| (5,1) | 2 | – | (5,1) |
| (4,2) | 3 | – | (4,2) |
| (4,1) | 16 | D | (5,1) |
| (3,3) | 5 | – | (3,3) |
| (3,2) | 4 | D | (4,2) |
| (3,1) | 6 | DR | (4,2) |
| (2,4) | 1 | – | (2,4) |
| (2,3) | 7 | R | (2,4) |
| (2,2) | 13 | RD | (3,3) |
| (2,1) | 9 | RDD | (4,2) |
| (1,6) | 11 | – | (1,6) |
| (1,5) | 15 | R | (1,6) |
| (1,4) | 14 | D | (2,4) |
| (1,3) | 8 | D | (2,3) |
| (1,2) | 10 | DDD | (4,2) |
| (1,1) | 12 | DDDR | (4,2) |

Před zpracováním prvního řádku jsou nižší řádky
[1 3 5 7;2 6 13;4 9;16]. To kontroluje delší závěrečné cesty.
Konečný P je[1 3 5 7 11 15;2 6 8 14;4 9 13;10 12;16]
a Q je[−2 −3 −1 −1 1 0;3 −2 −1 0;0 −1 0;−1 0;0].
Je doložena existence uvedeného vstupu a všechny jeho hodnoty.
Jednoznačnost závisí na obecném bodu(f), vymezeném v P0594.

## P0591: strom hintu a každá hrana vytištěného příkladu

Pro úplné standardní tableau má každá buňka kromě(1,1) horního
nebo levého souseda; vybere většího. Součet souřadnic se zmenšuje,
tedy všechny cesty dosáhnou(1,1). Jde o orientovaný strom s N−1
hranami. Chybějící soused může být0, protože štítky jsou kladné.

V příkladu(e) pět netriviálních buněk prvního řádku ukazuje
doleva a čtyři další buňky prvního sloupce nahoru. Zbylé hrany:

    (2,2)→(1,2), (2,3)→(2,2), (2,4)→(2,3),
    (3,2)→(2,2), (3,3)→(3,2), (4,2)→(4,1).

Rozhodují páry(2,3),(6,5),(8,7),(4,6),(9,8),(10,9).
Tím je ověřeno všech15 hran. Po částečné inverzi již celé P
není standardní a globální strom potřebuje aktivní hranici C0020.

## P0592: každý kandidát a kód počátečního příkladu614

Z prvního řádku Q v(e) jsou kandidáty(3,1),(4,2),(2,3),(2,4),
(1,6). P0591 dává kódy DDQ, DDDRQ, RDRQ, RDRRQ, RRRRRQ.
Sloupec5 má Q15=1 a kandidáta nedává. V pořadí D<Q<R je první
DDDRQ: jeho třetí D předchází Q v DDQ, zbylé kódy začínají R.
První volba je tedy skutečně(4,2).

## P0593: pomocný posun má inverzi a podmíněný počet je správný

Je-li správný konec(r,s) znám, P3 lze obrátit:
Q_i(k+1)=Q′_ik−1 pro j≤k<s. Původní Q_ij lze nastavit0,
protože před prvním navštívením nebylo použito. Pravý posun je
při implementaci od větších k k menším nebo ze starých hodnot
současně. Q′_is=i−r určuje kandidátní r. Po inverzním kroku už
Q_ij nebude nikdy čteno, takže knižní vynechání jeho vynulování
neovlivní další volby ani výstup.

Při bijekci všech N! vstupů na všechny dvojice standardního P
a přípustného Q by počet dvojic byl T_λ∏H_ij, protože intervaly
Q mají nezávislé H_ij možnosti. Rovnost by dala Theorem H.
Tato podmíněná úvaha je správná, ale nezaručuje kandidátní
invariant a nesmí sloužit jako jeho kruhový důkaz.

## P0594 — původní mezera, nyní uzavřená samostatným důkazem

Primární [Novelli–Pak–Stoyanovskii1997](https://www.math.ucla.edu/~pak/papers/bij.pdf)
byl přečten v rozsahu definic a algoritmů§2,4–5 a důkazů§6.1–6.4.
Přesné přeložení je A=P^T a f=−Q^T: sloupcové pořadí se stane
řádkovým, posun f o−1 posunem Q o+1, kandidáti f≥0 kandidáty
Q≤0. Zdrojové maximum kódu N<konec<W se po transpozici stane
minimem D<Q<R. Aktivní sloupcová hranice je právě řádková hranice
C0020. Vynulování opuštěného f odpovídá nepozorovatelnému
vynulování Q podle P0593.

Silnější stavová podmínka je konkrétní: aktivní řádkový suffix P
je uspořádaný, Q splňuje háčkové meze, opuštěné/nepoužité Q jsou
konceptuálně nulové a všechny kandidátní zpětné cesty při aktivní
horní hranici procházejí aktuální buňkou. Je třeba doložit její
zachování oběma směry a to, že konec posledního siftingu má první
kód. Lokální inverze při známé cestě ani P0593 nestačí.

Zdrojové Theorems6.7–6.10 tvrdí stabilitu a obě inverze na množině
stavů C; lokální rozdělení cest je v6.4. Sazba obou2×2 případů
a následující stabilita byly zobrazeny v images/tableaux-nps-proof-10.png
až -12.png. Vlastní úplná kontrola geometrického přenosu všech
kandidátů v řádkových souřadnicích zatím není dokončena. Bod proto
zůstává partial: nepovyšuje se podle názvu známé věty. Existence
publikovaného důkazu je doložena; správnost úplného převedení je
přesný další kurzor. P0590 zatím neuzavírá jednoznačnost(e).

Známá oprava „original permutation“2006 je jazyková. Kroky
příkladů byly ruční; žádná enumerace nebo program nebyly spuštěny.
Prvenství poznámky1992 se samostatně nepřezkoumávalo; bibliografické
údaje a dostupnost důkazu1997 ověřeny v primární publikaci.


Doplnění: tableaux-proof-39-inverse-invariant.md uzavírá přesně tuto mezeru
všemi lokálními/obecnými případy; také dokazuje jednoznačnost P0590.
Předchozí popis partial je historický stav před tímto doplněním.
