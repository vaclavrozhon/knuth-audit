# Nezávislá revize rekurzivního protipříkladu s maximem 32

**Závěr:** V přezkoumaném obecném důkazu jsem nenašel věcnou chybu.
Rodina skutečných historií dává pro doslovně popsanou zarovnanou
first-fit strategii asymptotický faktor alespoň

```
4709347/783360 = 6 + 9187/783360 > 6.
```

Níže uvádím vlastní kontrolu lokálních operací, jejich skládání,
rozpočtu i okrajových chyb. Tento závěr neodvozuji z výsledku
generátoru ani z konečné stopy. Stopa 5 554 555 operací zde nebyla
přehrána; její nezávislou doslovnou validaci úspěšně dokončil root.
Výsledek této oddělené kontroly je doplněn v oddílu 9. Dvě
softwarové kvalifikace v oddílu 8 nemění případ maxima 32.

Přezkoumané verze důkazu, předchozího lemmatu, celého generátoru
a metadat jsou zachovány v `sources/`. Jejich původní cesty a hashe
jsou v `SNAPSHOTS.json`, takže případné další autorské změny nemění
rozsah této revize. Není přiděleno žádné globální ID nálezu.

## 1. Model a rozsah tvrzení

Paměť má celočíselné adresy od 0. Blok délky s zabírá [p,p+s)
a jeho začátek musí být násobkem největší mocniny dvojky nepřevyšující
s. First-fit vybere nejmenší takové volné p. Živý objem je součet
délek současně přidělených bloků; uvolňuje se vždy celý blok.

Pro a, které je mocninou dvojky, označuji **t-kandidátem** každý
možný interval délky t=a+1 se začátkem na násobku a. **Slot šířky
2a** je interval [2aj,2a(j+1)) pro celé j. Neprázdný slot blokuje
kandidáta délky 2a+1 začínajícího na jeho levém konci, ale tyto dva
pojmy nejsou zaměnitelné. Zejména půlení jednotek může zachovat
kandidáty délky 2a+1, aniž zachová všechny neprázdné sloty.

Maximum je m=2^r; v rozhodném případu r=5 a m=32. Pomocný parametr
je n=18mh a celkový dovolený živý objem N=n+m. Počet etap je při
pevném m pevný. Index etapy označuji k, s a=2^k, aby se nepletl
s pevnou maximální mocninou m. Hranice 1+r z knihy je pro m=32
rovna 6.

Nový závěr se týká pouze této konkrétní doslovné politiky. Nevyvrací
existenci jiného alokátoru s faktorem 6 ani mez pro optimální N(32).
Původní Robsonovo pravidlo vyžadující celý větší volný slot není
v této revizi nahrazováno pravidlem pro přesný interval délky s.

## 2. Ocas a jeho první volné adresy

Nezávisle jsem prošel i převzatý text `right-to-left-sparsification.md`;
nepoužívám jen jeho asymptotický závěr. Uvažujme t=a+1, a>=2,
a čerstvou dávku na adresách P+2aj, přičemž P/a je liché.
Všechny t-kandidáty před P jsou zablokované a vpravo je prázdno.
Opakované žádosti t opravdu dostávají tyto adresy: kandidát o a
dále ještě zasahuje předchozí blok, kandidát o 2a dále je volný.

Lokální operace pro p=P+6ak používá původní bloky na
p, p+2a, p+4a, p+6a, p+8a. Po uvolnění prostředních dvou
je prvním volným pomocným blokem 2a interval na p+3a. Jeho
začátek je násobkem 2a díky liché fázi p/a. Dřívější volný
2a-kandidát by obsahoval volný t-kandidát se stejným začátkem;
to prefix vylučuje. Blok na p končí na p+a+1 a zbývající lokální
kandidáty rovněž vylučuje.

Po uvolnění t-bloku na p+6a dostane další t začátek p+5a.
Kandidát p+2a ještě zasahuje pomocný blok. Po uvolnění pomocného
bloku je naopak p+2a prvním volným t-kandidátem. Výsledkem jsou
bloky na p, p+2a, p+5a, p+8a. Nové mezery délky 2a-1 nepřijmou
pomocný 2a-blok; první zarovnaný t-kandidát v každé z nich zasahuje
pravého souseda jednou buňkou. Všechny dřívější kandidáty zůstávají
zablokované.

