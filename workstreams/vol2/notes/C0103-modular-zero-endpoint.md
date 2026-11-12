# V2-C0103: neznormalizovaná nula v modulárním násobení

**confirmed**, 2.11.2026. TAOCP 2, třetí vydání, první dotisk 1997,
§4.3.3, zadání pomocného problému na str.304 a rovnice (32)/(33) na
str.305. Originály [304](../images/vol2-p304.png) a
[305](../images/vol2-p305.png) byly vizuálně přečteny.

Označme M=2^f−1. Pro nesoudělná kladná e<f a nezáporné u<2^f má
postup vrátit `(c u) mod M`, kde `(2^e−1)c ≡ 1 (mod M)`.
Operace mod zde znamená nejmenší nezáporný zbytek, tedy číslo menší než M.
Pomocné číslo b je nejmenší kladná inverze e modulo f; jeho binární
zápis je b_s...b_0. Rovnice (32) začíná `u_0=u, v_0=b_0 u` a jako
výsledek vrací v_s.

Nejmenší přípustný protipříklad je

```
e=1, f=2, M=3, u=3,
b=1, s=0, c=1.
```

Vstup splňuje u<4 a gcd(e,f)=1. Inicializace dává v_0=3. Žádný další
krok se neprovede, takže výsledek je 3, zatímco `(1*3) mod 3=0`.
Stejná chyba nastává pro každé e=1,f>=2,u=2^f−1. Modulární inverze
čísla 2^e−1=1 existuje; protipříklad nepoužívá neexistující inverzi.

Také invariant (33) pro k=0 není při u=M doslova pravdivý ani pro
e>1: například e=2,f=3,u=7 dává u_0=7 místo zbytku0. V tomto druhém
příkladu už další krok výsledný zbytek opraví.

Možné opravy:

- V pomocném problému na str.304 zpřísnit mez na `u<2^f−1`.
- Nebo v (32) použít `u_0=u mod M`, `v_0=b_0 u_0`.

Druhá oprava zachovává celý deklarovaný vstupní rozsah a stojí O(f).
Vlastní metoda převodu z modulárního zápisu už používá normalizované
zbytky menší než M; její správnost tímto hraničním problémem zpochybněna
není. Jde o přesně vymezenou chybu samostatně formulovaného pomocného
postupu a počátečního případu invariantu.

`verify_fast_modular.py`, checkpoint `inverse`, ověřil všechny vstupy
pro 2<=f<=12 a všechna nesoudělná 1<=e<f: 46132 případů. Původní
výstup selhal přesně v jedenácti uvedených koncových případech;
opravený postup prošel všemi. Navíc 224 celých průchodů kontrolovalo
každý invariant proti nezávisle sečtené geometrické řadě a 108 větších
případů prošlo až do f=16384. Obecný důkaz je v
[fast-modular.md](fast-modular.md).

Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` byly
prohledány podle stran304/305, rovnic32/33 i popisu inicializace.
Známá oprava ze7.2.2000 přidává nesoudělnost e,f. Opravy ze6.10.2025
mění vstupní zbytky w_j a počet operací v převodu, nikoli mez u<2^f
v pomocném problému ani (32). Původní sazba těchto errat byla zobrazena
v `classical-errata-all2-prepre-17.png` a `fast-errata-all2-p7.png`.

Poslední fyzický dotisk, priorita a případná odměna neověřeny.
Anglický návrh zůstává neodeslaný.
