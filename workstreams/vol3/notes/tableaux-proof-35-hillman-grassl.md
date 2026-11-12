# Tableaux35: úplná Hillmanova–Grasslova bijekce

Zadání69/file80, odpověď612–613/file623–624. Původní sazba byla
zobrazena. Použit je opravený Algorithm H: před rozhodováním o pohybu
se musí v H4 zvýšit p_lk o1; pohyb je H5 a vrací se do H4.
Tato známá oprava z1.1.2006 je zobrazená v
images/tableaux-errata-answers33-35-file029.png. Není novým nálezem.

Tvar λ je konečný, řádky indexujeme shora, sloupce zleva;
h_j=λ′_j značí v této poznámce výšku sloupce (nikoli délku háčku).
Délku háčku píšeme H_ij=λ_i−j+h_j−i+1. Vstup p má nezáporné
celé položky, slabě rostoucí doprava i dolů. N=|λ| a M=Σp_ij.
Pořadí cest, oba směry inverze a cena níže mají vlastní argument;
nejsou převzaty z krátkého ujištění v tištěné odpovědi.

## P0562: celý invariant algoritmu G, včetně nezápornosti

G vybere nejlevější sloupec j s nenulovou spodní položkou p_(h_j,j).
Všechny sloupce vlevo jsou díky slabému růstu a nezápornosti nulové.
Cesta začíná v(h_j,j). V aktuální buňce sníží hodnotu o1; pokud
pak hodnota nad ní převyšuje novou hodnotu, jde nahoru. Jinak jde
doprava, pokud buňka existuje, a jinak skončí na pravém okraji.

Před prvním snížením je hodnota kladná a případná levá sousední
hodnota0 je striktně menší. Udržujme následující invariant:
před snížením buňky c s hodnotou v>0 je vlevo nejvýše v−1,
napravo nejméně v, nahoře nejvýše v a dole nejméně v−1.
Jediná možná již existující porušená relace je c>dole, když jsme
přišli zespodu. Po snížení c na v−1 je tato relace opravena;
všechny ostatní vztahy zůstávají platné kromě možného vztahu
nahoře>c. Ten nastane právě při horní hodnotě v.

Při pohybu nahoru je další zpracovaná hodnota opět v>0. Její levý
soused je nejvýše levý soused právě snížené buňky (svislá relace
mimo jedinou poruchu), a ten je nejvýše v−1. Dolní soused už má
v−1; ostatní potřebné relace jsou neporušené. Invariant se zachová.
Při pohybu doprava už horní porucha neexistuje, takže celé pole
je opět uspořádané. Pravý soused však měl před snížením hodnotu
nejméně v, zatímco právě zpracovaná buňka má v−1: levá ostrá
nerovnost pro nový krok je tedy zaručena a jeho hodnota je kladná.

Každý krok proto odečítá1 od kladné hodnoty a nemůže vytvořit
záporný prvek. Při ukončení cesty není porušená ani horní relace,
takže výsledkem je znovu reverse plane partition.

## P0563: konec cesty, délka háčku, hmotnost a ukončení G

Cesta jde jen nahoru a doprava, každou buňku navštíví nejvýše
jednou a končí v nějakém(i,λ_i). Její začátek je(h_j,j), takže
počet navštívených buněk je

    (h_j−i)+(λ_i−j)+1=H_ij.

G5 zvyšuje právě q_ij. Jedna cesta tedy sníží Σp oH_ij a zvýší
ΣH_ij q_ij o stejnou hodnotu. Zachovává se přesně

    M=Σp_ij+ΣH_ij q_ij.                                 (1)

Každá cesta sníží nezáporný součet alespoň o1, a tak jich může být
nejvýše M. Nulový sloupec už se po odečítání nemůže stát nenulovým,
proto je i scan j konečný a monotónní. G zastaví právě tehdy,
když jsou všechny spodní položky nulové, a tudíž je celé p nulové.
Rovnice(1) pak dává požadovanou váženou rovnici pro q.

## P0564: proč G plní q zleva doprava a zdola nahoru

V jednom sloupci k tvoří buňky jedné cesty svislý interval řádků
r_k,…,s_k, kde s_k je vstupní řádek a r_k výstupní řádek.
Jejich hodnoty před odečítáním jsou všechny stejné: každý krok
nahoru byl vynucen právě rovností horní hodnoty s původní dolní.
Po cestě jsou tedy všechny tyto hodnoty o1 menší a stále stejné.

