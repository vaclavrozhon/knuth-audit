# ZDD: přesné počty 255,257–259 a malé barevné modely

Původní DLX6 je archivován s URL, datem a SHA-256. Změnový soubor
`dlx6-small.ch` pouze snižuje kapacitu cache a hash tabulky; nemění algoritmus.
Nezávislý model používá množiny řádků a memoizaci podle zbývajících položek,
nikoli obousměrné seznamy. Počítá každé odstranění hlavičky a uzlu jako update.

Oba programy souhlasí na kompletních grafech K2 až K20, plných a omezených
permutacích n=1,…,10 a extrémních pokrytích n=1,…,9. Souhlasí přesné počty
řešení, updatů, uzlů ZDD i uložených signatur. Dalších300 malých náhodných
barevných XCC vstupů bylo ověřeno rozvinutím celého výstupního ZDD na množiny
čísel možností a porovnáním s úplným výčtem podmnožin řádků.

## F079: o jeden uzel méně ve vzorci pro perfektní párování

Na straně121 má být u sumy **+3 místo +2**, stejně jako v odpovědi255 na
straně481 má být **V_N+3**. Platí pro kladné sudé N. V součtu zahrnuje člen
l=N/2 dokončené řešení a přispívá −1. Tento stav ale nevytváří záporný počet
větví: nevytváří žádnou. Proto je třeba tento člen vyrušit a pak přičíst dva
terminály. Ekvivalentní oprava omezí sumu na l<N/2 a ponechá +2.

Nejmenší příklad K2 má jeden rozhodovací uzel a dva terminály, tedy3;
tisk dává2. Pro K8 má být99 místo98 a pro K16 10 228 místo10 227.
Číselné příklady99 a10 228 v hlavním textu jsou správné; chybný je obecný
vzorec. Uzavřený tvar V_n samotný, počty updatů W_N−1 a asymptotika zůstávají.
Obě místa potvrzena v obrazu PDF a autorova PS (strany57 a185).

U lichého N rozlišujeme navštívené signatury F_(N+1) a navíc předem uloženou,
ale nenavštívenou prázdnou signaturu. Tuto účetní konvenci zde nevydáváme za
samostatný nález.

## F080: v 259(b) chybí n uložených signatur

Počet má být **binom(n+1,2)+1**, nikoli binom(n,2)+1. Na úrovni l=0,…,n−1
existuje l+1 signatur: zbývají X_(l+1),…,X_n, všechny Y_(l+2),…,Y_n a právě
jedna z Y_1,…,Y_(l+1). Dále je uložena prázdná signatura. Součet je
1+1+2+…+n. Pro n=2 jde o čtyři signatury místo dvou, pro n=3 o sedm místo čtyř.

Slovní popis v 259(a,b) zaměňuje pokryté a nepokryté Y: podle definice
signatury na straně120 je u(a) potřeba (n−l)-prvková nepokrytá podmnožina,
u(b) právě výše popsaná množina. Pokud chce autor popisovat pokryté Y,
může tak učinit, ale musí výslovně říct, že kóduje jejich doplněk.
Číselné tvrzení o memech je chybné nezávisle na této volbě kódování.

Počty uzlů n²+2 a updatů (2n³+15n²+n)/6 v(b) jsou správné. Na úrovni
l<n−1 má každý stav2 větve a stojí 2(n−l)+3 updatů; posledních n stavů
stojí po3. To dává uvedenou kubickou formuli. V(a) stojí stav s m zbývajícími
X přesně m²+m+1 updatů; součet podle binomických násobností dává správnou
formuli knihy. Vzorce i příklady byly nezávisle ověřeny. Znění259 je stejné
v PDF str.481 i autorově PS str.185.

## Správné další vzorce a rozsah

257 má správných2^(n−1)+1 signatur. 258 má správnou binomickou transformaci
lokálních nákladů v_n a hodnotu V16=40 454 337 297. Člen ve vzorci je
1800 n 2^n, nikoli1800 n²; prvotní chybný přepis v našem kontrolním kódu byl
opraven po přečtení obrazu. Binomická transformace byla přesně porovnána
pro n≤100; obecné odvození používá (1+a)^(n−1) a jeho derivaci.

Neprověřujeme zde velké aplikace263, celé úlohy252,256,260,261 ani formální
správnost všech ukazatelových operací Z. Výstupy malých barevných úloh jsou
přesně ověřené, nikoli jen počty modelů.

Reprodukce: [check_zdd_counts.py](check_zdd_counts.py),
[všechny počty](results/zdd_counts/formulas.json),
[barevné rodiny](results/zdd_counts/colored-random.json),
[algebra](results/zdd_counts/algebra.json). Vstupy `.xcc`, původní logy a ZDD
jsou ve stejném adresáři. V all4b ani all4f5 odpovídající opravy nenalezeny.

## Obnova výpočetního prostředí

Stačí Python 3, C překladač a `ctangle` z CWEB. Archiv obsahuje také
potřebný modul GraphBase, takže není třeba zachovat původní soubory v `/tmp`.
Spusť `python3 audit-2026-10-31/build_zdd_solver.py` z kořene repozitáře.
Program přeloží zdroje v novém samostatném dočasném adresáři a vypíše cestu
`binary`. Potom spusť `check_zdd_counts.py` s proměnnou `KNUTH_DLX6_BIN`
nastavenou na tuto cestu. Kontrolní skript přepočítá a přepíše své výsledky;
pro pouhé čtení auditu to není nutné.
