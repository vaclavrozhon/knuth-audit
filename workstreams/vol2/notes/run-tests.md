# §3.3.2 G: běhy, kovariance a úlohy 11–14,25

Audit 1. 11. 2026. Text str. 66–69, úlohy str. 76–78, odpovědi
str. 563–564,566. Zdroj: třetí vydání, první dotisk 1997; obrazy
`images/vol2-p066.png` až `p069.png` a příslušné odpovědi.
**Vzorce, algoritmus a číselné tabulky souhlasí.** Úloha 25 je uzavřena
jako audit formulace a uvedených experimentů, nikoli jako vyřešení jejího
obecného výzkumného požadavku.

## 1. Model a nezávislá kontrola

Vstup tvoří n nezávislých veličin U_i se stejným spojitým rozdělením.
Jejich relativní pořadí je rovnoměrná permutace. Vzestupný běh končí
před každým sestupem U_i > U_(i+1). Označme R'_p počet běhů délky
alespoň p, R_p počet běhů délky přesně p a Z_(p,i) indikátor, že
takový běh začíná na pozici i. Platí R'_p = sum_i Z_(p,i) a
R_p = R'_p − R'_(p+1).

Program `verify_run_tests.py` používá vedle tištěných vzorců nezávislý
model předepsaných porovnání. Pro souvislý vzor vzestupů a sestupů
počítá permutace podle pořadí posledního prvku: přidává-li se nový
poslední prvek s pořadím r, při vzestupu se sečtou předchozí počty
s pořadím menším než r; při sestupu se sečtou zbývající. Po vydělení
faktoriálem délky dostaneme přesnou pravděpodobnost. Oddělené bloky
porovnání závisí na disjunktních vstupech, proto se pravděpodobnosti násobí.
Protichůdné požadavky na jedinou hranu dávají nulu.

Výsledky `results/run-tests.json`:

- 781 jednotlivých indikátorů a 24 137 dvojic indikátorů, n <= 16,
  p,q <= 6, souhlasí s (14).
- 385 dvojic momentů, všechny p,q <= n pro n <= 10, souhlasí s (17)–(19).
- 46 233 permutací délek 1–8 ověřuje algoritmus R a nezávisle
  všech 204 kovariancí pro tyto délky.
- 225 dvojic p,q <= 15 ověřuje počet z (16) pomocí uvedené rekurence.

## 2. Obecné odvození (14)–(20)

Je-li i > 1, vyžaduje Z_(p,i)=1 jeden sestup a p−1 vzestupů.
Mezi (p+1)! pořadími je p vhodných; pro i=1 je pravděpodobnost 1/p!.
Za koncem vstupu je indikátor nulový. Tím dostáváme první řádek (14).

Pro i < j platí: při j < i+p jsou podmínky neslučitelné; při j > i+p
závisí na disjunktních množinách vstupů. Při j=i+p se setkají ve
společném vrcholu. Pro i>1, s=p+q, spočteme permutace s předepsanými
vzestupy uvnitř bloků délek p a q; dva mezilehlé sestupy zatím nevyžadujeme.
Počet je (s+1) binom(s,p). Odečteme binom(s+1,p+1) případů s prvním
vzestupem a s+1 případů s druhým vzestupem. Úplně vzestupnou permutaci
jsme odečetli dvakrát, proto přičteme 1. To je (16), tedy i odpověď 13.
Pro i=1 první podmínka odpadne. Po vydělení faktoriálem vyjde druhý
řádek (14). Pro shodné pozice je součin Z_(p,i)Z_(q,i)=Z_(max(p,q),i).

Součet prvního řádku dává, pro 1 <= p <= n,

```text
M_p := E R'_p = (n+1)p/(p+1)! − (p−1)/p!.
```

Následující kratší mezivýpočet kontroluje i složitou (19). Pro p+q <= n
položme L=n−p−q a D=(p+1)!(q+1)!. Součet společných pravděpodobností
přes i<j označme A(p,q). Vzdálené dvojice dávají

```text
q [p L(L+1)/2 + L] / D;
```

sousedící dvojice dávají

```text
[p(L+1)+1] / ((p+1)!q!) − [(p+q)(L+1)+1] / (p+q+1)!.
```

Proto Cov(R'_p,R'_q)=M_max(p,q)+A(p,q)+A(q,p)−M_p M_q.
Roznásobení je přesně (18)–(19). Jestliže p+q>n, žádná dvojice
rozdílných začátků nevyhoví a zůstane M_max(p,q)−M_p M_q.
Rozdílové vztahy (20) jsou bilinearita kovariance. Pro p>n se používá
R'_p=0, nikoli extrapolace (17).

## 3. Matice, centrální limitní věta a aproximace

