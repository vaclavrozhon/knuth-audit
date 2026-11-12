# §4.3.1-39: BBP řada, jednotlivé bity a pomocné identity

Uzavřený matematický audit, 2.11.2026. Zadání na str.284, odpověď628–629
přečteny v původním prvním dotisku. Potvrzená lokální chyba C0100 nemění
BBP řadu ani hlavní algoritmus. Historické připsání přesně této řady Eulerovi
v doplňku2024 vedeme odděleně jako kandidát C0101.

## 1. Řady a filtr kořenů jednotky

Pro j=1,...,8 označme S_j součet 16^(-k)/(8k+j) přes k>=0.
Pro obecné celé m>=1,1<=a<=m definujme
F_a(z)=sum_{k>=0} z^(mk+a)/(mk+a), kde |z|<1.
Kořen jednotky ζ=exp(2πi/m) splňuje
sum_{r=0}^{m-1} ζ^{r(t-a)}=m, je-li t kongruentní a modulo m, jinak0.
Dosazení absolutně konvergentní řady log(1-w) proto dává

```
F_a(z)=-(1/m) sum_{r=0}^{m-1} ζ^(-ar) log(1-zζ^r).             (1)
```

Logaritmus zde znamená analytickou větev s hodnotou0 pro z=0.
Pro reálné |z|<1 má 1-zζ^r kladnou reálnou část. Spárování r a m-r
v(1), s θ=2πr/m, dává

```
cos(aθ) log(1-2z cosθ+z²)
    -2 sin(aθ) atan(z sinθ/(1-z cosθ)).
```

Člen r=0 a při sudém m také r=m/2 dávají zbývající dva logaritmy.
To dokazuje obecný vzorec na629 včetně znaménka před arctan a krajních
případů m=1,2 a a=m. Rozsah a=1,...,m je nezbytný a přirozený pro
zástupce zbytkových tříd; nejde o tvrzení pro libovolné a.

Pro m=8,z=1/sqrt(2) máme F_j(z)=2^(-j/2)S_j. Položme
L2=ln2,L3=ln3,L5=ln5,H=ln(1+sqrt2),T=atan(1/sqrt2),W=atan(1/3).
Jednotlivé logaritmy l_r=log(1-ζ^r/sqrt2) jsou

```
l0=-H-L2/2,             l4=H-L2/2,
l1=-L2/2-iπ/4,          l7=conj(l1),
l2=(L3-L2)/2-iT,        l6=conj(l2),
l3=(L5-L2)/2-iW,        l5=conj(l3).
```

Všechny individuální hodnoty tištěné v knize souhlasí. Rovnice(1) dává
pro kombinaci 4S1-2S4-S5-S6 koeficienty u l0,...,l7

```
(2, -2+2i, 0, 0, 2, 0, 0, -2-2i).
```

Výsledek je tedy 2l0-(2-2i)l1+2l4-(2+2i)l7=π.
Tisk má navíc2 před l1 a opačné znaménko před l7; viz C0100.
Dosazení do ostatních sedmi lineárních kombinací na628 potvrzuje přesně
ln2,ln3,ln5,sqrt2 H,sqrt2 T,W a0. Nevyužívá numerické hledání vztahů.

Čtyři obecné identity pro exponenty 8k+1,8k+3,8k+5,8k+7 na konci628
platí pro reálné |z|<1: všechny pravé strany mají hodnotu0 v0 a derivaci
z^(a-1)/(1-z^8). Symbolická kontrola je v bloku identities programu.
Tento argument zároveň určuje větve arctan a log; nepředpokládá globální
rovnost přes jejich řezy v komplexní rovině.

Druhý důkaz samotné BBP identity používá integrál od0 do1. Jeho integrand
je (4-2t³-t⁴-t⁵)/(1-t⁸/16). Přesná racionální identita jej rozloží na

```
4(2+2t+t²)/(4+t⁴)
 +4((1-t)/(2-2t+t²)-t/(2-t²)).                              (2)
```

První člen má primitivní funkci4 atan(t/(2-t)) a integrálπ. Oba integrály
uvnitř závorky mají hodnotu(ln2)/2, takže druhý člen přidá0.
Rozvoj geometrické řady dokazuje BBP formuli nezávisle na koeficientech
komplexních logaritmů. Rozklad(2) je rovněž algebraicky zkontrolován.

## 2. Certifikované získání bitu

n>=1 je pozice za binární čárkou. Hledaný bit je0, je-li zlomková část
2^(n-1)π menší než1/2, jinak1. Pro K=ceil(n/4) rozdělíme každý S_j:

```
2^(n-1)S_j = integer
 + sum_{k=0}^{K-1} (2^(n-1-4k) mod(8k+j))/(8k+j)
 + sum_{k=K}^infinity 2^(n-1-4k)/(8k+j).                    (3)
```

