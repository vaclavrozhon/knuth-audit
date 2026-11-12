# §1.3.2′, úlohy 21–23 — Farey a celé nulování

Zadání file55/p47, odpovědi file112–113/p104–105. Tento blok doplňuje
přesné převzetí matematického důkazu a úplné strojové náklady. Originální file113 byla zobrazena v `images/recovery-farey-zero-113.png`.
Žádný dříve
uložený verifier ani žádný MMIX/pipeline běh se neopakoval.

## 1. Převzatý uzavřený důkaz 21/22 a jeho předpoklady

Celé relevantní důkazy byly přečteny v
`workstreams/vol1/notes/mixal-farey.md`, v obnovené
`quality-recovery-section-1.3.2-harmonic-farey-2026-11-06.md` a pro
konstantu ζ(2) v `gamma-functions.md` (Fourierovy koeficienty),
`harmonic-analytic.md` a §3
`quality-recovery-section-1.2.7-2026-11-06.md`. Používají přesně stejné
kladné celé n, redukované zlomky v [0,1] a kladné jmenovatele≤n.
MIX kód ani jeho instrukční násobitele nepřebírám pro MMIX.

Pro a/b<c/d s bc−ad=1 a p/q přísně mezi nimi jsou
u=cq−dp≥1,v=bp−aq≥1. Identita p=ua+vc,q=ub+vd dává q≥b+d.
Počáteční pár 0/1,1/n má determinant1 a součet jmenovatelů n+1.
Pro h=floor((b+n)/d), X=hc−a,Y=hd−b platí

    n−d < Y ≤ n,  Xd−cY=1,  d+Y>n.

Proto kandidát X/Y je redukovaný a přísně větší než c/d; mezi nimi
žádný přípustný zlomek neleží. Dokud c/d<1, není X/Y>1, jinak by
zakázanou mezeru zaplnil 1/1. Konečnost množiny a striktní růst dokazují
zastavení právě v 1/1 i úplnost. Determinant je současně indukční důkaz22(a).
Počáteční pár již tvoří celý seznam při n=1.

Celý vytištěný důkaz22(b) lze číst nekruhově: označme p/q skutečného
následníka c/d v seřazeném seznamu. Kdyby c/d<p/q<X/Y, pak

    1/(dY)=X/Y−c/d ≥ 1/(Yq)+1/(dq)
          =(d+Y)/(dYq)>n/(dYq)≥1/(dY),

spor. Jde o rozdíly různých racionálních čísel s celočíselnými čitateli,
proto první nerovnosti nepotřebují předpokládat determinant tohoto
dosud neurčeného p/q. Tím je ověřen i konkrétní řetězec nerovností v knize.
Identita (a+X)/(b+Y)=c/d dokládá mediantovou vlastnost z historického odstavce.

Vytištěný seznam pro n=7 má19 členů. První polovina od0/1 do1/2 je
0/1,1/7,1/6,1/5,1/4,2/7,1/3,2/5,3/7,1/2; součty sousedních
jmenovatelů jsou8,13,11,9,11,10,8,12,9 a determinanty všechny1.
Druhá polovina vzniká x↦1−x v opačném pořadí, takže má tytéž vlastnosti.
Lemma zaručuje úplnost tohoto konkrétního seznamu bez nového výčtu.

## 2. Počet členů, konstanta a skutečná paměťová mez

L=1+Σ_(q≤n)φ(q). Möbiova identita Σ_(d|k)μ(d)=[k=1] dává pro počet
uspořádaných nesoudělných dvojic v [1,n]²

    A(n)=Σ_(d≤n)μ(d)floor(n/d)²
        =n²Σ_(d≥1)μ(d)/d²+O(n log n).

Chyba celé části je≤2n/d+1; součet je O(n log n). Ocas nekonečné sumy
je nejvýše n²Σ_(d>n)d⁻²=O(n). Absolutní konvergence dovolí vynásobit
Σμ(d)/d² a Σk⁻² a seskupit součinitele: u čísla r je Σ_(d|r)μ(d),
tedy součin je1. Nevkládá se formální divergentní Eulerův součin.

Hodnota Σk⁻²=π²/6 je přesně převzata z přečteného uzavřeného důkazu:
B₂(t)=t²−t+1/6 má nulový integrál a nenulový Fourierův koeficient
−2!/(2πij)². Absolutní konvergence a identita se spojitou periodickou
funkcí (Fejérovo jádro v příslušné obnovené části) dovolí dosadit t=0.
Vyjde1/6=Σ_(j≠0)1/(2π²j²)=ζ(2)/π². Předpoklady tohoto převzetí
nejsou numerická aproximace ani nedokázaná obecná analytická věta o ζ.

