# Úlohy56–57: obecná rekurence, všechny obrázky a omezení výkladu

Zadání56 na p118–119/file133–134 a odpověď p171/file186
byly zobrazeny, včetně původního výřezu formule zatáček
`images/file-134-turn-definition.png`. Všechny nativní cesty
sedmi polygonů jsou ověřeny v
`results/twindragons56-subpicture57.json`; samostatný cache
jejich již hotové geometrie je `twindragons56-native-cache.json`.
`check_twindragons56_subpicture57.py` byl spuštěn nice15.
Neprovádí census labelings; matice počítají přesně a úplně.

## E56-1 — přesně vymezená konvence symbolu

Původní zadání požaduje symbol(−1/k) pro všechna k včetně
sudých a k=1. Citovaná úloha4.5.4–23 ve svazku2 na p413
definuje Jacobiho symbol pouze pro kladný lichý jmenovatel>1;
její původní sazba `workstreams/vol2/images/vol2-p413.png`
byla přímo zobrazena. Již uzavřený důkaz
`workstreams/vol2/notes/primality-jacobi.md` dává pro liché u
hodnotu(−1/u)=(−1)^((u−1)/2) po rozšíření čitatele periodicitou.

Pro následující konkrétní výpočet definujeme výslovně

    χ(k)=+1, pokud lichá část k je1 mod4,
    χ(k)=−1, pokud lichá část k je3 mod4.

Tedy χ(2k)=χ(k),χ(1)=1. Na původně definovaných lichých
jmenovatelích tato hodnota přesně souhlasí s citovaným
Jacobiho symbolem. Je to výslovný předpoklad interpretace
pro sudé k, nikoli definice dodatečně připsaná původnímu
svazku2. Všechny níže uvedené nativní obrázky i celá
odpověď56 odpovídají právě této interpretaci. Zda ji kniha
míní jako implicitní rozšíření svého symbolu, zůstává
**partial**, bez nové karty nálezu. Položka119 v úplných
erratech se týká62 a tuto konvenci neřeší.

## E56-2 — od zatáček k celé slovní rekurenci

Nechť D_n je slovo písmen A/B pro χ(1),…,χ(2^n−1),
kde A znamená pravou zatáčku(+1), B levou(−1). Prázdné
D0 má délku0. Pro 1≤k<2^n pišme k=2^e u s lichým u.
Liché části2^n+k a2^n−k jsou2^(n−e)+u a2^(n−e)−u.
Pokud n−e≥2, jsou modulo4 opačné, takže mají opačná χ.
Pokud n−e=1, nutně k=2^(n−1); liché části jsou3 a1,
opět opačná χ. Současně χ(2^n)=1. Proto přesně

    D_(n+1)=D_n A complement(reverse(D_n)).

Tím jsou dokázána všechna písmena, ne pouze délka či součet
zatáček. Základ a první tři slova jsou
D0=empty,D1=A,D2=AAB,D3=AABAABB, přesně jako v odpovědi.
Indukcí délka D_n=2^n−1. Zadání předepisuje dvě stejné
poloviny, takže celé cyklické slovo T_n je

    (D_(n−1) A)(D_(n−1) A)

a má přesně2^n junctions. Pravá/levá zatáčka na hodinově
orientovaném jednoduchém obvodu odpovídá V/Λ z50, a tedy
A/B z55. Počet řešení závisí na tomto slovu, nikoli na
délkách jednotlivých čar či konkrétních nenulových úhlech.

## E56-3 — každý bod všech sedmi původních polygonů

Nativní cesty135–141 na file133 jsou postupně T2–T8.
Každá byla přenesena na svou přesnou racionální mřížku;
největší chyba bodu je menší než0.01pt. U každé cesty jsou
ověřeny všechny dvojice segmentů a všechna pořadí sousedů:
žádné nechtěné křížení, žádné další junctions, každý
junction je nekolineární V, dvě stěny včetně vnější.
Počty bodů i čar jsou jednotlivě4,8,16,32,64,128,256.

Pro každý obrázek je uloženo celé nativní slovo všech
zatáček a porovnáno s celou formulí E56-2. U T2 může
číslování začít v prvním nativním bodě; u T3–T8 se začátek
posune přesně o2vrcholy. Následně souhlasí každá z2^n
zatáček, nikoli jen počty A/B nebo výsledná stopa.
Všechny obrazy tedy skutečně realizují předpoklady55.

Geometrické tvrzení o konvergenci celé rodiny polygonů
k twindragonu z úvodu kapitoly4 se tím samo nedokazuje.
Identifikace této limitní množiny a geometrická konstrukce
pro nevyobrazená n zůstává **partial**. Níže odvozený
počet platí pro každé T_n s právě předepsaným cyklickým
slovem; sedm konkrétních obrázků je pokryto i geometricky.

## E56-4 — slovní operace a každá maticová rovnost

