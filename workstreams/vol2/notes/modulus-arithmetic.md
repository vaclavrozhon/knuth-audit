# §3.2.1.1: modul, strojová aritmetika a úlohy 1–11

Kontrola 1. listopadu 2026. Text str. 12–16; zadání 1–6 na str. 15,
7–14 na str. 16; odpovědi 1–11 na str. 543–545. Původní stránky jsou
v `images/vol2-pNNN.png`. Inventář obsahuje 14 úloh, žádnou přidanou.
Úlohy 12–14 jsou zpracovány samostatně.

## Model výpočtu a programy v textu

`w` je počet různých nezáporných hodnot jednoho slova, tedy magnituda
slova MIX leží v `0,...,w-1`. `m` je modul kongruenčního generátoru,
`a` násobitel, `c` přírůstek a `x` jeho stav. `mod` značí nezáporný zbytek.
MIX ukládá znaménko zvlášť; přetečení sčítání nastavuje příznak,
ale nepřetečená operace ho sama nemaže. Zbytek magnitudy zůstává v registru.

Sémantika instrukcí porovnána s TAOCP 1, §1.3.1, str. 131–135:
ADD/SUB, MUL, INCA, posuv a JOV/JNOV. MUL uloží horní a dolní část
součinu do A/X; obě části mají jeho znaménko. Posuv nemění znaménka.
JOV i JNOV při kontrole vypnou zapnutý příznak. Záporná nula se při
podmínkách porovnává jako nula. [Validátor](../verify_modulus_arithmetic.py)
modeluje tuto číselnou sémantiku; nejde o úplný assembler či simulátor MIX.

Pro `m=w` program (1) násobí, přesune dolní polovinu do A a přičte `c`.
Výsledek je tedy `(a*x+c) mod w`; overflow může být zapnutý, jak text uvádí.
Případné `JOV *+1` ho vymaže. Při běžném dělení dvouslovného součinu
modulo `m` je podíl menší než `w`, pokud `a,x,c<m<=w`: platí
`a*x+c<m^2`. V této aplikaci tedy nehrozí přetečení podílu DIV.

Pro program (2), `m=w+1`, napišme `a*x=q*w+r`, `0<=q,r<w`.
Po LDAN, MUL, STX, SUB je v A přesně `r-q`, a to bez přetečení.
Protože `a*x=q*(w+1)+(r-q)` a `-w<r-q<w`, stačí nezáporný rozdíl
ponechat, zápornému přičíst `w+1`. Dvě instrukce `INCA 2; ADD w-1`
to provedou; při `r-q=-1` poslední sčítání přeteče a uloží nulu.
Právě tehdy je skutečný zbytek `w`. To dokazuje i upřesnění errata 2011.

Varianta vynechávající stav `w` nahrazuje řádky 05–06 třemi instrukcemi
`JANN *+4; INCA 2; JAP *-5`. Kladný výsledek po INCA nastane pouze
při rozdílu `-1`, kdy A obsahuje 1. Skok do MUL tak provede další krok
ze stavu `w`, protože `-w=1 (mod w+1)`. Výsledek je `w+1-a`, pokud
`a>=2`; je reprezentovatelný. Pro `a=0,1` k tomuto přeskoku z povoleného
vstupu `x<w` ani nedojde. Většina vstupů potřebuje jeden součin,
výjimečný případ dva; bez přetečení.

## Dolní cifry a skutečné stroje

Je-li `d` kladný dělitel `m`, redukce `Y_n=X_n mod d` splňuje
`Y_(n+1)=(a*Y_n+c) mod d`, protože člen odečítaný při redukci modulo `m`
je násobkem `d`. Perioda tedy nepřesahuje `d`. Pro doporučené jednotkové
násobitele a `m=2^e` je `a` liché, takže nejnižší bit je konstantní
nebo střídavý od začátku; pro sudé `a` může mít nejvýše jednokrokový ocas.
Následující komentář o podobné kvalitě horních a dolních bitů při `w±1`
je doporučení k odstranění tohoto konkrétního defektu, nikoli záruka
náhodnosti při libovolném násobiteli. Statistickou kvalitu řeší §3.3.

