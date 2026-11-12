# §4.2.1: přesná aritmetika a hraniční zaokrouhlení

Kontrola 2. listopadu 2026. Celé214–228 a odpovědi611–613
přečteny vizuálně. Tento blok dokládá matematické algoritmy A/N/M
a úlohy1–5,7–13,16–18. MIX a zbývající úlohy uzavírá
[mix-float.md](mix-float.md); historický rozsah a jeho omezení
[single-precision-context.md](single-precision-context.md). Čtení stránky není samo
uzavřením všech jejích tvrzení. Nový interpretační kandidát je
[C0082](C0082-balanced-floating-rounding.md), nikoli potvrzená chyba.

## 1. Model a normalizace

Používáme konvenci třetího vydání: základ b>=2, počet cifer p>=1,
exces q a dvojice(e,F), kde F je celé, |F|<b^p. Její hodnota je
`F b^(e−q−p)`; knižní zlomek f tedy znamená F/b^p. Nenulové
normalizované číslo má b^(p−1)<=|F|<b^p. Nula nese nejmenší dovolený
exponent. V modelu s proměnným rozsahem se musí tato konvence dodržet
zvlášť: samotný nulový zlomek s libovolným exponentem není normalizovaný
vstup algoritmu A.

Násobení f základem a současné snížení e zachovává hodnotu; analogicky
při dělení a zvýšení e. Pro nenulové f skončí kroky N2–N3, protože
b>1. Před zaokrouhlením je |f| v[1/b,1). Nejbližší dva body mřížky
b^(-p) jsou zároveň nejbližší dvě plovoucí hodnoty, s možností souseda
±1 přes horní hranici exponentu. Dolní hranice1/b sama patří do mřížky,
takže žádný bližší bod s menším exponentem neunikne. To dokazuje,
že N poskytne nejlepší plovoucí aproximaci. Při zaokrouhlení na±1
je další dělení základem přesné; nenastává nebezpečné dvojí zaokrouhlení.

Pro sudé b vybírá rovnost vzdáleností celé k s lichým k+b/2. Tedy
b=2,10 dává sudé k, zatímco b=4,64,100 liché k. Pro liché základy
N výběr neurčuje; reproduktor používá v rovnosti větší absolutní
hodnotu, což je přípustná volba. Rozsah exponentu se kontroluje až
po normalizaci a zaokrouhlení.

Rozsahy úlohy2 plynou přímo z krajních e,F. Skrytá nejvyšší jednička
úlohy3 je přesně známá u každého nenulového normalizovaného binárního
čísla; jeden exponentový kód lze vyhradit nule. Tím se uloží p bitů
významové části pomocí p−1 bitů. Historické prvenství Zuse1936 není
součástí tohoto matematického argumentu.

## 2. A/M a potřebná přesnost

Po srovnání exponentů v A je přesný zlomek součtu
`fu+fv b^(ev−eu)`. Pro rozdíl exponentů nejméně p+2 je absolutní
hodnota druhého členu menší než b^(-p−2). Nejmenší vzdálenost od
normalizovaného fu k jeho sousedu je b^(-p−1), a to při přechodu
přes dolní hranici exponentu. Vynechaný člen je menší než polovina
této vzdálenosti, protože 1/b<=1/2. A4 je tedy bezpečný i tam.
Pro menší rozdíl stačí2p+1 cifer, neboť posun činí nejvýše p+1.

Vzorce M2 po dosazení hodnot dvojic dávají přesně součin a podíl.
Nenulový součin má |fw|>=1/b²; podíl fw=fu/(b fv) má |fw|>1/b².
Proto normalizace vlevo potřebuje nejvýše jeden krok. Pro podíl
s |fu|<|fv| je po tomto případném kroku

```text
1/b < |fu/fv| <= 1−b^(−p)/|fv| < 1−b^(−p).
```

