# Souvislá revize §3.3.2 J a úloh 26–30 — 6. listopadu 2026

Revidována původní sazba třetího vydání, prvního tisku: 71–72, zadání
78–79 a odpovědi 566–570. Stránka souboru je tištěná +12. Celé stránky
71, 567–569 jsou po spojení s předchozím blokem vypořádané. Strany 72,
78–79, 566 a 570 zůstávají částečné z níže uvedených důvodů.

Přezkoumány staré důkazy, čtyři programy, jejich výsledky i dokončovací
logy; žádný starý výpočet znovu spuštěn. Přijaté artefakty a jejich otisky
jsou v `results/sequential-spacings-review.json`. Trojúhelníkový obrázek
567 byl porovnán s rekonstrukcí včetně všech 36 dvouciferných popisků.
Pět stran uloženého článku Marsaglia–Zaman–Tsang bylo nově vykresleno
a celé vizuálně přečteno pro zdrojový kontext; nejde o audit ostatního
Fortranu a tvrzení o periodách v tomto článku.

## Spojité mezery a transformace

Pro pořadové statistiky n nezávislých rovnoměrných bodů má původní
označení S_i=U_(i+1)−U_(i), S_n=U_(1)+1−U_(n) hustotu n! S_n
v prvních n−1 souřadnicích. Poslední mezera obsahuje pevný počátek,
a proto je zvýhodněna délkou. Pro nezáporné prahy se součtem T≤1
je společná pravděpodobnost překročení

    (1−T)^(n−1) (1−T+n s_n).

Záporné prahy je nejprve nutno nahradit nulou. Pro n=2 dává
S_1=|U_1−U_2| pravděpodobnost 1/4 nad prahem 1/2, nikoli 1/2.
**C0018 potvrzen:** neplatí společné rozdělení v 26(a) ani tvrzení
27 o zachování původního označeného rozdělení. Oprava je označovat
od vybraného pozorování, například U_1, nebo náhodně cyklicky otočit.

Seřazené mezery jsou přesto správné: pro symetrickou funkci g je
n E[S_n g]=E[(Σ S_i)g]=E[g] pod rovnoměrnou simplexovou mírou.
Konstrukce pomocí nezávislých exponenciálních E_i dává E_i/ΣE_i
s rovnoměrným simplexovým rozdělením a nezávislým součtem.
Pro seřazené exponenciální hodnoty jsou
Z_j=(n−j+1)(E_(j)−E_(j−1)) opět nezávislé exponenciální:
Jacobián 1/n! ruší faktor n! a součty se rovnají. Odtud plyne
správnost transformovaných mezer a všech seřazených distribucí.

Inkluze a exkluze dává pro počet j mezer nejvýše s

    G_j(s)=binom(n,j) Σ_(l=0)^j binom(j,l)(−1)^(j−l)
                         (1−(n−l)s)_+^(n−1).

Je tedy 1−F_k=G_0+…+G_(k−1). **C0022 potvrzen:** mezilehlý
součet na 566 vynechává G_0; n=2,k=2,s=1/4 dává 1 oproti 1/2.
Výsledný zobrazený vzorec i momenty jsou správné. S označením
h=Σ_(j≤k)1/(n−j+1), h2=Σ_(j≤k)1/(n−j+1)^2 vycházejí
E S_(k)=h/n a Var S_(k)=(h2−h²/n)/(n(n+1)). Beta integrály
a uložených 464 momentových dvojic/2320 hodnot distribuční funkce
jsou v souladu. Hustota součtu n rovnoměrných veličin souhlasí
s x^(n−1) F_n(1/x)/(n−1)!; další kontrolou je inkluze a exkluze krychle.

Inverzní větev geometrického zobrazení má
s_(j)=Σ_(i≤j)y_i/(n−i+1), sloupcové součty 1, determinant 1/n!
a příslušné pořadové permutace. Vzdálenost vrcholů je
sqrt(|1/j−1/k|), vzdálenost cílových vrcholů sqrt(2). Každé dva
sloupce mají společnou hmotnost alespoň 1/n; kontrakce v L1 je
nejvýše 1−1/n. Každé nekonečné slovo proto určuje jediný bod.
Opačný směr potřebuje vyloučit hranice nebo určit pravidlo shody.

