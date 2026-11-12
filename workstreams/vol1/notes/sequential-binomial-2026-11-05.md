# Souvislý průchod §1.2.6: binomické koeficienty

5. listopadu 2026. Přímo přečteny původní strany 52–74 a odpovědi
483–491, včetně obou tabulek, tetraedrického obrázku, všech zadání
a rozšíření odpovědí. Strany souboru jsou o 15 vyšší. Celé dřívější
matematické poznámky byly znovu posouzeny proti sazbě; převzaté primární
prameny se posuzují jen v rozsahu jejich kořenových recenzí. Jejich celé
knihy znovu neprohlašujeme za přečtené. Uložené čtyři výsledkové JSON
soubory byly přečteny; úspěšné výpočty nebyly opakovány.

## Matematika a hranice platnosti

Pascalova tabulka, počet 20 bodů v tetraedru, číslo 635013559600
a jeho prvočíselný rozklad souhlasí. Základní polynomiální identity
zahrnují záporné celé dolní indexy podle nulové konvence. Symetrie
se nepřenáší bez podmínek na záporný horní index. Konečné diference
opravňují polynomiální pokračování; binomické řady a generující funkce
mají zvlášť zdůvodněnou konvergenci a správnou místní větev.

Rotheho a Abelovy zdánlivé podíly jsou nejprve zkráceny na polynomy.
Případ r+s=tn v příkladu 4 tedy není protiargument proti výsledku,
ale mezikrok s parciálními zlomky potřebuje dodatečný předpoklad,
který veřejná oprava doplňuje. U úlohy 25 nestačí malé z: pro t=r=1,
x=0 je z=0, ale řada má hodnotu 1 a x^r=0. Oprava vyžaduje x blízko 1.
Nové odvození příkladu 3 je kratší; původní konečná záměna součtů
je po ošetření nulových členů také správná.

Lucasův důkaz přes formální řady modulo p funguje i pro záporný celý
horní index. Kummerův důkaz zahrnuje koncový přenos a p=2. Konvoluce,
Pfaffův součet, dvojitý součet 63 a Dixonova q-identita mají konečné
důkazy pro uvedené obory, nikoli jen shodu několika vzorků.

Oba Stirlingovy trojúhelníky souhlasí s rekurencemi. Inverze, diagonální
polynomy stupně 2m, dualita a interpolační formule jsou správné.
Loganův rozvoj (59) má doloženou absolutní, lokálně stejnoměrnou
konvergenci pro Re(z)>0 a libovolné pevné komplexní r. (60) je konečný
asymptotický odhad; jeho nekonečná řada diverguje pro necelé r,
nikoli univerzálně i pro celá r. Celočíselné výjimky již vysvětluje
ověřená poznámka a Knuthův autorský článek. Nezakládáme z toho nový nález.

U beta integrálů byly ověřeny krajní body, limitování, gamma podíly
a rozlišení iterovaných limit. U Abelova nekonečného rozvoje je ocas
O(k^-2) na kompaktních množinách uvnitř analytického oboru; tento
odhad neodstraňuje nedefinované konečné členy na singularitách.
Nerovnost 66 platí ve staré i rozšířené podobě, včetně rovností na
hranici; původní důkaz používá z=n-1 zvlášť před dělením z-n+1.
Odchylka v úloze 68 teleskopuje na 2t_ceil(np), s oddělenými nulovými
případy. Část 53(b) nadále vyžaduje vyjasnění oboru.

## Nálezy a přesné umístění

- C0006: původní odpověď 58 na 489. Pro q=1/2,n=-1,x=3/4 jsou
  členy (-3/2)^k; nekonečný součin přesto konverguje k 2/5.
  Správný dostačující obor je |q^n x|<1 při 0<|q|<1 a pevné větvi.
- C0007: původní odpověď 42 na 487. Pro r=s=alpha=beta=-1/2
  je jediný nenulový součin při k=0 roven 1, ale C(-1,-1)=0
  podle výslovně předepsaného pořadí limit. Všechny koeficienty
  jsou konečné. První bilaterální binomický rozvoj je samostatné tvrzení;
  toto není jeho vyvrácení. Maximální opravený obor konvoluce netvrdíme.
- C0008: chyba ostrosti vzniklá spojením oprav 2005 a 2015.
  Pro n=2,y=z=1,x=2 je Y=0 a alpha=gamma=0. Důkaz se opraví
  neostrými mezikroky; obě závěrečné nerovnosti platí. Původní kniha
  z roku 1997 tento důkaz nemá, proto má strana 491 jen související
  vazbu na C0008, nikoli červenou značku způsobenou tímto nálezem.
