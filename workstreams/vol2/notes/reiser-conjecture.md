# §3.2.2-26: předpoklady a rozsah Reiserových výsledků

Kontrola 1. listopadu 2026. Uzavíráme audit formulace úlohy 26,
její poznámky a připsaných výsledků; netvrdíme řešení původní obecné
domněnky. Zadání je na [str.39](../images/vol2-p039.png); mezi odpověďmi
25 a 27 není samostatná odpověď 26.

Používáme k pro řád lineární rekurence, p pro prvočíslo, alpha pro
exponent modulu p^alpha, lambda_alpha pro nejmenší periodu a N_alpha
pro počet nul v ní. Primitivní charakteristický polynom stupně k
modulo p znamená, že jeho kořen má řád p^k-1 v tělese s p^k prvky.
Nedegenerovaný počáteční vektor zde znamená vektor nenulový modulo p.

## Dva odlišné problémy formulace

1. [C0010](C0010-reiser-primitivity.md): domněnce o počtu nul chybí
   primitivita. Pevná rekurence X_n=4X_(n-3) modulo 3^alpha se seedem
   (0,0,1) má N_alpha=2·3^(alpha-1), což vyvrací vytištěnou mez
   c·3^(alpha/2), dokonce pro údajně ověřený stupeň 3.
2. [C0009](C0009-period-search-termination.md): pro závěr o discrepancy
   nestačí ani primitivita modulo p a platná domněnka o nulách.
   Rekurence X_n=X_(n-1)-X_(n-2), p=2, má periodu nejvýše 6 pro
   všechny seedy a alpha; platí c=6, ale dvojice ze seedu (1,1)
   mají discrepancy nejméně 1/4. Chybí předpoklad růstu period.

Oba protipříklady mají přesné obecné důkazy i samostatnou konečnou
kontrolu v [verify_reiser_hypotheses.py](../verify_reiser_hypotheses.py).
Stejná znění přetrvávají v [náhledu digitálního vydání z července 2026](../images/publisher-preview-p039.png).

## Primární Reiserův pramen

Přečteny relevantní části původní disertace *Analysis of Additive Random
Number Generators*, CS-TR-77-601 (1977), [zdroj](../sources/reiser-1977.json):
zavedení rekurence na str.1, diskuse period v kapitole 1, odvození meze
počtu nul a discrepancy v kapitolách 3–4, zejména str.20 a 24–26.
Není to audit celé disertace ani kontrola všech jejích numerických testů.

Rekurence (1.1) je od začátku omezená na primitivní polynom a
nedegenerované seedy. Věta 4.4 na str.25 uvádí stupeň 3 s těmito
předpoklady. Domněnka 4.1 na str.26 odkazuje zpět na (1.1).
Analýza využívá fázi, v níž se perioda při zvýšení alpha násobí p;
například konec str.25 to výslovně předpokládá. Konstantní perioda
v C0009 tuto fázi nikdy nedosáhne. Protipříklad proto nevyvrací
odvození, které ji již předpokládá.

Připsání stupně 3 odpovídá primárnímu prameni po obnovení primitivity.
Jeho hlubší odhad se zde kontroluje jako citovaný výsledek s rozsahem,
nikoli jako nově nezávisle dokázaná obecná věta. Omezená rešerše
nenalezla primární novější řešení obecné domněnky; úplnou rešerši
literatury ani současnou otevřenost bez výhrad netvrdíme.

## Dolní mez na konci poznámky

Tvrzení o možných seedech s N_(2alpha)>=p^alpha pro k>=3 odpovídá
[větě 4.2 na str.20](../images/reiser-p20.png). Následuje vlastní
lineárně algebraický důkaz v zamýšleném primitivním případě, při
lambda_beta=p^(beta-1)(p^k-1) pro příslušné exponenty beta.

Označme T matici posunu vektoru k po sobě jdoucích členů; e_1 je řádek
(1,0,...,0). Protože primitivita modulo p činí každý nedegenerovaný
vektor cyklickým (jeho prvních k posunů tvoří bázi modulo p), mají
všechny nedegenerované vektory stejnou periodu, jako matice T.
Platí tedy T^lambda_alpha=I+p^alpha B pro celočíselnou matici B.

Zvolme vektor v modulo p^(2alpha) s první souřadnicí nulovou a
e_1 Bv=0 modulo p^alpha, avšak v!=0 modulo p. Takový v existuje:
zbývá jedna homogenní rovnice v k-1>=2 neznámých. Jsou-li všechny její
koeficienty nulové modulo p^alpha, vezmeme jednotkový vektor. Jinak
vydělíme koeficienty jejich společnou největší mocninou p; jeden
koeficient u_i je jednotka. Pro jiné j položíme v_j=u_i, v_i=-u_j,
ostatní souřadnice nula. Rovnice platí a v_j není dělitelná p.

Binomický rozvoj matic, jehož členy stupně >=2 jsou násobky p^(2alpha),
dává pro 0<=j<p^alpha

```
e_1 T^(j lambda_alpha) v
  = e_1 (I+j p^alpha B) v
  = 0                         modulo p^(2alpha).
```

Všechny tyto indexy jsou v jedné periodě a jsou různé, protože
lambda_(2alpha)=p^alpha lambda_alpha. Dostáváme alespoň p^alpha nul.
Seed může záviset na alpha, přesně jak poznámka dovoluje. Pro k=2
by jedna rovnice v jediné neznámé nemusela mít primitivní řešení;
požadavek k>=3 je v tomto důkazu podstatný.

Rovněž správná je heuristická konstanta pro rovnoměrně rozdělené
hodnoty: při lambda_alpha=p^(alpha-1)(p^k-1) je průměrný počet
výskytů jedné hodnoty lambda_alpha/p^alpha=(p^k-1)/p, nezávisle
na alpha. Neznamená to důkaz rovnoměrnosti pro libovolné seedy.

Všechny vrstvy errat prověřeny; relevantní oprava úlohy 26 nenalezena.
Záznamy C0009/C0010 obsahují úplnou stopu sazby, opravy a neodeslané drafty.
