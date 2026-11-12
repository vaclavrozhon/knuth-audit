# Obnova 4.1: úvod a strany 194–198

Přečteny původní 194–198 a následný kontext 199–202; tento uložený
blok posuzuje pouze tvrzení do konce 198. Originály 196–198 znovu
vizuálně, včetně všech zlomků, indexů a tabulky 2π. Celé staré
`positional-context.md` a `positional-basic.md` přečteny; z kódu
`verify_positional_basic.py` byly pro tento blok přečteny pomocné
funkce a celý blok printed_numbers, nikoli tvrzeno provedení programu.
Celý `verify_positional_context.py` a uložené výsledky rovněž přečteny.
Žádný starý výpočet ani hledání se neopakuje.

## Epigrafy a předmět kapitoly na 194

La Touche: originály uloženého vydání 1908, strany 49–50, znovu
vizuálně. Hlavička dopisu uvádí červenec 1878. Text odpovídá epigrafu,
včetně singularu Number a přiznané výpustky. Výrok o odlišném součtu
při obráceném pořadí je osobní humor, nikoli matematická věta knihy.
Pro konečný součet přesných reálných čísel totiž asociativita a
komutativita dávají stejnou hodnotu. Rukopis dopisu se tím neověřuje.

Parlett: celá uložená úvodní strana 1.1 Coonenovy disertace přečtena
a znovu zobrazena. Má stejnou větu a atribuci B. N. Parlett (1979).
Je to konkrétní rané písemné svědectví, ne záznam původního výroku ani
statistický průzkum zájmů numerických analytiků. Celá disertace se
tím neoznačuje za přečtenou.

Napier: uložené strany 379, 381–382 přetisku 1834 přečteny textově,
382 opět vizuálně. 379 uvádí anglické vydání 1616, předmluva obsahově
odpovídá epigrafu. Přetisk má modernizovaný pravopis a například
calculations, kde TAOCP píše Calculators. Bez originálu 1616 přesnou
pravopisnou shodu neuzavíráme: **skip bibliography** pro originál,
nikoli nový nález proti citaci. Tvrzení o namáhavosti výpočtů je
historická motivace, ne kvantifikovaná dolní časová mez.

Wales: původní obraz konkrétní pasáže 1936 nebyl získán (uložené
metadata HTTP 503). Starý indexovaný výňatek o existenci diskuse
nenahrazuje celý citát: přesné znění a atribuce **skip bibliography**.
Soud o potřebném množství násobení je dobový názor, nikoli vlastnost
aritmetického algoritmu.

Dva úvodní odstavce vymezují čtyři základní operace a plán kapitoly:
plovoucí čísla, velká celá čísla, zlomky, polynomy, mocninné řady,
převody, faktorizace a vyhodnocování. Jde o obsahové vymezení;
například dělení nepřidává implicitní slib definovaného výsledku pro
nulového dělitele. Hodnocení významu a zajímavosti není univerzální
výkonnostní věta. Důvod spojení reprezentace s aritmetikou je přesný:
stejný přenos jednotky do sousední pozice znamená faktor zvoleného
základu, a proto pravidla pro cifry závisejí na reprezentaci.

## Definice, konvergence a každý pojem na 195

Rovnice (1) definuje hodnotu jako součet a_j b^j. Pro konečný zápis
je b≠0 dostačující k definování všech celých mocnin, včetně záporných.
Hornerův invariant po každé další cifře je hodnota přečteného prefixu:
V←bV+a. Pro n cifer jde o n násobení/přičtení v aritmetickém modelu;
netvrdíme lineární bitovou cenu při růstu operandů.

Nekonečný zápis musí navíc konvergovat v zvoleném smyslu. Pro |b|>1,
shora omezené pozice a omezené cifry pravý ocas konverguje absolutně
geometrickou majorantou. Pro 0<|b|<1 se obdobně obrací strana, kde
lze mít nekonečný ocas. Věta „libovolné nenulové b a zvolená množina
cifer“ neříká, že pro každou takovou volbu dostaneme všechny hodnoty,
jednoznačnost nebo konvergenci libovolného oboustranného zápisu.
Případy |b|=1 ani formální rozvoje pozdější úlohy 7 se nesmějí
bez dalšího vydávat za konvergentní reálné řady.

Příklad je po všech členech
`(520.3)_6=5·36+2·6+0+3/6=180+12+1/2=192½`.
Desítkový případ znamená b=10 a cifry 0 až 9, vynechání indexu je
jen konvence. Pro celé b≥2 a cifry 0 až b−1 vzniknou uvedené binární,
ternární, kvartérní a kvintérní soustavy; každé nezáporné celé n má
konečný zápis: opakovaně n=bq+r, 0≤r<b, a q<n pro n>0. Zbytky
určují cifry i jednoznačnost bez úvodních nul.

