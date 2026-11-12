# Chybějící podmínka u §1.3.3-22(c)

Pracovní označení: `arbitrary-function-expectation`.
Lokace: zadání s.183, část(c), první dvě věty; odpověď s.524, část(c).
Stav: `confirmed` ve smyslu důkazu a uvedených zdrojů; bez tvrzení
o prvenství a bez kontroly fyzického exempláře.

## Přesný problém

Zadání dovoluje „any function“ φ nekonečné posloupnosti počtů cyklů
a tvrdí, že její střední hodnota je (1-w) sum_{n≥0}w^n φ_n.
Zde φ_n znamená konečný průměr φ přes všechny permutace n prvků.
V Poissonově modelu z(a) lze mít φ_n=0 pro každé n, a přesto nemít
žádnou střední hodnotu Eφ. Nejde tedy jen o chybějící záruku konečnosti
pravé strany.

## Protipříklad

Fixujme w=1/2. Pro každé celé n≥2 jsou I_n=(n,0,0,…) cyklový typ
identity a J_n=(0,…,0,1,0,…) typ jediného n-cyklu (jednička v n-té
souřadnici). Všechny tyto typy jsou vzájemně různé. Definujme na celé
doméně posloupností nezáporných celých čísel

```
φ(I_n)= 2^n n!   (n≥2),
φ(J_n)=−2^n n    (n≥2),
φ(α)=0          ve všech ostatních případech.
```

Poslední řádek zahrnuje posloupnosti s nekonečným součtem sum m α_m,
které mají v modelu nulovou pravděpodobnost. Funkce je všude konečná,
reálná a měřitelná: její nenulový nosič je spočetná množina měřitelných
atomů. Nejde o spor týkající se měřitelnosti na nulové množině.

V S_n má I_n pravděpodobnost1/n! a J_n pravděpodobnost1/n. Pro n≥2
tedy φ_n=(2^n n!)/n!−(2^n n)/n=0; pro n=0,1 rovněž φ_n=0.
Pravá strana tvrzení v knize je dobře definovaná, absolutně konvergentní
řada samých nul, a má hodnotu0.

Ale P(N=n)=2^(−n−1). Kladná část φ^+=max(φ,0) dostává od I_n
příspěvek 2^(−n−1)(1/n!)(2^n n!)=1/2 pro každé n≥2.
Záporná část φ^−=max(−φ,0) dostává od J_n rovněž1/2. Proto

```
E φ^+ = +∞,    E φ^− = +∞.
```

Eφ tudíž neexistuje ani jako rozšířená reálná střední hodnota.
Odpověď(c) neoprávněně seskupuje členy do konečných bloků podle N,
uvnitř nichž se obě nekonečné znaménkové části navzájem ruší.

## Minimální oprava a důkaz opravené verze

Pro konečnou reálnou střední hodnotu stačí předpoklad E|φ|<∞.
Pak lze absolutně konvergentní součet přes všechny typy přeskupit
podle N a pravá strana je skutečně Eφ. Ekvivalentní explicitní podmínka
je sum_n(1-w)w^n E_n|φ|<∞. Samotná konvergence sum_n w^n φ_n
nepostačuje, jak ukazuje protipříklad.

Alternativně lze říci „any nonnegative function“, dovolíme-li hodnotu
střední hodnoty +∞. Všechny členy jsou potom nezáporné a přeskupení
je oprávněné monotónní konvergencí. Obecně stačí také existence alespoň
jedné konečné znaménkové části, ale tato formulace je pro učebnici delší.

## Dřívější konvence a posouzení

Přečten byl celý pravděpodobnostní výklad §1.2.10 na s.98–104.
S.98 definuje průměr jako sum k p_nk v konečné úloze; s.100 zavádí
generující funkce nezáporných celočíselných veličin; s.103 ztotožňuje
průměr a očekávanou hodnotu a definuje E. Žádná z těchto stran nestanoví
globální konvenci, podle níž by „any function“ automaticky znamenalo
integrovatelnou funkci. Na s.104 je u zobecněné Markovovy nerovnosti
naopak výslovně uvedena podmínka existence E f(X), místně pro toto
tvrzení. Tato místní kvalifikace se na pozdější cv.22(c) nevztahuje.

Práce Shepp–Lloyd1966 uvádí na s.341–342 obdobné podmínění pro
„some given functional“ bez explicitní podmínky integrability. To může
vysvětlovat původ formulace, ale samo to není konvence knihy a neřeší
konkrétní protipříklad. Je možné, že autor považuje existenci střední
hodnoty za implicitní. Nález hodnotím jako chybějící matematickou
hypotézu, ne jako nesprávný zákon podmíněné střední hodnoty.

## Errata a originály

Skeny s.183 a524 byly vizuálně přečteny. Kontrola všech čtyř vrstev
`errata/text/{all1-prepre,all1-pre,all1,err1}.txt` podle stran
183,524 i podle slov function, average, probability, expectation,
Shepp, Lloyd a integrability nenašla tuto opravu. Relevantní opravy:

* 9.9.1998 opravuje interpunkci P(n;k_1,k_2,…), nikoli část(c).
* 1.1.2006 opravuje j≥0 na j>0 ve čtyřech součinech odpovědi22.
* 29.3.2023 opravuje „for all n“ na „for all n≥1“ v příkladu φ=α_1.

Příslušné stránky originálů errat jsou uložené v `../images/`;
all1-pre neobsahuje k přidělenému rozsahu relevantní opravu.
Aktuálnost čtyř vrstev byla koordinátorem zkontrolována 1.11.2026.

## English ASCII draft

Page 183, exercise 1.3.3-22(c): The words "any function" need an
integrability qualification. For w=1/2, let I_n be the cycle structure
of the identity and J_n that of a single n-cycle. For n>=2, put
phi(I_n)=2^n n! and phi(J_n)=-2^n n, and set phi=0 elsewhere.
Then phi_n=0 for every n, so the displayed series converges to zero.
However, each n>=2 contributes 1/2 to each of E(phi^+) and E(phi^-),
so E(phi) is undefined. One could require E|phi|<infinity; alternatively,
nonnegative functions are allowed if infinite expectations are admitted.
