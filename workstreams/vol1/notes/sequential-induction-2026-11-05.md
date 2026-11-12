# Souvislý průchod §1.2 a §1.2.1

5. listopadu 2026. Přímo zobrazeny a přečteny původní strany 10–21
(obrazy 25–36) a odpovědi 468–469 (483–484). Na stranách 21 a 469
už začíná §1.2.2: kontrola této části pokračuje samostatně, takže tyto
dvě stránky nejsou tímto záznamem uzavřeny celé. Žádný starý dlouhý
výpočet ani inference Z3 se znovu nespouštěly.

## Matematika a návaznost dřívějších důkazů

Přečteny celé `notes/induction.md`, `notes/assertion-tool-root-review.md`,
`notes/well-ordering-root-review.md` a vymezení jazyka a zvukovosti
v `parallel/induction-assertion-followup/notes/language-and-soundness.md`.
Zachovány jejich meze: obecné matematické argumenty nejsou totéž jako
konečný výčet vstupů; externí výsledky o forcingu nejsou celé znovu dokázány.

- Strany 10–12: úvodní odkazy na následující oddíly odpovídají soupisu.
  Princip silné indukce a diagram I mají základ v 1 a klesající vzdálenost
  n−k. Text na 17 výslovně přiznává, že tento diagram nezakládá indukci
  bez příslušného axiomu o přirozených číslech. Součet lichých čísel,
  seznam sedmi rozkladů čísla 5 a hodnoty p(1),…,p(7) souhlasí s důkazem
  a dříve uloženou přesnou kontrolou. Doplněné p(0)=1 znamená prázdný rozklad.
- Strana 13: obrázek má šest vrstev 1,3,…,11. Fibonacciho horní mez používá
  dva výslovně ověřené základy, nikoli nepovolený předpoklad P(0).
  Platí φ²=φ+1; vytištěné 1<1.6<φ je také správné. Pozdější úpravy
  těchto vět nejsou nově nalezené matematické chyby.
- Strany 14–16: všechny čtyři řádky tabulky, pořadí sekvenčních přiřazení
  a aserce A1–A6 souhlasí s rozšířeným Eukleidovým algoritmem. Kontrolní
  rovnost je 8845−8816=29. Invarianty zachovávají gcd a Bézoutovu rovnost;
  pro ukončení je navíc potřeba klesání kladného d. Při větvení platí jen
  aserce skutečně zvolené hrany, jak opravuje známé X0026.
- Rozšíření na Z[√2] v textu používá celočíselné podíly a nemusí skončit.
  Pro 1 a √2 by poslední nenulový zbytek při ukončení dal racionální poměr
  vstupů, což je spor. Alternativní metoda v odpovědi 12 dovoluje podíly
  v celém okruhu: zaokrouhlením obou koeficientů na nejbližší celá čísla
  získá |N(r)|≤|N(d)|/2<|N(d)|. To je jiná, konečná metoda. Tisk na 16
  vynechává d ve výčtu rozšířených proměnných; jde o známou opravu z roku 1999.
- Úlohy 1–13: důkazy a odpovědi byly porovnány s původními obrazy.
  Záměrné chybné důkazy v úlohách 2 a 3 nejsou chybami knihy.
  U úlohy 9 je na obrazu neostrá nerovnost; rozšíření na záporné celé n
  má samostatný sestupný indukční krok. Teleskopický rozklad úlohy 11
  a hodinové meze úlohy 13 souhlasí. Chybějící člen obrázku 5 a n=0
  v zadání 13 zůstávají známými opravami X0027/X0028.
- Úloha 14: X0707 už obsahuje skutečný obecný nástroj pro vymezený jazyk,
  úplný výčet cest mezi řezovými body a důkaz částečné správnosti.
  Požadovaný příklad E přijímá pouze A1,A4,A6; shoda doplněných A2,A3,A5
  je doložena obousměrnými implikacemi. Zadání žádá pokus o doplňování
  asercí, nikoli rozhodovací algoritmus pro všechny programy. Naše
  certifikace obecně nedokazuje ukončení; u E je ukončení zvlášť doloženo.