Souměrnost a jediná diagonální nesoudělná dvojice(1,1) dávají
A(n)=2Σφ(q)−1, tedy L=(A(n)+3)/2=3n²/π²+O(n log n).

Výrok „thus ... n<2^32“ lze navíc podložit bez dosazování asymptotiky
na jeden konečný bod. Každá nesoudělná-nepravdivá dvojice má společného
dělitele d≥2; sjednocením přes všechny takové d dostaneme

    n²−A(n) ≤ Σ_(d=2)^n floor(n/d)²
             ≤n²Σ_(d≥2)d⁻² < (3/4)n².

Poslední přísnost je1/4+Σ_(d≥3)d⁻²<1/4+∫₂^∞x⁻²dx=3/4.
Proto L>n²/8. Dvě disjunktní pole tetrabytes potřebují8L>n² bajtů;
pro n≥2^32 by to bylo více než celých2^64 adres. Tato mez opravňuje
zvolený vstupní rozsah; samotné n<2^32 ovšem dostatečnou paměť nezaručuje.

## 3. Celé MMIX tělo21: stav, meze, návrat a cena

`sources/farey21.mms` je úplný vlastní podprogram, zatímco odpověď21
obsahuje pouze zástupné tělo. Předpoklady:1≤n<2^32 v $0, X/Y jsou
disjunktní globální adresové registry s čtyřbajtově zarovnanými oblastmi
kapacity4L, žádný zápis mimo ně a žádné přetečení adres/offsetu.
Volající poskytuje normální rámec. Lokální $1...$9 a rH/rR jsou pracovní;
signed DIV zde rD nevyužívá. Globals X/Y ani n se nemění.

Před 1H jsou(a,b),(c,d) poslední dva sousedé, oba již uložené, a off je
čtyřnásobek indexu druhého. CMP/BZ odejde iff c=d, protože redukovanost
znamená právě1/1. Jinak ADD/DIV vytvoří h a oba MUL/SUB vytvoří další
zlomek. Přesuny zachovají sousedy, INCL posune off o4 a dva STTU uloží
přesně další termín. Indukce z §1 dává správnost a ukončení.

Vstup dělení b+n≤2n a produkty hd=b+Y≤2n, hc=a+X≤2n jsou<2^33.
Všechny jsou nezáporné signed octabytes a DIV nemá nulový d. Výsledky
násobení se vejdou do spodních 64 bitů; instrukce MUL registr rH nemění.
Výsledné čitatele/jmenovatele≤n<2^32 se vejdou do STTU bez ztráty.
Počet iterací je L−2; L=2 pro n=1 funguje bez dělení a násobení.
Vrací se POP0,0; obecný důkaz zásobníku je přesně přijatý dřívější blok,
ne nový neověřený předpoklad o implementaci zásobníku.

Inicializace má10 instrukcí, z nich4 STTU. Úspěšný průchod1H má
CMP,BZ,ADD,DIV,MUL,SUB,MUL,SUB,čtyři SET,INCL,dvě STTU,JMP:
16 základních oops, k tomu DIV+59 a dva MUL+9, celkem93υ a2μ.
Závěrečný CMP/BZ/POP stojí1+3+3=7υ. Přesná nominální cena v tabulkovém
modelu je proto

    2L μ + [93(L−2)+17]υ.

Paměť polí je8L bajtů, práce Θ(L)=Θ(n²) za jednotkové strojové operace.
Není to benchmark, tvrzení o aktuálním procesoru ani o globálně nejrychlejší
generaci. Vytištěná výzva MMIXmasters a budoucímu vydání není algoritmická
záruka a neznamená, že zástupné tělo samo řeší úlohu.

## 4. Zero23: úplný invariant a bezpečnost

Vstup a=s, signed0≤n≤2^63−1, celý interval [s,s+n) je zapisovatelný,
bez nežádoucího wrapu či přetečení signed adresových ADD. Případný širší
modulární kontrakt potřebuje explicitní zachování výsledků V handlerem;
tento blok ho netvrdí. Pracovní jsou $0,$1,$2,$255 a běžný návratový rámec.
Žádná počáteční hodnota z není před prvním zápisem použita: Zero nejprve
pro n>0 vykoná SET z,0. Pro n=0 skočí rovnou na POP.

Invariant: [s,a) je vynulovaný prefix, n je délka zbývajícího suffixu,
a+n=s+n_original; paměť mimo původní interval se nemění. Byte smyčka1H
spotřebuje jeden bajt a vrací se přes test prázdnosti. Jakmile a je
násobek8, n<64 jde do malé koncovky. Pro n≥64 smyčka2H postupuje po8
do násobku64. Spotřebuje nejvýše56 bajtů, proto n zůstává≥8.

