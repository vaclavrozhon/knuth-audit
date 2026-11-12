# §2.2.1, cvičení 7–11: omezené oboustranné fronty

Kontrola V1-X0013, 1. listopadu 2026. Zadání je na tištěné s. 243,
odpovědi na s. 538–539; obrázky mají čísla souboru 258, 553 a 554.
Použit první dotisk třetího vydání. **V tomto bloku nebyla nalezena nová
chyba.** Níže jsou obecné důkazy a odděleně konečné výpočty.

## 1. Operace a malé protipříklady (cvičení 7–8)

Vstup tvoří čísla 1,...,n v tomto pořadí. Oboustranná fronta, dále deque,
uchovává posloupnost mezi levým a pravým koncem. Vstupně omezená deque
dovoluje vkládat jen zprava a odebírat z obou konců; výstupně omezená
dovoluje vkládat z obou konců a odebírat jen zleva. Výstupní permutace
je pořadí všech odebraných čísel.

Pro n=4 jsou množinové rozdíly přesně:

- vstupně omezená, ale nikoli výstupně omezená: 4132;
- výstupně omezená, ale nikoli vstupně omezená: 4213;
- nedosažitelná ani jedním omezeným typem: 4231.

První dva výstupy lze vytvořit: pro 4132 vložit 1,2,3,4 zprava a odebírat
pravý, levý, pravý, levý konec. Pro 4213 vkládat 1,2,3,4 postupně na
levý, levý, pravý, levý konec a pak číst zleva. Jestliže vstupně omezený
výstup začíná 4, zůstane po prvním odběru fronta 123, ze které nelze
odebrat 2. Jestliže výstupně omezený výstup začíná 4, všechny vstupy už
musely být vloženy. Výsledná fronta musí klesat směrem k 1 a poté růst:
prvky vložené vlevo stojí v opačném pořadí vstupu, prvky vpravo ve vstupním
pořadí. To vylučuje 4132 i 4231. Úplnost těchto rozdílů ověřuje konečný
výčet všech 24 permutací.

Neomezená deque dovoluje všechny čtyři operace. Pro n<=4 vytvoří všechny
permutace. Pro n=5 chybí právě 51324, 51342, 52314, 52341, v souladu
s odpovědí 8. Nezávislý operační výčet tuto konečnou větu ověřuje úplně.
Nejde o důkaz nekonečné charakterizace ve cvičení 13.

## 2. Bijekce mezi oběma omezenými typy (cvičení 9)

Permutaci chápeme také jako zobrazení pozic na hodnoty; p^(-1)(v) je
pozice hodnoty v. Označme R(i)=n+1-i. Zobrazení p -> R p^(-1) R je
involuce, tedy při dvojím použití vrací p, a převádí dosažitelné výstupy
jednoho omezeného typu na druhý.

Obrátíme čas v celé historii. Původní odběry se stanou vklady a původní
vklady odběry. Nový vstup má pořadí p(n),...,p(1); přeznačíme jej na
1,...,n. Nový výstup, původně n,...,1, pak má na pozici j hodnotu
n+1-p^(-1)(n+1-j), právě R p^(-1) R. Omezení na jeden vstupní konec
se změní v omezení na jeden výstupní konec. Proto mají oba typy stejný
počet výstupů pro každé n, nejen pro ověřené malé velikosti.

## 3. Kanonické historie (cvičení 10)

Pro výstupně omezenou deque označuje S vložení dalšího čísla zleva,
Q vložení zprava a X odebrání zleva. Výška prefixu je počet dosavadních
vkladů minus počet odběrů. Kanonické slovo má n vkladů a n odběrů,
nezáporné výšky, při výšce 0 vkládá pouze Q a neobsahuje sousední XQ.

**Existence.** V každé legální historii lze změnit S na Q při prázdné
frontě. Sousední XQ lze zaměnit za QX: původní X odebírá z neprázdné
fronty a vložení zprava jeho výsledek nezmění. Výstup se při obou úpravách
zachová. Úpravy skončí: změna S na Q snižuje počet S; při pevném počtu S
každá záměna XQ snižuje počet dvojic, v nichž X předchází Q. Tato dvojice
nezáporných čísel lexikograficky klesá. Výsledkem je kanonické slovo.

**Jednoznačnost.** Uvažujme první rozdíl dvou kanonických slov se stejným
výstupem. Mají stejnou současnou frontu D a stejný další vstup u.
Rozdíl S/X nebo S/Q je možný jen při neprázdné D. Její první prvek t
vyjde po u při S a před u při X i Q; již přítomné prvky totiž nelze
navzájem předběhnout. Zbývá Q/X. Ve druhém slově po první X následuje
maximální blok r odběrů a potom vklad u. Musí to být S, protože XQ je
zakázáno. Fronta po těchto odběrech musí zůstat neprázdná, protože S při
výšce 0 je zakázáno. V druhém slově proto u předběhne další dosud
přítomný prvek D; v prvním slově Q zařadilo u až za celou D. Opět různé
výstupy. Jiný první rozdíl neexistuje.

