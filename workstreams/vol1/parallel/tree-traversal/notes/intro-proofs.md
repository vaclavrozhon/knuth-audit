# §2.3: definice a obecné důkazy

Rozsah původních obrazů: 308–318, 560(dolní odpověď 1)–564(horní dokončení 22). Níže `strom` znamená konečný zakořeněný uspořádaný strom podle induktivní definice knihy; `orientovaný strom` zde znamená, že pořadí sourozenců nebereme v úvahu. Binární strom je jiný induktivní typ: prázdný, nebo kořen a dvě rozlišené možnosti levého/pravého podstromu, z nichž každá může být prázdná. `n_k` je počet uzlů s právě k dětmi. Vlastní předek uzlu je uzel na cestě ke kořeni kromě samotného uzlu.

## Hlavní text: technická část

Induktivní definice stromu zajišťuje disjunktnost podstromů a jedinečnost rodiče i cesty, viz úloha 3 níže. Les je konečná posloupnost disjunktních stromů; pořadí je součást dat. Kresby 15/19, vnořené oblasti 20, strom aritmetického výrazu 21 a Deweyho adresy 22 jsou s tímto rozlišením konzistentní. Dva binární stromy s jedním levým, respektive pravým dítětem mají odlišnou strukturu, i když po zapomenutí této role dávají tentýž obecný strom. Binární genealogie je strom rolí, nikoli nutně různých osob: opakovaný člověk na více pozicích proto není cyklus (známé upřesnění 311 z roku 2000).

Deweyho adresa začíná číslem stromu v lese; každé další číslo určuje pořadí dítěte. Odebrání poslední složky dává rodiče; zápis F[a, b,..., d] naproti tomu vrací podles dětí daného uzlu, takže jeho rodičem je uzel s odpovídající adresou. Tato rozdílnost vysvětluje odpověď 17. V Lists jsou prvky atomy nebo odkazy na další seznamy. Sdílení a cyklyM=(M), N=(a: M, b: M, c, N) jsou konečné grafové popisy; induktivně definované konečné stromy tyto cykly nepřipouštějí. Obrázky(4),(7) správně rozlišují definici podseznamu hvězdičkou od dalšího odkazu na již definovaný podseznam.

Historická tvrzení a osobní genealogie Fig. 18(a) mají meze v pramenných poznámkách. Fig. 18(b) byla samostatně porovnána s Genesis 10: 1–25; po známém erratu souhlasí. Známé textové opravy jsou v inventáři a JSON, nejsou novými nálezy.

## Úlohy 1–10