Primární technické manuály potvrzují rozdíl popsaný na str. 15:
[DEC, 1982](https://www.bitsavers.org/pdf/dec/pdp10/1982_ProcRefMan.pdf),
str. 1–20/1–21 a instrukce MUL, používá v dolním slově 35 datových bitů
a opakované znaménko. [IBM System/370, 1975](https://bitsavers.org/pdf/ibm/370/princOps/GA22-7000-4_370_Principles_Of_Operation_Sep75.pdf),
instrukce MULTIPLY, str. 136, ukládá dolních 32 bitů součinu do lichého
registru, bez vyhrazení kopie znaménka. Vybrané původní strany a jejich
provenience jsou v `sources/dec-1982-processor-*` a `sources/ibm-1975-principles-*`.
Kontrolována instrukční specifikace, nikoli běh na historickém hardwaru.

## Úlohy 1–8

1. Protože `gcd(a,w)=1`, lze zvolit `c'=a^(-1)*c mod w`.
   Program `LDA X; ADD CPRIME; MUL A` dává v X správný zbytek i při
   přetečení mezisoučtu: redukce před násobením nemění výsledek modulo `w`.
   Při `c=a` je `c'=1` a lze použít INCA. Pokud je `X_0=0`, stav `w-1`
   vyvolávající přetečení má následníka 0. Jelikož jde o permutaci,
   první takové přetečení může nastat až při uzavření počátečního cyklu.
2. RANDM ukládá návratovou adresu pomocí STJ do adresního pole JNOV.
   LDA/MUL/SLAX/ADD/STA aktualizují stav a vynulují X. Je-li overflow
   vypnutý, JNOV se vrátí přímo; jinak ho vymaže a přes JMP se vykoná
   znovu. Návrat nastane nejvýše při druhém průchodu a s overflow off.
3. Předpokládá se `gcd(m,w)=1`, `0<=a,x<m<w`. Předpočítejme
   `a'=a*w mod m` a `m'=m^(-1) mod w`. Rozdělme `a'*x=z*w+y`,
   položme `t=m'*y mod w` a `u=floor(m*t/w)`. Dolní poloviny `m*t`
   a `a'*x` jsou obě `y`, takže jejich rozdíl je `(z-u)*w`.
   Po redukci modulo `m` a krácení jednotkou `w` dostaneme
   `a*x=z-u (mod m)`. Protože `0<=z,u<m`, stačí zápornému rozdílu
   jednou přičíst `m`. Všechna násobení používají pouze horní/dolní polovinu.
4. Dvojkový doplněk je jiná reprezentace týchž zbytků modulo `2^e`:
   vybírá interval `[-2^(e-1),2^(e-1)-1]`. Dolní bity součinu i součtu
   jsou stejné bez ohledu na interpretaci znaménka. Indukce tedy dává
   stejné bitové posloupnosti jako při nezáporných zbytcích.
5. Rozdíl `x-y` leží v `(-m,m)`, takže čtyřinstrukční program jen
   přičte `m`, je-li záporný. U součtu se nejdřív vytvoří `x-m`,
   potom se přičte `y`; mezivýsledek opět leží v `[-m,m)`.
   Všechno se vejde do slova, pokud `m<w`. Obrácené pořadí může přetéct.
6. Odčítání `c` je přičítání `(-c) mod m`; třída posloupností je stejná.
   Případná výhoda v samostatném odečítání z úlohy 5 není automaticky
   výhodou při sloučení s násobením. Odděleně lze zachovat overflow toggle.
7. Identity `z^(kr)-1=(z^k-1)*(1+z^k+...+z^((r-1)k))`,
   pro liché `r` analogická alternující suma pro `z^(kr)+1`,
   a `z^(2k)-1=(z^k-1)(z^k+1)` dokazují uvedené vzory.
8. Je-li `a*x=q*w+r`, pak modulo `w-1` stačí `q+r`, který je menší
   než `2w-2` pro `a,x<w`. Při přetečení ADD uloží `q+r-w`; INCA 1
   tedy odečte dohromady `w-1` a znovu nepřeteče. JNOV vymaže příznak.
   Nula a `w-1` se podle zadání pokládají za ekvivalentní. Pro jedničkový
   doplněk je kód záporného součinu kongruentní s jeho hodnotou modulo
   `w^2-1`; protože `w-1` dělí `w^2-1`, složení obou polovin s přenosem
   kolem dokola funguje i se zápornými operandy. Nejde o dva oddělené
   sign-magnitude registry MIX, nýbrž o doplňkový kód celého součinu.

## Tabulka prvočíselných rozkladů

Všech 92 položek [tabulky na str. 14](../images/vol2-p014.png) přepsáno
z původní sazby do [validátoru](../verify_modulus_table.py). Každý součin
se přesně rovná `2^e±1` nebo `10^e±1`, včetně násobností faktorů.
Prvočíselnost nebyla převzata pouze z knihovního predikátu: uložen je
rekurzivní Lucasův certifikát pro 179 prvočísel včetně pomocných.

Certifikát čísla `p>2` obsahuje úplný rozklad `p-1` a celé `g`, pro něž
`g^(p-1)=1 (mod p)` a pro každý prvočíselný faktor `q` čísla `p-1` platí
`gcd(g^((p-1)/q)-1,p)=1`. Pro libovolný prvočíselný dělitel `r` čísla
`p` má pak `g mod r` řád přesně `p-1`; tedy `p-1` dělí `r-1` a `r>=p`.
To dokazuje prvočíselnost `p`. Rekurze končí u 2. SymPy pouze hledá
rozklady; validace certifikátů používá součiny, modulární mocnění a gcd.
[Výsledek včetně všech certifikátů](../results/modulus-table.json).

## Úlohy 9–10: násobení s malými mezivýsledky

Pro `0<a<m` napišme `m=a*q+r`, kde `q=floor(m/a)>=1`, `0<=r<a`.
Položme `h=floor(x/q)`. Pak `x-(x mod q)=q*h`, a tedy
`a*(x-(x mod q))=(m-r)*h`, což dokazuje 9(a). Proto

```text
t=a*(x mod q)-r*h = a*x-m*h.
```

První součin je menší než `m`. Jestliže `r<=q`, je i druhý menší
než `m`: pro `r=0` je nulový, jinak `floor((m-1)/q)=a` a `r*h<=r*a<m`.
Proto `-m<t<m` a zbytek vznikne jedinou opravou záporného `t`.
Podmínka `a^2<=m` zaručuje `r<a<=q` a stačí pro 9(b).

Jestliže naopak `r>q`, zvolme `x=m-1`. Potom `h>=a+1` a
`r*h>=r*(a+1)>a*q+r=m`. Tento mezisoučin se nevejde do povolené
velikosti. Podmínka `r<=q` je tedy nutná i postačující pro bezpečnost
metody pro všechny `0<=x<m` (ne pouze pro správnost výsledku při
neomezené přesnosti).

Pro přesný počet takových násobitelů označme `t=floor(sqrt(m))`
a `d(m)` počet kladných dělitelů `m`. Pro `m>=2` jsou všechna `1<=a<=t`
bezpečná. Zbývající kandidáty pokryjí disjunktní celočíselné intervaly
`I_q=[m/q-1,m/q]`, `1<=q<=t`. Každý má jeden člen, navíc druhý právě
tehdy, když `q` dělí `m`. Započítají nepřípustné `a=m`, které odečteme.
Se skupinou `1,...,t` se překrývají v `a=t`, právě když
`m<=t^2+t`, a navíc v `a=t-1`, pokud `m=t^2`. Počítání dělitelů
do odmocniny dá `floor(d(m)/2)+[m=t^2]`; hranaté závorky zde znamenají
1 při pravdivé podmínce, jinak 0. Dostáváme přesně knižní vzorec

```text
2*t + floor(d(m)/2) - [m<=t^2+t] - 1.
```

Podmínka v hranaté závorce je pro celočíselné `m` ekvivalentní
`sqrt(m)-floor(sqrt(m))<1/2`. Pro `m=1` nejsou žádné násobitele;
vzorec dává 0 přímo. Počet byl nezávisle spočten pro všechna `m<=2000`.

## Úloha 11: obecná mez dvanácti operací

Po případném nahrazení `a` číslem `m-a` a závěrečném modulárním záporu
můžeme předpokládat `a<=m/2`. Pokud `a^2<=m`, použijeme přímo úlohu 9.
V ostatních případech položme

```text
s=floor(sqrt(m-1)),  u=ceil(a/s),  v=s*u-a.
```

Pak `a=s*u-v`, `0<=v<s<sqrt(m)` a `u<=s`. Poslední nerovnost
plyne z `floor(m/2)<=s^2` pro `m>=2` kromě `m=4`; výjimečné případy
`m<=4` už pokrývá přímá větev. Násobitele `s,u,v` lze tedy bezpečně
použít v metodě úlohy 9. Rozklad
`a*x = s*(u*x mod m) - v*x (mod m)` vyžaduje nejvýše tři takové výpočty.

Jeden výpočet potřebuje jedno dělení `h=floor(x/q)` a tři násobení
`q*h`, `a*(x-q*h)`, `r*h`, všechny výsledky menší než `m`.
Je-li `x<q`, dělení z povoleného modelu ani nepotřebujeme a vrátíme
rovnou `a*x`; nulové násobitele se rovněž vynechají. Ostatní kroky
jsou omezený počet odčítání modulo `m`, jak požaduje zadání.
Výsledkem je nejvýše dvanáct násobení a dělení. Tím také zpřesňujeme
heuristické `a'≈sqrt(m)-1` v odpovědi bez problému s malými moduly.

Pro příklad `m=2^31-1`, `a=62089911` je přesně
`a=3641*17053-62=883*70317`. Úplným výčtem dělitelů potvrzeno:
192 dělitelů `m-1`, z nich 86 vhodných trojic; 24 dělitelů `a`, z nich
pět neuspořádaných vhodných dvojic. Všechny podíly a zbytky ve vzorcích
na str. 545 souhlasí. Trojice potřebuje 7 násobení a 3 dělení (součiny
jedničkou se vynechají), dvojice 6 násobení a 2 dělení; počty odčítání
jsou 7 a 4. Změna pořadí dvojice v erratu 23. 12. 2024 zachovává
správnost; obě pořadí prošla kontrolou. Netvrdíme chybu původního pořadí.

Závěrečná otázka, zda lze obecně zlepšit 12 na 11 v daném modelu,
není součástí dokázané horní meze. Rešerše 1. 11. 2026 podle přesné
otázky a spojení Knuth/Schrage/twelve multiplications nenašla její
vyřešení. [Manuál autorů knihovny TRNG](https://www.numbercrunch.de/trng/trng.pdf),
§7, str. 117, stále popisuje mez dvanácti operací;
[uložený výňatek](../sources/trng-manual-excerpt.pdf). To je pouze
stav nalezených pramenů, nikoli důkaz, že zlepšení neexistuje.
Zrychlení pomocí širších registrů či jiných instrukcí není odpovědí
na přesný model operací z tohoto zadání.

## Errata a rozsah validace

Vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` i `err2.textxt`
prohledány 1. 11. 2026 podle str. 12–16, 543–547 a obsahu vzorců.
K textu a úlohám 1–11 patří:

- 26. 10. 1998: odstraněn chybný odkaz na úlohu 3 za programem (2).
- 29. 12. 1997: gramatická oprava zadání 9 na str. 16.
- 15. 9. 2011: přeformulování tvrzení o zapnutí overflow na str. 13.
- 23. 12. 2024: prohozeno pořadí násobitelů v posledním příkladu úlohy 11.

[Výsledky aritmetiky](../results/modulus-arithmetic.json): 299 520
kontrol modulo `w`, po 5440 pro oba postupy modulo `w+1` a pro `w-1`,
97 140 dvojic pro sčítání/odčítání, 48 540 redukcí pomocí půlsoučinů,
26 506 malých bezpečných násobení, počty pro `m<=2000`, 941 327 rozkladů
násobitele a 20 058 vstupů velkého příkladu včetně hranic a pevného seedu.
Právě prověřené matematické a instrukční postupy nevykázaly novou chybu.

Reprodukce (již prošla, bez nové změny neopakovat):

```sh
python3 workstreams/vol2/verify_modulus_arithmetic.py
python3 workstreams/vol2/verify_modulus_table.py
```