Vezměme dvě po sobě jdoucí cesty začínající ve stejném j.
Druhá začíná opět v h_j. V prvním sloupci musí projít celý
předchozí konstantní interval a případně pokračuje výše, tedy
r′_j≤r_j. V dalším sloupci má vstupní řádek s′_k≤s_k.
Je-li již s′_k≤r_k, je výstupní řádek také≤r_k. Jinak leží
v předchozím konstantním intervalu, jímž musí vystoupat alespoň
do r_k. Indukcí platí r′_k≤r_k v každém společném sloupci.

Druhá cesta nemůže skončit před posledním sloupcem první:
jestliže první z řádku r_k ještě pokračovala doprava, pak
λ_(r_k)≥k+1, a pro r′_k≤r_k platí totéž. Nakonec tedy druhá
končí ve stejném nebo vyšším řádku než první. Sloupce j rostou,
a uvnitř stejného j indexy koncových řádků i slabě klesají.
To je přesné pořadí aktualizací q, včetně opakování stejné buňky.

## P0565: opravený H a jeho samostatný invariant

H začíná nulovým polem p a zpracovává buňky q po sloupcích zprava
doleva, uvnitř sloupce shora dolů. Dokud je q_ij>0, sníží je o1,
začne v(i,λ_i) a provede tuto cestu: zvýší aktuální p_lk o1;
pokud je pak větší než existující dolní soused, jde dolů.
Jinak jde doleva, je-li k>j; při k=j a bez dolní poruchy skončí.

Je to přesný opravený H3–H5, nikoli jiná varianta algoritmu.
Před zvýšením buňky s hodnotou v je případný pravý soused nejméně
v+1, levý nejvýše v, dolní nejméně v a horní nejvýše v+1.
Jediná možná již existující porucha je nahoře>aktuální, po příchodu
shora. Zvýšení na v+1 ji opraví; jediná nová možná porucha je
aktuální>dole, a nastává právě při dolní hodnotě v.

Na začátku je buňka na pravém konci řádku, takže pravá podmínka
je prázdná. Při pohybu dolů je další hodnota v a její pravý soused
je nejméně pravý soused právě zvýšené buňky, tedy≥v+1. Při pohybu
doleva je vpravo právě zvýšená hodnota, striktně větší než dřívější
levý soused. Ostatní relace se přenášejí stejně jako v P0562.
Invariant tedy platí a po dokončení cesty je celé p opět slabě
rostoucí a nezáporné. Cesta je konečná: jde jen dolů a doleva.

## P0566: každá cesta H opravdu skončí na dně určeného sloupce

Před prvním vkládáním pro daný j jsou všechny sloupce≤j nulové:
dřívější cesty zpracovávaly sloupce>j a nikdy nešly dále vlevo
než do svého cílového sloupce. Při prvním vstupu do j tedy hodnota0
vzroste na1 a vynutí pohyb dolů přes všechny zbývající nulové
buňky až do(h_j,j).

U dalších cest stejného j startují řádky i′≥i, protože H prochází
q shora dolů. Ukážeme, že další cesta leží stejně nízko nebo níže
než předchozí. V každém sloupci měla předchozí cesta interval
s_k,…,r_k se stejnými původními hodnotami; po zvýšení jsou opět
stejné. Pokud nová cesta vstoupí v s′_k≥s_k, buď už je pod r_k,
nebo musí v tomto konstantním intervalu sestoupit alespoň do r_k.
Její výstupní řádek tedy splňuje r′_k≥r_k a tvrzení se přenese
do dalšího sloupce vlevo.

Zbývá doložit první vstupní nerovnost, neboť nové začátky mohou
mít různé pravé konce. Nechť nový první sloupec je L′=λ_(i′).
Má-li předchozí cesta stejný první sloupec, vstupovala v i≤i′.
Měla-li širší začátek, vstoupila do L′ z L′+1 v nějakém řádku u
s λ_u≥L′+1. Proto u<i′, neboť λ_(i′)=L′ a délky slabě klesají.
V obou případech začíná nový vstup alespoň tak nízko jako starý.

Indukce se tedy vztahuje na všechny sloupce od L′ do j. V j už
předchozí cesta končila v h_j; další skončí nejméně tak nízko,
a tudíž také právě v h_j. Každá cesta H pro q_ij proto zvýší
přesně H_ij buněk a končí tam, kde G musí začínat.

