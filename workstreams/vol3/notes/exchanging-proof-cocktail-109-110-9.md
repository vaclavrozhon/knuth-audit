# Refinements109–110: všechny průchody, Iverson a skutečný rozsah9

2026-11-07. P0957–0968. Originály109–110/134 a dopředné
353/356/696 zobrazeny; poslední tři jsou v
`sources/cocktail-cross-reference.pdf` a odpovídajících třech
obrazech. Offset všech+11. Pět vrstev doplňuje
`sources/cocktail-pass-count-errata-review.json`.
Známý humor v popisku16 není překlep; moderní dodatek2021
je zohledněn jako známá změna. Bez matematického programu.

## P0957: všechny uvedené zbytečné porovnání a pravý nejmenší prvek

Z úplných již doložených řad obrázku14 se ověřují přesně
následující případy. Po průchodu3 jsou pozice1,2 hodnoty61,87;
při průchodu4 jsou tedy stále ve stejném pořadí a porovnání j=1
je nadbytečné. Průchod4 nezmění první tři pozice61,87,170:
při průchodu5 jsou proto zbytečná j=1,2. Po průchodu5
i po průchodu6 zůstává první čtveřice61,87,170,275, takže
v průchodech6 i7 jsou zbytečná j=1,2,3. Důvodem posledního
případu není to, že170 už má globálně správnou pozici:154
se teprve blíží zprava. Jde o známý nezměněný uspořádaný
prefix v okamžiku příslušných porovnání.

Pokud nejmenší hodnota1 začíná na n, má b_1=n−1. P0943 pak
dává po r neprázdných průchodech BOUND=n−r: člen b_1+1=n
je maximální možný a zůstává aktivní. Každý takový vstup
proto vynutí C=(n−1)+…+1, bez ohledu na ostatní hodnoty.
Samotné tvrzení, že hodnota jde doleva nejvýše o1, dává
počet průchodů; přesná hranice navíc dokazuje i uvedený
**maximální počet porovnání**. Tyto dva závěry nejsou zaměněny.

## P0958: formální varianta odpovídající obrázku16

Aktivní interval je[L,R], původně[1,n]. Levý i pravý vnější
úsek jsou už na svých finálních místech a svými klíči oddělují
aktivní interval. Dopředný průchod porovná j=L,…,R−1 a po
poslední výměně t nastaví R=t. Zpětný průchod porovná
j=R−1,…,L a po poslední výměně t nastaví L=t+1. Je-li
průchod bez výměny, končíme. To je symetrické zkrácení B;
nepředpokládá navíc Iversonovy vnitřní dělicí body.

Dopředný prefixový důkaz P0937 se při obrácení směru mění
na přenos minima suffixu. Po poslední zpětné výměně t je
prefix do t hotový. Oba kroky tedy zachovávají uvedený
intervalový invariant. Průchod s výměnou zkrátí délku alespoň
o1; bez výměny zjistí uspořádání všech sousedů aktivního
intervalu. Tím jsou správnost i konečné ukončení úplné.
Při L=R může být poslední ověřovací průchod prázdný; jeho
započtení do počtu průchodů musí být výslovné.

Stabilita a celkový počet výměn rovný původnímu počtu inversí
se přebírají z P0938, protože obě směrové varianty používají
jen ostré sousední výměny. Každý aktivní průchod délky m
má m−1 porovnání. Proto jich je nejvýše binom(n,2), neboť
aktivní délka po každém neprázdném průchodu ostře klesá;
reverzní vstup tuto mez dosáhne postupným vylučováním maxima
a minima. Průměr z této nejhorší meze samotné neplyne.

## P0959: celý obrázek16, všechny výměny a obě hranice

Základní vstup je stejný jako u obrázku14. Výstupy po sedmi
zobrazených průchodech jsou:

