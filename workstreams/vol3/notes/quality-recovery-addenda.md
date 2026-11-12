# Doplnění nalezených mezer v evidenci

6. listopadu2026. Bez výpočtového běhu. Navazuje na
quality-recovery-2026-11-06.md; tato doplnění nejsou nové nálezy v knize.

## P0376: třídění pomáhá vyhledávání, s.2

Konkrétní svědek kvalitativního tvrzení: v seřazeném poli hledáme první
index s klíčem≥x. Přidej pouze logické okraje K_0=−∞,K_(N+1)=+∞,
udržuj l<h, K_l<x≤K_h a začni l=0,h=N+1. Pro h−l>1 polož
m=floor((l+h)/2). Při K_m<x nahraď l hodnotou m, jinak h hodnotou m.
Uspořádání vylučuje celý vyřazený úsek; invariant zůstává platný.
Celočíselná délka h−l se zmenšuje nejvýše na svůj horní poloviční
zaokrouhlený podíl. Po nejvýše ceil(log₂(N+1)) porovnáních je délka1.
Je-li h≤N a K_h=x, máme první shodu, jinak x chybí. Prázdné pole,
duplicitní klíče i krajní hledané hodnoty jsou zahrnuty. Předpokládán
přímý přístup do pole; není tvrzen stejně rychlý páskový přístup.

## P0377: Eulerova pomocná rekurence, odpověď5.1.1-14, s.594

Původní sazba images/inversions-file-605.png dává pro n≥1
`s_n=1−z^(2n−1)−z^(3n−1)s_(n+1)`. Pracujeme s formálními řadami
v nezáporných mocninách z. Po k rozvinutích má přenesený faktor
exponent `A_(n,k)=k(3n−1)+3k(k−1)/2`, který jde do nekonečna.
Proto koeficienty určují právě jednu soustavu takových řad a

`s_n=Σ_(k≥0)(−1)^k z^A_(n,k)(1−z^(2(n+k)−1))`.

Dosazením do rekurence se první člen oddělí a zbytek po k→k+1 přesně
souhlasí; existence je tedy také doložena. Pro n=1 první exponent
je k(3k+1)/2, druhý je (k+1)(3(k+1)−1)/2. Druhá část má po j=k+1
znaménko(−1)^j. Dostáváme obě větve pentagonální řady včetně
konstanty1. Již doložený P0083 ji ztotožňuje s∏_(j≥1)(1−z^j).
Historické autorství Eulerovy argumentace zůstává bibliografickou výjimkou;
její matematický obsah je tímto doplněn bez nového důkazu pentagonální věty.

## Přesné externí závislosti P0280 a P0295

