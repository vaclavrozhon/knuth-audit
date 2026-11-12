# V3-C0019 — příliš silný odhad ocasu v opravě z roku2006

Potvrzený matematický rozpor v aktualizovaném znění, nízký dopad.
Cílem je **oprava** all3-prepre, PDF/souborová7, položka pro s.64,
„line2 above(52)“, datovaná1.1.2006. První dotisk knihy s.64/file75
obsahuje slabší, tímto příkladem nevyvrácený odhad. Není to opětovné
hlášení již opravené chyby: právě nová pravá strana opravy je vadná.

Původní sazba a oprava byly zobrazeny v
images/tableaux-file-075.png a images/tableaux-errata-tail-bound-file007.png.
Oprava mění O(exp(−2n^ε)) na O(exp(−2n^(2ε))) při nahrazení
mezí α,β v pravé straně Eulerova součtového vzorce(50) nekonečny.
Text říká „in each term“. Stačí proto zkontrolovat **integrální
člen** pro výslovně povolené t=0, nikoli zaměnit integrál za
diskrétní součet nebo sečíst chyby různých členů.

## Přesný kontext a důkaz

Z(45) se sčítají x na jednotkové posunuté mřížce v intervalu
[−A_n,A_n], A_n=n^(1/4+ε), kde je například ε=0.001. V(50) tedy
α_n=−A_n+O(1) a β_n=A_n+O(1), s β_n první vyloučenou horní
mřížkovou hodnotou. Pro t=0 je f_n(x)=exp(−2x²/sqrt(n)).
Změna integrálního členu je kladné číslo

    D_n = ∫_(-∞)^α_n f_n(x)dx + ∫_β_n^∞ f_n(x)dx.

Položme J(b)=∫_b^∞ exp(−2y²)dy, b>0. Integrace po částech dává

    J(b)=exp(−2b²)/(4b) − (1/4)∫_b^∞ exp(−2y²)/y² dy.

Poslední integrál je mezi0 a J(b)/b², tedy

    exp(−2b²)/(4b(1+1/(4b²))) ≤ J(b) ≤ exp(−2b²)/(4b).

Odtud J(b)~exp(−2b²)/(4b), bez použití numerického odhadu. Po změně
x=n^(1/4)y je pravý integrální ocas

    ∫_β_n^∞ f_n(x)dx
      ~ (1/4)n^(1/4−ε) exp(−2n^(2ε)).

Zaokrouhlení β_n o O(1) zde nemění ekvivalenci: b=β_n/n^(1/4)
=n^ε+O(n^(−1/4)), takže b²−n^(2ε)=O(n^(ε−1/4))→0 pro pevné
0<ε<1/4. Levý ocas má stejnou ekvivalenci. Proto

    D_n ~ (1/2)n^(1/4−ε) exp(−2n^(2ε)).

Jeho poměr k opravenému O-měřítku diverguje. Už jediný pravý ocas
stačí k vyvrácení odhadu; faktor1/2 se týká až součtu obou ocasů.

Je-li požadována úplně konkrétní celočíselná rodina, vezměme knižní
ε=1/1000 a n=m^1000 pro celá m→∞. Potom posun
(n−sqrt(n))/2 je celé číslo, A_n=m^251 je také celé číslo,
α_n=−m^251 a β_n=m^251+1. Jediný pravý ocas má ekvivalent
(1/4)m^249 exp(−2m²), zatímco oprava požaduje O(exp(−2m²)).
Žádné členy této obrovské rodiny nebyly počítány nebo enumerovány.

## Oprava a rozsah dopadu

Pro každý pevný mocninný faktor a pevný řád derivace jsou jednotlivé
okrajové a ocasové členy nejvýše polynom v n krát exp(−2n^(2ε)).
Stačí tedy například napsat **O(exp(−n^(2ε)))**, anebo přiznat
polynomiální faktor O(n^C exp(−2n^(2ε))). Také původní slabší
O(exp(−2n^ε)) polynomiální faktor absorbuje.

Všechny tyto opravené varianty jsou menší než libovolná záporná
mocnina n. Chyba proto nevyvrací součtový závěr(52) ani finální
asymptotiku(53); týká se přesně uvedené příliš ostré pomocné meze.
Závažnost low odpovídá tomuto dopadu.

## Vrstvy errat

Prověřeny všechny místní relevantní vrstvy aktualizované9.6.2026:
all3-prepre obsahuje právě spornou změnu2006 a žádnou její opravu;
all3-pre nemá další relevantní změnu; all3 a err3 přidávají na64
pouze bibliografickou poznámku2024 o dalších koeficientech. Historická
err3-1e na odpovídající s.67 zavádí v roce1978 původní slabý odhad
O(exp(−2n^ε)), nikoli opravený silný odhad. Relevantní znění,
lokace a vyhledání jsou v sources/tableaux-tail-bound-errata-review.json.
Fyzický výtisk a prvenství nálezu neověřeny; dokazován je místní
aktuální zdroj a jeho přesný matematický rozpor.
