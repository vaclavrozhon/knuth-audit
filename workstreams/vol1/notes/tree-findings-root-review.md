# Kořenová revize nových stromových nálezů

Kontrola 1. listopadu 2026. Tato poznámka zachycuje nezávislé ověření
jednotlivých podezření; nenahrazuje úplnou revizi přidělených oddílů.

## V1-C0041: opětovné vybrání vrcholu v odpovědi §2.3.4.1-12

Originál s. 580 a obrazy errat `all1-prepre-page43`, `all1-pre-page17`,
`all1-page15`, `err1-page13` jsem přímo prohlédl. Zadání 371 dovoluje
obecné ceny; geometrický příklad neomezuje celý kontrakt. Znovu jsem
prohledal všechny čtyři texty errat podle strany i operací.

Pro ceny z podagentova dokladu je průběh tabulky a přesně
`(1,3,10) -> (infinity,2,10) -> (2,infinity,10)`. Následuje opět výběr
indexu 1 a duplicitní hrana 12, zatímco vrchol 3 zůstává izolovaný.
Už vybraná nekonečna nesmí vstoupit do aktualizace; po doplnění této
podmínky zůstává a(j) minimální cenou hrany ze zbývajícího j do vybrané
množiny. Výměna hrany přes její řez dokazuje minimalitu pro libovolnou
konečnou úplnou síť. Podmínka j!=i pouze vyjasňuje chybějící diagonálu;
samotná vada na diagonále nezávisí.

Protipříklad i obecný důkaz opravy jsem ověřil ručně. Konečné testy jsou
doplňkem, nebylo třeba je znovu pouštět. Stav: **confirmed**. Fyzický
výtisk ani prvenství se netvrdí.

## V1-C0042 a V1-C0043: přetečení pomocných testů v derivátoru

Přímo jsem prohlédl s. 338, 345 a 574, přečetl souvislý kontrakt
337–340 a relevantní program. Konstanta má TYPE=0 a její hodnota je
celé slovo INFO; menší rozsah ani zákaz záporných konstant zde není.
Označme b základ MIX a B=b^5, první kladnou hodnotu, která se do slova
nevejde. Absolutní hodnota slova se při přetečení redukuje modulo B.

V MULT je c=-(B-1) přípustné. Výpočet c-1 dá zápornou nulu; JANZ
tedy neodbočí a TYPE=0 nechá operand odstranit jako jedničku. Při
derivování c*x je správným výsledkem právě c, takže příklad nevyžaduje
žádnou nereprezentovatelnou matematickou operaci. Obě operandové větve
obsahují stejnou vadu. CMPA s existující konstantou a JNE ji opravují.

Pro PWR volíme v=-(B-2). Exponent výsledku v-1=-(B-1) je stále
přípustný; přeteče pouze nadbytečný test v-2. JAZ zamění v za 2 a
ponechá základ x místo x^(v-1). Následující MULT se pro tento v
chová správně, protože v-1 není nula ani přetečený výsledek. Příklady
jsou tedy nezávislé. CMPA CON2+1, JE 3F, DECA 1 tvoří správnou opravu
tohoto testu. Analytický příklad bereme na x>0.

Přečetl jsem přepis `programs.py`, celou nezávislou symbolickou funkci
v `check_mix.py`, nastavení skutečných uzlů a jejich kontrolu, a záznamy
74 běhů. Bez opakování již provedených testů souhlasí všechny základy
64–100 s obecným výpočtem. Oba nálezy jsou **confirmed**.

## V1-C0044: čas COPY

Originál 573 přímo uvádí 36n+22. V přepisu jsem znovu sečetl ceny
deseti tištěných skupin instrukcí: výsledkem je 36n+14 pro 064–103,
nezávisle na počtu neterminálních uzlů a. Při vstupu COPY připočítáme
STJ a návratový JMP, tedy 36n+17. U jediného listu jsou navštíveny
063–067, 070–079, 089–095, dvakrát 096–098 a jednou 099–104;
cena je 53. Další možné vstupy přidají pouze 1 nebo 2 jednotky,
volající JMP další 1. Žádná konvence nedává tištěných 58.

Jde o úspěšné kopírování s dostatkem paměti; zadání tento předpoklad
výslovně nevyslovuje, proto byla podagentova příliš silná formulace
opravena. Rozpor platí již pro jediný list. Stav: **confirmed**.

Pro C0042–C0044 jsem navíc znovu prohledal čtyři vrstvy errat podle
stran, názvů rutin i testů a prohlédl původní all1-prepre 23/42,
all1-pre 17, all1 15 a err1 13. Zásahy COPY2/COPYP2 a chybějícího
operandu TREE jsou odlišné a zdejší vady neopravují.

## V1-C0045: kardinální úrovně nekonečného stromu

Originály 317/562 přímo prohlédnuty. Každé T[a] má c=|R| vlastních
předků, každé S[a,m,n] má c+n=c předků. Proto je množina hodnot
definované funkce level jednoprvková. Slabší požadavek nespočetného
řetězce předků je však splněn. Podklad eviduji jako **candidate** pro
terminologii, nikoli jako chybu vnořené konstrukce. Pouhé nahrazení
kardinálu ordinálem tuto hustou hierarchii neopravuje.

## V1-C0046: levý odkaz při vkládání uzlu

Originály 327/333/570 přímo prohlédnuty. Tištěná odpověď LLINK(Q)
skutečně nezapisuje. Pro nově přidělenou paměť s LLINK(Q)=P se
po vložení pod jediný P vytvoří cyklus; pro Q již inicializovaný
jako izolovaný list však algoritmus funguje. Předloha I svůj
odpovídající odkaz výslovně nastavuje, což podporuje návrh doplnění,
ale samo nevylučuje silnější výklad vstupu „single node“. Proto
konzervativně **candidate** s přesně popsanou nejistotou kontraktu.
