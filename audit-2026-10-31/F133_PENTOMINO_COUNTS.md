# F133: dva příliš malé počty v odpovědi DLX134

V našem 4B, 1. vydání / 2. dotisk, str. 450, odpověď 7.2.2.1–134,
jsou dva počty výskytů pentomin nesprávné:

| Pentomino | Kniha | Ověřený počet komponent |
|---|---:|---:|
| P | 1 672 | **1 685** |
| Y | 242 | **243** |

Ostatních deset čísel souhlasí. Počítáme jednotlivé monochromatické
komponenty složené z pěti čtverců, ve všech 13 328 třídách řešení
předchozí úlohy. Dva výskyty v jednom řešení se počítají dvakrát,
jak výslovně připouští odpověď. Rotace, odrazy a společná záměna
obou nebílých barev jsou již odstraněné.

## Krátká reprodukce bez řešiče

Z kořene projektu:

```sh
python3 audit-2026-10-31/verify_f133.py
```

Program používá jen standardní knihovnu Pythonu a komprimovaný
[certifikát](results/squares133/f133-witnesses.json.gz). Neimportuje
naše generátory, řešiče ani původní klasifikátor pentomin. Ověří:

- všech 24 různých cyklických typů dílků v každém skládání;
- shodu sousedních hran a bílý obvod;
- vzájemnou neekvivalenci všech **1 734** přiložených skládání;
- jejich monochromatické komponenty a přesné tvary P a Y.

Už tato podmnožina obsahuje **1 685 výskytů P a 243 výskytů Y**.
Je tedy samostatným důkazem, že knižní počty jsou příliš malé;
k vyvrácení není třeba důvěřovat úplnosti našeho hledání.
[Výsledek kontroly](results/squares133/f133-lower-bound-checked.json).

## Úplný výčet a jiné konvence počítání

Nativní Algorithm C dal 13 328 reprezentantů. Nezávislé hledání
konfliktními bitovými množinami dalo všech 106 624 označených řešení.
Celá množina je přesně rozšířením nativních reprezentantů o osm symetrií;
neporovnávaly se jen čítače. Všechny modely byly geometricky validované.

Cenzus komponent se shoduje ve dvou postupech: průchod po otočené
čtvercové mříži a spojování jednotlivých trojúhelníkových výsečí.
Další samostatná kontrola dolní meze pracuje přímo se sdílenými hranami.

| Co se počítá | P | Y |
|---|---:|---:|
| Všechny výskyty komponent | 1 685 | 243 |
| Řešení s alespoň jedním výskytem | 1 611 | 237 |
| Dvojice řešení–barva s alespoň jedním výskytem | 1 631 | 243 |
| Čísla v knize | 1 672 | 242 |

Rozdíl tedy nevysvětluje ani jedna z těchto přirozených alternativních
konvencí. P se vyskytuje dvakrát v 74 řešeních, Y v šesti. Jediné
řešení se čtyřmi pentominy má P, P, W, Y, jak ukazuje
[ověřený obrázek](images/squares134-four-pentominoes.png).
Tvrzení o jedinečnosti tohoto řešení souhlasí.

## Kontrola zdrojů a omezení

Původní strana 450 byla zobrazena. Stejná dvě čísla jsou i v autorově
Pre-Fascicle 5C z 11. září 2019, tištěná str. 154 / PDF str. 160;
[originální strana](images/fasc5c-squares133-134.png) byla zobrazena.
Nejde tedy jen o chybu OCR.

Prohledáno šest aktuálních i historických vrstev errat 4B a Fascicle 5,
včetně posunů stran, čísel úloh, jmen a počtů. Jejich hashe souhlasí
s ověřením oficiálních souborů z 2. listopadu 2026 v 08:06 UTC.
[Kontexty](results/squares133/errata-contexts.json) obsahují pouze opravy
jiné úlohy MPR133 a známou opravu obvodu v DLX133; oprava těchto počtů
v DLX134 nalezena nebyla.

Nález je potvrzený v našich zdrojích a certifikátu. Prvenství ani
stav všech novějších tištěných exemplářů tím netvrdíme. Původní návod
Multimatch I z roku 1991, citovaný pro historickou atribuci úlohy,
zatím nemáme. Nevznikl žádný emailový návrh a nic nebylo odesláno.
