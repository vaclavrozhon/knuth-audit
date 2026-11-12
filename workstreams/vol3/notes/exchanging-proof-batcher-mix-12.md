# Batcher12: celý MIX program a všechny nákladové vzorce

7. listopadu2026. Originál134/file145 a629–630/file640–641 zobrazen.
P0984–0989 dokazují vlastní algoritmus a jeho okraje; P0994 již
ručně doložil všechny63 porovnání a25 výměn konkrétní tabulky.
Tyto kontroly se neopakují. Žádný matematický běh.

Použito aktuální opravené znění: duplicitní číslo05 je známá
oprava2000 na06; řádek23 má podle opravy2012 `J4N 8B` místo
`J4N 4B`. Pět vrstev je v `sources/exchanging-errata-review.json`.
Oprava obnovuje inicializaci I5 pro další blok; nejde o náš nález.
Pannyho autorství a původní externí odvození nejsou bibliograficky
ověřena. Následující argument je samostatný.

## P0997: všechny indexy, bloky a instrukce01–23

Předpokládáme binární MIX se SRB, jednoslovné záznamy/klíče,
N≥2 a platný rozsah adres i indexových registrů. TT=H=2^(t−1),
t=⌈lg N⌉. Bitová podmínka je ekvivalentní

    i=r+2kp+s, k≥0, 0≤s<p, i+d<N.

Řádek01 nastaví I1=p=H.02–05 uloží q=H do adresové části
instrukce Q, nastaví I2=r=0 a I4=d=p. Řádky06–08 nastaví
I3=i=r, I4=i+d−N, I5=p−1−s=p−1. P0984 dokazuje i+d<N
pro první dvojici každého skutečného průchodu, takže chybějící
předběžný test nezpůsobí nepřípustné čtení.

Řádky09–10 čtou přesně INPUT+1+i a
INPUT+N+1+(i+d−N)=INPUT+1+i+d. Oba indexy jsou platné.
11 skočí na15 právě při levém klíči≤pravého. Jinak12–14
přes X prohodí oba záznamy; původní levý záznam zůstává v A
až do posledního STA. Řídicí registry se výměnou nemění.

Je-li I5>0,15 nepřeskočí a16–18 zvýší s,i i relativní
pravý index o1.19 pokračuje právě při i+d<N. Při dosažení
hranice v neúplném bloku jde20 do M5. Je-li I5=0, dokončil se
celý blok p po sobě jdoucích indexů.21–22 zvýší i a I4
o p+1: z r+2kp+(p−1) na r+2(k+1)p. Opravený23 při
platné další dvojici skočí na08 a obnoví s=0; jinak přejde
do M5. Každý přípustný index se tedy provede právě jednou,
žádný nepřípustný se nepoužije pro čtení.

I3 po závěrečném přeskočení nepřeroste N: celý dokončený
blok se začátkem i0 splňuje i0+p≤N−d, takže nový index
i0+2p≤N−d+p≤N, protože d≥p. Ani tento konečný řídicí
index nevyžaduje rozsah N+p. Pro p=1 je I5 hned0 a každý
jednoprvkový blok prochází větví21–23; argument platí i zde.

## P0998: instrukce24–35 a přesný význam samomodifikace

24 nastaví r=p.25 načte původní q do I4.26–28 přenesou q
do A, provedou binární posun doprava a zapíší ⌊q/2⌋ do
adresové části Q; kladné znaménko instrukce Q se zachová.
29 odečte p od **původního** q v I4, takže d=q_old−p.
30 se vrátí na06 právě při d>0. Protože q_old≥p, je to
ekvivalentní q_old≠p; při rovnosti je nová hodnota Q již
nepotřebná a M6 pokračuje správně.

31–34 stejně vytvoří ⌊p/2⌋ a zapíší je do adresové části
následujícího ENT1.35 pokračuje na02 právě při p≠0.
Každý návrat na02 znovu nastaví q=H, takže zbylá hodnota Q
z předchozího velkého cyklu nevadí. Posuny zachovají požadovaná
celá nezáporná čísla. Spolu s P0997 a ukončením P0984 je
tím doložen každý instrukční přechod opraveného programu.

## P0999: všechny četnosti, zrušení D a konkrétní čas939u

Zaveďme T=t,A=t(t+1)/2,B počet výměn,C počet porovnání,
D počet **úplných** bloků délky p a E počet neúplných bloků.
Pouze B závisí na datech. Pojem D je tímto zpřesněn podle
tabulky četností: úplné i neúplné bloky dohromady mají počet
D+E, nikoli D. Volné slovní „number of blocks“ na630 je
nutno číst s touto konvencí; všechny vzorce ji jednoznačně
určují. Samostatnou matematickou chybu z této zkratky netvrdíme.