```text
1→: 087 503 061 512 170 897 275 653 426 154 509 612 677 765 703 908
2←: 061 087 503 154 512 170 897 275 653 426 509 612 677 703 765 908
3→: 061 087 154 503 170 512 275 653 426 509 612 677 703 765 897 908
4←: 061 087 154 170 503 275 512 426 653 509 612 677 703 765 897 908
5→: 061 087 154 170 275 503 426 512 509 612 653 677 703 765 897 908
6←: 061 087 154 170 275 426 503 509 512 612 653 677 703 765 897 908
7→: 061 087 154 170 275 426 503 509 512 612 653 677 703 765 897 908
```

V každém řádku lze přenášené maximum/minimum sledovat
po uvedených výměnných indexech; nejsou vypočteny programem:

| Průchod | Všechny výměny j v pořadí provádění | Porovnání | Nová hranice |
|---|---|---:|---|
|1→|1,3,5,…,15|15|R=15|
|2←|14,9,8,7,6,5,4,2,1|14|L=2|
|3→|3,5,7,…,14|13|R=14|
|4←|8,6,4|12|L=5|
|5→|5,7,9,10|9|R=10|
|6←|8,6|5|L=7|
|7→|žádné|3|konec|

Počty výměn13+9+10+3+4+2=41 souhlasí s původním invariantem.
Porovnání je71 proti75 pro obyčejný bubble na témže vstupu.
Všechny křivky i horizontální čáry obrázku odpovídají řadám
a hranicím v tabulce. Sedmý průchod má tři skutečná porovnání,
ačkoli řada byla setříděna již šestým. Tento konkrétní rozdíl
je důležitý při dopředné odpovědi5.4.8-9; není to simulovaný
experiment nebo tvrzení o všech náhodných vstupech.

## P0960–0961: obecný Iversonův argument a celý příklad

Předpokládejme nejprve plný průchod zleva doprava a pak zprava
doleva. Při prvním porovnání na hranici j,j+1 je na j maximum x
původního prefixu1,…,j. Pokud se na této hranici nevymění,
zůstane tam x, všechny klíče nalevo jsou≤x a pozdější část
průchodu už pozici j nezmění. Obsah levého a pravého úseku
se na hranici nepromísil.

Při opačném průchodu přichází na j+1 minimum y celého pravého
suffixu. Pozice j se dosud nezměnila. Jestliže se ani nyní
nevymění, x≤y. Máme proto současně

    každý levý klíč≤x≤y≤každý pravý klíč.

Hodnoty x,y jsou na pozicích j,j+1 finální. Pokračování
zpětného průchodu je nezmění: bezprostřední levý soused≤x,
takže ani jeho porovnání nemůže x posunout. Už žádná následná
sousední inverze nemůže překročit tyto dvě pozice. Mohou se
vyjmout ze všech dalších porovnání a oddělit nezávislé úseky.
Při duplicitách zůstává předchozí stabilní pořadí shodných
záznamů, takže závěr platí i pro ně, bez neplatného požadavku
na ostré x<y.

Pro první směr zprava doleva je argument zrcadlový, s prvním
minimem suffixu a druhým maximem prefixu. Při zkrácených
průchodech platí totéž v aktivním intervalu, neboť vnější
úseky jsou již finální a oddělené. Podmínka se týká dvou
**provedených** porovnání této hranice; pouhé vynechání
dosud neprověřené dvojice se za informaci o jejím pořadí nebere.

Příklad432186975 má v dopředném průchodu výměny j=1,2,3,5,7,8
a výsledek321468759. Na hranici j=4 se nevyměnily4 a8.
V opačném směru výměny7,6,5 přinesou5 na pozici5, před
porovnáním j=4 je řada321456879. Porovnání4≤5 je opět
bez výměny; obě hodnoty jsou finální, jak tvrdí text.
Pokračování zbývajících výměn j=2,1 dá132456879 a jejich
pozice opravdu zachová. Původní Iverson218–219 a jeho
historická priorita byly bibliograficky přeskočeny; matematický
argument zde na nedostupném prameni nezávisí.

## P0962: dopředné5.4.8-9, každá souřadnice u_k

Skutečná definice353 pro b=1 je

    u_k=#{i≤k:a_i>k}, 1≤k≤n.

