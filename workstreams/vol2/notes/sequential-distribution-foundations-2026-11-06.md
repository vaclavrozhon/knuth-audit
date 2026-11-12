# Souvislý průchod §3.5 A/B: distribuce posloupností

6. listopadu 2026, `V2-X0130`. Původní třetí vydání, první dotisk 1997;
tištěná strana +12 = strana souboru. Matematicky přezkoumány strany
149–158, úlohy 1–18, 22–25 a 28 a jejich odpovědi 592–596. Jde o 23
úloh včetně výzkumné 17, u níž se ověřuje pouze doložená část a formulace,
nikoli řešení otevřené otázky. Další text začíná na 159; stránky se
smíšenými odpověďmi se tím automaticky neuzavírají.

Všech 19 příslušných obrázků knihy znovu zobrazeno a přečteno. Kompletně
přečteny starší poznámky `distribution-foundations.md`, všech 92 řádků
jejich verifikátoru, celý výsledek a log. Výsledky nepocházejí z nového běhu.
Úplná obecná matematická argumentace je v původních poznámkách; níže je
záznam jejího přezkoumání, doplnění a přesných mezí.

## Výsledek a závažnost

Žádný nový nález. `C0059` i `C0060` obstály při kontrole sazby a všech
vrstev errat. U C0059 se mění závažnost **high → low**: chybné rovnosti
jsou lokální mezikrok, věta zůstává pravdivá. C0060 zůstává medium:
tištěná odpověď nedává požadovanou četnost. Ani jeden nález není tímto
prohlášen za dosud nikým neohlášený nebo ověřený v posledním dotisku.

- C0059, strana 153: pro `k=b=2`, všechny `u=0, v=1/4`, je vnitřní
  interval `[1/2,0)` prázdný, ale součin dvou záporných délek je `1/4`.
  Vnější rovnost pro `k=1,u=0,v=1` udává `1+1/b`, přestože hustota je 1.
  Druhý problém nezmizí volbou většího b. Stačí oříznout boxy na jednotkovou
  krychli a prázdnému boxu přiřadit objem 0. Vnitřní hranice
  `ceil(bu)/b, floor(bv)/b` a vnější `floor(bu)/b, ceil(bv)/b` sevřou
  cílový box; chyba délek jde k nule. Důkaz věty A tak platí obecně.
- C0060, odpověď 28 na straně 596: perioda `0001000111011101`, indexovaná
  od nuly, má na sudých místech `0,0,0,0,1,0,1,0`. Tedy `(X_n+U_n)/2`
  leží v horní polovině v jedné čtvrtině sudých míst, nikoli ve třech.
  Oprava `(1-X_n+U_n)/2` má požadovanou četnost. Doplnění bitů zachovává
  četnosti trojic a věta C dává rovnoměrné reálné trojice v každé fázi
  modulo 16. Proto oprava zachovává i požadovanou 3-distribuci.

Známé opravy na 149/150/151/153/155 a v odpovědi 6 na 593 jsou pouze
zohledněná errata. Podle nového pokynu uživatele se neprezentují jako
nálezy, nezvyšují počet chyb a nebarví stránky UI. Zvláště odkaz 5 → 4
na straně 151 je známý od 17. 9. 2017; nejde o další chybu k hlášení.

## Definice a obecné důkazy

Definice A–E rozlišují přirozenou hustotu od náhodného výběru celého indexu.
Rovnoměrné rozdělení na všech nezáporných celých číslech se nepředpokládá.
Konečná aditivita je správná, spočetná obecně selhává (úloha 6).
Střídání dolní a horní poloviny na straně 150 je ekvidistribuované, ale
nikoli 2-distribuované. Projekce oken a sloučení tříd dokazují (12)/(13).
Výrok o milionu nul má přesnou kladnou hustotu `2^(-1000000)`; nejde
o garantovanou vlastnost libovolného konečného vzorku.

Věta B platí pro omezené Riemannovsky integrovatelné funkce. Darbouxovy
horní a dolní schodovité funkce přenesou četnosti boxů na integrály.
Důsledek P používá k! stejných oblastí mimo hyperroviny shodných souřadnic.
V důsledku S je posun k kladný v kontextu definice; momenty jsou
`1/2,1/3,1/4` a jmenovatel limitně `1/12`. Konečný úvod s nulovým
jmenovatelem neovlivňuje limitu. Nulová korelace sama není nezávislost.

