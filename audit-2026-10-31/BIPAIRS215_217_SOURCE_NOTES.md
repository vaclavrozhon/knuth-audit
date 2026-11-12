# Celý zdrojový průchod 215–217

3. listopadu 2026. Zadání na str. 151, odpovědi 473–474 a související
odstavec hlavního textu 108 byly porovnány s autorovým draftem
(87, 177–178, 44). Všechny úlohy 215–217 mají dokončený průchod.
Přijaté výpočty se neopakovaly. F072/F073 zůstávají platné, nevzniklo
nové neopravené erratum. E098 dokumentuje již zapracované opravy 215(e,g).

## 215: obecné počty, stromy a náklady

Čtyři vrcholy mají tři perfektní párování; dvě taková párování tvoří
bipár. Proto je bipárů 3·C(2q+1,4). Při pevném pořadí hran vyhraje
jediné párování obsahující nejmenší ze šesti hran; ostatní dvě
jsou zakázané. Různé bipáry mohou zakázat stejnou dvojici, proto
je počet různých zakázaných čtveřic 2·C(2q+1,4), přesně dvě třetiny.
Pro K21 je tato hodnota 11 970.

Lexikografické pořadí povolí na a<b<c<d jen dvojici ab,cd. Při
větvení na nejmenší zbývající i skončí každá volba ij s j>i+1
izolací i+1. Jediná větev i(i+1) pokračuje stejnou úlohou na zbývajících
vrcholech. Profil je tedy 1,2q,2q−2,…,2 a celkem 1+q(q+1) uzlů.
**F072** opravuje 215(d): na úrovni l≥1 má být 2(q−l+1), nikoli
2(q−l). Nejmenší protipříklad q=1 má kořen a dvě děti; nesprávný
vzorec by první úroveň vynuloval. Kořenová úroveň 0 je výslovně
definována v hlavním textu str. 105.

Pro stejný strom stačí zákazy (i,j,k,l), kde i je sudé a
k=i+1<min(j,l). V dosaženém nekoncovém stavu už byly zvoleny
01,23,…,(i−2)(i−1); právě uvedené zákazy izolují i+1 po každé
špatné volbě ij. Při správné volbě i(i+1) se neuplatní a indukce
pokračuje. Počet je

`2·sum(r=1..q−1) C(2r+1,2) = q(q−1)(4q+1)/3 = Θ(q³)`.

Tato omezená instance má Θ(q²) hran a Θ(q³) datových uzlů.
V nekoncovém stavu s 2r+1 zbývajícími vrcholy má každá špatná
volba i j Θ(r) příslušných sekundárních položek. Ty odstraní
Θ(r) možností incidentních s i+1; každá z těchto možností má
Θ(r) datových uzlů. Cena špatné větve je tedy Θ(r²), takových
větví je Θ(r), a existuje jediná pokračující větev. Součet cen
Θ(r³) přes r=1,…,q dává **Θ(q⁴) mems**, včetně menších nákladů
na čtení vstupu a výběr MRV. To doplňuje obecný odhad z hlavní
strany 108; nejde o fit naměřených časů.

Chytré pořadí začíná disjunktními hranami 1(2q),2(2q−1),…,
q(q+1). Po kořenové volbě 0k se izoluje její partner
p(k)=2q+1−k. Stačí výslovně zakázat společný výběr 0k a p(k)l
pro l mimo {0,k,p(k)}: celkem (2q)(2q−2) různých zákazů.
Každá jiná hrana než 0k má nejvýše dva tyto sekundární výskyty,
zatímco 0k jich má 2q−2. Vstup, počáteční zakrytí sloupce 0
i všech 2q bezprostředně končících větví proto stojí **Θ(q²)**.
Dolní mez plyne již z velikosti explicitního vstupu. Strom má
1+2q uzlů; méně není možné, protože samotné přidání sekundárních
položek nezmění počáteční stupeň primárních položek 2q.

Všech 40 přijatých profilů pro čtyři konstrukce a q=1,…,10 bylo
pouze znovu načteno a hashováno, nikoli přepočítáno.
[Původní důkazy a F072/F073](MATCHING_BIPAIR_NOTES.md),
[přijatá data](results/matching_bipairs/native.json).

## 216: rozsah experimentu a F073

Původních 500 náhodných pořadí je nadále zachováno: 46 mělo některou
úroveň větší než lexikografické pořadí, žádné větší celkový počet
uzlů. Tyto omezené vzorky nejsou důkaz obecné maximální velikosti.
Přijatý krátký protipříklad **F073**, K7 s prvními hranami
12,13,23, má profil 1,6,2,4 proti lexikografickému 1,6,4,2.
Tvrzení o nejhorším případu na každé úrovni je tedy nesprávné.
Stejný celkový počet tohoto příkladu nevyvrací samostatně celkovou
mez. Původní svědek, přímý strom a výsledek DLX2 zůstávají beze změny.

