# §1.3.2′, úloha26 — celé smyčky a přesný výkonový rozsah

Zadání file55/p47, odpověď file115–116/p107–108. Dřívější poznámka
správně ponechala vynechané úseky partial. Nyní jsou konkrétně doplněné
v `sources/frequency26-one-table.mms` a `sources/frequency26-two-tables.mms`.
Druhá rutina obsahuje vlastní koncovku a celé sečtení tabulek; nic z toho
není vydáváno za doslova vytištěný kód. Originální sazba116 byla zobrazena
v `images/recovery-frequency-116.png`. Žádná simulace ani starý verifier
se nespustily; jediný nový nice15 statický součet ověřil obě nová těla
43instrukcí/17mems (`results/frequency26-structure.json`).

## 1. Společné podmínky a extrakce

Stejné vstupy jako v úplném důkazu25: aligned p, konečný řetězec délky n
s nulou, přístupné zdrojové octabytes, disjunktní vynulované tabulky,
0≤n≤2^63−1, platný rámec a pracovní registry. One-table používá256
octabytes, two-tables512; všechny255 nenulové výsledky jsou nakonec ve freq.
Vlastní malé hlavní programy obsahují data jen pro konkrétní spustitelné
rozmístění, důkaz se nevztahuje pouze na tento text.

Pro byte j je `((a <<8j) mod2^64)>>53 =8u+v`, kde u je příslušný
bajt a0≤v≤7. Zaokrouhlení LDO/STO adresy zruší v. Dodatečné SRU b,b,3
v terminální smyčce vrátí přesně u, takže PBNZ testuje původní bajt,
nikoli přimíchané adresní bity. BDIF v prologu a na konci hlavního těla
povolí vstup do unrolled části pouze pro osm nenulových bajtů.

## 2. Celá jednovýsledková smyčka

Registry b a bb střídavě nesou adresový index aktuálního a následujícího
bajtu. Před zvýšením c je mezi LDO a INCL vložen nezávislý SLU pro další
bajt. SRU dalšího indexu je rovněž vykonán před STO aktuálního čítače.
Potom LDO načte následující čítač. Tímto vzorem je v úplném souboru
rozepsáno všech osm bajtů, nejen vytištěný začátek a konec.

Invariant po každém STO: tabulka obsahuje správné četnosti všech
dosavadních bajtů, b/bb připravuje následující adresu a a se nezměnilo,
dokud nejsou extrahované všechny potřebné indexy. I při stejných
sousedních znacích se nový čítač načte až PO předchozím STO. Sekvenční
sémantika proto dává dvě zvýšení, nikoli ztracenou aktualizaci.

Po načtení čítače osmého bajtu lze a přepsat následujícím octabyte:
starý osmý index je již v bb. INCL p a nový BDIF nezmění tento čítač;
STO jej uloží a PBZ buď opakuje osm nenulových bajtů, nebo přejde do3H.
Koncovka prochází až po první nulu včetně, zvýší i freq[0] a odejde.
Nula není mezi požadovanými výsledky; žádný bajt za ní se nezapočítá.
Všechny frekvence jsou nejvýše n, výsledek je tedy přesný.

## 3. Dvě tabulky a všechny aliasing případy

V hlavní části druhé rutiny dostanou bajty na pozicích0,2,4,6 tabulku
freq a1,3,5,7 tabulku freqq. Každá dvojice používá různé fyzické tabulky,
takže předběžná dvě LDO se neovlivní ani při stejných znacích. Po obou
STO se načítá další dvojice; opakování téhož znaku v rámci jedné tabulky
se proto opět zvyšuje po předchozím zápisu.

Registry b/bb a bbb/bbbb se střídají pro dvě dvojice. Nové extrakce
nepřepíší index právě ukládané dvojice. Poslední osmý index zůstává
v bbbb, takže a lze znovu načíst před posledními zvýšeními a zápisy.
To dokazuje invariant celé vytištěné části i všech doplněných středů.

Vlastní koncovka3H ukládá všechny zbývající bajty do freq. Nemusí zachovat
paritu pozice: stačí invariant, že freq[j]+freqq[j] je počet dosud
zpracovaných j. Po první nule se pro j=255,...,1 provede celé
`freq[j]←freq[j]+freqq[j]`. Dvojice čítačů je nezáporná a součet≤n,
takže ADD nepřeteče. Indexy8...2040 jsou v obou tabulkách, žádná složka
se nevynechá a finální výsledek splní zadání.

Knižní důvod pro dvě tabulky je skutečný: kdyby se oba předběžné LDO
obrátily na tutéž tabulku a oba znaky byly j, oba by načetly c, následná
zvýšení dala c+1 a oba STO by zapsaly c+1. Správně má být c+2. Například
první dva bajty `aa` při nulové tabulce dají1 místo2. Nezávislost tabulek
řeší všechny takové páry, nikoli pouze tento konkrétní příklad.