- C0009: původní zadání 53(b) na 73 zůstává candidate.
  Při m=-1,n=1 vychází 0 versus 1. Dokázán je obor n>=1,m>=0;
  nelze jej automaticky vydávat za výslovně napsaný obor knihy.

Žádný z těchto nálezů není nový v tomto průchodu. Dnešní stažené
erratové zdroje mají shodné hashe s předchozí kontrolou; změna jejich
závěrů nenastala. Prvenství, Knuthovo přijetí ani fyzický dotisk
nejsou prokázány. Nevzniká žádný emailový návrh.

X0081–83 obsahují i rozšíření a redakční změny, které samy nejsou
chybami prvního dotisku. Do červené mapy se promítají jen konkrétní
původní vady: názvy a bibliografické údaje na 53,54,59,63; prefaktor
a meze na 60–61; překlep „of less“ na 64; term/factor na 65;
meze (56) na 68; obor úlohy25 na 70; atribuce33 na 71;
odpovědi21–22 na485, posuny28 a padající mocniny34 na486,
r→n na489, Dixonova počáteční strana na490, závorka q-exponentu
a chybějící nulový základ na491, k=0 v zadání67 na74.
Přejmenování combinadických indexů, širší úloha31 a nová úloha66
nevyvracejí původní správné formulace. Chybná značka řady (2) u JLMS
na66 byla zavedena až později; v našem originálu není.
Oprava jména de Moivre z1998 mění velké D na malé d. Omezení jeho
historického případu na celé np je už v původní odpovědi491;
starší souhrnná poznámka chybně spojila toto omezení s opravou1998.

## Přeskočená bibliografie a otevřená fakta

Úlohy 10,42,52,58,62,66,68 se nyní uzavírají v matematickém rozsahu
s výslovnými bibliografickými výjimkami. Uzavření úlohy neznamená,
že její text neobsahuje chybu: C0006/7/8 zůstávají samostatnými nálezy.
Výjimky se nepřepisují na ověřené prameny:

| Úloha | Přeskočeno |
|---|---|
| 10 | Dickson1902,383–384; ostatní citace již doloženy |
| 42 | Ramshaw1977,223–226; protipříklad na článku nezávisí |
| 52 | Původ soukromého Hautusova pozorování není určen |
| 58 | Rothe1811, Schweins1820, Gauss1808, Cauchy1843, Jacobi1846, Heine1847, Knuth1971 a doporučená Gasper–Rahman; žádné nové tvrzení o prioritě |
| 62 | MacMahon1902,274–288; Dixon, Rogers a Dougall již doloženi |
| 66 | Lovász13.31(a), Redheffer1996,62–64; vlastní důkaz nezávislý |
| 68 | de Moivre1730,101; Poincaré1896,56–60; Diaconis–Zabell1991,284–302 |

Přijaty přesné starší pramenné recenze X0693–94,X0701,X0710,X0719,
X0722,X0725–26,X0730; X0733 zůstává neúspěšným pramenným hledáním.
Nedošlo k opakování těchto neúspěšných rešerší bez nové stopy.
Doporučené externí asymptotické práce, Dutkova historie a další pasáže
CMath nejsou úplně auditovány; odkazy63 jsou přeskočeny, vlastní obecný
důkaz je úplný. Odkaz na rodinu trojúhelníků II4.7–21 zůstává zvlášť
přeskočeným křížovým odkazem, nikoli automaticky ověřeným cílem.

Hlavní historické odstavce zůstávají partial: stáří indických a čínských
výsledků, původ zápisu, Newtonova korespondence a výroky o Eulerově
a Gaussově prvenství, Karamatovo zavedení značek a Stirlingův původní
záměr. Tyto faktické výroky nejsou potvrzeny samotnou správností vzorců.
Průchod dalšího textu jimi není blokován.

## Rozdílný starší obrázek errat

`images/errata-all1-pre-file015.png` obsahuje „but sharper“, zatímco
aktuální stažený PostScript, společný PDF převod i text mají „but often
sharper“. Nový přímý render strany15 z dnešního hashovaného PostScriptu
toto potvrzuje; původní datum staršího obrázku není doloženo. Zachován
je starý soubor i nový obraz s manifestem
`sources/sequential-2026-11-05/binomial-current-images.json`.
Na tomto místě rozhoduje aktuální zdroj, nikoli starší náhled.
Při n=k=2 je zlepšená mez e/8<1 oproti (n/k)^k=1; slovo „often“
proto věcně záleží. V aktuálních erratech tato námitka není chybou.
Stejným přímým renderem zkontrolována strana33 all1-prepre;
kombinovaný protipříklad C0008 se potvrzuje i v aktuálních zdrojích.
