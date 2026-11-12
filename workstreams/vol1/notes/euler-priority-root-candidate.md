# V1-C0089: kvalifikace Eulerova prvenství na s. 49

Stav **candidate**, nikoli potvrzená historická chyba. Knižní větu
„he was the first to find“ lze číst jako tvrzení obecného prvenství,
ale v kontextu také jako porovnání s právě probíraným Stirlingem.
Získané dopisy dávají důvod k redakčnímu upřesnění; pořadí objevu
z nich samotných neplyne.

Root přímo zobrazil knižní s. 49, titul Fuss II a s. 324–325
(PDF 11, 362, 363). Dopis XLVII je datován 6. října 1729 a podepsán
Danielem Bernoullim. Jeho dovětek má obecný výraz, nikoli pouze
jednotlivou interpolovanou hodnotu. Pro pevné reálné x > 0 a kladné
celé A jej označme

    B_A(x) = (A+x/2)^(x-1) product_{j=1}^{A-1} (j+1)/(j+x).

Knižní konečná aproximace pro kladné celé m je

    T_m(x) = m^x m! / product_{j=1}^m(x+j).

Přesným krácením součinů dostáváme

    B_{m+1}(x) / T_m(x)
      = (1+1/m) (1+(1+x/2)/m)^(x-1) -> 1.

Jde tedy o stejnou limitu pro každé pevné x > 0. Root také přímo
četl Eulerův dopis ve Fuss I, s. 3–5, a v kritickém přepisu 2016,
s. 99 a 102. Euler v něm výslovně zmiňuje jejich dřívější komunikaci.
Dřívější datované Bernoulliho sdělení proto **nedokazuje**, že Bernoulli
výsledek objevil dříve než Euler.

Kritický komentář na s. 586, pozn. 5, označuje Bernoulliho dopis
jako 10. října; root obraz PDF 595 přímo přečetl. To nesouhlasí
s datem 6. října v přečteném Fussovi. Obě data předcházejí Eulerovu
13. říjnu, ale rozpor není svévolně rozhodnut. Eulerovo datum 13. října
podporuje kritický přepis; Fuss I tiskne 16. října. Meze edice a
nepřečteného autografu jsou v hlavní root poznámce.

Možná minimální úprava je „he found“, ale nejde o hotové hlášení
potvrzené chyby. Anglický ASCII návrh je v neměnném paketu
`reports/euler-first-generalization.txt`; žádná zpráva se neodesílá.
Čtyři erratové vrstvy byly prohledány; odpovídající oprava nenalezena.
Vzorec (13) ani datum Eulerova dopisu se tím nenapadají. Matematické
testy nebyly opakovány. Všechny podklady fixuje
`results/stirling-euler-legendre-root-manifest.json`.
