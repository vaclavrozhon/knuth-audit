# §5.2–12: MacLarenův úplný invariant, inverze a cena

Zadání80/file91, odpověď618/file629, originál zobrazen.
Vstup je úplný seznam všech N záznamů právě jednou,
zakončený0; ne libovolný graf ukazatelů. Záznamy si
označme různými požadovanými hodnostmi1,…,N podle
jejich pořadí ve vstupním seznamu. To zahrnuje i stejné
klíče: nepředpokládá se jejich přísná nerovnost.
LINK je součástí záznamu a v M4 se s ním vyměňuje,
jak výslovně požaduje kniha.

## P0669: skutečně proveditelná dvouprůchodová alternativa

První průchod vede z HEAD. Před přepsáním LINK(P)
si uložíme jeho starou hodnotu Q; potom nastavíme
LINK(P)=k a pokračujeme P=Q,k←k+1. Po N krocích
má každý záznam ve svém linku jednoznačnou cílovou
hodnost. Uložení Q před zápisem chrání zbytek seznamu.

Ve druhé fázi projdeme i=1,…,N. Dokud LINK(i)≠i,
vezmeme k=LINK(i) a vyměníme celé záznamy i,k,
včetně linku. Záznam v k má nyní svou hodnost k,
takže je konečně na místě; dřívější již správné pozice
se neporuší, protože každá cílová hodnost je jedinečná.
Počet nesprávných pozic při výměně klesá, takže se
skončí se všemi LINK(i)=i a s požadovaným pořadím.
Máme O(N) výměn a jeden pomocný záznam plus O(1)
indexů. Zde se link přesouvá se záznamem; nepoužívá
se chybný předpoklad, že by šlo o samostatnou pevnou
tabulku adres z úlohy10.

## P0670: silný invariant MacLarenovy metody

Na začátku M2 při hodnotě k platí:

1. Pozice1,…,k−1 obsahují přesně již konečné hodnosti.
2. Cesta od P po aktuálních LINK končí0, nemá opakované
   uzly a při vynechání všech uzlů<k obsahuje každou
   pozici≥k právě jednou, v rostoucím pořadí hodností
   zbylých záznamů.
3. Pro j<k je LINK(j)≥j. Každý takový j, který leží
   na cestě z bodu2, má dokonce LINK(j)>j.

Pro k=1 je to přesně úplný vstupní seznam; třetí
podmínka je prázdná. Silnější konečnost a nezacyklenost
v bodu2 je nutná: samotné nerovnosti LINK(j)≥j by
nevylučovaly dosažitelnou samosmyčku.

## P0671: každý přechod M3/M4 a přesné ukončení

M3 odstraní z počátku cesty uzly<k, dokud nenajde
první aktivní P≥k. Pro k≤N takový uzel podle invariantu
existuje; před ním tedy není0. Konečnost cesty dokazuje
ukončení M3. Tento P obsahuje právě požadovanou hodnost k.

Je-li P=k, výměna nic nezmění. Q je starý následník
k; nastavení LINK(k)=k vytvoří samosmyčku mimo
zbývající cestu a P←Q odstraní její první uzel k.
Všechny ostatní body invariantu pro k+1 zůstávají.

Je-li P>k, označme před výměnou q=LINK(P), s=LINK(k).
Po výměně celých záznamů má k správný záznam i link q,
zatímco na P se přesunul starý záznam z k a link s.
M4 si uloží Q=q a nahradí LINK(k) hodnotou P.

Původní cesta od P začínala aktivním P a v pozdějším
ocasu obsahovala aktivní k právě jednou. Nová cesta
od q vznikne z tohoto ocasu nahrazením výskytu

    k   za   k,P.

První k je nyní jen přesměrování na novou adresu
svého starého záznamu. Staré P nebylo v původním
ocasu, takže náhrada nemůže vytvořit opakovaný uzel.
Nový link P=s zachovává pokračování. To platí i pro
q=k a všechny sousední případy. Aktivní záznamy
po odfiltrování uzlů≤k jsou ve stejném pořadí jako
předtím, jen hodnost k byla odstraněna a její místo
ve fixním prefixu je správné. Nový pevný uzel k má
LINK(k)=P>k. Invariant pro k+1 je tedy plně dokázán.

Nemůže existovat neprázdný ocas cesty tvořený jen
pevnými uzly: každý jejich link je kladný a poslední
by nemohl vést do0. Při posledním kroku k=N proto
musí být P=N a LINK(N)=0; potom nové P=0,k=N+1.
Obráceně pro k≤N cesta obsahuje aktivní uzel, takže
P≠0. Oba ukončovací testy M2 jsou skutečně ekvivalentní.
Po N výměnových krocích jsou všechny hodnosti na místě.

## P0672: všechny výstupní konfigurace a explicitní inverze

Označme b_k hodnotu P při M4 pro dané k. Je to
aktuální adresa záznamu hodnosti k a b_k∈{k,…,N}.
Po M4 je LINK(k)=b_k. Pozdější výměny používají
jen indexy≥k+1, takže tuto hodnotu již nezmění.
Konečná linková tabulka je právě b_1,…,b_N.