1. Pro daný kořen existují dvě pořadí zbývajících dětí u rozvětveného stromu a dvě pořadí zbývajících uzlů v řetězci. Jsou tři volby kořene: 3(2+2)=12. Případy jsou disjunktní a vyčerpávají dvě možné rozdělení velikosti 2 mezi podstromy.
2. Bez pořadí sourozenců se první dvě možnosti sloučí; 3(1+2)=9.
3. Indukce podle počtu uzlů. Kořen má jednoprvkovou cestu. Jiný uzel leží právě v jednom kořenovém podstromu díky disjunktnosti definice; indukční cesta v něm, doplněná kořenem, je cesta v celém stromě. Žádná jiná cesta nemůže opustit tento podstrom před jeho kořenem, protože všechny rodičovské hrany uvnitř vedou do téhož podstromu. Tím je současně existence i jedinečnost cesty a rodiče.
4. Pravda při konvenci, že úroveň 0 je kořen a úroveň roste po hranách dolů. Formulace je konvence kreslení, nikoli omezení libovolného geometrického vložení.
5. Tři sourozenci plus A jsou přesně čtyři děti B, tedy stupeň 4.
6. Označme p^k(X) k-tého předka, pokud existuje. Podmínka p^(m+1)(X)=p^(m+n+1)(Y) a p^m(X)≠p^(m+n)(Y) říká, že uvedený společný předek je nejbližší: obě cesty vstupují do jeho různých dětí. Pro m, n≥0 dává obvyklé stupně příbuzenství, s výslovně asymetrickým významem kladného n. Předci v rovnosti musí existovat; nedefinované hodnoty nad kořenem se nepovažují za společného předka.
7. Nechť Z je nejbližší společný předek a q, r jsou vzdálenosti Z→X, Z→Y. Pak m=q−1 a n=r−q. Dostaneme m≥−1, n≥−(m+1), jak požaduje zadání. Rovnost vzdálenějších předků by současně způsobila rovnost bezprostředně nižších předků, a tedy nesplnila druhou podmínku. Konvence, že výrazy s exponentem−1 nejsou nikdy rovné, pokrývá X=Z, Y=Z i X=Y. Tím je existence a jednoznačnost pro všechny dvojice. Nepoužíváme neexistujícího rodiče kořene.
8. Jde o odlišné induktivní typy; zobrazení neprázdného binárního stromu na obecný strom zapomíná levý/pravý prázdný slot a není prosté. Tištěná odpověď není jen upozornění na prázdný strom.
9. Kořen je A podle polohy nahoře; označení písmeny neurčuje pořadí rodičovství.
10. Konečná vnořená kolekce neprázdných množin dává les: maximální množiny jsou disjunktní; pod každou jsou její maximální vlastní podmnožiny disjunktní děti a indukce se opakuje. Jediný maximální prvek dává strom; více maximálních prvků dává více komponent. Prázdná kolekce dává prázdný les. Nekonečná kolekce nemusí mít maximální prvek, například řetězec{1,..., n}, n≥1, takže sama bez další definice nedává konečný strom z textu. Pořadí sourozenců nelze odvodit ze samotné inkluze, proto výsledek je neuspořádaný.

## Úloha 11: přesný rozsah

RelaceX~Y právě tehdy, když nějakéZ z kolekce obsahujeX∪Y, je ekvivalence. Reflexivita a symetrie jsou přímé. Pro tranzitivitu použijeme dvě obalující množinyZ1, Z2; mají neprázdný průnik obsahující prostřední neprázdnou množinu, a proto je jedna obsažena v druhé, která obalí oba krajní uzly. Rozklad potomků uzlu na tyto komponenty definuje stupeň i bez bezprostředních dětí.

Příklad(a): u desetinného rozvoje volíme standardní jednoznačnou reprezentaci, která nekončí samými devítkami. S[a, k] fixuje všechny číslice na pozicích nedělitelných 2^k. Pro k=0 je to společný kořen; přechod z k na k+1 fixuje nekonečnou novou množinu pozic, takže počet neprázdných odlišných větví je kontinuum. Větve jsou disjunktní a každá menší množina má právě jednu nadmnožinu pro každou nižší celočíselnou úroveň. Úrovně jsou tedy 0, 1, 2,... a všechny stupně jsou nespočetné. Volba nejednoznačných desetinných zápisů bez konvence by byla nevhodná, nikoli nutná pro konstrukci.

Příklad(b),(c) a rozlišení kardinální úrovně od množství různých úrovní jsou samostatně v `infinite-level-candidate.md`; doslovný požadavek(c) má kandidátní rozpor. Navazující poznámka o dobrém uspořádání má samostatný rozbor v témže dokumentu; doslovná konstrukce nemůže splnit zároveň obě uvedené vlastnosti. Proto se celá úloha nevykazuje checked.

## Úlohy 12–22

