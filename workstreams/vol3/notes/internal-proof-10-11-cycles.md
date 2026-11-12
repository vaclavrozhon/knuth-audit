# §5.2–10 a11: oba směry cyklů, čas a pravděpodobnost

Zadání79–80/files90–91, odpověď616–617/files627–628,
původní sazba zobrazená. Známá oprava2020 mění MacLeod
na Macleod; matematiku nemění. Pět vrstev je již
v `sources/insertion-errata-review.json`.

## P0660: celá správnost Algorithm P

Původní permutaci označme p_0, původní záznamy R^0.
Po dokončení kteréhokoli cyklu platí v jeho pozicích
R_j=R^0_(p_0(j)) a p(j)=j. Nedotčené cykly mají
p=p_0 a původní záznamy. To je invariant vnější smyčky.

Pokud p(i)≠i, leží i v dosud nedotčeném netriviálním
cyklu a_0=i,a_1,…,a_(l−1), kde p_0(a_t)=a_(t+1)
a p_0(a_(l−1))=i. P3 uloží R^0_i do t a nastaví j=i.
Po s průchodech P4 jsou pozice a_0,…,a_(s−1) správné
a označené samoodkazem; j=a_s. Zbytek cyklu stále má
původní p i záznamy. Proto lze bezpečně načíst
k=p(j)=a_(s+1), zkopírovat jeho původní záznam do j
a teprve pak označit p(j)=j a pokračovat na k.

Po l−1 průchodech je j=a_(l−1) a jeho stále původní
p(j)=i ukončí smyčku. P5 tam uloží t=R^0_i a označí
poslední uzel. Nečte se již přepsaný záznam a nemůže
se předčasně narazit na značku z jiného cyklu.
Vnější smyčka nakonec navštíví každý nedotčený cyklus;
jednobodové cykly správně přeskočí. Důkaz nezávisí
na vzestupném či sestupném pořadí vnějších i.

Tím je provedeno přesně R_j←R^0_(p_0(j)), nikoli
opačný směr permutace. Na konci je uložená tabulka p
identita; algoritmus ji záměrně používá jako značky.

## P0661: čas, paměť a opačný směr přemísťování

Nechť A je počet cyklů a B počet singletonů p_0.
Netriviálních cyklů je A−B. Jejich kroky P4 mají
souhrnnou četnost∑(l−1)=N−A; kroků P3 i P5 je A−B.
Každá nesamostatná pozice se zapíše právě jednou,
celkem N−B zápisů do pole záznamů. Vnějších testů je N.
Čas při konstantní ceně záznamu a přístupu je O(N).
Pomocná paměť je jeden záznam t a O(1) indexů;
existující tabulka p není nová přidaná paměť.

Pro opačný požadavek R_(q(i))←R^0_i můžeme použít
stejné cykly s neseným záznamem. Na začátku uložíme
t=R_i; v každém kroku načteme k=q(j), vyměníme t
s R_k, označíme q(j)=j a přejdeme j=k. Jakmile
k=i, cyklus je hotov. Invariant: t je původní záznam
právě opuštěné pozice, všechny již zapsané cíle jsou
správné a další q ještě nebylo změněno. Takto se
realizuje i přemístění podle COUNT+1 z úlohy4.

Výměna velkého záznamu s t se provádí slovo po slovu
s jedním skalárním slovem navíc; nevyžaduje druhou
celou pomocnou oblast záznamu. U jednoho wordu stačí
registry. Singleton lze opět přeskočit. Prázdný vstup
má prázdnou vnější smyčku.

## P0662: B1–B3 při vypočítávaném, neměnném p

Při hledání vůdce navštěvuje k=p(i),p²(i),… prvky
cyklu i, dokud poprvé nenajde k≤i. Pokud k<i, není
i minimum cyklu a žádná data se nehýbají. Pokud k=i,
prošel se celý cyklus a všechny jeho ostatní prvky
jsou větší. Je to právě jeho jednoznačné minimum.
Smyčka vždy skončí nejpozději při návratu do i.

