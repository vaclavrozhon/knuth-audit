# Souvislý průchod §2.3.4.6 — 5. listopadu 2026

X0978. Přímo přečteny všechny části oddílu na 406–408 a 597–601.
Přezkoušeny oba obecné důkazy, celý correspondences.py, přesné
pramenné meze H01–H25/A01–A05 a pozdější doplňky X0889/X0893.
Matematické testy se neopakovaly. Nový nález nevznikl, C0070 trvá.

## Čtyři úlohy a doplňky

1: při pevné základně má triangulace jediný přilehlý trojúhelník,
který určuje levý a pravý podpolygon. Rekurze je obousměrná;
n vnitřních uzlů odpovídá n+2 stranám. Dvojúhelník je formální
prázdný základ. V obrázku 597 souhlasí všech devět trojúhelníků,
závorkování (((01)2)((3(45))((67)(89)))) i dřívější strom.

2: disekce r-úhelníku k diagonálami dává uspořádaný strom
s r−1 listy a k+1 nelisty, bez stupně 1, tedy N=r+k vrcholy.
Pozice nelistů a rozdělení přebývajících stupňů dávají
binom(r+k,k+1) binom(r−3,k) posloupností. Cyklické lemma
se součtem sum(1−d_j)=1 poskytuje právě jeden přípustný začátek
z N pozic; kratší perioda by odporovala součtu 1. Výsledek
dělíme r+k. Krajní k=0 i k=r−3 souhlasí. Konvexita je nutná
a je doplněna známým erratem 2023.

3a: maximální pravé řetězce preorder očíslovaného binárního
stromu jsou neprotínající se části. Levé hrany spojují j s j+1
při začátku nové části. V obou směrech rozdělení do mezer
dokazuje nekřížení a inverzi. Při k částech je k−1 levých hran
a n−k pravých, tedy převod na les dává n−k+1 listů; po záměně
levé a pravé k listů.

3b: binární slovo s m nulami, n jedničkami a k výskyty 01 má
počet binom(m,k)binom(n,k), rozložením na běhy. U špatného
vyváženého slova změníme nulu za posledním globálním minimem
na jedničku. Inverze mění jedničku při prvním globálním minimu
slova s rozdílem −2 zpět na nulu. Počet 01 se nezmění.
„Good“ zde znamená nezáporné prefixy, nikoli nutně nulový
celkový součet. Známý chybný parametr 1 musí být k.
Odečtení dává N(n,k)=binom(n,k)binom(n,k−1)/n, 1≤k≤n.
Prázdný les n=k=0 má zvlášť počet 1; faktoriály tam nejsou
definované. Znění příkladu 0010101001110 skutečně dává (7,6,4).

Svaz Dyckových cest má bodové minimum a maximum a je
distributivní. Neprotínající se rozklady obsahují pro n=3
M3; Tamariho uspořádání obsahuje N5. To přímo dokazuje
uváděný rozdíl, ne jen odlišné názvy tří rodin.
Doplněk 2024 pro l×n rozklady s hodnotami nejvýše 2:
dvě vnořené Ferrersovy hranice, zrušení protínajících dvojic
výměnou ocasů a determinant dávají
binom(l+n,l)^2−binom(l+n,l−1)binom(l+n,l+1)
=N(l+n+1,l+1). Prázdný rozměr má správně počet 1.

4: u friezu s m−1 kladnými řádky přidáme nulové hranice.
Lokální determinant 1 vede indukcí k
F(t,u)F(v,w)+F(t,w)F(u,v)=F(t,v)F(u,w).
Míra (w−t)m+(u−t)+(w−v) klesá ve vytištěných případech;
vedlejší součet nepřesáhne rozpětí. Při krácení jsou příslušné
vnitřní hodnoty kladné. Před odvozením symetrie je chybný
faktor (v,u) místo (u,v) skutečně nedefinován: známá oprava.
Dosazení na hranici dává klouzavou symetrii a periodu m.

Pro m≥3 existence jedničky druhé řady plyne z
d_(j+2)=a_(j+1)d_(j+1)−d_j: všechna a≥2 by nutila neklesající
diference, přesto první je 1 a poslední −1. Odstranění této
jedničky znamená odstranění ucha triangulace. Vložení má
F(x,y)=F(p,y)+F(q,y) a zachovává kladnost i celočíselnost.
Vektorová determinantová konstrukce dokazuje obecnou identitu;
rekurze z druhého řádku dává nezávislost na pořadí odstranění uší.
Druhý řádek počítá přilehlé trojúhelníky. Hodnoty 1 jsou přesně
hrany triangulace; hodnoty 2 jsou opačné diagonály sousedních
trojúhelníků. V základní oblasti je obojího m−3 pro m≥3.

