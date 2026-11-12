# Tableaux39(f): úplný důkaz opravené inverze

Doplnění P0594, zadání70–71/file81–82 a odpověď614/file625.
Sazba614 byla znovu zobrazena kvůli přesnému pravidlu Q2/Q3.
Používají se obě již doložené opravy: návrat S′ do S2′ (C0006)
a potlačení horního souseda na aktuálním řádku i (C0020).
Protipříklady ani příklady P0583–93 se neopakují.

Níže je vlastní úplný argument v knižních souřadnicích. Publikovaný
NPS důkaz byl orientací; jeho geometrická tvrzení se zde nenahrazují
pouhým odkazem. Všechny klíče jsou různé a kladné, buňky mají pevný
Youngův tvar. Chybějící soused při zpětném kroku má hodnotu0.

## 1. Přesný stav a dvě lokální inverze

Pro u=(i,j) označme S_u všechny buňky v nižších řádcích a buňky
řádku i od j doprava. Před inverzním krokem je P na S_u rostoucí
po řádcích/sloupcích. Pomocná Q mají háčkové meze. Každá nekladná
Q_ik, k≥j, určuje kandidáta c=(i−Q_ik,k), jehož zpětná cesta
max(horní,levý), s horním sousedem potlačeným v řádku i,
dosáhne u. To je potřebná silnější indukční podmínka.
Zpracované Q lze konceptuálně nulovat; později se nečtou (P0593).

Zpětné hrany na celém pásu řádků≥i tvoří strom: vždy zmenšují
součet souřadnic a každý vrchol má jediného rodiče, až na(i,1).
Řádek i může mít vlevo od j neuspořádané hodnoty; toto nezávisí
na jejich pořadí. Kandidátní cesty mají společný kořen u v jeho
podstromu. Kódy se čtou od u dolů/doprava a končí Q, s D<Q<R.

Nechť dopředný sift přesune K z u po cestě
π=(x_0=u,x_1,…,x_L=z). Před ním je uspořádané S_v, kde
v je následující buňka řádkového pořadí. Hodnoty A(x_l), l≥1,
striktně rostou a jsou<K (P0583). Po siftingu B(x_(l−1))=A(x_l)
a B(z)=K. Zpětný krok z x_l vybere x_(l−1):
druhý severní/západní soused neleží na π a je menší než A(x_l),
protože A je na S_v uspořádané. Je-li mimo tvar, má0; při prvním
vodorovném kroku je horní soused v řádku i potlačen. Druhý soused
nemůže být jinou dřívější buňkou π: monotónní cesta by z ní
nedošla do x_(l−1) bez kroku nahoru nebo doleva.
Takto se π přesně obrátí.

Naopak začněme uspořádaným B na S_u a libovolnou jeho zpětnou
cestou od z do u. Při unfixu se původní B(x_(l−1)) posune do x_l,
l≥1, a K=B(z) do u. Výsledné A je uspořádané na S_v:
v x_l je větší ze starých dvou severních/západních sousedů;
druhý soused není na π. Následující buňka π dostala původní
B(x_l), tedy větší hodnotu, a jiný jižní/východní soused zůstal
ještě větší než B(x_l). Vztahy mimo π se nezměnily.
Dopředný sift K pak v x_l vybere x_(l+1), protože tam je B(x_l),
zatímco druhý jižní/východní soused má větší původní hodnotu.
V z oba další sousedé>K, takže se zastaví právě tam.
Obě lokální inverze tedy platí bez předpokladu bijektivity.

## 2. Pořadí cest v rovinném stromu

Dvě cesty z u ve stromu se po prvním rozdělení již nesetkají:
jinak by společný vrchol měl dvě různé cesty k rodičům.
Jsou to monotónní mřížkové cesty bez křížení.

Pišme pro π v každém dosaženém sloupci h její první a poslední
řádek a_h,b_h. Platí a_j=i, a_(h+1)=b_h pro h<s, kde z=(r,s).
Každý sloupcový úsek π obsahuje všechny řádky od a_h do b_h.

Potřebujeme následující přesné důsledky. α je kód konce π.

