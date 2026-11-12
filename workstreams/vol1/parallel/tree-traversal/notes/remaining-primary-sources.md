# Zbývající pramenné meze §2.3 a §2.3.1

Stav k 1. listopadu 2026. Matematické a algoritmické výsledky jsou vedeny samostatně v `progress.json`; tato fronta nesnižuje již provedené vlastní důkazy, ale brání označení celého historického obsahu za ověřený.

| Místo knihy | Přesný primární podklad | Co chybí |
| --- | --- | --- |
| 310, Fig. 18(a); odpověď §2.3-15 na 562 | *Burke's Peerage* (1959); *Almanach de Gotha* (1871); *Genealogisches Handbuch des Adels: Fürstliche Häuser*, sv. 1 | Původní rodové záznamy všech hran šestigeneračního rodokmenu Charlese. Binární adresy Christian IX jsou z obrázku ověřeny; jejich genealogická pravdivost nebyla nezávisle ověřena. |
| 311 | Knuthův vlastní průzkum obrázků a rozhovorů, více než 80 procent kořenů nahoře po dvou letech vlastní opačné konvence | Kniha neposkytuje data ani přesnou publikovanou referenci; jde o autorovo svědectví. Numerický podíl nelze nezávisle přepočítat z dostupného textu. |
| 322 | A. J. Perlis, C. Thornton, *Symbol Manipulation by Threaded Lists*, CACM 3 (1960), 195–204, DOI 10.1145/367177.367202 | Nezískán celý původní článek; vyhledání ukázalo katalogy a první odstavec připojený k McCarthyho článku, nikoli celý doklad threaded reprezentace. Tento bod se může přirozeně překrýt s budoucí §2.3.4.6. |
| 329 | A. J. Blikle, *Investigations in the Theory of Addressless Computers*, Bull. Acad. Polonaise Sci., Série Sci. Math. Astr. Phys. 14 (1966), 203–208 | Nezískáno původní oznámení, zejména klasifikace přesně šesti addressless pořadí. Název dohledán v původní bibliografii pozdějšího článku ACM (DOI 10.1145/800157.805038), nikoli jako náhrada důkazu. |
| 567, §2.3.1-21 | J. M. Morris, *Traversing Binary Trees Simply and Cheaply*, IPL 9 (1979), 197–200, DOI 10.1016/0020-0190(79)90068-1 | Přečtena pouze metadata vydavatele. Celý článek, původní postorder varianta a vztah k tištěné variantě U zatím nejsou porovnány. Vlastní důkaz U a W je hotový. |
| totéž | J. M. Robson, *An Improved Algorithm for Traversing Binary Trees Without Auxiliary Stack*, IPL 2 (1973), 12–14 | Původní článek nedostupný v provedeném hledání; neověřen popis uložení zásobníku plných uzlů do prázdných listů. Tato alternativa nebyla vydávána za implementovanou. |
| totéž | G. Lindstrom, *Scanning List Structures Without Stacks or Tag Bits*, IPL 2 (1973), 47–51, DOI 10.1016/0020-0190(73)90012-4 | Celý originál nedostupný, vydavatelský odkaz vrátil 403. Neověřena historická atribuce W a poznámky o každém třetím uzlu. Samotné W má vlastní obecný důkaz. |
| totéž | B. Dwyer, *Simple Algorithms for Traversing a Tree Without an Auxiliary Stack*, IPL 2, 143–145 | Celý originál nedostupný. Kniha udává 1973; metadata a pozdější citace kolísají mezi 1973 a 1974, proto rok zatím není novým nálezem. Nutno přečíst záhlaví původního čísla a článek. |

Osobní atribuce R. Bigelowovi (562) a S. Araujo, 1976 (565) nemají v knize připojenou dohledatelnou publikovanou referenci. Vlastní konstrukce a algoritmus byly auditovány, autorství ani priorita nejsou tímto ověřeny. Běžný název Dewey decimal notation je vysvětlen jako analogie knihovnického třídění na 313; text netvrdí, že Dewey vynalezl tuto konkrétní stromovou definici.

Cross-reference meze: místní tvrzení odkazující na jiné části knihy byla ověřována v rámci tohoto bloku jen tam, kde byla jejich přesná premisa potřebná (zejména sémantika CMPi na 134). Odkazy na §2.3.2, §2.3.4 a §7.2.1 ani zamýšlenou Chapter 10 nejsou tvrzením o prověření celých těchto sekcí. §2.3.2 vlastní druhý agent, další části se auditují zvlášť.

Získané výškové články 1982 a 1993 mají v `sources.md` přesně uvedené přečtené stránky. Zbylé důkazy těchto článků nejsou potřebné pro prosté potvrzení bibliografického odkazu, ale nebyly prohlášeny za nezávisle auditované. Galton, Brent–Kung, de Bruijn–Knuth–Rice, Swainson a text Genesis v uvedených lokálních rozsazích jsou již uzavřeny.