**C0023 potvrzen:** a=sqrt(2)/4 a bod (a/3,5a/6,1−7a/6)
mají různé kladné iracionální souřadnice, ale další obraz je
(a,a,1−2a). Striktní pořadí neplatí; uzavřené oblasti připouštějí
druhé číslice 4 i 5. Výjimečná množina je nulové míry, obsahuje
však i iracionální body. Uložená rekonstrukce 258 buněk a 366
společných hran potvrzuje sousednost kódů i obrázek knihy.

Částečné součty transformovaných mezer mají rozdělení pořadových
statistik n−1 rovnoměrných bodů, takže KS normalizace sqrt(n−1)
na 79 je správná. Iterace nejsou navzájem nezávislé. Pro n=2 jde
o stanové zobrazení 2 min(x,1−x); dyadické jmenovatele klesají,
a po dosažení 1/2 následují 1 a 0. Uložených 32780 případů
a 16 Grayových kódů sedí. Pro obecné n je konečná implementace
nakonec periodická; samo o sobě to nedokazuje překročení každého
KS prahu. Kniha tvrzení o konečném dosažení vrcholu omezuje na n=2;
pevný bod (3/8,1/2,1/8) pro n=3 není protipříklad k tomuto tvrzení.

## Narozeninový test, přesné počty a certifikát

Označme R=n−počet různých délek kruhových mezer a s počet nulových
mezer. Je q_n(m)=p_n(m−N), N=n(n+1)/2. Ukotvení první označené
osoby dává m rotací, (n−1)! pořadí ostatních osob a n!/Πm_i!
pořadí délek. Proto b_(n,0,0)=m n!(n−1)! q_n(m). Sloučení osob
se stejnými narozeninami dává pro s>0

    b_(n,r,s)={n brace n−s} b_(n−s,r+1−s,0).

**C0024 potvrzen:** pravděpodobnosti případů s=0 a s=1 pro R=0
se musí sečíst. V 28(c) má být plus před
(1/2)p_(n−1)(m−binom(n,2)). Pro n=2,m=3 má všech devět slov
R=0, ale vytištěné minus dává 1/3. Číslo v tabulce na 71 už je
správné: .367360956321390903874224 + .00144062077652998641163531.

Generující funkce pro r=0,1,2 byly odvozeny přímo z bloků stejných
délek. Pro obecný binární vzor rovností b_k určují
c_0=1, c_k=1+b_k c_(k−1) násobnosti, Πc_k=Πm_i!. Čitatel má
exponent N−Σ(n−k)b_k, faktor Π_(b_k=1)(1−z^(n−k)) a dělitel Πc_k.
Součet přes všechny vzory dává generující funkci kladných kompozic,
jak požaduje speciální případ w=1. Uložený nezávislý výčet 219456
slov, 292022 seřazených rozkladů, 2160 koeficientů a 24 zjednodušených
čitatelů souhlasí. Obecné důkazy nejsou nahrazeny jen těmito výčty.

Přezkoumán celý racionální certifikát pro F_n(z)=Π_(j=1)^n(1−z^j)^−1.
Pól v 1 dává polynom

    P_n(M)=(1/n!) [t^(n−1)] exp(a t) H_n(t), a=M+N/2,
    H_n(t)=Π (jt/2)/sinh(jt/2).

Koeficient log H u t^(2j) je −B_(2j)Σk^(2j)/(2j(2j)!). Rekurence
pro koeficienty H a přesný Hornerův výpočet s A=2M+N jsou správné.
Pro H(iu) jsou koeficienty nezáporné podle Eulerova součinu sinu.
Při r=8n/a_lo, nr/2≤1, je log H(ir) omezeno
S2 r²/[24(1−n²r²/24)]≤1/2; H(ir)<2 a zbytek od L je nejvýše
2 a_hi^(n−1)/64^L. Použito L=24 nebo celý malý polynom.

Pro primitivní pól řádu d položme p=floor(n/d), rho=p/M,
M≥4n². Ostatní kořeny mají vzdálenost alespoň 4/(dn) a
rho≤1/(4nd). Násobky d dávají |1−z^j|≥j rho/2; ostatní
faktory jsou alespoň poloviční oproti hodnotě v kořenu. Úplný blok
má součin d, neúplný je ≥exp(−d/2)>3^(−d). Integrál rezidua je
proto nejvýše

    B_d=2^n 3^(d+2p+1) (M/p)^(p−1)/(d^(2p) p!).