Věta C, strany 155–158: redukce na (m,m), lemma E i všechny vážené
součty (18)–(25) byly porovnány s původní sazbou. `m|q` je potřeba
v aritmetickém součtu (22). Pro výskyty slova délky m, `p=b^(-m)`,
průměr L indikátorů na nepřekrývajících se oknech má rozptyl
`p(1-p)/L`. Jensenova nerovnost v třídách modulo m dává
`limsup sum_j(p_j(N)-p)^2 <= m*p*(1-p)/L`. Po `L→∞` mají všechny
třídy limitu p. S normalizací knihy vyjde přesně
`p²/m + p(1-p)/(mL) = (q-m)/(qm b^(2m)) + 1/(q b^m)`.
Nejde o neodůvodněnou výměnu limit v N a q: nejprve je q pevné.

Nově získán a celý vizuálně přečten Casselsův článek 555–557,
[primární PDF](https://msp.org/pjm/1952/2-4/pjm-v2-n4-p06-s.pdf).
Jeho důkaz průměruje výskyty přes klouzající bloky délky s. Neobvyklé
bloky mají libovolně malý podíl; běžné bloky mají správné četnosti v každé
třídě. Hraniční rozdíl je nejvýše řádu s² a po dělení N mizí.
Použitý odhad pro běžné bloky plyne přímo z rozptylu součtu nezávislých
indikátorů v pevné třídě a Chebyshevovy nerovnosti. Není třeba znovu
otevírat Hardyho–Wrighta, aby byl tento potřebný krok doložen.

Citace Knutha **PJM 2 (1952), 555–557** souhlasí s vydavatelem a DOI
`10.2140/pjm.1952.2.555`. Samotný Casselsův sken má na první straně
rozpornou patičku „3 (1953)“ a v bibliografii uvádí Niven–Zuckerman
103–110. Tyto údaje z cizího článku nepřenášíme jako chyby TAOCP.
Niven–Zuckerman končí na 109 a Knuth uvádí správně 103–109.
Jejich celý text 103–109 znovu přečten; nově zobrazeny sazby 103 a 106.
OCR část vzorců ztrácí. Přesné ověření nese vlastní důkaz a sazba TAOCP;
netvrdíme novou kontrolu každého symbolu sedmistránkového primárního článku.

U věty F byl znovu přezkoumán celý vlastní důkaz v původních poznámkách.
Pro nenulový celočíselný polynom P a kompaktní interval `[a,b]`, `a>1`,
mimo kořeny P, jsou derivace `(θ^m-θ^n)P(θ)` pro velká m stejnoměrně
kladné a první roste alespoň jako `m*a^(m-1)`. Integrace po částech
omezuje křížový integrál `O(1/(m*a^(m-1)))`. Součet přes n<m je
absolutně konvergentní. Čtvercové průměry exponenciál tak mají integrál
`(b-a)/N+O(N^-2)`. Na `N=j²` stačí Tonelli a mezi čtverci omezenost
členů. Spočetné sjednocení výjimek přes P a intervaly dokončí Weylovo
kritérium pro téměř každé θ. Z algebraického vztahu `P(θ)=0` naopak
plyne, že takové θ nemůže být nekonečně distribuované.

Tvrzení „téměř všechna θ“ nedokazuje nic o konkrétním θ=π. Věta F
také neřeší ekvidistribuci jednotlivých racionálních mocnin z úlohy 17.

## Úlohy a odpovědi

1–4: periodická reálná posloupnost vynechá interval; číslicová může být
rovnoměrná. Perioda 0011 má všechny dvojice a chybí jí 111. Úloha 3
používá již ověřenou ternární periodu z §3.2.2-17; starý soupis se neopakoval.
Inkluze–exkluze je přesná pro konečné počty, takže stačí libovolné tři limity.

5–12: oscilující příklad má bloky délek 1,2,4,… a podíly s liminf 1/3,
limsup 2/3. Závorková hodnota 1/2 odkazuje na jiné, logaritmické
průměrování v §4.2.4; nejde o existující přirozenou hustotu. U 6
postačují singletony `n=j-1`. U 7 se hustota řádku sevře hustotou jeho
doplňku; spočetná aditivita se tím nepředpokládá. Sloučení tříd, lemma E,
projekce sudé podposloupnosti a objem `v^k-u^k` ověřují zbytek.

13–14: četnost mezer je hustota vzoru `p²(1-p)^(k-1)` dělená hustotou
zásahů p. Umělý začátek `f(0)=0` dává nejvýše jednu výjimku; rovnost
konečných počtů v odpovědi 13 se chápe až na tento úvod, limita je správná.
U běhů je hustota vzoru `k/(k+1)!-(k+1)/(k+2)!`; dělení hustotou sestupů
1/2 dává uvedený zákon. Shody sousedních hodnot mají nulovou hustotu.

15–16: Stanleyho synchronizační slovo `(b-1,…,0,0,…,b-1)` resetuje
každý stav sbírky na prázdný. Pravděpodobnost, že v M předchozích pozicích
není žádná pevně zarovnaná kopie, je nejvýše
`(1-b^(-2b))^floor(M/(2b))`. Stav proto lze aproximovat konečnou minulostí;
teprve z toho se smí odvodit jeho nezávislost na libovolném pevném
budoucím slovu. Stacionární tok dává hustotu začátků `1/(b*H_b)` a
kuponový zákon `b!*S(k-1,b-1)/b^k`; pro b=2 je to `2^(1-k)`.

17–18: pro r=p/q je `exp(2πi(qU_(n+1)-pU_n))=1`, takže podle Weyla
není posloupnost 2-distribuovaná. Druhá, výzkumná otázka se tím neřeší.
Změna členu menší než 1/n zachovává hustoty pevných boxů po sevření
o ε; `V_0` lze zvolit libovolně, protože konečný úvod nehraje roli.

22–25: Fourierovo kritérium pro boxy používá spojité horní a dolní
aproximace v integrálu, nikoli stejnoměrnou aproximaci nespojitého
indikátoru. Pro složené b v 23(b) zajistí primitivní vektor koeficientů
surjektivitu Bézoutova identita; není nutný jednotlivý invertibilní
koeficient. Obrácený směr plyne z konečné Fourierovy inverze.
V 24 nejprve fixujeme počet posunů K, pak N→∞ a teprve K→∞.
Polynomiální indukce snižuje stupeň; vyšší racionální koeficienty lze
odstranit rozdělením indexů modulo společný jmenovatel. V 25 je kladný
posun výslovný a ekvidistribuce zajišťuje kladný limitní rozptyl.
Úloha 28: potvrzení C0060 výše.

## Výpočty, bibliografie a pokračování

Přijaty uložené malé kontroly: 2 418 mřížkových intervalů; 65 536 členů
oscilujícího příkladu; 46 230 permutací běhů; 501 kuponových stavů;
97 632 kuponových slov v 18 modelech. Všechna pole výsledku a úplný
zdrojový kód přečteny. Obecné důkazy byly přezkoumány samostatně.
Žádná z těchto enumerací se znovu nespouštěla.

Explicitně přeskočeno nebo odloženo:

- Parafráze Lehmera 1951 a Franklina 1962 na straně 149, vlastní obsah
  von Misesovy knihy (errata 2024 mění bibliografický odkaz na rok 1928).
  Sken Lehmerova sborníku vrací webu 403; Franklinův primární PDF byl
  dříve nedostupný. JSTOR nyní ověřuje pouze článek 1963, 28–59, nikoli
  znění parafráze z roku 1962. Filozofický výklad není novým matematickým tvrzením.
- Současný stav důkazu normality π a racionálních mocnin nově nerešeršován.
  Dřívější omezená rešerše z 1. listopadu je pouze datovaný podklad;
  neprohlašujeme důkaz absence pozdější práce. Výzkumná otázka 17 není vyřešena.
- Historická zpráva na 158 o předvýpočtu 10 000 mocnin π a ukládání
  35 bitů nemá v tomto průchodu ověřený původní doklad. Strana 158
  zůstává partial také kvůli pokračující konstrukční otázce na 159.
- Přesná původní attributions Weyl 1914, van der Corput 1931, Knuth AMM
  1968 a Mahler 1957, osobní připsání řešení Stanleymu a kapitola
  Hardy–Wright nebyly zvlášť čteny. Potřebná matematika má vlastní důkazy.
- Závorkový vnitřní odkaz v odpovědi 5 na §4.2.4 se znovu zkontroluje
  při průchodu touto sekcí; přirozená hustota není změněna na logaritmickou.

Celostránkový záznam nově uzavírá 149–157 a 593; 158, 179–182,
592 a 594–596 zůstávají částečné v přesně popsaném rozsahu. Další krok:
§3.5 C/D od strany 159, včetně rozporových měr, výběrových pravidel,
Waldovy konstrukce a dosavadních C0061–C0070. Žádné emaily se netvoří.
