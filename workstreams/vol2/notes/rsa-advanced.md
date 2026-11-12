# §4.5.4: úlohy 44 a 47

Audit 3. listopadu 2026, třetí vydání, první dotisk. Zadání na
[417](../images/vol2-p417.png), odpověď 44 na
[669](../images/vol2-p669.png) a [670](../images/vol2-p670.png)
a relevantní historická errata byly přečteny vizuálně.

**Výsledek:** mřížový důkaz 44 je správný. Potvrzen bibliografický
[C0168](C0168-hastad-year.md): LNCS 218 vyšlo v roce 1986.
Původní šifra 47 byla nezávisle dekódována a její tři prvočinitele
certifikovány. Náhradní šifra z roku 2012 je auditována ve vymezeném
výzkumném rozsahu; její rozluštění ani faktorizaci zde nemáme.

## 1. Úloha 44: význam mřížové konstrukce

Máme k polynomů f_i(X)=sum_{j=0}^{d-1} a_ij X^j a po dvou
nesoudělné moduly m_i. Hledáme celá x s |x|<m=min(m_i), pro
něž f_i(x)=0 (mod m_i). Každý seznam koeficientů je společně
nesoudělný s příslušným m_i. Není třeba, aby některý jednotlivý
koeficient byl invertovatelný. Položme

    k = d(d-1)/2+1, n=d+k, M=prod_i m_i.

Pro kubické zadání je d=4, k=7, n=11. **Mříž** tvoří všechny
celočíselné kombinace řádků regulární matice L. Její determinant
je absolutní hodnota determinantu této matice, tedy objem
základního rovnoběžnostěnu. Délka vektoru je zde euklidovská:
odmocnina součtu čtverců jeho souřadnic.

Knižní nápověda dodává algoritmus LLL (Lenstra–Lenstra–Lovász),
který v polynomiálním čase najde nenulový celočíselný vektor v
s délkou vL nejvýše sqrt(n*2^n)*det(L)^(1/n).
Tuto algoritmickou větu používáme jako výslovný externí vstup.
Håstadův autorský článek na straně 3 uvádí dokonce silnější
koeficient 2^((n-1)/4), takže slabší knižní mez postačuje.

Zvolme CRT koeficienty u_i, které jsou 1 modulo m_i a 0 modulo
ostatní moduly. Prvních d řádků L má na diagonále m^j M,
0<=j<d. Další řádek i má v prvních d sloupcích
m^j a_ij u_i a v soukromém posledním sloupci M/(m_i d).
Ostatní složky jsou nulové. Matice je dolní trojúhelníková a

    det(L) = M^(n-1) m^(k-1) d^(-k).              (1)

Racionální jmenovatel d odstraníme vynásobením celé matice d.
Délky i odmocnina determinantu se změní stejným činitelem,
takže lze přímo použít celočíselný LLL.

Protože M>=m^k, z (1) plyne

    length(vL) <= sqrt(n*2^n) M m^(-1/n) d^(-k/n) < M/d,

pokud

    m > n^(n/2) 2^(n^2/2) d^d.                  (2)

Pro d=4 je celá část pravé strany přesně

    222953590820751881043264879 < 10^27.

Kontrola používá celočíselnou odmocninu čísla 11^11*2^121*4^8,
nikoli zaokrouhlený desetinný logaritmus. Hypotéza zadání tedy stačí.

Pišme v=(t_0,...,t_(d-1),v_1,...,v_k) a definujme

    c_j = t_j M + sum_i a_ij u_i v_i,
    P(X) = sum_j c_j X^j.

Prvních d souřadnic vL je m^j c_j. Pro hledané x máme
P(x)=v_i f_i(x)=0 (mod m_i), tedy M|P(x).
Současně |m^j c_j|<M/d a |x|<m dávají |P(x)|<M.
Proto platí přesná celočíselná rovnost P(x)=0.

Zbývá podstatný krok: P není nulový polynom. Jinak by pro
všechna j platilo m_i|v_i a_ij. Bézoutova identita pro společný
gcd koeficientů a m_i dává m_i|v_i. Poslední souřadnice krátkého
vektoru současně dávají |v_i|<m_i, tedy všechna v_i=0.
Potom c_j=t_j M=0 vynutí všechna t_j=0, spor s v≠0.

