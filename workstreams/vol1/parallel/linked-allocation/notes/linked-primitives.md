# §2.2.3: alokace a základní operace se seznamy

## Rozsah a model

Původní obrazy s. 254–261, 268–269, 273 a odpovědí 545–546,
551 byly přečteny. K hlavnímu textu patří rovnice (1)–(17),
obrázky 4–5 a příklady vložení/odebrání. Zde pokrýváme úlohy
1–8, 29 a obě formulace úlohy 30. Programové běhy jsou doplňkem
následujících obecných invariantů.

Uzel je přidělitelná buňka pevné velikosti c. `LINK(p)` je odkaz
z uzlu p, `INFO(p)` jeho data a `Λ` nulový odkaz. Platný seznam
je konečný řetězec různých uzlů zakončený Λ. Zásobník volných
uzlů má hlavu AVAIL; jeho uzly se nesmějí překrývat s uzly
živých seznamů. V části o MIX je Λ=0, adresy jsou kladné,
INFO=(0:3), LINK=(4:5), a řídicí proměnné T, AVAIL apod.
zabírají samostatná slova, jako v programech (10)–(11).
Tato reprezentace nevyžaduje, aby `INFO` obsahovalo adresu.

## Alokátor (4)–(7)

Je-li AVAIL=p≠Λ a LINK(p)=q, odebrání první volné buňky
nastaví AVAIL=q a vrátí p. Právě p zmizí z množiny volných
uzlů. Vrácení nezávislého přiděleného p uloží do LINK(p)
dřívější AVAIL a nastaví AVAIL=p. Obě operace zachovávají
rozklad zásobníku na hlavu a zbytek; vracení nesmí být provedeno
dvakrát pro tutéž živou buňku. Prázdná volná zásoba vyvolá
OVERFLOW. To je také celá odpověď úlohy 1: zkratka alokace
již obsahuje podmínku (6).

U postupně rostoucího poolu je POOLMAX první nepoužité místo.
Jeho dosud zprovozněná oblast je [L0,POOLMAX), rozdělená na
uzly délky c. Nový uzel [POOLMAX,POOLMAX+c) je disjunktní
s dřívějšími uzly. Podmínka POOLMAX+c≤SEQMIN je přesně
nepřekrytí se sekvenční tabulkou začínající na SEQMIN.
Nejprve se využívají uvolněné uzly; pool se zvětší pouze při
prázdné AVAIL zásobě. POOLMAX se nezmenšuje, takže výrok o
nejmenším poolu znamená tento způsob růstu, nikoli globální
kompakci živých objektů.

## Zásobník (8)–(11), úlohy 2–4

Po přidělení p nastavíme INFO(p)=Y a LINK(p)=T. Změna T=p
připojí nový první uzel a nezmění pořadí starých uzlů. Při
odebrání si před vrácením p=T uložíme LINK(p) do T a INFO(p)
do Y. Teprve potom smí být LINK(p) přepsán odkazem AVAIL.
Prázdný T vede do UNDERFLOW bez čtení uzlu 0. Vložení
cyklicky přenese tři původní odkazy (AVAIL, LINK(p), T),
odebrání provede opačný cyklus. Obrázky souhlasí.

MIX (10) i (11) jsou doslovná implementace; osm paměťových
operací po 2u a jeden podmíněný skok po 1u dávají 17u.
Známé erratum z 13. 8. 1997 nahrazuje nesprávnou jednotku
`cycles` za `units of time`; hodnota 17 se nemění.

V INSERT se rJ po volání rovná adrese řádku NOP T. Dvě STJ
uloží tuto adresu do instrukcí, které pak přečtou adresní pole
NOP a provedou návrat. rI1 je nový uzel, rI3 adresa T a rI2
původní T. rA, rI4–rI6 a rX se nemění. Návrat na NOP je
povolen: NOP pouze projde k další instrukci. Při přetečení
řešitel vrací řízení na znovunačtení AVAIL.

V DELETE je rI2 adresa T a rI3 původní T. Při prázdném
zásobníku zůstane rI3=0 a návrat skočí na NOP; následný JMP
UNDERFLOW je první výstup. Při úspěchu rI1 dostane nový T,
rA vyjmutá data a rI3=2 posune návrat za obě volací pomocné
instrukce. Komentář na s. 545 má známou opravu INFO(rI1)
na INFO(rI3), 23. 4. 2019; instrukce byla správná už v tisku.

Obsluha úlohy 4 před použitím rI1 uloží celý jeho obsah včetně
znaménka do adresního pole budoucí ENT1. Uloží také původní
rJ. Zprovozní jeden uzel v POOLMAX, zvětší hranici o c,
ověří nepřekrytí a vynuluje LINK nového uzlu. Před návratem
vypočte původní rJ−2 a uloží je do posledního skoku; pak
obnoví rI1. Žádný jiný datový registr ani přepínač přetečení
se nemění, srovnávací indikátor se změnit smí. Výstup TOOBAD
je nevratné hlášení skutečně vyčerpané paměti, nikoli návrat
s porušeným pool invariantem.

