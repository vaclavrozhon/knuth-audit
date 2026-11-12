# §3.5-26–27,29–30: nulové korelace a odchylka sudých pozic

Stav1.11.2026. Původní zadání182 a odpovědi596–597 včetně obrázkuA-5
přečteny v sazbě. Všechny čtyři vrstvy errat a aktuální TeX zkontrolovány
podle stran, jmen a témat. Známé erratum23.9.2024 správně přeznačuje
páry v26 na(2n,2n+1), čímž odstraňuje nedefinovaný počáteční člen.
Oprava596 z29.6.1999 mění `. We` na `We` v odpovědi30, nikoli
Watermanovu konstrukci. Původní blok nepřidal potvrzený nález;
obnovovací revize6.11.2026 přidává C0250 v tištěné identitě29.
Úloha27 je auditována jako výzkumná otázka, ne jako vyřešený problém;
přesný rozsah a nedostupná konstrukce jsou v oddílu3.

Ekvidistribuce znamená správnou limitní četnost každého intervalu.
Nekonečná distribuce navíc požaduje správné společné četnosti všech
pevných konečných slov. Podle již dokázané větyC to platí i při pevném
kroku začátků oken. Pro ekvidistribuovanou [0,1) posloupnost znamená
**bělost** nulovou limitní korelaci pro každý pevný kladný posun k,
eboli průměr součinů (V_n−1/2)(V_(n+k)−1/2) konverguje k0.

## 1. Franklinova konstrukce26

Vezmeme po sobě jdoucí nepřekrývající se páry nekonečně distribuované
posloupnosti U. Každý pár(x,y) přeuspořádáme tak, aby ležel v oblasti

```
G = {(x,y): x−1/2<y<x nebo x+1/2<y} v jednotkovém čtverci.
```

Mimo několik hraničních úseček patří z bodů(x,y),(y,x) do G právě jeden.
Výsledný pár má proto limitní hustotu2 na G a0 jinde. Tento popis plyne
přímo z větyC a integrace Riemannovsky integrovatelných funkcí; nepotřebuje
pravděpodobnostně nezávislé původní členy. Každý konečný počet výstupních
párů má součinový zákon, protože původní odpovídající blok je rovnoměrný.
Hraniční množiny mají míru0 a správně i nulovou četnost.

Každý vodorovný i svislý řez G má délku1/2. Pro x<1/2 je svislý řez
(0,x) sjednoceno(x+1/2,1); pro x>=1/2 je(x−1/2,x). Vodorovné řezy
mají stejnou délku. Oba výstupní členy páru jsou tedy jednotlivě
rovnoměrné. Součin xy se při záměně nezmění, a proto

```
2*integral_G xy dx dy = integral_[0,1]^2 xy dx dy = 1/4.
```

Vnitřní korelace páru je0. Členy z různých párů mají součinový zákon
a rovněž nulovou korelaci. Pro každý pevný posun k se obě parity
začátku ošetří tímto argumentem a sloučí; V je ekvidistribuovaná a bílá.

Oblast G pod diagonálou má plochu3/8, takže uvnitř páru nastává sestup
s četností3/4. Přes hranici dvou párů je četnost1/2. Celkově
Pr(V_n>V_(n+1))=(3/4+1/2)/2=5/8. Výsledek26 je správný.
Franklinův původní článek nebyl dostupný (předchozí AMS403 a nedostupný
mirror v `sources/franklin-1963-deterministic.json`); tento oddíl je
úplný vlastní důkaz, nikoli tvrzení o přečtení jeho stran50–54.

## 2. Watermanova alternativa: libovolné dva vstupy

Odpověď596 bere libovolnou ekvidistribuovanou U a nekonečně distribuovanou
binární X. Pro n v bloku[j^2,(j+1)^2) položí
V_n=U_j při X_n=0 a V_n=1−U_j při X_n=1. Vzájemná nezávislost U a X
se nepředpokládá a nelze ji do důkazu přidat.

Položme Y_n=(−1)^X_n. Pro pevné H definujme průměr H po sobě jdoucích
členů z posloupnosti z, kde buď z_n=Y_n, nebo z_n=Y_nY_(n+k) pro pevné
k>0. Nekonečná distribuce X dává

