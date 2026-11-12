# Tableaux42: pět převratů a všechny první možnosti

Zadání72/file83, odpovědi614–615/file625–626, sazba zobrazená.
Znaménko minus označuje obrácenou orientaci genu; R[a,b] obrátí
pořadí úseku a zároveň všechna jeho znaménka. Nejde o nepodepsané
reversals. Kontrola je ruční, bez prohledávání permutací.

## P0606: přesný graf a koncové vrcholy

Každý gen k má dva konce kL,kR. V kladné orientaci jdeme
zleva kL→kR, v záporné kR→kL. Přidáme pevné konce0R,(n+1)L.
Černé hrany spojují sousední konce v aktuálním uspořádání,
šedé hrany jsou kR—(k+1)L pro0≤k≤n.
Každý vrchol má právě jednu hranu každé barvy; jejich sjednocení
je tedy disjunktní sjednocení střídavých sudých cyklů.
Shodná černá/šedá dvojice je platný2-cyklus, nikoli odstraněná
paralelní hrana. Cíl má n+1 takových cyklů.

Černé hrany budeme orientovat fyzicky zleva doprava podél
aktuální posloupnosti. Převrat mění pouze dvě hranice úseku.
Pro hranice(L_a,R_a),(L_b,R_b) nahradí hrany dvojicemi
(L_a,L_b),(R_a,R_b); všechny vnitřní neorientované hrany zachová.

## P0607: změna počtu cyklů i kritérium zvýšení

Jsou-li obě vybrané černé hrany v různých cyklech, jejich
odstraněním vzniknou dvě cesty a nové hrany je spojí v jeden
cyklus: změna je−1.
Jsou-li ve stejném cyklu, vzniknou po odstranění dvě cesty.
Nové hrany je buď znovu spojí do jednoho cyklu, nebo každou
uzavřou zvlášť: změna je0 nebo+1. Žádný jiný cyklus se nemění.

Při průchodu jedním cyklem zvolme orientaci a u každé jeho
černé hrany zaznamenejme, zda se prochází ve fyzickém směru
zleva doprava. Dvě vybrané hrany rozdělí cyklus právě tehdy,
když tato znaménka jsou opačná: zbylé cesty pak mají konce
R_a,R_b a L_b,L_a, které nové hrany jednotlivě uzavřou.
Při stejných směrech mají cesty konce R_a,L_b a R_b,L_a,
takže se znovu propojí.

Z počátečního c cyklů je proto třeba nejméně n+1−c převratů.
Dosáhne-li posloupnost přesně této délky, každý její krok
musí zvýšit počet cyklů o1. Zejména nesmí přerušit již hotovou
2-cyklovou sousednost: její jediná černá hrana by se musela
spojit s hranou jiného cyklu a počet by naopak klesl.

## P0608: všechny hrany a tři knižní cykly

Pro S=[−7,1,2,4,5,3,−6] jsou fyzicky orientované černé hrany

    b0:0R→7R, b1:7L→1L, b2:1R→2L, b3:2R→4L,
    b4:4R→5L, b5:5R→3L, b6:3R→6R, b7:6L→8L.

Střídání s šedými dává přesně

    (0R,1L,7L,6R,3R,4L,2R,3L,5R,6L,8L,7R),
    (1R,2L), (4R,5L).

Všechny vrcholy se objeví právě jednou. Je c=3 a cílových
cyklů8, tedy dolní mez5. Dvě hotové sousednosti jsou1,2 a4,5.

## P0609: proč právě pět vytištěných prvních kroků

V uvedeném pořadí velkého cyklu mají černé hrany
b1,b6,b3,b5,b0 směr−, kdežto b7 směr+.
Abychom mohli dosáhnout cíle pěti kroky, první krok musí
rozdělit tento cyklus (P0607), tedy musí přerušit b7 a právě
jednu z pěti opačně orientovaných hran. Tím je doloženo
„musí přerušit6L—8L“ i úplnost pěti možností:

| Řez a převrat v S | Výsledný stav |
|---|---|
|b1,b7: R[2,7]|A=[−7,6,−3,−5,−4,−2,−1]|
|b6,b7: R[7,7]|B=[−7,1,2,4,5,3,6]|
|b3,b7: R[4,7]|C=[−7,1,2,6,−3,−5,−4]|
|b5,b7: R[6,7]|D=[−7,1,2,4,5,6,−3]|
|b0,b7: R[1,7]|E=[6,−3,−5,−4,−2,−1,7]|

Řez některé z hotových hran b2,b4 by cykly spojil, a proto
nemůže být počátkem optimálního pětikrokového řešení.

## P0610: čtyři konkrétní dokončení bez enumerace

Označme tři společné mezistavy

    T=[1,2,4,5,3,−6,7],
    U=[1,2,6,−3,−5,−4,7],
    V=[1,2,3,−6,−5,−4,7].

Platí T —R[3,6]→ U —R[3,4]→ V —R[4,6]→ [1,2,3,4,5,6,7].
Všechny čtyři požadované větve se dokončí takto:

- A —R[1,7]→ T, pak uvedené tři kroky.
- E —R[1,6]→ T, pak stejné tři kroky.
- C —R[1,7]→ [4,5,3,−6,−2,−1,7]
  —R[1,6]→ U, pak poslední dva kroky.