- Jestliže jiná stromová cesta β končí ve sloupci h<s a její kód
  je větší než α, její koncový řádek t splňuje t<b_h.
  Je-li β prefix π, musí π dále jít D (Q>D), takže končí před
  spodním koncem sloupcového úseku. Jinak se β oddělí krokem R
  tam, kde π jde D. Bez dalšího průsečíku zůstává β nad π:
  při vstupu do společného sloupce je celá β nad první buňkou π.
  Rovnost by byla společný vrchol. Opačné rozdělení D/R by dalo
  menší kód. π nemůže být prefix β, protože h<s.
- Jestliže větší β končí ve sloupci h>s, její poslední zpětný
  vstup na π jde zprava. Buď se dopředně oddělí R proti D,
  nebo pokračuje z konce π krokem R (R>Q). Pokračování D by
  naopak dalo D<Q.
- Obráceně každá cesta končící v buňce(t,h), j≤h<s, t<b_h,
  která se napojí na π, má větší kód. Na π končí před krokem D;
  mimo π je nutně nad ní, takže se oddělí R proti D.

Pro přesnost použitého „nad“: po rozdělení R/D mají cesty různou
výšku na první svislé přímce mezi sloupci. Kdyby se pořadí výšek
v následujícím sloupci změnilo, dva svislé souvislé úseky v něm
nebo sousední vodorovné hrany by měly společný vrchol.
To je ve stromu po rozdělení vyloučeno. U koncové buňky druhé
cesty totéž platí i tehdy, když tam skončí dříve než první.

Ještě jedna geometrická skutečnost nevyžaduje stromové pravidlo:
z(t,h) s t<b_h vede každá cesta nahoru/doleva v pásu řádků≥i
na π dříve, než by opustila její levou stranu. Pokud nezačíná
na π, má t<a_h. Při kroku doleva do h−1 pak t<b_(h−1)=a_h;
buď vstoupí na π, nebo zůstane nad jejím úsekem. Tak nemůže
minout sloupec j, jehož první řádek je i.

## 3. Dvě lokální bariéry pro dopřednou cestu

Nechť A je pole před dopředným siftem z u, v=(i,j+1), j<λ_i.
Zpětné cesty A končí v v a do sloupce j tedy nikdy nevstoupí.
π je skutečná dopředná cesta z u do(r,s).

**Dolní oblast.** Pro j<k≤s žádná zpětná cesta do v nemůže
obsahovat buňku(t,k) s t>a_k. Kdyby takovou buňku obsahovala,
každý další krok doleva zůstane pod hranicí, protože a_k neklesá.
Krok nahoru může překročit hranici jen z(a_k+1,k).
Ale π přišla do sloupce k doprava z(a_k,k−1); její volba znamená

    A(a_k,k) < A(a_k+1,k−1).

Dolní/levá buňka existuje, pokud existuje(a_k+1,k).
Zpětný max-krok proto v(a_k+1,k) vybere levého souseda,
nikoli horního. Pod hranicí tedy zůstane, případně opustí oblast
doleva do sloupce j; ani potom již nemůže dojít do v.
Tento rozpor dokazuje požadovanou mez pro každou buňku staré
kandidátní cesty, nikoli jen pro její počáteční buňku.

**Horní oblast.** Rozšiřme a_k pro k>s hodnotou r a definujme

    G={ (t,k) v diagramu : k≥j+1, i≤t≤a_k }.

Každá zpětná cesta v A začínající v G dosáhne v a G neopustí.
Krok nahoru zachovává nerovnost. Levý krok by ji porušil jen
při a_(k−1)<t≤a_k, tedy uvnitř svislé části π ve sloupci k−1
(včetně posledního sloupce, je-li k=s+1). Při kroku π z(t−1,k−1)
dolů totiž platí

    A(t,k−1) < A(t−1,k),

a zpětné maximum vybere horního souseda. Pro k=j+1 se používá
a_j=i. V horním řádku se jde doleva až do v. Pro k>s+1 jsou
hranice stejné, takže jejich překročení vlevo nenastane.
Cesta je konečná, neboť součet souřadnic klesá. Všechny buňky
nutné pro uvedené porovnání existují podle Youngova tvaru;
vnější pravý soused se zde nemůže objevit, protože(t,k) existuje.

