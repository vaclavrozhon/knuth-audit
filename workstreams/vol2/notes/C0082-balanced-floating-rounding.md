# V2-C0082: význam „rounding“ ve vyvážené trojkové soustavě

**Candidate, nikoli confirmed.** §4.2.1-7, odpověď612; kontext
nejlepší plovoucí aproximace na231. Sazba všech těchto míst přečtena
vizuálně. Kniha doporučuje normalizovat do1/6<|f|<1/2 a uvádí,
že zaokrouhlení kromě dělení odpovídá odříznutí cifer.

To je správné pro zaokrouhlení zlomku v pevné poloze řádové čárky,
ale obecně nikoli pro nejlepší hodnotu v celé plovoucí soustavě.
Pro p=2,q=0 jsou u=2/9 a v=−4/81 normalizované vstupy:

```text
u=(0, .1[-1])_3,
v=(−2, .[-1][-1])_3,
u+v=14/81=.1[-1][-1][-1]_3.
```

Přesný součet je v[1/6,1/2), takže tištěná normalizace nemění
exponent. Odříznutí na dvě cifry dává2/9 s chybou4/81.
Reprezentovatelný normalizovaný soused s exponentem−1 je
`.11_3/3=4/27` a má chybu2/81. Obě hodnoty jsou bezprostřední
sousedé v celé kladné dvouciferné soustavě; obecně jsou její
zlomky2/9,3/9,4/9 krát libovolná mocnina3.

Přesný protipříklad vyvrací výklad „odříznutí vždy poskytne
nejbližší plovoucí číslo“. **Nevyvrací** výklad, že se nejprve
zvolí exponent podle uvedené normalizace a potom se nejlépe
zaokrouhlí pouze zlomek. Proto je zatím vhodný redakční dotaz,
nikoli tvrzení o jednoznačně chybné větě. Samotný požadavek p+1
míst akumulátoru a normalizační rozmezí konečných zlomků zůstávají
platné v tomto druhém výkladu.

Všechny čtyři vrstvy errat a aktuální TeX prohledány2.11.2026
podle612, úlohy7 a souvisejících slov; změna nenalezena. Ověření
v novém fyzickém dotisku ani prvenství nemáme. Reprodukce:
`verify_single_precision.py`, blok balanced_and_auxiliary.

Obnova X0202: [celá7](recovery-floating-balanced-2026-11-06.md)
doplňuje každou mez, úplný p+1 akumulátor a důkaz pořadí kódu.
Kandidát se nemění; úloha zůstává partial v rozsahu významu
zaokrouhlení a nedourčených půlek dělení. Archivní běh neopakován.
