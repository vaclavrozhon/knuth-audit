# Kořenová revize buddy alokace

1. listopadu 2026. Přečteny oba stabilní reporty, PROOFS-buddy.md,
buddy.py, minimální reprodukce a její výsledky. Přímo zobrazeny původní
strany 443,611,612 a příslušné původní opravy all1-prepre29,46;
aktuální all1-pre18 již přečten při předchozí revizi. Výpis ze všech
čtyř vrstev je results/buddy-root-errata.json. Úspěšné testy podagenta
se při kořenové revizi neopakovaly.

## C0067: konec fondu není přesah

M je počet slov na adresách 0,...,M−1, k určuje délku bloku 2^k
a P jeho počátek. Všechny adresy bloku jsou uvnitř právě tehdy,
když P+2^k<=M. Rovnost se proto nesmí vylučovat. V odpovědi 26
na straně 611 je neostré >= přímo viditelné.

Pro M=6 a rezervovaný blok [0,4) mohou být bloky [4,5) a [5,6)
uvolněny v tomto pořadí: nejdřív 5, potom 4. Při druhém vrácení
je buddy P=5, k=0. Vytištěná podmínka jej označí za rezervovaný,
ačkoli je celý ve fondu a je ve správném seznamu volných bloků.
Žádost o dva volné sousední bloky pak selže. Ostré > vše opraví.
Jde o neúspěch slévání, nikoli o čtení neexistujícího slova.

## C0068: neúplná záměna konců seznamu v roce 2006

Nechť h je adresa hlavy a F(P), B(P) dopředný a zpětný odkaz uzlu.
V platném dvouprvkovém seznamu h→a→b→h máme B(a)=h, B(h)=b.
Instrukce 08 a14 ponechávají rI4=a=F(h). Publikované změny pouze
v řádcích 17,18,20 pak provádějí

```text
rI5 <- B(a) = h,
B(h) <- rI5 = h,
F(rI5) <- h, tedy F(h) <- h.
```

Oba odkazy hlavy ukazují na ni samu. Blok a se rezervuje, ale
blok b už není dostupný ze seznamu. Protipříklad nepotřebuje
spoléhat na simulátor; plyne přímo z těchto tří přiřazení.

Minimální fond čtyř slov má a=0,b=2 a rezervované bloky 1,3.
Je dosažitelný přidělením čtyř jednotkových bloků a vrácením 2,0.
Další žádost po ztrátě b nesprávně hlásí overflow. Původní
instrukce z roku 1997 odpojují ze seznamu správně a jsou zde
bez této vady. Abstraktní oprava R2 na straně 443 je také správná.

Vložení LD4 AVAIL,2(LINKB) na nový vstup R2 opraví jak nalezení
bloku v počáteční velikosti, tak větev po prohledání vyšších velikostí.
Nemění znaménkovou kontrolu sentinelu v řádcích14–15. Samotná
výměna LINKF za LINKB na těchto dvou místech by vyžadovala zvlášť
přezkoumat rozsah pole zahrnující znaménko; report navrhuje jednodušší
jednu vloženou instrukci.

Kořenový součet nákladů původních řádků: vstup05–08 stojí6,
smyčka09–11 stojí3(1+R), řádky12–15 stojí5R, část17–22 stojí10,
část23–33 stojí17R. Celkem19+25R, po lokální opravě21+25R.
R je počet dělení; volající skok a kód DONE se nezapočítávají.

## C0069: komentář zaměňuje L a P

Nezávisle na publikované změně má původní řádek20 v odpovědi27
komentář LINKB(L)←LOC(AVAIL[j]). Instrukce však ukládá na adresu
v rI5, tedy P=LINKF(L), které předtím načetl řádek17. Správný
komentář je LINKB(P)←LOC(AVAIL[j]), jak má abstraktní R2 na443.
V roce2006 se v komentáři mění B na F, ale chybný argument L
zůstává. Opravený komentář nové varianty je LINKF(P)←LOC(AVAIL[j]).

Tato třetí vada je pouze chyba vysvětlujícího komentáře. Původní
instrukce20 ukládá správně a nesmí se kvůli komentáři měnit.
Je evidována zvlášť od funkční vady pozdějšího errata.

V žádné ze čtyř vrstev nebyla nalezena oprava hranice úlohy26,
chybějícího načtení konce seznamu ani argumentu komentáře.
U C0068 je zdrojem vady právě veřejná oprava z 6. listopadu2006;
nejde o tvrzení, že původní program1997 selhává. Pozdější fyzický
tisk nebyl prohlédnut, prvenství se netvrdí a nic nebylo odesláno.