Obě bariéry jsou přímé dvoubuněčné nerovnosti z rozhodnutí
min(dolní,pravý). Nejde o předpokládaný globální obrázek.

## 4. Dopředná stabilita a skutečně první kandidát

Před krokem z u nechť platí kandidátní invariant pro v.
Po siftingu π v B zpětně přesně vede z z do u (část1).
P3 udělá ze z kandidáta nastavením Q_is=i−r.

Starý kandidát ve sloupci k>s zůstane na místě.
Hodnoty na π kromě u se při siftingu zvětší, mimo π se nezmění.
Jeho nová zpětná cesta tedy sleduje starou cestu do v až do
prvního vstupu na π: zvýšený soused na π může přitáhnout cestu
dříve, nemůže ji od π odklonit. Pokud na ni nevstoupí dříve,
dojde do v a po horním řádku do u.

První vstup na π nemůže jít zdola. Kdyby π od příslušné buňky
pokračovala D, buňka těsně pod ní by již byla na π. Při R nebo
na konci π by stará cesta obsahovala buňku pod a_h ve sloupci
h≤s, což zakazuje dolní bariéra; pro h=j tam stará cesta
nemůže být vůbec. Vstup je proto zprava. Jeho dopředný kód
se od π oddělí R proti D, nebo pokračuje R za koncem π;
v obou případech je větší než α.

Starý kandidát(t,k), j<k≤s, se po levém posunu Q zachová
jako kandidát právě při Q_ik≤−1, a pak se stane(t−1,k−1).
Při Q_ik=0 se změnil v kladnou hodnotu a kandidátem již není.
Dolní bariéra dává t≤a_k=b_(k−1), tudíž t−1<b_(k−1).
Geometrie části2 zaručí, že nová zpětná cesta narazí na π,
odtud dojde do u a má větší kód než α. Její buňka existuje:
z původní buňky je jeden krok nahoru/doleva, t≥i+1.

To jsou všichni noví kandidáti. Koncový z je jediný s kódem α;
všichni ostatní mají kód větší. Invariant i pravidlo prvního
kandidáta jsou tedy zachovány.

Je-li u poslední buňka svého řádku, není třeba předchozí řádkový
invariant: P3 vytvoří jediného kandidáta z ve sloupci j=λ_i.
Jeho zpětná cesta je lokální inverzí. Totéž pokrývá první krok
celého dopředného průchodu. Nulová cesta π=(u) je zahrnuta:
žádný kandidát se diagonálně neposouvá a ostatní se připojí zprava.

## 5. Zpětná stabilita, obě meze Q a všechny kandidátní případy

Začněme libovolným stavem splňujícím invariant pro u a vezměme
první kandidát z=(r,s). Takový kandidát existuje: Q_i,λ_i≤0
a jeho dolní mez zaručuje platnou buňku.
Jeho cesta π se unfixem změní na A uspořádané na S_v;
dopředný sift K ji obrátí podle části1.

Q2 mění budoucí hodnoty na

    Q_old,i(h+1)=Q_new,ih−1,    j≤h<s.

Horní háčková mez se zachová přímo:
Q_new,ih−1≤λ_i−h−1. Pro dolní mez rozlišíme:
pokud Q_new,ih≥1, nová hodnota je nezáporná.
Pokud Q_new,ih≤0, jde o současného kandidáta(t,h).
Jeho kód je větší než kód vybraného z a h<s. Část2 dává
t<b_h, takže buňka(t+1,h+1) existuje: π v řádku b_h přešla
do h+1 a Youngův diagram obsahuje všechny buňky nad ní.
Nová hodnota i−(t+1) tedy splňuje i−λ′_(h+1)≤Q_old,i(h+1).
Ostatní Q se nezmění a opuštěné Q_ij lze vynulovat.

Nyní všechny nové kandidáty:

- Q_new,ih≤0 dává(t+1,h+1) s t+1≤b_h=a_(h+1).
  Je v horní oblasti G z části3, proto zpětně dojde do v.