Máme tedy nejvýše d-1 celočíselných kandidátů. Otestujeme je
v původních kongruencích. Obecné zadání nemusí určovat jediný
kořen; odpověď tuto možnost výslovně připouští. Všechny vstupní
koeficienty lze nejprve redukovat modulo m_i. Pro pevné d=4
mají matice i následný polynom polynomiální velikost v log M.

## 2. Získání kořenů a nezávislá kontrola

K dokončení algoritmu není nutná faktorizace konstantního členu P.
Vlastní validátor používá **Sturmovu posloupnost**: po odstranění
společného dělitele P a jeho derivace vytváří posloupnost
P, P', záporný zbytek po dělení, a tak dále. Rozdíl počtů změn
znaménka na koncích intervalu určuje počet různých reálných kořenů.

Interval celých kandidátů [1-m,m-1] dělíme binárně a počty kořenů
vyhodnocujeme na půlcelých hranicích. Celočíselný kořen tak nikdy
neleží na hranici. V každé úrovni zbývá nejvýše deg(P) neprázdných
intervalů; po O(log m) úrovních testujeme jednotlivé celočíselné
kandidáty přesným dosazením. Sturmovu větu zde používáme jako
standardní externí algebraickou větu; dělení a vyhodnocení
posloupnosti jsou implementovány vlastní racionální aritmetikou.

Devět instancí pokrývá d=2,3,4,5, nulový kořen, oba krajní
případy |x|=m-1, obecné polynomy, známé lineární změny před
umocněním, tři společné kořeny a společnou nesoudělnost bez
jednotlivého invertovatelného koeficientu. Moduly jsou po dvou
nesoudělné prvočíselné mocniny; pro poslední zvláštní případ je
první modul mocnina 6. Testuje se obecné algebraické zadání 44,
nikoli jen součiny dvou prvočísel.

FLINT navrhuje redukovanou bázi i transformační matici.
Vlastní celočíselný validátor ověřuje celou rovnost T*A=R,
det(T)=±1, determinant A=dL, racionální ortogonalizaci řádků,
nerovnosti redukce a především přesnou požadovanou délkovou mez.
Potom kontroluje koeficienty P, všechny kongruence a nulové
dosazení. Samostatný checkpoint nalezne kořeny bez znalosti
zasazeného x a kontroluje i násobné a půlcelé kořeny.

Na začátku 405 se známé časové značky převádějí na právě takové
kubické kongruence. Jejich vedoucí koeficient je mocnina dvou,
a proto je u lichých RSA modulů invertovatelný. Sedm kongruencí
se tedy vejde do prokázané konstrukce, za velikostní podmínky 44.

## 3. Úloha 47: původní šifra

[Přesný vstup](../sources/rsa47-inputs.json) obsahuje obě původní
šifrované hodnoty i modul, porovnané s původní sazbou. Modul má
211 desetinných číslic a 701 bitů. Návrh rozkladu byl převzat
z veřejné databáze FactorDB; jeho správnost ani prvočíselnost
jsme nepřijali jen podle stavu databáze.

