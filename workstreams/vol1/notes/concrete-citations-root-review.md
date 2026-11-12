# Concrete Mathematics: citace z §1.2.7 a §1.2.11.2

X0689, 2. listopadu 2026. Ověřen obsah obou konkrétních odkazů:
§6.5 obsahuje odvození sudých hodnot zeta pomocí Bernoulliho čísel;
§9.5 obsahuje Eulerův sumační vzorec, integrální zbytek i jeho
odhad. To uzavírá tyto dvě citační mezery, nikoli audit celé
pomocné knihy nebo všechny historické atribuce v jejím výkladu.

## Prameny a skutečný rozsah četby

Již uložený `sources/permutation-remaining/concrete-mathematics.pdf`
má 639 stran a hash začínající `7ec19c0777491146`. Přímo přečtený
titul, předmluva ix (květen 1988) a obsah xiii identifikují starší
sazbu odpovídající prvnímu vydání. §6.5 začíná na 269 a §9.5 na
455; chybí nová §5.8 druhého vydání. Tiráž a přesný dotisk nebyly
doloženy. Datum vytvoření PDF není datem vydání knihy. Soubor se
neztotožňuje s druhým vydáním 1994 jen podle obecného katalogu.

[Autorova stránka](https://www-cs-faculty.stanford.edu/~knuth/gkp.html)
výslovně identifikuje druhé vydání a odkazuje na
[náhradní strany pro 34. dotisk, leden 2022](https://www-cs-faculty.stanford.edu/~knuth/gkp34.pdf).
Ty byly nově získány přímo ze Stanfordu. Obsahují celé relevantní
§§6.5 a 9.5 v novější konvenci. Nejde o úplný sken druhého vydání
1994 a takový rozsah se netvrdí.

Root přímo obrazově přečetl:

- TAOCP 76 a 114 s oběma odkazy a požadovanými vzorci;
- starší CMath: titul, ix, xiii, 272, část 455 od začátku §9.5,
  457 a odpověď 6.73 na 535;
- náhradní strany: 283–286, úlohu 6.73 na 317, 365–367,
  začátek 368 po (7.81), celou §9.5 na 469–475.

Z původního OCR byly navíc čteny 269–273 a 455–460. Zbylé
vykreslené obrazy nejsou pouhým vytvořením považovány za přečtené.
Manifest rozlišuje soubory, závislosti a přímo čtené obrazy.

## Bernoulliho čísla a hodnoty zeta

Značíme `zeta(s)=sum_{k>=1} k^(-s)` pro reálné s>1.
Současná Bernoulliho čísla B_j jsou definována generující funkcí
`F(z)=z/(1-exp(-z))=sum B_j z^j/j!` v okolí nuly.
Rekurence (6.79), odvození na 365 a tabulka 284 dávají B_1=1/2.
Starší konvence používá `z/(exp(z)-1)` a B_1=-1/2; sudé
koeficienty jsou stejné. Polynomy P_m(x) jsou definovány
`z exp(xz)/(exp(z)-1)=sum P_m(x) z^m/m!`.
Jsou totožné s knižními B_m(x), ale písmeno P zde brání záměně
čísla B_m a hodnoty polynomu P_m(0).

Strany 285–286 nejprve odečtou z/2 od F(z), čímž vznikne sudá
funkce `(z/2)coth(z/2)`. Po dosazení imaginárního argumentu
(i je odmocnina z -1) dostanou mocninný rozvoj z cot z. Druhé
vyjádření je rozklad

```text
z cot z = 1 - 2 sum_{k>=1} z^2/(k^2 pi^2-z^2).         (C1)
```

Shoda koeficientů z^(2n) dává přesně

```text
zeta(2n) = (-1)^(n-1) (2pi)^(2n) B_(2n)/(2(2n)!), n>=1. (C2)
```

To je TAOCP (6) na 76, protože kladnost levé strany určuje
znaménko B_(2n). Dosazení čtyř hodnot B_2 až B_8 dává (7).
Porovnání koeficientů je analyticky oprávněno pro |z|<pi:
dvojitá geometrická řada v (C1) absolutně konverguje. Samotný
rozklad (C1) plyne také z již přijatého sinusového součinu
v `gamma-functions.md` lokálně stejnoměrným logaritmickým
derivováním. Nové čtení nenahrazuje tento důkaz konečným testem.

CMath úloha 6.73 odvozuje (C1) konečným rozkladem kotangentu
na argumenty dělené 2^n a limitou. Přečtená starší odpověď 535
zdůvodňuje konečnou identitu a bodové limity; oprávnění přechodu
pod součet pouze uvádí. Tato míra podrobnosti je zaznamenána,
nepřipisujeme odpovědi neuvedený důkaz stejnoměrnosti. Naše
ověření konvergence používá výše uvedený vlastní důkaz.
Obecná historická atribuce (C2) Eulerovi se tím ještě neuzavírá:
citace moderního důkazu není původní Eulerův článek.

## Eulerův vzorec a zbytek

Nechť a<=b jsou celá čísla a f má potřebné spojité derivace.
Zlomková část je `{x}=x-floor(x)`. Integrální zbytek řádu m je

```text
R_m = (-1)^(m+1)/m! integral_a^b P_m({x}) f^(m)(x) dx.  (C3)
```

CMath (9.67) s B_1=+1/2 sčítá a<k<=b. Současná TAOCP (10)
sčítá a<=k<=b, a má proto navíc f(a). Původní zápis s B_1=-1/2
sčítá a<=k<b. Ve všech případech jsou vyšší členy i (C3) stejné.
Přímé odvození přes integraci po částech na jednotkovém intervalu,
P'_m=m P_(m-1) a P_m(1)=P_m(0) pro m>1 souhlasí s již dokázanými
(E3)–(E6) v `euler-summation.md`. Formální manipulace s operátory
na 470–471 je v prameni výslovně oddělena od tohoto důkazu.

Strana 474 dokládá maximum `|P_(2m)(x)|<=|B_(2m)|` na [0,1]
a pomocí (C2) odhad koeficientu řádu `(2pi)^(-2m)`. To je přesně
citovaný kontext TAOCP (12). Na 475 následuje odhad zbytku posledním
ponechaným členem a, při stejném znaménku příslušných vyšších
derivací, prvním vynechaným členem. Znaménkový argument lze psát
přesně: na každém jednotkovém intervalu spárujeme t a 1-t pro
0<t<1/2. Lichý polynom má opačné hodnoty v páru a derivace
f^(2m+1) je neklesající, takže každý spárovaný integrand má
po vynásobení (-1)^m nezáporné znaménko. Totéž o řád výše
ukazuje opačná znaménka R_(2m) a R_(2m+2). Jejich rozdíl je
první vynechaný člen, což dává faktor theta mezi 0 a 1.

TAOCP požaduje ostře kladný součin obou vyšších derivací uvnitř
intervalu, proto její ostrá varianta 0<theta<1 není v rozporu
s neostrou variantou CMath. Plný argument včetně možnosti
záporných derivací a a=b je již v (E10)–(E11) tamtéž.
Úspěšné dřívější matematické programy nebyly znovu spuštěny.

## Meze a vedlejší textová odchylka

Byly znovu vyhledány relevantní bloky všech čtyř vrstev errat
TAOCP; uložený výřez obsahuje 11 záznamů. Zachovává známý přechod
konvence 2021, opravu absolutní hodnoty 2013 a nenulového členu
2024. Žádná zdejší kontrola nepřidává chybu svazku 1.

Na náhradní straně CMath 471 je drobná odchylka v pokynu k posunu:
uvedeno je f(x+l), ale následuje integrál od l-1 do l a levá
strana f(l). Ty odpovídají dosazení f(x+l-1) do identity na [0,1].
Samotná zobrazená identita je správná. Starší strana 457 má
f(x+l) s intervalem [l,l+1], což spolu souhlasí. Záznam slouží
k přesnému popisu přečteného důkazu; není započten mezi nálezy
TAOCP, není odeslán a netvrdí ověření všech vydání CMath.
Historické formulace CMath o roku vydání a prvenství nejsou
nahrazením již oddělené kontroly Eulerových originálů.

X0091 a X0135 zůstávají partial pro své ostatní konkrétní prameny.
Počty hotových úloh se touto kontrolou dvou citací nemění.
