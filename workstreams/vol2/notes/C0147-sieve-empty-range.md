# V2-C0147: síto nemá ošetřen prázdný rozsah

Stav: **confirmed**. §4.5.4-8, zadání412 a odpověď658.
Kontrola3.11.2026, třetí vydání/první tisk1997; původní
strany412/658 a all2-prepre41 zobrazeny.

Vezměme N=2, tedy M=1. Výstup musí být prázdný, protože
žádné liché prvočíslo není menší než2. Původní S1 vytvoří
X[1]=1, nastaví j=1,p=3,q=4; S2 vypíše3, což je mimo rozsah.

Známé opravy23.4.2001 a21.8.2001 zavádějí k=1, mění pole
na X[1..M-1] a meze smyček na ostré. **Po těchto opravách**
je pro M=1 pole prázdné, ale j=1 a bezpodmínečný přechod
doS2 zůstává. S2 tedy čte nedefinované X[1].
Nejde jen o opakování již opraveného krajního indexu.

Stačí předS1 ukončit algoritmus pro N<=3, případně výslovně
předpokládat M>=2. Pro obecný celočíselný vstup lze volit
M=floor(N/2). Úplný důkaz opraveného síta a obou implementací
je v [factoring-basic.md](factoring-basic.md).

Prohledány all2-prepre,all2-pre,all2,err2 i současný
`sources/err2.textxt`: jiná oprava tohoto vstupu nenalezena.
Přesný reproduktor vrací u původního kódu[3] a u verze
se všemi známými opravami KeyError(1); opravená verze vrací[].
To je ilustrace přímého důkazu, nikoli důkaz jen testováním.
Nový fyzický dotisk a priorita neověřeny; návrh neodeslán.
