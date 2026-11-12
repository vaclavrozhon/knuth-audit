# V2-C0130: výjimka v pomocné nerovnosti pro řetězové zlomky

Stav: **confirmed**, drobná chyba formulace v důkazu.
§4.5.3-6, odpověď na straně 647, první dva řádky.

Text tvrdí 0<=C(x_1,...,x_n)<1 pro kladné celočíselné podíly,
kde C je knižní zápis se dvěma lomítky. Pro n=1,x_1=1 však
podle samotné definice C(1)=1. Jde o jedinou výjimku mezi
neprázdnými konečnými seznamy kladných celých podílů.

Stačí doplnit výjimku jednočlenného seznamu (1), případně zde
výslovně omezit tvrzení na ocasy s posledním podílem >1.
Samotná jednoznačnost požadovaná v zadání úlohy je správná:
u konečného vstupu zadání předpokládá B_m>1 a u nekonečného
vstupu je každý následující ocas kladný. Vlastní úplný důkaz
je v `euclid-basic.md`; nejde o protipříklad hlavní věty.

Původní stránka 647 byla zobrazena, ostré znaménko < je zřetelné.
Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
prohledány 2026-11-03 podle stránky, odpovědi 6 a podmínek pro
kladné podíly. Nalezena pouze sousední oprava odpovědi 7,
která se této nerovnosti netýká. Oprava tohoto místa nenalezena.
Nejnovější fyzický dotisk ani priorita nebyly ověřeny;
návrh hlášení zůstává neodeslaný.