```
lim_(N->infinity) (1/N)*sum_(n<N) ((1/H)*sum_(h<H) z_(n+h))^2 = 1/H.
```

Při rozvinutí čtverce jsou diagonální členy1. V každém smíšeném součinu
zbude některý binární symbol v liché mocnině, takže jeho průměr je0;
to platí i při překrývání dvojic se vzdáleností k.

Nechť a_n jsou libovolné reálné váhy, |a_n|<=B, konstantní na blocích
[j^2,(j+1)^2). Mohou záviset na celém X. Posun součtu o h změní jen
O(h*sqrt(N)) vah a O(h) krajních členů. Nahrazení z_n jeho H-průměrem
proto mění průměr váženého součtu o O_B(H/sqrt(N)). Cauchyho nerovnost
a předchozí identita dávají

```
limsup_N |(1/N)*sum_(n<N) a_n*z_n| <= B/sqrt(H).
```

Nejprve necháme N růst pro pevné H, potom H růst. Vážený průměr je0.
Jde o obecný důkaz pro všechny takové váhy, ne o neodůvodněný předpoklad
nezávislosti. Rozklad indikátoru každého binárního páru do kombinace
1,Y_n,Y_(n+1),Y_nY_(n+1) dává také vážené četnosti všech čtyř párů1/4.

Pro interval I lze indikátor V_n v I zapsat jako

```
(1_I(U_j)+1_I(1−U_j))/2
 + Y_n*(1_I(U_j)−1_I(1−U_j))/2.
```

Druhý člen má průměr0. První má průměr délky I: obyčejné Cesàrovy
průměry funkce U_j mají tuto limitu a sumace po částech zachovává limitu
při vahách2j+1, tedy délkách bloků. Poslední neúplný blok má jenO(sqrt(N))
členů. Tím je ekvidistribuce V dokázána. Případná hodnota1 vznikne jen
z U_j=0 a tvoří množinu hustoty0; je-li vyžadován doslovně obor[0,1),
lze ji nahradit0 bez změny všech zde uvedených limit.

Mimo O(k*sqrt(N)) začátků přes hranice bloků platí

```
(V_n−1/2)*(V_(n+k)−1/2) = (U_j−1/2)^2 * Y_n*Y_(n+k).
```

Vážený argument dokazuje bělost. Mimo bloky s U_j=1/2, které mají nulovou
váženou četnost, nastává V_n=V_(n+1) právě když X_n=X_(n+1). Četnost
rovností je1/2; vzestupy i sestupy mají četnost1/4. U vzestupů se
příslušný binární pár mění podle toho, zda U_j leží pod či nad1/2,
ale vážené četnosti dávají stále1/4.

Pro W_n=(V_n−epsilon_n) mod1 zvolme epsilon_n přísně klesající k0.
Přechody přes kraj0 mají nulovou hustotu podle ekvidistribuce V.
Mimo libovolně malé okolí U_j=1/2 se nenulové rozdíly V_(n+1)−V_n
od určitého místa zachovají ve znaménku. Rovnosti se díky přísnému
poklesu epsilon mění na vzestupy. Proto Pr(W_n<W_(n+1))=1/4+1/2=3/4.
Malá perturbace modulo1 zachovává ekvidistribuci i všechny korelace.

**Upřesnění jazyka, nikoli potvrzený nález:** pro tvrzení o ostrých
vzestupech zde čteme „decreases monotonically“ jako přísný pokles.
Pouhé nerostoucí epsilon by nestačilo: epsilon konstantní na čtvercových
blocích a klesající mezi nimi nechá hustotu1/2 rovností nezměněnou,
a vzestupů pak zůstane1/4. Výslovné „strictly decreasing“ by význam
zpřesnilo. Například epsilon_n=1/(n+2) bez potíží dává uvedenou konstrukci.

## 3. Výzkumná úloha27: co bylo a nebylo ověřeno

