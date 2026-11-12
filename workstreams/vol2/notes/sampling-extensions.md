# §3.4.2: přeskakování, permutace a kompaktní vzorky

Kontrola 1. listopadu 2026 navazuje na [S/R](sampling.md). V tomto bloku
jsou dokončeny původní úlohy 1–4,8,10,12,13,15,17 a matematika algoritmu P.
Úlohy 5–7,9,11 byly hotové dříve a jejich úspěšné kontroly se neopakovaly.
Úlohy 14,16 a doplněné 18,19 se dokončí samostatně. Kontextové citace
promíchávání zatím nejsou tímto blokem uzavřeny.

Sazba 142–148 a odpovědi 590–592 byly zobrazeny. Původní inventář je 17
úloh, all2-prepre přidává 18 a19. Relevantní změny: 20.8.2001 zbytek modulo
místo „division“ v P3; 17.3.2001 P místo S na str.146; 23.2.2012
posloupnost místo množiny v zadání P; 29.6.1999 odečtení X+1 od N v odpovědi8;
17.9.2011 závorky v součinu8(c); 1.1.2008 x−1 v odpovědi13. Všechny čtyři
vrstvy errat i aktuální TeX byly prohledány. Tento blok nepřidává nový nález.

## S: podmíněné pravděpodobnosti a úlohy 1–4

N je počet záznamů, n velikost vzorku, t počet již zpracovaných záznamů
a m počet dosud vybraných; E označuje střední hodnotu. Binomický koeficient C(a,b) počítá b-prvkové
podmnožiny a-prvkové množiny; mimo 0<=b<=a jej definujeme jako nulu.
Pravděpodobnost dalšího přijetí plyne z poměru
`C(N−t−1,n−m−1)/C(N−t,n−m)=(n−m)/(N−t)` pro dosažitelný stav.
Je-li n−m=N−t, přijetí je jisté; algoritmus se proto nemůže dostat za konec.

Pro účely rozdělení po čase t dokončený vzorek rozšíříme imaginárními
odmítnutími. Pak p(m,t), pravděpodobnost m výběrů z prvních t, splňuje

```text
p(m,t+1) = p(m−1,t)*(n−m+1)/(N−t)
           + p(m,t)*(N−t−n+m)/(N−t).
p(m,t) = C(t,m)*C(N−t,n−m)/C(N,n).
```

Druhý vzorec splňuje první dosazením a Pascalovou identitou; počáteční
p(0,0)=1 souhlasí. Máme E[m]=tn/N, a proto nepodmíněná pravděpodobnost
přijetí dalšího záznamu je `E[(n−m)/(N−t)]=n/N`. To vysvětluje úlohu3.
Podmíněné pravděpodobnosti jednotlivých kroků nemusí být stejné.

Úloha10 nahrazuje odkazy R přímo n záznamy v paměti. Stejná volba M
nahradí M-tý záznam. Je to přesně původní tabulka odkazů s dereferencí;
rovnoměrnost již dokázaná pro R se nemění. Pokud je třeba zachovat původní
pořadí, lze s každým záznamem uložit i jeho vstupní index a na konci je seřadit.

## Úloha8: přesné rozdělení a vlastní úplný důkaz O(1)

X je počet přeskočených záznamů před prvním výběrem, tedy 0<=X<=N−n.
Pravděpodobnost, že prvních k záznamů chybí, a bodová pravděpodobnost jsou

```text
T(k) = Pr(X>=k) = C(N−k,n)/C(N,n),
f(k) = Pr(X=k) = C(N−k−1,n−1)/C(N,n).
```

Počáteční T(1)=(N−n)/N a vztah
`T(k+1)/T(k)=(N−n−k)/(N−k)` dávají algoritmus8(b) s jedním U a O(X+1)
operacemi. O(X) v textu popisuje počet iterací po konstantní inicializaci.
Součin `product_{j=0}^{n−1}(N−j−k)/(N−j)` je T(k); to dokazuje minimum
nezávislých diskrétních veličin v8(c). Za hranicí podpory bereme příslušný
faktor jako nulu. Po výběru se n sníží o1 a N oX+1, jak říká oprava1999.

Následuje vlastní varianta odmítacího důkazu8(d). Neprohlašujeme ji za
řádkovou reprodukci optimalizovaného Vitterova programu. Pracujeme v obvyklém
modelu knihy, kde reálná aritmetika, mocnina a rovnoměrná veličina stojí O(1).
Čas fyzického přečtení X záznamů ani bitovou složitost přesné aritmetiky
tento model nezahrnuje.

Pro n=1 je X rovnoměrné celé číslo 0..N−1. Pro n>N/2 lze použít8(b),
neboť E[X]=sum_{k>=1} T(k)=C(N,n+1)/C(N,n)=(N−n)/(n+1)<1. Zbývá 2<=n<=N/2. Nechť U,W jsou nezávislé
rovnoměrné veličiny v (0,1) a definujme spojitého kandidáta Z a jeho hustotu g:

