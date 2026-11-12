# V2-C0175: předčasné zastavení E může ztratit faktor

**Stav: candidate.** Odpověď §4.5.4-37 na665 doporučuje skončit
v E5 při U=U' nebo V=V', protože druhá část periody opakuje
hodnoty V. Palindromická věta i symetrie stavů jsou správné;
jsou dokázány v [factoring-refinement.md](factoring-refinement.md),§5.
Prosté přidání uvedené stop-podmínky ale může zahodit faktorizaci.

Původní E, N=323=17·19, k=1, báze2,7,11:

|Průchod|U|U'|V|P|S|Zbytek po E3|
|---|---:|---:|---:|---:|---:|---:|
|1|34|34|34|17|1|17|
|2|34|34|1|18|0|1|

Předčasná varianta skončí v prvním řádku bez výstupu.
Celý algoritmus dá `18²=1 mod323`; F vrátí gcd(18−1,323)=17.
Báze je nesoudělná s N a všechny její členy jsou dovolené
kvadratickým testem. Nejde o dřívější C0159.

Příklad přetrvává i se změnou E1 z2.7.2001. Pro N=323,k=2,
bázi2,3,5,7,13 je inicializace U=42,V=21,P=51.

|Průchod|U|U'|V|P|S|Zbytek po E3|
|---|---:|---:|---:|---:|---:|---:|
|1|42|42|17|51|0|17|
|2|50|42|21|127|1|1|
|3|50|50|1|305|0|1|

Předčasná varianta opět nedá výstup. Celá dá relace−21 a1;
z druhé F získá gcd(305−1,323)=19. Obě stopy byly zkontrolovány
nezávislými nezkrácenými konvergenty. Jsou uloženy v JSON.

Klasifikace zůstává opatrná. E je pouze pokus o získání relací
a kniha dovoluje jeho dřívější ukončení; věta u37 výslovně
neslibuje zachování všech nalezitelných faktorů. Protipříklady
proto dokazují ztrátu informace, nikoli doslovné porušení takové
výslovné záruky. Doporučení by bylo přesnější doplnit výhradou
nebo zpracováním středového/závěrečného stavu. V našich příkladech
by přidaný gcd s centrálním V faktor odhalil, ale tento krok E
neobsahuje. Netvrdíme obecnou dostatečnost takové opravy.

Sazba397–398/415/665 přečtena. Všechny vrstvy errat a err2.textxt
prohledány pod stránkami,37,periodou a ukončením; odpovídající
oprava nenalezena. Pozdější fyzický dotisk a priorita neověřeny.
Hlášení nebylo připraveno k odeslání ani odesláno.