Pro zlomkovou část x∈[0,1) volíme d_j=floor(bx_(j−1)),
x_j=bx_(j−1)−d_j. Invariant je
`x=sum_(j=1..N) d_j b^(−j)+x_N b^(−N)`, 0≤x_N<1;
zbytek mizí. U dvou různých rozvojů první rozdíl na pozici k může
být vyrušen jen maximálním geometrickým ocasem:
`sum_(j<k)(b−1)b^j=b^k`. Rovnost vynutí rozdíl cifry právě jedna
a všechny další cifry b−1 oproti nule. Tím jsou vysvětleny právě
obvyklé dvě reprezentace končících hodnot, ne fiktivní plná
jednoznačnost reálných zápisů.

Řádová čárka odděluje váhy b^0 a b^(−1). Slova decimal/binary point,
leading/trailing a významné cifry jsou zavedené konvence. Pro kladný
standardní základ roste váha s indexem; u obecného b tato terminologie
není tvrzením o uspořádání komplexních hodnot. Nekonečný ocas nemusí
mít poslední cifru. Bity označují cifry 0/1; šestnáct symbolů 0–9,A–F
zastupuje hodnoty 0–15, nikoli šestnáct různých číselných základů.
Známé doplnění 2008 dovoluje též malá a–f. Historické geografické
užívání čárky a zvýšené tečky není tímto definičním důkazem doloženo;
konkrétní zdroj nebyl dodán, zůstává partial.

## Každý číselný mezikrok na 196–198

V babylonském modelu bez uvedeného měřítka reprezentuje stejný
mantisový řetězec třídu násobků 60^k. Proto 2, 120, 7200 a 1/30
odpovídají 2·60^k pro k=0,1,2,−1. Dvojice mantis v součinu mění
výsledek jen mocninou 60, protože (u60^r)(v60^s)=uv60^(r+s);
podíl obdobně, v≠0. Historická existence tabulek je jiná otázka.

Příklad čtverce 30 má 30²=900=15·60. Čtení s posunutou čárkou má
(30/60)²=1/4=15/60. Dále `(1 21)_60=60+21=81`.
Reciproční mantisa je
`(44 26 40)_60=44·3600+26·60+40=160000` a
`81·160000=12960000=60^4`, takže jde přesně o 1/81 při měřítku
60^(−4). Její čtverec má hodnotu mantisy
`32·60^5+55·60^4+18·60^3+31·60^2+6·60+40=25600000000=160000²`.
Měřítko je 60^(−8), tedy 1/6561. Každá vytištěná cifra i její
váha jsou tím pokryty; přebíráme i shodný archivní přesný výsledek.

Kořen na 197: f(x)=x³+2x²+10x−20 má
`f′(x)=3(x+2/3)²+26/3>0` pro každé reálné x, a limity opačných
znamének na ±∞. Proto existuje právě jeden reálný kořen. Archivní
přesný zlomek s ciframi
`1;22,7,42,33,4,38,30,50,15,43`
je r=827665919577540943/604661760000000000. Uložená přesná kontrola
vyhodnocuje f(r)<0<f(r+60^(−10)); kód obou stran byl nyní přečten.
Monotonicita tedy dokazuje všech deset tištěných šedesátkových míst.
Fibonacciho příklad končí po šestém místě cifrou 40 místo skutečného
38 následovaného nenulovým ocasem. Je tedy větší než kořen a chyba
leží přísně mezi 60^(−6) a 2·60^(−6). Text slibuje aproximaci,
ne správné zaokrouhlení posledního místa. Atribuce Fibonacciho není
součástí tohoto numerického důkazu.

Výhoda pro 1/3: v základu 60 je to konečné `.20`; v desítkové
soustavě nemůže být rovno a/10^k, neboť 3 nedělí 10^k. Nekonečný
rozvoj `.333…` má hodnotu (3/10)/(1−1/10)=1/3. Jednotky stupňů,
minut a vteřin používají násobení 60; jejich úplný historický rodokmen
se z této algebraické identity nevyvozuje.

Řetězec osmi čínských jednotek s deklarovanými desetinovými poměry
na 198 dává přesně 3.1415927. Archivní racionální interval pro π
jej umísťuje nad π s chybou přibližně 4.641·10^(−8), menší než
5·10^(−8); jde o správné zaokrouhlení na sedm desetinných míst.
Původ názvů jednotek, průměr hedvábného vlákna, autorství a rozšíření
po 1250 jsou samostatné historické údaje, zde nedoložené.