Operace probíhají zprava doleva. Pravý strážce následující levé
operace je obnoven na původní adrese p+2a právě poslední rezervací
předchozí operace. Tím je ověřena jejich skutečná složitelnost,
nejen jednotlivý izolovaný obrázek. Při počátečním objemu W je
vrchol nejvýše W: uvolněné dvě délky a+1 zaplatí pomocnou délku
2a s rezervou dvou buněk.

Pro počet J>=5 je počet operací K=floor((J-2)/3). Zůstane jeden
levý krajní blok, řetězec 2K+1 bloků po 3a a nejvýše dva pravé
krajní bloky. Poslední původní blok je zachován. Uvolní se přesně
K délek t a doplnění za koncem tedy vytvoří přesně další dávku K.
Zbytek rozpočtu modulo t je v každé plné fázi stejný.

Položíme-li J_0=floor(M/t), J_(i+1)=floor((J_i-2)/3) a poslední
kladný J_l<=4, dostáváme pro S=sum J_i a e_i=J_i-3J_(i+1)
nezávisle teleskopováním

```
2S=3J_0-sum e_i,
1<=e_l<=4,     2<=e_i<=4 pro i<l,
l+1<=1+floor(log_3 J_0).
```

Konec ocasu je přesně P+2aS-2a+t. Proto se od P+(3a/t)M
liší o O(a log(2+M/t)), se skutečnou konstantou nezávislou na h.
Přípravný vrchol nepřekročí objem prefixu plus M. Tím jsou
ověřeny jak délkový, tak živý účet převzatého lemmatu.

## 3. Nová regularizace a její fáze

Vezměme pět t-bloků na p, p+3a, p+6a, p+9a, p+12a.
Uvolnění p+9a umožní přesně rezervaci t na p+8a: levý blok
končí na p+7a+1. Po uvolnění p+3a a p+6a je prvním volným
začátkem p+2a; následující rezervace jde na p+4a, protože
dočasný blok končí na p+3a+1. Jeho následné uvolnění ponechá
p, p+4a, p+8a, p+12a. Žádný mezikrok nepřekročí počáteční
objem W; konečný objem je W-t.

Původní mezery po 3a před právě zpracovanou skupinou nepřijímají
t-kandidáta. Nové mezery po 4a jej už přijímat mohou. Proto je
zásadní právě sestupné pořadí všech skupin i všech řetězců:
nově uvolněné kandidáty leží napravo od dalších rezervací.
Společný krajní strážce skupin s bázemi vzdálenými 12a zůstává
na místě. Operace nepoužívá neověřené přeskakování volných adres.

Při p/a lichém označme první zasažený 2a-slot indexem u.
První čtyři původní bloky zasahují postupně sloty

```
{u,u+1}, {u+2}, {u+3,u+4}, {u+5}.
```

První tři nové zasahují

```
{u,u+1}, {u+2,u+3}, {u+4,u+5}.
```

Pravý strážce je stejný. Sjednocení obsazených slotů je tedy
přesně zachováno. Nejde jen o zachování jejich počtu.

Pro další etapu je nutná silnější fáze p==-a (mod 4a).
V řetězci po 3a se zbytky prvních čtyř začátků modulo 4a
vystřídají všechny, takže výběr vždy existuje. Bází dalších
skupin je p+12ak, a tudíž má tutéž fázi. Vlevo i vpravo
zůstane nejvýše tři nepoužité bloky; krátký řetězec, na který
skupina nevyjde, má nejvýše sedm bloků a lze jej celý ponechat
jako okraj. To není lineární ztráta v délce dlouhého řetězce.

Výsledné řetězce nejsou proloženy jinými živými bloky. Tento
pomocný prostorový invariant plyne konstrukcí: jednotlivé dávky
ocasu jsou oddělené, regularizace mění jen vnitřek jednoho řetězce
a jeho nové okraje leží mimo nový pravidelný vnitřek. Pozdější
půlení přidává k okrajům jen konce. Hypotéza lokálních operací
„mezi nimi nic jiného“ je tedy splněna i při opakovaných etapách.

## 4. Půlení zachovává právě požadované kandidáty

Kandidát délky 2a+1 s indexem v začíná na 2av. Jednotka nebo
dvojice na 2aj zasahuje přesně kandidáty s indexy j-1,j.
Totéž platí pro blok délky b+1 na 2aj-b, kde 2<=b<a:
jeho poslední buňka je 2aj a zbytek leží vlevo od této hranice.