- D —R[1,7]→ [3,−6,−5,−4,−2,−1,7]
  —R[1,6]→ [1,2,4,5,6,−3,7]
  —R[3,6]→ V —R[4,6]→ cíl.

Každá větev má právě4 další převraty. S P0608 to dokazuje
přesnou vzdálenost5 v obou směrech: převrat je svou vlastní
inverzí, takže lze celé řešení obrátit.

## P0611: proč druhou možnost nelze dokončit čtyřmi kroky

Po prvním kroku má B čtyři cykly. Čtyřkrokové dokončení
by tedy muselo každý cyklus pouze rozdělovat a nikdy nepřerušit
hotové sousednosti1,2 a4,5. Smíme je sloučit do jediných bloků.
Přejmenujme bloky(1,2),3,(4,5),6,7 jako1,2,3,4,5.
Pak B přejde na [−5,1,3,2,4], cíl na[1,2,3,4,5].
Kontrakce sníží počet genů i cyklů o2; potřebný přírůstek4
se nezmění a každý dovolený převrat respektuje celé bloky.

V tomto zmenšeném stavu jsou dva netriviální cykly

    C1=(0R,1L,5L,4R,6L,5R),
    C2=(1R,2L,3R,4L,2R,3L).

Černé hrany C2 mají při tomto průchodu všechny stejný směr.
V C1 je hrana4R→6L opačně orientovaná než0R→5R a5L→1L.
Jediné kroky zvyšující počet cyklů jsou proto

    R[1,5] → X=[−4,−2,−3,−1,5],
    R[2,5] → Z=[−5,−4,−2,−3,−1].

V X je hotová poslední hranice5R—6L, v Z je hotová sousednost
5L—4R. Cyklus C2 má v obou případech stále všechny tři černé
hrany ve stejném směru: celý příslušný vnitřní úsek se obrátil
najednou. Druhý netriviální cyklus má jen dvě opačně orientované
černé hrany. Jediné další rozdělení je R[1,4] v X, respektive
R[1,5] v Z. Obě dávají

    Y=[1,3,2,4,5].

V Y zůstal C2 se všemi směry stejnými, ostatní cykly jsou
hotové2-cykly. Žádný následující převrat již počet cyklů nezvýší,
zatímco pro domnělé čtyřkrokové dokončení musí zbývající dva
kroky přidat dva cykly. Spor. Větev B tedy opravdu potřebuje
více než čtyři další kroky. Důkaz prošel jen vynucené řezy,
nikoli všechny permutace nebo všechny krátké posloupnosti.

## P0612–0613: dvě odlišné početní informace

Celkový počet uspořádání je2^7·7!=128·5040=645120:
pořadí všech různých genů a jejich sedm znamének lze volit
nezávisle. To je obecný argument i přesná aritmetika P0612.

P0613 zůstává partial: knižní číslo179904 pro počet stavů
ve vzdálenosti≤5 nebylo nezávisle reprodukováno.
Jde o výslovně vynechaný rozsáhlý census podle uživatelského
pokynu; nezahájil se BFS ani enumerace všech645120 stavů.
Důkaz vzdálenosti konkrétního S toto číslo nepotvrzuje.
Nevzniká z něj podezření ani nález.

## P0614–0615: historický model a aktuální algoritmická poznámka

Primární [Bafna–Pevzner1993](https://www.cs.sjsu.edu/faculty/khuri/HUT_2008/Bafna_1993.pdf),
tištěná149, výslovně převádí obrázek Lobelia na podepsanou
permutaci(−7,+1,+2,+4,+5,+3,−6,+8). Poslední pevný blok8
je v knižní úloze pravá hranice. Zdroj tím potvrzuje stejný
abstraktní model; vlastní biologické mapování celého chloroplastu
Knox–Downie–Palmer1993 se znovu nezkoumalo. Nejde o tvrzení,
že skutečná evoluce musela proběhnout vybranou optimální cestou.

Známá změna2001 aktualizuje Kececioglu–Sankoff na
Algorithmica13(1995),180–210. Změna2008 nahrazuje poznámku
na615 přesnými novějšími odkazy a mezí O(n^(3/2)√(log n)).
Primární [Tannier–Bergeron–Sagot2007](https://pbil.univ-lyon1.fr/members/sagot/htdocs/publications/tannier2007_dam.pdf),
881–882, vymezuje přesně tento problém: nalezení celé
nejkratší posloupnosti podepsaných převratů, ne pouze vzdálenosti.
Uvádí deterministickou mez O(n^(3/2)√(log n)); její celý
důkaz zde není samostatně odvozen, jde o externí výsledek.

Zdroj také rozlišuje dřívější Kaplan–Verbinův náhodný postup,
jehož úspěch není zaručen na každé permutaci, od nové zaručené
varianty. V evidenci tuto kvalifikaci zachováváme; výsledná
existence algoritmu s uvedenou mezí je doložena druhým pramenem.
Historická prvenství a celé důkazy všech postupně nahrazených
algoritmů nejsou tímto rychlým bibliografickým ověřením
samostatně certifikovány. Matematické kroky P0606–0612 jsou
nezávislé na těchto externích algoritmech.

