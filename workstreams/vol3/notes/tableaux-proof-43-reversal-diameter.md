# Tableaux43: horní mez a všechny extrémní případy

Zadání72/file83 a odpověď615/file626. Používá se graf,
kritérium rozdělení cyklu a význam2-cyklu přesně z P0606–07;
tyto hotové argumenty se neopakují. Převrat vždy obrací
pořadí i znaménka, včetně jednoprvkového úseku.

## P0616: kontrakce správné sousednosti

Správná sousednost je buď(+k,+(k+1)), nebo(−(k+1),−k).
Obě odpovídají téže černé/šedé2-cyklové hraně.
Lze ji sloučit v jediný orientovaný blok, který se v dalších
převratech přesouvá celý. Cílové pořadí menšího problému
vznikne sloučením týchž sousedních hodnot a přeznačením hodností.
Kladný/záporný blok představuje správný/vzhůru obrácený vnitřní
pořádek; převrat jej rozvine na původní geny správně.

Sousednost s hranicí0 nebo n+1 dovoluje vypustit správně
umístěný krajní blok. Počítání genů se v každém případě sníží
o1 a každé řešení menší úlohy se zvedne na stejně dlouhé řešení
původní. Dvě různé správné sousednosti lze kontrahovat postupně.
Pro n≥2 to sníží počet o2; pokud sdílejí gen, sloučí se řetěz
tří objektů, případně s jedním pevným koncem. Jediná výjimka,
kdy obě hranice obepínají jediný gen, je n=1 a řeší se zvlášť.

## P0617: jeden převrat na hodnotové hranici znamének

Je-li−k přítomno a k−1 kladné, označme jejich pozice q,p.
Pro k=1 je k−1 pevná levá hranice0.

- Při p<q převraťme[p+1,q]. Kladné k se připojí za k−1,
  vznikne správná sousednost.
- Při q<p převraťme[q+1,p]. Vznikne(−k,−(k−1));
  původní−k zůstalo mimo převrat, takže zůstává záporný blok.

Obdobně, je-li−k a kladné k+1 (nebo pravá hranice pro k=n),
vznikne správná sousednost po převratu od−k po buňku před
kladným k+1, leží-li−k vlevo. Leží-li vpravo, převrátí se
úsek od kladného k+1 po buňku před−k; vznikne
(−(k+1),−k) a záporný blok zůstane.
Všechny intervaly jsou neprázdné a uvnitř skutečných genů.
Tím jsou doloženy obě orientace obou knižních pravidel.

## P0618: chybějící případ, kdy by zmizela všechna minus

Vezměme nejmenší zápornou hodnotu a a největší b.
Hodnoty a−1,b+1 jsou kladné nebo pevné hranice.
Zkusme dva speciální kroky P0617, spojující a−1 s a
a b s b+1. Pokud alespoň jeden ponechá zápornou hodnotu,
vznikla jedna správná sousednost a po její kontrakci je
menší problém stále záporný: buď je nová sousednost kladná
a minus je jinde, nebo sama představuje záporný blok.

Zbývá případ, kdy oba kroky odstraní všechna minus.
Převrat to může udělat jen tehdy, když převrací právě všechny
záporné prvky a žádný kladný. Jinak by buď některé minus
zůstalo venku, nebo by uvnitř vzniklo nové minus.

První z těchto dvou kroků tedy říká, že všechny záporné prvky
tvoří jediný souvislý fyzický blok, bezprostředně za a−1,
s posledním prvkem−a. Druhý říká, že tentýž blok začíná−b
a bezprostředně za ním je b+1. Obrácení celého bloku proto
vytvoří současně sousednosti(a−1,a) a(b,b+1).
Byly to dvě různé nesprávné hranice a staly se dvěma2-cykly.
Vnitřní pořadí bloku se nemusí předpokládat.
Tím je zejména dokázán knižní silnější předpoklad „když všechny
speciální kroky odstraní minus“; stačily dva konkrétní.

## P0619: nekruhová simultánní indukce a kladný případ

Dokážeme současně:
B_n: obsahuje-li permutace minus, stačí nejvýše n převratů;
A_n: každé permutaci stačí nejvýše n+1.
Pro n=0 je prázdný problém hotový, pro n=1 stačí0 nebo1 krok.