Matice L a R připojují větve a transpozice obrací cestu.
Celá matice (*) souhlasí s násobením; m=2 je identita.
Každá nezáporná celočíselná matice s determinantem 1 má kromě
identity porovnatelné sloupce. Odčítání menšího od většího
jednoznačně odebírá poslední písmeno a snižuje součet prvků,
což dokazuje jediný rozklad do L/R. Pro kontinuant je faktor
i^(1−k+j) správný: při substituci i*a se plus změní na minus.
Párovací interpretaci dokazuje odstranění ucha a rozlišení,
zda sousední vrchol dostane jeho trojúhelník. Prázdné párování
na hraně má počet 1. Oba vytištěné číselné pásy mají přijaté
úplné kontroly; konečné výpočty se nyní znovu nespouštěly.

## C0070 a přesné chybové lokace

Na 599 je m=2 výslovně zahrnuto, proto ho nelze dodatečně
vyloučit z domény. Na 600 má jeho řádek 2 samé nuly, žádnou
jedničku. Na 601 je základní oblast prázdná a má 0 jedniček
i dvojek, nikoli m−3=−1. Obě pomocná tvrzení potřebují m≥3;
hlavní bijekce s prázdným stromem je správná. Lokace jsou
pouze 600 a 601, nikoli správné zadání 408 ani základ 599.
Závažnost medium zůstává. Nejde o nový nález v tomto průchodu.

Čerstvé čtyři vrstvy errat obsahují stejných 20 různých
oprav/doplňků; C0070 mezi nimi není. Oprava n>0 na 597
patří úloze 3, ne friezům. Přehled: tree-history-errata-extract.json.
X0588 se jako původní matematické/faktické vady mapuje na:
407 (Eulerova atribuce), 408 (konvexita), 598 (parametr k
a rok Poupard 1971), 600 (pořadí argumentů a rok 1973).
Změna pravopisu König, rozlišení čísla Brouwerova pojednání,
přejmenování lokálních indexů a doplněné citace nejsou samostatné
matematické vady. „To appear“ bylo v roce vydání 1997 namístě;
pozdější rok 1999 není zpětnou chybou původního skenu.
Špatný ročník 64 u Dershowitze–Zakse vznikl až v dodatku 2006,
oprava na 62 v roce 2022 neopravuje původní knižní sazbu 1997.

## Historický obsah a výslovné výjimky

Všech 25 jednotek hlavního textu je přiřazeno k pramenům nebo
konkrétně přeskočené kontrole. Přijaté přímé doklady zahrnují
von Staudta 1847; vymezené autorovy přetisky Cayleyho prací;
Borchardta a Jordana; Königovo lemma E; Eulerův dopis 4.9.1751;
sedm francouzských příspěvků; Stanleyho 66 a pozdějších 214
interpretací; Coxeterovo pojmenování; Sylvesterův determinant;
Moonův přehled; Pólyovy relevantní části; Huffmana a Zimmermana.
Přesné rozsahy zůstávají v původních sources.md; převzetí
není další novou úplnou četbou cizích knih. Úvod o třetím dni
je biblická slovní hříčka, nikoli empirická časová osa.

Podle současného pokynu se přeskakují tyto samostatné kontroly:
- Kolace Kirchhoffovy původní sazby 1847 a anglického překladu
  1958 proti přečtenému autorovu přetisku; původní časopisecké
  stránkování Listinga a Sylvestera proti dostupným přetiskům.
- Vyčerpávající prvenství a doložení Cayleyho neznalosti
  Kirchhoffa/von Staudta; nezávislost Borchardta, Listinga,
  Prüfera a Zimmermana. Absence citace není důkaz nezávislosti.
- Königova kniha 1936, kapitola 6; přesné historické předpoklady
  Brouwerova výsledku 1919 a Heyting 1956 §3.4.
- Mingova původní kniha, Luo 1988:239–245 a 1993:68–70;
  přesné předrokové prvenství a absence kombinatorické interpretace.
- Prüfer 1918:143–144 a Harary 1967:1–41.
- Samostatné původní články Kreweras 1972, Poupard 1972,
  Edelman 1982 a Dershowitz–Zaks 1986; celý obsah nepřečtených
  částí Edelman 1980 se netvrdí. X0889 již doložil §4 překladu
  Krewerase 2005 a nezávisle ověřil jeho výčet, ne francouzskou sazbu.
- Conway–Coxeter 1973b:175–183 a Broline–Crowe–Isaacs 1974:171–176.
  X0893 již uzavřel všech sedm citovaných stran Conway–Guy 1996;
  stará mezera pro ně neplatí.
- Rukopis Eulerova dopisu proti přetisku, samostatná atribuce
  nepodepsaného summary a širší historické soudy o motivacích.

Tyto neověřené historické údaje zůstávají výjimkami, nejsou prohlášeny
za pravdivé. Žádná otevřená matematická pochybnost se nepřeklasifikovala
na bibliografii. Přesné mezisvazkové cíle 4.5.3-32 a 7.2.1.6-26 až34
již zkontroloval dřívější root; nejde o audit celých cizích úloh.
Hlavní text a všechny čtyři úlohy jsou v novém vymezeném průchodu
checked s výjimkami. Strany 406–407 a 597–600 jsou celé pokryté;
408 a 601 mají ještě část následujícího oddílu.