Pro pevnou mez t seskupujeme počty do vektoru
R=(R_1,...,R_(t−1),R'_t). Kovarianční matice má pro n>=2t tvar
C=n C1+C2. Matice C1 je koeficient u n, C2 je konstantní člen.
Převod od R' je rozdílová matice s jedničkami na diagonále a minus
jedničkami nad ní. Program tímto převodem přesně ověřil všech
36+36 tištěných zlomků pro t=6.

Koeficient střední hodnoty je tištěný vektor
b=(1/6,5/24,11/120,19/720,29/5040,1/840). Přesně platí E R=nb+d,
kde d=(2/3,1/24,−7/60,−47/720,−13/630,−29/5040).
Přesná inverze C1 byla ověřena násobením. Všech 36 položek tištěné
matice A je správně zaokrouhleno na zobrazenou přesnost; některé
velké položky uvádějí dokonce šest platných číslic. Přesný rozklad
C1=L D L^T s kladnou diagonálou D dokládá pozitivní definitnost.
Také zaokrouhlená A je pozitivně definitní.

**Proč platí asymptotická normalita.** Každá složka vnitřního příspěvku
na pozici i závisí jen na U_(i−1),...,U_(i+t−1). Příspěvky vzdálené
o více než t jsou tedy nezávislé. Okraje mění součet o omezený vektor.
Pro libovolnou pevnou lineární kombinaci rozdělíme vstup na bloky délky
floor(n^(1/3)), oddělené mezerami délky t. Blokové součty jsou nezávislé;
vynechané mezery mají rozptyl O(n^(2/3)), takže po dělení sqrt(n)
zaniknou v kvadratickém průměru. Jednotlivý centrovaný blok je omezen
O(n^(1/3)), tedy o(sqrt(n)); splňuje Lindebergovu podmínku. Limitní
rozptyl je odpovídající kvadratická forma v C1. Tento argument pro
všechny lineární kombinace dává společnou normální limitu.

**Proč žádný stupeň volnosti nechybí, i pro obecné pevné t.** Lineární
kombinaci počtů pišme jako součet vah h(r)=a_min(r,t) přes běhy délky r.
Rozdělme vstup na disjunktní buňky s t+1 vnitřními prvky a dvěma krajními
prvky. Podmiňme na krajní hodnoty a neuspořádané množiny vnitřních hodnot.
S kladnou pravděpodobností je levý kraj větší než všechny vnitřní hodnoty
a pravý kraj menší. V takové buňce jsou oba kraje od vnitřních běhů
odděleny sestupy. Náhodné vnitřní permutace jsou mezi buňkami nezávislé
a nemění žádný vnější běh.

Každé složení délky t+1 na kladné části je možné jako seznam vnitřních
délek běhů. Kdyby všechny tyto seznamy měly stejnou váhu, srovnání se
samými jedničkami by dalo a_r=r a_1 pro r<=t. Jediný běh délky t+1
by současně dal a_t=(t+1)a_1, tedy a_1=...=a_t=0. Nenulová kombinace
proto má v dobré buňce kladný podmíněný rozptyl. Podmíněním navíc na
permutace špatných buněk a sečtením rozptylů dobrých buněk dostaneme
Var(sum h)>=c n pro nějaké c>0. Tím je C1 pozitivně definitní pro
každé pevné t, nikoli jen pro ověřenou matici 6×6.

Po centrování přesnou střední hodnotou a násobení inverzní kovariancí
má kvadratická forma limitní rozdělení chí-kvadrát s t stupni volnosti.
Pro t=6 je tedy správně šest, nikoli pět. Pevná změna centrování
z E R na nb v limitě zaniká.

Tištěná A je pouze aproximace C1^−1. Její pevné zaokrouhlení se
s rostoucím n nezmenšuje; doslovná limitní distribuce tištěné (10)
je vážený součet šesti nezávislých čtverců normálních veličin.
To odpovídá výslovnému upozornění knihy na přibližnost koeficientů.
Například přesná limitní střední hodnota s tištěnou A je
6.027427434044..., pro n=4000 je 6.034009262944....
Údaj „4000 nebo více“ je praktické doporučení, nikoli dokázaná mez
chyby konečné kalibrace; zde taková mez nebyla odvozena.

## 4. Úlohy 11,12,14

Úloha 11: sestupné běhy jsou |1|2|9 8 5 3|6|7 0|4|.

Úloha 12: algoritmus R začíná j=−1. V R3 zvětšuje délku r a index j,
dokud právě zpracovaný prvek má většího následníka. V R4 je tedy r
přesná délka právě ukončeného běhu. Strážná hodnota U_n=U_(n−1)
vynutí konec posledního běhu a sama se nezapočte. Index j vždy
roste, celkově je zpracováno právě n prvků. Výstup je přesně počet
délek 1,...,5 a společná kategorie délky alespoň 6; předpoklad n>=1.

Úloha 14: po ukončení běhu vynecháme prvek, který způsobil sestup.
Celý blok včetně tohoto prvku je určen zastavovací dobou posloupnosti
nezávislých vstupů. Vstupy za tímto blokem zůstávají nezávislé
s původním rozdělením. Délky po sobě jdoucích úplných běhů jsou proto
nezávislé a stejně rozdělené. Pravděpodobnost délky alespoň r je 1/r!,
neboť prvních r prvků musí být vzestupných. Dostáváme
p_r=1/r!−1/(r+1)! a pro poslední kategorii p_t=1/t!.
Nedokončený běh na předem daném konci vstupu je cenzorovaný; jednoduchá
přímá multinomická interpretace používá pevný počet úplných běhů.

## 5. Výzkumná úloha 25: doložený rozsah

Počítáme B=C1^−1 C2 C1^−1. Úloha pozoruje, že jednotlivé poměry
B_ij/(C1^−1)_ij jsou přibližně −t. Všechny následující matice a jejich
inverze byly počítány přesně racionálně; až výstupní desetinná čísla
jsou zaokrouhlena.

| t | Nejmenší poměr | Největší poměr |
|---|---:|---:|
| 5 | −5.133464391153 | −5.014113512947 |
| 6 | −6.110955395549 | −6.039282362353 |
| 7 | −7.100219305114 | −7.050441426932 |
| 8 | −8.092111029480 | −8.055003954511 |
| 10 | −10.078965944841 | −10.055958920112 |
| 12 | −12.068771166749 | −12.053134799295 |
| 16 | −16.054359915600 | −16.045808247981 |
| 20 | −20.044817692298 | −20.039439180956 |

Tištěné intervaly pro t=6 a20 tedy souhlasí. Matice nejsou přesně
proporcionální. Rozvoj inverze (n C1+C2)^−1 začíná
C1^−1/n − B/n²; dosazení B≈−6 C1^−1 vysvětluje heuristický jmenovatel
n−6, ale nedává obecnou přesnou identitu.

Částečné strukturální vysvětlení: pro v=(1,...,t) platí přesně
v^T R = n−E, kde E je celkový přebytek délek běhů nad t.
Dlouhé běhy jsou vzácné, takže tato kombinace má malý rozptyl.
Například pro t=6 je v^T C1 v=345473/1362160800, mnohem méně než
součet jednotlivých příspěvků v_i²(C1)_ii. To vysvětluje velké položky
inverze a její citlivost na téměř deterministickou kombinaci.
Samo to **nedokazuje** pozorovanou shodu všech poměrů s −t:
(v^T C2 v)/(v^T C1 v)=−6.2399219693... se navíc liší od jejich rozsahu.
Obecný asymptotický důkaz této entrywise aproximace zde netvrdíme.

Cílená rešerše 1.11.2026 nenalezla primární práci výslovně řešící
Knuthovu úlohu25; to není důkaz, že řešení neexistuje. Wolfowitzův článek
*Asymptotic Distribution of Runs Up and Down*, Annals of Mathematical
Statistics15(1944),163–172, DOI10.1214/aoms/1177731281, je ověřen
v metadatech Crossref a [obsahu původního čísla](https://www.jstor.org/stable/i312738).
Plný text nebyl získán: Euclid vrací HTML obal, nikoli PDF. Proto
netvrdíme přímou kontrolu historického důkazu. Knižní odkaz163–165 může
odkazovat na konkrétní část článku; odlišný rozsah celého článku sám
není prokázaná chyba. Metadata jsou v `sources/run-test-bibliography.json`.

## 6. Errata a reprodukovatelnost

Zkontrolovány `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální
TeX ze zdrojového archivu; datum kontroly1.11.2026. Uplatněny známé
opravy str.69 z30.4.2008 (chybějící inverze C1) a11.12.2009
(explicitní vymezení vektoru Q u závěrečné aproximace). Slovní změna
str.68 z20.4.2019 nemění výpočet. Nový nález v tomto bloku nevznikl.

```text
python3 -u workstreams/vol2/verify_run_tests.py
```

První průchod skončil0 a uložil všechny bloky. Při kontrole artefaktu
bylo opraveno jen parsování dvou desetinných koeficientů: SymPy je
nejprve převedlo přes binární float. Znovu se provedl pouze blok
`matrices`, tentokrát s přesnými desetinnými zlomky a explicitní
kontrolou zaokrouhlení; ostatní úspěšné bloky zůstaly zachovány.
Oba průchody jsou v `results/run-tests.log`.
