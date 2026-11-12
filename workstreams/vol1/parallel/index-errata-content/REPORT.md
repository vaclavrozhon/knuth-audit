# Obsahová kontrola indexových změn ve čtyřech vrstvách errat

Všech 435 výskytů přidaného či nahrazeného hesla má samostatný ruční
záznam v `results/index-errata-reference-review.json`. Všech osm
indexových stran errat bylo přímo obrazově přečteno. Záznamy zahrnují
388 výskytů v dlouhých historických seznamech a 47 obrazově porovnaných
duplikátů v krátkém `err1`. Jednotlivé cíle jsou odděleny od původního
rejstříku; žádný sdílený inventář ani zmrazená starší dávka se nemění.

| Vrstva a strany PDF | Výskyty | checked | partial | candidate |
|---|---:|---:|---:|---:|
| all1-prepre, 48–50 | 232 | 230 | 2 | 0 |
| all1-pre, 19–20 | 109 | 104 | 4 | 1 |
| all1, 16 | 47 | 46 | 0 | 1 |
| err1, 14–15 | 47 | 46 | 0 | 1 |
| Celkem včetně krátkých duplikátů | 435 | 426 | 6 | 3 |
| Bez krátkých duplikátů | 388 | 380 | 6 | 2 |

`checked` zde znamená smysluplný obsahový cíl, případně skutečný cíl
odkazu `see`. Není to nové ověření všech matematických důkazů, osobních
jmen, historických priorit nebo původních článků. Při čtení cílů se
použily konkrétní pasáže knižního textu, textové změny errat a dříve
ověřené záznamy původního rejstříku. Přímá nová obrazová četba cílů
je přesně vymezena v `notes/read-scope.md`; netvrdíme ji pro všechny
odkazované strany.

## Dva místní kandidáti

- `levy-363-wrong-volume`, `idxerr-pre-19-054`: nové heslo Lévyho
  uvádí 363, kde svazek 1 probírá grafy a stromy. Původní správný
  cíl 105 výslovně uvádí jeho continuity theorem. Totožný nový řádek
  patří k obsahu 363 ve svazku 2. Navržená místní oprava je 363 → 105,
  při zachování rozvedeného jména. Doklad: `notes/levy-363.md`.
- `chebyshev-377-388-wrong-volume`, `idxerr-all-16-004` a jeho krátký
  duplikát `idxerr-short-14-004`: 377 a 388 nemají ve svazku 1
  odpovídající obsah, ale stejný nový řádek i oba konkrétní cíle
  se nacházejí ve svazku 4B. Správné doložené cíle nerovností ve
  svazku 1 jsou 98, 104 a nově 472. Varianty jména nejsou předmětem
  kandidáta. Doklad: `notes/chebyshev-377-388.md`.

Oba kandidáti se týkají veřejných errat. Pozdější úplný rejstřík
svazku 1 chybí, takže netvrdíme přenos těchto čísel do fyzického
pozdějšího tisku. Shoda s jiným svazkem dokládá konkrétní stopu,
nikoli redakční mechanismus vzniku. Globální ID nejsou přidělena;
anglické ASCII návrhy v `reports/` nebyly odeslány.

## Šest přesných neuzavřených položek

| ID | Heslo | Meze |
|---|---|---|
| idxerr-prepre-48-028 | Case Institute of Technology | Původní i chybí. Dedikace novějšího náhledu byla textově přečtena. |
| idxerr-prepre-48-036 | Christie Mallowan | Původní xvii chybí. Novější Poirotův epigraf byl textově přečten. |
| idxerr-pre-19-033 | Geek art | Původní xx chybí. Binomický strom na xx novějšího náhledu byl přímo zobrazen. |
| idxerr-pre-19-045 | Internet | iv a nový text na 112 mají obsah; původní xvi chybí. Novější xvi byla textově přečtena. |
| idxerr-pre-19-048 | Nancy Jill Knuth | Původní x je doložena, původní xx chybí. Podpis autora kresby v novějším obrazu nebyl nezávisle identifikován. |
| idxerr-pre-20-029 | Jonathan Swift | Nová fyzická 630 chybí. Přesun původního úvodu rejstříku z 628 je zatím jen strukturální inference. Starý C0076 se neduplikuje. |

Prvních pět položek patří k již vedené mezeře X0024. Stav `partial`
neoznačuje chybu knihy. Naopak Fuller a Gordon na xi i Turing machines
na 9 jsou potvrzeni přímo v dostupné současné sazbě. U Chakravartiho,
Halāyudhy, Piṅgaly, Virahāṅky, Stavera a Mallata je dodaný obsah
výslovný, zatímco pozdější fyzický přelom či stránka nebyly čteny;
tuto odlišnou mez zachovává `physical_later_page_unseen`.

## Historické vrstvy a reprodukovatelnost

`results/chronology.json` seskupuje 388 neduplikovaných výskytů do
360 obsahových řad; 27 má více uvedených verzí. Nejde o rekonstrukci
úplného dnešního rejstříku. Úvod errat říká, že vypuštění starých hesel
obvykle neuvádí; změnu názvu nebo novou hlavní položku proto nečteme
jako automatické zrušení všech podhesel. Přesné významnější přechody
a známé opravy jsou v `notes/chronology.md`.

Samostatná institucionální definice OEIS je podložena vymezeným
čtením primárního webu provozovatele; podrobnosti a datum obsahuje
`notes/oeis.md`. Právní registrace značek ani celá historie databáze
se tím neověřují. Další historická hesla s knižními cíli zůstávají
kontrolou navigace, nikoli novými primárními biografickými audity.

Mechanická kontrola ověřila počty, jedinečnost ID, všech 47 vazeb
krátkého seznamu, existenci odkazovaných oprav, cílů `see`, obrazů
a poznámek. Neproběhly žádné nové matematické ani MIX testy.
`INPUTS.json` zachycuje přesné vnější závislosti a jejich SHA-256;
`MANIFEST.json` zmrazuje vlastní soubory. Čtení souboru jako vstupu
neznamená jeho celý obsahově auditovaný rozsah.
