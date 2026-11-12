# Úplné posloupnosti: §3.2.2-17,21,29

Stav 1. listopadu 2026: úlohy uzavřeny v níže uvedeném rozsahu.
Úloha 21 obsahuje novou chybu **V2-C0012 v erratu z 8. 7. 2001**;
původní kombinace abeced na str. 556 je správná. Úlohy 17 a 29 bez nové
matematické chyby. Základní zdroj: třetí vydání, první tisk 1997,
str. 38–40 a 555–557; obrázky `images/vol2-p038.png` až `p040.png`
a `vol2-p555.png` až `p557.png`. Stránka souboru = tištěná strana+12.

## Definice a přesný rozsah

Abeceda velikosti m je množina {0,...,m-1}; k je délka okna.
**Úplná posloupnost řádu k** je cyklické slovo, v jehož m^k pozicích
se každá k-tice číslic vyskytne právě jednou. Jde o posloupnost typu B
v odpovědi 21. Typ A má délku m^k-1 a obsahuje právě všechny nenulové
k-tice; „nenulová“ zde znamená jiná než (0,...,0), nikoli bez nulových
číslic. Každá taková posloupnost určuje funkci další číslice z k
předchozích číslic. Pouhá délka periody by tuto vlastnost nezaručovala.
Kontext odpovědi 21 nadále předpokládá rekurenci řádu k.
Pro m=1 je úplná posloupnost konstantní nula a není třeba konstrukce A.

## Úloha 17: proč hladový postup skončí a nic nevynechá

Použijme orientovaný graf: vrcholy jsou (k-1)-tice a hrana s číslicí y
vede z (v1,...,v_(k-1)) do (v2,...,v_(k-1),y). Hrany jsou právě k-tice;
každý vrchol má m vstupních i m výstupních hran. Pro k=1 jde o jediný
vrchol a m různých smyček. Algoritmus začne nulovou smyčkou v nulovém
vrcholu a dále volí největší dosud nepoužitou výstupní číslici.

Nejvýše m^k hran lze použít. V koncovém vrcholu odlišném od počátečního
by cesta použila o jednu vstupní hranu více než výstupní; z celkového
stupně m tedy ještě zbývá výstupní hrana. Zastavení proto nastane
v nulovém vrcholu. To dokazuje(a), včetně posledních k-1 nul.

Použité hrany nyní tvoří uzavřený tah, takže i nepoužité hrany mají
v každém vrcholu stejný vstupní a výstupní stupeň. Kdyby z nenulového
vrcholu v zbývala hrana, musela by zbývat i jeho hrana s číslicí 0:
tu algoritmus používá až po všech větších číslicích. Cíl této hrany
má nepoužitý vstup, tedy i nepoužitý výstup. Iterací nulové hrany
nejvýše k-1krát dospějeme do nulového vrcholu. Ten ale při zastavení
nemá žádný nepoužitý výstup. Spor dokazuje(b). Nulový vrchol samotný
nemůže být počátkem tohoto argumentu, protože je již vyčerpán.

Každá hrana se tudíž objeví právě jednou, n=m^k a délka lineárního
zápisu s koncovými nulami je m^k+k-1. Příklad m=k=3 v knize má
správných 29 číslic a přesně 27 různých oken. Hraniční k=1 i m=1 sedí.

## Úloha 21: vkládání nuly, seskupování a součin abeced

Do periody typu A vložme jednu nulu do libovolného běhu k-1 nul.
Takový běh existuje; pro m>2 jich obecně není jen jeden. Okna
zasahující přes jeho levý či pravý kraj zůstanou stejná, přibude
právě okno 0^k. Žádné staré okno délky k nemůže obsahovat současně
obě nenulové sousední číslice. Pro k=1 lze nulu vložit kamkoli.
Opačně z typu B smažeme jednu nulu z jedinečného běhu k nul.
Delší běh by opakoval okno 0^k. Tím vznikne typ A.

