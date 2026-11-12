# V3-C0009 — distribuční třídění při u=v

Potvrzená chyba MIX programu v odpovědi §5.2-9, s.616 / file627.
Algorithm D na78 výslovně připouští u≤Kj≤v; odpověď přidává pouze
požadavek, aby |u| a |v| vešly do dvou bytů. Pro u=v je M=v−u=0.
Akumulační smyčka přesto provede jednu iteraci: ENN3 M-1 nastaví rI3=1,
LDA načte COUNT[u], ADD a STA přistoupí na COUNT[v+1]. To je mimo
povolenou tabulku; samotný abstraktní Algorithm D tuto chybu nemá.

Konkrétní ruční průchod s platnými, navzájem disjunktními oblastmi:
N=2, U=V=0, COUNT=INPUT=100, OUTPUT=200. COUNT[0] zabírá pouze adresu100,
vstupní záznamy jsou na101 a102, výstup na201 a202. Vstupní celá slova
R1=+1, R2=+2 mají oba klíč0 v poli0:2, satelity1 a2 v poli3:5.
D1–D3 nastaví paměť[100]=2. Chybný D4 načte2, přičte paměť[101]=1
na3 a zapíše3 zpět do101. D5–D6 potom vydají slova+3,+2 místo+1,+2.
Výstup tedy není permutací původních záznamů. Žádný přetečený registr
ani překrývající se oblast nejsou potřeba.

Oprava: při M=0 přeskočit D4 (případně výslovně omezit program na M≥1).
Sazba78 a616 prohlédnuta. V all3-prepre, all3-pre, all3, err3 a historické
err3-1e nebyla nalezena odpovídající oprava; sources/insertion-errata-review.json.
Prvenství ani fyzický výtisk neověřeny. Důkaz je ruční, bez emulace/enumerace.