Pro |fu|>=|fv| je normalizovaný zlomek |fu/(b fv)| v
`[1/b,1−b^(−p)]`. Nikdy tedy nezaokrouhlí na1. Dolní nerovnost
ve druhém případě musí být neostrá; právě to opravuje erratum2006
k odpovědi12. U násobení naopak může vzniknout přetečení po jednom
posunu vlevo, jak ukazuje správný příklad11.

V úloze5 značí x~y stejnou celočíselnou část po dělení b a stejnou
ze čtyř kategorií zbytku:0, mezi0 a b/2, rovno b/2, mezi b/2 a b.
Přičtení celého násobku b tuto vlastnost zachová. Dělení b ji zachová
také: nové hranice kategorií buď leží na celém původním bloku, nebo,
pro liché b, na jeho půlce, kterou kategorie již rozlišují.
Zaokrouhlení x a y na celé číslo je stejné při **bx~by**, nikoli
při pouhém x~y; oprava2000 je nutná.

Člen b^(p+2)fu je násobkem b; vztah~ tedy přejde ze zkráceného
fv na celý součet. Pokud se fv skutečně změnilo, rozdíl exponentů
je nejméně2 (pro rozdíl0,1 je jeho škálovaná hodnota násobkem b).
Jeho velikost i velikost náhrady zůstávají pod b^(-2). Pro náhradu
to plyne z polohy hranic±b^p v souřadnici b^(p+2)fv, které jsou
násobky b. Proto |fu+fv|>b^(-1)−b^(-2)>=b^(-2), totéž pro náhradu;
normalizace vlevo má nejvýše jeden krok. Opakovaným dělením vztahu~
dostaneme shodné zaokrouhlení v každé možné výsledné poloze.

Pro sudé b>2 lze zvolit celočíselného zástupce všech kategorií.
Pro b=2 otevřené intervaly(0,1),(1,2) neobsahují celé číslo, ale
obsahují půlcelé zástupce: nutný dodatečný bit vysvětluje p+3.
Pro liché b se přesná půlka nevyskytne u konečných b-adických
vstupů sčítání a násobení; v dělení nastat může. Tím jsou vysvětleny
všechny výjimky na612.

## 3. Příklady a směrované zaokrouhlení

Úlohy4,8–11 byly přepočteny přesnými zlomky. Čtyři výsledky4 včetně
poznámky o změně poslední cifry souhlasí. V8 jsou výsledné exponenty
−1,−1,100,100; jde opravdu o podtečení a přetečení rozsahu0..99.
Příklad9 po nahrazení podtečených výsledků nulou dává
66666667/100000000 v prvním pořadí a přesně1 ve druhém. Příklady10
sledováním N dávají přetečení až v kroku zaokrouhlení; v11 nejprve
nastane jeden posun vlevo.

Konverze1 souhlasí pro původní i opravené hodnoty(3). Důležitý rozdíl:
(3) již obsahuje zaokrouhlené desetinné konstanty. Přímé zaokrouhlení
přesného nynějšího10h do základu100 by v rovnosti vzdáleností volilo
66260701, zatímco převod hodnoty h z(3) vede k66260702 uvedenému
v erratech2020. Proto zde nejde o doloženou chybu řešení1.

Pro13 stačí podržet přesný výsledek, normalizovat a v N5 místo
nejbližšího bodu vzít podlahu či strop b^p f. Horní přechod na±1
se normalizuje přesně. **V A4 se nesmí prostě zahodit nenulový malý
sčítanec**: pro vnější mez může být nutný soused fu. Reproduktor
proto pro směrované operace tuto zkratku vypíná. Obdobně je třeba
při zkracování uchovat informaci o nenulovém zbytku. U konečného
rozsahu je nutná explicitní politika, když požadovaná mez není
reprezentovatelná; zde dokazujeme případ reprezentovatelných mezí.

Yoheho citovanou práci se zatím nepodařilo získat: oficiální
technická zpráva AD0713699 vrací403. Obnova X0203 našla i odkaz
na desetistránkový časopisecký sken, ale nedostala čitelný obsah.
[Úplná obnova13](recovery-floating-directed-2026-11-06.md) doplňuje
sousedy na hranicích pásem, všechny změny A/N/M a konečné kraje.
Je to vlastní důkaz, nikoli předstírané přečtení Yoheho algoritmů.

