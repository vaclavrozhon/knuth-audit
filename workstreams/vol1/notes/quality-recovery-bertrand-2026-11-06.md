# Úplný důkaz dostupnosti prvočísla pro Program P

§1.3.2, odpověď6 na512 odvozuje bezpečnost čtení tabulky z Bertrandovy
věty. Staré poznámky správně ověřily aplikaci, ale samotnou větu pouze
pojmenovaly. Zde je její elementární důkaz se všemi konečnými případy.
Nejde o nový nález v knize. Staré síto ani běhy MIXu se neopakují.

**Věta.** Pro každé celé n≥2 existuje prvočíslo p s n<p<2n.

## 1. Součin malých prvočísel

Označme P(x)=∏_{p≤x, p prvočíslo}p. Pro celé m≥1 platí

    P(m) ≤ 4^(m−1).

Důkaz silnou indukcí. P(1)=1 a P(2)=2≤4. Pro liché m=2k−1≥3
každé prvočíslo k<p≤2k−1 dělí binom(2k−1,k−1): čitatel obsahuje
jeden jeho násobek, oba faktoriály jmenovatele žádný. Proto

    P(2k−1) ≤ P(k) binom(2k−1,k−1)
             < 4^(k−1) 2^(2k−2) = 4^(2k−2).

Použitá ostrá mez binom(2k−1,k−1)<2^(2k−2) plyne z toho, že
v součtu všech binomických koeficientů 2^(2k−1) jsou dva stejné
prostřední členy a vedle nich další kladné členy. Pro sudé m=2k≥4
není m prvočíslo, takže P(m)=P(m−1)≤4^(m−2)≤4^(m−1).
Indukce je úplná; pro reálné x≥1 zvlášť platí P(x)≤4^x.

## 2. Centrální binomický koeficient

Položme C=binom(2n,n). Všechny binomické koeficienty jsou ≤C.
Dva krajní koeficienty mají součet2≤C; jejich spojením dostaneme
2n sčítanců, každý ≤C. Tedy

    4^n ≤ 2n C.

Mocnost prvočísla p v C je

    v_p(C)=Σ_{j≥1}(floor(2n/p^j)−2floor(n/p^j)).

Každý sčítanec je 0 nebo1, a pro p^j>2n je0. Pro každé p tudíž
p^v_p(C)≤2n. Příspěvek prvočísel p≤sqrt(2n) je nejvýše
(2n)^sqrt(2n); počet těchto prvočísel je totiž nejvýše sqrt(2n).

Pro p>sqrt(2n) může být exponent jen0 nebo1. Pokud navíc
2n/3<p≤n, je floor(2n/p)=2 a floor(n/p)=1, takže exponent je0.
Předpokládejme nyní, že mezi n a2n není prvočíslo. Samotné2n
je pro n≥2 složené. Všechna zbývající velká prvočísla v C tedy
leží nejvýše na2n/3; jejich součin je ≤P(2n/3)≤4^(2n/3).
I případné dvojí zahrnutí malých prvočísel tuto horní mez jen zvětší.
Dostáváme nutnou podmínku

    4^(n/3) ≤ (2n)^(sqrt(2n)+1),

tedy po logaritmu a dělení n

    (2/3) ln2 ≤ sqrt(2/n) ln(2n) + ln(2n)/n.                 (1)

Pro n≥512 obě funkce na pravé straně přísně klesají:
derivace ln(2n)/sqrt(n) má znaménko 1−ln(2n)/2<0,
derivace ln(2n)/n znaménko 1−ln(2n)<0. Na n=512 je pravá
strana přesně

    (1/16+1/512)·10 ln2 = (165/256) ln2 < (2/3) ln2,

protože495<512. To odporuje(1) pro všechna n≥512.

## 3. Všechny menší hodnoty

Použijme explicitní řetězec prvočísel

    2, 3, 5, 7, 13, 23, 43, 83, 163, 317, 631.

Každé další je menší než dvojnásobek předchozího. Je-li
2≤n<631, vyberme sousední a≤n<p z tohoto řetězce; potom
n<p<2a≤2n. To pokrývá zvlášť všechny2≤n<512.

Prvočíselnost každého členu byla přesně ověřena dělením všemi
prvočísly nejvýše jeho odmocnina. Tento seznam je úplný: složené
kladné celé číslo má prvočíselného dělitele nejvýše své odmocniny,
jak samostatně dokazuje odpověď6(a). Pro největší631 stačí
2,3,5,7,11,13,17,19,23; nenulové zbytky jsou uloženy pro každý člen
v `../results/quality-recovery-bertrand-chain-2026-11-06.json`.
Jediný nový drobný výpočet běžel s nice15. Nejde o opakované síto
prvních500 prvočísel ani o rozsáhlé vyčerpávání.

## 4. Přesná aplikace na Program P

Před zkoušením lichého N≥5 tabulka obsahuje všechna prvočísla <N.
Je-li N složené, jeho nejmenší prvočíselný dělitel je ≤sqrt(N)<N,
tedy už je v tabulce; smyčka jej najde dříve, než dojde za její konec.

Je-li N prvočíslo a p je předchozí prvočíslo, p≥3 a dokázaná věta
dává N<2p<p²+p. Nejpozději při testu dělitele p proto
Q=floor(N/p)≤p. Zbytek R není0, takže se N správně přijme.
Ani tento případ nepřečte první nevyplněnou položku tabulky.

Při dřívějším Q≤p a R>0 máme N=pQ+R<p²+p<(p+1)².
Všechny prvočíselné dělitele ≤p už algoritmus vyloučil; případný
zbývající dělitel je ≥p+1>sqrt(N), spor se složeností. Proto není
možné ani předčasné chybné přijetí. Počet kandidátů do každého
dalšího prvočísla je konečný. Existence libovolného počtu prvočísel
plyne také přímo z Euclidova součinu již nalezených prvočísel plus1.
Tím je dokončení matematického algoritmu a dostupnost každého čtení
prokázána obecně; konkrétní strojové kapacity do500. prvočísla
zůstávají zvláštní přesnou kontrolou Programu P.
