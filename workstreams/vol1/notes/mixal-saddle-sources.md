# Rozsah pramenů a errat: §1.3.2-10–12

Dne1.11.2026 byly zobrazeny originální s.159,513–515 knihy
(tisk ed3,print1,1997; souborové strany174,528–530), all1-prepre37
a all1-pre16. Všechny čtyři textové vrstvy errat a aktuální zdrojový
TeX byly prohledány podle stránek i obsahu. Konkrétní opravy: věta
R(i)1999; přesun ENT1 a540→530 v1999; doplnění m>=n2002; duplicita
čitatele1997; nová odpověď12 z24.4.1997; dvě opravy první/druhé fáze2013.
Změna ratingu12 M47→HM42 již zaznamenána v předchozím inventáři.
C0023 aC0024 nejsou opravou žádné nalezené pozdější položky.

## Hofri–Jacquet

Čtrnáctistránkový preprint získán přes veřejnéAPI Rice; URL, čas,
SHA-256 a popis skutečného čtení v
`sources/hofri-jacquet-saddle-rice-api.metadata.json`. Celý extrahovaný
text1–14 přečten; matematicky relevantní PDF stránky5–11 skutečně
zobrazeny. Dodatek13–14 nebyl ověřen z obrazu a jeho depoissonizace
není použita. Publikovaná verze: Algorithmica22(1998),516–528,
DOI10.1007/PL00009237. Nepředstíráme totožnost preprintu se sazbou
časopisu. Citace ověřena též v primárním článku Dallant et al.2024.

Pramen poskytuje rozdělení délek řádkových zkoušek a třetí variantu
pro různé hodnoty. Konkrétní MIX koeficienty však neuvádí. Vlastní
odvození je v `mixal-saddle.md`, nikoli jen opakování závěru článku.
Pozor na několik míst preprintu:

- Modifikace „zkoušej všechny řádky“ dovolí nepodmíněné marginální
  pravděpodobnosti; nedokazuje vzájemnou nezávislost D_i, kterou
  text na s.5 naznačuje. Události sedla v různých řádcích se vylučují.
  Náš důkaz používá jen linearitu střední hodnoty.
- (7) používá i nekonečný ocas pomyslného sloupce; skutečný stroj
  má jen m porovnání. Náš D používá přesně oříznutý součet.
- Suma pro skutečný počet čtení končí q_(n-1), nikoli q_n
  (s.8 a10). Rozdíl je vzácný případ průchodu celým řádkem;
  pro přesné konečné hodnoty jej nelze ignorovat.
- Přesnější rozvoje (19)–(21) ani dodatek nepřebíráme bez důkazu.
  Druhou odpověď v knize dokazuje přímý momentový odhad μ; potřebný
  zbytek je slabší a má doloženou uniformitu za log(n)/m→0.

Tyto poznámky jsou vymezením použitelnosti pramene, nejsou samostatná
nová hlášení chyb knihy.

## Odkaz na Bienstock et al.1991 a obecná složitost

Původní dvoustránkový článek se přes JSTOR nepodařilo otevřít.
Bibliografické údaje potvrzují obsah vydavatele pro AMM98(5) a
bibliografie nového primárního článku:

- https://www.tandfonline.com/toc/uamm20/98/5
- https://doi.org/10.2307/2323858
- https://www.wild-inter.net/publications/dallant-haagensen-jacob-kozma-wild-2024.pdf

Poslední zdroj je uložen jako `sources/dallant2024-saddle.pdf`;
přečteny definice, důkazy lemmat2,3,5,7 a věty8 na s.4–7,
a bibliografické položky1,6 na s.13, včetně zobrazení těchto stran.
Moderní rychlejší algoritmus ze zbytku článku se zde nekontroloval.

**Rekonstrukce tvrzení knihy.** Nový článek používá opačnou konvenci
sedla; pro naši konvenci stačí negovat hodnoty při dotazu. U čtverce
udržujeme nejvýše jeden označený prvek v každém řádku a sloupci,
původně diagonálu. InvariantyP2/P3 o vyřazených řádcích/sloupcích
zaručují, že poslední označená hodnota leží mezi maximinem a minimaxem.
Pro minimum a maximum označené množiny jediný dotaz v jejich křížové
pozici dovolí odstranit jeden krajní prvek nebo oba nahradit křížovým;
tři případy v lemmatu7 zachovávají invarianty. Každý krok zmenšuje
množinu, takže stačí2n-1 dotazů a O(n log n) operací s vyváženým
stromem. Kandidátní hodnotu ověří dvě monotónní cesty a jeden řádek
se sloupcem v O(m+n) dotazech (lemma3). Pro m>=n rozdělíme matici
na ceil(m/n) čtverců; jejich vhodný extrém zachovává interval kandidáta
(lemma5). Celkem O(m+n) dotazů a O(m log n) pomocných operací,
pro n>=2; jednosloupcový případ se vyřeší přímo za O(m).

Tak je matematický obsah odkazu doložen, přestože původní článek1991
není přečten. Podmínka m>=n je známá oprava2002. Toto není důkaz
historického prvenství ani audit všech výsledků článku2024.

## Stav

Úlohy10–12 jsou uzavřeny. Konkrétní třetí obecná varianta uchovává
všechny řádky s maximem v jednom minmaxovém sloupci; další podmínky
ověřuje postupně. Má obecný důkaz a přesné průměry pro obě rozdělení;
pro9×8 je v obou rychlejší než druhý tištěný program. Nejde o tvrzení
globální optimality ani o předstírání, že kniha dává instrukce třetího
řešení. Důkazy jsou v oddílu8 `mixal-saddle.md`.
Kontroly9381+3118+6126 prošly, neopakovat bez věcného důvodu.
Pokračují úlohy13–23; cíl celého svazku zůstává aktivní.
