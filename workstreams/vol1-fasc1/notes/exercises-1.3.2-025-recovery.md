# §1.3.2′, úloha25 — celý čítač a přesné srovnání

Zadání file55/p47, odpověď file114–115/p106–107. Vlastní úplná
jednofázová varianta je `sources/frequency25-one-phase.mms`; není
vydávána za explicitně určený program v knize. Originální sazba114/115 byla
zobrazena (`images/recovery-strcpy-114.png`, `images/recovery-frequency-115.png`). Žádná simulace ani
starý verifier se nespouštěly. Všechny níže uvedené ceny jsou odvozené
z úplných větví, nikoli z naměřeného vzorku.

## 1. Vstupy, adresy a přesná sémantika obou fází

Zdrojový p je násobek8, n nenulových bajtů končí nulou. Každý octabyte
obsahující bajt této posloupnosti je čitelný. Tabulka count má65536
vynulovaných octabytes, freq má256 octabytes a obě jsou zarovnané,
zapisovatelné, disjunktní a nepřekrývají zdroj ani kód. Jejich uvedená
alokace stojí2^19 a2^11 bajtů. Null není mezi255 požadovanými výsledky.
Předpokládáme n≤2^63−1 a platný rámec/registry; tím žádný součet
četností nevyvolá signed overflow. Registrační symboly count,freq,p
jsou globální báze, a,b,c,t,x,y jsou pracovní, stejně jako posunuté p.
Inicializace tabulek nulovou pamětí je součástí zdejšího vstupního
kontraktu. Cena jejich opětovného nulování při dalším volání se nepřidává
do porovnání, které je také neobsahuje ve vytištěném programu.

Je-li první wyde v a rovna U∈[0,65535], pak b=a>>45=8U+v s0≤v≤7.
Zaokrouhlení paměťové adresy dolů zruší v a LDO/STO míří na count[U].
Není chyba, že SRU izoluje19 místo16 bitů. Každý průchod zvýší právě
tento čítač a posun16 bitů odstraní zpracovanou dvojici.

Je-li octabyte bez nul, jeho každý neprázdný zbývající suffix je nenulový,
takže PBNZ a skončí právě po čtyřech dvojicích. Před další Phase1 jsou
započteny všechny dvojice před p a nic za nimi. BDIF s ones detekuje nuly
po bajtech přesně jako v úplném StrCpy důkazu.

V posledním octabyte je t nulový marker po bajtech. Konečná smyčka nejprve
zvýší count aktuální dvojice a teprve potom vezme b=t>>48; b=0 iff oba
bajty této dvojice jsou nenulové. Následné posuny a přepočet t připraví
další dvojici. Končí přesně dvojicí obsahující první terminátor, nejpozději
po čtyřech průchodech. Nuly vložené posunem zespodu nemohou test zastavit
dříve než původní terminátor.

Pokud je poslední dvojice(u,0), musí se nenulové u ještě započíst.
Pokud je(0,v), nesmí se započíst v, ani když je nenulové. Phase2 pro
j=255,...,1 vytvoří přesně

    freq[j]=count[j,0]+Σ_(k=1)^255(count[k,j]+count[j,k]).

Tato formule započte obě souřadnice úplných nenulových dvojic, diagonálu
dvakrát, první souřadnici(u,0) jednou a celou(0,v) nula-krát. Proto
počet je přesně požadovaný počet j před prvním terminátorem.

Konkrétní registry realizují tuto formuli: p=8j; SL a,p,8 dává2048j,
LDA přidá count a LDO c,a,0 načte count[j,0]. t začíná8j a postupně
přičítá2048, tedy prochází count[k,j] vzestupněk=1,...,255. b začíná
2040 a klesá po8, tedy druhý LDO prochází count[j,k] sestupněk=255,...,1.
Po každé dvojici ADD je c součet právě navštívených položek; na konci
je nejvýše n. SUB/PBP pokryje všech255 vnitřních i vnějších iterací a POP
nastane. Adresy count jsou od0 do524280, freq od8 do2040, vše v alokaci.

Vytištěné testovací `abracadabraa`,0,`abc` má12 nenulových bajtů před
terminátorem. Započtené dvojice jsou ab,ra,ca,da,br,aa,0a; poslední
dvojice je zahozena právě pravidlem count[0,v]. Výsledek je a6,b2,r2,c1,d1,
ostatní0. Za nulou uvedené b,c se neobjeví v žádném výsledku.

## 2. Přesná cena skutečného vytištěného programu

Položme q=floor(n/8), r=n mod8, h=floor(r/2)+1. Je q celých nenulových
octabytes a h dvojic v konečném octabyte, včetně té s terminátorem.

Každý úplný octabyte: Phase1 má LDOU,INCL,BDIF,PBZ, tedy4υ+μ;
čtyři vnitřní šestice stojí24υ+8μ a poslední nevykonaný PBNZ přidá2υ.
Celkem9μ+30υ. Poslední Phase1 má nevykonaný PBZ, tedyμ+6υ.
Konečné dvojice mají osm instrukcí a dva mems, poslední PBZ přidá2υ;
tedy2hμ+(8h+2)υ.

Phase2 začíná jedním SET. Pro každý j je pět přípravných instrukcí
včetně jednoho LDO. Vnitřní smyčka má255 sedmic a poslední chybný PBP:
510μ+(7·255+2)υ. Konec vnějšího průchodu má STO,SUB,PBP, poslední
PBP opět+2υ; po všech j následuje POP za3υ. Celkem

    Phase2 = (255·512)μ+[1+255(5+7·255+2+3)+2+3]υ
           =130560μ+457731υ.

