# V3-C0025 — vylepšené ProgramL:433u místo358u

**confirmed / low**,2026-11-07. Tištěná626/file637, odpověď§5.2.1-36,
poslední věta. Chybný je číselný čas, nikoli třídění nebo jeho stabilita.
Sazba625 (kód33 a správná obecná cena) i626 (údaj358u) zobrazeny.

Program33 má dvě střídající se porovnávací banky LD/CMP/JG, každou za5u.
Každé z N−1 vložení udělá b_j úspěšných porovnání a jedno závěrečné.
Zápisy stojí4(N−1), dodatečný JMP se provede N' krát, závěrečná skupina
DEC/ENT/LDA/J1P stojí5N a inicializace6. Proto obecně přesně

    T=6+5(B+N−1)+4(N−1)+N'+5N=5B+14N+N'−3.

Tento vzorec je na625 vytištěn správně a celý invariant/kód jsou doloženy
v `insertion-proof-list-95-97-32-33.md`. Sentinel je největší platný
klíč a JG je přísné; všechna závěrečná porovnání jsou nutná i při rovnosti.

U16 zadaných hodnot jsou počty menších klíčů napravo

    (6,1,6,0,11,1,9,1,4,1,0,0,0,0,1,0).

Tedy B=41 a N'=7 lichých členů. Násobení klíčů1000 podle zadání36
pořadí nemění a tři byty základ100 hodnoty pojmou. Dostáváme

    T=5·41+14·16+7−3=433u.

Už dolní mez N'≥0 by dávala426u>358u. Rozdíl433−358=75u se rovná
5(N−1), tedy přesně ceně závěrečných porovnávacích bank; to je možné
vysvětlení, nikoli tvrzení o autorově postupu. PůvodníL má správně496u.

Oprava: v poslední větě odpovědi36 nahradit358u za433u.
Pět vrstev errat: `sources/list-insertion-time-errata-review.json`.
Známé typografické úpravy625 a závorky626 nic nemění na číselném údaji;
historické603–604 obsahují jen opravy komentářů33 a jiný programS.
Žádný matematický běh, žádná enumerace; tvrzení je doloženo součtem
všech instrukcí a přímo vytištěnými16 klíči. Nejde o garanci novosti.
