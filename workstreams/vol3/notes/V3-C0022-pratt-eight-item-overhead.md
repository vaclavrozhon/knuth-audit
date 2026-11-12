# V3-C0022 — v osmiprvkovém průměru chybí režie průchodů

Stav: confirmed/low, 7. listopadu 2026.
Lokace: §5.2.1, odpověď31, tištěná624/file635, odstavec
za časovým vzorcem. Originál `images/insertion-file-635.png`
je zobrazen. Sken je druhé vydání, první tisk1998; fyzický
tištěný exemplář tím není samostatně ověřen.

Text uvádí pro N=8 přírůstky6,4,3,2,1, průměr A≈3.892
a celkový průměrný čas276.24u. Přímo nad tím je čas

    time=7NT+7A−2S+1+15T.

Tento vzorec je instrukčně správný. Níže jej odvozujeme;
chyba je v uvedeném číselném průměru, nikoli ve třídicím programu.

## Konkrétní rozpor bez enumerace průměru

T=5 a S=6+4+3+2+1=16. Pro každý vstup tak platí

    time=7·8·5+7A−2·16+1+15·5=324+7A≥324u,

protože A je nezáporný počet. Průměr276.24u je tedy nemožný
bez ohledu na to, zda je publikovaný průměr A přesný.
Na již seřazeném vstupu je A=0 a čas přesně324u.

Dosazení uvedeného A≈3.892 dává přibližně351.24u.
Rozdíl351.24−276.24=75 je právě15T, čili publikované číslo
odpovídá vynechání celé režie pěti průchodů. Přesný průměr A
ani všech8! vstupů se znovu nepočítaly; k rozporu nejsou potřeba.

## Úplný instrukční součet

Před každým Prattovým h-průchodem je pole2h- i3h-ordered:
tyto větší přírůstky již proběhly, nebo jsou≥N a podmínka je
prázdná. Věta K zachovává dřívější uspořádání. Podle úplného
matchingového důkazu P0780–0781 má každá h-třída pouze
disjunktní sousední inverse. Program proto správně zamění
inversní pár a přeskočí následující srovnání v téže třídě.

Nechť M=NT−S je počet všech sousedních hran tříd přes průchody,
B počet provedených záměn a A počet záměn na poslední hraně
příslušné třídy. Každá záměna kromě těchto A vynechá právě
jedno existující srovnání; poslední záměna už nemá co vynechat.
Počet vykonaných srovnání je tedy C=M−B+A.

V následujícím součtu mají MIX load/store/compare cenu2u,
enter/increment/decrement/jump1u, jako v předešlých programech:

|řádky|četnost a příspěvek|
|---|---|
|01|1u|
|02–08,21–22|13T: 2+1+2+2+2+1+1+1+1 za průchod|
|09–11|5C: load2, compare2, jump1|
|12–15|7B: load2, store2, store2, increment1|
|16–17|2(C+S): po každém srovnání a jednou na začátku každé třídy|
|18|S|
|19–20|2(S+T): každá třída a jeden konečný test rI2=0 za průchod|

Celkem je

    1+13T+5C+7B+2(C+S)+S+2(S+T)
    =1+15T+5S+7(C+B)
    =7NT+7A−2S+1+15T.

Žádná část15T není volitelnou externí inicializací: všechny
uvedené řádky se vykonávají uvnitř zobrazeného programu.
Navíc už záporný případ276.24<324 vylučuje, že by šlo pouze
o zaokrouhlení neověřeného A.

## Errata a dopad

`sources/pratt-eight-item-errata-review.json` zaznamenává všech
pět vrstev. Známé opravy624 pouze centrují T v tabulce četností
a ruší nadbytečné slovo; historická prvovydaná oprava602 mění
znaménko adresy ENN2 a už je v našem originálu zapracovaná.
Žádná nemění276.24 ani chybějící75u v tomto číselném příkladu.

Navržená lokální oprava je zahrnout15T; při převzetí původního
výpočtu průměru tím číslo276.24 vzroste na351.24u. Závažnost
low: jde o aditivní režii v analýze malého vstupu. Správnost
programu a asymptotická Θ(N(log N)²) se touto chybou nemění.
Celá úloha31 včetně dalších empirických údajů se tímto jediným
nálezem nepovažuje za zkontrolovanou.


Doplnění7.11.2026: P0842 v `insertion-proof-eight-items-table5.md` nyní samostatně dokládá přesný E A=467/120 a E B=142/21 přes rankové prefixy, bez generování permutací. Správný průměrný čas je tedy42149/120=351.241666…u. Původní kratší důkaz chyby z minima324u zůstává platný a nebyl opakován.
