# Souvislý průchod §2.6 — 6. listopadu 2026

Celé původní obrazy457–465 znovu přečteny, včetně poznámek pod čarou,
citátů a pokračování odstavců. Porovnány přijaté důkazy, původní
čtecí záznam, jednotky H01–H68/Q01–Q03 a nynější čtyři vrstvy errat.
Nový výpis má22 výskytů13 různých změn; tematický zásah mimo oddíl
je jen rejstřík. Žádná nová chyba ani nový výpočet. Nula původních
a nula přidaných úloh potvrzena. Neopakoval se celý audit primárních
článků; přesný dříve přečtený rozsah zůstává v read-log.md.

## Matematika a technické výroky

457: příklady bubnové paměti n+7/n+18 vysvětlují rotační čekání;
nejde o univerzální čas všech strojů. Samomodifikace adres při
průchodu polem je doložena konkrétní rutinou V1 ve WWG1951.
Konkrétní historické zrychlení šestkrát či sedmkrát z celého
Knuthova článku1961 však doloženo není.

458: zápisy INFO(P)/LINK(P) mohou být realizovány jako pole
indexovaná adresou P; P.INFO je jiná konvence, nikoli jiná
matematická datová struktura. Argument s proměnným číslem pole
uzlu je srozumitelná motivace značení, ne tvrzení o sémantice
všech programovacích jazyků.

459: trojadresové mezivýsledky reprezentují uzly rozvinutého
stromu výrazu. Sdílení společného podvýrazu by mohlo tvořit DAG,
ale text netvrdí, že libovolný sdílený program musí být strom.
Obousměrné nezávislé seznamy Sketchpadu jsou vazby uvnitř jedné
struktury, nikoli důkaz historické nezávislosti jejího objevu.

460: Pawlakovy termíny nelze mechanicky prohodit. Číslování,
pořadí provádění a pořadí operací v zápisu programu jsou různé:
v základních L1/L1bar dává vhodné zrcadlení skutečně dvojici
postfix/prefix. Přijatá kvalifikace a root-review obsahují
konkrétní strom a obě posloupnosti. Žádný potvrzený rozpor se
z této nejednoznačnosti nevyrábí.

461: přijatý úplný Weizenbaum1963,524–544 včetně programové
přílohy nyní uzavírá starou mezeru H32. Rozsah536 v některých
metadatech je neúplný. Kruhové dvojité spoje, referenční počítadla
a dokumentované rutiny jsou doloženy; nejde o nové ověření
každé instrukce SLIPu. U IPL-V jsou vlastnictví a půjčování
podseznamů doloženy manuálem; odpovídající tvrzení pro FLPL
zůstává neověřené. McCarthyho značení dosažitelnosti a následující
sweep jsou primárně doloženy. Comfortův rukopis1961 přímo
popisuje alokaci a slučování; není to četba časopisecké sazby1964.

462: počet12 systémů u d’Imperio potvrzují přímo abstrakt a úvod
autorského strojopisu. Nečtená sazba1969 je bibliografická výjimka,
nikoli důvod ponechat samotný počet neověřený. Rozlišení datové
struktury, implicitního sousedství v paměti a explicitních spojů
odpovídá konstrukcím kapitoly. Přečtené úvody Mealyho a Hoara
i Englesův abstrakt dokládají charakter doporučené četby.

463: model má pevné počty polí k/r a registrů l/s, rovnost
ukazatelů, vytváření uzlů a přenos hodnot; nemá aritmetiku adres.
Odkazy na5/6 míří na řazení a vyhledávání,9/10 na plánované
kapitoly, jak je již vymezeno v předmluvě. Plánovaná kapitola
není vydávána za skutečně přečtenou publikaci.

464: znovu přezkoušen celý obecný důkaz konstantní simulace.
Je-li q pevný počet typů, mají vrcholy nejvýše q sousedů.
Okolí pevného poloměru n má nejvýše B=1+q+...+q^n vrcholů.
Konečně mnoho pravidel vytváří nejvýše pevný počet W uzlů.
Uzel lze reprezentovat typem a q ukazateli na sousedy podle
jejich typu. Konečný počet cest délky≤n najde celé okolí;
rovnost ukazatelů rozezná opakované vrcholy. Lokální přepis,
obousměrné hrany i případná úprava hran u hranice potřebují
jen konstantně mnoho operací. Reprezentační invariant se
zachovává indukcí; nedosažitelné staré uzly lze ponechat jako
odpad. To je časový důkaz, nikoli důkaz optimální paměti.
Opačný směr je v knize výslovná domněnka, ne prokázaná mez.
Pevná šířka b bitů dovoluje nejvýše2^b−1 nenulových adres.
Fyzikální číslo10^30 a soud o praktické věrnosti modelu jsou
ilustrace a hodnocení, nikoli obecné fyzikální věty.