01 se provede jednou.02–05 a31–35 po T.06–07 a24–30
po A. Každý úplný či neúplný blok vstoupí na08, tedy D+E.
09–11 a15 mají četnost C,12–14 četnost B. Jediný poslední
prvek každého úplného bloku přeskočí16–19, takže tyto čtyři
instrukce mají četnost C−D.20 je právě jednou pro každý
neúplný blok, tedy E;21–23 právě jednou pro každý úplný,
tedy D. I poslední celý blok průchodu se počítá do D.

Standardní MIX časy dávají tyto příspěvky:

    01:1;
    02–05:5T; 31–35:7T;
    06–07:2A; 24–30:9A;
    08:D+E; 09–11 a15:6C; 12–14:6B;
    16–19:4(C−D); 20:E; 21–23:3D.

LOAD/STORE/CMP a SRB stojí2u, uvedené indexové změny a skoky1u.
Součet je přesně11A+6B+10C+2E+12T+1; D se vyruší.

Pro N=16 jsou velikosti bloků jednotlivých průchodů p a z
již odvozených C vychází D po řadě1,2,1,4,2,3,8,4,6,7,
celkem38. Neúplné bloky nejsou, E=0. S T=4,A=10,B=25,C=63
je čas110+150+630+48+1=939u. Nejde pouze o dosazení
knižních četností: jejich význam a úplnost jsou odvozeny výše.

## P1000: obecný počet úplných bloků D

Pro jeden průchod polož L=N−r−d≥0. Porovnávané indexy
jsou r+2jp+s,0≤s<p,2jp+s<L. Úplných bloků je

    D_pass=⌊(L+p)/(2p)⌋,

a neúplný existuje právě při0<L mod2p<p. V prvním průchodu
pevného p je L=N−p. V dalších L=N−q_old, kde q_old
postupně probíhá H,H/2,…,2p. Tím je odvozen počítaný objekt
i přesná hranice p, nikoli jen asymptotický počet bloků.

Piš N=Σ_(j=0)^e b_j2^j, b_e=1, e=⌊lg N⌋. Pro jednotné
počítání můžeme i při N=2^e formálně použít kapacitu2^(e+1):
přibude pouze prázdný průchod p=N a po jednom prázdném
průchodu q_old=N pro každé menší p. Mají L=0,D=E=0.
Nemění to D ani E; tuto konvenci nepoužíváme pro skutečné T,A.

Pro p=2^k,0≤k≤e, označ u=⌊N/2^(k+1)⌋ a b=b_k.
První průchod má D=u. Každý z dalších e−k má
D=u+b−q_old/(2p), takže dohromady

    D_k=(e+1−k)⌊N/2^(k+1)⌋+(e−k)b_k−(2^(e−k)−1).

Koeficient b_j v součtu prvních dvou členů je

    Σ_(k=0)^(j−1)(e+1−k)2^(j−k−1)+(e−j)=e·2^j.

To plyne po h=j−k−1 z Σ2^h=2^j−1 a
Σh2^h=(j−2)2^j+2, včetně j=0 s prázdnou sumou.
Součet posledních členů je2^(e+1)−e−2. Proto

    D=eN−2^(e+1)+e+2=e(N+1)−2(2^e−1).

Při N=2^t je e=t a dostáváme(t−2)N+t+2, přesně oba
tvary odpovědi. Vše platí i pro nejmenší přípustné N=2.

## P1001: obecný počet neúplných bloků E

Piš N=2^(k+1)u+b_k2^k+ell,0≤ell<2^k. První průchod
má neúplný blok právě při b_k=1 a ell>0; každý další právě
při b_k=0 a ell>0. Pro stejnou neškodnou kapacitu výše
tedy příspěvek pevného k je

    E_k=[ell>0](b_k+(e−k)(1−b_k)).

Označ f nejnižší nenulový bit N. Podmínka ell>0 znamená
přesně k>f, takže

    E=Σ_(k=f+1)^e(e−k)+Σ_(k>f,b_k=1)(1−e+k)
     =binom(e−f,2)+Σ_(j=1)^(r−1)e_j−(e−1)(r−1),

kde e=e_1>…>e_r=f jsou všechny nenulové bity. To je přesně
tištěný obecný vzorec. Pro mocninu2 je e=f,r=1 a E=0.
Pro N=3 je D=2,E=1: první p=2 průchod má jediný neúplný
blok a oba p=1 průchody úplný blok. Tento okraj současně
objasňuje konvenci D v P0999.

## P1002 — partial: nevymezené praktické srovnání na113

Instrukční režie a příklad939u jsou prokázány. Věta, že program
je méně efektivní než dříve viděné metody, však neudává rozsah
N, rozdělení dat ani konkrétní soupeřící implementaci. Jeden
časový příklad ani paralelní hloubka z ní neudělají univerzální
nerovnost. Tento obecný praktický soud zůstává partial; není
označen za chybu. Historická formulace o nejrychlejší známé
obecné metodě má navíc vlastní bibliografickou/modelovou výjimku
u P0995. Počty14–15, maximalizace11 a průměr16 čekají odděleně.
