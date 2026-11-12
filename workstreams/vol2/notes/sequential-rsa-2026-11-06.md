# §4.5.4 — souvislé argumenty: RSA, Rabin a mřížový útok

6. listopadu 2026, V2-X0147. Hlavní text od Secret factors na 403
po první odstavec 407; původní zadání 415 a 417, odpovědi 664–665
a část 669–670 patřící úloze 44. Strana 671 byla přečtena pro
ověření konce odpovědí oddílu; původní odpověď 47 tam není.
Vizuálně porovnána také náhrada 47 v all2-pre, str. 11.
Párovány úlohy 32–35, 44 a 47: čtyři uzavřené, dvě partial.
Mapa jednotlivých tvrzení je v results/sequential-rsa-evidence.json.

Žádný nový nález ani výpočet. Převzaté důkazy nejsou znovu
přepisovány a staré certifikace nejsou spouštěny. Tato kontrola
neaktualizuje historický text na současné doporučení kryptografie.

## Přesné matematické pokrytí

`rsa-basic.md`, §1–4, samostatně dokládá:
- inverzi x^e včetně nejednotek pomocí CRT;
- malé krychle, útok třemi moduly a přesný počet násobení pro 65537;
- opravu doplnění v celé úloze 32 včetně rozsahu a dekodéru;
- počty kořenů x^m=1, obě větve úlohy 34 a úspěch nejméně 1/2
  při rozdílných dvojkových řádech;
- všechny čtyři Rabinovy kořeny pro jednotky a odpovídající
  redukci na faktorizaci;
- Williamsovo kódování, nulový Jacobiho symbol po známé opravě,
  jednoznačnost dekodéru a útok i při příslibu platných šifer.

C0166 je neplatná pravděpodobnostní mez na 405: součin dvou
malých mezí lze použít, chybějí-li oba příslušné dělitele m,
ne pouze jejich součin. Závažnost medium, bez tvrzení, že tím
byla prolomena obecná RSA konstrukce. C0167 je konkrétní nechráněná
hraniční zpráva x=floor(cuberoot(N)) v odpovědi 32; závažnost low.
Známá změna horní meze y tento jiný krajní případ neopravuje.
Opravený náhodný postup má vlastní úplný argument, nepředstavuje
však důkaz obecné bezpečnosti doplňování.

Při čtení 406 je výslovně zachováno: čtyři různé odmocniny jsou
jen pro jednotku, dvě pro nenulový násobek jednoho faktoru a jedna
pro nulu. Tento zřejmý okraj je zaznamenán jako kvalifikace,
bez nové karty. Předběžný gcd vyřeší nejednotky v redukci.
Kompozice funkcí různých uživatelů předpokládá vhodnou reprezentaci
zpráv v blocích příslušného modulu; samostatný zbytek nemusí
automaticky ležet v rozsahu druhého modulu.

`rsa-advanced.md`, §1–2, dává celý argument úlohy 44 pro obecné
společně nesoudělné koeficienty, nikoli pouze monický polynom.
Odděleně jsou doloženy determinant, odstranění jmenovatele d,
krátkost, nenulovost výsledného polynomu i nalezení všech jeho
celočíselných kořenů v polynomiálním čase. Pro d=4 má mříž dimenzi
11 a přesná prahová konstanta je menší než 10^27.
Algoritmická věta LLL je explicitní vstup daný nápovědou,
Sturmova věta je explicitní standardní algebraický vstup.
Vlastní aplikace obou má doložený argument. Sedm časových značek
na 405 vede právě na tuto konstrukci: mocnina dvou je invertibilní
modulo každý lichý RSA modul.

C0168 opravuje pouze rok konferenčního svazku v odpovědi 44
na 670; jde o low, nikoli chybu mřížového argumentu.

## Výzkumné úlohy a bezpečnostní hranice

Úloha 33 je nově v coverage.json partial. Důkaz obecné účinné
redukce faktorizace na inverzi RSA zde nemáme. Již přečtený
primární článek z roku 2024 řeší omezený generický model;
tento výsledek nepovyšujeme na řešení zadání ani na úplný přehled
současné literatury. Stav rešerše a vyřešení úlohy jsou odlišné.

U úlohy 47 jsou převzaty tři nezávisle certifikované prvočinitele,
přesný součin, obě modulární odmocniny, zpětné umocnění a ASCII
dekódování původní 211ciferné verze. Nová 318ciferná výzva
z errat 2012 má ověřený číselný přepis a složenost modulu,
ale její faktory ani zprávu nemáme. Celá aktualizovaná úloha
je proto partial. Známá náhrada není nález a nezobrazuje se
jako chybová karta. Nový faktorizovací běh se nespouští.

Tvrzení o neprolomitelnosti fyzické RSA krabičky, nepadělatelnosti
podpisů a bezpečnosti adresáře se nepovažují za dokázané matematické
výsledky. Fyzická ochrana je hypotéza modelu. Algebra podpisové
kompozice a popsané podvržení adresáře jsou srozumitelné, avšak
text nevymezuje úplný bezpečnostní model, kódování ani všechny útoky.
Obecná bezpečnost proto zůstává výslovně neověřena; nevytváří se
z ní nový potvrzený nález pouze na základě absence důkazu.

## Číselné odhady a historie

Poměr 8.5 na 405 je poměr 17 a 2 modulárních operací, ne univerzální
poměr naměřených časů. Logaritmický model vedoucího bloku dává přibližně
třetinu malých zpráv; jiné rozdělení zpráv může dát jiný podíl.
Přibližných 90 pokusů při konstrukci prvočísel je hustotní heuristika,
nikoli obecná mez prvočíselných mezer. Algebra podmínek na k dává
p=2 modulo 3. Padesát nezávislých Millerových–Rabinových pokusů má
mez chybného přijetí pevného složeného kandidáta 2^−100; není to
bez dalšího předpokladu Bayesova věta o libovolně vybraném zdroji.
Časový příklad s rokem 365.2425 dnů je převzat jako podmíněný
aritmetický přepočet, nikoli odhad dnešní bezpečnosti.

`rsa-history.md` uzavírá dobové X.509 v původním svazku 1989,
Cocksovu zprávu 1973 a oznámení odtajnění 1997. Správnost Cocksovy
transformace x^(pq) se odvozuje ze stejného CRT argumentu.
Rozlišujeme přepis zprávy, archivní kopii oficiálního oznámení
a původní fyzický dokument. Dosavadní čtyři vrstvy errat a jejich
použití se přebírají; nový rozpor nebyl zjištěn. Původní šifra
a nová náhrada zůstávají oddělené i v evidenci.

Další kurzor: The largest known primes, tištěná 407 / file419.
BBS úloha 43 a dopředný odkaz ze strany 36 čekají na samostatné
párování, stejně jako zbývající prvočíselné a výzkumné úlohy.