465: Lehmerův citát je doložen původní142 a programem sympozia
1949, přestože sborník vyšel1951. Knižní varianta Conan Doyla
má stejné pořadí slov jako TAOCP; odlišný časopisecký slovosled
není nová chyba. Rok1888 je již opravené erratum na1914.

## Přeskočené bibliografické podrobnosti

Podle aktuálního pokynu se znovu neobcházejí již doložené
nepřístupné články a vydání. Následující údaje nejsou označeny
za ověřené. Příbuzná primární verze nenahrazuje přesnou sazbu.

- 457: CW V113–116, přesné GMD63(1972), Garwick137–140,
  Mauchlyho Lecture37 a Luhnovo původní memorandum.
- 458: přesné články a konferenční poznámky IPL1956/57,
  Carrův plný článek a Rossův úplný příspěvek1961.
- 459: Schlatterch7, přesná paginace ACE1986, KLS1962,
  Hellerman/Gower, Kahrimanian, RC390/603, Salton a celé
  Perlis–Thornton196–204.
- 460: Holtova disertace, přesný termín subtree order v RC390/603,
  Oettinger203–224, Gorn223–240, FLPL87–101, Bobrow–Raphael
  časopiseckých231–240 a Woodward–Jenkins47–53 za abstraktem.
- 461: přesná sazba historie LISP1981, COMIT1963, SNOBOL1964,
  Collins1960/66 za abstraktem, Weizenbaum1964 dopis38,
  Cohen–Trilling22–30 za abstraktem, EULER1966, Lawson1967,
  identifikace Hoare262–284 v Bobrow1968 a Comfort1964.
- 462: plné Knowlton1965/66 a Markowitz1963, SASP339–346,
  Berztiss512–513, Ross481–492, d’Imperio1969 proti strojopisu,
  kompletní obsahy sympozií CACM1960/66, Earley617–627.
  U doporučení dalších zdrojů se nevyžaduje audit celých článků.
- 464: samostatný Kolmogorov1953 a překlad AMS1963; model
  i dataci1952 dokládá přímo ruský originál1958.
- 465: původní Carrollovy galley proofs1896/97 a Bartley1977/86;
  jde o citát přidaný erraty, který původní strana1997 neobsahuje.

## Faktické mezery, které výjimka neuzavírá

457: sepsání von Neumannovy pasáže1946, Zuseho proměnné seznamy
a prvenství1945, Dunlap/CITRUS a jejich chronologie, zrychlení6–7×,
Mauchlyho původ a Luhnovo rané řetězení. 458: konkrétní datace
IPL-II/III a jarní/letní sezóna, Carrův a Rossův prvenstevní soud.
459: historie názvů stack/deque a nezávislost Dijkstrova zavedení,
první přehledy polí/stromů a diferenciace, vývoj vláken.
460: priority vláken, přesná data IPL-V/FLPL a dosud nedoložené
historické názvy pořadí. 461: přesná chronologie LISP1958/59,
FLPL vlastnictví, Collinsovo prvenství a vlastní svědectví
o boundary tags/B5000 roku1962. 462: Markowitz/Knowlton a jejich
nezávislost. Tyto výroky zůstávají výslovně neověřené.
„Perhaps“, „unlikely“ a doporučující soudy nejsou absolutní
matematické či prvenstevní výroky. Dobové „nowadays“ se nečte
jako tvrzení o roce2026.

Proto457–462 zůstávají stránkově partial;463–465 jsou reviewed
s výše uvedenými oddělenými bibliografickými výjimkami.
Celá §2.6 zůstává partial. To nebrání dokončení souvislého
průchodu a pokračování na další části knihy.

## Známé opravy a přesné lokace

X0659 mapuje skutečné původní obsahové opravy na457,458,460,
461,462,465: Cambridge;61–79; úplné tituly IPL-V a Part I;
Collins578–589; sympozium547–643 a Engles1–64; Holmes1914.
Oprava gramatiky457, kapitalizace Fortran460, doplnění rozsahu
d’Imperio a nový Carrollův citát samy nejsou další obsahové vady
původního dotisku. Uvozovky Carrollova Tree2024 se týkají až
vloženého citátu. Zachováno13 historických změn, bez nového nálezu.

Další krok: doplnit chybějící samostatné stránkové záznamy
odpovědí466–467 a projít dodatky619–627 i rejstřík628–650.