Součet d B_d pokrývá všechny netriviální póly. Nezávislá Laurentova
expanze u 1 a dynamické počítání pro 76 malých modelů potvrzují
normalizaci i intervalové meze. V kódu jsou čtyři příznaky správného
zaokrouhlení pouze vypočtené, nikoli assertované; v uloženém výsledku
jsou všechny true a byly samostatně přečteny.

Certifikované pravděpodobnosti pro n=512,m=2^25:

| R | Hodnota | Absolutní chyba nejvýše |
|---|---|---|
| 0 | .368801577097920890285859 | 2.445e−43 |
| 1 | .369035243450689819080441 | 1.250e−40 |
| 2 | .183471182131179017765623 | 2.388e−38 |
| ≥3 | .0786919973202102728680761 | 2.401e−38 |

Všechny devítimístné údaje tabulky sedí. Též
q/10^1514=7.0806934695902640946216551145491358: všech 19 cifer
uvedeného prefixu je správně. Tříčlenná aproximace začíná
7.0806935013461898 a správně se zaokrouhluje na 7.080693501.

Pro m=n³/alpha, pevné alpha>0, koeficienty
h1=−S2/24 a h2=S2²/1152+S4/2880 reprodukují všechny hlavní
členy knižní asymptotiky. Odhad vyššího ocasu s poloměrem
sqrt(n)n/a dává O(n^−3); ostatní póly jsou relativně
exp(O(n)) n^(p−n), zanedbatelné vůči libovolné pevné mocnině.
Přechod na q odpovídá alpha→−alpha. Konečné diference pevného
řádu a posuny O(n) dávají Poissonovu limitu s lambda=n³/(4m).
Střední hodnota byla ověřena zvlášť: shoda jedné dvojice mezer
má pravděpodobnost (n−1)/(2(m−1))+O(n²/m²), trojice O(n²/m²);
rozdíl mezi počtem párů a R pokryjí trojice. Výsledkem je
lambda+O(1/n). Případy nulových mezer přidávají O(1/n).

Na 570 se bn00/m^n zapisuje jako pravděpodobnost R=0 bez bn01.
Následující věta výslovně uvádí zanedbaný případ a jeho řád 1/n;
v asymptotickém odstavci to neevidujeme jako další nezávislou chybu.

## Pomocné chyby v odpovědi 30

Hlavní asymptotické výsledky jsou správné, ale potvrzeny jsou:

- **C0025, původní 569:** v Eulerově derivaci j! místo (j−1)!
  a opačné znaménko regulárního Bernoulliho součtu. Pro n=1,j=2
  je správně rho^−2−1/12+rho²/240+…, vytištěno
  2rho^−2+1/12−rho²/240+…. Při rho=1 je skutečná hodnota
  A=1/[4sinh²(1/2)]<1, chybný konvergentní výraz 3−A>2.
- **C0026, pouze erratum 7. 1. 2004:** změna j≥8 na j≥3 pro
  c_j=O(n^−3) je chybná. c3=1/(3sqrt(n))+O(n^−9/2).
  Původní práh 8 je pro každé pevné j v souladu s vedoucím členem
  1/[j n^(j/2−1)]. UI mapuje původní 569 jen jako související.
- **C0027, původní 569:** reciproční identita vyžaduje
  q_n(m)=(−1)^(n−1)p_n(−m), m>0, při kvazipolynomiálním
  pokračování p. Pro n=2,m=3 je q=1 a p_2(−3)=−1.
- **C0028, původní 569:** nahrazení f(z) výrazem f(z)+N log z
  zvyšuje c1 přesně o N delta=alpha(n^−1/2+n^−3/2)/2.
  Uvedený alpha(n^1/2−n^−1/2)/2 nesedí; pro n=2,m=8
  jde o 3sqrt(2)/8 oproti sqrt(2)/4. Konstantní faktor a finální
  asymptotika zůstávají správné.

## Generátory a hranice reprodukce