Nyní nechť p je prvočíslo a e=q*r, kde q je mocnina p a p nedělí r.
Začneme typem A nad p číslicemi s oknem e*k a periodou L=p^(e*k)-1.
Po seskupení q po sobě jdoucích číslic do jedné číslice v základu p
má nové okno r*k číslic přesně e*k původních číslic. Jeho počátek
má index q*n modulo L. Protože gcd(q,L)=1, projde každý původní
počátek právě jednou: dostáváme typ A s parametry(p^q,r*k).
Po vložení nuly má periodu p^(e*k). Seskupení r číslic opět zachová
všechna okna, protože gcd(r,p^(e*k))=1. Výsledek je typ B(p^e,k).
To ověřuje potřebnou jednoznačnost oken, nejen rovnost period.

Pro nesoudělná r,s kombinujme typy B(r,k) a B(s,k) původním vzorcem
Z_n=s*X_n+Y_n. Libovolná k-tice nad rs číslicemi se jednoznačně
rozloží po souřadnicích na dvojici k-tic nad r a s číslicemi.
Jejich jedinečné počátky určují pomocí čínské věty jediné n modulo
r^k*s^k, protože tyto periody jsou nesoudělné. Vzorec tedy dává
úplnou posloupnost typu B(rs,k). Stejně funguje explicitní čínské
kódování Z_n=s*(s^(-1) mod r)*X_n+r*(r^(-1) mod s)*Y_n modulo rs.