Poznámka o postupném podtečení na222 má jednoduchý důvod:
všechna čísla včetně nenormalizovaných při nejmenším exponentu0
jsou násobky h=b^(−q−p). Součet i rozdíl jsou také násobky h.
Je-li jejich velikost menší než nejmenší normální číslo, jsou
tedy přesně reprezentovatelné; žádný další podtečený zbytek nevznikne.
Obecně lze zvolit chybu x−round(x) jako x delta v normální oblasti,
|delta|<=b^(1−p)/2, a jako epsilon v malé oblasti, |epsilon|<=h/2.
To dokládá tvar vztahu v poznámce; historická atribuce X8 se prověřuje
s dalším kontextem.

## 4. Vyvážená trojková soustava (7)

Cifry jsou−1,0,1. S p místy je největší absolutní zlomek
(1−3^(−p))/2; nejmenší s nenulovou první cifrou je
(1+3^(1−p))/6. Tištěné rozmezí1/6<|f|<1/2 tedy správně
charakterizuje takto normalizované konečné zlomky.

Konec konečného rozvoje za p-tou cifrou má absolutní velikost
striktně menší než3^(−p)/2. **Při pevné poloze řádové čárky**
je tudíž odříznutí cifer rovno zaokrouhlení. Ve sčítání stačí
p+1 míst; úplný důkaz s rozlišením znamének, polohy čárky,
přenosu a mřížkových vzdáleností nyní obsahuje
[obnova celé7](recovery-floating-balanced-2026-11-06.md).
Starý stručný argument o přesnosti při rozdílu exponentů0/1
opomíjel celočíselný přenos u stejně orientovaných sčítanců.
Pro dělení může konec rozvoje dosáhnout poloviny kroku.

Tento argument nedokazuje nejlepší aproximaci v celé plovoucí
soustavě. Pro p=2 součet2/9−4/81=14/81 po normalizaci a odříznutí
vrátí2/9, ačkoli soused4/27 je dvakrát blíž. To je přesně vymezený
kandidátC0082. Rozlišení pevné a plovoucí polohy řeší význam
závěru; žádná z výše uvedených správných vlastností se neruší.

Navržené uložení exponentu za první cifru se zdůvodní lexikograficky:
kladné normalizované číslo začíná1 a jeho velikost nejprve určuje
exponent, teprve pak ostatní cifry. U záporných čísel opačné pořadí
exponentů získáme změnou jejich znamének. Tím se zachová pořadí
při porovnání jako pevných vyvážených trojkových slov; nulu je třeba
uložit zvláštním nulovým slovem.

## 5. Komplexní dělení (16)

Nechť c+di!=0. Při |c|>=|d| je c nenulové a r=d/c má |r|<=1.
Pak s=c+rd=(c²+d²)/c a

```text
(a+br)/s=(ac+bd)/(c²+d²),
(b−ar)/s=(bc−ad)/(c²+d²).
```

Druhá větev s r=c/d je obdobná a obě přesně dávají podíl.
Pomocné součiny rd,rc nepřekročí velikost příslušného d,c;
nevznikne umělý kvadratický mezivýsledek c²+d². To splňuje zadání,
ale **není to záruka proti každému možnému přetečení**: například
s může překročit rozsah, když c a d jsou oba blízko jeho horní
hranice. Kniha takovou univerzální záruku výslovně nedává.
Erratum2010 přidává nenulový jmenovatel a upozorňuje na podtečení r.
Čtyři symbolické identity byly nezávisle ověřeny krácením polynomů.

## 6. Proměnná přesnost v pevném slově (17)