```text
Z = N*(1−U^(1/n)),  K=floor(Z),
g(z) = (n/N)*(1−z/N)^(n−1),  0<z<N,
c = N/(N−n+1).
```

Pokud K>N−n, kandidáta ihned odmítneme. Jinak přijmeme s pravděpodobností
`f(K)/(c*g(Z))`. To je platná pravděpodobnost: pro k<=N−n,z∈[k,k+1]

```text
f(k) = (n/N)*product_{j=1}^{n−1}(1−k/(N−j))
     <= (n/N)*((N−k−1)/(N−1))^(n−1)
     <= (N/(N−1))^(n−1)*g(z)
     <= c*g(z).
```

Poslední krok je Bernoulliho nerovnost
`(1−1/N)^(n−1)>=1−(n−1)/N`. Integrací přes každý jednotkový interval
je pravděpodobnost přijetí K=k v jednom pokusu f(k)/c. Celkové přijetí
má pravděpodobnost1/c a výsledek správné f. Odmítnutí má přesně
(n−1)/N=O(n/N), jak požaduje knižní odpověď.

**Rychlá dolní mez.** Položme

```text
epsilon(k) = k*n*(n−1)/(2*(N−n+1)*(N−k)),
L(k) = max(0,1−epsilon(k))/c.
```

Pro platné k jsou následující faktory v [0,1]:

```text
f(k)/g(k) = product_{j=1}^{n−1}
            (1−j*k/((N−j)*(N−k))) >= 1−epsilon(k).
```

Použili jsme `product(1−a_j)>=1−sum a_j` a
`sum j/(N−j)<=n(n−1)/(2(N−n+1))`. Protože g je nerostoucí,
`L(k)<=f(k)/(c*g(z))`. Jestliže W<=L(K), můžeme ihned přijmout. Jen jinak
spočítáme f(K) přesný součinem délky K:

```text
f(k) = n/(N−k) * product_{j=0}^{k−1}(N−n−j)/(N−j).
```

**Očekávaná cena.** Podíl pokusů vyžadujících součin je nejvýše
`(1−1/c)+epsilon(K)/c`. Z toho počet jeho násobení v jednom pokusu má
střední hodnotu nejvýše

```text
(1−1/c)*E[K]
 + n(n−1)/(2N)*E[K²/(N−K)]
<= (n−1)/(n+1) + 1 < 2.
```

Poslední krok plyne z K<=Z, monotónnosti z²/(N−z), a dvou beta integrálů
`E[Z]=N/(n+1)`, `E[Z²/(N−Z)]=2N/(n(n−1))` pro n>1.
Odmítnuté pokusy se opakují nezávisle, jejich počet má průměr c<2.
Celková očekávaná délka drahých součinů je tedy <4; ostatní práce je
konstantní na pokus. Tím je O(1) dokázáno rovnoměrně v obou parametrech,
ne pouze z faktu, že pravděpodobnost odmítnutí je malá.

