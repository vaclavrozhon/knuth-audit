# §1.2.2: algoritmy logaritmu a exponenciály

Kontrola 1. listopadu 2026, V1-X0030 a V1-C0002. Původní zadání je
na s. 24–27, odpovědi na s. 470–471. Všechny tyto strany i opravy
2001,2002,2011,2024 byly zobrazeny. V této poznámce x_0 či X označuje
původní vstup; pracovní x se během algoritmu mění. Základ logaritmu
splňuje b>0,b!=1, pokud není výslovně uvedena silnější podmínka.

## 1. Bity logaritmu opakovaným umocňováním

Nejprve zvolíme celé n tak, aby 1<=X/10^n<10, a položíme x_0=X/10^n.
Číslice b_k je 0 nebo 1 podle toho, zda x_(k−1)^2<10; při překročení
prahu se čtverec vydělí deseti. Invariant je

```text
1 <= x_k = X^(2^k) / 10^[2^k(n + sum_(j=1)^k b_j/2^j)] < 10.
```

Odmocnění/logaritmování tedy dává
0<=log_10 X−(n+sum b_j/2^j)<2^(−k). To dokazuje správnost všech
bitů i konvergenci. Při rovnosti s prahem musí být b_k=1; poté
x_k=1 a následují nuly, tedy kanonický binární zápis. V původním
(19) je člen n přítomen, ačkoli pomocný Markdown jej vypouští.
Náhrada desítky dvojkou dokazuje odpověď úlohy 24.

Čtyřmístný příklad jsme provedli doslovně, s přesnými celými čísly
pro tisíciny a zaokrouhlením na nejbližší hodnotu po normalizaci.
Všechny hodnoty x_0,...,x_10 souhlasí s knihou. První chybná cifra
je b_19. Přesný konečný automat zaokrouhlených stavů má od indexu
185 periodu délky 47. Opakující se bity proto definují přesné
racionální číslo, přibližně
0,3010314518384567767915839465423414803, v souladu s prefixem v textu.
Prvních 48 správných bitů bylo nezávisle určeno racionálními
intervaly pro ln2/ln10, nikoli stejnou rekurencí.

## 2. Obecná chyba umocňovací metody, úloha 27

Nechť e_0=log_10(10^n x'_0/X) a e_j=log_10(y_j/(x'_(j−1))^2).
Předpoklady úlohy znamenají log_10(1−delta)<=e_j<=log_10(1+epsilon)
pro j>=0; vyžadujeme 0<=delta<1, epsilon>=0. Po j-tém kroku je
0<=log_10 x'_j<1. Označíme-li S_k=n+sum_(j=1)^k b_j/2^j,
opakované dosazení dává přesnou rovnost

```text
S_k = log_10 X + e_0 + sum_(j=1)^k e_j/2^j − log_10(x'_k)/2^k.
```

Součet vah chyb je 2−2^(−k)<2. Dosazením mezí vyjde přesně
nerovnost v zadání; dolní mez je ostrá díky log_10 x'_k<1.
Indukční multiplikativní nerovnost na s. 470 je táž rovnost před
logaritmováním, s exponentem 2^(k+1)−1 u krajních faktorů chyby.

Při zaokrouhlování na čtyři významné cifry stačí delta=epsilon=0,0005.
Obě asymptotické meze absolutní chyby jsou nejvýše
0,00043440309173... <0,00044. Pro konečný počet bitů je třeba
navíc ponechat člen 2^(−k); tvrzení textu o hodnotě celého získaného
logaritmu je správné. Explicitní předpoklad 1<=y_j<100 patří k úloze:
neprohlašujeme zde chybnou normalizaci nebo přetečení za zahrnuté.

## 3. Algoritmus L s přesně stanovenou aritmetikou, úlohy 25–26

Zvolme p>=1 a D=2^p. Pracovní čísla mají p bitů za binární čárkou;
skutečné x se reprezentuje celým N=Dx. Vstup je 1<=x<2. Pravý posun
zahazuje spodní bity, takže z=D^(−1) floor(N/2^k). Odečítání x−z
je přesné; hodnoty y a tabulky mají dostatečný celočíselný rozsah,
aby nevzniklo přetečení. Je to konkrétní model požadovaný úlohou 26.

