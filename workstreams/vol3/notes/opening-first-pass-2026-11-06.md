# Úvod svazku 3 — rychlý první průchod

6. listopadu 2026. Rozsah: souborové strany 1–21 (titul, iv–vii,
ix–xiii, tištěné 1–10) a odpovědi §5 na tištěných 584–591.
Jde o souvislé čtení a krátké matematické kontroly, nikoli certifikaci
všech vět nebo nezávislý druhý audit. Bibliografické údaje níže přeskočeny.

## Vydání a stránkování

Původní sazba souborových stran 2–3 potvrzuje druhé vydání, první dotisk,
březen 1998, ISBN 0-201-89685-0. Soubor má 791 stran. Číslovaná strana 1
je souborová 12; 584 je 595 a 780 je 791. Pro arabské stránky platí +11.
Před nimi je mapa 1–2 nečíslovaný titul, 3=iv, 4=v, 5=vi, 6=vii,
7=ix, 8=x, 9=xi, 10=xii, 11=xiii; prázdné viii a xiv v souboru nejsou.
Strana x je ve skenu dole useknutá, takže zůstává partial. Poslední stranu
780 jsem použil jen k ověření offsetu, nikoli jako zkontrolovaný rejstřík.

## Závěry obsahu

- Definice lineárního uspořádání, stability a sentinelů na s. 4 dávají smysl.
  Stabilní výsledek je jednoznačný: je to řazení podle dvojice (klíč, původní
  index). Důkazy §5-1 až 3 na s. 584 prošly krátkou kontrolou. V netranzitivním
  turnaji zachová vkládání dalších vrcholů tři různá pořadí počátečního cyklu.
- Rekurzivní kód §5-5 je prefixový a zachovává pořadí: nejprve kóduje délku
  zbývajících bitů, pak tyto bity. Rekurence L(n)=1+L(floor(lg n))+floor(lg n)
  dává požadované lg n+O(log log n). Výpisy kódu přečteny, bez plošného testu.
- MIX §5-6 až 8: kontrola principu CMP proti odečítání, lexikografického
  sestupu a rozdělení na poloviny bez přetečení. Neprováděl jsem emulaci
  každé instrukce. Druhé řešení minima používá správnou tabulku pro porovnání
  podepsaných zbytků -1,0,1, od nejnižších bitů k nejvyšším.
- §5-9: distribuční funkce je součet binomických pravděpodobností pro alespoň
  r úspěchů; derivace beta integrálu i koeficienty střídavého součtu souhlasí.
- §5-10 až 17: třídění a slévání, transpozice, náhodná inverzní tabulka,
  převod pořadí znaků a pomocné katalogové klíče přečteny. U transpozice
  potřebuje úvodní rozdělení vlastní průchod: známá oprava +1 je zohledněna.
- §5-18: přesná identita 27^5+84^5+110^5+133^5=144^5 dává 61917364224.
  Rozdělení šesti proměnných na dvě trojice a následný test po shodě zbytků
  je korektní filtr. Brute force hledání řešení se nespouštělo.
- §5-19 až 22: dva ukazatele pro doplňující páry; průnik koulí poloměru 1
  pro Hammingovu vzdálenost nejvýše 2; dělení do tří desetibitových bloků;
  třídění anagramů a izomorfní invarianty. Výrazy 499500 a 31000 souhlasí.
  Existenci a úplnost historických slovníkových seznamů jsem neověřoval.
- §5-23: algoritmus generování klik je logicky správný, ale zdůvodnění malého
  výstupu zákazem 25-kliky selhává; samostatný kandidát V3-C0001.
- §5-24: zdvojování vzdálenosti v seznamu a slučování sedí. OCR ztrácí čárky
  nad x, ale původní s. 591 je má správně. Není to nález. Přesný optimalizovaný
  počet průchodů pro tři miliony lidí nebyl znovu modelován.
- §5-25: základ baby-step/giant-step je správný. V doplňku k výpočtu
  diskrétního logaritmu je chybný modul; V3-C0002 obsahuje krátký důkaz.

## Zohledněná známá errata (nejsou nálezy)

Vrstvy all3-prepre, all3-pre, all3, err3 a související err3-1e byly
prohledány podle stran i věcných pojmů, viz sources/opening-errata-review.json.
Mezi relevantními opravami jsou: Machiavelli 1951→1513; §5-9 n→N;
§5-12 méně než dvanáct průchodů a v odpovědi ceil(lg n)+1; §5-2 v odpovědi
R_p(n)→R_p(1); úpravy knihovních titulů a klíčů; operátor & místo klínu
v §5-20; doplněná odpověď Notes-2 z roku 2023. Pozdější rozšíření obsahu
o Appendix C není chybou stránkování prvního dotisku.

## Výslovně přeskočené prameny

Epigrafy Burton/Livius, Swift, Mahon, Machiavelli, Gardner/Perry Mason,
Edmund Scientific a Carroll; Bellmanova anekdota; historie LARC a statistika
času věnovaného třídění; ALA 1942 a přesné životopisné/katalogové údaje;
Euler 1778/1795, Lander–Parkin–Selfridge 1967, Elkies 1988; Levenshtein 1968;
slovníkové priority a významy slov u anagramů; Hopcroft–Tarjan 1972,
Hardyho datace, Silver/Pohlig–Hellman/Pollard bibliografické údaje.
Fermatova věta rozpoznána jako standardní správné tvrzení; Wilesův důkaz
ani odkazované monografie se v tomto prvním průchodu znovu neprokazovaly.

Další kurzor: tištěná 11 / souborová 22, §5.1.1 Inversions.