Zadání je výzkumné, ne věta o jediné optimální soustavě. Vlastní
úplný příklad má16 bitů: znaménko s, dva bity j volící délku
exponentu k z{1,2,4,8}, k bitů pro exponent e ve dvojkovém doplňku
a t=13−k zbylých bitů pro F. Hodnota je
`(−1)^s (1+F/2^t)2^e`, 0<=F<2^t. Vždy zvolíme nejmenší přípustné
k pro dané e. Významová část je tak jednoznačně v[1,2) a kódování
je prosté; nekanonický kód j1,e0,F0 lze vyhradit nule.

U e0,−1 máme13 významných bitů. U krajních exponentů−128,127
jen6 bitů; rozsah kladných hodnot je od2^(−128) do(63/32)2^127.
Běžné stejně dlouhé rozdělení1+5+10 by mělo11 významných bitů
a exponent pouze−16..15. Příklad tedy skutečně směňuje přesnost
a rozsah podle velikosti exponentu. Zaokrouhlení lze přesně definovat
výběrem bližšího ze sousedních hodnot této konečné množiny; na
hranicích délek k se musí použít skuteční sousedé. Jediná uniformní
relativní mez podle maximální přesnosti13 bitů tam neplatí.

Morrisův primární [patent US3742198](https://patents.google.com/patent/US3742198A/en),
podaný19.3.1971, popisuje tentýž základní princip pole určujícího
délku exponentu. Přečten titul, obrázky a sloupce1–4 originálu.
Naše16bitová konstrukce není přepis jeho36bitového příkladu.
Samotný IEEE článek1971 se nepodařilo otevřít přes ověřovací stránku;
tento rozdíl ve zdrojích se zachovává. Neověřujeme každou vedlejší
numerickou formulaci patentu ani tvrzení o prvenství Cockeho.

## 7. Dvojkový doplněk (18)

U kladného výsledku se posouvá, dokud zlomek neleží v[1/2,1),
a po zaokrouhlení se případná1 posune zpět. Pro záporný zlomek
je zrcadlový interval[−1,−1/2), protože nejvyšší uložený bit0
značí hodnotu pod−1/2. Zaokrouhlení na−1 dá nulové pole zlomku,
ale **není to skutečná nula**: musí se aritmeticky posunout na−1/2
a upravit exponent. Tím se obnoví normální kód hranice−2^k.
U ostatních výsledků zůstává zlomek v požadovaném intervalu a jde
o přesně tutéž nejbližší aproximaci jako při práci s velikostí.

Obě vytištěné ukázky proto dávají575|400000000 a576|000000001.
Nezávislý převod jejich hodnot přes znaménkovou velikost souhlasí;
4057 dalších záporných normalizací pro2..8 významných bitů také.

## 8. Reprodukce a errata

[Model](../float_model.py) odděluje přesnou hodnotu a postup N/A/M.
[Kontrola](../verify_single_precision.py) používá jako nezávislé
orákulum explicitně seřazenou množinu reprezentovatelných hodnot,
ne druhé zavolání normalizace. [Výsledky](../results/single-precision.json)
se ukládají po blocích. První běh zachoval hotové algoritmy a ochranné
cifry, ale úloha9 měla v našem modelu nesprávný exponent nuly0 místo−50;
po opravě byly spuštěny jen zbývající bloky. Jde o chybu modelového
vstupu, nikoli knihy. Doplněné dva bloky pak prošly samostatně.

170632 operací,114118 směrovaných součtů,95678 zkrácených součtů
a712 vztahových kontrol prošlo. Další konkrétní počty jsou v JSON.
Konečné kontroly doplňují obecné argumenty výše, nenahrazují je.

Prohledány all2-prepre, all2-pre, all2, err2 a aktuální TeX
(snímek9.6.2026). Relevantní bloky jsou uloženy v
`sources/single-precision-errata-excerpts.txt`. Opravy1999/2020
mění konstanty;2007 popisek Fig.2;2002 MIX program a časování;
2000 podmínku bx~by;2006 neostrou nerovnost v12;2010 komplexní
dělení;2023 místo vydání historické knihy. Žádná oprava7 nebyla
nalezena. Plánované změny konvence pro čtvrté vydání nejsou
uplatňovány jako změna tohoto třetího vydání.
