# C0092: iterace faktoriálu začíná pevným bodem2

**Confirmed**, 2.11.2026. TAOCP2,3.vydání,1.dotisk1997, §4.2.4,
poznámka za odpovědí19, tištěná str.623 (DjVu635).
[Originál](../images/vol2-p623.png) vizuálně zkontrolován v celé stránce
i zvětšení. Je vytištěno `2!, (2!)!, ((2!)!)!, ...` a následně otázka,
zda tato posloupnost má logaritmické zlomkové části.

Definujme a_0=2 a a_(n+1)=a_n!. Indukcí a_n=2 pro každé n, protože
2!=2. Všechny úvodní číslice jsou2. Například pro hranici r=2 je četnost
události `10 f_(a_n)<r` nulová místo kladného `log_10 2`. Otázka v
uvedené podobě tedy není otevřená: odpověď je záporná.

Ve všech čtyřech vrstvách `all2-prepre`, `all2-pre`, `all2`, `err2`
byly prohledány str.622/623 a výrazy factorial/Eureka; oprava této
posloupnosti nebyla nalezena. Historické erratum27.9.1999 opravuje
logaritmy v odpovědi19 na str.622, nikoli začátek této iterace.

Přirozená oprava musí zvolit počáteční celé číslo větší než2, například3
nebo4. Reprint Conway–Michael J. T. Guy v Eureka62, str.28–29, byl následně
vizuálně přečten. Článek „Pi in Fours“, označený jako původně publikovaný
v čísle25(1962), iteruje faktoriál od4 a zkoumá opakované odmocniny
výsledků. Jde o související hustotní otázku, ne doslovně tutéž formulaci
Benfordova zákona. Původní číslo25 nebylo získáno; z přetisku nelze
jednoznačně určit zamýšlenou opravu Knuthovy posloupnosti. Netvrdíme vyřešení netriviální
verze problému ani její současný publikovaný stav.

Poslední fyzický dotisk ani prvenství hlášení nejsou ověřeny. Návrh
hlášení je [zde](../reports/C0092-iterated-factorial-start-draft.txt), neodeslán.