Příklad složeného úroku dává pro n=1,2,3,4,5 postupně
148.5, 163.35, 179.685, 197.6535, 217.41885, vždy násobením
předchozího čísla 11/10. Tištěný prefix odmocniny 3.162277 je také
přesný jako prefix: 3162277²=9999995824729 < 10·10^12,
ale 3162278²=10000002149284 > 10·10^12. Tedy
3.162277<sqrt(10)<3.162278. Nejde o údaj zaokrouhlený na šest míst.

Tabulka al-Kášího obsahuje dvě celočíselné buňky 0,6 a šestnáct
zlomkových buněk 2,8,3,1,8,5,3,0,7,1,7,9,5,8,6,5, tedy
6.2831853071795865. Celá mantisa v obrázku byla porovnána. Starý
printed_numbers dokládá chybu <10^(−16); silnější archivní interval
pro π v positional-context, z Machinovy identity, umísťuje 2π do
`(6.28318530717958647692528676655900576,
  6.28318530717958647692528676655900578)`.
Odchylka tabulky je tedy kladná a <5·10^(−17), takže souhlasí i
běžný význam správného zaokrouhlení na šestnáct míst. To není
nezávislé potvrzení prvenství nejlepší historické aproximace.

Machinova identita se nepřebírá bez předpokladů: pro a=atan(1/5)
platí tan(2a)=5/12, tan(4a)=120/119. S t=atan(1/239) dává vzorec
pro rozdíl tan(4a−t)=1. Úhel 4a−t je v (0,π/2), proto π/4.
Násobení čtyřmi dává použitou identitu. Alternující řady pro oba
arctangenty, 70 a 24 členů v uloženém kódu, svírají hodnoty dvěma
sousedními součty; kombinace dolních/horních mezí respektuje záporné
znaménko druhého členu. Starý certifikát na 35 míst tedy stačí pro
obě právě uvedené přesnosti; žádný nový výpočet π nebyl spuštěn.

„Turecké“ násobení: 153.5=307/2 a 16.25=65/4, takže součin
19955/8=2494.375. Historická přezdívka není důsledkem výpočtu.
Známé doplnění Mádhavy 2023 má podle uloženého přesného intervalu
`2827433388233−9·10^11π` mezi 2.186 a 2.187. Je to uvedená
aproximace, ne správné zaokrouhlení celého čísla; příslušná chyba π
leží mezi těmito mezemi dělenými 9·10^11. Sanskritský pramen se
nepovažuje za přečtený.

## Každé historické tvrzení a zdrojová hranice

Následující inventář přiznává chybějící doklady jednotlivě. Výraz
skip znamená **skip bibliography**, nikoli nepravdivost tvrzení.
Algebra z předchozího oddílu se nesmí použít jako důkaz dat či prvenství.