Citovaný Algorithm 3.4.2S byl přímo zobrazen ve svazku 2, str. 142
(DjVu strana 154). Skutečně vybírá přesně n z N položek rovnoměrně;
tedy při N=11 970 a n=m vzorkuje požadovanou podmnožinu zákazů.
Odkaz je správný. Pracovní proud svazku 2 se neměnil.

Historické hodnoty **540 Gμ** a pro m=2000,4000,6000,8000,10000
přibližně **40 Gμ, 1,6 Gμ, 145 Mμ, 31 Mμ, 12 Mμ** výslovně
nereplikujeme podle pokynu uživatele. Závisí na konkrétních
náhodných podmnožinách a implementaci. Registr má `verified:false`.
Slova o obvyklém chování jsou experimentální pozorování, nikoli
ověřená univerzální věta. Další velké náhodné fronty se nespouštějí.

## 217: všechny obrázky odpovídají úplnému katalogu

Nový [zdrojový checker](check_bipairs215_217_sources.py) přečetl
barevné vektorové obrysy všech 36 vytištěných rozkladů odpovědi
a dvou rozkladů zadání. V každé verzi je to **38 obrázků, 76
pentomin, 380 buněk**. Každý dílek má správný geometrický typ,
barvu a přesně pět buněk; dvojice se nepřekrývají.

U prvních osmnácti obrázků dá druhý rozklad zrcadlení vlevo/vpravo,
u dalších čtrnácti transpozice. Zbývající dvě třídy mají vytištěné
oba rozklady a desetibuněčné oblasti bez netriviální symetrie.
Jejich osm otočených/zrcadlených poloh je opravdu různých.
Všech **34 kanonických klíčů** souhlasí přesně s dříve přijatým
katalogem. Žádný obrázek nechybí, žádný se neopakuje omylem.
Také celé algebraické přepsání žlutého S a zeleného Y v zadání
souhlasí s oběma původními obrázky.

Staré dva nezávislé úplné výčty 34 případů bez děr a sedmi s dírou,
všechna čísla delt a dřívější algebraické příklady zůstávají
přijaté; neprováděly se potřetí. Závěrečná podmínka bez děr je
výslovně doplněna v odpovědi, proto z jejího vynechání v zadání
nevzniká nový nález. Omezení rozdílu na k≤4 je úplné: při k=5
by se dvě polohy téhož dílku nepřekrývaly a kompenzující druhý
typ by musel být kongruentní s prvním, proti odlišnosti typů.

Nově doplněn malý čtyřpřípadový příklad z horní části str. 474.
Delta má kladné buňky 00,01,02,03 a záporné 20,21,22,23.
Zrušená buňka Q je 10 nebo 13, buňka Y je 11 nebo 12. Dvě ze
čtyř kombinací mají díru; zbývající dvě jsou kongruentní a dávají
jediný přípustný bipár, jak uvádí text. Žádný globální výčet.

[source-checked.json](results/bipairs215_217/source-checked.json)
má čas **1,111 s při nice 15**, bez nového solveru a bez opakování
přijatých výčtů. [Staré úplné důkazy](PENTOMINO_BIPAIR_NOTES.md)
zůstávají původní; tento záznam uzavírá jejich výslovnou mezeru
jednotlivě nepřepsaných obrázků.

## Původní Millerův článek a errata

Získán [původní ročník Eureka 23](https://archive.org/details/eureka-23),
PDF s původní archivní titulní stranou Archimedeans a kontrolním
SHA1 souhlasícím s metadaty. Titul ročníku výslovně uvádí říjen
1960. Článek J. C. P. Millera začíná na str. 13; citované strany
14–15 skutečně probírají lokální výměny. Obrázky 4 a 5 a pravidlo
(3) uvádějí přeskupení dvou sousedních dílků při zachování oblasti.
Odkaz v TAOCP je tedy obsahově i bibliograficky doložen.
Zobrazeny byly titul, str. 13–15 a archivní licenční list;
neprohlašujeme za auditované ostatní články ani všechna Millerova
číselná tvrzení o větších skupinách řešení.

**E098**: oprava 17. 2. 2022, Fascicle 5 str. 281, nahrazuje
215(e) uvedeným sousedním sudým minimem a mění chybný počet
(q−1)(q−3) v (g) na (2q)(2q−2). Naše kniha obojí již obsahuje,
draft 2019 nikoli. Primární TeX a zobrazená strana 15 úplných
errat souhlasí. Všech šest relevantních vrstev bylo prohledáno;
žádná odpovídající oprava F072 nebo F073 se nenašla.

Úloha 217 nemá zbývající obrázkovou ani bibliografickou mezeru.
Hlavní str. 108 zůstává částečná pro následující preprocessing,
zadání 151 pro 218–222 a odpovědi 474 pro 218–220.
Další blok začíná 218; celý svazek zatím dokončený není.
