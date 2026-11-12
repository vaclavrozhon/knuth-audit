# Kořenová revize dokončených stromových bloků

Datum 2026-11-01, pracovní větev audit/vol1. Zmrazené podklady:
parallel/binary-tree-representation/HANDOFF.md a parallel/free-trees/REPORT.md.
Kořen přečetl oba celé soubory obecných důkazů, inventáře, přehledy errat
a přesné vymezení pramenů. Nové nálezy C0041–C0044 byly nezávisle potvrzeny
již v notes/tree-findings-root-review.md, včetně původních obrazů,
instrukčních pravidel, ručních protipříkladů a součtů časů.

## §2.3.2

Přijaty obecné důkazy bijekce lesů a binárních stromů, vztahů průchodů,
lexikografického pořadí, předků, rodičovského seznamu i vložení stromů.
U vložení je podstatné zachování obou průchodů: přesun obrazu kořene výše
nezpůsobí kolizi s obrazem potomka. Explicitní protipříklad opačné implikace
má kořen se třemi listy versus kořen s dvoulistým dítětem a dalším listem.

Diferenciační pravidla mají vyznačené domény a oddělují hodnotovou shodu
od zachování původního definičního oboru. Kořenový invariant původního D
správně rozlišuje přesměrovaný vnější RLINK a nedotčený vnitřek podstromu.
COPY obnovuje vstup a jeho registrový kontrakt dovoluje všechna použitá
volání v DIV/PWR. Dříve přečtený doslovný MIX a jeho hraniční příklady
nebyly bezdůvodně znovu spouštěny. Nové úplné testy mají 1 930 diferenciací
a 498 kopií; jsou oddělené od 74 hraničních běhů a dalších pomocných dávek.
Vlastní COPY, DIV a PWR jsou skutečné MIX instrukce, ne hostitelské náhrady.

U volného svazu končí rozhodovací rekurze podle součtu velikostí dvojice
termů; prioritní konjunkční pravidla při souběhu dávají stejné čtyři páry.
Druhá kontrola přes konečný uzávěr používá doplnění částečného uspořádání
pomocí řezů, které zachová existující průseky a spojení. Výklad nepředpokládá
distributivitu: pro a meet (b join c) proti (a meet b) join (a meet c)
je výslovný nedistributivní pětiprvkový protimodel. Technická odpověď
19 je proto dokončená i při chybějícím textu obou Whitmanových článků.

Celkově zůstává partial hlavní historická datace1952 a úlohy17/19
kvůli přesně uvedeným pramenům. TRIAGE u odpovědi8 chybějící indexovou
mez k<nprime nepočítá jako další potvrzený nález. Žádný nový report
kromě C0042–C0044 se při této revizi nepřidává.

## §2.3.4 a §2.3.4.1

Přijaty obecné důkazy Theorem A, báze toků, obou směrů Theorem K,
všech13 úloh a ručně vysvětlené koeficientové identity obrázků.
Důkaz Theorem A pro nekonečné grafy používá konečné cesty; počet hran
n−1 je uplatněn jen v konečné neprázdné části. Eulerovský důkaz Theorem K
pracuje s celočíselnými toky a se souvislou kladnou podporou. Bez těchto
předpokladů by opačná implikace neplatila; knižní kontext je poskytuje.

U úlohy8 byly zvlášť zkontrolovány tři vyčerpávající možnosti rozštěpení
sloučených hran, včetně smyčky. Surjektivita se správně týká reálných toků,
nikoli nezápornosti. Ekvivalence příchozí a odchozí konstrukce používá
komponenty bipartitního grafu s kopiemi zdroj/cíl; obě hrany pro tok vrcholu
v vedou z komponenty R(v) do komponenty L(v). To dokazuje obecné tvrzení
bez spoléhání na nedostupný Nahapetianův článek.

Algoritmus E, použitý úlohou6, byl mezitím kořenově dokázán i otestován
v §2.3.3. Výměnný argument minimální kostry dovoluje rovné i záporné ceny
a potvrzuje opravu C0041. Primův primární text navíc přímo odstraňuje
již vybrané sloupce, takže nová chyba patří tabulkové odpovědi TAOCP.

Úloha8 zůstává partial pro Nahapetiana a obrazový originál
Knuth–Stevenson. Navíc kořen zachovává dosud výslovně nevyřešenou
bibliografickou dataci GraphBase1993/1994 jako partial u úlohy12;
technický nález C0041 zůstává confirmed. Tato konzervativní odchylka
od UNIT_STATUS podagenta zabraňuje ztrátě mezery přiznané v sources.md.
Nejde o potvrzenou bibliografickou chybu ani nový kandidát.

## Meze revize

Kořen četl všechny uvedené obecné důkazy a samostatně rozhodl nové
nálezy. Nepřisvojuje si osobní přečtení všech obrazů citovaných článků,
které dokumentuje podagent; přesné čtecí meze zůstávají u každého zdroje.
Neopakoval úspěšné velké testy. Fyzický výtisk nebyl ověřen, žádný report
nebyl publikován ani poslán autorovi. Práce na zbytku svazku pokračuje.

