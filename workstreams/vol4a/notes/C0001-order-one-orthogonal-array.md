# V4A-C0001 — chybějící n>1 v úloze 7–20?

Stav: **candidate**, nízký dopad. Není to potvrzený nález. Zbývá posoudit,
zda autor implicitně vyhrazuje pojem ortogonální pole pro n>1; explicitní
omezení v definici úlohy 7–18 nevidím. Předchozí úloha 7–19 n>1 výslovně má.

Místo: úloha **7–20, tištěná s.37 / file54**, a odpověď **7–20,
tištěná s.518 / file535**. Původní sazba obou míst zobrazena 6. 11. 2026:
`images/file054.png`, `images/file535.png`.

Definice 7–18 připouští při doslovném čtení pole řádu n=1 a hloubky m=2:

```
A = [0]
    [0]
```

Má n²=1 sloupec; jediná dvojice hodnot (0,0) se mezi dvěma řádky neopakuje,
tedy splňuje vytištěnou definici ortogonality. Nahrazení k výrazem
exp(2πik/n) však dá dva řádky (1). Jejich skalární součin je 1, nikoli 0
(s komplexním sdružením i bez něj). V odpovědi se použije součet n-tých
kořenů jednotky `sum(ω^k,k=0..n−1)=0`, který pro n=1 neplatí.

Pro n>1 argument funguje. Případná oprava tedy zní přidat „of order n>1“
do zadání, případně výslovně tuto konvenci uvést do definice pole.
Neoznačuji nic jako nově potvrzenou chybu, protože jde o hraniční konvenci.

Errata ověřena 6. 11. 2026 v lokálním archívu staženém 31. 10. 2026:
`errata/text/all4a-pre.txt`, `all4a.txt`, `err4a.txt`, `all4f0.txt`, `err4f0.txt`.
Hledány strany 37 a 518, „orthogonal“, „roots“, „unity“, „answer 20“,
„exer ise 20“ a změny n>1. V F0 jsou na s.37 pouze změny hodnocení úloh18/23;
4A na s.517 mění odpověď17 a doplňuje hodnoty latinského čtverce; aktuální
řada na s.519 mění bibliografii odpovědi23. K tomuto hraničnímu případu oprava
nenalezena. Strany F0 pro odpovědi se liší, proto se nehledalo jen číslo strany.
F1–F4 nepokrývají úvodní kapitolu; nevznikl tematický důvod je zapojit.
Tištěný fyzický výtisk a prvenství nejsou ověřeny. Žádný výpočet nebyl potřeba.