- Q_new,ih=1 dává(i,h+1), tedy rovněž buňku v G.
- Q_new,ih>1 nedá kandidáta.
- Kandidát ve sloupci k>s zůstane na místě. Jeho kód je větší
  než α, a proto jeho původní zpětná cesta poprvé vstoupí na π
  zprava (část2). Při unfixu hodnoty na π kromě u klesají.
  Dokud stará cesta nevybere souseda na π, nová se nemění:
  dosud nevybraný soused na π se jen zmenšil.
  Před prvním takovým vstupem je cesta v buňce(t,h+1) napravo
  od π, s t≤b_h. Je tedy v G, protože b_h=a_(h+1) pro h<s
  a b_s=r pro h=s. V A odtud podle horní bariéry dojde do v,
  ať nyní vybere levého, nebo horního souseda.

Změna hodnoty v u tento argument neporuší: prvním sousedem u
na cestě přicházející zprava je v, kde už nová cesta končí.
Příchod zdola je u těchto větších kódů vyloučen.

Je-li j=λ_i, další v=(i+1,1) začíná celý nižší řádkový pás.
Po lokálním unfixu je tento pás uspořádaný. Každá zpětná cesta
s novou horní hranicí i+1 končí v jeho levé horní buňce v,
takže nový kandidátní invariant platí automaticky. Poslední
buňka celého diagramu ukončuje průchod.

Tím jsou zpětně zachovány všechny části stavu; nebyla použita
hook formula ani rovnost počtů vstupů a výstupů.

## 6. Oba směry bijekce, jednoznačnost(e) a hranice

Dopředný průchod začíná s konceptuálními nulovými Q a prázdným
uspořádaným suffixem. Část4 induktivně dokazuje první kód konce
každého siftingu. Opravené Q tedy obrátí každý krok P a vrátí
původní permutaci.

Opačně vezměme libovolné standardní P a libovolné Q v háčkových
mezích. V u=(1,1) všechny zpětné cesty dojdou do u, takže výchozí
invariant platí. Část5 zachovává tento invariant až do konce.
Každý krok lze lokálně obrátit siftingem a přesným opačným
posunem Q (P0593); dopředné opakování v opačném pořadí tedy
vrátí tento původní pár. Konceptuálně vynulované Q jsou právě
výchozí Q dopředného algoritmu.

Jde o oboustrannou bijekci všech permutací s dvojicemi
(standardní P,přípustné Q). Jednoznačnost vstupu(e), jehož
existenci již ověřil P0590, tím skutečně plyne. Počítání
N!=T_λ∏H_ij je nyní důsledek bijekce, nikoli předpoklad důkazu.

Prázdný tvar má jediný prázdný pár a prázdnou permutaci.
Singleton má nulové Q a žádný přesun. U posledního sloupce,
posledního řádku a nulové cesty nebyl použit neexistující soused.
Aktivní horní hranice je podstatná v částech1,3 a5; její
vynechání v původním textu zůstává chybou C0020.

## 7. Realizace a náklady

Dopředný náklad je již přesně doložen v P0584; neopakuje se.
Kniha explicitní asymptotiku inverze Q neuvádí. Lze však
realizovat i výběr prvního kódu v O(N) čase na jeden krok:
v pásu řádků≥i se vytvoří rodiče max(horní,levý) s horní
hranicí i, označí se kandidáti a projde se podstrom u v pořadí
„podstrom D, vlastní kandidát Q, podstrom R“. To je přesně
lexikografické pořadí D<Q<R; řetězce kódů není třeba ukládat.
Strom má nejvýše N vrcholů a každá buňka nejvýše dva potomky.

N kroků s O(N) konstrukcí/průchodem, přesuny a posunem Q dá
O(N²) porovnání/aritmetických operací a O(N) pomocných buněk.
Nejde o tvrzení o bitové ceně libovolně velkých klíčů ani o
povinnost strom po každém kroku znovu stavět; je to doložená
horní mez konkrétní přímočaré implementace. Žádný program
nebo numerický průchod nebyl pro tento důkaz spuštěn.

