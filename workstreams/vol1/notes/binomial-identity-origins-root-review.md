# §1.2.6-25,31,33–34: původní důkazy a přesné odkazy

Kořenová revize 2. listopadu 2026, V1-X0710. Čtyři celé úlohy jsou
nově checked. Obecné matematické důkazy již byly přijaty v X0072;
nyní jsou uzavřeny konkrétní citované pasáže i křížové odkazy.
Nevznikl nový nález chyby. Nejde o tvrzení, že byly přečteny celé
stažené svazky nebo vyčerpány všechny možné starší zdroje.

Zmrazený balík `parallel/binomial-identity-origins/` má 86 souborů,
203809595 bajtů. Před převzetím root ověřil každý hash a délku;
SHA-256 manifestu je
`26631fe1605681878443f7c539700da8bc6cb54aab25400773c6b9c17309c8ee`.
Souhlasí také všech osm hashů textových vstupů čtyř vrstev errat
svazku I a čtyř vrstev svazku II. Úspěšné matematické programy
nebyly znovu spouštěny. Root přečetl všech pět odborných poznámek,
SOURCES a HANDOFF a níže uvedené původní obrazy.

## Rozsah přímé kořenové četby

| Pramen | Root přímo zobrazil a přečetl | Závěr |
|---|---|---|
| Gould 1956 | Původní s. 84–85, PDF 18–19 | Přesný citovaný důkaz úlohy 25 přes konečné diference a záměnu součtů |
| Pfaff | Titul, s. 37 a celý §11 na 51–52, PDF 5,53,67–68 | Původní věta a úplná indukce pro úlohu 31 |
| Vandermonde | S. 490–492, PDF 638–640 | Definice faktoriálových symbolů a §VI s konvolucí |
| Kramp | S. 347–348,358–359, kapitola PDF 2,3,13,14 | Definice mocnin s krokem, binomické koeficienty a formule §555 |
| Torelli | S. 179–180, PDF 198–199 | Formule (1) a její celý indukční důkaz |
| Rothe | S. 1–2 a detail 18, PDF 10,11,26 | Definice koeficientových znaků a přesný korolář B |
| TAOCP I | Odpovědi 485–486; §2.3.4.4-33 na 399 a 594 | Shoda čtyř odpovědí a konkrétní Lagrangeův odkaz |
| TAOCP II | §4.7-22 na 535 a odpověď 723 | Přesný implicitní koeficientový vzorec a zpětný odkaz |

Agent navíc přímo přečetl celý Gouldův článek 84–91, celý Torelliho
179–182, další úvodní a závěrečné strany a tituly. Přesný rozsah
této převzaté četby je v jeho HANDOFF; výše jej nevydáváme za
opakovanou vlastní četbu. Zdrojová metadata, URL a mapy stran jsou
v jeho SOURCES.json.

## Gould a oba odkazy úlohy 25

Označme C(a,k) zobecněný binomický koeficient, tedy padající součin
k činitelů dělený k!, pro celé k >= 0. Gould používá polynom
A_k(a,b) = C(a+b*k,k)*a/(a+b*k), kde odstranitelný podíl nejprve
zkrátíme. Jeho (5)–(6) na 84 a (7) na 85 dávají
`sum A_k(a,b) z^k = x^a`, kde `z=(x−1)/x^b`.
Dosazení a=r, b=−t a převod Gouldovy pomocné proměnné před (7)
na −w dávají právě odpověď 25. Výběr větve x blízké 1 je známá
oprava z 7. října 2013; nepřipisujeme jí nový nález.

Pro křížové odkazy nechť W je formální řada s nulovým konstantním
členem splňující W=z*(1+W)^(−t). Značka [z^n] znamená koeficient
u z^n. Pro n >= 1 platí

```text
[z^n](1+W)^r = (r/n)*C(r-t*n-1,n-1)
             = r/(r-t*n)*C(r-t*n,n).
```

Podíly opět mají polynomiální význam. §2.3.4.4-33 dává obecnou
Lagrangeovu koeficientovou formuli; aplikujeme ji na binomicky
rozvinutou řadu (1+W)^(−t). Netvrdíme, že exponenty e_i v tamním
stromovém zadání smějí být libovolná reálná čísla. §4.7-22 přesně
říká: je-li V=U(z*V^alpha), pak
`[z^n]V^r = r/(r+n*alpha)*[z^n]U^(r+n*alpha)`.
U=1+z a alpha=−t uzavírá druhý odkaz; odpověď 723 výslovně uvádí
zpětnou souvislost. Dřívější obecný důkaz pokrývá i analytickou
verzi v dostatečně malém okolí.

