# Souvislá revize úvodu ke stromům — 5. listopadu 2026

X0969: celé originály 308–318 a odpovědi 560–564 přečteny, s výjimkou
navazujících odpovědí §2.3.1 na564, které patří do příštího bloku.
Definice a první reprezentace §2.3.1 na318 už byly přečteny. Přijaty a
znovu logicky prověřeny obecné důkazy `parallel/tree-traversal/notes/intro-proofs.md`
a rozbor nekonečných úrovní; přečteny pozdější kořenové revize včetně
genealogie X0905. Žádné úspěšné výpočty se neopakovaly.

## Definice a konečné konstrukce

Indukce podle počtu uzlů skutečně zajišťuje jedinečnost rodiče i cesty
ke kořeni. Pořadí sourozenců je dodatečný údaj; binární levý/pravý slot
není totéž jako obecný strom s nejvýše dvěma dětmi. Prázdný binární strom
je výslovně přípustný. Obrázky15–17 zachovávají stejné rodičovské hrany,
ale15/16 různé pořadí; obrázky19/20 spolu souhlasí v hranách, závorkách
i odsazení. Fig.21 správně reprezentuje oba podíly uvnitř násobeného
součtu a vnější odčítání. Fig.22 odpovídá skutečnému členění kapitoly2.

Deweyho zápis má jednoznačný rodičovský prefix a uspořádané děti.
`F[a,b,...]` označuje podles dětí daného uzlu; není to samotný uzel
s danou adresou. Proto je parent(F[1,2,2])=E v úloze17 správně.
Listy mají konečné posloupnosti odkazů, které se smějí sdílet a cyklit;
nekonečné rozvinutí Listu se nesměšuje s konečnou stromovou definicí.
Všechna zobrazená vnoření a hvězdičky definující podseznamy souhlasí.

Pro tři označené uzly jsou3 volby kořene a4 uspořádané struktury,
tedy12 stromů; bez pořadí jsou3 na kořen, tedy9. Příbuzenské vzorce
určuje nejbližší společný předek: vzdálenosti q,r dávají m=q−1,n=r−q.
Konvence exponentu−1 pokrývá předka i totožný uzel; neexistující rodiče
nad kořenem se neztotožňují. Čtyři děti při třech sourozencích jsou správně.

Konečná vnořená kolekce neprázdných množin dává neuspořádaný les svými
maximálními množinami a jejich maximálními vlastními podmnožinami.
Jediný maximální prvek dává strom. Obdobně konečný poset dává les právě
tehdy, když horní množina každého prvku je řetězec; minimální větší prvek
je rodičem. Konečnost nelze vypustit bez další definice. Úloha14 zaručuje
prefixovou uzavřenost a žádné mezery mezi sourozenci. Opravená odpověď13
vede od úplné adresy ke kořeni, jak se ptá zadání; první dotisk má opačný
směr. Binární adresy odpovědi15 jsou jednoznačné a skutečně dávají obě
pozice ChristianaIX, 10000 a110010.

Výrazové stromy16 zachovávají pořadí operandů; alternativní asociace
součtu jsou matematické, neslibují shodné zaokrouhlování každého stroje.
V18 je výsledkem List(2), nikoli atom2; index do prázdného Listu není
definován. Cyklus19 dává L[2]=(L) a L[2,1,1]=a. Přidání vnějších listů
binárního stromu dává0–2 strom s2n+1 uzly včetně n=0. Rovnost počtu hran
N−1=Σk*n_k dává n_0=1+Σ(k−1)n_k bez dalších předpokladů o stupních.

## Nekonečné stromy: co je a není uzavřeno

Relace X≡Y, pokud nějaké Z obsahuje X∪Y, je ekvivalence: při tranzitivitě
mají oba obaly neprázdný průnik, a tedy jeden obsahuje druhý. Definice
stupně počtem komponent potomků dovoluje komponentu bez nejvyššího uzlu.
Tím se stupeň může lišit od počtu bezprostředních dětí.