## Fronta (12)–(17), úlohy 5 a 6

Neprázdná fronta má F na prvním a R na posledním uzlu,
LINK(R)=Λ. Prázdná má F=Λ, R=LOC(F); uložení F v poli LINK
je zde výslovnou součástí reprezentace. Vložení za R tak
v prázdném případě zapíše první uzel přímo do F. Odebrání
uloží nový F před vrácením starého uzlu a při vyprázdnění
obnoví R=LOC(F). Jednoprvkový případ proto funguje.

Vložení na začátek (úloha 5) nastaví LINK(p)=F a F=p;
pouze byl-li starý F=Λ, musí rovněž změnit R=p. Při odebrání
zezadu se od fiktivního předchůdce LOC(F) hledá p s LINK(p)=R.
Po vyjmutí starého R nastavíme R=p a LINK(p)=Λ. Pro jediný
uzel je p=LOC(F), takže poslední přiřazení právě vynuluje F.
Vyhledání skutečného předchůdce je při této reprezentaci
v nejhorším případě lineární: žádná informace o zpětném
odkazu není u R uložena.

V úloze 6 nemusí být LINK(R) smysluplný. Před čtením odkazu
odebíraného uzlu proto testujeme staré F=R. Pokud ano, vytvoříme
prázdnou frontu přímo; jinak načteme LINK(F). Tento test musí
být před vrácením uzlu do AVAIL, které jeho LINK přepíše.
Knižní náhrada příkazů to umožňuje a pořadí zbylých úkonů
nemění. Poznámka o garbage collection je omezením dané
konvence rozpoznávání odkazů, nikoli tvrzením, že všechny
možné kolektory musí slepě procházet všechny bity LINK.

## Obrácení a vymazání, úlohy 7, 8, 29

Po i průchodech obracení ukazuje Q na obrácených prvních i
uzlů původního seznamu; P ukazuje na nedotčený zbytek.
Oba řetězce jsou disjunktní a jejich sjednocení jsou přesně
původní uzly. Krok zachrání staré Q do R, přesune první uzel
z P do Q, před přepsáním zachrání jeho následníka a nastaví
LINK(Q)=R. Velikost zbytku klesne o jednu, tedy postup skončí
včetně n=0. MIX odpověď 8 má tři inicializační instrukce
za 4u, n iterací po 7u a závěrečné ST2 za 2u: (7n+6)u.

Zlepšení na 5n+O(1) skutečně existuje. Přímá varianta je třícestné
rozvinutí, které střídá tři indexové registry v rolích aktuálního uzlu,
hlavy obrácené části a následujícího uzlu:

```
LD1 FIRST; ENT2 0; J1Z END2
A: LD3 0,1(LINK); ST2 0,1(LINK); J3Z END1
B: LD2 0,3(LINK); ST1 0,3(LINK); J2Z END3
C: LD1 0,2(LINK); ST3 0,2(LINK); J1NZ A
END2: ST2 FIRST; JMP DONE
END1: ST1 FIRST; JMP DONE
END3: ST3 FIRST
DONE:
```

Každý zpracovaný uzel stojí jednu dvojici load/store a jeden
skok, tedy 5u; inicializace a odpovídající konec jsou konstantní.
V každém ze tří míst lze přímo dosadit invariant P/Q a ověřit
stejný krok jako v abstraktní verzi.

Pro vymazání celé hlavy FIRST najdeme poslední uzel p,
nastavíme LINK(p)=AVAIL a AVAIL=FIRST. Získáme právě spojení
obou původních disjunktních řetězců. Prázdná hlava se nesmí
předat jako uzel. Pokud se proměnná FIRST dál považuje za
živý seznam, musí být resetována na Λ; kniha to výslovně
uvádí jako závislost na dalším použití. Při známém R se hledání
vynechá a operace fronty je konstantní. Pokud známe pouze
FIRST, je lineární průchod nutný v ukazatelovém modelu:
dokud nebyl načten konec, nerozlišíme dosavadní řetězec od
řetězce s dalším uzlem, který je také nutné vrátit.

## Obě úlohy 30

Původní varianta 1997 dovoluje nedefinované R při F=Λ.
Vložení tento případ otestuje a nastaví F=p namísto zápisu
LINK(R). Nakonec vždy R=p. Odebrání je zásobníkové odebrání
z F; zastaralé R se ve stavu F=Λ nikdy nečte.

Nová varianta z 17. 8. 2021 má za posledními daty přidělený
prázdný uzel R; fronta tedy vlastní jeden uzel i při F=R.
Vložení zapíše data do starého prázdného R, připojí nový
prázdný p a přesune R=p. Odebrání je dovoleno právě při F≠R,
uloží jeho data a následníka a vrátí starý F do AVAIL.
Nový R nemůže být vrácen omylem: při posledním odebrání se
F přesune na R. Oba invarianty i tvrzení o efektivnějších
základních operacích jsou správné; cena je jeden rezervní uzel.