## 4. Přesné nominální profily obou úplných těl

Nechť q=floor(n/8),k=(n mod8)+1. Prolog první rutiny má čtyři
instrukce a1mem; při q=0 stojí BNZ navíc2υ. Jedno úplné tělo od2H
po PBZ má43 instrukcí a17mem (16count operací a jedno předčtení zdroje).
Při q>0 poslední PBZ přidá2υ; tento příplatek přesně nahrazuje příplatek
q=0 v prologu. Koncovka má k sedmic, poslední PBNZ+2υ a POP3υ. Proto

    T_A=(17q+2k+1)μ+(43q+7k+11)υ.                       (1)

Vlastní jednoduchá jednofázová rutina25 měla stejný počet mems a cenu
(54q+8k+11)υ. Zdejší plné unrolling tedy ušetří přesně(11q+k)υ pro
každé n≥0. Tato nominální převaha je doložená bez měření pipeline.

Dvoutabulkový prolog má o jeden SLU více, hlavní tělo opět43 instrukcí
a17mem. Vlastní koncovka bez POP má7k+2υ a2kmem. Celé spojení tabulek
má SET,255 šesticek LDO,LDO,ADD,STO,SUB,PBP, posledníPBP+2 a POP3:
765μ+1536υ. S vyvážením poslední větve jako výše je

    T_B=(17q+2k+766)μ+(43q+7k+1545)υ.                   (2)

Rozdíl je přesně765μ+1534υ. Ve fixním mems/oops modelu tento konkrétní
dvoutabulkový program není rychlejší. Knižní tvrzení se však výslovně
týká jiného, superskalárního modelu; tyto dvě ceny nejsou protipříkladem.

## 5. Co lze dokázat o rozvrhu a co ještě zůstává partial

V první hlavní smyčce opravdu žádný výsledek LDO není použit hned
následující instrukcí. To stačí proti této jedné závislosti na stroji
s jedním vydáním za cyklus, load latency nejvýše2, ostatními používanými
latencemi1, dostatečnými porty, dostupnými cache daty a respektovaným
store-to-load pořadím. Pro každý load je výše vyznačený nezávislý gap;
závislý INCL proto nastane nejdřív po dvou issue časech.

To není úplná záruka absence všech stallů. Již vytištěná krátká koncovka
má LDO c bezprostředně následované INCL c. Dále mohou rozhodovat cache
missy, store forwarding nebo konflikt zdrojů. Výrok o nepoužití hned
v další instrukci je doslovně platný pro dlouhé hlavní tělo, nikoli pro
všechny instrukce celého programu.

Ve druhém hlavním těle lze první42 instrukce párovat po dvou a PBZ
vydat jako43. instrukci zvlášť. Takové22cyklové schéma je přípustné,
pokud stroj vydá dvě nezávislé ALU či paměťové instrukce za cyklus,
má dvě paměťové cesty, load latency≤2, ostatní latency1, potřebné
forwarding/pořadí a hit/branch předpoklady. Dvojice LDO c,LDO cc je
oddělena od dvojice INCL c,INCL cc jedním cyklem nezávislých SLU;
ostatní dvojice mají tytéž vztahy. Čtení nového a je před BDIF/SLU
rovněž oddělené jedním cyklem. V jedné vydané dvojici není RAW
závislost. Čtení starého p a jeho následná aktualizace musejí respektovat
pořadí operandů, jak vyžaduje sekvenční sémantika.

Samotná šířka vydávání2 tyto ostatní předpoklady nezaručuje. Ani uvedené
přípustné schéma samo nedokazuje převahu vůči optimálnímu rozvrhu jiného
programu nebo při libovolné distribuci cache missů. Vlastní krátká
koncovka/merge nejsou vydávány za dokonale rozvržené pro všechny stroje.

Zadání požaduje optimalizaci na realistických konfiguracích pipeline
simulátoru. Tyto konkrétní konfigurace a jejich měření nebyly zvoleny ani
spuštěny; **právě tento výkonový závazek zůstává partial26**, včetně
přesného významu úvodních slov o cache na file115. Chybějící funkční
tělo, aliasing invariant ani nominální cena už mezerou nejsou. Globální
optimalita není doložena a knižní návrh ji sám neprokazuje.

Celá file116 má nyní mapu: oba celé fragmenty/ellipsis, oba koncové
přechody, tabulkové náklady a poslední aliasing odstavec jsou pokryté
výše; výkonnostní tvrzení mají přesné podmínky a otevřený rozsah.
Vzor úplného stavového důkazu brání uzavřít jen první pár bajtů; nákladový
vzor vyžaduje merge a krátký konec; vzor mezí odděluje nominální čas
od přípustného, ale dosud neměřeného pipeline rozvrhu.
