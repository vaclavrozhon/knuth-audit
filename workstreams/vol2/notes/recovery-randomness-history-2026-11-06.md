# Obnova §3.5 G177–179 — V2-X0159

6. listopadu2026. Originály177,178,179 nově zobrazeny vcelku;
úlohy1–4 na spodku179 jsou již samostatně uzavřeny v mapě a zde
se znovu nezapočítávají. Celý `randomness-history.md`, příslušné
`selection-extensions.md`, C0070 a archivní Shenův výňatek znovu
přečteny. Church1940 čten celý z původní textové vrstvy130–135;
Kolmogorov1963 přesně369–374 pro definice, algoritmy a existenční
vztah. Následující bibliografické limity zůstávají výslovné.

## R1, normálnost a souvislost s Bernoulliho posloupnostmi

Úvodní souhrn o vlastnostech R1 se opírá o již uzavřené jednotlivé
důkazy maxim, mezer, běhů, dvoutypového sběru a dalších konkrétních
úloh. Neznamená platnost každého představitelného statistického testu;
například více typů kupónů má přesný omezený rozsah v úloze16.
Hodnocení vhodnosti definice pro teorii je redakční úsudek, nikoli
další všeobecná věta.

Matematický výrok o téměř všech b-árních rozvojích má přímý důkaz.
Pod Lebesgueovou mírou jsou jednotlivé číslice nezávislé a uniformní:
každý délkyℓ pevný prefix určuje interval délky b^(−ℓ). Nejednoznačné
konečné rozvoje tvoří spočetnou nulovou množinu. Fixujme m,k a vzor
délky k. Indikátory jeho výskytu na pozicích mn+r mají průměr b^(−k).
Každý indikátor překrývá jen O(k) jiných, takže rozptyl součtu N
indikátorů je O(kN). Čebyšev pro N=j² má součet chyb O(Σ1/j²)<∞.
Pravděpodobnost odchylky po libovolně velkém j je tedy0; mezi j²
a(j+1)² se relativní četnost změní nejvýše O(1/j). Dostáváme správnou
limitu pro všechny N. Spočetný průnik přes m,k,vzory,r a případně
b dokazuje požadované téměř jisté tvrzení. Nejde o ověření priority
nebo přesného původního znění Borelova článku.

Známá oprava177 z11. ledna2000 mění historické pojmenování na
„entirely normal“ a doplňuje Borelův informální výrok odpovídající
větě C. Původní Borel1909 ani zadané stránky knihy1914 nebyly získány
a čteny; tento historický obsah je **skip**. Potřebná matematická větaC
má samostatný uzavřený důkaz a dřívější primární Niven–Zuckerman1951.

Při **0<p<1** se ∞-distribuovaná reálná U prahuje na
X_n=[U_n<p]. Pro k-bitový vzor s r jedničkami je příslušný box
součinem r intervalů[0,p) a k−r intervalů[p,1), objemu
p^r(1−p)^(k−r). R1 dává přesnou Bernoulliho frekvenci. Pevné
zarovnané vzory a rozestupy vyplývají z věty C a z doplnění
nepředepsaných souřadnic.

Obráceně nechť pevná binární X má tyto frekvence všech konečných
vzorů. Nahradíme každou1 nezávislou uniformní hodnotou z[0,p) a
každou0 nezávislou uniformní hodnotou z[p,1). Pro pevný racionální
k-box je střední hodnota indikátoru jeho okna součinem podmíněných
délek; zprůměrování podle2^k vzorů X konverguje k objemu boxu,
protože faktory p a1−p se vykrátí. Disjunktní okna jsou nezávislá,
tedy rozptyl součtu je O(kN). Tentýž čtvercový podposloupnostní
argument a spočetný průnik přes racionální boxy a k dávají skoro
jistě reálnou R1, která se **přesně** prahuje na původní X.
Obecné konce intervalů dostaneme sevřením racionálními boxy.

Church132 uvádí Copelandovu definici pomocí součinů na pevně
rozložených pozicích. Úplné vzory z těchto momentů p^r získáme
rozvinutím součinů X_i a(1−X_i). Z klouzavých frekvencí výše plyne
zarovnaná verze přes reálné zvednutí a větu C. V opačném směru
zvolíme blok délky m≥k: všechna okna neležící přes jeho hranici
mají požadovanou frekvenci, zbývajících nejvýše k−1 z m reziduí
tvoří chybu≤(k−1)/m. Po limitě v N necháme m→∞. Tím jsou oba
výklady Bernoulliho posloupnosti skutečně ekvivalentní.

**Kraje p=0,1 se nepřebírají jako přesné zvednutí libovolné posloupnosti.**
Například posloupnost s jedinou1 má všechny degenerované Bernoulliho
frekvence p=0, ale žádná reálná U nemůže splnit[U_n<0]=1 na této
pozici. Konstantní posloupnosti se zvednout dají; to však není obecný
důkaz na krajích. Churchova poznámka11 na132 výslovně potvrzuje,
že Copeland vylučuje p=0 a1. Proto je knižní historická ekvivalence
správná v tomto původním nevyjádřeném kontextu. Starší naše věta
o krajích byla zpřesněna, nevytváří se tím nový nález knihy.

