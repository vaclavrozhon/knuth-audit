# Asymptotika dam — úloha 7.2.2–15

Kontrola 1. listopadu 2026. Zadání na str. 55 a odpověď na str. 399 byly
znovu zobrazeny v původním PDF. **Nová chyba nenalezena.** Hodnota
σ ≈ 0.389068 je správně zaokrouhlená. Následující kontrola už není pouze
reprodukcí desetinného výsledku: obsahuje přesně přípustného racionálního
svědka a intervalové vyhodnocení dolní i horní meze.

## Co se bere z literatury a co bylo odvozeno zde

[Simkinův článek](sources/queens/simkin-2021.pdf), věty 1.1 a 1.2,
dává limitu Q(n)^(1/n)/n = exp(−α) a koncentraci rozmístění kolem jediné
optimální queenonové míry γ*. Tento hluboký výčtový a variační teorém zde
**používáme jako publikovaný vstup**; nepředstíráme nový nezávislý důkaz
všech pomocných vět jeho šedesátistránkového preprintu. Byla přečtena
formulace, definice normalizace, argument existence a jednoznačnosti maxima
z kompaktnosti a striktní konkávnosti a přechod od velkých odchylek k oběma
hlavním tvrzením. Ty odpovídají tomu, na co odkazuje knižní odpověď.

Ze Stirlingovy formule plyne (n!)^(1/n)/n → exp(−1). Proto

    (Q(n)/n!)^(1/n) → σ = exp(1−α).

Pro pevné ε ∈ (0,σ) je navíc ε < 1 a z definice této limity pro všechna
dostatečně velká n plyne

    ((1−ε)σ)^n < Q(n)/n! < ((1+ε)σ)^n.

To je právě zpřesnění uvedené v odpovědi. Znak ≈ v zadání zde neznamená
silnější tvrzení Q(n)/(σ^n n!) → 1; to kniha svým zpřesněním netvrdí.
Omezení ε < σ je zbytečně úzké, ale platné. „q.s.“ se v MPR, str. 11–12,
definuje superpolynomiálně malou pravděpodobností selhání. U této deterministické
nerovnosti je selhání pro velká n nulové, takže označení není nepravdivé.

Také věta o průměru všech řešení odpovídá koncentraci z věty 1.2. Je-li
d(γ_q,γ*) ≤ 1 a pravděpodobnost d ≥ ε exponenciálně malá, pak
E d ≤ ε + Pr(d ≥ ε). Konvexita supremové vzdálenosti d dává
d(Eγ_q,γ*) ≤ E d → 0. Není třeba předpokládat bodovou konvergenci hustot.

## Numerické meze: přesná kontrola zveřejněných svědků

