# D185 — dokončení celé MPR84, Gilatova reprezentace

7. listopadu 2026. Zadání p20/file40 a celá odpověď
p382/file402 i odpovídající PS p20/file26 a p39/file45
přímo posouzeny. Části(a,b) a F159 se přebírají z
D099 podle přesného rozsahu níže; staré svědky
ani jiné výpočty neopakujeme. Zbývající matematická
reprezentace má nyní vlastní úplný důkaz.

## Přesně převzaté části(a,b)

V notes/sequential-mpr-006-008.md, odstavce
„Konvexní transformace“, „F159“ a „Doplněný rozsah
MPR84(b)“, jsou dokázány tyto konkrétní kroky:

- Podmíněný Jensen pro integrabilní f(Z_n),
  následovaný nutným druhým podmíněním na historii f(Z).
- Celá trojatomová chyba ztotožnění dvou podmínění
  v odpovědi(a), F159; opravená nerovnost zůstává.
- Pro neklesající konvexní f a submartingale Z
  obě po sobě jdoucí nerovnosti a přechod na vlastní
  historii f(Z).
- Každý pokles f(x)>f(y) při x<y vytváří
  deterministický submartingalový protiargument,
  takže monotónnost je potřebná pro univerzální
  kladnou odpověď(b).

Přebírá se přesná obecná konvence existence očekávání.
Samotná integrabilita Z_n nezaručuje integrabilitu
libovolné konvexní transformace. Interval může být
neomezený, ale zvolená f musí být definována na hodnotách
procesu a transformace integrabilní. Tím nejsou
přidány žádné nové neprověřené případy starého důkazu.
F159, jeho původní sazba, šest vrstev errat a přijetí
koordinátorem zůstávají zachovány bez nového běhu.

## Přesný význam reprezentace

