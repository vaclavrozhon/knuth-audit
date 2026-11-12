# §2.3.4 a §2.3.4.1: obecné důkazy a jednotlivé úlohy

Auditované vydání je třetí vydání, první dotisk (1997). Přečteny byly původní
obrazy s. 362–371 a odpovědí 578–580. Část s. 362 před nadpisem §2.3.4 a část
s. 580 od nadpisu §2.3.4.2 sem nepatří. Historická tvrzení a zdrojové mezery jsou
odděleny v `sources.md`; opravy vydání v `errata.md`. Nález v odpovědi 12 má
samostatný, zmrazený podklad `prim-answer12.md`.

## 1. Pojmy, obrázky 29–30 a Theorem A

**Graf** zde znamená neorientovaný graf bez smyček a násobných hran. **Sled** je
konečná posloupnost sousedních vrcholů, **cesta** takový sled bez opakování
vrcholů a **cyklus** uzavřený sled délky aspoň tři, v němž se kromě prvního a
posledního vrcholu žádný vrchol neopakuje. Toto je terminologie errata z roku
2008; první dotisk říká obecně „path“ a pro neopakující se sled „simple path“.
**Volný strom** je souvislý graf bez cyklu. Pro srovnání: knižní „tree“ má navíc
kořen a pořadí synů; názvoslovný úvod §2.3.4 neurčuje nový matematický objekt.

Obrázek 29 má hrany AB, AC, BD, CD, BE, DE. Má tedy pět vrcholů, šest hran a
uvedené dvě cesty délky dva z B do C. Obrázek 30 má 14 vrcholů a 13 hran
AC, BC, CD, CG, FG, EF, GH, HI, HM, FK, JK, KL, KN; je souvislý, tedy strom.
Přesný přepis a nezávislé prohledání jsou v `check_figures.py`.

Pro libovolný, případně nekonečný graf jsou ekvivalentní:

1. Souvislost a nepřítomnost cyklu.
2. Souvislost a rozpad souvislosti po odebrání každé hrany.
3. Jediná cesta mezi každými dvěma různými vrcholy.

Pokud v grafu bez cyklu po odstranění hrany uv zůstala cesta z u do v, tato
cesta spolu s uv tvoří cyklus. Naopak hranu cyklu lze odstranit, neboť její
použití v libovolném sledu lze nahradit zbytkem cyklu. Dvě různé cesty se
někde poprvé rozcházejí a později poprvé znovu setkávají; úseky mezi těmito
místy tvoří cyklus. Cyklus také dává dvě různé cesty mezi sousedními vrcholy.
Tyto argumenty pracují jen s konečnými sledy, takže nepotřebují konečnost
celého grafu. Případ vrcholu se sebou řeší sled délky nula.

Pro konečný neprázdný les, tj. graf bez cyklu, platí `m = n - c`, kde n je
počet vrcholů, m počet hran a c počet komponent souvislosti. Důkaz: v každé
netriviální komponentě vezměme nejdelší cestu; její krajní vrchol má stupeň
jedna, jinak by šla prodloužit nebo by vznikl cyklus. Odebereme tento list a
jeho hranu, čímž n i m klesnou o jednu a c se nezmění. Po opakování zbývá c
izolovaných vrcholů. Proto acykličnost a `m=n-1` vynucují `c=1`. Souvislý
graf obsahuje kostru: postupně mažeme hrany cyklů, dokud žádný nezbude. Kostra
má n−1 hran. Má-li už původní souvislý graf právě n−1 hran, žádnou hranu jsme
smazat nemohli, takže byl stromem. Tím jsou dokázány i části d/e Theorem A.

Knižní důkaz listu ve starém dotisku vybíral libovolný vrchol, ačkoli může být
izolovaný. To je známé erratum z 2. 9. 1997. Nové chyby v Theorem A nenalezeny.
Kniha výslovně předpokládá `n>0` pro konečné ekvivalence d/e. Prázdný graf
proto není protipříklad.

## 2. Toková báze a Theorem K

U orientovaných hran je **tok** libovolné reálné číslo přiřazené každé hraně.
**Zachování toku** znamená, že součet příchozích toků se v každém vrcholu rovná
součtu odchozích toků (první Kirchhoffův zákon). Podkladový neorientovaný graf
je souvislý; text tuto vlastnost grafů vzniklých z vývojových diagramů výslovně
uvádí na s. 365. Smyčky a rovnoběžné hrany lze buď rozdělit pomocnými vrcholy
jako v knize, nebo s nimi pracovat přímo, viz úloha 9 níže.