Hadamard: Sheng-Chi Liu, poznámky Jakob Streipel, Lecture Notes in
Analytic Number Theory, aktualizace29.7.2019, věta24.1.1, s.59/file63.
[Zdroj](https://bpb-us-w2.wpmucdn.com/faculty.umaine.edu/dist/1/19/files/2022/08/analyticnumbertheory.pdf).
Použita faktorizace celé funkce řádu≤1 nenulové v0 do genus1 faktorů
a lineární exponenciály, s lokálně stejnoměrnou konvergencí.
Pro D(z)=e^(z−1)−z máme |D(z)|≤e^(|z|−1)+|z|≤2e^|z| pro |z|≥1
a D(0)=e^−1≠0; předpoklady jsou splněny. Dvojnásobný kořen1 se
počítá dvakrát, ostatní kořeny a jejich asymptotika jsou v P0272–74.
Logaritmickou derivaci ospravedlňuje na každém kompaktu mimo kořeny
odhad ocasu O(|z|/|ρ|²) a∑|ρ|^−2<∞. P0280 tedy používá přesně
přípustnou externí větu; věta sama zde není vydávána za vlastní důkaz.

Lévy: CMU21-425, Moment generating and characteristic functions,
věta25 a normální charakteristická funkce v tvrzení19(6).
[Zdroj](https://www.math.cmu.edu/~gautam/c/2026-425/notes/mgf.html).
Dosavadní blokový argument P0295 pro každé reálné t dává limit
e^(−t²/2), právě charakteristickou funkci N(0,1). To jsou podmínky
věty25. Vynechaný centrovaný zbytek R má E|R|/σ→0, a tedy
`|E exp(it(B+R)/σ)−E exp(itB/σ)|≤|t|E|R|/σ→0`.
Není zapotřebí další nepojmenovaná věta pro zanedbání zbytku.

## Znovu otevřený P0365 a související úloha Runs27

Důkaz v runs-proof-23-27.md přesně prokazuje bijekci a počet listů
pro neprázdný les. V celém bloku úlohy27 je nyní explicitně otevřený
pouze obor n=0: prázdný les má0 listů, zatímco A(0,0)=1, takže vzorec
„k+1 listů“ v tomto případě neplatí. Definice lesa ve svazku1, §2.3,
výslovně dovoluje nula stromů (text/vol1.txt, odstavec začínající
„A forest is a set“). To neprokazuje, že autor úlohy27 zamýšlel n=0;
nelze však tuto hranici skrýt za již hotový důkaz pro n≥1.
P0365 a související ledgerX0026 jsou proto partial. Nejde o potvrzenou
chybu ani novou UI kartu. P0364 a ostatní úlohy23–26 zůstávají ve svém
prokázaném rozsahu uzavřeny.

## Přesná mapa kontrolovaného inventáře

Čísla níže jsou tištěné stránky; každá jejich arabská file stránka je+11.
Položky odkazují na samostatné argumenty, nikoli na pouhé čtení.

| Text | Inventarizovaný obsah a důkazy |
|---|---|
|1–3|Terminologie a historie odděleny; seskupování/shody/kompilátor P0001–3, vyhledávání doplněno P0376.|
|4|Uspořádání, stabilita, nepřímé pořadí, sentinely P0004–7.|
|5|Náklady P0008–11 (10/11partial); úlohy1–4 P0012–15.|
|6|Kód, MIX, pořadové statistiky P0016–24; začátek druhé sady P0025–28.|
|7–10|Úlohy13–25 a všechny jejich uvedené metody P0029–64; bibliografie explicitně vyňata.|
|11–12|Inverze, determinant, tabulky, maxima P0065–70; počet permutací i rekonstrukce.|
|13–14|GF maxim, sousední výměny, obr.1, inverzní permutace, Rothe P0071–79; geometrie i P0099–100.|
|15–17|GF, tabulka1, pentagonální vzorce, momenty, index/MacMahon P0080–98; dopředné14/15/25.|
|17–19|Úlohy1–13 P0101–127 plus převzaté3/10; úloha14 P0083–84 a doplněný P0377.|
|20–22|Úlohy15–29 P0092/P0095–98/P0128–158; u20 kombinatorická involuce partial.|
|22–25|Multinomiály, číselné příklady včetně dodatku2004, interkalace/cykly P0159–63.|
|26–27|Nejkratší faktor, větyA/B a příklady P0164–69.|
|28–31|Počítání, prvofaktory, větaC, identity20–30 P0170–82 včetně dopředných12/13.|
|31|Úlohy1–11 P0183–99; C0017/izolované vrcholypartial.|
|32–35|Úlohy12–24: P0177/P0179/P0200–243; opravené značení a závorkování z errat zahrnuto.|
|35–38|Runs: definice, rekurence, tabulka1, Worpitzky, GF a momenty P0244–59.|
|39–40|SuperGF, první běh, model nekonečné permutace, kumulativní délky P0260–69.|
|41–43|Tabulka2, začátky běhů, kořeny/obr.3, póly a asymptotiky P0270–81; Hadamard nyní přesně citován.|
|43–44|Multisetová symetrie a oba průměry P0282–85; úloha1 P0286.|
|45|Úlohy2–12 P0287–317, včetně všech pomocných vztahů odpovědí602–604; Lévy nyní citován.|
|46|Úlohy13–19 P0318–40; obr.4 včetně nové verze2025, všechny rekurence a momenty.|
|47 horní část|Úlohy20–27 P0341–65; nověpartial hranice n=0 u27.|
|Errata, nominálně47|Nové úlohy28–29 P0366–75; singleton29(a) jižpartial.|
|47 dolní část|Definice a první tableau patří k dosud nedokončenému náskoku Tableaux.|

Odpovědi584–591 jsou pokryty úvodními položkami;591–597 inverzními;
597–602 multisetovými;602–607 položkami Runs. Dodatečné matematické věty
uvnitř odpovědí jsou součástí mapy, včetně nově doplněné Eulerovy rekurence.
Odstavec o n! různých statistikách v odpovědi Inversions24 byl odstraněn
erratem22.9.2024 a není opomenutým platným tvrzením. Hudební identifikace
not, historické implementace a priority zůstávají explicitními výjimkami.
Mapa nedokazuje úplnost každého dřívějšího důkazu; vybrané tři byly nově
odvozeny, ostatní jsou převzaté v rozsahu jejich skutečných argumentů.