Na poli hodností tedy algoritmus provádí obyčejný
výběr: pro k=1,…,N vymění pozice k a b_k, kde
leží hodnost k. Z libovolných čísel b_k∈[k,N]
rekonstruujeme původní pole hodností takto: začneme
identitou1,…,N a pro k=N,N−1,…,1 vyměníme k,b_k.
Tato reverze skutečně vynucuje dané dopředné volby.
Po odvolání všech větších kroků totiž pozice≤k ještě
obsahují své vlastní hodnoty; reverzní výměna umístí
hodnotu k právě do b_k. Dopředné zrušení menších
kroků pak při výběru k najde přesně toto b_k.

Z rekonstruovaného pole a_j=hodnost záznamu na j
se jednoznačně získá původní HEAD=a^−1(1) a
LINK(j)=a^−1(a_j+1), pokud a_j<N, jinak0.
Tím je dána explicitní inverze z konečných linků
na původní seznam, včetně HEAD; není to pouhé
porovnání dvou stejných počtů.

Počet dovolených konečných tabulek je
∏_(k=1)^N(N−k+1)=N!. Úplných vstupních seznamů
na N různých adresách je také N!, a právě popsané
oba směry dávají jejich bijekci. Tvrzení o možnosti
zpětné rekonstrukce nevyžaduje, aby tato důkazová
rekonstrukce sama používala O(1) paměti.

## P0673: samoodkaz právě u maxima původního cyklu

Původní pole hodností a je permutace adres. Při
výběrovém kroku k je b_k předchůdce hodnoty k
v aktuálním cyklu zobrazení a: a_(b_k)=k.
Je-li b_k≠k, výměna a_k a a_(b_k) oddělí singleton k
a připojí jeho původního předchůdce k původnímu
následníkovi. Ostatní členové a pořadí cyklu zůstanou.

Po krocích1,…,k−1 je tedy v původním cyklu k stále
tentýž cyklus s vymazanými menšími členy. b_k=k
nastane právě tehdy, pokud žádný větší člen v tomto
původním cyklu není, tedy právě když k byl jeho maximum.
Každý původní cyklus dá právě jeden takový samoodkaz.
Adresní permutace požadovaného seznamu je inverzí a;
její cykly mají stejné množiny prvků, takže formulace
odpovědi o původní permutaci platí v obou konvencích.

## P0674: proč se každý přesměrovací odkaz následuje právě jednou

Při b_k>k přechod P0671 vloží do zbývající cesty
právě jeden nový pevný uzel k. Při b_k=k nevloží
žádný. M3 vždy odstraní navštívený pevný uzel
z počátku cesty. Pozdější přechody jen zachovávají
dosavadní ocas a případně přidávají **nový** pevný
uzel; odstraněný starší pevný uzel se nemůže vrátit.
Na konci je cesta prázdná. Každý vložený pevný uzel
tedy musí být odebrán M3 právě jednou a samosmyčky
se M3 nikdy nenásledují.

Je-li C počet původních cyklů, pak podle P0673 je
počet nesamoodkazů N−C. Přesný počet operací
P←LINK(P) v M3 je tudíž

    A_M=N−C.

Nejde o neodůvodněný odhad založený jen na tom,
že odkaz míří doprava; takový odhad by nevyloučil
opakované návštěvy. Z celé transformace cesty vyplývá
amortizovaný lineární počet všech těchto návštěv.

## P0675: přesná statistika, cena a krajní případy

Pro N≥1 má C minimum1 a maximum N; proto
0≤A_M≤N−1, obě meze jsou dosažitelné. Pod rovnoměrnou
vstupní permutací přebíráme již dokázané P0665,
E C=H_N. Tedy E A_M=N−H_N, jak uvádí odpověď.

M4 se provede N krát, M3 má N základních testů
a N−C pokračování, ostatní práce na krok je konstantní.
Pro záznam délky ℓ je čas O(Nℓ+N), pomocná paměť
jeden záznam a O(1) indexů. Nejsou potřeba nové
značkové bity ani pole N adres. Prázdný seznam má
HEAD=0 a skončí okamžitě; singleton0-link přejde
na finální samoodkaz1 bez M3 pokračování.

To uzavírá také věcný prostorový odkaz z74 na úlohu12.
U neurčené relativní časové konstanty P0646 tím však
nevzniká žádný nový univerzální závěr.

## P0676 — partial: „kratší a rychlejší“ než druhý průchod

Vytištěný M4 obsahuje N výměn, včetně možných výměn
pozice se sebou. Vynecháme-li tyto triviální výměny,
zůstává jich přesně N−C. Běžná výměna pomocí jednoho
záznamu má3 kopie; proti tomu cyklová metoda z10
má N+C−2B kopií, kde B je počet pevných bodů.
Rozdíl3(N−C)−(N+C−2B)=2N−4C+2B je nezáporný:
každý netriviální cyklus délky l přispěje2(l−2).
To přesně vysvětluje, proč mohou dlouhé záznamy
omezit výhodnost MacLarenovy metody.

Úspora předběžného průchodu seznamem může být podstatná
pro krátké záznamy, ale text neurčuje instrukční
implementaci obou metod ani práh „not too long“.
Tvrzení o jejich relativní délce/rychlosti proto
zůstává modelově partial. Celá správnost, bijekce,
lineární čas a přesný počet M3 jsou nezávisle
dokázány výše; tato mezera není chyba algoritmu.

Historické zdroje MacLaren1966 a Gries–Prins1987
nebyly nově přečteny; nevydávají se za zdroj vlastních
výše uvedených důkazů. Žádný nový program ani nález.