Tři prvočinitele mají 25, 91 a 97 číslic. Jejich součin přesně
souhlasí s knižním N. PARI vytvořilo certifikáty a náš samostatný
validátor ověřil 19 článků na eliptických křivkách a 35 koncových
Lucasových prvočísel. Pracuje přesnou afinní aritmetikou a kontroluje
invertovatelnost jmenovatelů, velikostní podmínku a nenulovost bodů.
Koncové certifikáty jsou rekurzivně ověřeny celočíselnými kongruencemi.
Všechna tři prvočísla jsou 2 modulo 3, takže umocnění na třetí je
permutací všech zbytků modulo jejich součin, stejným důkazem jako
v [RSA §1](rsa-basic.md#1-modulární-inverze-a-společná-zpráva).

Každá třetí odmocnina byla získána přímou modulární inverzí,
vlastním binárním umocňováním a rekonstrukcí ze tří prvočíselných
modulů. Zpětné umocnění obou bloků přesně vrací tištěné šifry.
Bloky obsahují 86 a 87 ASCII bajtů v pořadí od nejvýznamnějšího.
[Celý ověřený text](../results/rsa47-original-plaintext.txt) je
Chestertonův citát z příběhu The Tremendous Adventures of Major Brown
v The Club of Queer Trades (1905).

[Knuthovo oznámení z roku 2012](https://www-cs.stanford.edu/~knuth/news12.html)
říká, že se o rozluštění od Grega Childerse dozvěděl 14. září.
[Archiv NFS@Home](https://escatter11.fullerton.edu/nfs/old_news.php)
má zprávu s odhaleným citátem z 15. září 2012. Jde o různá data
sdělení a veřejného oznámení, nikoli rozpor. Odkazy na podrobné
forum 373/374 dnes přesměrovávají na přihlášení; jejich obsah
nemáme. Pozdější [nezávislá reprodukce](https://github.com/sytelus/taocp/blob/main/problems/taocp-v2-4.5.4-47.md)
sloužila jako navigace k číselným údajům. Nová vlastní certifikace
a dešifrování jsou uloženy v tomto pracovním stromu.

## 4. Náhradní šifra a hranice auditu

Errata z 23. října 2012 nahrazují číselné údaje úlohy a přidávají
odpověď o starém řešení. Nový modul má **318 číslic a 1056 bitů**.
Všechny tři hodnoty z Knuthova [desítkového souboru](https://www-cs.stanford.edu/~knuth/newn)
souhlasí přesně s jeho [hexadecimálním souborem](https://www-cs.stanford.edu/~knuth/newn-hex);
byly také vizuálně porovnány s [erraty, strana 11](../images/all2-pre-rsa-advanced-p11.png).
Zvláště počáteční c modulu a další písmena c se při běžné textové
extrakci PDF ztrácejí; nelze tedy vycházet z prostého OCR.

Obě nové šifrované hodnoty leží v [0,N). Nový modul je složený:
báze 2 porušuje Fermatovu kongruenci, ověřeno dvěma algoritmy
modulárního umocnění. Se starým modulem má gcd=1.
FactorDB při přístupu 3. listopadu 2026 eviduje složené číslo
bez netriviálních faktorů. Tato informace není důkazem, že nikdo
nezná jiné rozluštění; při naší rešerši jsme je nezískali.
Novou šifru jsme nefaktorizovali ani nerozluštili.

Od 6. listopadu 2026 je celá aktualizovaná úloha 47 partial:
stará verze je úplně numericky ověřena, ale známá náhrada a její
výzkumný status nejsou vyřešením nové 318ciferné výzvy.

## 5. Zdroje, errata a běhy

Håstadův [původní náhled strany 403](https://page-one.springer.com/pdf/preview/10.1007/3-540-39799-X_29)
má v zápatí rok 1986. Potvrzuje jej
[vydavatel](https://link.springer.com/chapter/10.1007/3-540-39799-X_29).
Autorská [pozdější verze](https://johanhastad.se/rsalowexponent.pdf)
byla čtena v úvodu a §§2–3 i Application 1; strany 3–5 vizuálně.
Používá úspornější mříž než knižní odpověď. Z ní nepřebíráme
bez důkazu knižní determinant ani jeho konkrétní konstantu.
Podrobný externí audit celé publikace nebo algoritmu LLL se netvrdí.

Prohledány všechny čtyři vrstvy errat i aktuální TeX podle 417,
669–671, Håstad, 218, 44, 47 a low exponent. Rok citace není
opraven. Známé změny 43 a 45–46 na okolních stranách patří
k jiným úlohám; náhrada 47 a nová odpověď byly přečteny vizuálně.

[Program](../verify_rsa_advanced.py), [výsledky](../results/rsa-advanced.json),
[certifikáty](../results/rsa47-certificates.json) a
[metadata](../sources/rsa-advanced.json) umožňují reprodukci.
První běh PID 1301447, session 12935, limit 240 s skončil kódem 1:
všech devět mřížových kontrol prošlo, ale zápis velkého determinantu
narazil na Pythonův limit 4300 desetinných číslic. Log je zachován.
Po změně pouze serializace bylo nutné vytvořit chybějící uložené
výstupy znovu. Druhý běh, session 21055, skončil exit 0:
mříže 3.140 s a šifra s certifikáty 1.249 s.
Následná extrakce kořenů je oddělený třetí checkpoint; předchozí
dva se neopakovaly. Přesné časy a PID jsou v metadatech.

Pozdější fyzický dotisk a prvenství nálezu roku neověřeny.
Žádné hlášení nebylo odesláno.
