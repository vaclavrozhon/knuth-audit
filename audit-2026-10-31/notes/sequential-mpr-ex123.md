# MPR 123: Bayesův krok a očekávaná změna logaritmu šancí

D221, 7. listopadu 2026. Celé zadání p25/file45 a odpověď
p390/file410 zobrazeny, stejně jako autorův PS p25/47,file31/53.
Původní F007 převzat pod stejným ID. Žádný nový nález,
kandidát, matematický výpočet nebo restart. Jediná přesná
bibliografická výjimka je historické tvrzení o původní motivaci
autorů z roku1951; matematický argument je úplný.

## Model a správné váhy: převzatý F007

A je hypotéza, že se používá cílový zákon y; při jejím
popření se používá x. Pro daný krok k pišme a=p_k.
Model tedy stanoví Pr(Z=t|A)=y(t), Pr(Z=t|¬A)=x(t).
Lze ho realizovat nezávislým výběrem A a příslušného
zdroje. Jsou-li k dispozici předchozí pozorování,
všechny tyto pravděpodobnosti jsou podmíněny jejich
dosavadní historií; pro jeden krok není třeba
dokazovat žádnou další nezávislost nepoužitých hodnot.

Fráze „hypothesis Z=Y“ znamená výběr komponenty A,
nikoli náhodnou rovnost dvou číselných hodnot.
I kdyby se konkrétní hodnoty X a Y někdy shodovaly,
událost A označuje původ vzorku. To je kontext
směsového modelu v zadání, nikoli nová interpretace
čistě hodnotové rovnosti.

Rozkladem na disjunktní události A a ¬A dostáváme

    Pr(A,Z=t)=a y(t),
    Pr(¬A,Z=t)=(1−a)x(t),
    z_k(t)=a y(t)+(1−a)x(t).

Součet z přes t je a+(1−a)=1. Tištěný vzorec zaměňuje
x a y, a proto F007 zůstává platný. Přečtený starý
přesný svědek z results/information.json je

    x=(3/4,1/4), y=(1/4,3/4), a=1/4.
    správné z=(5/8,3/8), tištěné z=(3/8,5/8).

Všechna čísla jsou přísně kladná; nejde o nulové
jmenovatele nebo okrajový prior. PDF i autorův PS
mají shodnou záměnu. Oprava se týká jen zadání p25;
samotný Bayesův vzorec odpovědi p390 je při správném
významu z_k platný, proto se tato odpověď F007 nebarví.

## Každý krok Bayesovy odpovědi

Nejprve 0<a<1 a pozorování t s z_k(t)>0. Podmíněná
pravděpodobnost a'=p_(k+1) je přesně

    a'=a y(t)/z_k(t),
    1−a'=(1−a)x(t)/z_k(t).

Druhá rovnost vzniká buď přímo z ¬A, nebo odečtením
první od1 za použití správného součtu z_k.
Je-li navíc x(t),y(t)>0, oba posteriory jsou v(0,1)
a dělení dává

    a'/(1−a')=[a/(1−a)]·[y(t)/x(t)],
    ρ(t)=(1−a)a'/[a(1−a')].

Poslední řádek je přesně tištěná rovnost odpovědi,
bez chybějícího normalizačního faktoru. Logaritmem

    lg(a'/(1−a'))−lg(a/(1−a))=lgρ(t).

Výchozí logaritmus šancí je konečný, protože prior
je nedegenerovaný. Tím je dokázán bodový výrok,
jehož očekávání úloha žádá.

## Podpory, nulová pozorování a krajní priory

Je-li x(t)=0<y(t), z_k(t)=a y(t)>0 a a'=1.
Levá změna logaritmu šancí je +∞ minus konečné
číslo, tedy +∞, stejně jako lgρ(t).

Je-li y(t)=0<x(t), posterior je0 a změna je−∞.
Pod cílovým zákonem Y se však takový bod nepozoruje;
má nulovou váhu v požadovaném očekávání.
Je-li x(t)=y(t)=0, je i z_k(t)=0 a t je
nemožné v celém modelu. Podmíněný posterior zde
lze zvolit podle nulové konvence knihy, ale
nikde se z něj nedělí ani nepočítají šance.

Při a=0 nebo1 je už výchozí logaritmus šancí
nekonečný a jeho změna může být ∞−∞ nebo−∞+∞.
Přirozenou doménou zadané změny je tedy0<a<1.
Degenerovaný prior nelze tímto rozdílem aktualizovat;
formální logaritmus likelihood ratio tím nepřestane
existovat, ale není hodnotou nedefinovaného rozdílu.
Kniha neuvádí zvláštní konvenci pro takové odčítání,
a nenutíme mu hodnotu. Nevzniká nový kandidát
z pouhého doplnění domény logaritmu šancí.

## Očekávání pod Y, včetně nekonečné divergence

Na všech bodech s kladnou pravděpodobností Y
je právě dokázaná změna rovna lgρ(t), konečnému
číslu nebo +∞. Její záporná část je integrovatelná:
na 0<ρ<1 je y|lgρ|=x·ρ|lnρ|/ln2≤x/(e ln2).
To je přesně obecný odhad D219 pro úlohu121.

Proto očekávání existuje rozšířeně a

    E_Y[lg(p_(k+1)/(1−p_(k+1)))−lg(p_k/(1−p_k))]
      =Σ_t y(t)lg(y(t)/x(t))=D(y||x).

Nepoužívá se zde neplatná první forma D z F008,
takže singularita cílového zákona správně vede k+∞.
Vážení je zákonem Y, jak zadání výslovně požaduje;
nejde o očekávání pod směsí z_k. Pro x=y je ρ=1,
posterior zůstává a a obě strany jsou0.

Bayesův krok zachovává a'∈[0,1]; při obou kladných
likelihoodech zachovává otevřený interval(0,1).
Jedno vyhodnocení po získání x(t),y(t) má konstantní
počet aritmetických operací. Není tu nekonečný
algoritmus ani tvrzení o nákladech získání těchto hustot.

## Historie, errata a přesný rozsah

Primární vydavatelská metadata Crossref pro
DOI10.1214/aoms/1177729694 potvrzují S.Kullbacka,
R.A.Leiblera, název On Information and Sufficiency,
Annals of Mathematical Statistics22(1951),79–86.
Jsou uložena jako sources/kullback-leibler-1951-crossref.json.

Otevření současné stránky i PDF adresy Project Euclid
vrátilo pouze obalovou stránku. Starší oficiální PDF
URL také vrátilo HTML, nikoli PDF; nebylo uloženo jako
falešný článek. Původní argument o motivaci autorů
nebyl rychle dostupný. Přesně toto historické tvrzení
zůstává bibliografickou výjimkou, nikoli matematickou
mezerou. Obsah celého článku ani jeho prvenství se
netvrdí jako nezávisle ověřené.

Všech šest vrstev errat a tři TeX zdroje prohledány:
žádná oprava F007 ani jiná použitelná oprava123.
Shoda p25 se týká již známé změny následující124;
ostatní shody čísla123 patří Dancing Links, nikoli MPR.

Celá123 je checked s jednou historickou výjimkou.
File45 zůstává partial pro124–128, včetně úvodní
části128; file410 zůstává partial pouze pro124.

