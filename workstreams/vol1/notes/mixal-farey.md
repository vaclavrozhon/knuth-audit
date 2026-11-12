# §1.3.2-18–19: Fareyovy zlomky

Originály s.161 a519–520 zobrazeny1.listopadu2026. Fareyova posloupnost
řádu n je vzestupný seznam všech redukovaných zlomků mezi0 a1 včetně,
jejichž kladný jmenovatel nepřesahuje n. Redukovaný znamená, že čitatel
a jmenovatel nemají společného dělitele většího než1.

## Lemma o mezeře mezi sousedy

Nechť a/b<c/d, b,d>0 a bc−ad=1. Pro libovolný zlomek p/q přísně
mezi nimi, s celým q>0, jsou čísla

```
u=cq−dp >=1,  v=bp−aq >=1
```

kladná celá. Přímým roznásobením dostaneme
p=ua+vc a q=ub+vd. Zejména q>=b+d. Jsou-li tedy oba krajní
zlomky ve Fareyově posloupnosti a b+d>n, není mezi nimi žádný další
zlomek s povoleným jmenovatelem. Pro mediantu (a+c)/(b+d) nastane
rovnost; medianta znamená součet čitatelů dělený součtem jmenovatelů.
Jednotkový determinant zajišťuje, že tato medianta je redukovaná.

## Rekurence a úplnost

Začneme0/1 a1/n. Jejich determinant je1 a součet jmenovatelů n+1>n,
tedy jsou skutečnými sousedy. Pro dosavadní sousedy a/b<c/d položme
h=floor((b+n)/d), X=hc−a, Y=hd−b. Pak

```
n−d < Y <= n,       Xd−cY=bc−ad=1.
```

Proto0<Y<=n, X/Y je redukovaný zlomek větší než c/d a d+Y>n.
Lemma o mezeře říká, že žádný přípustný zlomek mezi c/d a X/Y není.
Je-li c/d<1, musí X/Y<=1: jinak by přípustný zlomek1/1 ležel
v zakázané mezeře. Vzestupná posloupnost z konečné množiny tak
skončí v1/1 a nic nevynechá. To dokazuje část(a), jednotkový
determinant, i část(b), skutečnou Fareyovu posloupnost, pro obecné n.

Tištěný důkaz používá stejnou myšlenku ve formě nerovnosti rozdílů.
Je třeba číst jeho x_{k+2}/y_{k+2} jako skutečného příštího člena
seřazeného seznamu, dokud se neukáže, že se rovná kandidátu X/Y.
Jde o induktivní porovnání dvou definic; bez tohoto rozlišení by
fráze „by definition“ mohla působit kruhově. Kniha zde nevyžaduje
novou opravu. Součet sousedních jmenovatelů >n je výše odvozen,
nikoli předpokládán bez důkazu.

Z rekurence rovněž plyne
(a+X)/(b+Y)=c/d. To je prostřední člen jako medianta obou sousedů,
přesně vlastnost zmíněná v historické poznámce.

## Velikost posloupnosti

Označme phi(q) počet celých1<=p<=q nesoudělných s q; phi(1)=1.
Počet členů je přesně1+sum_{q<=n}phi(q), kde první1 je0/1.
Pro odvození asymptotiky zaveďme Möbiovu funkci mu(d): je0, pokud
d obsahuje druhou mocninu prvočísla, jinak(−1)^r, má-li r různých
prvočíselných dělitelů. Součet mu(d) přes dělitele kladného k je1
pro k=1 a0 jinak; plyne to z rozvoje součinu(1−1) pro prvočíselné
dělitele k.

Počet nesoudělných uspořádaných dvojic1<=p,q<=n je tedy

```
A(n)=sum_{d<=n}mu(d)floor(n/d)^2
    =n² sum_{d>=1}mu(d)/d²+O(n log n).
```

Poslední odhad plyne z chyby O(n/d) při nahrazení celé části a z
ocasu sum_{d>n}1/d²=O(1/n). Absolutně konvergentní Eulerův součin
dává sum mu(d)/d²=1/zeta(2)=6/pi². Zde zeta(2)=sum_{d>=1}1/d²;
jeho hodnota pi²/6 byla již ověřena v matematické části svazku.
Souměrnost dvojic a jediná diagonální dvojice(1,1) dávají
A(n)=2sum phi(q)−1. Proto počet členů je
3n²/pi²+O(n log n), jak přibližně uvádí zadání.

## MIX program a skutečné meze

`mixal_farey.py` přepisuje původní podprogram bez změn a přidává
pouze volající program a umístění polí. Vstup rI1=n, předpoklad
originálu n>1. rI2=k; výpočet TEMP=h a následná dvě násobení
vytvářejí Y a X z obecné rekurence. CMPA porovná nový čitatel a
jmenovatel. INC2 nemění porovnávací indikátor; JL tedy pokračuje
právě do dosažení1/1. Návratové místo se zachová pomocí STJ9F.
Po návratu je počet uložených zlomků rI2+2.

Předpokládáme dvě disjunktní pole, každé nejméně délky seznamu,
bez překrytí s kódem a TEMP. V našem konkrétním rozmístění X=400,
Y=2200 je kapacita každého1800 slov. Nejvyšší přípustný řád je76,
jenž má1773 členů; řád77 by potřeboval1833 a do této volby se nevejde.
Obecný důkaz platí pro libovolné rozmístění splňující tyto podmínky.
Mezivýsledky h d=b+Y<=2n a h c=a+X<=2n jsou malé; totéž platí
pro vstup dělení b+n. Za paměťové meze je n mnohem menší než
nejmenší velikost slova a nevzniká přetečení.

Pro n=1 je celý seznam rovnou0/1,1/1. Originál tuto hodnotu výslovně
vylučuje; nepovažujeme to za novou chybu. Varianta `handle_one=True`
je naše doplnění CMP1/JE po inicializaci, které tento triviální
vstup bezpečně vrátí. Není vydávána za součást tištěného řešení.

Checker prošel313852 kontrolami. Rekurence pro1<=n<=100 souhlasí
s přímým nezávislým výčtem všech redukovaných zlomků; ten nepoužívá
rekurenci. Celá pole MIX souhlasí v290 bězích: všechny řády2–76
pro b=64,100, a řády2,3,7,76 pro zbývající b. Zvlášť ověřeny
oba běhy rozšíření n=1. Zlomky řádu7 souhlasí i s původní sazbou
zadání. Úspěšný checker neopakovat.

Historie a přesné čtení pramenů jsou v `mixal-farey-sources.md`.
Matematika a program jsou uzavřeny; otevřené bibliografické meze
se nemají zaměňovat za chybu rekurence.