LDA s těmito třemi registračními operandy je jedna ADDU instrukce;
žádná skrytá expanze či velká okamžitá konstanta nezvyšuje uvedený počet.
Celá rutina, VČETNĚ POP, má tedy přesnou cenu

    T₂=(9q+2h+130561)μ+(30q+8h+457739)υ.                (1)

Pro n=0 je q=0,h=1 a čítačcount[0,v] je ignorován; cena130563μ+457747υ
zůstává definovaná. Pro dlouhé řetězce je hlavní člen(9n/8)μ+(15n/4)υ,
ale pevná Phase2 se nesmí zamlčet při porovnání krátkých vstupů.

## 3. Konkrétní jednoduchá jednofázová varianta

Vlastní přiložené tělo mění výše popsanou Phase1 na jednotlivé bajty:
SRU53 izoluje8j plus tři zanedbatelné adresní bity, posun je8 a konečný
test t>>56 zkoumá jeden bajt. Tabulka má256 položek a výsledek v položce0
se zahodí. Stejný invariant a přístupné stavy z§1 dokazují celé tělo
pro libovolné n; poslední počítaná nula neovlivní žádný požadovaný výstup.
Úvodní PUSHJ/TRAP vlastního driveru nejsou součástí porovnání rutin.

Pro k=r+1 má plný octabyte osm šesticek, poslední PBNZ+2 a Phase1 čtyři
instrukce:17μ+54υ. Konečný octabyte stojí(1+2k)μ+(8k+8)υ a POP3υ.
Proto

    T₁=(17q+2k+1)μ+(54q+8k+11)υ.                       (2)

Oba programy jsou správné na stejných řetězcích; T₁ navíc nepotřebuje
velkou wyde tabulku. Z h−k=−ceil(r/2) vychází přesně

    T₂−T₁ = [130560−8q−2ceil(r/2)]μ
           +[457728−24q−8ceil(r/2)]υ.                  (3)

Nezávislost μ a υ se nezaměňuje za jediný počet instrukcí.

## 4. Co přesně dokládají vytištěná číselná porovnání

Kniha neuvádí celé tělo „simple one-phase approach“ ani poměr μ/υ.
Proto nelze(2) automaticky dosadit za autorův neurčený program. Pro naši
přirozenou konkrétní variantu dostaneme při n=10^6:

    T₂=1255563μ+4207747υ,
    T₁=2125003μ+6750019υ.

Poměr závisí naρ=μ/υ>0. Je klesající, protože křížový rozdíl
1255563·6750019−4207747·2125003<0. Jeho obor je mezi přesnými
poměry1255563/2125003 a4207747/6750019. První je přibližně0.59085,
druhý0.62337; přiρ=1 je5463310/8875022≈0.61558. Knižních10/17≈0.58824
je tedy rozumná orientace pro paměťově dominantní limit tohoto
konkrétního srovnání, nikoli přesný či naρ nezávislý poměr.

U téhož programu je T₂ pro n≤130560 striktně dražší pro libovolná
kladná μ,υ: mems rozdíl130560−n−[n odd]≥0 a oops rozdíl je kladný.
Tento přirozený přechod je blízko2^17=131072. Přiρ=1 jsou pro všechna
n<2^17 oba členy dohromady kladné; maxima q≤16383 a ceil(r/2)≤4
dávají v(3) dolní mez63992υ>0.

Univerzální ostré čtení prahu však z(3) neplyne: pro n=131071 je
T₂−T₁=−512μ+64504υ, tedy přiρ=128 je nový program o1032υ levnější.
To není novýconfirmed ani novýcandidate proti knize, protože autorův
jednofázový komparátor nebyl určen. Je to přesná hranice toho, co lze
opravdu převzít ze srovnání s konkrétním celým programem.

Úloha25 proto zůstává partial pro přesnou interpretaci těchto dvou
vytištěných porovnání. Sémantika obou fází, všechna malá n, jejich úplný
nominální čas a konkrétní vlastní srovnání jsou již uzavřené. Nejde o
chybějící experiment; potřebný údaj je tělo porovnávaného programu nebo
výslovně zvolený přibližný význam a poměr cen.

## 5. Další věty na p107 a hranice následujícího zadání

„Unrolling“ skutečně může snížit nominální cenu: čtyři plné wyde kroky
se provedou bez prvních tří PBNZ a po čtvrtém bez posledního3υ PBNZ;
poslední SLU na nulu je také mrtvá. Jejich účinky se nahradí přímým
pádem do Phase1. Odstraní se tedy7υ z každého prokazatelně nenulového
octabyte, zatímco konečná smyčka zůstane. Test PBZ v Phase1 již předem
zaručil všechny čtyři dvojice; nevkládá se nový předpoklad o datech.

Jump table a128 registrů jsou pouze námět „worthy of consideration“,
nikoli vytištěný hotový algoritmus nebo přesná tvrzená převaha. Není
třeba dokazovat optimum přes všechny možné rutiny. Bourne–Ford1961,
48–67 zůstává explicitně přeskočená bibliografie bez nového shánění.

Úvod26 tvrdí problém s cache menší než2^19. Velikost celé wyde tabulky
je přesně tato; z menší kapacity samotné však neplyne počet missů ani
výkonnostní převaha. Distribuce četností, přístupová posloupnost, asociativita,
výplň a cena missů by potřebovaly konkrétní model. Tato výkonnostní
část i požadovaná měření26 zůstávají partial; normativní definice MMIX
cache se nezaměňuje s tvrzením o všech realizacích.

Použití vzorů: stavový důkaz zvlášť řeší(0,v) a(u,0); nákladový vzor
vynucuje poslední špatné predikce obou smyček i pevnou Phase2; vzor
přesných mezí odděluje korektní hlavní člen od neurčeného komparátoru.