V B3 se tedy každý cyklus přesune právě jednou.
Na začátku této části je k=i; uložení R_i do t,
kopírování R_k←R_(p(k)) až před návrat do i a poslední
zápis t mají přesně invariant P0660 bez označování p.
U singletonu se jen uloží a vrátí tentýž záznam.
Vnější testování pozdějších i se stále řídí stejným
neměnným p, takže přesun dat nemůže vyvolat druhý
přesun téhož cyklu. Potřebujeme jeden záznam a O(1)
indexů, žádné pole značek.

Má-li vyhodnocení p(i) konstantní cenu, může hledání
v nejhorším stát Θ(N²). Pro cyklus(1,2,…,N) má
testování i délku N−i+1, celkem N(N+1)/2 testů.
To je současně obecná horní mez, protože před prvním
≤i lze navštívit nejvýše N−i různých větších prvků.
Přesun dat samotný zůstává lineární.

## P0663: přesný průměr počtu provedení B2

T_i počítá **všechna** provedení testu B2 pro dané i,
včetně posledního, kdy k≤i. V rovnoměrné náhodné
permutaci mají postupně odkrývaní následníci, dokud
se neuzavře/nezastaví cesta, rovnoměrný výběr mezi
dosud nepoužitými cíli: každé přípustné částečné
injektivní zobrazení má stejný počet doplnění.

Zastavujeme při prvním z i cílů1,…,i; mezi nimi je
i samo, které cestu uzavře. Ostatní dříve navštívené
cíle jsou>i a už se nemohou opakovat. T_i má tedy
rozdělení pozice prvního označeného prvku v náhodném
uspořádání N prvků s i značkami. N−i neznačených
prvků se rozděluje do i+1 výměnných mezer; první
mezera má střední délku(N−i)/(i+1). Proto

    E T_i=1+(N−i)/(i+1)=(N+1)/(i+1),
    E∑T_i=(N+1)(H_(N+1)−1)=(N+1)H_N−N.

To je přesně vytištěný vzorec, odvozený bez pouhého
odkazu do svazku1. Počet úspěšných opakování k←p(k)
by byl o N menší; nesmí se za T_i zaměnit. Pro N=1
je T_1=1, opakování0. Průměrný celkový čas v uvedeném
modelu je O(N log N), při dražším p se jeho cena
musí započítat zvlášť.

## P0664: každá instrukce MIX odpovědi11 a její četnost

I1 je stálý začátek aktuálního cyklu i, I2 pohyblivé j,
I3 načtené k a X pomocný záznam t. CMP1 P,1 a JE
přeskočí právě samoodkazy. LDX/ENT2 vytvoří P3.
LD3 načte dosud původní p(j), LDA/STA přenesou R_k,
ST2 P,2 označí právě staré j, ENT2 přejde na k.
CMP1 P,2 nyní porovnává původní i s p(nového j),
tedy přesně ukončovací podmínku P4. STX/ST2 dokončí
poslední uzel. DEC1/J1P projdou N,…,1; jiný směr
než v abstraktním zadání neovlivňuje P0660.

Celý součet časů je

| část | čas/u |
|---|---:|
|počáteční ENT1|1|
|CMP1,JE,DEC1,J1P vnější smyčky|5N|
|LDX,ENT2 v P3|3(A−B)|
|sedm instrukcí P4|12(N−A)|
|STX,ST2 v P5|4(A−B)|

Tedy T/u=17N−5A−7B+1. Tím jsou doloženy i všechny
vytištěné četnosti A−B a N−A. N=1 dává6u,
samoodkaz se skutečně jen otestuje; N=0 se zachytí
před nehlídanou MIX smyčkou, jako u předchozích programů.

## P0665: všechny uvedené momenty počtu cyklů

