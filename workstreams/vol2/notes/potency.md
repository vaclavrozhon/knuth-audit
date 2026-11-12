# §3.2.1.3: potence a nízký stupeň algebraických závislostí

Kontrola 1. listopadu 2026. Text začíná dole na str. 23, pokračuje
na str. 24–25; osm původních úloh končí na str. 26. Odpovědi jsou
na str. 550–551. Všechny tyto původní stránky byly vizuálně přečteny:
[24](../images/vol2-p024.png), [25](../images/vol2-p025.png),
[26](../images/vol2-p026.png), [550](../images/vol2-p550.png),
[551](../images/vol2-p551.png). Žádná dodatečná úloha nebyla nalezena.

## Definice a text

Kongruenční posloupnost splňuje X_(n+1)=(aX_n+c) mod m. Zbytky X_n
volíme z 0,...,m−1. Předpokládá se plná perioda m podle věty §3.2.1.2A.
Položme b=a−1. **Potence** s je nejmenší kladné celé číslo s b^s=0
modulo m. Existuje, protože každé prvočíslo v m dělí b.
Kladnost doplňuje erratum ze 14. 5. 2016.

Pro m=z^e, a=z^k+1, 2<=k<e a c=1 jsou podmínky plné periody splněny:
prvočísla v m jsou právě prvočísla v z; pokud 4|m a z je sudé,
pak 4|z^k. Pro binární a desetinný základ je to aplikace věty A.
Stejný argument platí pro velikost bytu B v MIXu a modul B^5.

Při X_0=0 dává geometrický součet po binomickém rozvoji

```
X_n = c sum_{j=0}^{s−1} binom(n,j+1) b^j mod m.
```

Binomický koeficient binom(n,r) je n nad r, s hodnotou 0 pro r>n.
Vyšší mocniny b zmizí modulo m. Pro a=1, tedy b=0, interpretujeme
geometrický součet polynomiálně, nikoli jako dělení 0/0: X_n=cn mod m.

Potence 1 tak dává aritmetickou posloupnost. Pro potenci 2 je
X_n=cn+cb binom(n,2) modulo m, první rozdíl je c+cbn modulo m
a druhý rozdíl je cb. Pro d=cb mod m tedy trojice (x,y,z)=(X_n,X_(n+1),X_(n+2))
splňuje x−2y+z=d modulo m. Protože −2(m−1)<=x−2y+z<=2(m−1),
možné roviny jsou přesně podmnožinou vytištěného seznamu
d+m,d−m,d,d−2m. Netvrdí se, že se každá rovina nutně obsadí.

Při m=2^35 a b=2^k je s=ceil(35/k): k=18,...,34 dává s=2,
k=12,...,17 dává s=3, k=9,10,11 dává s=4. Požadavek s>=5
nechá k<=8, tedy a<=257. Takový malý násobitel současně dává
velmi krátkou relaci −aX_n+X_(n+1)=c modulo m, takže má hrubou
strukturu sousedních dvojic. To je matematický důvod následného
varování před malými násobiteli.

Hodnocení potřebné potence 5 je doporučení opřené o uváděnou zkušenost,
nikoli postačující či univerzálně nutná věta o každé aplikaci.
Text správně výslovně odmítá zaměnit vysokou potenci za důkaz náhodnosti.
Přesná kontrola spektrálního testu zůstává v §3.3.4.

## Úlohy 1–7

**1.** Instrukce LDA X načte kladný zbytek; SLA 2 posune pět bytů
o dvě místa doleva a zahodí dvě nejvyšší. V registru je B^2 X mod B^5.
ADD X a INCA 1 dávají (B^2+1)X+1 modulo B^5. Případný přetečený
příznak se dále nepoužívá. Plná perioda plyne z výše uvedeného argumentu
pro libovolné B>=2. Čas je 2u+2u+2u+1u=7u proti 16u předchozího
programu; u je jednotka časování MIXu. Jde o matematický model uvedených
instrukcí, nikoli úplný assembler nebo model fyzického procesoru.

**2.** (B^2)^2=B^4 není násobkem B^5, ale (B^2)^3=B^6 je. Potence je 3.

**3.** Číslo 3141592620 i 2^23+2^13+2^2 mají přesně dva faktory 2.
Potence je proto ceil(35/2)=18 v obou případech.

**4.** Pro plnou periodu modulo 2^e, e>=3, je v_2(a−1)>=2.
Zde v_p(t) značí počet faktorů p v nenulovém t. Hodnota s=ceil(e/v_2(a−1))
je nejvýše ceil(e/2), dosažená při a=5 modulo 8. Pro a=1 je s=1.
Úloha říká postačující podmínku pro maximum; neříká, že jiné zbytky
nikdy stejného maxima dosáhnout nemohou (například e=4).