| Místo a tvrzení | Přesný rozsah |
|---|---|
|195: nejstarší skupiny prstů/kamenů, zvláštní náhrady pěti/deseti, vztah k babylonským/egyptským/řeckým/čínským/římským zápisům|Archeologické a etnografické zdroje nepřečteny, skip. Srovnávací „nepohodlnost“ není opatřena modelem ceny a zůstává kvalitativní.|
|196: dvě babylonské soustavy, obchodní skupiny po deseti/stu, dědictví Mezopotámie a řídké velké hodnoty|Konkrétní hliněné tabulky ani úplné historické studie nepřečteny, skip.|
|196: rozvoj kolem 1750 př. n. l., kontextové měřítko, nula jen uvnitř|Matematický model výše funguje; datování a skutečné užívání znaků skip.|
|196: Neugebauer 1952|Celá kniha skip.|
|196: van der Waerden/Dresden 1954|Celá kniha a konkrétní překlad skip.|
|196: Knuth CACM 1972, 671–677|Celý původní článek skip.|
|196: Knuth CACM 1976, 108|Samostatná pozdější položka skip.|
|196: mayské prvenství před 2000 lety, základ 20, astronomie a kalendář|Historický rozsah a přesné směšování vah nelze prokázat pouhou definicí základu, skip.|
|196: mayská nula kolem 200, ničení knih, nalezené násobení a absence dělení|Každé z těchto tvrzení vyžaduje pramenný/soupisový doklad; ty nebyly přečteny, skip.|
|196: Thompson|Převzata známá oprava 1942/37–62 na 1941/37–67; obsah celé práce skip.|
|196: Justeson|Známá náhrada příslibu plnou bibliografií 2001 a oprava italského názvu 2011; obsah skip.|
|196–197: řecký abakus několik století př. n. l., desítkové řady, nepřevedení do zápisu, snadnost a gramotnost|Historické doklady skip. Přisuzované úvahy Řeků jsou v textu domněnka, nikoli dokázaná psychologická příčina.|
|197: řecké astronomické šedesátkové zlomky a přenos z Babylonie|Prameny přenosu nepřečteny, skip.|
|197: indický původ, odhad 600, astronomie, nejstarší obrácený směr a pozdější ustálení|Každé datování, prvenství a orientace rukopisů skip; „good guess“ je výslovně nejistý odhad.|
|197: přenos do Persie kolem 750, arabské překlady, Ibn Ezra/AMM 1918|Celý hebrejský pramen a anglický překlad skip.|
|197: al-Khwarizmi, etymologie algorithm, latinské překlady, Fibonacci 1202 a evropský vliv|Původní knihy a konkrétní etymologický doklad se v tomto bloku nepřebírají z pouhé zmínky, skip.|
|197: zachování pořadí číslic při dvou přenosech a směry ostatního písma|Konkrétní historické rukopisy skip; nejde o důkaz odvozený ze současných zvyklostí.|
|197: D. E. Smith I (1923), kapitoly 6 a 8|Celý uvedený rozsah skip.|
|197: původně jen celé desetinné hodnoty; arabské, ptolemaiovské a evropské šedesátkové tabulky|Historické rozsahy a cesta k dnešním jednotkám skip; číselné vztahy výše dokázány.|
|197: Fibonacciho autorství konkrétní aproximace|Primární text skip, hodnota a chyba příkladu doloženy.|
|197–198: čínské prvenství, chybějící nula a desítkové míry|Konkrétní historické doklady skip; staré „nikdy sexagesimály“ už opravuje erratum 2021 na „jen zřídka“.|
|198: Zu Chongzhi, délkové názvy, rozšíření po 1250|Výpočet 3.1415927 uzavřen; autorství/jednotky/rozšíření skip. Úmrtí je známým erratem upraveno na 500 nebo 501.|
|198: al-Uqlidisi v Damašku 10. století, příklady, vliv a zapomenutí|Celé uvedené strany 110,114,343,355,481–485 nepřečteny, skip. Rok překladu je zvlášť uzavřený C0233, nikoli tato historie.|
|198: al-Samaw'al 1172 a možnosti zápisu|Numerický prefix odmocniny doložen, původní text a tvrzení o zápisu skip.|
|198: al-Káší, úmrtí 1429, nový objev a prvenství přesnosti do van Ceulena|Číslo 2π doloženo; životopis, prvenství a konkrétní originální výpočet skip. Interval van Ceulena už opraven na 1586–1610.|
|198: turecký příklad, Bianchini před 1450, Rudolff 1525, Viète 1579, Stevin 1585, popularizace/logaritmy|Násobení doloženo; každý historický bod skip. Bianchiniho doplnění 2001 se nepovažuje za nové vlastní ověření.|
|198: D. E. Smith II (1925), 228–247|Celý rozsah skip.|
|198: Katz 1993 a později upřesněné stránky|Celý citovaný rozsah skip.|
|198: Rosińska 1995 v dodatku|Celý článek skip.|
|198: Mádhava/Nílakantha v dodatku 2023|Numerika výše uzavřena; komentář ke Gaṇita §10 a historické autorství skip.|
|198: párové počítání v kulturách, Seidenberg 1960, 215–300|Celá etnografická práce skip. Skupiny po dvou samy neurčují zvláštní pozice vah 2^k: logické rozlišení je správné.|
|198: hudební příklad|Půlení základní délky dává geometrické váhy 2^(−k); platí pro tuto běžnou řadu délek, ne tvrzení, že každá rytmická délka včetně triol je dyadická.|

C0233 se přebírá v úplném přesném rozsahu: přečteno celé odůvodnění
v `powers-history.md` §2 a report; obraz 198 i vydavatelská tiráž
znovu vizuálně. Tiráž výslovně udává první pevnou vazbu 1978, nikoli
1975. Nejde o záměnu s pozdějším digitálním vydáním. Původní nález má
uložené porovnání všech vrstev errat a zůstává stejným nálezem, nikoli
novým C-ID. Všechny zde uvedené známé opravy se do nálezů nepřidávají.

Starý X0133 je otevřen partial: seznam přečtených stránek nemůže
zastoupit jednotlivé důkazy. Zbývá od 199/file211, pokračování historie,
potom vlastní podepsané/záporné soustavy a všech 34 úloh. Dopředný
kurzor 418/file430 zůstává držen. Tento blok nepřidává uzavření úloh.