V první sumě je exponent nezáporný; v druhé záporný. Celočíselná
modulární mocnina nepotřebuje ukládat číslo2^n. Pro pracovní přesnost m
každý kladný člen násobený2^m uzavřeme mezi podlahu a strop jeho přesného
racionálního podílu. Po T=ceil(m/4)+2 členech druhé sumy má zbytek horní mez

```
(16/15) 2^(n-1-4(K+T))/(8(K+T)+j).                        (4)
```

Ve škále2^m je tato mez menší než1. Všechny operace používají celá čísla.
Z intervalů [L_j,U_j] tvoříme
[4L1-2U4-U5-U6, 4U1-2L4-L5-L6]. Z něj stačí zjistit, zda oba konce
leží ve stejném intervalu mezi dvěma sousedními násobky1/2. Parita indexu
tohoto intervalu je hledaný bit. Není nutné odhadovat pravou hodnotu
zlomkové části při přechodu přes celé číslo: odebrané celočíselné části
v(3) mění tento index o sudé číslo.

Pokud interval překrývá hranici, zvýšíme m a výpočet zopakujeme.
Iracionalitaπ zaručuje konec pro každé jednotlivé n. Čas O(n log n)
a paměť O(log n) pro O(log n)-bitové operandy používají výslovný předpoklad
zadání o absenci překvapivě dlouhých běhů stejných bitů. Přesněji stačí,
aby vzdálenost2^(n-1)π od nejbližšího násobku1/2 byla alespoň n^(-C)
pro nějakou pevnou konstantu C. Pak m=O(log n) stačí: celková šířka je
O((n+m)2^(-m)), vnějších členů je O(n), modulární mocnina stojí O(log n)
operací a všechny pracovní registry mají O(log n) bitů. Opakované zvýšení
přesnosti je za této hypotézy omezeno konstantním počtem kroků od m~2log n.

Věta v odpovědi o přesnosti druhé sumy předpokládá odpovídající hlídání
zaokrouhlení. Samostatné zaokrouhlení T členů přidává až T jednotek
pracovní škály; náš algoritmus je výslovně započítává. O(log m) dodatečných
bitů případně zaručí chybu druhé sumy<=2^(-m). Dominantní O(n2^(-m)) mez
hlavní metody se tím nemění. Netvrdíme, že každé pevné m=2log n vždy stačí.

## 3. Nezávislá kontrola a zdroje

[verify_classical_bbp.py](../verify_classical_bbp.py), [výsledky](../results/classical-bbp.json),
[log](../results/classical-bbp.log):12 základních symbolických identit
(8 kombinací a4 derivace), dále obecné odvození(1) a nezávislý rozklad(2).
664 pozic1–512 a vybraných pozic až10000 souhlasí s nezávislými přesnými
intervaly z Machinovy formule π=16atan(1/5)-4atan(1/239). Pro ni stačí
spočítat tan(4atan(1/5)-atan(1/239))=1 a určit kvadrant. Orákulum používá
střídavou arctan řadu, podlahy/stropy a znaménko prvního vynechaného členu.
Jeho přesnost10064 bitů,2165+636 členů, šířka37204 jednotek této škály
jednoznačně určila všechny testované bity. Velké registry jsou jen
v nezávislém orákulu, nikoli ve zkoušeném algoritmu.
18 běžných případů potřebovalo zvýšit přesnost; samostatných64 běhů
s úmyslně malým m=2 ověřilo tutéž opravnou větev. Maximum pracovní
přesnosti bylo32 bitů. Běh85620 skončil exit0; úspěšné bloky neopakovat.

Primární předtisk Bailey–Borwein–Plouffe, NAS-96-016, duben1996, uložen
jako sources/bailey-borwein-plouffe-1996.pdf. Vizuálně přečteny strany2,3,7,8:
BBP identita, integrál, modulární výpočet a analýza přesnosti. Nejde o totožnou
sazbu časopiseckého článku Math.Comp.66(1997),903–913.
NASA: https://ntrs.nasa.gov/api/citations/19970009337/downloads/19970009337.pdf

Ojanguren, Elemente der Mathematik77(2022),94–100, doi10.4171/EM/438,
celý PDF vizuálně přečten; pro tento audit využity zejména94–97 a bibliografie100.
https://ems.press/content/serial-article-files/45728
Zbytek obsahuje silnější větu o jediné racionální nulové relaci; její celý
transcendenční důkaz zde není prohlášen za samostatně ověřený výsledek.
Rozdíl Eulerovy a BBP řady viz C0101. Rok online2021 versus svazek2022
není bibliografická chyba knihy.

Errata: all2-prepre,all2-pre,all2,err2 a aktuální uložený TeX prohledány
podle628/629,answer39,logaritmů,polylog,Euler/Ojanguren. Jediná změna
odpovědi39 je historický dodatek30.9.2024; chybný logaritmický mezikrok
neopravuje. Originál dodatku: images/normal-errata-all2-p10.png.
