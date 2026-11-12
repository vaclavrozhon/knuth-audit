# Audit §1.4.1: podprogramy

Datum 1.11.2026. Zdroj je první dotisk třetího vydání (květen1997),
ověřený společným inventářem a tiráží. Fyzický tištěný exemplář nebyl
ověřen. Tištěná strana p odpovídá straně p+15 souboru DjVu. Zobrazeny
byly originály186–193,527–528 a dříve uložený originál145; výřezy/OCR
slouží pouze k navigaci. Vlastní obrázky jsou v `../images/`.

Značení: rA,rX a rI1,...,rI6 jsou registry MIX; rJ drží návratovou
adresu. CI je porovnávací indikátor se stavy less/equal/greater. Bajt
má b možných hodnot, 64<=b<=100. X[k] znamená slovo v adrese X+k.
Paměťové intervaly jsou platné a nezasahují do kódu ani jeho pomocných
buněk, není-li výslovně řečeno jinak. Dva datové intervaly MOVE se
překrývat mohou. Znaménko nulového slova se zachovává, pokud instrukce
výslovně neurčuje jiné.

## Hlavní text a programy

Pojmy podprogram, vazba, parametry, argumenty, vstup a výstup jsou
použity konzistentně. Pro MAX100(1) platí stejný invariant jako pro
Program1.3.2M: před porovnáním X[k] je rA maximum již prohlédnutého
suffixu a rI2 jeho největší index. Jen striktně větší X[k] mění maximum.
Po posledním DEC3 je rI3=0; rA a rI2 mají požadované hodnoty. STJ
na vstupu uloží adresu za volajícím JMP do adresního pole EXIT;
pozdější skoky mění rJ, ale tuto uloženou adresu neovlivní.

Je-li délka opakovaného bloku k a počet jeho umístění m, nahrazení
podprogramem používá k+m+2 slov, a proto šetří
`mk-k-m-2=(m-1)(k-1)-3`. Pro k=2 je zisk až při m>4.
JMP,STJ,JMP stojí1+2+1=4u na každé volání. Má-li volací sekvence c
slov a tělo přídavnou režii L, úspora je
`mk-k-mc-L=(m-1)(k-c)-(c+L)`, což dává(3). Jde o výslovně
idealizovaný model; text upozorňuje na specializaci a ukládání registrů.

Uložení rI3 instrukcí ST3 do pole(0:2) budoucího ENT3 a následné
ENT3 jej obnoví včetně znaménka nuly. Dodatek má dvě instrukce a3u.
Tvrzení o nejkratší/nejrychlejší variantě je zde posouzeno pro danou
metodu zachování registru v jinak nezměněném MAX100, ne jako globální
optimalita libovolného programu počítajícího maximum.

Vstup MAX100 v(5) nastaví rI3=100, obecný MAXN zachová zadané n;
ENT3 nemění J, takže společné STJ uloží správný návrat. V(6) musí
pomocný skok být JSJ, protože JMP by přepsal dosud neuložený návrat.
V(8) se adresa argumentu uloží do ENT1; následně rI1 drží tuto adresu,
LD3 načte n a JMP1,1 přeskočí argument. Zvláštní MAX100 s lokálním
návratovým JMP opravdu funguje: svůj návrat ukládá mimo společný
MAXN, který se vrátí právě na tento JMP.

V(9) je po hledání rI3=0. JANP volí první výstup při max<=0,
CMPA/JGE totéž při max>=rX; pouze zbývající větev nastaví rI3=1.
EXIT s indexem3 proto míří právě do požadované ze dvou adres. Na n=1,
záporné hodnoty, shodná maxima a hranice0/rX není potřeba zvláštní
výjimka. TEMP je zde skutečný vedlejší zápis;(9) netvrdí úplný
kontrakt bez paměťových účinků.

V(10) opětovný vstup A přepíše EXITA adresou uvnitř C. Bez samostatného
zásobníku či kopie se původní návrat ztratí. Konvence dočasných buněk
ze s.191–192 je správná v nerekurzivním grafu volání: všechny buňky
potomků mají nižší čísla než buňky aktuální rutiny; současně aktivní
řetězec si tedy nekoliduje. Sousední podprogramy mohou buňky sdílet,
neboť nejsou současně aktivní. Rady o návrhu, přepracování a ladění
jsou zkušenostní doporučení, nikoli univerzální výkonové záruky.

## Cvičení1–7 a odpovědi

**1 — checked.** Vstupy MAXN/MAX100 a výstupní kontrakt souhlasí
s(5), včetně rI3=0 a nezměněných ostatních registrů; n je určen
vstupní podmínkou. Sken jasně má n>=1, nikoli OCR n>1.

**2 — checked.** Náhradní MAX50 nejprve STJ uloží návrat, pak
nastaví50 a JMP2F už může J změnit. Jde o správnou alternativu(6).

**3 — confirmed: MAXIMUM-nonpositive-input.** Zadání na s.193 výslovně
žádá také stav při nekladném rI1. Odpověď527 zavádí n=1, pokud rI1<=0,
a tvrdí rI3=min(0,rI1). Žádná normalizace ale v ProgramuM není.
Označme q vstupní číselnou hodnotu rI1. Pro q<=0 se provede jediný
průchod: ENT3 nastaví q, ENT2 nastaví q, LDA načte X[q], DEC3
nastaví q-1 a J3P už neskočí. Pokud jsou adresa X+q a hodnota q-1
přípustné, správný výstup je tedy

```
rA = X[q], rI2 = q, rI3 = q-1,
rI1 unchanged, rJ = EXIT+1, CI unchanged.
```