## Pfaffova formule a celý opravený obor

Definujme D_k(a)=a(a−1)...(a−k+1) a U_k(a)=a(a+1)...(a+k−1)
pro celé k >= 0; oba prázdné součiny jsou 1. Pfaffův §11 dokazuje
konečný součet

```text
sum_(k=0)^l D_k(l)*D_k(r)*D_k(m)
               / (k!*U_k(p)*D_k(l+r+m+p-1))
  = U_l(p+r)*U_l(p+m) / (U_l(p)*U_l(p+r+m)).
```

Pro knižní parametry R,S,M,N použijeme l=N, r=M−R+S,
m=−R−1, p=R−S+1. Poměr sousedních členů je přesně

```text
(M-R+S-k)*(N-k)*(R+k+1)
/ ((k+1)*(R-S+k+1)*(R+k+1-M-N)).
```

Root ověřil tento převod i zkrácení součinů na C(R,M)*C(S,N).
Při M,N >= 0 pokračujeme polynomiálně v R,S přes zdánlivé póly.
Pro N < 0 nebo M+N < 0 je celý součet nulový; pro −N <= M < 0
má výsledný součin nulový činitel U_N(M+1). Případ N=0 je
jednočlenný. To pokrývá „všechna celá m,n“ z opravy 2001.
Kompletní algebra i původní indukční krok jsou v agentově pfaff.md.

Titul a první strana rozlišují historický ročník 1793, tisk 1798
a předložení článku 14. ledna 1797. Knižní 1797 není tímto zjištěním
vyvráceno. Oprava začátku článku z 38 na 37 je již zveřejněná v 2023.

## Vandermonde, Kramp, Torelli a Rothe

Vandermondův §VI v ročníku 1772, vytištěném 1775, dává konvoluci
padajících mocnin. Jeho symbol [0]^(−k) je 1/k!, takže koeficienty
jsou obyčejné C(n,k). Záměna znamének dává rostoucí formu úlohy 33.
Pro pevné celé n >= 0 jde o polynomiální identitu; historická tvrzení
o necelých exponentech nejsou potřebná. Kramp v §555 na 359 dává
součet pro součiny F_n(a;r)=product_(j=0)^(n−1)(a+j*r).
Kroky r=−1 a r=+1 dávají obě knižní formy.

Torelliho (1) a důkaz na 179–180, s přejmenováním x,y a h=z,
dávají rostoucí formu úlohy 34. Volba h=0 zahrnuje i úlohu 33.
Rotheho koeficientový znak Q_j(v) znamená [u^j]Q(u)^v; dobový
index je posunut o 1. Jeho korolář B na 18 je

```text
sum_(k=0)^n f/(f+k*d)*Q_k(f+k*d)*Q_(n-k)(g-k*d) = Q_n(f+g).
```

Pro Q(u)=1+u, f=x, g=y, d=−z a po násobení n! dostaneme

```text
D_n(x+y) = sum_(k=0)^n C(n,k)*x*D_(k-1)(x-k*z-1)*D_(n-k)(y+k*z).
```

Vážený faktor pro k=0 má hodnotu 1 po odstranění podílu;
nezavádíme nedefinovaný součin se záporným počtem činitelů.
Posun −1 souhlasí se známou opravou z 14. července 1997.
Rotheho titul datuje disputaci 31. srpna 1793. Torelliho dopis
je datován dubnem 1895; obálka lednového/únorového prvního sešitu
není datací tohoto článku. Žádný z těchto rozdílů není nová chyba.

## Stav evidence

Relevantní již známé opravy všech čtyř vrstev jsou přesně rozepsány
v `notes/crossrefs-and-errata.md` zmrazeného balíku. Zahrnují také
Vandermondovu atribuci z 2005, polynomiální čtení z 2022 a pozdější
změnu pořadí činitelů. Starší root obrazové kontroly příslušných
errat zůstávají platné. X0084 je nadále partial pro ostatní
výslovně vyjmenované prameny; tyto čtyři úlohy již nezahrnuje.