Pro po sobě jdoucí markery j_min,...,j_max je celé sjednocení
blokovaných indexů interval [j_min-1,j_max]. Zachování sudých
j pokrývá jeho vnitřek; zachování prvního a posledního bloku
pokryje případné krajní chybějící indexy. U řetězce jediného
bloku se první a poslední samozřejmě počítají jen jednou.
Tím je zachováno celé sjednocení kandidátů každého řetězce.
Jeho překrytí s ostatními třídami závěr neoslabuje.

Nový pravidelný krok je 4a. Pro jednotky a dvojice zůstává
fáze 0; pro starší b+1 fáze -b. Po přeznačení a'=2a to
jsou přesně indukční požadavky na krok 2a'. Aktuální třída
a+1 se v tomto kroku správně nepůlí: její regularizace už
vytvořila požadovaný krok 4a a fázi -a.

U b+1 tentýž blok zasahuje také přesně 2a-sloty j-1,j;
jejich sjednocení je tedy půlením zachováno. Jednotky a dvojice
zasahují jen jediný 2a-slot, takže tento silnější závěr pro ně
neplatí. Závěrečná etapa je proto správně ponechává všechny.

## 5. Globální přechod mezi etapami a živý rozpočet

Před regularizací končí poslední blok na E a první další
t-kandidát je E+a-1. Každý 2a-slot začínající před
Q=2a ceil(E/(2a)) je neprázdný: kdyby byl prázdný, obsahoval
by volný t-kandidát se stejným začátkem, který leží před E.
Regularizace toto sjednocení slotů přesně zachová. Proto jsou
první volný 2a-slot i první kandidát délky 2a+1 právě na Q.

Je-li Q/(2a) sudé, vložená mocnina 2a jde skutečně na Q,
zablokuje i příslušný kandidát 2a+1 a posune nový začátek
na P=Q+2a. Jinak P=Q. Vždy je P/(2a) liché a napravo od P
je prázdno. Tato případná mocnina je vložena **před** půlením
jednotek a dvojic; není dodatečně předpokládáno, že i po jejich
půlení zůstávají všechny 2a-sloty neprázdné.

Půlení zachová kandidáty 2a+1. Nový ocas pro a'=2a je tedy
oprávněn použít předchozí lemma v celém původním prefixu.
Jeho pomocné bloky 4a také nemohou uniknout do starší mezery:
volný 4a-kandidát by obsahoval kandidáta délky 2a+1 se stejným
začátkem. To ověřuje first-fit i pro nový, větší pomocný typ.

Živý objem se v regularizaci nezvyšuje, půlení jen uvolňuje.
Případná mocnina přidá 2a k objemu nejvýše n; při přechodu
4a<=m tedy určitě nepřekročí N=n+m. Prefix po půlení má
pro velká h objem menší než n. Doplnění ocasu využívá pouze
n minus tento skutečný objem; jeho lemma nepřekročí n.
Konce etap se od n liší o méně než délku aktuálního bloku,
tedy o O_m(1).

V závěru m=2a se aktuální třída regularizuje a starší b+1
se půlí. Jednotky, dvojice a všechny okraje zůstávají. Všechny
m-sloty před Q=m ceil(E/m) jsou proto nadále neprázdné. Následující
m-bloky se opravdu ukládají na Q,Q+m,... a počet je určen skutečnou
zbývající kapacitou do n. Není používán součet prefixových maxim,
která by se nemusela dát dosáhnout současně.

Pro m=32 používá konstrukce jen délky
1,2,3,4,5,8,9,16,17,32. V posledním ocasu délky 17 je pomocníkem
32; žádný krok už nepotřebuje 64. Obecně se přechod provádí jen
při 4a<=m a závěrečná regularizace nepoužívá větší pomocné bloky.

## 6. Výslovný počet okrajů a uniformita chyby

Položme d(n)=1+floor(log_3 n). Jeden nový ocas vytvoří nejvýše
d(n) pravidelných řetězců a 3d(n)+1 okrajových bloků: každá
velká dávka přidá jeden levý a nejvýše dva pravé okraje,
poslední malá dávka nejvýše čtyři.

Označme C_k a e_k počty pravidelných řetězců a okrajových bloků
na konci etapy k. Regularizace nepřidá žádný řetězec a vytvoří
nejvýše 7 okrajů na původní řetězec, včetně krátkých řetězců.
Půlení přidá nejvýše dva okraje na řetězec. Případná mocnina
přidá jeden. Lze tedy použít konkrétní hrubé odhady