Po testu64 je velká smyčka4H dovolena jen při n≥64. Osm STCO pokryje
přesně a+0,...,a+63; SUB odečte64, CMP připraví test dalšího bloku a ADD
posune a. PREST63 je výkonnostní nápověda pro týž interval, nikoli
další logický zápis. Úplný invariant se zachová. Nakonec6H opakuje
octabyte pouze při n≥8 a8H zapisuje posledních1...7 bajtů. Kladný zbytek
v každé smyčce klesá, takže POP nastane; žádná větev nepřekročí konec.

## 5. Zero23: všechny tabulkové ceny

PREST stojí1υ a v tomto modelu není load/store mem. Položme
p=min(n,(-s) mod8), r=n−p. Každý počáteční byte cyklus od Zero přes
1H stojí9υ+μ: BZ1,SET1,AND1,BNZ3,STB1,SUB1,ADD1.

Je-li r=0, poslední BZ/POP stojí6υ, tedy

    T = pμ+(9p+6)υ.                                      (Z0)

To zahrnuje n=0. Je-li0<r<64, nechť o=floor(r/8),e=r mod8. Vstup
od zarovnaného Zero po JMP5F stojí9υ. Větev5H a případná octasmyčka
stojí5o+4υ: buď CMP/BN=4υ při o=0, nebo2υ plus5o+2υ za smyčku.
Větev7H a případná bytesmyčka až po POP stojí4e+6υ, včetně e=0.
Proto

    T = (p+o+e)μ+(9p+19+5o+4e)υ.                        (Z1)

Je-li r≥64, nechť c=(-(s+p) mod64)/8∈{0,...,7},
r−8c=64B+8o+e,0≤o,e≤7. Zarovnaný vstup po PBNN3F stojí6υ;
celá část3H/2H do64zarovnání stojí5c+4υ (i pro c=0).
Následující CMP/BN stojí4υ při B=0, nebo2υ při B≥1.
Každý velký blok má PREST,SUB,CMP,8×STCO,ADD,PBNN, tedy13υ,
poslední nevykonaný PBNN navíc2υ. Spojením s koncovkou ze(Z1):

    T = (p+c+8B+o+e)μ
        +(9p+24+5c+13B+5o+4e)υ.                         (Z2)

Stejná formule platí pro B=0, protože ušetřená poslední2υ velké
smyčky přesně odpovídá dražšímu BN. Například zarovnaných64 bajtů stojí
8μ+37υ. V dlouhé části je jeden store na osm bajtů, maximální šířka
běžného MMIX zápisu. Nic z toho nedokazuje vytištěné „most pipeline and
cache configurations“ bez konkretizace těchto konfigurací.

Úloha23 proto zůstává **partial výhradně pro požadované pipeline měření
a tvrzení o praktickém výkonu**; algoritmus i celý nominální profil jsou
uzavřené. Nejde o chybějící matematický invariant ani o úlohu dokazovat
všechen hypotetický hardware. Žádný nový dlouhý experiment se nespustil.

## 6. Historie a rozsah celé file113

Přesně přečtená a převzatá `workstreams/vol1/notes/mixal-farey-sources.md`
dokládá Harosův přetisk a jeho chybějící obecné lemma, Fareyův celý dopis
a výslovnou žádost o důkaz, francouzský Cauchyho úplný přetisk i relevantní
Hardy–Wright§3.1–3.4. Matematické tvrzení o mediantě má vlastní důkaz§1.
Původní Harosovo číslo svazku/strany a přesné dějiny pojmenování celé
posloupnosti zůstávají výslovně bibliograficky přeskočené, stejně jako
neověřené tvrzení o okolnostech nezávislého objevu a Fareyově povolání geologa. Známá oprava názvu
philomatique je v erratech a není nález.

File113 dále obsahuje úvod24, včetně možnosti zrychlit stejně zarovnané
adresy. Přesná specializace r=0,l=64 odstraní z každého úplného osmibajtového
cyklu StrCpy tři mrtvé operace: SRU tt,in,0, MUX out,tt,out s rM=-1
a SLU out,in,64. Jejich účinek nahradí přímý STOU in; test BDIF a posun
adres zůstanou. Koncová větev použije out=in a již dokázanou poslední
masku, inicializační prefix zůstane stejný. Jednorázový test zarovnání
má omezenou cenu a úspora3υ za každý celý blok roste bez omezení.
To dokazuje přesně tvrzenou možnost rychlejší specializace pro dlouhé
stejně zarovnané řetězce, nikoli převahu na každém malém vstupu.

Každý odstavec file113 je tím přiřazen argumentu nebo přesné výjimce;
stránka zůstává partial kvůli23 a uvedené bibliografii. Vzor binomických
mezí vede k explicitnímu konečnému důkazu n<2^32, nákladový vzor k oběma
nulovým okrajům a úplným profilům, stavový vzor k omezení adres a rámce.
