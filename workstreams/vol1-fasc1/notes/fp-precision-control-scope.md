# MMIX — přesný povinný rozsah IEEE §4.3

7. listopadu 2026. Tato kontrola uzavírá jednu dříve příliš silně
formulovanou mezeru V0054; nezavírá desítkové konverze ani enabled trips.
Primární zdroje jsou `sources/ieee754-1985.txt` §1.1, §3.4, §4.3,
§5.1–5.3 a `sources/mmix-doc-20131017.w`:1498–1538.

IEEE §1.1 určuje shodu podle prostředí viditelného programátorovi,
včetně potřebného softwaru. Podle §5.1 musí být aritmetika dostupná
pro dva operandy stejného podporovaného formátu a výsledek musí mít
formát alespoň tak široký jako širší operand. Smíšené vstupní formáty
jsou doporučené, nikoli povinné. Totéž pravidlo šířky platí pro square
root v §5.2. Samostatná konverze do užšího formátu je podle §5.3
jiná operace s vlastním jediným zaokrouhlením.

§4.3 vyžaduje přepínač kratší přesnosti **u systému, který dodává
výsledky pouze do double/extended destinací**. Podmínka není tvrzení,
že každý systém podporující double musí navíc poskytovat jednorázově
zaokrouhlenou operaci nad double vstupy s24bitovou mantisou a širším
exponentem. Poznámka2 výslovně vysvětluje účel: napodobit přesnost
systému se single destinací tam, kde vlastní systém takovou destinaci
neposkytuje. Rozšířený exponent je tam dovolený („may“), nikoli
univerzální požadavek na další formát. Tatáž poznámka naopak nedoporučuje
operace s double vstupy a single výstupem s jediným zaokrouhlením.

MMIX v programátorském prostředí single destinaci poskytuje. Přesná
implementovaná operace je:

    LDSF operand(s); one arithmetic operation; STSF destination

Zdroj ji výslovně nabízí pro všech sedm operací. Úplný již uložený
důkaz `notes/fp-short-arithmetic-recovery.md` pokrývá libovolné binary32
vstupy, všechny čtyři stejné režimy, oba signed zero, NaN/infinity,
celou subnormální a overflow mez i všechny disabled-trip eventy.
Má každé zaokrouhlení, každý false-midpoint případ a deklarované ceny;
nezaměňujeme jej za tvrzení „double má dost bitů“. Výsledná destinace
je **binary32 v paměti**. Pro širší binary64 vstupy jsou samostatně
poskytovány binary64 operace. Proto prostředí nesplňuje předpoklad
„only double or extended destinations“ a nový obecný precision-control
režim se z §4.3 neodvozuje.

Přípustné stavy převzaté sekvence zůstávají přesně stejné: povolené
paměťové adresy, zachované operandy, neměnný režim a vypnuté arithmetic
trips. U architektonického kontraktu je tím konkrétní precision otázka
uzavřena. Původní doprovodný program vyžaduje již doložené opravy
S0002/S0003/S0004; tato poznámka je nezamlčuje ani je znovu netestuje.
Enabled-trip rozhraní a jeho případná softwarová vrstva mají zvláštní
otevřený závazek. Nelze je uzavřít tímto důkazem defaultní aritmetiky.

Leaf MMIX-FP-IEEE-PRECISION-CONTROL lze označit argument_recorded.
Široký V0054 zůstává partial kvůli desítkovému a trapping rozhraní.
Žádný nový nález ani běh. Z dřívějšího seznamu se odstraňuje dodatečný
nevytištěný úkol; nepřidává se předpoklad o hypotetickém hardwaru.