## Silnější výběry a nemožnost všech měřitelných množin

Úvodní souhrn177, že R1 nevyjadřuje všechny dodatečné podmínky,
má konkrétní důkazy z dřívějších bloků. R6 zahrnuje R5 použitím
čtení v původním pořadí a R4 použitím pevného vypočitatelného
injektivního pořadí. Coppersmithova konstrukce z úlohy37 má úplný
převzatý důkaz v `selection-extensions.md` §3: každý dostatečně velký
paritní blok má správný součinový zákon na každé vlastní podmnožině;
rozptylový argument současně pokrývá všechny vypočitatelné injekce.
Předvídatelný výběr posledního bitu bloku podle jeho minulosti ovšem
selže pro R5, a tedy i R6. To dokazuje R4 bez R6 a také R1 bez R6.
Historické prvenství Herzog–Owings1976 a obsah jejich konkrétní
„large family“ nejsou tímto samostatným důkazem ověřeny.

R6 může mít přísnou převahu jedné poloviny intervalu v každém
prefixu, jak dokazuje celý C0070 pro přesné reálné R6 a všechny základy.
Proto tvrzení o shodě R6 s intuitivním pojmem náhody zůstává
filozofickým hodnocením; není z něj nová matematická karta.
Oprava výzkumné poznámky597 je již evidována v C0070.

Požadavek správné frekvence pro **všechny** Lebesgueovsky měřitelné A
je nemožný: pro danou posloupnost vezměme A={U₀,U₁,…}. Je spočetná,
má míru0 a empirickou frekvenci1. Tento argument platí bez dalších
předpokladů o U. Nesmí se zaměnit „pro všechna A současně“ za
„pro každé pevné A skoro jistě“. Připsání této chyby konkrétnímu
Waldovu originálu1937 nebylo ověřeno přímo v něm a zůstává skip.

## Church, Kolmogorov a přesné mezery Lovelandova tvrzení

Church131–132 sám rozlišuje neurčitý původní úmysl von Misese od
příliš široké formalizace všemi funkcemi. Pro0<p<1 je druhá
formalizace nemožná: pro konkrétní posloupnost existuje funkce
zakódující právě indexy jejích jedniček a vybírající jen je, ačkoli
není nutně efektivní. To nevyžaduje číst aktuální bit při běhu;
zakázaná informace je zabudovaná v libovolné funkci. Právě tuto
obtíž odstraňuje efektivní omezení. Historický původní článek1919
zůstává nepřečtený a Churchův přesnější popis se nevydává za jeho
doslovnou formulaci. Pro p=0 nebo1 původní „neexistence“ takto neplatí;
reálný R3 a nevyjádřený netriviální binární případ jsou odlišeny.

Church133–134 zavádí efektivně vypočitatelné výběrové funkce a
na134 cituje přesně Wald1937,38–72. Jeho existence vychází ze
spočetnosti efektivních pravidel; potřebný vlastní pravděpodobnostní
důkaz výběrů již máme v `selection-randomness.md`. Na135 ukazuje
nemožnost efektivně vypočitatelné netriviální náhodné posloupnosti:
pak lze efektivně vybrat všechny jedničky nebo nuly. Tyto konkrétní
obsahy a přímá citace jsou z primárního článku uzavřené, nikoli
historická prvenství všech jmen z jeho přehledu.

Kolmogorov371 definuje volbu dalšího dosud nečteného indexu funkcí
minulé historie a rozhodnutí o zařazení bez aktuální hodnoty.
Zastavení je samostatné. Na373 přechází k nekonečnému efektivnímu
čtení; na374 existence konečných tabulek plyne ze sjednocení
špatných událostí přes konečnou rodinu algoritmů. Tím je doložena
souvislost R6 a Q2 s tímto primárním článkem. Přesná konstanta
v knize má vlastní uzavřený důkaz37 v `finite-randomness.md`;
výzkumná38 a obecné optimum se tím neuzavírají.

Obě práce formulují zde použité definice pro binární hodnoty.
Churchův úvod přitom výslovně zmiňuje i obecné prostory výsledků;
slovo „only“ v knižním shrnutí chápeme v rozsahu skutečně uvedené
specializované definice, nikoli jako tvrzení, že jeho článek nemluví
o jiných prostorech vůbec. Reálná rovnoměrná posloupnost současně
dává správnou četnost[U_n<p] pro každé p sevřením racionálních
hranic. Tento frekvenční význam „all p at once“ neobsahuje automatický
algoritmus pro rozhodování každého nevypočitatelného prahu.

Lovelandův původní článek1966,12,279–294 má ověřená metadata,
nikoli přečtený celý důkaz. Zde jsou samostatně **partial**:

1. přesná existence reálné R5 posloupnosti nesplňující R4 v uváděném
   provedení;
2. konkrétní vypočitatelná permutace f a algoritmus W′;
3. mez limsup četnosti[U_f(n)≥1/2]−liminf≥1/2 pro všechny uvedené
   výstupy W′ a rodiny pravidel.

Shen–Uspensky–Vereshchagin2017, věta203(d), ve skutečně uloženém
výňatku308 tvrdí, že Churchova náhodnost není stabilní při vypočitatelné
permutaci. Její vlastní důkaz(d) v tomto výňatku **není**. Navíc
ztráta R5 po permutaci sama neznamená ztrátu základní frekvence
a tím nevyvrací R4 původní posloupnosti. Tento slabší výrok tedy
neuzavírá ani přesnou mez1/2, ani sám o sobě první bod. Staré obecné
checked na X0024 bylo otevřeno jako partial, aby mezeru neskrývalo.

## Ostatní bibliografické výroky a179

Následující body mají vlastní záznamy v mapě. Nedostupné původní
texty se výslovně vynechávají; neuplatňuje se domněnka, že shodná
metadata dokazují obsah nebo prioritu:

- Korobov1948,21–22 a rozvoj v50.letech: původní práce nečteny;
  „completely equidistributed“ je zde přímo význam R1 pro reálné U.
- Franklin1963,28–59: předchozí přístup k primárnímu PDF selhal;
  motivace a nezávislost historického objevu neověřeny. Vlastní
  matematické konstrukce mají oddělené důkazy, nikoli tuto prioritu.
- Kuipers–Niederreiter1974: celý obsah a hodnotící úplnost knihy
  neauditovány; bibliografický skip.
- Besicovitch1934,146–156 a údajná poloha „mezi“ Q1/Q2: přesná
  definice ani implikace v původním článku neověřeny, matematicky partial.
- Howard1975,215–224: konkrétní zpřesnění neověřeno; skip.
- Kolmogorov1965, Chaitin1968 a jednotlivé Solomonoff1964/1978/1997
  práce: původní historické vztahy neověřeny. Samostatně přečtený
  Martin-Löf1966 a důkazy složitostních výroků z E nejsou jejich náhradou.
- Popper1959,162–163 a prvenství1934: původní stránky nečteny; skip.
- LovelandTAMS1966,497–510, Schnorr1969,27–35 a Brouwer1919:
  přesné souvislosti s rekurzí a nulovými druhy neověřeny; skip.
- Schnorr1971 a Li–Vitányi1993: celé monografie ani jejich
  hodnotící charakteristiky neauditovány; skip.
- Blum–Micali/Yao1982/1984, prvenství a původP4: původní celé
  práce zde nečteny. Obsah P4 má úplný vlastní důkaz, jeho historický
  původ a prvenství prvních konstrukcí jsou samostatný skip.
- Levin1987: původní práce nečtena; skip.

Definice tvrdého bitu na179 je podmíněná průměrná obtížnost
f(g^(−1)(y)) pro daný zákon y, při snadném f a g. Nejde pouze o
nějaký těžký izolovaný vstup. V našem permutačním případě dáváP4
přesně redukci od rozlišení výstupů k předpovídání takového bitu.
Obecné Goldreich–Levin1989 maskování je v primárním autorově textu
přečteno jen v rozsahu1–4, takže úplný obecný důkaz není převzat.
Zde potřebnou speciální lineární redukci plně dokazuje L/G.

Levinův autorský přetisk1993 z2012 byl nově přečten celý. Obsahuje
párovou nezávislost a transformační metodu a v poděkování jmenuje
Rackoffa a Venkatesana. Známé erratum179 z8. srpna2005 přisuzuje
algoritmusL Charlesi Rackoffovi. Zůstává známou opravou, nikoli
novým nálezem ani samostatně dokázanou prioritou. Původní časopisecká
sazba1993 není tímto porovnána.

Výrok o generátorech z **libovolné** jednosměrné funkce vyžaduje
obecný výsledek HILL. Jeho celý důkaz není doložen v tomto auditu
a stav je **partial**; samotná redukce pro jednosměrnou permutaci
nebo modulární druhou mocninu nemá stejný rozsah. Známé změny179
z2000 na SICOMP28(1999),1364–1396 a z2004 na „beyond the scope“
jsou zapracované mimo nálezy. L’Ecuyer–Proulx1989,467–476,
konkrétní empirické výsledky a připsané prvenství zůstávají skip.
Marsagliova citace1984 není nově porovnána s primárním zdrojem;
nejde o matematický výrok a původ není tímto potvrzen.

Tím je celý text159–183 a všech44úloh §3.5 **posouzen po tvrzeních**,
nikoli plošně prohlášen za dokázaný. Výzkumné17/27/38 a všechny
výše jmenované matematické, modelové a zdrojové mezery zůstávají
partial. Obnova pokračuje3.6 na184/file196; dopředný418 je držen.
