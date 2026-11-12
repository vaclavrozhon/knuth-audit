# Kořenová revize §2.2.4 a nových nálezů C0036–C0038

Celé NOTES.md kruhových seznamů bylo přečteno včetně obecného průchodu
A/M, případů sdílení vstupů, paměťové bilance, MIX časů a obousměrného
kódování odkazů. Zdrojový přepis kandidátů a kontrolní program byly
přečteny; úspěšné výpočty bez nové pochybnosti znovu neběžely.

## C0037: nulování sdíleného zdroje

Kořen znovu zobrazil276,277,279 a552. Zadání výslovně požaduje případ
P=Q; odpověď mu přisuzuje součin faktorů bez výjimky konstanty−1 v M.
Pro P=Q=1,M=−1 není potřeba žádná nová paměť. Jediný term se zruší,
A4 vrátí jeho uzel doAVAIL a poté načte právě přepsaný LINK přes P.
Při původně prázdnémAVAIL dostane null. Opravené pořadí přiřazení Q
z roku2022 tomu nezabrání. Jde o potvrzenou chybějící výjimku, analogickou
výjimce pro jiný případ M=Q, kterou odpověď správně uvádí. Reprodukce
ukazuje konkrétní porušení reprezentace a pozdější HLT, nikoli timeout.

## C0038: koeficienty časového vzorce

Původní553 zobrazen. Z přesného výrazu odečteného ze stránky vzniká
koeficient pr roven21+18=39 a koeficient alpha*pr roven−18+27−4=5.
Tištěných40 a4 tedy není možné dostat z uvedených součtů. Konkrétní
P=x+1,Q=x,M=1 splňuje0<alpha<1 přesně s alpha=1/2: původní vzorec
42+38+29+18+27=154, tištěná simplifikace4+80+4+38+29=155.
Přesný MIX běh souhlasí s154. Potvrzená algebraická chyba v odpovědi16;
první přesný časový vzorec je správný.

## C0036: nadbytečná exponenciála v erratu2018

Samostatně zobrazen celý all1-pre PDF16, detail vzorce a primární
Brightwell–Tetali Theorem1.3 na souborové3. Dosazení k=n+1 vrstev
 a2^n prvků dává přesně B_n bez exp. Výpočet r přes binomickou identitu
souhlasí. Důkaz agenta pro všechna n≥1 i celočíselně podložené srovnání
při n=16 byly nezávisle algebraicky přepočteny. Chyba je ve tvrzeném
zlepšení a reprodukci věty, nikoli v pravdivosti samotné velmi slabé
horní meze exp(B_n). Potvrzení neříká nic o fyzicky ověřeném dotisku.

## Rozsah technického převzetí

Původní inventář18 úloh a náhrada4 z2021 jsou rozlišené. Vlastní
COPY2/ZERO2/ERASE2/MULT2 mají skutečný MIX kód a oddělené časové
konstanty. Obecný argument pro původní COPY i ZERO zahrnuje nulový
polynom; ERASE má v tomto modelu stále hlavu a není voláno s null.
U dělených a sdílených cyklů jsou v poznámce výslovné potřebné
předpoklady. XOR i modulární součet/rozdíl mají algebraickou inverzi,
nejde pouze o konečný test.

Historické použití triků bez předchůdce dokládá primární IPL-V manuál
na46–47. Atribuce Xie je výslovně doložena Knuthovým publikovaným
erratem; není vyžadován neexistující citovaný článek. Kniha sama
přiznává neznámý původ obousměrného kódování, takže se jeho určení
nepovažuje za nedokončený matematický důkaz. Odkaz na jiné dílo
neznačí audit celé související kapitoly svazku3.