Nejprve pro dané n≥2 dokážeme B_n s použitím jen menších indexů.
P0617–18 buď vytvoří jednu správnou sousednost a ponechá minus,
nebo jedním krokem vytvoří dvě sousednosti. V prvním případě
po kontrakci použijeme B_(n−1): cena≤1+(n−1)=n.
Ve druhém použijeme A_(n−2): cena≤1+(n−2+1)=n
(pro n−2=0 je ve skutečnosti potřeba0 dalších kroků).

Potom dokážeme A_n. Záporný případ má již B_n; kladná identita
nepotřebuje nic. V jiné kladné permutaci má graf netriviální
cyklus. Šedé i černé hrany spojují R-konec s L-koncem,
takže při střídavém průchodu kterýmkoli cyklem jsou všechny
černé hrany orientované stejně. Vybereme dvě v témže
netriviálním cyklu. Jejich převrat zachová počet cyklů podle
P0607 a vytvoří alespoň jedno minus. Následuje již dokázané
B_n, celkem≤n+1. Takto se nepoužívá A_n k důkazu B_n.

Argument dává realizovatelnou posloupnost převratů se
sloučenými bloky. Kniha zde nestanoví čas datové struktury;
mez počtu převratů se nevydává za stejnou mez elementárního
výpočetního času.

## P0620: sudé n a jediný cyklus před i po prvním kroku

Pro kladné obrácené pořadí n,n−1,…,1 kontrahujme každou
šedou hranu kR—(k+1)L do vrcholu k,0≤k≤n.
Černé hrany tvoří neorientované dvojice

    k—(k−2) pro2≤k≤n,   0—(n−1),   1—n.

Při sudém n první skupina vytvoří dvě cesty:
0,2,…,n a1,3,…,n−1. Poslední dvě hrany je spojí v jediný
cyklus, tedy původní střídavý graf má c=1.
Všechna znaménka jsou kladná, proto žádný první převrat
nemůže tento cyklus rozdělit. Dva řezy jsou nutně v témže
cyklu, takže jej také nespojí s jiným: po prvním kroku je
stále přesně jeden cyklus, jak tvrdí kniha.

K cílovým n+1 cyklům je po tomto prvním kroku třeba ještě
alespoň n převratů. Dolní mez n+1 spolu s A_n dokazuje
rovnost. Důkaz platí již pro n=2; požadované sudé n>3
jsou tím pokryty.

## P0621: liché n>3, dva oddělené sudé obrácené bloky

Pro permutaci2,1,3,n,n−1,…,4, kde n≥5 je liché,
tvoří první obrácený blok délky2 a poslední obrácený blok
délky n−3 dva samostatné střídavé cykly.
První cyklus používá kontrahované šedé vrcholy0,1,2,
druhý3,4,…,n. Pro každý jde o předchozí sudou konstrukci
s vlastními dvěma hranicemi; tyto množiny pokrývají všechny
vrcholy. Je tedy c=2 a potřebný přírůstek cyklů n−1.

Označme v libovolném řešení počty kroků měnících c o+1,0,−1
jako p,z,q. Pak p−q=n−1 a celková délka je

    p+z+q = n−1+z+2q.

Jestliže kdykoli dojde ke spojení dvou cyklů (q≥1),
délka je alespoň n+1.
Jestliže ke spojení nedojde, každý převrat má obě hranice
uvnitř téhož původního bloku: cykly se pouze dělí nebo
zůstávají v jeho fyzickém intervalu. První blok zaujímá
pozice1–2, druhý4–n; gen3 mezi nimi se nepřesune.
Tato vlastnost se zachovává po každém takovém kroku.

Oba bloky jsou zpočátku kladné a nesetříděné. První převrat
uvnitř každého z nich musí mít změnu0, protože dosud nedotčený
kladný cyklus nemá opačně orientované černé hrany. Oba bloky
se přitom musí změnit, aby vznikla identita. Proto z≥2,
opět délka≥n+1. S A_n jde o přesnou rovnost.

Podmínka n>3 je potřebná, aby druhý blok měl kladnou sudou
délku alespoň2. Nevyvozujeme odtud chybný případ n=3.
Všechny požadované sudé a liché velikosti jsou pokryté,
bez enumerace vzdáleností a bez externího algoritmu.