Watermanův příklad po odrazu dává vlastní dokázanou dolní mez3/4 pro
supremum četnosti sestupů bílých ekvidistribuovaných posloupností.
Jednoduchá vlastní horní mez je11/12. Pro d_n=V_n−V_(n+1) totiž
průměr d_n jde k0 (teleskopický součet) a průměr d_n^2 jde k1/6:
dva kvadratické momenty jsou1/3 a smíšený moment je1/4. Protože
|d_n|<=1, máme d_n^2<=|d_n| a

```
sum_(n<N) |d_n| = 2*sum_(n<N) max(−d_n,0) + O(1)
                <= 2*#{n<N: V_n<V_(n+1)} + O(1).
```

Dolní hustota vzestupů je alespoň1/12, a horní hustota sestupů nejvýše11/12.
Toto není důkaz optimální hodnoty ani tvrzení, že mez je ostrá.

Kniha přisuzuje Coppersmithovi lepší hodnotu7/8. Stejné oznámení je
v Knuthově primární zprávě Stanford CS-TR-73-392 (říjen1973), str.24
(strana26 souboru), s dodatkem „to appear“. Tato strana byla stažena,
vizuálně přečtena a uložena jako `sources/knuth-1973-errata-file26.pdf`.
[Primární autorský dokument](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/OCR/CS-TR-73-392-ocr.pdf).
Dokládá historii oznámení; neobsahuje konstrukci ani její důkaz.

Vymezené dotazy a metadata jsou v `sources/white-sequences-research.json`.
Nenašli jsme nezávislý primární důkaz7/8 ani aktuální úplné řešení.
To není důkaz, že úloha zůstává otevřená v roce2026. Konstrukci7/8
neoznačujeme za nezávisle prověřenou. Exploratorní jednoposunové LP
v témž souboru neřeší všechny korelace a má jen numerické výstupy,
proto se nepoužívá jako certifikát existence bílé posloupnosti.
Audit výzkumné formulace je dokončen v tomto výslovně omezeném rozsahu.

## 4. Úloha29: univerzální mez pro sudé pozice

Fixujme k>=1. Pro binární slovo x délky2k nechť r(x) je počet nul na
lichých místech slova a s(x) počet nul na sudých místech. Nu_x^E(N)
a nu_x^O(N) počítají výskyty začínající na sudé a liché pozici mezi1 a N;
nu_x je jejich součet. Nu_0^E počítá jednotlivé nuly na sudých místech.
Posun počítání ke každé z2k pozic slova mění jen O(k) krajních případů,
takže po sečtení

```
2k*nu_0^E(N)
 = sum_x [r(x)*nu_x^E(N)+s(x)*nu_x^O(N)] + O(k^2)
 = sum_x [s(x)*nu_x(N)+(r(x)−s(x))*nu_x^E(N)] + O(k^2).
```

Protože0<=nu_x^E<=nu_x a nu_x(N)/N jde k2^(−2k), je horní limita
levé strany dělené N nejvýše

```
k/2 + 2^(−2k)*sum_(r>s) (r−s)*binom(k,r)*binom(k,s)
    = k/2 + k*binom(2k−1,k)/2^(2k).
```

Identita pro poslední součet má krátký důkaz: rozdíl dvou počtů jedniček
v k bitech má stejné násobnosti jako počet jedniček ve2k bitech minus k.
Potom součet přejde na sum_(d=1)^k d*binom(2k,k+d). Rovnost

```
d*binom(2k,k+d)
 = k*(binom(2k−1,k+d−1)−binom(2k−1,k+d))
```

jej teleskopuje na k*binom(2k−1,k). Protože sudých pozic je N/2+O(1),
vychází přesně horní hustota ze zadání:

```
upper_Pr(X_(2n)=0) <= 1/2 + binom(2k−1,k)/2^(2k).
```

Doplňkové identity pro sumu max(r,s) a min(r,s) na596 plynou z
max/min=(r+s +/- |r−s|)/2 a téhož součtu. Jejich konstanty jsou správné.
**Oprava revize 6.11.2026:** původní zdejší závěr o správnosti všech
znamének neplatí. V hlavní tištěné identitě odpovědi29 chybí plus mezi
prvním a druhým členem. Vlastní důkaz výše má správný součet;
`C0250-parity-missing-plus.md` odděluje jeho platnost od chyby tisku.

## 5. Úloha30: obecná konstrukce a souvislost