Nyní D_n označuje také součin matic svého slova. Protože
A^T=A a B^T=B, obrácené slovo má matici D_n^T: pořadí
činitelů se při transpozici obrací. Pro X=diag(1,−1)
platí B=XAX a A=XBX. Záměna každého písmene se tedy
vyjádří konjugací celého součinu X D_n X; vnitřní X se
po dvojicích zruší. Obrácení a záměna dohromady jsou
X D_n^T X, takže přesně

    D_(n+1)=D_n A X D_n^T X.

Pro kontrolu základů jsou D1=A,
D2=[[1,−2],[0,−1]], D3=[[1,−1],[−1,0]]=B.
To odpovídá každému ze tří vytištěných slov.

## E56-5 — indukce všech čtyř položek překvapivé formule

Definujme K(t)=[[1,t−1],[−1−t,−t²]]. Základ D3=K(0)
byl právě přesně vypočten. Pro libovolné celé t≥0 nejprve

    K(t) A X = [ t,−1 ; −t²−t−1,t+1 ].

Násobením K(t)^T X získáme jednotlivě položky
1,t,−t−2,−(t+1)²: první je t−(t−1), druhá
−[−t(t+1)+t²]=t, třetí−t²−t−1+(t+1)(t−1),
čtvrtá−[(t²+t+1)(t+1)−t²(t+1)]. Tedy

    K(t) A X K(t)^T X = K(t+1).

Indukce tak dokazuje celý tištěný vzorec

    D_(t+3) = [1,t−1; −1−t,−t²]   pro t≥0.

Žádná položka nebyla odhadnuta z OCR ani ze shody několika
počátečních hodnot. Matici v originálefile186 bylo možné
přímo přečíst; zápis−n² je skutečně čtverec n.

## E56-6 — obecná stopa, výjimky n=3 a n=2

Pro n≥4 položíme t=n−4. Poloviční součin je

    H=D_(n−1)A=[t,1; −t²−t−1,−t−1].

Má stopu−1 a determinant1. Pro každou2×2 matici plyne
z rozvinutí čtyř položek trace(H²)=(traceH)²−2detH;
zde tedy trace(H²)=−1. Z55(a), které je nezávislé na
chybném pomocném exponentu55(c), dostáváme

    počet(T_n)=trace(D_(n−1)A D_(n−1)A)+L_(2^n)
               =L_(2^n)−1       pro n≥4.

Pro n=3 nepoužíváme vzorec s nepovoleným t=−1. Přímé
D2A=[−1,1;−1,0] má opět stopu−1,determinant1, a tedy
stejný výsledek L8−1=46. Pro n=2 je D1A=A² se stopou3
a determinantem1; trace(A⁴)=9−2=7, L4=7, takže počet14.
To ověřuje obě závěrečné výjimky tištěné odpovědi zvlášť.

Pro úplnost uložené konkrétní počty pro n=2,…,8 jsou
14,46,2206,4870846,23725150497406,
562882766124611619513723646,
316837008400094222150776738483768236006420971486980606.
Jsou důsledky matice a lineární Lucasovy rekurence, nikoli
nezávislý census, a tak jsou také označeny v certifikátu.

## E57-1 — každá část původního podobrazu

Cesty18–19 na file186 dávají v normalizovaných souřadnicích
vnější konce L=(0,1),R=(6,1), junctions Y=(2,1),V=(4,0),
W=(4,2). Čáry jsou LY,YV,YW,VW,WR. Všechny průsečíky
i lokální determinanty byly ověřeny; jediná tři omezení jsou

    Y=Y(V,W,L),  V=V(W,Y),  W=W(Y,V,R).

Pořadí Y lze cyklicky posunout; zrcadlení se nepoužívá.
Konce L,R jsou záměrně volné konce podobrazu a nemají
vlastní dodatečné omezení. Síť tedy splňuje přesně požadavek
jednoho V, jednoho W a jednoho Y, bez skrytého T.

## E57-2 — úplný dvoupřípadový spor bez prohledávání

Pišme y pro štítek V→W. Jde o prostřední větev W, takže
podle všech tří řádků W musí být y buď+ nebo−.

- Je-li y+, jediný řádek V s první větví+ je +O, takže
  Y→V je příchozí šipka I. Jediný řádek Y začínající I
  je IO−; Y→W proto musí být O, tedy W→Y je I.
  Jenže při prostředním+ má W první větev pouze O nebo−.
  To je spor.
- Je-li y−, jediný řádek V s první větví− je−I, takže
  Y→V je O. Jediný řádek Y začínající O je O−I; čára
  YW proto musí být−. Při prostředním− však jediný řádek
  W je+−+, a nutí tutéž čáru+. Opět spor.

Tím jsou vyloučeny všechny možné štítky prostřední čáry
a tím každý labeling celého podobrazu, bez jakéhokoli
předpokladu na štítky jeho dvou volných konců. Uložená
krátká propagace je dodatečný kontrolovatelný doklad;
vyčerpání dokazuje tento dvoupřípadový argument.

Odkazy na obr.9(d) a obr.8 v Huffmanově článku1971 se
zatím výslovně bibliograficky přeskakují: originál článku
není v lokálních zdrojích. Matematická nemožnost všech
předchozích24–25 i nynější57 již má vlastní plný důkaz.