Příklad11(a) fixuje desetinné číslice mimo násobky2^k. S jednoznačnou
desetinnou reprezentací vznikají úrovně0,1,... a v každém kroku kontinuum
větví. Dyadická konstrukce11(b),(c) je rovněž vnořená, všechny stupně jsou2
a každý uzel má kontinuum předků. Doslovná funkce `level=|ancestors|`
však nabývá jen jediné hodnoty c: u T[a] je předků c, u S[a,m,n] je jich
c+n=c. **C0045 zůstává candidate**, protože „nespočetně mnoho úrovní“
může být míněno jako nespočetná délka hierarchie. Výpočet je určitý,
redakční význam formulace nikoli. Neřešíme jej pouhým přejmenováním
kardinálu na ordinál, neboť předkové v hustém řetězci nejsou dobře uspořádáni.

**C0056 zůstává confirmed**: navazující poznámka o dobrém uspořádání
chce nespočetnou úroveň u každého uzlu. Nejmenší použitý index a0 má
koncový úsek T[a0] bez vlastního předka, tedy úroveň0. Žádný dyadický
svislý úsek jej neobsahuje; dalších použitých indexů je stále nespočetně.
Tento rozpor nevyužívá terminologickou nejistotu C0045. Konstrukce s
indexy R×Z a uzavřenými počátečními úseky má naopak přesně dvě děti
a kontinuum předků všude; není to dobré uspořádání. Všechny její úrovně
jsou opět c, takže tím neuzavíráme původní formulaci11(c).

Úloha11 proto zůstává partial. Osobní připsání Bigelowovi výslovně
přeskakujeme; samotné chybějící autorství není matematická mezera.

## Kreslení a prameny

Půlení delší strany obdélníku poměru√2 a rotace dávají podobný obdélník
s poloviční plochou. Indukce přesně vytváří kresbu22 a oba její obrázky;
vnější obdélníčky jsou prázdné sloty rozšířeného stromu. Nejde o tvrzení
nekonečného fyzického rozlišení papíru.

Přímo obrazově znovu přečteny všechny tři strany46–48 původního
Brent–Kung1980 v lokálním autorském PDF. H-rozložení má plochu O(n),
zatímco obvyklé má O(n log n), v modelu jednotkově vzdálených uzlů
a vodičů jednotkové šířky. Dolní mezΩ(n) plyne už z balení uzlů; alternativně
z jednotkových hran při pevném počtu vrstev. „Most efficient“ na563 lze
číst asymptoticky pro plochu bez požadavku všech listů na okraji. Článek
výslovně odlišuje konvexní hranici s listy na ní, kde je potřebaΘ(n log n).
Neprohlašujeme optimální konstanty ani všechny technologické modely.

Převzaty přesně vymezené primární doklady Galtonovy binární notace na249
a literární shody Fig.18(b) s Genesis10:1–25; nejde o ověření historické
existence biblických osob. Fig.18(a) přímo porovnána s přijatým záznamem
X0905:63 pozic,62 rodičovských hran, včetně opakovaných rodinných rolí.
Zachovány meze odborných genealogických záznamů, transkripce pamětí
a autorizovaného přetisku; netvrdíme čtení všech matrik ani genetické ověření.

Přesné Burke1959 a GHdA Fürstliche HäuserI1951 nebyly získány ani nově
čteny. Jejich kolace je nyní bibliografickou výjimkou, nikoli překážkou
již doložených rodičovských vazeb. Gotha1871 byl dříve přímo čten v X0905.
Na311 zůstává neověřený autorův průzkum „více než80 procent“ a dvouletá
historie vlastní kreslicí konvence; bez jeho vzorku to nepřepočítáme.
Hlavní text proto zůstává partial právě pro toto empirické tvrzení.

## Mapa a errata

Čtyři vrstvy z5. listopadu prohledány po úplných stránkových blocích.
V úvodu jsou věcné známé opravy Meschech→Meshech na310 a obrácená cesta
v odpovědi13 na562. Oprava0→∅ na561 je notace; přejmenování F na Z,
kurzíva, slovosled a doplnění rozlišení vlastních předků jsou evidovány
bez nové matematické chyby. Změna Charles→CharlesIII z2022 je dobová
aktualizace a nedokládá chybu znění roku1997.

C0045 iC0056 lokalizovány na562, s přesným vysvětlením statusu v anglickém
UI. Celé stránky308–310,312–316,318,560–561 a563 jsou nyní pokryty
(červená310 zůstává známou opravou). Stránky311,317,562 zůstávají partial
kvůli uvedenému průzkumu či neuzavřené úloze11;562 je současně červená
kvůli doloženému C0056. Stránka564 čeká na dokončení průchodových odpovědí.
Nový nález ani nové testy nepřibyly; pokračuje §2.3.1 od319.