## P0567: H vrátí každou jednotlivou cestu G a celé původní p

Nechť G odečetl cestu γ od(h_j,j) do(i,λ_i). Z výsledného p
spusťme H pro buňku(i,j) a cestu sledujme pozpátku. Po zvýšení
aktuální buňky je její původní hodnota obnovena.

Přišel-li G do této buňky zespodu, byly obě původní hodnoty stejné.
Dolní buňka ještě zůstává snížená o1; H tedy zjistí ostrou dolní
poruchu a správně jde dolů. Přišel-li G zleva, buňka pod aktuální
buňkou nebyla na γ: jde o první vstup γ do tohoto sloupce a
pozdější kroky jsou jen nahoru/doprava. Její hodnota tedy nebyla
změněna a je nejméně původní aktuální hodnota. H nejde dolů,
ale správně doleva. Na původním začátku(h_j,j) už neexistuje dolní
buňka a levý pohyb je zakázán, takže H končí.

H tak obrátí celou γ po buňkách. Pořadí P0564 je přesně opačné
k pořadí H. Z agregovaných q je seznam koncových buněk G proto
jednoznačně určen; opakované aktualizace téže buňky jsou stejné
položky seznamu. Indukcí zpět přes všechny cesty H(G(p))=p.
To samo zatím dokazuje injektivitu G, nikoli ještě úplnou surjektivitu.

## P0568: opačný směr pro libovolné q a skutečná bijekce

Vezměme libovolné nezáporné celé q a poslední cestu, kterou pro ně
provedl H. Má parametry(i,j), začátek(i,λ_i) a podle P0566 konec
(h_j,j). Ve výsledném p jsou sloupce<j nulové a spodní hodnota
v j je kladná, takže G opravdu zvolí právě tento j.

Sledujme cestu H zpětně. Po odečtení1 v aktuální buňce G obnoví
její původní hodnotu. Přišel-li H zeshora, byly původní hodnoty
stejné, horní buňka je dosud zvýšená o1 a G jde správně nahoru.
Přišel-li H zprava, buňka nad aktuální buňkou neležela na cestě H
(jde o první vstup do tohoto sloupce, ostatní kroky jsou dolů/vlevo).
Její nezměněná hodnota je nejvýše původní aktuální hodnota; G tedy
nejde nahoru, ale doprava. Na počáteční buňce H už horní porucha
neexistuje a napravo žádná buňka není, takže G skončí právě v(i,λ_i).

Obnoví se pole před posledním vkládáním a do q se vrátí právě
jedna jednotka v(i,j). Indukcí přes předchozí cesty G(H(q))=q.
Spolu s P0567 to dokazuje obě inverze na celých oborech.
Počet buněk každé cesty dokazuje, že se přesně přiřazují reverse
plane partitions součtu M a všechna q s ΣH_ij q_ij=M.

## P0569: nulové případy, terminace H a cena

Pro nulové p jsou všechna q nulová; pro nulová q se nic nevloží.
Jednobuňkový tvar má H_11=1 a oba algoritmy jen převádějí p_11
na q_11 a zpět. Prázdný tvar má jedinou prázdnou konfiguraci
součtu0; jako obvykle jde o prázdnou větev před inicializací,
která jinak odkazuje na první řádek/sloupec.

H sníží součet q o1 při každé cestě a všechny q zůstávají
nezáporné. Celkem tedy provede přesně Σq_ij cest a
ΣH_ij q_ij=M zvýšení p. G provede přesně M snížení p;
neopakujeme žádný předchozí výčet, jde o důsledek invariantu(1).

Inicializace a úplné scany buněk stojí O(N); G prochází počáteční
sloupce jen doprava a H buňky q jen v pevném pořadí. Jedna jednotková
změna p potřebuje nejvýše konstantně mnoho sousedních testů, cesta
navíc jednu změnu q a cest je nejvýše M. Oba algoritmy tedy používají
O(N+M) aritmetických operací a porovnání a O(N) buněk pro pole.
U celých hodnot s neomezenou bitovou délkou se z toho bez dalšího
nevyvozuje jednotková bitová cena operace.

Úplný původní článek Hillman–Grassl1976 a jeho historická priorita
nebyly bibliograficky přezkoumány. Výše je celý potřebný obecný
důkaz bez externí věty, bez numerického běhu a bez nového nálezu.
