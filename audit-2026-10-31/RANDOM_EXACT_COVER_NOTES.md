# Náhodné exact cover úlohy — 7.2.2.1–39

Kontrola 1. listopadu 2026. Zadání je na str. 127, odpověď na str. 423–424.
PDF: první vydání, druhý dotisk 2022. Autorův PostScript `fasc5c` má odpověď
na str. 127–128. Původní stránky byly vykresleny a vizuálně zkontrolovány.

## F110: vzorec v části (b) počítá jinou veličinu

Zadání výslovně dovoluje opakované možnosti. Řešením je výběr **indexů řádků**;
str. 126, úloha 32, jej výslovně zapisuje jako binární vektor délky M.
Stejnou konvenci používá pravděpodobnostní výpočet v odpovědi 39(a)
i skutečný Algorithm X. Na str. 424 se však počítá počet různých rozkladů
množiny položek, bez násobnosti stejných řádků.

Malý příklad má položky a,b a tři nezávislé možnosti velikosti jedna.
Každá je a nebo b s pravděpodobností 1/2. Z osmi stejně pravděpodobných vstupů
jsou aaa a bbb neřešitelné; ostatních šest má po dvou řešeních, protože lze
vybrat jeden ze dvou stejných řádků. Střední počet řešení je tedy **3/2**.
Pravděpodobnost, že se vyskytly oba typy, je pouze **3/4**. Pro konkrétní
vstup a,a,b jsou řešení 101 a 011.

Protipříklad lze ponechat i v přesných parametrech knihy: rozdělme sto položek
na dvacet disjunktních pětic. První pětici zopakujme 481krát a ostatních
devatenáct použijme jednou. Tento možný výsledek 500 nezávislých tahů má
**481 řešení**, ale jediný rozklad položek. Původní nezměněný DLX1 potvrdil
oba počty, 2 a 481. Pro malý vstup souhlasí také doslovný překlad Algorithm X
a nezávislý výčet podmnožin řádků.

### Opravená střední hodnota

Předpokládejme n=kr, r≥1, N=binom(n,r) a
P=n!/(k! (r!)^k). Pro každý pevný rozklad do k bloků má každý indexový výběr
k možností pravděpodobnost k!/N^k, že obsahuje právě tyto bloky.
Linearita střední hodnoty proto dává

\[
\mathbb E Z=P\frac{(m)_k}{N^k}
=\binom mk\frac{n!}{(r!)^kN^k}.
\]

Při m<k je výsledek nula; při r nedělícím n řešení neexistuje.
Stejný důkaz lze formulovat pomocí násobností bloků: jeden rozklad přispívá
součinem jejich četností, nikoli indikátorem, že všechny četnosti jsou kladné.

Oba vytištěné výrazy pro g jsou samy správně:

\[
g(N,m,k)=\frac{1}{N^m}\sum_{j=0}^k(-1)^j\binom kj(N-j)^m
=\frac{1}{N^m}\sum_{t=k}^{\min(m,N)}
 {m\brace t}\,t!\binom{N-k}{t-k}.
\]

První je inkluze–exkluze chybějících typů. Ve druhém se vybere t−k dalších
typů a surjekce m označených tahů na všech t typů. **P g** je správná střední
hodnota počtu geometricky různých rozkladů; nepočítá obecně řešení Algorithm X.
Pro výběr bez opakování je správná pravděpodobnost
binom(N−k,m−k)/binom(N,m)=(m)_k/(N)_k. Ani ta se nemá zaměňovat
s modelem s opakováním.

| m, při n=100 a r=5 | Řešení podle indexů | Geometrické rozklady P g |
|---:|---:|---:|
| 500 | 0,00000189659343588 | 0,00000189647252137 |
| 1000 | 2,41399681506 | 2,41368261152 |
| 1500 | 8557,93320792 | 8556,25105975 |

Pro knižní velké N=75 287 520 je relativní rozdíl jen asi 0,0064–0,0197 %.
Hrubé číselné odhady knihy a její kvalitativní srovnání tím prakticky zůstávají.
Nález se týká přesného vzorce a jeho odůvodnění, ne tvrzení, že tyto příklady
mění obtížnost úloh o velký faktor.

## Část (a): odmítání prázdných řádků je podstatné

Pro k označených řádků znamená pokrytí každé položky právě jednou funkci
z n položek do k řádků. Nepřítomnost prázdného řádku požaduje surjekci,
tedy k! {n brace k} možností. Každá má pravděpodobnost
p^n(1−p)^{n(k−1)}. Po podmínění neprázdností všech k nezávislých řádků
se dělí [1−(1−p)^n]^k. Součet přes binom(m,k) výběrů dává přesně
knižní vzorec. Pro n≥1 stačí 1≤k≤min(m,n).

Pro m=500, n=100, p=1/20 vychází správně **297,0406839427…**.
Nesprávný výpočet bez podmínění dává **3736,9637245343…**.
Obě vytištěná zaokrouhlení jsou správná. Pravděpodobnost odmítnutí
prázdného řádku je (1−p)^n; nezávislé opakování losování zachovává
nezávislost přijatých řádků.

## Rozsah ověření a zbývající mezera

`check_random_exact_cover.py` používá přesné zlomky. Úplně vyčíslil
2927 vstupních matic Bernoulliho modelu pro dvě racionální pravděpodobnosti
a 13 905 matic uniformního modelu, vždy včetně opakovaných řádků.
Ověřil jak počet indexových řešení, tak počet geometrických rozkladů,
oba vzorce pro g a opravený vzorec střední hodnoty.

Dvacet dalších reprodukovatelných pokusů na 12 položkách a 36 možnostech
ověřilo shodu původního DLX1 s nezávislým dynamickým programem.
Výsledky, vstupy, semena a kontrolní součty jsou v `results/random_exact_cover/`.

**Celá úloha zatím zůstává partial.** Nemáme původní semena a přesný generátor
deseti knižních pokusů ani reprodukci jejich přibližně 100 megamemů na řešení.
Nezaměňujeme vlastní jiné pokusy za reprodukci těchto historických čísel.
Zmíněné nepublikované asymptotické poznámky Pemantla a Pittela také nemáme.

Aktuální i historická errata 4B/F5 byla prohledána podle stran i obsahu;
žádná odpovídající oprava F110 nebyla nalezena. Hashově ověřené stažení
oficiálních souborů z 18:17 UTC je evidováno v navázaném záznamu.
Stejné znění je v PDF i původním PS. Fyzický exemplář není ověřen.
