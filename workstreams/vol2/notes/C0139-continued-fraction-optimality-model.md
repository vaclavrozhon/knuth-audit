# V2-C0139: kvalifikace optimality v odpovědi 4.5.3-46

Stav: **candidate**, interpretační otázka. Knižní horní mez
O(n (log n)^2 log log n) pro celočíselný gcd je správná.
Není zde doložen protipříklad k žádné přesně formulované
Strassenově větě.

Odpověď 656 v celočíselném kontextu dodává, že Schönhageův
algoritmus je asymptoticky optimální pro výpočet řetězového
rozvoje vzhledem k počtu násobení a dělení. Odkazuje na
V. Strassen, SICOMP 12 (1983), 1–27. Původní knižní strana
byla vizuálně přečtena; všechny čtyři vrstvy errat i aktuální
TeX byly prohledány bez nalezené kvalifikace této věty.

Vydavatelský abstrakt Strassenova článku výslovně popisuje
podíl polynomů. Z dostupného textového přepisu původního
článku byly přečteny strany 1–3 a závěrečný oddíl 6,
zejména formulace 6.4, 6.6, 6.8 a 6.9. Jejich vstupy jsou
dvojice polynomů nad tělesem. Strana 2 výslovně počítá jen
neskalární násobení a dělení; lineární operace jsou zdarma.
Základní dolní mez předpokládá algebraicky uzavřené těleso,
další formulace mají přesně vyjmenovaná rozšíření.

Na straně 2 autor také odlišuje původní celočíselné algoritmy
Lehmera, Knutha a Schönhageho od překladu do polynomiálního
prostředí, který připisuje Moenckovi. Knižní věta tedy
potřebuje alespoň vysvětlení, zda má na mysli tento
polynomiální analog, nebo jinou doloženou celočíselnou větu.

Samotná algebraická dolní mez se na bitovou složitost celých
čísel nepřenáší. Také doslovný model s bezplatnými celočíselnými
součty, odečty a porovnáními by měl jiný obsah: jednotlivé
podíly lze získávat opakovaným odečítáním, aniž by se použila
samostatná instrukce násobení či dělení. Tento příklad pouze
ukazuje nutnost specifikovat model; nenapadá Strassenovu
algebraickou větu.

Proto kandidáta zatím nepovyšujeme na confirmed. Přirozené
zpřesnění by mluvilo o polynomiálním analogu a algebraickém
modelu. Před případným hlášením je vhodné získat obrazový
originál nebo další autorovu formulaci k celočíselnému případu.
Vydavatel poskytuje abstrakt, nikoli celý text; veřejný sken
časopisu byl dostupný v textovém webovém přepisu, ale přímé
stažení selhalo na síťovém spojení a screenshoty timeoutem.
Vizuální kontrolu tohoto externího originálu tedy netvrdíme.

Poslední fyzický dotisk a priorita nejsou ověřeny. Návrh
dotazu je neodeslaný. Metadata zdrojů jsou v
sources/euclid-fast-gcd.json.