Rovnoměrnou permutaci velikosti j vytvořme z rovnoměrné
permutace velikosti j−1 jednou z j možností: buď nový
singleton j, nebo vložení j hned za kterýkoli z j−1
starých prvků v jeho cyklu. Vymazání j je jednoznačná
inverze, takže jde o bijekci j·(j−1)!=j! objektů.
Volby lze provádět nezávisle a rovnoměrně pro j=1,…,N.

Počet cyklů A je součet nezávislých indikátorů nové
singletonové volby s pravděpodobnostmi1/j. Proto

    E A=H_N,    var A=H_N−H_N^(2).

Minimum1 realizuje jediný cyklus, maximum N identita;
pro N=1 je rozptyl0. To samostatně dokládá celý
odkaz na svazek1, nikoli jen správnou podobu vzorce.

## P0666: všechny uvedené momenty pevných bodů

Pro B=∑I[p(i)=i] je jednotlivá pravděpodobnost1/N,
tedy E B=1 pro N≥1. Pro různé i,j a N≥2 je společná
pravděpodobnost(N−2)!/N!=1/(N(N−1)). Odtud
E B(B−1)=1, E B²=2 a var B=1. Nevyžaduje se
nepravdivá nezávislost jednotlivých pevných bodů.

Maximum B=N je identita. Minimum0 pro N≥2 realizuje
cyklický posun. Pro N=1 je B=1 a var0, proto je
vytištěné omezení N≥2 důležité a správné.

## P0667: výsledná cena a přesně vymezené srovnání s kopírováním

Z P0664–66 při rovnoměrných permutacích plyne

    E T/u=17N−5H_N−6.

Pro N≥2 je minimum5N+1 na identitě, protože
5A+7B≤12N; maximum17N−4 na jediném N-cyklu,
protože A≥1 a B≥0. Hodnoty jsou dosažitelné.

Přímé kopírování R_(p(i)) do odděleného S_i lze na MIX
provést smyčkou LD2 P,1; LDA INPUT,2; STA OUTPUT,1;
DEC1 1; J1P…, s počátečním ENT1 N. Stojí8N+1u.
V tomto přesném modelu jednoho wordu a rovnoměrného p
se poměr průměrných časů blíží17/8=2.125. To poskytuje
konkrétní smysl přibližnému poměru z74, ale neověřuje
jeho nevymezené slovo „usually“ ve všech aplikacích.

Pro dlouhé záznamy kopírované přes pomocný záznam
má cyklus délky l cenu l+1 kopií záznamu proti l
kopiím do druhé oblasti; v součtu N+A−2B proti N.
V pohybově dominantním modelu s náhodným p se tento
poměr blíží1. Nelze proto z jednoho modelu udělat
univerzální faktor2. P0646 zůstává partial v tomto
konkrétním neurčeném srovnání. Seznamová metoda12 je
v pozdějším `internal-proof-12-list-rearrangement.md`
také plně dokázaná, takže prostorový odkaz už mezeru nemá.

## P0668 — partial: historické srovnání pohybu dat

Primární obsah vydavatele potvrzuje existenci
[Algorithms supplement, Computer Journal10(3)(1967),306–312](https://academic.oup.com/comjnl/issue/10/3).
Odkaz na vlastní článek přes DOI10.1093/comjnl/10.3.306
se však neotevřel. Původní Boothroydův program a přímé
historické srovnání pohybu dat proto nejsou ověřeny;
totéž platí pro konkrétní Macleodova zdokonalení1970
a poznámku Cybernetics1965. Nejde o závislosti žádného
z výše uvedených důkazů a nejsou vydávány za prověřené
vnější věty. Konkrétní tvrzení o menším pohybu dat
zůstává samostatné partial; bibliografická výjimka
nenahrazuje jeho výpočet. Další bibliografické hledání se zde
výslovně přeskočilo. Nový nález ani výpočet nevznikl.