Při nepřípustné adrese či přetečení indexového registru se výpočet
stává nedefinovaným; nelze tvrdit univerzální fallback na X[1].
Nejkratší rozlišení: q=0, X[0]=5,X[1]=7 dává(5,0,-1), kdežto
odpověď předpovídá(7,1,0) pro(rA,rI2,rI3). Případ je plně definován
pro každý povolený radix b. Odpověď pro q>=1 je správná: při q=1 se
neporovnává; jinak poslední CMPA proti X[1] dává greater, je-li konečné
maximum větší, equal, je-li stejné maximum i napravo, a less právě
tehdy, je-li jediné maximum v X[1]. EXIT JMP nastaví rJ=EXIT+1.

**4 — confirmed minor omission: SMAX1-unlisted-I1.** Pro kladné n,r
prochází algoritmus indexy n,n-r,...,a, kde a=1+(n-1)mod r. Stejný
invariant maxima platí nad tímto podseznamem. Poslední rI3 je a-r,
tedy(n-1)mod r+1-r=-((-n)mod r); formule odpovědi je správná.
Vstup SMAX1 ale začíná ENT1 1 a jeho vstupní podmínka původní I1
neomezuje. Pro n=1,rI1=2 tedy vrátí I1=1, aniž to výstupní podmínky
uvedou. Na s.188 je konvence výslovná: nezmíněné registry se nemění;
text právě rI1 používá jako příklad. Doplnit rI1=1 pro vstup SMAX1
(pro obecný SMAX zůstává rI1=r beze změny). Nejde o chybu nalezeného
maxima ani aritmetické formule.

**5 — checked.** Volací ENTA *+2 předá návrat v A. STA EXIT(0:2)
jej uloží, před vlastním hledáním se A stejně přepisuje prvním prvkem.
Návrat nečte J; změny J při skocích jsou pro tuto variantu irelevantní.
Ostatní účinky odpovídají MAX100.

**6 — checked with known erratum.** Oprava21.8.2001 přidává spotřebu
prostoru k povoleným odlišnostem oproti hardwarové instrukci. Pro
důkaz označme s původní efektivní adresu, d původní rI1 a f počet
kopírovaných slov z F. Routine si uloží rA,rI2 a návrat, přečte pole
adresy a indexu NOP do ENT A, a před jeho vykonáním obnoví rI2, takže
funguje také I=2. Efektivní s je spočteno ještě před změnou rI1,
takže funguje I=1. Po načtení -f do rI2:

- při f=0 se žádné datové slovo nekopíruje ani rI1 nemění;
- jinak se do adresních polí uloží s+f a d+f, rI1=d+f;
- před iterací k, 0<=k<f, je rI2=k-f, a načítá se aktuální paměť
  na s+k, která se ihned zapisuje na d+k.

Poslední bod je přesně vzestupné sekvenční kopírování MOVE, včetně
obou směrů překryvu; neporovnáváme s chybným modelem souběžné kopie.
Adresy s+f,d+f jsou nejvýše4000 při nenulovém přípustném kopírování,
tedy se vejdou i do dvou bajtů báze64. A a I2 se obnoví včetně
znamének nuly, ostatní registry kromě I1/J nejsou změněny. Žádný
příkaz nenastavuje CI a jediná aritmetika v A nepřetéká, takže se
zachová i přepínač přetečení. Návrat na NOP je správný; jeho indexovaná
adresa po změně I1 je stále přípustná (pro I=1 je s+f<=4000).

**7 — checked in stated practical context.** Čistý kód umožňuje
sdílené stránky a jednodušší cache/pipeline; nekontrolované změny kódu
mohou zneplatnit přednačtené instrukce a diagnostickou jump-trace.
Větu o nemožnosti více procesů vykládáme jako bezpečné současné použití
téže měněné kopie běžné rutiny bez další koordinace; samostatné kopie
a explicitní synchronizace samozřejmě mění předpoklady. Tento
pedagogický výčet není označen za nový technický nález.

## Errata, inventář a reprodukce

Z originálu193 je potvrzeno právě7 cvičení. Ve všech čtyřech vrstvách
není nové cvičení do§1.4.1; dodatky na527 patří ještě§1.3.3.
Prohledány all1-prepre,all1-pre,all1,err1 podle stran i výrazů
SMAX/MAXIMUM/MAX100/MOVE/subroutine/register/comparison a původní
err1.textxt. Přesné hity jsou v `../results/errata-search.json`.
Relevantní původní PDF strany all1-prepre16,17,39 a all1-pre11 byly
zobrazeny. Tři známé opravy do§1.4.1:186 'occupying less space'
(17.9.2005);190 EXITC(7.1.1999);193 čas **a prostor** v úloze6
(21.8.2001). Na527–528 není oprava obou výše uvedených nových rozporů.
Jde o absenci v těchto kontrolovaných vrstvách, ne o tvrzení prvenství.

`../check_subroutines.py` využívá společné modely beze změny. Výsledek
`../results/subroutines.json`:29 520 kontrol, včetně4592 případů MOVE
(každé F báze64 a100, každé I=0..6, čtyři druhy překryvu/vzdálenosti),
960 případů dvojího výstupu,240 parametrů stride a720 porovnávacích
stavů z úlohy3. Obecné důkazy výše jsou hlavní evidence; testy jsou
jen jejich nezávisle očekávané konečné doplnění. Úspěšný běh se bez
změny neopakuje.

Bibliografické a historické odkazy mají zvlášť vymezený rozsah čtení
v `sources.md`; tento audit netvrdí přečtení všech odkazovaných knih.
