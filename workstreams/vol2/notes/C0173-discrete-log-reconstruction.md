# V2-C0173: nesprávná rekonstrukce diskrétního logaritmu

Stav: **confirmed** vůči dostupnému prvnímu dotisku a řadám errat.
Odpověď4.5.4-46 na671 násobí koeficienty vztahů exponentem e_jk namísto
původního exponentu mocniny n_i. Už p=7,a=3 a jediný vztah3²=2 modulo7
dává podle tisku logaritmus2 roven1; správně je2.

Současně je třeba sjednotit koeficienty pro různé souřadnice: správně
sum_i c_ik e_ij+(p−1)t_jk=[j=k] a N_k=sum_i c_ik n_i modulo p−1.
Koeficient c_ik je stejný pro všechna j. Všechny vady tohoto jednoho
algebraického přepisu sdružujeme pod C0173.

[Obecný důkaz a testy](discrete-log.md); původní
[detail sazby](../images/vol2-p671-answer46-detail.png). Všechny vrstvy
errat prohledány3.11.2026; oprava9.2.1998 mění jen závěrečné modulo p
na modulo p−1 a uvedenou chybu rekonstrukce neřeší.

Pozdější fyzický dotisk a priorita neověřeny.
[Návrh hlášení](../reports/C0173-discrete-log-reconstruction-draft.txt)
nebyl odeslán.