Počet hodnot≤k v pravé části je stejný: celkem existuje právě
k takových hodnot a v levé části jich je k−u_k. Rovnost
u_k=d_(k+1) proto platí bez předpokladu o algoritmu.

Fixujme k a nahraďme každou hodnotu≤k nulou a každou>k
jedničkou. Přísné compare/exchange se na těchto znacích
chová jako10→01; výměny uvnitř stejné třídy nic nemění.
Je-li binární slovo neuspořádané, jeho první1 na p leží
před poslední0 na q. Celý dopředný průchod odstraní právě
tuto první1 z p a přidá1 vpravo: nese1 přes všechny další
znaky a zbývající slovo zachová v původním pořadí. Následující
zpětný průchod odstraní poslední0 a přidá0 vlevo. Složený
účinek je tedy

    0 + (původní slovo bez první1 a poslední0) + 1.     (A)

Když u_k>0, platí p≤k<q. V prvních k znacích proto(A)
odstranilo jednu1 a přidalo jednu0, takže u'_k=u_k−1.
Při u_k=0 má původní prvních k znaků jen nuly; po(A)
zůstane tento počet jedniček0. Je-li celé binární slovo už
setříděné, oba průchody je nezmění. Pro každé k a současně
pro všechny tedy po dvojici platí

    u'_k=max(u_k−1,0).

Zkrácené průchody lze doplnit o neúčinná porovnání ve finálních
úsecích, takže závěr platí i pro variantu z obrázku16. To je
úplný nový argument pro skutečné dopředné tvrzení; neodvolává
se kruhově na celý dosud neauditovaný elevator algorithm.

## P0963 partial / C0027 candidate: co přesně počítá vzorec na696

Nechť U=max u_k. Všechny u_k=0 právě tehdy, když každý prefix
délky k obsahuje1,…,k, tedy permutace je identita. Po r úplných
dvojicích jsou souřadnice max(u_k−r,0). Pro U>0 tedy první
průchod, po němž je permutace skutečně uspořádána, nastane
v čase2U−1 nebo2U. Pro U=0 je tento čas0. To je platný
obsah vzorce odpovědi5.4.8-9.

Nemusí to být počet **vykonaných** průchodů včetně zjištění,
že žádná další výměna není potřebná. Například2341 má
u=(1,1,1,0). Varianta obrázku provede

    2341 → 2314 → 1234 → 1234,

s aktivními hranicemi po prvním průchodu R=3, po druhém
L=2; třetí průchod ještě opravdu porovná pozice2,3.
Jsou to3 průchody, zatímco2U−(0 nebo1) připouští jen1 nebo2.
Ještě přímo původní obrázek16 má U=3 a sedm vykonaných
průchodů, z toho poslední ověřovací. Jeho u po jednotlivých
prahových k jsou

    1,1,2,2,3,3,3,3,3,3,2,2,2,2,1,0.

Znění na696 neříká, zda tento poslední průchod vynechává.
Korektní interpretace jako času do prvního uspořádání je možná;
proto **candidate/low**, nikoli confirmed. Samotná redukce u
ani správnost cocktail sortu není vyvrácena. Přesné předání,
všechny vrstvy a originály jsou v `notes/V3-C0027-cocktail-pass-count.md`.

## P0964–0965 partial: výzkumná9 a praktická srovnání

Úloha5.2.2-9 žádá analýzu počtu průchodů a porovnání, nikoli
jen pravdivou vazbu na U. Obecný deterministický vztah a
nejhorší počet porovnání jsou doloženy výše; rozdělení U,
rozlišení posledního půlcyklu a úplné průměry/rozptyly počtu
porovnání zde řešeny nejsou. **P0964 partial** pro tento přesný
výzkumný rozsah, bez enumerace permutací.

