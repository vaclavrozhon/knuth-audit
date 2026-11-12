# V3-C0004 — označení rozptylu střídavých běhů

Drobná potvrzená chyba značení v odpovědi §5.1.3-16, tištěná 605 / file616,
řádek „Hence var(g_n) = (16n−29)/90, n≥4“. Sazba prohlédnuta v
images/multisets-file-616.png. Má být var(G_n).

Úloha 16 zavádí G_n jako generující funkci střídavých běhů. Malé g_n je
na s.38 definováno pro vzestupné běhy a jeho rozptyl je (n+1)/12. Např.
pro n=4 by uvedená věta tvrdila 7/18 místo správného 5/12. Samotný vzorec
(16n−29)/90 pro G_n je správný: po odečtení x_n² od y_n+x_n v předchozích
řádcích dostaneme právě tento výraz. Není zpochybněn výpočet ani výsledek
úlohy, jen použití již definovaného jiného symbolu.

Zkontrolovány all3-prepre/all3-pre/all3/err3 a historické odpovědi
585–587 v err3-1e. Oprava z 1.1.2006 na téže straně mění g_n(−1) na
G_n(−1) v pozdějším řádku; tento výskyt var(g_n) nepokrývá.
Výřezy: sources/runs-errata-review.json. Prvenství/fyzický výtisk neověřeny.