Pokud x>1, pak N>=D+1. Pro k=p je z=1/D a x−z>=1, takže se
porovnávací smyčka zastaví nejpozději při k=p; nikdy nepoužije z=0.
Každé úspěšné odečtení zmenšuje kladné celé N−D a nezmenší N pod D.
Proto výpočet skončí v x=1. Oprava odpovědi 25 z 10. října 2001
výslovně zdůrazňuje kladnost z.

Počet kroků je O(p), a to i bez předpokladu, že každý k lze použít
jen jednou. Pro k>=2 při příchodu z předchozího indexu platí
N−floor(N/2^(k−1))<D. Položme H=D/2^k, kladné celé číslo.
Pak N−D<2N/2^k<4H. Každé úspěšné odečtení při tomto k je
alespoň H jednotek, takže jich jsou nejvýše tři. Při k=1 je
N−D<2H a stačí nejvýše jedno. Index se zvýší nejvýše p−1krát.
Celkový počet odečítání M je tedy nejvýše 3p−2, případně bezpečně 3p.
Konečné kontroly nalezly nejvýše dvě opakování jednoho k; obecný
důkaz zde používá konzervativní mez tři.

Pro odhad chyby označme h=1/D. V jednom odečtení je
x_new=x(1−2^(−k))+tau, kde 0<=tau<h. Tabulková hodnota
A_k=log_b(1/(1−2^(−k))) má absolutní chybu nejvýše eta. Potom se
veličina y+log_b x změní o

```text
log_b[1 + tau/(x(1−2^(−k)))] + chyba tabulky.
```

Protože x_new>=1, je první jmenovatel alespoň 1−h, takže absolutní
hodnota tohoto přírůstku nepřekročí −ln(1−h)/|ln b|+eta.
Po ukončení log_b x=0 a dostáváme rigorózní mez

```text
|y−log_b X| <= 3p [−ln(1−2^(−p))/|ln b| + eta].
```

Pokud se zaokrouhlují také součty y, přičte se maximální chyba
jednoho sčítání k eta. Při pevné binární čárce a tabulce na stejné
mřížce jsou tyto součty přesné. Nezahrnutá počáteční konverze X na
mřížku přidá samostatný člen |log_b(X_grid/X)|. Pro přesnou tabulku
je chyba jednostranná: nezáporná pro b>1 a nekladná pro 0<b<1.

Tento důkaz vyplňuje úlohu 26, ke které kniha neuvádí odpověď.
Nepoužívá veřejné komentáře, které započítávají pouze chyby tabulky;
chyby zahazovaných bitů v x jsou zde zahrnuty výslovně.

## 4. Exponenciální varianta, úloha 28

Označme původní exponent a a největší reprezentovatelný exponent
A=1−epsilon. Správná inicializace je x=A−a, y přibližně b^A.
Invariant ideálního kroku je y b^(−x): krok odečte z x hodnotu
alpha_k=log_b(1/(1−2^(−k))) a násobí y číslem 1−2^(−k).
Po dosažení x=0 tedy y=b^a. Původní inicializace x=A ztrácí vstup a;
pro dvě různé hodnoty a vytváří stejný výpočet. Je to známá oprava
z 3. února 2002; přeuspořádání E1 z 28. října 2011 odstraňuje
další nejasnost. Ani jedna nemění kroky E3–E4.

Při chybách x_new=x−alpha_k+delta_j a
y_new=y(1−2^(−k))(1+epsilon_j) plyne teleskopováním

```text
y_final = b^[a−sum delta_j] · product_(j>=0)(1+epsilon_j),
```

kde epsilon_0 je relativní chyba počátečního y. Toto je vzorec
v odpovědi; přesná mez závisí na reprezentaci a zaokrouhlení.

Pro ověřitelnou realizaci s b=2 volíme x v násobcích h=2^(−p),
tabulku alpha_k zaokrouhlenou **nahoru** na tutéž mřížku, počáteční
y na nejbližší mřížkovou hodnotu a pravé posuny y se zahozením bitů.
Tato volba je výslovnou součástí našeho modelu; kniha ji nepředepisuje.
Pro k=p+2 je zaokrouhlená tabulková hodnota h. Porovnávací smyčka
proto vždy najde kladnou hodnotu nejvýše zbývajícímu x a zmenší x
alespoň o h. Tím se odstraňuje možnost nulové tabulkové položky
a nekonečného opakování téhož stavu.