Gilatův citovaný název a bibliografická data jsou
ověřena v [primárním archivu čísla Annals of Probability](https://www.jstor.org/stable/10.2307/i312950):
David Gilat, svazek5(3), červen1977, pp475–481.

[Maisonneuveho výzkumný článek1979, p642](https://www.numdam.org/item/SPS_1979__13__642_0.pdf)
výslovně formuluje reprezentaci na vhodném
pravděpodobnostním prostoru, se shodným zákonem
původního procesu a absolutních hodnot martingalu.
Původní stránka byla stažena a zobrazena.
Zde neprovádíme audit jeho celého dalšího důkazu;
následující diskrétní konstrukce je soběstačná.

Přesný výrok pro knižní posloupnost je: daný nezáporný
integrabilní submartingale X lze přenést na produktový
prostor, aniž se změní jeho společný zákon, a tam
existuje integrabilní martingale M s |M_n|=X_n
současně pro všechna n skoro jistě. To zejména
reprezentuje původní proces v zákoně.

Netvrdíme existenci nové náhodnosti na každém pevně
daném původním prostoru. Na jednoatomovém prostoru
například X_n=n+1 nemůže být absolutní hodnotou
martingalu, neboť každý takový martingale je konstantní.
Tato nezbytnost rozšíření je standardní, zde pramenně
doložený význam reprezentace; knižní dovětek žádný
zákaz rozšíření prostoru nestanovuje. Nejde o nový
nález ani kandidáta.

## Úplná diskrétní konstrukce

Nechť F_n je původní historie X do času n
(nebo libovolná filtrace, vůči níž je X submartingale).
Položme

    μ_n=E(X_{n+1}|F_n).

Integrabilita dává konečné μ_n skoro jistě,
nezápornost a submartingalová vlastnost dávají
0≤X_n≤μ_n. Všechny tyto vlastnosti lze vzít na
jediné množině plné míry: časů je jen spočetně mnoho.

Rozšiřme prostor o nezávislý férový znak S₀∈{−1,1}
a nezávislé U₁,U₂,…, rovnoměrné na[0,1], nezávislé
i na celé původní náhodnosti. Jde o běžný spočetný
produkt původního prostoru, dvoubodového prostoru
a jednotkových intervalů; jeho konečné prefixy
mají konzistentní součinové pravděpodobnosti.
Původní X_n na produktu závisí jen na původní
souřadnici, takže všechny jeho společné zákony
zůstávají přesně stejné.

Definujme F_n-měřitelný faktor

    q_n=X_n/μ_n, pokud μ_n>0;
    q_n=1, pokud μ_n=0.

Na zanedbatelných výjimečných množinách můžeme
zvolit libovolně q_n=1. Tedy0≤q_n≤1 a
q_n μ_n=X_n skoro jistě. Pro μ_n=0 totiž také
X_n=0. Navíc X_{n+1}=0 skoro jistě na této
události, protože

    E(X_{n+1}[μ_n=0])=E(μ_n[μ_n=0])=0.

Dále rekurzivně položme

    B_{n+1}= 1, pokud U_{n+1}≤(1+q_n)/2,
            −1 jinak;
    S_{n+1}=S_n B_{n+1};
    M_n=S_n X_n.

Obě pravděpodobnosti(1±q_n)/2 jsou nezáporné
a mají součet1. Každý S_n je znak±1, takže
|M_n|=X_n přesně a E|M_n|=E X_n<∞.
Konečná indukce definuje každý člen bez dělení
nulou. Při X_n=0<μ_n máme q_n=0 a nový znak
je férový; konstrukce proto zahrnuje i odchod
z nuly. Při μ_n=0 se nula zachová v dalším
kroku a volba q_n=1 nijak neškodí.

## Každý podmíněný krok a vlastní historie

Označme G_n=F_n rozšířenou o S₀,U₁,…,U_n.
Veličiny S_n,q_n a M_n jsou G_n-měřitelné.
Přidání dosavadních pomocných veličin nemění
podmíněný zákon původních budoucích X:
na produktu jsou tyto pomocné souřadnice
nezávislé na celé původní náhodnosti. Proto

    E(X_{n+1}|G_n)=μ_n.

Ještě podmiňme celou původní náhodností a
S₀,U₁,…,U_n. Nové U_{n+1} je stále nezávislé
rovnoměrné, přičemž q_n je již známé; tedy
podmíněný průměr B_{n+1} je
(1+q_n)/2−(1−q_n)/2=q_n.
Podmíněním zpět na G_n a vytknutím omezených
známých faktorů dostáváme

    E(M_{n+1}|G_n)
      =S_n E(B_{n+1}X_{n+1}|G_n)
      =S_n E(q_n X_{n+1}|G_n)
      =S_n q_n μ_n
      =S_n X_n=M_n.

Všechny součiny jsou integrabilní, protože mají
absolutní hodnotu nejvýše X_{n+1}. Žádná
neomezená transformace podmíněného očekávání
se neprovádí. Na události μ_n=0 je poslední
rovnost0=0; všechny větve tedy byly posouzeny.

Historie H_n=σ(M₀,…,M_n) je podmnožinou G_n.
Věžová vlastnost a H_n-měřitelnost M_n dávají

    E(M_{n+1}|H_n)
      =E(E(M_{n+1}|G_n)|H_n)=M_n.

Jde proto o martingale i podle vlastní definice
knihy, nikoli jen o proces s nepoužitelnou pomocnou
historií. Současné absolutní hodnoty jsou přesně
přeneseným X. Férová nezávislá volba S₀ navíc
při změně S₀ na−S₀ obrátí celý proces M
a zachová pravděpodobnostní zákon; konstrukce
tedy dává i symetrický martingale.
Tato dodatečná symetrie není pro knihu potřebná.

## Pramenné výjimky a uzavření

Plný text původního Gilat1977 nebyl při krátkém
přístupu Project Euclid/JSTOR dostupný. Jeho
historický původní důkaz a širší spojité či
zobecněné verze se bibliograficky vynechávají;
žádná z nich není potřebná pro právě úplně
dokázaný diskrétní výrok knihy. Metadata a
kontext vhodného prostoru jsou ověřeny
v přesně uvedených primárních archivech.

Dřívější výjimka Doob1953 se zachovává výslovně
i pro citované pp295–296 v odpovědi84(b).
Matematika(a,b) má vlastní důkaz D099,
takže vynechání této historie neuzavírá
žádnou nedokázanou matematickou větu.

Původní manifest77–84 pro stránky a odpovědi
se přebírá; nový doplňkový manifest84 hledá
Gilatův dovětek ve všech šesti vrstvách errat
a třech TeX zdrojích. Jediné shody jsou cizí
SAT odpověď84 a nesouvisející indexové stránky.
Použitelná oprava tohoto dovětku nenalezena.

D185 uzavírá dřívější matematickou mezeru84;
celá úloha je nyní reviewed s převzatou F159
a přesnými bibliografickými výjimkami.
Historický stav partial v D099 se nezatajuje.
Žádný nový nález, kandidát, výpočet ani restart.