Zvolme kostru T. Každá hrana e mimo T uzavírá s jedinou cestou v T jeden
**fundamentální cyklus**. Orientujme tento cyklus ve směru e; jeho vektor c_e
má koeficient +1 na hranách souhlasných s oběhem, −1 na protisměrných a 0
jinde. Jeho tok se zachovává. Na hranách mimo T je koeficient c_e roven 1
právě u e a 0 u všech ostatních takových hran.

Libovolně zadané reálné hodnoty x_e na hranách mimo T tedy rozšíříme na celý
graf předpisem `f = sum_e x_e c_e`. Rozšíření je jediné: rozdíl dvou rozšíření
je zachovávaný tok podporovaný na T. Pro každou hranu stromu rozděluje její
odstranění vrcholy na dvě části; součet rovnic zachování toku přes jednu část
je, až na znaménko, právě tok této hrany. Musí tedy být nula. To je současně
obecný důkaz úlohy 4. Konečnost je podstatná: na oboustranně nekonečné cestě
orientované jedním směrem může mít každá hrana tok 1.

Je-li hran m a vrcholů n, má kostra n−1 hran a prostor zachovávaných toků má
rozměr `m-n+1`. Matice rovnic zachování toku má proto hodnost n−1; součet všech
jejích řádků je nula a další nezávislá závislost není. Čísla v tomto odstavci
se týkají již uzavřeného grafu, včetně případné pomocné hrany e0.

Pro původní diagram Start–Stop s m hranami a n vrcholy přidáme e0 ze Stop do
Start a zvolíme kostru bez e0. Ta existuje, protože původní diagram je
souvislý. Uzavřený graf má `m-n+2` fundamentálních cyklů. Cyklus c_0 bez e0
je fundamentální cesta Start–Stop, případně s některými zápornými koeficienty;
ostatních cyklů je `m-n+1`. Při podmínce `E0=1` má každý tok jednoznačný tvar
fundamentální cesta plus lineární kombinace ostatních cyklů. Rozdělení hrany
přidá současně jednu hranu a jeden vrchol, takže rozměr nemění. To dokazuje
lineární část Theorem K a uzavírá příslušný dopředný odkaz z §1.3.3.

Pro skutečný běh diagramu jsou všechny toky nezáporné celé a jejich kladná
podpora souvislá. Tyto podmínky jsou také postačující v grafovém modelu knihy,
který nezná sémantická omezení programu. Nahradíme každou hranu E_e kopiemi a
přidáme jednu kopii e0. Dostáváme konečný orientovaný multigraf, v němž se
vstupní a výstupní stupeň každého vrcholu rovnají a podklad kladných hran je
souvislý. Začneme chodit po nepoužitých odchozích hranách. Zastavit se lze jen
ve výchozím vrcholu: v jiném vrcholu jsme zatím použili o jednu příchozí hranu
víc než odchozích, proto zbývá odchozí hrana. Vznikne uzavřený tah. Zůstanou-li
nepoužité hrany, souvislost podpory a rovnost zbývajících vstupních/výstupních
stupňů zaručí nepoužitou odchozí hranu v některém vrcholu již vytvořeného tahu.
Odtud vytvoříme další uzavřený tah a vložíme jej do předchozího. Po konečně
mnoha krocích máme Eulerův tah obsahující všechny kopie. Rozříznutím u e0
dostaneme požadovaný sled Start–Stop. Tím je dokázána i opačná část Theorem K
a tvrzení odkazující na §2.3.4.2-24; vlastní text a odpověď té další úlohy zde
ještě nejsou auditovány.

Ve výroku Theorem K jsou „počty průchodů“ celočíselné. Samotné nezáporné
reálné řešení by na realizaci sledem nestačilo; bezprostředně předcházející
odstavec celočíselnost výslovně stanoví. Nepovažuji její neopakování v téže
formulaci za nový nález.

## 3. Přesná kontrola příkladu na s. 365–369