```
C_1 <= 2+d,          e_1 <= 3d+1,
C_(k+1) <= C_k+d,
e_(k+1) <= e_k+9C_k+3d+2.
```

Pro pevný počet etap z toho plyne C_k,e_k=O_m(log n).
Každý okrajový blok má délku nejvýše m, a proto stejný řád
platí pro jejich objem. V závěrečné regularizaci a půlení
platí obdobný odhad bez nového ocasu. Konstanty jsou nezávislé
na h; neukrývá se zde lineární počet ponechaných bloků.

U regularizace řetězce délky J se odebere
K=max(0,floor((J-1-j_0)/4)), kde 0<=j_0<=3. Počet zbývajících
bloků se liší od 3J/4 o méně než dva. U půlení se počet
zbývajících bloků liší od J/2 nejvýše o dva. Staré okraje
se nemění. Objem celé třídy se tedy mění příslušným faktorem
3/4 nebo 1/2 s chybou O_m(C_k+e_k)=O_m(log n).

Nový začátek P se od posledního E liší o méně než 4a.
Chyba nového ocasu je O(a log n) podle oddílu 2. Na každé
z konečně mnoha etap se tedy předchozí O_m(log n) jen násobí
pevnou konstantou a přičítá se další O_m(log n). Nevzniká
člen log^2 n ani nevyřčený limit současně rostoucího m.
Protipříklad potřebuje pevné m=32 a h rostoucí do nekonečna.

## 7. Vlastní algebraická kontrola koeficientu

Základ má jednotkový objem n/4 a dvojkový objem n/3, dohromady
7n/12. Je vytvořen od prázdné paměti při vrcholu n: n jednotek,
uvolnění lichých, n/6 trojic a jejich výměna za dvojice zprava
doleva. Teprve pak se jednotky proředí na násobky 4. První volný
začátek trojky je P=5n/3-2. Dělitelnost n=18mh zajišťuje, že
P/2 je liché a n je násobkem 36. Ocas trojek má objem 5n/12
a přidává asymptotickou délku 2(5n/12), takže L_1=5/2.

Nechť w_k n je vedoucí člen objemu aktuální třídy a+1,
q_k n objemu jednotek a dvojic a L_k n pravého konce.
Výše ověřené změny objemů dávají vlastní odvození

```
w_1=5/12,           q_1=7/12,            L_1=5/2,
w_(k+1)=1/2-w_k/4,
q_(k+1)=q_k/2,
L_(k+1)=L_k + [6a/(2a+1)] w_(k+1),       a=2^k.
```

Rekurze pro w má uzavřený tvar

```
w_k=2/5 + (-1)^(k-1)/(60*4^(k-1)).
```

Tedy 19/48<=w_k<=5/12; kladný podíl pro každý nový ocas je
zaručen, nikoli odhadnut z konečné tabulky. Také v závěru
w_(k+1)-q_k/2 >= 19/48-7/24 = 5/48 > 0, takže pro velká
h zbývají skutečně další bloky m.

Konečný koeficient je

```
F_k = L_k+1/2-q_k/2-w_k/4
    = L_k+w_(k+1)-7/(12a).
```

Přímým zlomkovým rozvinutím:

```
w_2=19/48,   w_3=77/192,   w_4=307/768,   w_5=1229/3072,
L_2=5/2+19/20=69/20,
L_3=69/20+77/72=1627/360,
L_4=1627/360+307/272=69133/12240.
```

Pro a=16 je q_4/2=7/192. Na společném jmenovateli 783360
má součet L_4+w_5-q_4/2 čitatele

```
69133*64 + 1229*255 - 7*4080
= 4424512 + 313395 - 28560
= 4709347.
```

Šestinásobek jmenovatele je 4700160; rozdíl je skutečně 9187.
Proto existuje konstanta K_m nezávislá na h, pro niž dosažený
konec splňuje

```
E >= (6+9187/783360) N - K_m log(2+N),     N=576h+32.
```

Přechod z n na N mění jen konstantní člen, protože m je pevné.
Kladný lineární přebytek pro všechna dostatečně velká h převáží
logaritmickou chybu. Nejde o odhad z konkrétního h=2048.

