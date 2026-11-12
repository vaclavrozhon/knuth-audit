# MMIX — rejstřík, slovníček a závěrečné tabulky

**V0181, p. 127–134 — opakované matematické definice, převzato.**
Associative law na p.127 je rovnost závorkování a používá se přesně
ve V0050. Commutative law na p.128 je záměna pořadí operandů;
pro bitové operace a maticovou transpozici má argument V0045/V0052.
Big-/little-endian na p.127/130 jsou pořadí vah v pozičním rozvoji,
V0014. Bit, byte, wyde, tetra, octa mají velikosti1,8,16,32,64 podle
V0010; nybble4 a nyp2 jsou polovina a čtvrtina osmibitového byte
(úloha §1.3.1′–1). Definice matrix jako dvourozměrného pole je
konzistentní s indexy V0050. Profile jako počet provedení instrukcí
je právě invariant a součet použitý u Programu M a úlohy §1.4.3′–2.
Notace b,m,t,s,u,v,w,monus,shifts a množinové operace pouze odkazují
na již jednotlivě zdůvodněné V0012,V0041–V0053 a příslušné úlohy.
Žádný nový matematický výsledek zde není tvrzen.

**V0182, p. 127–134 — bibliografie rejstříku, partial.**
Jména, plná osobní jména, přepisy hebrejštiny/arabštiny/čínštiny,
všechny jednotlivé stránkové odkazy a úplnost hesel nebyly nezávisle
ověřeny. Tato přesná bibliografická výjimka se týká celého rejstříku,
nikoli dříve doložených matematických definic. Rozšíření zkratek
společností/standardizačních organizací jsou terminologické údaje;
externí registry nebyly znovu dohledány.

**V0183, zadní listy file144–145 — původně partial, nyní úplné tabulky.**
ASCII blok má šest řádků po16 pozicích, #20…#7f; 95 tisknutelných
znaků #20…#7e plus netisknutelný DEL. Počet a konkrétní MMIX/Latin
příklady přebírá V0006 a results/character-examples-p003.json.
Dvojice zadních listů opakuje tutéž tabulku opcode jako p.20:
16×16 pozic, immediate/backward dvojice a π=2υ pro taken.
Základní strukturální a časové vztahy přebírají V0073–V0075,
operandové rodiny V0172. Při obnově kvality nyní byly všechny256 buňky
každé ze tří tabulek samostatně porovnány s primární tabulkou opcodů
a deklarovaných cen v MMIX-SIM, včetně obou výsledků každého B/PB.
Všech95 tisknutelných ASCII pozic a DEL na obou zadních listech bylo
porovnáno s primární tabulkou Unicode/Latin-1 a původní sazba zobrazena.
Úplné certifikáty jsou `results/opcode-table-reconciliation.json` a
`results/ascii-endpaper-reconciliation.json`; rozsah/důkaz v
`notes/recovery-pages-024-033.md`. V0183 je proto argument_recorded.
Tento závěr netvrdí správnost všech implementací opcodů: úplná IEEE
sémantika zůstává odděleně partial ve V0054/V0055.

Souvislý argumentový průchod dospěl ke konci knihy. Neznamená to
uzavření všech položek partial v inventáři. Celé čtení145/145 bylo
hotové už dříve a bylo zachováno samostatně.