## 4. Jednoznačná gramatika a vytvářející funkce (cvičení 11)

Gramatika zde znamená pravidla pro skládání slov z menších slov.
Symboly A a B jsou pomocné třídy slov, nikoli operace; A nahrazuje
neterminál, který kniha označuje stejně jako terminál S. Pravidla jsou

```text
A -> Q^k (B X)^k                    (k >= 0)
B -> empty | S Q^k (B X)^(k+1) B    (k >= 0).
```

Každé úplné neprázdné kanonické slovo začíná maximálním blokem Q^k.
Rozdělíme zbytek při prvním sestupu z výšky k na k-1, poté na k-2,
až na 0. Před každým z těchto X je vyvážený úsek B, který neopustí
svou výchozí výšku. Neprázdný B začíná S: Q vylučuje maximalita úvodního
bloku nebo předchozí X. Po tomto S vezmeme maximální blok Q^k, rozklad
při prvních sestupech a zbývající vyvážený úsek B. Dostáváme druhé
pravidlo. Rozklady jsou jednoznačné a obráceně skládají legální kanonická
slova. Všechny úseky B se v úplném slově zpracovávají nad výškou 0,
takže jejich úvodní S neporušuje pravidlo pro prázdnou frontu.

Nechť F(z)=sum b_n z^n počítá úplná slova A podle počtu odběrů a B(z)
stejným způsobem počítá pomocná slova. Prázdné slovo má váhu 1.
Jednoznačnost gramatiky opravňuje násobení řad a dává

```text
F = 1/(1-zB),       B = 1 + z B^2/(1-zB),
F^2 + (z-3)F + 2 = 0,
F = (3-z-sqrt(1-6z+z^2))/2.
```

Poslední větev určuje F(0)=1. První koeficienty jsou
1,1,2,6,22,90,394,1806,8558. Přímé porovnání koeficientů kvadratické
rovnice dává b_n=b_(n-1)+sum_(k=1)^(n-1) b_k b_(n-k) pro n>=1.
Derivací odmocniny a porovnáním koeficientů dostaneme též knižní
rekurenci n b_n=3(2n-3)b_(n-1)-(n-3)b_(n-2) pro n>=2.

Ověřeno i původní odvození pomocí prefixů. G(x,z) počítá neprázdné
legální prefixy nekončící X a H(x,z) prefixy končící X; mocniny x a z
udávají výšku a délku. Označme h(z)=H(0,z). Jednokrokové přechody dávají

```text
G/z = 2xG + x(H-h) + x,
H/z = (G+H-h)/x,
G = xz(x-z-xh)/(x-z-2x^2 z+xz^2).
```

Člen x v první rovnici je první Q. Odečtení h odstraňuje nelegální
přechody po X při prázdné frontě. Malý kořen jmenovatele, tedy kořen
r(z) s nulovým konstantním členem, je

```text
r(z) = (1+z^2-sqrt((1+z^2)^2-8z^2))/(4z).
```

Formální dosazení x=r(z) je přípustné, protože r má kladný řád v z.
Z čitatele plyne h=1-z/r=2zr-z^2. Dosazení a krácení dává
G=xz/(1-2xr), jak stojí v knize, a F(z^2)=1+h(z). Obě odvození
tedy poskytují stejnou vytvářející funkci.

## 5. Reprodukovatelné konečné kontroly a errata

`check_deques.py` a `results/deques.json` obsahují tyto oddělené kontroly:

- Přímý model všech legálních operací obou omezených typů pro 0<=n<=8;
  nepoužívá kanonická pravidla ani vzorec pro počty.
- Kanonická slova, jejich různé výstupy a úplnou shodu s operačním
  modelem pro 0<=n<=8; involuci z oddílu 2 na všech těchto výstupech.
- Doslovné generování gramatiky pro 0<=n<=7 včetně počtu odvození
  každého slova; vždy právě jedno, s přesnou shodou s kanonickými slovy.
- Kvadratickou a lineární rekurenci a nezávislé počítání přechodů
  prefixů podle výšky a posledního znaku až do n=100.
- Neomezenou deque pro 0<=n<=7; počty 1,1,2,6,24,116,634,3762.

Běh skončil úspěšně. Výčty doplňují obecné důkazy, nenahrazují je.
Skeny zadání i odpovědí byly zobrazeny a porovnány s přepisem.
Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1` a aktuální textová
errata podle stránek i témat deque/admissible/Pratt; dne 1. listopadu 2026
nenalezena oprava cvičení 7–11. Opravy cvičení 5 a 12 jsou mimo tento
blok a vedou se zvlášť. Charakterizace ve cvičení 13 ani historické
bibliografické výroky tímto záznamem nejsou uzavřeny.