Identita lagged-Fibonacci 55/24 na 72 má skutečně kongruenční
znaménka. Obě strany se redukují na
X_(n−24)+X_(n−55)+X_(n−86) modulo m. Při sousednosti příslušných
narozenin tak vzniknou stejné kruhové mezery. Výběr každého druhého
členu odstraní tento konkrétní čtyřindexový mechanismus, nikoli
všechny možné statistické vady nebo všechna špatná semena.

Přezkoumán stavový posun i index i+31 v původním programu, tři
55slovná semena ze SHAKE256, podmínka lichého členu, stride 2
i konstrukce kruhových mezer. Přijaty dokončené výsledky po 2000
pokusech, nikoli znovu spuštěny. Průměry pro stride 1 jsou
2.587/2.657/2.574 oproti .9515/1.0125/.957 pro stride 2 a .979
referenční sekvence. Uvedené extrémní chvosty chi-kvadrátu jsou
asymptotické, nikoli přesné pravděpodobnosti konečného experimentu.
Reference je deterministická SHAKE sekvence, nikoli důkaz nezávislosti.

Původní semena a přesné pravidlo knižního R′ nejsou doložené.
Kvalitativní závěr podporují vlastní data i primární článek, ale
strana 72 **zůstává partial**. Tato mezera není bibliografická výjimka.

## Errata a dostupná bibliografie

Všechny čtyři vrstvy errat čerstvě staženy 6. listopadu 2026 a
porovnány s uloženými soubory; manifest v `sources/sequential-2026-11-06/`.
Relevantní úplný výpis je `empirical-tests-errata.json` v téže složce.
Opravy 569 z let 1999/2004/2021 byly zkontrolovány i obrazově.
Změny roku 2021 vyjadřují globální konvenci B1=+1/2: (−k)^l,
log((e^z−1)/z), −N B1. Nejde o nezávislé početní chyby.
Známé opravy jsou 72: svazek časopisu 8→9; 566: Whitworthův
odkaz; 569: c^3→c3; 570: 1093→1953. Změna prahu j≥3 je naopak
samostatná chyba errata C0026. Další opravy C0018/C0022–C0028
v žádné vrstvě nenalezeny; poslední fyzický dotisk ani prvenství
nálezů nejsou ověřeny.

Přečteny uložené primární bibliografické podklady:

- Barton–David 1956: metadata vydavatele. Pyke 1965: článek
  395–436 a diskuse 437–449 vysvětlují správný knižní rozsah 395–449.
- Durbin: metadata 41–65 se rozcházejí s autorovou pozdější opravou
  41–55 a další položkou od 57. Knižní rozsah ponechán, nikoli
  automaticky „opraven“ podle metadat.
- Sukhatme 1937: institucionální metadata. Daniels 1962: metadata,
  abstrakt a dostupný výňatek; celé znění neověřeno.
- Szekeres: metadata obou článků potvrzují rok 1953 v opravě 570.
  Pólya: vydavatel uvádí 1929 a přijetí 1928, kniha 1928;
  přesné datování původního svazku neověřeno, bez nového nálezu.
- Marsaglia–Zaman–Tsang: všech pět stran 35–39 nově vizuálně.
  První záhlaví má 8, další čtyři Volume 9, Number 1; i samotný
  primární otisk vysvětluje opravu citace. Test má **lineární** mezery,
  nikoli kruhové. Tabulka používá 512 narozenin v 2^25 dnech,
  100 pokusů a odčítací generátory 97/33 a 55/24. Výsledky
  podporují kvalitativní selhání, nejsou rekonstrukcí Knuthova
  konkrétního experimentu. Rok 1984 u jiné citace v knize označuje
  konferenci, zatímco sborník vyšel 1986; není tím doložena chyba.

Výslovně přeskočeno: plné znění de Finettiho 1964, Danielsova článku,
Whitworthovy Proposition LVI a historické atribuce, de Bruijnova
kapitola 5, přesný rok původního Pólyova svazku. Bibliografické
výjimky nevydáváme za ověřený obsah.

Další kurzor: zbytek empirických testů L/M na 73–75 a úlohy 31–35
na 79–80 s odpověďmi 570–572. Úloha 25 na 78/566 dál vyžaduje
obecné vysvětlení; potvrzené numerické poměry ji celé neuzavírají.
