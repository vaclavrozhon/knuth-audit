# Exchanging sort — sedmý čtenářský checkpoint

Přečteny s. 106–138 (files 117–149), všech 56 úloh §5.2.2 a odpovědi
628–639 (files 639–650). Na 138 i úvod selection; odpovědi selection
na 639 byly přečteny, ale ještě nespárovány, proto celá 639 zůstává partial.
Jde o dosavadní první průchod, nikoli splnění nového požadavku na
samostatný argument ke každému tvrzení a každé úloze.

Krátce zkontrolovány invarianty bubble/cocktail, merge-exchange,
quicksortu a radix exchange; partition rekurence, binomická transformace,
základní Mellinovy reziduové kroky a třídění do tří částí. Nezávisle
nebyla odvozena každá instrukční frekvence, globální extrémy srovnávacích
sítí, veškerá asymptotická algebra ani všechny doplňky odpovědí.
Úloha 9 je otevřený výzkumný problém; její řešení netvrdíme.
Úloha 42 odkazuje na externí důkaz Karpovy nerovnosti, který zatím
nebyl samostatně reprodukován. Tyto mezery jsou v seznamu důkladné kontroly.

Nové konkrétní důkazy jsou C0011–C0015 v samostatných krátkých poznámkách.
Neběžel žádný numerický test ani enumerace. Sazba podezřelých míst
prohlédnuta; archivované vrstvy all3-prepre, all3-pre, all3, err3 a
err3-1e věcně spárovány v sources/exchanging-errata-review.json.

Známé opravy zohledněny samostatně: MIX značky/jumpy, B_N v (25),
radix frekvence X_N, odkazy úloh, Bernoulliho znaménka, sumace (36),
EX_jk, odstranění δ_k0, zbytek odpovědi48, přepis49, meze oscilací50,
ζ(−n), index rekurence53 a předpoklad M>1 pro55. Nejsou to naše nálezy.

Bibliografie přeskočena: historické priority a přesné citace k bubble,
cocktail a Batcherovým sítím; Hoare, Sedgewick, Singleton, van Emden,
Hurwitz, Shackleton, Dromey, Raman, Dijkstra/Feijen, Karp,
McDiarmid–Hayward, de Bruijn, Rice, Nørlund a historické benchmarky.
Číselné tabulky a optimalizační příklady byly čteny a krátce posouzeny,
nikoli znovu globálně enumerovány.

Čtenářský kurzor: 139 / file 150. Nový důkladný kurzor: 1 / file 12;
celý dosavadní první průchod je rozepsán v proof-audit.json a
notes/deep-review-backlog-2026-11-06.md. Existující konkrétní důkazy
se přebírají bez opakování.