Původní obrázek 31 má 19 vrcholů a 27 hran; po přidání e0 a rozdělení e13/e19
má obrázek 32 celkem 21 vrcholů a 30 hran. Deset vynechaných hran kostry je
`0,2,5,8,13d,17,19d,20,21,25`; značka d znamená druhou polovinu dělené hrany.
Skript `check_figures.py` vychází z koncových vrcholů hran a kostru nezávisle
prohledá. Takto nalezené cykly přesně souhlasí se všemi deseti tištěnými cykly
(3). Všechny jejich incidence jsou nulové. Z těchto cyklů nezávisle odvozených
souhlasí všech 20 rovnic (6), včetně znamének u E21 a E25. V (6) je proto
opravdu transponována matice tištěných cyklů.

Rovnice `E0=1`, `E2=2`, `E8=0` dávají E3=−1, jak říká s. 368. Další příklad
s `E19d=1`, ostatními nezávislými proměnnými nulovými a `E0=1` dává kladnou
cestu Start–Stop a oddělený dvouhranový cyklus K–L; nelze jej projít v jednom
sledu. Oba příklady tedy správně oddělují zachování toku, nezápornost a
souvislost kladné podpory.

## 4. Úlohy 1–7

**1.** Z B přes A je další krok v jednoduchém cyklu vynucen C a potom D. Z D
se vracíme přímo do B nebo přes E. To dává BACDB a BACDEB a jejich opačné
orientace. Bez A a C zbývá trojúhelník BDE se dvěma orientacemi. Celkem právě
šest cyklů vyjmenovaných v odpovědi 578. Přesný nezávislý průchod téhož grafu
je zaznamenán v `results/figures.json`.

**2.** Zvolme sled nejmenší délky mezi danými vrcholy. Kdyby opakoval vrchol na
pozicích j<k, vynechání úseku mezi těmito pozicemi jej zkrátí. Proto jde o
cestu. Jsou-li krajní vrcholy totožné, minimum je sled délky nula. Terminologii
odpovědi aktualizuje známé erratum 2008.

**3.** Přičtení c_2 ruší hrany e3 a e4 fundamentální cesty a nahrazuje je e2.
Výsledný sled má hrany `1,2,6,7,9,10,11,12,14`, přesně jako odpověď.

**4.** Obecný důkaz přes řez stromu je v oddílu 2. Knižní důkaz listem podpory
je rovněž správný, i když některé toky jsou záporné: vrchol podpory stupně jedna
má rovnici `±E_e=0`.

**5.** Všech patnáct rovnic A,…,S souhlasí se součty příchozích toků; nezávislá
kontrola je součástí `check_figures.py`. Devět původně nezávislých toků lze
z vrcholových toků získat zpět:

```
E8   = A-1       E2   = A-B       E5   = A-D
E13d = G-1       E17  = J         E21  = J-H
E20  = Q         E19d = K-Q       E25  = S.
```

Tedy se ani při přechodu na vrcholové toky v tomto konkrétním diagramu žádný
z devíti stupňů volnosti neztratí. Stejně označené boxy C mají stejný tok
`1+E8`; pomocný box ONE má tok 1. To odpovídá s. 365 i odpovědi 5.

**6.** Udržujeme rozklad vrcholů na komponenty dosud vybraného lesa. Hranu
přijmeme a vytiskneme právě tehdy, pokud její konce leží v různých komponentách;
potom tyto komponenty spojíme. Indukčně nevytváříme cyklus a komponenty lesa
jsou přesně komponentami všech dosud čtených hran. Po zpracování všech hran
tedy máme kostru právě při jediné komponentě; jinak ohlásíme neúspěch.
V propojeném případě se počet komponent zmenšil z n na 1, takže jsme vytiskli
přesně n−1 hran. Pro n=1 je výstup prázdný a úspěšný. Toto je přesně použití
Algorithm 2.3.3E uvedené v odpovědi; jeho interní implementace patří kořeni a
nebyla zde znovu testována. Alternativní prohledání do hloubky z jednoho vrcholu
v čase O(n+m) vytiskne hrany, jimiž poprvé objeví vrchol, a ověří dosažení všech
vrcholů. Tím je obecná účinnost alternativy dokázána. Přesná implementace
Algorithm 2.3.5A a obsah §7.4.1.2 zůstávají budoucími křížovými odkazy.

**7.** Po přidání e0 má obrázek šest vrcholů a deset hran; pět hran kostry je
1,2,3,4,9. Nezávislé prohledání této kostry dává všech pět cyklů uvedených na
s. 578 a rovnice

```
E1=1, E2=E5-E6, E3=E5-E7-E8,
E4=1+E6-E7-E8, E9=1-E8.
```