Podobně konkrétních71<75 z obrázku není důkaz tvrzení110,
že průměr porovnání je poněkud menší. Ani bodová dominance
není pravdivá pro prosté střídání: na3215476 má bubble
6+5=11 porovnání, zatímco uvedený cocktail6+5+4=15,
s koncovými řadami2134567,1234567,1234567. To nevyvrací
tvrzené **průměrné** srovnání. Přesný obecný průměr a velikost
slovního „slightly“ proto zůstávají **P0965 partial**.

Stejná položka výslovně nezavírá neurčené globální „better
than straight insertion“ ani empirický cache/branch argument
nové věty2021. Zde nejsou dány programy, stroje, délky ani
výkonnostní kritérium. Z P0958 plyne kvadratická nejhorší
práce a z P0968 i kvadratický průměr výměn, ale ne přesné
pořadí konstant na libovolném stroji. Známé doplnění2021 se
nepočítá jako naše chyba staré knihy a výrok o vhodnosti
pro velká n je správný jen v příslušném srovnávacím modelu.

## P0966–0967: posun počátku a co z něj opravdu plyne

V dopředném průchodu na aktivních m položkách nesme maximum
v registru. Při načtení dalšího x se vypíše min(maximum,x)
a v registru zůstane max(maximum,x). To je přesně prefixový
přechod B. Pokud na všechny nevynesené položky pohlížíme
s počátkem posunutým o1, původní další x už leží na logické
výstupní pozici. Pro x≤maximum se proto nemusí zapisovat;
pro x>maximum je nutno na jeho fyzické místo uložit staré
maximum a nést dál x. V závěru se maximum uloží zvlášť.
To je konkrétní platný obsah návrhu s posunem počátku.

Pro rovnoměrný první průchod je očekávaný počet nových
prefixových maxim H_m, protože každá pozice j má pravděpodobnost
1/j být maximem prefixu. Ostatních m−H_m položek opravdu
jen přejde o1 logické místo doleva. Slovo „most“ se tak
dá odůvodnit průměrově; pro již setříděný vstup by stejné
deterministické tvrzení neplatilo.

Jedna konkrétní úplná implementace: aktivní fyzický úsek je
[l,n]. Jeho první záznam načteme do registru, projdeme l+1,…,n
popsaným pravidlem a vynesené maximum uložíme na l. Zbytek
na[l+1,n] obsahuje všechny ostatní records a má pořadí jako
jeden bubble pass po odstranění maxima. Zvyšujeme l a opakujeme.
Na konci jsou maxima fyzicky v sestupném pořadí; jediná
závěrečná reverze O(n) přesunů dává vzestupné pořadí.
Každý záznam je zachován a každý krok oddělí skutečné maximum,
takže správnost je induktivní. Počet porovnání je přesně
(n−1)+…+1, stejný jako u prosté selection. Posun indexů
sám tuto kvadratickou porovnávací práci neodstranil.

Kniha však neudává přesný MIX program této varianty, rozložení
už uloženého suffixu, započtení závěrečné změny reprezentace
ani smysl celkového „no better“. **P0967 partial** se týká
tohoto neurčeného nákladového srovnání, nikoli právě dokázané
lokální transformace, uvedené korektní implementace nebo
jejího přesného počtu porovnání.

## P0968: sousední výměny a začátek Batcherova odstavce110–111

Každá sousední transpozice změní počet inversí právě o±1.
Proto algoritmus, který smí přesouvat položky pouze takto,
potřebuje z permutace s I inversemi alespoň I výměn; při
výhradně opravných výměnách jich provede přesně I. Pro
rovnoměrnou permutaci je E I=n(n−1)/4 a maximum binom(n,2),
jak už dokazují P0088/P0089. V používaném **sériovém** modelu
s konstantní cenou jedné výměny je proto čas Ω(n²) v průměru
i v nejhorším případě. Chceme-li překonat tento řád v daném
modelu, musí se povolit i jiný přesun, zde nesousední výměna.
Jde o počet práce, nikoli tvrzení, že libovolný paralelní
stroj nemůže provést mnoho disjunktních sousedních výměn
současně. Následující Batcherův algoritmus se tím ještě neověřuje.