Graf má vrcholy(E,w),(O,w), kde w je binární slovo délky2k−1.
Pro celé slovo x délky2k definujme
D(x)=x_1−x_2+...−x_(2k), f(x)=sign(D(x)). Hrana posune okno o jedno
místo a připojí poslední bit; z E do O má násobnost1+f(x), z O do E
násobnost1−f(x). Násobnosti jsou0,1,2.

Doplňování stejného bitu vlevo či vpravo mění znaménko D, protože
celková délka je sudá. Proto má každý vrchol stejný vstupní a výstupní
stupeň. Pro liché slovo w položme d(w)=w_1−w_2+...+w_(2k−1).
Vrchol E má nenulový stupeň právě když d>=0; O právě když d<=1.
To jsou přesně vynechané izolované vrcholy z odpovědi.

Zde je explicitní důkaz chybějícího „is seen to be connected“.
Z každého neizolovaného O lze připojit bit1 a přejít do E. Z každého
neizolovaného E lze připojit dvojici01: první krok vyžaduje d>=0;
po něm je nová hodnota d'=w_1−d<=1, takže druhý krok připojující1 je
povolen. Po k takových dvojicích je okno vždy101...1 a jsme ve vrcholu
(E,101...1). Každý neizolovaný vrchol tedy má cestu k tomuto středu.

Konečný orientovaný graf s vyrovnanými stupni a touto vlastností je
silně souvislý. Kdyby jeho rozklad do silně souvislých komponent měl
více vrcholů, existovala by zdrojová komponenta s výstupní hranou a bez
vstupní; součet vyrovnaných stupňů uvnitř ní to vylučuje. V grafu tedy
existuje uzavřený tah používající každou hranu právě jednou.

Celkový počet hran je2^(2k+1): každé slovo x má dohromady2 hrany v obou
paritách. Začneme v(E,00...0), prvních2k−1 bitů položíme rovno0 a další
bity čteme z tahu. Každé2k-slovo se v periodě objeví právě dvakrát,
takže periodická posloupnost je2k-distribuovaná.

**Pozor na indexy, nejde o chybu:** kniha výslovně začíná X_1, nikoli
X_0. První hrana označená E tedy odpovídá lichému začátku, O sudému.
Názvy vrcholů samy parity indexů neurčují. Pro skutečný sudý začátek
je násobnost1−sign(D)=1+sign(r−s), protože r−s=−D. Právě tehdy jsou
všechny výskyty slov s r>s na sudých a s r<s na lichých pozicích;
rovnost r=s nehraje roli. Konstrukce tudíž dosahuje rovnosti v každém
odhadu oddílu4. U k=2 vytištěná perioda
`00001000110010101001101110111110`, čtená od X_1, dává11/16 nul na
sudých indexech, jak uvádí597. Případné X_0 lze doplnit před periodu;
neovlivní žádnou limitu, ale posun celé fáze by převrátil paritní bias.

## 6. Konečné přesné kontroly

`verify_white_parity.py`, výstup `results/white-parity.json`:

- Symbolické integrály Franklinovy oblasti dávají oba první momenty1/2,
  druhé1/3, smíšený1/4 a sestupy5/8; oba typy řezů mají hmotnost1.
- Všech15300 binárních historií pro H=1,...,8 a posuny1,...,4 ověřuje
  přesný druhý moment1/H Watermanova průměrovacího jádra.
- Pro k=1,...,64 je přesně ověřena teleskopická kombinatorická identita.
  Grafy k=1,...,8 mají dohromady174760 hran. Kontrolovány všechny stupně,
  obě dosažitelnosti a explicitní cesty přes01. Nezávislé počítání slov
  ve výsledných Eulerových periodách ověřuje četnost2 každého slova
  a optimální paritní odchylku. Samostatně projde tištěný příklad k=2. Všech32 číslovaných hran
  obrázkuA-5 bylo jednotlivě vizuálně porovnáno s cestou tohoto slova
  a souhlasí; přepis hran je uložen ve výsledkovém JSON.

Všechny tři bloky prošly, běh11432 skončil0. Obecná tvrzení závisejí
na důkazech výše, nikoli na extrapolaci těchto konečných rozsahů.