Také zde je počet redukcí O(p). Pro k>=2 platí alpha_(k−1)<3alpha_k,
neboť pro t=2^(−k)<=1/4 máme (1−t)^3<1−2t. Zaokrouhlené
celočíselné položky tedy splňují A_(k−1)<=3A_k. Při příchodu na
nové k je zbytek menší než A_(k−1), a proto se A_k odečte nejvýše
dvakrát. Pro b=2 se k=1 vůbec nepoužije, protože jeho hodnota je 1
a zbytek je menší než 1. Stačí M<=2(p+1).

Zaokrouhlení tabulky nahoru způsobuje delta_j v (−h,0]. Počáteční
relativní chyba má velikost nejvýše h/2; během výpočtu y>=1:
invariant s kladnými korekcemi dává y>=1−h/2 a mřížka s krokem h
pak vynutí y>=1. Pravý posun tedy dává relativní korekci menší
než 2h. Dostáváme explicitní mez logaritmu relativní chyby

```text
|ln(y_final / 2^a)| <= −ln(1−h/2) + M [h ln2 + ln(1+2h)].
```

Pravá strana jde s p do nekonečna k nule díky M<=2(p+1).
Pro jiná pevná b>1 platí tentýž invariant a lze zvolit dostatečně
dlouhou kladnou tabulku; konkrétní výpočetní validátor certifikuje b=2.

## 5. Chybějící omezení základu, V1-C0002

Na s. 22 je b pro celý oddíl definováno jako kladné reálné číslo.
Text výslovně zavádí také mocniny a logaritmy pro 0<b<1. Úloha 28
na s. 26 omezuje exponent na 0<=a<1, ale základ dále neomezuje.
Postup v odpovědi však potřebuje **b>1**: jen tehdy jsou alpha_k
kladné a odečítání zmenšuje zbývající exponent.

Přesný protipříklad po použití obou oprav E1 je b=1/2,
epsilon=1/4 a vstup a=1/4. Inicializace dává x=1/2. První
tabulková položka je log_(1/2)2=−1, což je přesně reprezentovatelné.
Podmínka E3, x<−1, neplatí; E4 mění x na 3/2. Následují
5/2,7/2,..., index k zůstává 1 a E2 nikdy nevidí nulu. Už první
krok opustí rozsah původního exponentového formátu. Výsledek
nezávisí na volbě zaokrouhlení y ani na chybách logaritmické tabulky.

Toto dokládá chybějící předpoklad v našich zdrojích. Přidání b>1
je stručná oprava odpovědi a zahrnuje běžné základy 2,e,10.
Hodnota b=1 se řeší konstantním výstupem 1; hodnoty 0<b<1 lze
ošetřit zvlášť přes převrácený základ. Neprohlašujeme zde za chybný
algoritmus L, který funguje i pro záporné hodnoty log_b X.

Prohledány všechny historické i současné řady errat pro s. 22,26,470,
úlohu 28, logaritmy a omezení b. Relevantní změny jsou právě
inicializace 2002/2011 a přečíslování rovnic 2024; omezení b>1
jsme nenalezli. Ve veřejné rešerši byla nalezena
[Werkemova vzpomínka na chybu inicializace](https://www.werkema.com/2021/10/14/my-knuth-check/),
která tento odlišný problém neřeší. Jeho znění opravy není používáno
místo autorových errat. Nenalezení dřívější zmínky není důkaz prvenství.
Tištěný exemplář ani stanovisko autora nebyly ověřeny.

## 6. Výpočetní doklady a rozsah

`check_logarithms.py` prošel jednou. Obsahuje doslovný celočíselný
model zaokrouhlených čtverců, racionální intervaly pro správné bity,
certifikované zaokrouhlení tabulkových konstant a všech 8190
reprezentovatelných vstupů pro p=1,...,12 pro každý z modelů L/E.
Přechody a protipříklad jsou přesné. Porovnání pozorované chyby
s obecnou mezí používá Decimal se 70 ciframi a je diagnostické;
důkazy mezí jsou v oddílech 2–4, nezávisle na těchto porovnáních.
Výsledky jsou v `results/logarithms.json`.

Historické a bibliografické věty v poznámkách k úlohám 25,28
ještě nejsou uzavřeny. Řada pro ln(1/(1−t)) na s. 471 je správná:
integrace geometrické řady dává sum_(j>=1)t^j/j pro |t|<1,
tedy po t=2^(−k) přesně uvedené koeficienty. Celé citované články
o trigonometrických algoritmech tím nejsou certifikovány.
