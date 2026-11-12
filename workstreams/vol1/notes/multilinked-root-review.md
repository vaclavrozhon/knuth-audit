# Kořenová revize §2.4

1. listopadu 2026. Celý zmrazený REPORT, UNIT_STATUS, general-proofs,
sources a errata přečteny. Všech 56 záznamů zdrojového manifestu
souhlasí v délce i SHA256. Úplný kořenový manifest připojuje rovněž
programy, důkazy a výsledky; složka se dále nemění.

Algoritmus A udržuje zásobník právě aktivních předků s rostoucími
hladinami. B zkouší všechny stejnojmenné kandidáty přes PREV a hledá
kvalifikátory po rodičích v nejbližším možném výskytu. Volba bližšího
předka nemůže znemožnit pokračování, které by připouštěl vzdálenější.
Úplná kvalifikace, obecná kvalifikace a varianta PL/I jsou v důkazu
výslovně rozlišeny. C páruje stejné úplné relativní cesty od kořenů
s inkluzivní podmínkou, že alespoň jeden z obou konců je list.

Výklad CORRESPONDING v knize dovoluje listové kořeny; srovnaný
IBM COBOL 1964 požaduje skupiny. Úloha8 se odvolává výslovně na
knižní definici, takže tato odlišnost sama není novou chybou.
U všech patnácti úloh jsou obecné důkazy. Vlastní varianta úlohy15
ukládá do dosud nepoužitého SIB dočasně hladinu a používá PARENT
jako cestu zpět; před uzavřením uzlu SIB správně obnoví. Má lineární
čas a konstantní pomocnou paměť mimo vytvářenou tabulku.

Křížový odkaz z §2.3.3 na SCOPE v §2.4-12 je uzavřen. Obě
reprezentace využívají souvislý úsek preorderu, jen konec intervalu
je v §2.3.3 výlučný a v §2.4 zahrnutý. Rozdíl c odpovídá velikosti
jednoho záznamu. Zbylé historické citace §2.3.3 tím uzavřeny nejsou.

C0061 je potvrzen samostatnou kořenovou revizí původních stran:
EOF odpovědi13 popne i sentinel a potom čte prázdný zásobník.
Úplný protipříklad a oprava jsou v reportu a tree-boundaries-and-eof-root-review.
Známých15 oprav kontroluje errata.md; nález EOF jimi pokryt není.

Úspěšný doplňkový běh se neopakoval: 5461 vstupních řad hladin,
10066 pojmenovaných lesů, 362376 kvalifikací, 46462 dvojic kořenů,
341706 porovnání jmen a10066 kontrol pravidla(c). To doplňuje,
nikoli nahrazuje obecné důkazy. Technika celé sekce je uzavřena,
celkově jsou úlohy4,12,15 a historická pasáž433 stále partial
výhradně pro přesně vypsané historické/atributivní prameny.
Fyzický výtisk nebyl ověřen, žádný report nebyl odeslán.
