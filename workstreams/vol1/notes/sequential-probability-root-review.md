# §2.2.2-13: dokončení obou zbývajících limitních důkazů

> Aktualizace5.11.2026: souvislá revize a aktuální pramenné výjimky jsou v [novém zápisu](sequential-allocation-2026-11-05.md). Starší stav otevřených kroků níže je historický; úloha13 je nyní uzavřena, C0035 zůstává otevřený.


Koordinátor 1. listopadu 2026 přečetl a zkontroloval celé
`parallel/sequential-probability/critical-proof.md` a
`contracting-proof.md`, včetně všech limitních přechodů. Nový
matematický nedostatek nezůstal. Předchozí kořenový důkaz pro
pevné m a p→1, přesné malé kapacity a rostoucí případ p<1/2
zůstává v `sequential-probability.md`.

Zde p znamená pravděpodobnost odebrání, m kapacitu a X,Y velikosti
zásobníků v okamžiku zaplnění. Pro p=1/2 je nyní obecně dokázáno
`E max(X,Y)/m -> 0.6753144833135676...`; pro každé pevné
1/2<p<1 je X/m asymptoticky rovnoměrné na [0,1], tedy
`E max(X,Y)/m -> 3/4`. Při p=1 k zaplnění vůbec nedojde.

## Nezávisle zkontrolované podstatné kroky

Přesné diskrétní rozvinutí používá půlčíselné osy odrazu. Posun
o polovinu je nutný, aby odebrání z prázdného zásobníku bylo
nulovým krokem. Po otočení vyjde diagonální procházka ve čtverci
se startem (h,0), h=1/(m+1). Parita vylučuje rohy a dává přesnou
identitu pro maximum, ne pouze asymptotickou aproximaci.

Fourierovy koeficienty hraniční funkce 1−|t| byly ověřeny přímou
integrací: jsou 2/a_k² pro a_k=(k+1/2)pi. Celá řada stejnoměrně
konverguje až k hranici. Stažení argumentu na r<1 umožní Taylorův
odhad s omezenými čtvrtými derivacemi; jeden krok má chybu O_r(h^4),
zatímco střední doba zastavení je nejvýše h^−2. Pořadí limit
h→0 a poté r→1 je správné. Tím je kritická diskrétní limita
dokázána bez nezdůvodněného zastavení funkcionálního limitního teorému.

U Greenovy funkce byl samostatně ověřen rozklad logaritmických
singularit, koeficient 2/pi a jednotkový tok čtvrtkružnicí. Nulový
průměr určuje konstantu Neumannovy úlohy a antisymetrie vynuluje
potenciál na přeponě. Hraniční tok `J(t)=2+4(f(t)+f(1−t))` má
integrál jedna. Váha t v integrálu pro maximum zajišťuje absolutně
sumovatelný odhad O(n^−2), takže integrace po členech je oprávněná.
Obě pomocné primitivní funkce v rovnici(20) byly derivovány zpět;
výsledek dává přesně knižní sinh řadu i identitu s cosh řadou.

V kontrakční oblasti je `rho=(1−p)/p<1`. Kvadratický potenciál
X²+Y² má mimo pevnou konečnou množinu drift nejvýše −1; opakovaný
kladně pravděpodobný pokus odebrat vše uvnitř této množiny dává
skutečný konečný odhad doby návratu, nikoli pouze formální drift.
Vratnost zastavené Greenovy funkce pak ohraničuje pravděpodobnost
návratu z hloubky L k zaplnění výrazem `(m+1)(m²+C_p)rho^L`.
Pro L řádu log(m) tento výraz mizí. Jednorozměrný zásahový vzorec
a kontrola pravděpodobnosti předčasného dotyku os dávají návratovou
pravděpodobnost 1−rho na vnitřku předposlední vrstvy.

Přesná identita `H_m(j)=W_m(j)/sum W_m`, kde W je součet těchto
návratových pravděpodobností v předchůdcích, odstraňuje neplatnou
záměnu prvního zásahu za stacionární hmotnost. Vnitřní W konvergují
k 2(1−rho); omezení W≤2 samostatně kontroluje koncovou hmotnost.
Slabá uniformní limita a limita maxima proto platí i bez bodové
uniformity přímo v koncích.

## Zdroje a stav evidence

Originály zadání a odpovědi byly již kořenově prohlédnuty. Nově
koordinátor zobrazil výřez Flajoletovy původní s.336: skutečně
tiskne nesprávný integrál bez váhy t a číslo0.67526. Ze správně
normalizované hustoty má tento integrál hodnotu9/8. TAOCP takový
vzorec ani číslo nepřebírá. Ani silnější bodová koncová formulace
externí věty3 není tvrzením knihy. Tyto vady externího pramene
nedostávají globální ID nálezů TAOCP; prvenství jejich zjištění
ani pozdější opravy článku zde nejsou prověřovány.

Všechny matematické části úlohy13 jsou nyní checked. Celkový stav
úlohy zůstává partial pouze kvůli přesnému časopiseckému Yao1981,
jehož plný text nebyl získán. Přečtený autorův report1979 není
vydáván za totožnou časopiseckou verzi. Úspěšné starší výpočty
se znovu nespouštěly a Lean nebyl potřebný.
