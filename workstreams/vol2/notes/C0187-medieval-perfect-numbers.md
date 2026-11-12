# V2-C0187 — možné posunutí dvojice prvočísel na 412

**Stav:** candidate, nikoli confirmed. [Původní strana412](../images/vol2-p412.png)
byla vizuálně přečtena. Knuth připisuje anonymnímu italskému autorovi
znalost prvočísel 2^17−1 a2^19−1 do roku1460 a cituje Picutti1989.

Picuttiho anglický abstrakt, reprodukovaný v bibliografických panelech
ResearchGate, přisuzuje rukopisu *Ottobonianus Latinus3307* z1460
páté a šesté dokonalé číslo. **Dokonalé číslo** je kladné celé číslo
rovné součtu svých kladných vlastních dělitelů. Tradiční seznam
prvních sedmi známých dokonalých čísel odpovídá exponentům
2,3,5,7,13,17,19 v Euclidově výrazu 2^(p−1)(2^p−1). Proto jde
v abstraktu o p13 a17, zatímco Knuth píše17 a19.

| Pořadí v historickém seznamu | p | Dokonalé číslo |
|---|---:|---:|
| páté |13|33550336|
| šesté |17|8589869056|
| sedmé |19|137438691328|

Převod mezi exponenty a čísly je elementární; prvotní certifikace
příslušných Mersennových prvočísel už je v `primality-lucas.md`.
Nové aritmetické testy nejsou potřeba. Podezření se týká historické
atribuce, nikoli prvočíselnosti těchto čísel.

[Záznam čtení abstraktu](../sources/picutti-1989-abstract-reading.txt)
uvádí oba hostitele a omezení. Oficiální ElsevierAPI potvrzuje
bibliografii DOI10.1016/0315-0860(89)90034-7, ale nevrátilo vlastní
článek. Sken stran123–136 nebyl získán. Z abstraktu samotného
nelze vyloučit další zmínku o exponentu19 v plném článku.
Knuth navíc známým erratem8.1.2005 přesunul citaci a doplnil
Williams1998, Chapter2; tuto kapitolu jsme zatím nečetli.

Všechny vrstvy errat all2-prepre/all2-pre/all2/err2 i TeXerr2 byly
prohledány podle412,1460,Picutti a souvisejících jmen. Jediná
související změna2005 nemění exponenty. K potvrzení je třeba
přečíst Picuttiho rozhodnou pasáž a pozdější Williamsovu citaci,
případně přímo příslušné listy rukopisu. Do té doby se položka
nepočítá mezi potvrzené chyby a návrh hlášení se neodesílá.