**5.** Při m=product p_i^e_i a b=k product p_i^f_i, gcd(k,m)=1,
má b^s v prvočísle p_i exponent s f_i. Dělitelnost m|b^s je přesně
s f_i>=e_i pro všechna i; minimum je max_i ceil(e_i/f_i).
Pro a=1 se zvlášť použije s=1; zápis s nenulovým k a gcd(k,m)=1
tuto degeneraci pro m>1 nepokrývá.

**6.** Pro potenci >=4 je nutná aspoň mocnina 2^7 nebo lichého p^4
v modulu. Pro p=2 totiž f>=2, zatímco pro liché p může být f=1.
Všech 92 modulů již [certifikované tabulky](../results/modulus-table.json)
je lichých. Pouze 2^27+1 a 10^9−1 mají prvočíselný exponent aspoň 4,
v obou případech u prvočísla 3. Volbou b jako součinu různých prvočísel
v modulu maxima 4 také dosáhneme. Odpověď je úplná.

**7.** Konečná geometrická řada
a' = 1−b+b^2−...+(−b)^(s−1) mod m splňuje
(1+b)a'=1−(−b)^s=1 mod m. Jde o korektní inverzi a modulo m.

## Úloha 8 po opravě zadání z roku 2004

Generátor má m=2^35, a=2^17+3, X_0=1. Všechny stavy jsou liché.
Proto a^2=2^34+6a−9 modulo m implikuje

```
X_(n+2) = 2^34+6X_(n+1)−9X_n mod m.
```

Opravené zadání kvantuje stav do dvaceti intervalů:
Y_n=floor(20 X_n/m), kde floor je zaokrouhlení dolů.
Při zlomkových částech epsilon_1,epsilon_2 v [0,1) pak platí

```
Y_(n+2) = floor(10+6(Y_(n+1)+epsilon_1)−9(Y_n+epsilon_2)) mod 20.
```

Výraz 6epsilon_1−9epsilon_2 je v otevřeném intervalu (−9,6).
Po podlaze je tedy možných pouze 15 z 20 třetích hodnot pro každou
první dvojici. Nejméně 2000 z 8000 buněk histogramu trojic je prázdných
při libovolné délce běhu. To vysvětluje vadu bez statistické aproximace.

Milion nepřekrývajících se trojic podle opraveného zadání dal přesně
2000 prázdných buněk, maximální počet 351 proti rovnoměrnému průměru 125.
Původní desetinná varianta s 30 000 trojicemi dala všechny buňky
obsazené, počty 12 až 51. Úprava zadání proto činí strukturální vadu
mnohem zřetelnější; původní slabší popis není novým nálezem.

Erratum z 14. 5. 2016 se snaží změnit aproximaci na přesnou rovnost,
ale podlaha v něm chybí. Trojice (Y_75,Y_76,Y_77)=(6,16,3) pak
nevyhoví pro žádná povolená epsilon. To je nový nález
[V2-C0006](C0006-quantized-equality.md); přesný intervalový důkaz,
původní PS a anglický draft jsou u něj. V milionu trojic nastalo
9285 takových případů. Hlavní vysvětlení vady generátoru je správné.

Závěrečná poznámka odpovědi mění násobitel na a=2^33+2^18+5.
Pak (a−5)^2 je násobkem 2^35, takže pro libovolný přírůstek c

```
X_(n+2)−10X_(n+1)+25X_n = (a−9)c mod 2^35.
```

Pravá strana je konstantní. To dokazuje uvedenou druhou závislost,
přestože obvyklá potence je velká. Obecně velká dělitelnost a−h
pro malé h může vytvořit podobnou relaci s malými koeficienty;
v textu se tato vada nazývá „second-order impotency“.

## Errata a reprodukce

Relevantní změny: odstranění tečky na str. 24 (13. 1. 1998),
kladnost s (14. 5. 2016), nové zadání na str. 26 i vzorec na str. 551
(27. 2. 2004), změna znaménka aproximace na rovnost (14. 5. 2016).
Všechny vrstvy errat byly prověřeny; poslední změna zakládá C0006.

[Program](../verify_potency.py) a [výsledky](../results/potency.json):
165 791 modelovaných MIX přechodů, 341 potencí a inverzí,
151 335 hodnot binomického vzorce, 47 926 kontrol čtyř rovin,
úplná tabulka kandidátních modulů a milion trojic opraveného zadání.
Protipříklad je navíc ověřen samostatně modulárními mocninami;
používají se jen přesná celá čísla a racionální čísla.