Výsledky jsou přesné koeficientové identity, nikoli pouze test dosazených toků.

## 5. Úloha 8: redukce vrcholových toků

Spojujeme dvě hrany e:u→v a f:u→w pocházející ze stejného původního vrcholu,
sečteme jejich toky na S a případně spojíme cílové vrcholy. Již sloučené
supervrcholy nesmějí vést k novému slévání toků různých původních vrcholů;
výsledkem má být právě jedna hrana pro tok každého původního vrcholu.
Ukážeme, že každý reálný zachovávaný tok výsledného grafu lze rozštěpit zpět.

Ve všech třech případech jsou toky ostatních hran už známy. Výraz
`d(x)=ostatní odchozí toky z x - ostatní příchozí toky do x` zahrnuje jen hrany
jimž se právě neobnovují hodnoty; případné jiné smyčky se v něm zruší.

* Pokud v=w, lze zvolit e libovolně a položit f=S−e. Rovnice obou krajů závisejí
  jen na S, takže zachování toku zůstává v platnosti. Patří sem i dvě smyčky.
* Pokud u,v,w jsou různé, položíme e=d(v) a f=d(w). Zachování toku sloučeného
  vrcholu dává právě S=d(v)+d(w). Rovnice u závisí jen na S; obnovené rovnice
  v a w jsou splněny jednotlivě.
* Pokud e je smyčka v u=v a f vede do w≠u, je f=d(w) a e=S−f. Smyčka nemá
  vliv na bilanci u. Rovnice sloučeného vrcholu pak vynutí rovnici u.

Případ f smyčka je symetrický. Tyto možnosti jsou vyčerpávající. Obrácením
všech kroků dostaneme požadované původní toky, které mohou být záporné, jak
úloha výslovně dovoluje. Tento důkaz je surjektivitou mezi prostory reálných
toků; netvrdí zachování nezápornosti při rozštěpení.

Jen první případ ztrácí jeden stupeň volnosti: dvě hrany se změní v jednu bez
změny počtu vrcholů. V druhém/třetím případě ubyde jedna hrana i jeden vrchol.
To dokazuje tvrzení odpovědi o úspoře jednoho měření při každém prvním případu.
Minimum měření je zde algebraické minimum vyplývající ze zachování toku,
stejně jako v odstavcích, které úlohu uvádějí; další znalost programu může dát
další vztahy. Jednotkový tok e0 je známý bez měření (doplněno erratem 2021).

V příkladu jsou tři supervrcholy Start, U={A,B,D,Stop}, C a šest hran:

```
s: Start→U   t: U→Start
a: U→U      d: U→U
b: U→C      c: C→U.
```

Z rovnic plyne s=t=1 a b=c. Tři volné měřené toky jsou a,c,d. Původní diagram
má po určení e0 čtyři stupně volnosti. Opravený obrázek v erratu 2004 přesně
odpovídá těmto koncům hran.

Tvrzení, že spojování příchozích místo odchozích hran vede k témuž grafu, má
následující přímý důkaz. Předpokládáme, že v uzavřeném diagramu má každý vrchol
alespoň jednu příchozí a jednu odchozí hranu. Vytvoříme pomocný bipartitní graf
se dvěma kopiemi každého vrcholu, L(v) pro zdroj a R(v) pro cíl. Za každou
původní hranu u→v vložíme neorientovanou hranu L(u)—R(v). Označme C(x)
komponentu pomocného grafu obsahující x. V odchozí redukci se spojí právě pravé
vrcholy téže komponenty: nejprve cíle společného zdroje, pak tranzitivní
uzávěr. Hrana představující tok původním v vede

```
C(R(v)) → C(L(v)).
```

Při příchozí redukci se naopak spojí levé vrcholy téže komponenty: zdroje
společného cíle a jejich tranzitivní uzávěr. Hrana představující tok v vede
opět mezi přesně týmiž komponentami ve stejném směru. Identita na komponentách
a na hranách v je tedy požadovaný izomorfismus. Nahapetianova ani
Knuthova–Stevensonova práce není potřebná jako neověřená věta pro tento důkaz;
jejich dostupnost se přesto samostatně eviduje pro historický audit.

## 6. Úlohy 9–13