12. Pro konečný poset je nutná a postačující podmínka, že horní množina každého prvku je lineárně uspořádaná. Každý ne-maximální prvek má pak jednoznačný nejmenší přísně větší prvek, svého rodiče. Opakováním skončíme v jediném maximálním prvku příslušné komponenty; striktní růst zabraňuje cyklům. Jediný největší prvek znamená jediný strom. Obráceně se všichni předkové uzlu ve stromě nacházejí na jedné cestě. Nekonečnou verzi nelze ztotožnit s konečnou induktivní definicí; právě to odpověď výslovně kvalifikuje.
13. Cesta odX ke kořeni vzniká postupným škrtáním poslední složky: a1...ak, a1...a(k−1),..., a1. Tištěný opačný směr má známou opravu 2007.
14. Z podmínky předchozího sourozence po konečně mnoha krocích získáme první dítě, poté jeho rodiče. Tak se z každého prvku dostaneme až k 1; podmínka proto zajišťuje prefixovou uzavřenost. Děti každého prefixu tvoří počáteční interval 1,..., d. Konečnost zajišťuje konečnýd a konečnou hloubku; každá adresa kromě 1 má jednoznačný rodičovský prefix. Dostáváme strom, jehož Deweyho adresy jsou přesně S. To je přímý důkaz bez závislosti na zkrácené indukci tištěné odpovědi.
15. Adresa kořene 1, levého dítětew 0, pravéhow 1. Jednoznačné dekódování dává obecné řešení; čísla jsou pozitivní binární celá čísla. Technický přepis Fig. 18 dává Christian IX na10000 a110010. Galtonova původní strana 249 byla přečtena a atribuce notace ověřena; genealogická správnost Fig. 18(a) zůstává odděleným pramenným úkolem.
16. (a) kořen násobení, vlevo atom 2, vpravo odčítání a a podílu b/c. (b) kořen sčítání a, b, 5*c; při binárním sčítání lze asociovat (a+b)+5*c nebo a+(b+5*c), jak správně ukazují alternativy odpovědi. Operátory a pořadí operandů jsou zachovány.
17. Pro lesZ obsahující Fig.19 je parent(Z[1, 2, 2])=E. OznačeníF je známě opraveno naZ. Operace vybere děti E, nikoli uzel E samotný; proto se nepoužije prosté odebrání posledního indexu.
18. L[5, 1, 1]=(2), jednoprvkový List, nikoli atom 2. L[3]=(), tedy L[3, 1] není definován.
19. L=(a,(L)) má druhý prvek (L); rozvinutím tří indexů dostaneme L[2, 1, 1]=a. Konečný graf má jeden cyklus délky 2 přes vnitřní jednoprvkový seznam a sdílený zpětný odkaz na L.
20. Přidáme ke každému prázdnému levému/pravému slotu binárního stromu list a zachováme všechny původní uzly jako vnitřní. Výsledek má 0 nebo 2 děti v každém uzlu. Inverze smaže všechny listy. Indukce dává početN=1 pro prázdný strom a N=1+(2nL+1)+(2nR+1)=2(1+nL+nR)+1 pro neprázdný. Obě transformace jsou inverzní včetně n=0; parita je lichá.
21. Počet hran jeN−1 zároveňΣ k*n_k; odečtenímΣ n_k=N plyne n_0=1+Σ_{k≥1}(k−1)n_k. Nevyžaduje binaritu ani předpoklad, že každý stupeň do maxima je zastoupen.
22. Obdélník s poměrem stran sqrt(2) se po půlení delší strany a otočení stává podobným původnímu s lineárním měřítkem 1/sqrt(2) a poloviční plochou. Rekurzivně přidělujeme levému/pravému podstromu dvě disjunktní poloviny; kořen a spojnice tvoří středovou hranici popsanou v odpovědi. Každý konečný strom končí po konečně mnoha půleních, takže vznikne jednoznačná konečná kresba na jediném listu. Přidaný erratový údaj A_n má plochu 2^(−n) m^2 a přesný poměr vysvětluje tuto podobnost. Rozložení prázdných slotů na obdélníčky je obdobná indukce. Globální optimalitaVLSI je zvláštní pramenné/tvrzovací omezení, nikoli důsledek pouhé existence kresby.