V paměti velikosti 6N vezmeme první rezervaci této nekonečné
adresní historie, která by končila za 6N. Před ní se doslovná
omezená politika chová totožně; nemůže existovat jiné dřívější
volné zarovnané místo, jinak by je vybral i původní first-fit.
Tato přípustná rezervace proto selže. Případné číslování paměti
od 1 lze ošetřit konstantním počátečním prefixem jednotek do
hranice m a posunem všech dalších adres o násobek m. Změní
objem i délku jen o O(m), nikoli rozhodný koeficient.

## 8. Kontrola generátoru a konkrétní meze této revize

Celý generátor jsem přečetl proti makrům důkazu. `tail` používá
právě K=floor((J-2)/3), klesající pořadí lokálních skupin a
správný koncový řetězec. `regularize` vybírá j_0 podle fáze
-a modulo 4a, pracuje sestupně a správně zachovává konce.
`halve_older` volí paritu podle absolutního markeru; nejde
o nesprávné půlení od lokálního prvního bloku. Při finálním
kroku vynechává jednotky a dvojice. Volání `tail` po přechodu
respektuje nový živý objem včetně okrajů a vložených mocnin.

Generátor sám kontroluje začátky živých bloků, zarovnání,
délky, objem a souhrny tříd. **Neověřuje překryvy intervalů
ani volbu nejnižší volné adresy**; jeho hlavička i metadata
tuto mez správně přiznávají. Důkazová revize výše tyto podmínky
řeší obecně, zatímco kontrolu konkrétní dlouhé stopy zajišťuje
odděleně root. Zde nebyl generátor znovu spuštěn, nebyl importován
a gzip stopa nebyla rozbalena. Byl pouze ověřen její SHA-256.

Dvě nalezené kvalifikace byly ihned odeslány rootovi i autorovi:

1. Pole `end` v některých záznamech `before_tail` obsahuje P,
   první začátek budoucího ocasu, nikoli poslední současnou živou
   adresu. Například před pětkami může být Q>P_old bez vložené
   mocniny, takže se žádný živý konec ještě neposunul. Neovlivňuje
   to pole `final_end`, skutečnou stopu ani asymptotickou rekurzi.
2. Parser dovoluje r=8, ale `bytearray` nepřijme hodnotu délky
   256. Tento konkrétní generátor tedy nepokrývá r=8 bez změny
   úložiště. Přezkoumaný r=5 je uvnitř rozsahu a matematický
   důkaz na `bytearray` nezávisí. Autor obě meze výslovně potvrdil.

Metadata uvádějí pro h=2048 rozpočet N=1179680, konec 7088928
a přebytek 10848 nad 6N. Tyto údaje jsou zde čteným vstupem,
nikoli výsledkem vlastního přehrání. Závěr o obecném protipříkladu
opírám o oddíly 2–7; závěr o přesném obsahu této konkrétní stopy
opírám pouze o samostatný výsledek root validátoru z oddílu 9.

## 9. Kolace konečné verze a přijatý root výsledek

Po dokončení důkazové revize jsem textově porovnal pracovní
snapshot s konečným autorským `proof.md`. Změny jsou omezeny
na stav předání a zprávu o úspěšné validaci konkrétní stopy;
žádný matematický krok oddílů 1–8 se nezměnil. Konečný důkaz
má SHA-256

```
be6e02896510d08c7d4603c9acd9ba6a78ff2e64d38f1b8820e7924e1ce1e220
```

Autorský `TRACE_NOTES.md` jsem celý přečetl. Výslovně dokládá
obě kvalifikace z oddílu 8 a zachovává původní metadata i kód
beze změny. Zmrazený autorský manifest má hash

```
477678f7ec62d681208bc3f7beb9e0f702842a29ee9aa28be1c033aae42a3598
```

Celé soubory `results/aligned-m32-h2048-independent.json` a
`results/aligned-m32-h2048-independent-run.json` byly přímo
přečteny. Root kontrola potvrzuje všech 5 554 555 operací,
maximum délky 32, vrchol živého objemu 1 179 648 při dovolených
1 179 680 a dosažený konec 7 088 928. Ten převyšuje
6N=7 078 080 o 10 848. Hash výsledku je

```
28afe4b5c7ae1d6d91c7d14eecce39062cdde0a9747c3d1fab61e98ae891d0c4
```

Tuto kontrolu nepřepisuji na vlastní běh; její zdrojový validátor
jsem zde nově neauditoval ani nespouštěl. Samostatná obecná
důkazová revize a tato root kontrola jsou dva odlišné doklady.