**9.** V orientovaném multigrafu se zachovávají celé identity oddílu 2. Smyčka
má nulový sloupec incidence a je samostatný fundamentální cyklus. Mezi dvěma
různými vrcholy ponecháme jednu z k+1 rovnoběžných hran e; každá zbývající e_i
dá cyklus `e_i-e` při stejných směrech, `e_i+e` při opačných. Poté provedeme
konstrukci na zbývajícím grafu. Čísla na přidaných vrcholech při dělení e13/e19
v knize jen vynucují rovnost toku obou polovin; žádný stupeň volnosti nepřidají.

**10.** Terminály předpokládají n≥1. Každé spojení všech terminálů je souvislý
graf, který obsahuje kostru s n−1 hranami. Tolik hran tedy stačí a méně
nestačí. Při právě n−1 hranách je souvislost ekvivalentní stromu podle
Theorem A. Pro n=1 není potřeba žádný drát.

**11.** Nechť již vybrané hrany spojují množinu S a jsou obsaženy v nějaké
minimální kostře T. Vyberme nejlevnější hranu e mezi S a jeho doplňkem. Je-li
e v T, invariant trvá. Jinak její přidání vytvoří jediný cyklus; ten musí
obsahovat jinou hranu f přes týž řez. Ta není dosud vybraná a má cenu nejméně
jako e. `T+e-f` je opět kostra, obsahuje všechny dříve vybrané hrany i e a
není dražší než T. Je proto rovněž minimální. Po n−1 krocích je vybraný strom
minimální. Argument dovoluje shodné i obecné reálné ceny; žádnou geometrickou
vlastnost vzdáleností nepotřebuje. Kontrakční verze úlohy je stejný algoritmus,
pokud si u každé minimální ceny uchováme původní koncové vrcholy, jak říká
závorka v zadání.

Pro obrázek 33 byly původní souřadnice čteny ze skenu. Délky osmi uvedených
hran mají čtverce `2,5,1,4,4,2,4,5`; součet délek je tedy
`7+2*sqrt(2)+2*sqrt(5)`. Na každém uvedeném kroku skript porovnal celočíselné
čtverce všech vzdáleností přes příslušný řez. Všechny volby jsou nejlevnější;
u poslední volby jsou 4–2 a 4–6 shodné. Globální optimalita plyne z obecného
výměnného důkazu výše, nikoli z pouhého numerického součtu.

**12.** První implementace v odpovědi znovu aktivuje dříve vybrané vrcholy;
protipříklad, oprava a invariant jsou v `prim-answer12.md`. Druhá varianta
explicitně udržuje seznam dosud nevybraných vrcholů, takže správně realizuje
úlohu 11. Pro hustou tabulku cen má n−1 kol, každé s nejvýše n porovnáními pro
minimum a n aktualizacemi. Její čas je O(n²) a pomocná paměť O(n). Zde nebyly
opakované dříve úspěšné testy nálezu.

**13.** Transpozice hrany prohazuje její dva konce a ostatní vrcholy nechává
na místě. V nesouvislém grafu všechny takové permutace zachovávají každou
komponentu, takže nevygenerují transpozici mezi komponentami. V souvislém
grafu vezměme cestu v0,…,vk. Její hranové transpozice t_i=(v_(i−1),v_i)
dávají transpozici krajních vrcholů jako součin

```
t_1 t_2 ... t_(k-1) t_k t_(k-1) ... t_2 t_1.
```

Je to konjugace t_k součinem prvních k−1 transpozic; oba krajní prvky se
prohodí a všechny vnitřní se vrátí na svá místa. Tedy lze vyjádřit každou
transpozici, a jelikož každou permutaci lze rozložit na transpozice, vygeneruje
graf všechny permutace. Strom dává n−1 generátorů a s n−2 hranami nemůže být
graf souvislý. Případy n=1 a prázdného součinu fungují přímo. V indukčním
zápisu knihy se při j=n−1 faktor (j,n−1) prostě vynechá jako identita; nejde
o chybné tvrzení o nutném netriviálním generátoru.

## 7. Výsledek matematického auditu

Úvod, Theorem A/K, všechny uvedené tokové identity, obrázky a úlohy 1–11 a 13
jsou matematicky uzavřeny uvedenými obecnými důkazy a přesnou kontrolou
přepisu. Nový technický nález se týká pouze prvního algoritmu odpovědi 12.
Známé chyby prvního dotisku se nepočítají jako nové. Toto není tvrzení, že jsou
přečteny všechny citované publikace; přesný stav zdrojů je oddělen.