[Nobel, Agrawal a Boyd](sources/queens/nobel-agrawal-boyd-2021.pdf), §3.3,
výslovně rozlišují numerický výpočet od racionální a intervalové certifikace,
kterou sami v tomto článku neprovedli. Jejich soubory `L_2048.npz` a
`U_1024.npz` byly převzaty z [původního repozitáře](https://github.com/cvxgrp/n-queens),
commit `666965da4dfb4da098ce2212ff2a5d9ef56c0c9d`; hashe jsou v
[manifestu](sources/queens/n-queens.source.json).

Výpočet [check_queens_constant.py](check_queens_constant.py) používá
python-flint 0.9.0 / Arb se 128bitovou přesností. Desetinné výpisy níže
jsou intervaly, nikoli počty platných cifer odhadnuté opakováním výpočtu.

**Dolní mez.** Všech 12 287 prvků duálního vektoru se načte jako přesná
dyadická racionální čísla, která dané binary64 soubory reprezentují.
Slabá dualita dává pro libovolné v

    L(v) = vᵀb − Σ exp((Aᵀv)_j − 1) + 4 log n + 2 log 2 + 3 ≤ α.

Velká řídká matice A se nesestavuje. Pro buňku (r,c) se součet čtyř
exponenciál rozloží na součin exp(R_r+C_c−1),
exp(a_(r+c))+exp(a_(r+c+1)) a
exp(d_(n−1+c−r))+exp(d_(n+c−r)). Koeficienty tohoto nezávislého přepisu
byly pro n=1,…,6 porovnány s původní řídkou maticí. Každá operace
včetně exponenciál a konečného součtu potom probíhá intervalově.

Výsledek pro n=2048:

    L(v) ∈ 1.9440007520197274311974566534358722 ± 5.20×10^−35.

**Horní mez.** Nestačí dosadit téměř přípustný desetinný vektor. Hustoty
čtyř trojúhelníků v každé buňce nejprve zaokrouhlíme na násobky 2^−30,
potom přesnou racionální projekcí opravíme všechny řádkové a sloupcové
rovnosti z [Knuthovy formulace Xqueenonů](sources/queens/knuth-xqueenons.pdf), str. 3.

Pro celočíselné matice P,Q nad jmenovatelem D definujme

    R_i = nD − Σ_j P_ij,
    T_i = nD − Σ_j Q_ij,
    C_j = 2nD − Σ_i(P_ij+Q_ij),  C = Σ_j C_j.

Nové čitatele jsou

    Y_P,ij = 2n² P_ij + 2n R_i + n C_j − C,
    Y_Q,ij = 2n² Q_ij + 2n T_i + n C_j − C,

se společným jmenovatelem 2n²D. Součty řádků každé matice jsou přesně n
a součty sloupců jejich součtu přesně 2n: stačí dosadit definice deficitů.
Takto opravíme dvojici N,S a transponovanou dvojici E,W.

Všech 4 194 304 opravených hustot je kladných. Diagonální nerovnosti
ΣNW, ΣSE, ΣNE, ΣSW ≤ 2n byly také ověřeny přesnými celočíselnými součty;
kontrolovány jsou i meze, které vylučují přetečení int64. Největší změna
proti původní hustotě je přibližně 5.20×10^−10. Jmenovatele hustot a
diagonálních rezerv jsou 2^51 a 2^62. Hash všech výsledných čitatelů je
uložen ve výsledku, takže svědka lze znovu vytvořit přímo ze zdrojového NPZ.

Tím vzniká skutečná přípustná Xqueenonová míra. Její záporná Q-entropie
je horní mezí α. Integrály funkce g(x)=x log x podél úseček počítáme
intervalově pomocí primitivní funkce H(x)=x² log(x)/2−x²/4,
se zvláštním ošetřením stejných konců a nuly. Kontrola uniformní míry
pro n=1,…,6 dává přesně hodnotu 2, jak má.

Výsledek pro n=1024:

    U ∈ 1.944001081309223136616683610690059 ± 8.22×10^−34.

Obě meze tedy rigorózně potvrzují uváděný širší interval

    1.944000752 < α < 1.944001082,

a jeho převodem dostáváme

    0.389068023905406729… < σ < 0.389068152297875803… .

Celý interval leží mezi 0.3890675 a 0.3890685. **Zaokrouhlení na šest
desetinných míst je proto jednoznačně 0.389068.** Výsledek neopravuje
knihu; zpřesňuje sílu naší kontroly jejího správného údaje.

[Certifikát a metadata](results/queens_constant/certificate-run.json),
[log](results/queens_constant/certificate.log). Běh trval přibližně 28 sekund.
Rozsah certifikace: přesná přípustnost a rigorózní numerické meze při užití
publikovaného výčtového a variačního teorému. Optimalitu zveřejněného
numerického řešení není nutné dokazovat ani znovu hledat Newtonovou metodou.

## Errata a bibliografie

Oficiální `err4b.textxt` uvádí dvě **známé aktualizace citací** odpovědi 15:
4. července 2025 nahrazuje Simkinův preprint článkem v *Advances in Mathematics*
427 (2023), 109127:1–83; 9. května 2023 nahrazuje druhý preprint článkem
v *Optimization Letters* 17 (2023), 1229–1240. Matematické znění ani konstantu
tyto položky nemění. Errata fasciklu 5 obsahují dřívější vložení Simkinova
výsledku do úlohy 15. Datum a rozsah preprintové verze uvedené ve starší
knize tedy nejsou novým bibliografickým nálezem.