[Autorský katalog J. S. Vittera](https://www.ittc.ku.edu/~jsv/Papers/catalog/5SAMPLING_HISTOGRAMS.html)
potvrzuje všechny tři citace v odpovědi8: CACM27(1984),703–718;
TOMS13(1987),58–67; TOMS11(1985),37–57. Čteny bibliografické záznamy
s autorskými abstrakty. Vlastní důkaz výše nevyžaduje převzetí jejich
programových optimalizací.

## P a úloha12: obě transpoziční reprezentace

Transpozice (a,j) vymění pozice a,j, přičemž (j,j) je identita. V P se
j snižuje od t do2. Před každým krokem je prvních j dosud neumístěných
prvků; volba k rovnoměrná v1..j umístí každý z nich na pozici j stejně
pravděpodobně. Indukcí každá permutace má pravděpodobnost
`1/(t*(t−1)*...*2)=1/t!`. Obráceným čtením pozic zjistíme jedinou historii
voleb. Pro duplicitní hodnoty lze označit původní pozice; odstranění značek
dá rovnoměrné různé multisetové permutace, každá se stejnou násobností.

Také varianta s rostoucím j je správná: vloží nový prvek j na rovnoměrnou
pozici k a starý prvek této pozice přesune na konec. Z každého výsledku
lze jednoznačně odstranit j a získat předchozí permutaci. Když k=j,
operace pouze zapíše j na konec; v implementaci netřeba číst neinicializovanou
paměť. Prázdný případ lze obsloužit předem; pro t=1 je výsledek identita.

Pro úlohu12 skládáme funkce zprava doleva. Nechť tau_j=(a_j,j) a
`gamma_j=tau_2...tau_j`, takže gamma_t je inverzí permutace v zadání.
Po prvním rostoucím cyklu odpovědi je tabulka b právě gamma_t. Při
sestupném cyklu na indexu j obsahuje její prefix gamma_j; zejména
b[a_j]=j a b[j]=gamma_(j−1)(a_j). Přiřazení b[a_j]←b[j] obnoví prefix
gamma_(j−1), zatímco konečnou hodnotu b_j=gamma_(j−1)(a_j) ponechá na
pozici j. Pro a_j=j je obojí j. Jelikož gamma_(j−1) fixuje j, platí

```text
gamma_(j−1)*(a_j,j) = (b_j,j)*gamma_(j−1).
```

Indukcí gamma_t=(b_t,t)...(b_2,2); po inverzi dostaneme přesně požadovaný
opačný rozklad. Jednoznačnost plyne z jednoznačnosti P aplikovaného na
inverzní permutaci. Oba cykly mají čas O(t).

Omezení na počet seedů je prosté počítání obrazů deterministické funkce:
m počátečních stavů může dát nejvýše m permutací. Přesně
`13!/2^32=6081075/4194304=1.4499...`, tedy tištěné1.45 souhlasí.
Alespoň t! dosažitelných seedů je nutná podmínka, nikoli postačující
podmínka rovnoměrnosti. Totéž omezení platí i pro generátor s více slovy stavu.

## Úloha13: perfektní prokládání a řezy

Očíslujme pozice0..m−1, m=2n−1. Perfektní proložení posílá pozici x
na2x modm, řez na x−1 modm, jak opravuje erratum2008. Jakákoli kompozice
je tedy afinní mapa `x↦2^a*x+b modm`. Označme h nejmenší kladné číslo
s2^h=1 modm (multiplikativní řád2). Všech m*h takových map je dosažitelných
a různých: b poznáme z obrazu0, 2^a z rozdílu obrazů1 a0. Eulerova věta
dává h<=phi(m)<=m−1, tedy požadovaný počet nejvýše(2n−1)(2n−2).
Změna znaménka řezu nemění počet map; při skládání funkcí zprava doleva
platí s∘c=c²∘s.

## Úloha15: Dahlova úsporná simulace

Položme d=t−n. Požadujeme jen posledních n výstupů P a dovolíme navíc
neškodnou identickou výměnu při j=1, pokud n=t. Není třeba alokovat t buněk.

Před krokem j nezměněné malé pozice mají svou původní hodnotu k.
Pokud již pozice k<=j svou původní hodnotu nemá, její hodnota je >j:
výměna s vyšší pozicí přinese právě takovou hodnotu a pozdější kroky tento
invariant zachovávají. Udržujeme n buněk Y pro d<k<=t a n hotových
výstupů X. Aktivní vysoké pozice k<=j zastupuje Y_k; aktivní malá pozice
k<=d, která už byla změněna, má právě jeden odkaz z dříve vydaného X_i=k,
i>j, a její současná hodnota je Y_i.

To přímo dává tři větve tištěného algoritmu. Je-li k>d, hodnotu čteme
zY_k. Má-li malé k existující odkaz, čteme a přepíšeme Y_i. Jinak má
stále identickou hodnotu k; jejím vydáním X_j=k vzniká nový odkaz a
Y_j už obsahuje hodnotu, která se přesune z pozice j na k. Každou výměnu
proto simulujeme přesně. Zpracování k=j je také správné. Ukládáme O(n)
hodnot; případná tabulka odkazů má nejvýše n klíčů. Zadání15 nepožaduje
zvláštní časový odhad pro jeho konkrétní symbolovou tabulku.

## Úloha17: Floydova indukce

Před krokem j je S rovnoměrná (r−1)-prvková podmnožina1..j−1,
kde r=j−N+n. Pro cílovou r-prvkovou množinu A neobsahující j může poslední
nový prvek být kterýkoli z r prvků A; předchozí množina je pak jednoznačná.
Pro A obsahující j musí předchozí množina být A bez{j}; novou hodnotu j
dostaneme pro každé k z této množiny i pro k=j, opět r možností.
Obě pravděpodobnosti jsou
`r/(j*C(j−1,r−1))=1/C(j,r)`. Indukce dokazuje rovnoměrnost; kolize vždy
přidá dosud nepoužité j, takže velikost opravdu naroste o1.

## Reprodukovatelné kontroly

[Verifier](../verify_sampling_extensions.py), [JSON](../results/sampling-extensions.json)
a [log](../results/sampling-extensions.log), běh97038 exit0:

- 163064 přesných pravděpodobností prefixu;11480 mezer a inverzních intervalů.
- 1128 modelů dolní/horní meze,73696 racionálních sond; přesný očekávaný
  počet faktorů drahého součinu kontrolován pro každý model. Globální důkaz
  je výše, sondy jej nenahrazují.
- 46233 všech vektorů voleb až do t=8: bijekce P, opačný rozklad a
  rostoucí varianta. Pro šest prvků s třemi dvojicemi duplicit90 výsledků
  s přesnou násobností8.
- 21753 Dahlových historií a115137 kontrol invariantu proti plnému poli.
- 15 úplných skupin perfektních proložení a řezů,3237 dosažitelných
  uspořádání, nezávisle proti afinním mapám.
- 16278 mezistavů Floydovy metody, představujících1421542628 úplných
  historií; každá r-podmnožina má přesně r! historií.
