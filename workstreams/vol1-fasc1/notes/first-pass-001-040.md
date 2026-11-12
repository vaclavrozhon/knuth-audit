# První průchod MMIX — file 1–40

Souvisle přečteny file 1–40, tedy obálka, přední listy a tištěné p.1–32. Rozsah zahrnuje celý popis instrukcí §1.3.1′, **zadání** úloh 1–58 a začátek §1.3.2′ po algoritmus P. Řešení úloh na p. 94 a dále zatím souvisle přečtena nejsou; nelze z tohoto bloku vykázat procento vyřešených či ověřených úloh.

Vydání: první vydání 2005, třetí digitální vydání květen 2023, 145 souborových stran. Inventory záznam vol1-fasc1 se shoduje s prohlédnutou tiráží. Hlavní p.1–134 odpovídají file 9–142 (offset +8); iii–v jsou file 5–7. Titul/copyright file 3–4 nemají vytištěné číslo; číslování i/ii je pouze konvenční. File8 je blank, nikoli obsah. Obsah je skutečně hlavní tištěná p.1/file 9.

Čtení probíhalo přes nativní text PDF, s původní sazbou u podezření, vzorců a tabulek, které se v extrakci rozpadly. Souborové obrázky nejsou samy důkazem celostránkového pokrytí. `reviewed` znamená první přečtení celé stránky, nikoli úplnou formální kontrolu všeho.

Cílené kontroly: konverze bit/hex a meze dvoukomplementových hodnot; příklady zarovnání, sign extension a store; bitové a maticové příklady; formáty instrukcí a rozsahy relativních skoků; drobná kontrola návaznosti dvou tabulek instrukcí/registrů. V tabulkách nebyla nezávisle porovnána každá z 256 instrukcí s implementací. Výklad floating point přečten; všechny mezní stavy IEEE a epsilon operací se nyní nereprodukovaly.

Program M p.28–30 byl přečten a jeho profil součtem uvedených nákladů dává nμ+(5n+4A+5)υ. Ručně přečteny větve i kódování skoku #55 02 ff fa (známá oprava z roku 2005 už zapracována). Program H p.30–32: řetězec má devět bytů včetně newline/nuly, rozložení argv odpovídá příkladu. Algoritmus P na p.32 přečten; test q≤p po odmítnutí dělitelnosti je v souladu s testováním rostoucích prvočísel. Kompletní reprodukce tabulky 500 prvočísel ani běhy M/H/P nebyly provedeny.

Nové položky: MMIX-C0001 (nízká textová matematická chyba, první bity vs zaokrouhlení), MMIX-C0002 (nízký překlep), MMIX-C0003 (otevřený kandidát rY/NEG). U každého je samostatná krátká poznámka.

Zohledněná veřejná errata: MixMaster→Mixmaster na p.iv (2024-06-20), squadron→Squadron v Hellerově citátu p.3 (2024-04-27) v digitálním vydání 2023 přetrvávají; jsou **known_erratum**, nikoli naše nálezy. Ostatní relevantní starší opravy byly při čtení zohledněny; přesné dostupné položky jsou v `results/errata-first-32.json`.

Bibliografie ověřena pouze na úrovni přečteného údaje, nikoli v originálních pramenech: Gove 1961; Dickens/Murray v předmluvě; Neil Simon 1996; MMIXmasters 2012 a Ruckert 2015; MMIXware/LNCS1750 (1999); uvedené články CACM 1965/1968/1969; Heller 1961 (mimo známou opravu); Iverson 1962 pp.23–24; Kernighan/Van Wyk 1998; Wordsworth 1804; Randolph/Wilson 1953. Přesná rozdělená anglická evidence je u příslušných stránek v `ui-page-coverage.json`. Dobová tvrzení o komerčních CPU na p.23 byla přečtena v kontextu konce tisíciletí, nikoli přezkoušena průzkumem současného hardware.

Cíleně mimo souvislý blok: file 91/p. 83, file 96/p. 88 a file 130/p. 122 pouze řádky pro rY/NEG; evidence `partial`. Další souvislý kurzor: **file41 / tištěná p.33**, pokračování Programu P.