- Úloha 15: přijat obecný důkaz částí (a)–(g), včetně závislé volby u
  obrácení tvrzení o nekonečném sestupu. U poznámky 15(c) zůstává výslovné
  čtení X0718: jedna formule bez parametrů, o níž samotné ZFC dokazuje,
  že dobře uspořádává reálná čísla. Přijetí tohoto čtení nepotvrzuje
  neurčené historické tvrzení „nobody has yet“ ani všechny možné významy
  slova explicitní. Historická část odpovědi proto není obecně ověřena.

## Bibliografie a fakta

Metadata *Concrete Mathematics*, druhé vydání, Graham–Knuth–Patashnik,
Addison-Wesley, 1994, ověřena na
[autorově stránce](https://www-cs-faculty.stanford.edu/~knuth/gkp.html).
Obsah celého druhého vydání tohoto zdroje se tím neprohlašuje za přečtený.

[Vydavatelský záznam Golombova článku](https://www.cambridge.org/core/journals/mathematical-gazette/article/3121-a-geometric-proof-of-a-famous-identity/E97A38F5789CD7278F642D58107C9860)
potvrzuje titul, autora, Mathematical Gazette 49(368), květen 1965,
strany 198–200 a DOI 10.2307/3612319. Dostupná prezentace neposkytla
přečtený text strany 200. Atribuce obrazce Warrenovi Lushbaughovi je
tedy převzata z Knuthovy oficiální opravy, nikoli nezávisle ověřena
z Golombovy poslední stránky. Tuto bibliografickou kontrolu přeskakujeme.

U úlohy 14 zachováno přesné rozlišení konferenčních textů a jiných
Floydových/Kingových prací z X0708/X0902. Nedostupné původní IFIP texty
jsou nyní výslovně přeskočené doporučené prameny. Technická úloha je
proto podle nového zadání uzavřena; původní záznamy nedostupnosti se
nemění na přečtené prameny. Totéž platí pro bibliografii úlohy 8.

Přeskočeny jsou také přímé kontroly Hardyho kapitol 6/8, Henkinova článku,
Pólyovy kapitoly, Gardnerovy a Conwayovy–Guyovy doporučené četby.
Samostatně **fakticky částečné** zůstávají historické odstavce na 17–18:
prvenství a přesné vztahy mezi staršími autory, datování Goldstineových
a von Neumannových diagramů a přesné znění a vydání Turingova epigrafu.
Rychlé vyhledání Turingova manuálu ukázalo i odlišné katalogové datace;
bez porovnání vydání nejde o potvrzenou chybu. Nepokračujeme v dlouhém
shánění těchto dokumentů. Červená na 17 zachycuje doloženou autorovu
opravu Maurolicova prvenství z 17. listopadu 2023, nikoli vyřešení
všech ostatních historických vět na stránce.

## Errata a stav

Znovu prohledány všechny čtyři historické vrstvy pro 11–20 a 468–469,
včetně dodatků p(0), záporných n, nového falešného důkazu úlohy 2 a
jeho nové odpovědi. Přímo zobrazeny `all1-prepre` strany 4–5 a 30–31 a `all1`
strana 3; další změny jsou v dříve přijatém protokolu a původní poznámce.
Originály byly právě 5. listopadu obnoveny a jejich hashe se nezměnily.

V1-X0932 uzavírá souvislou matematickou recenzi a původně částečné
úlohy 8 a 14 s explicitními bibliografickými výjimkami. X0933 doplňuje
do mapy známé opravy, které dosud neměly vlastní stránkový záznam.
Žádná nová dosud neopravená chyba tímto blokem nevznikla. Celý oddíl
nadále není fakticky uzavřen kvůli historickým odstavcům. Počet uzavřených
původních úloh svazku se mění z 842 na 844 z 932.