Erratum nahrazující původní vzorec prostým (X_n+Y_n) mod rs je
nesprávné; viz [C0012](C0012-complete-sequence-sum.md). Úloha13 dokazuje
součin period, ale nedokazuje jednoznačnost k-oken ani rekurenci řádu k.
Bibliografické údaje Rees 1946 ověřeny na vydavatelském záznamu
[článku](https://academic.oup.com/jlms/article-abstract/s1-21/3/169/845008).
Plný článek je za přístupovým omezením; uvedený důkaz je vlastní kontrola
knižní konstrukce, nikoli tvrzení o přečtení celého Reesova článku.

## Úloha 29: kontrola algoritmů X a Y

**Rotace** slova přesune některý počáteční úsek na konec.
Lexikografické porovnání používá první rozdílnou číslici.
Pro nenulové slovo w končící nenulovou číslicí definujme H(w): po
přesunutí všech počátečních nul na konec dostaneme největší rotaci w.
Pro pevný ocas s délky k-1 označme h největší kladné y<m s H(sy),
resp. h=0, když takové y neexistuje. Vlastnost platí právě pro y=1,...,h.

Zde je přímý důvod posledního tvrzení a správnosti Y. Nejsou-li všechny
číslice s nulové, i je první nenulová pozice. Rotace začínající před i
jsou automaticky menší. Pro j>i porovnáváme cyklické posloupnosti
začínající v i a j. Proměnná poslední číslice y se poprvé objeví
na pravé straně, při j+ell=k; na levé straně ještě není.
Dřívější první rozdíl tedy povolí všechna y, nebo žádné. Při dosavadní
rovnosti musí y být nejvýše levá pevná číslice c. Hodnoty y<c už
vyhovují přísně; pro y=c se pokračuje v porovnání. Jestliže později
vznikne opačná nerovnost, jediná možnost je snížit mez na c-1.
To jsou přesně čtyři větve Y2. Průnik těchto omezení je počáteční
interval kladných číslic a algoritmus jej postupně zkracuje.
Pokud je s celé nulové, i=k a všechna kladná y vyhovují bez volání Y.

Důležitý detail: v prázdném případě může Y dočasně vrátit a_k=-1,
například pro m=2 a vstup(1,1,0,0,1). Není to chyba výstupu:
X3 pak pro každé a_0>=0 použije první větev a vrátí a_0, stejně jako
při h=0. Správný invariant je max(0,a_k)=h. Test nejprve chybně
požadoval a_k=h; jeho vlastní příliš silný invariant byl opraven.
Pro triviální m=1 doplňuje implementace přímý výstup 0 před X2,
který by jinak hledal neexistující nenulovou číslici. Nevedeme tento
triviální okraj jako samostatný nález v konstrukci náhodného generátoru.

X3 proto vrací a_0 pro a_0>h, a_0-1 pro 1<=a_0<=h, a h pro a_0=0.
Ztotožnění tohoto pravidla s Martinovou posloupností má primární
oporu v [Amram et al., 2019](https://www.ece.mcmaster.ca/~schwam10/publications/MSjrnl39.pdf),
Definice 3 a Věta 4: po komplementaci číslic d↦m-1-d je jejich
„necklace head“ právě H. Jejich Lemma 7 odpovídá počátečnímu intervalu
přípustných y. Přečten důkaz Věty 4 včetně lemmat 6–9 na str. 227–230;
používá rozklad na Lyndonova slova. Tím je obecně ověřena identita
pravidla, nikoli jen jeho úplná perioda. Jejich novější lineární
implementaci z §4 zde neauditujeme. Náš přímý rozbor Y výše je
kontrolou konkrétního knižního pseudokódu.

Každé z nejvýše k-1 volání Y provede nejvýše k porovnání, tedy O(k²)
operací; paměť O(k). Knižní „perhaps O(log k) or even O(1)“ je výslovná
spekulace o průměru, nikoli dokázaná asymptotika. K jejímu potvrzení
nestačí naše konečné výčty, takže žádnou takovou mez netvrdíme.

## Reprodukovatelná kontrola a errata

`verify_complete_sequences.py` / `results/complete-sequences.json`:

- 60 dvojic m,k: 1<=m<=8, 1<=k<=12, m^k<=20000;
  všech 112716 stavů. Tři modely: doslovný hladový algoritmus,
  knižní X/Y a nezávislý výčet Lyndonových slov s komplementací.
  Porovnán celý cyklický pořádek, každá následující číslice a mez h.
- Devět konstrukcí prvočíselných mocnin, včetně e=6, tedy obou
  netriviálních seskupení. Po každém kroku ověřena přesná množina oken.
- Osmnáct kombinací nesoudělných abeced; původní vzorec i čínské
  kódování úplné, erratum vynechává maximální číslici.
- Explicitní C0012 nezávisle spočtena přímo z n mod2 a n mod3.

První výpočet dokončil celý Martinův blok, pak narazil na chybný
předpoklad **testu**, že typ A má jediný běh k-1 nul. Jeho log zachován
v `complete-sequences-first-pass.log`. Po opravě následoval úspěšný
běh `--resume` (exit 0), který už uzavřený Martinův blok neopakoval.
Seznam jeho 60 případů přesně rekonstruován z mezí cyklů a součet
112716 ověřen proti prvnímu logu; počty operací po jednotlivých
případech nebyly z nedokončeného prvního běhu uchovány.

Prohledány všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
a aktuální TeX, stažené1. 11. 2026. Změny: 8. 7. 2001 upraven hint 21
(a současně chybná náhrada na str. 556), 29. 7. 2006 opraven odkaz 29
na Fredricksen–Maiorana a Algoritmus 7.2.1.1F. Oprava 5. 4. 2026
odstraňuje zatoulané „(2)“ před číslem odpovědi 21; jde o sazbu,
nikoli o další změnu matematické kombinace. Na str. 38/555 k úloze17
žádná relevantní změna nalezena. Pozdější oprava C0012 nenalezena.

## Upřesnění souvislého průchodu 6. listopadu 2026

Dříve neevidovaný okraj m=1 je nyní samostatný nízký [C0240](C0240-unary-martin-alphabet.md). Úspěšný model měl větev navíc; tištěný X2 pro tento povolený vstup nemá hledaný index. Věta a algoritmus pro m≥2 zůstávají přijaty.
