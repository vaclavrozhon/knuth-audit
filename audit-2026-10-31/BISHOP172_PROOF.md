# Úloha 172: obecný důkaz pro střelce

Odvozeno 3. 11. 2026 bez nového hledání cest. Pro sudé **n ≥ 4** je
největší délka indukované střelcové cesty na n×n rovna 2n−4. Každá
nejdelší cesta má právě jeden roh jako krajní bod. Z daného rohu je
2^(n−2) poloh a modulo symetrie celé desky 2^(n−3) tříd.

## Převod na diagonály

Na jedné barvě očíslujme součtové diagonály S_i: r+c=2i, 0≤i<n,
a rozdílové diagonály D_j: r−c=2j, −(n/2−1)≤j≤n/2−1.
Pole je hranou S_i D_j právě tehdy, když |j|≤min(i,n−1−i).
Střelcový graf je hranovým grafem tohoto bipartitního grafu H.
Indukovaná cesta s alespoň třemi poli odpovídá prosté cestě v H:
dvě sousední hrany se stýkají, ale žádné nesousední hrany nesmějí
sdílet vrchol. Její k hranám v H odpovídá k polí a délka k−1.

H má 2n−1 vrcholů; S_0 a S_(n−1) jsou listy se společným sousedem D_0.
Hamiltonovská cesta by oba listy musela spojit přes D_0 a nemohla
obsáhnout ostatní vrcholy. Proto má cesta nejvýše 2n−3 hran,
tedy střelcová cesta nejvýše 2n−4 kroků.

Při dosažení této meze chybí v H jediný vrchol. Musí být typu S:
vynechání D by dalo n vrcholů S a n−2 vrcholů D, což cesta nemůže mít.
Oba listy nelze použít současně, takže vynechaným vrcholem je jeden
z nich. Použitý list je krajním bodem. Na druhé barvě je argument
otočeným obrazem tohoto. Proto každá nejdelší střelcová cesta obsahuje
právě jeden roh, a to jako krajní bod.

## Počet a dosažení meze

Zafixujme roh (0,0), takže cesta v H začíná S_0,D_0 a vynechává S_(n−1).
Po odebrání S_0,D_0 zbývají páry

- A_i={S_i,S_(n−1−i)},
- B_i={D_i,D_−i}, pro 1≤i≤k=n/2−1.

Vrchol páru A_i sousedí právě s oběma vrcholy B_1,…,B_i. Hledaná
Hamiltonovská cesta ve zbytku začíná v A a končí v B.
Oba vrcholy A_1 mají jen dva sousedy B_1. Pokud žádný z nich není
počátkem, oba musejí mít v cestě stupeň dva: vytvořily by se čtyři
hrany izolovaného cyklu. Jeden vrchol A_1 je tedy počátkem. První
čtyři vrcholy jsou vynuceně

    jeden z A_1, jeden z B_1, druhý z A_1, druhý z B_1.

Pro tyto dva výběry jsou čtyři možnosti. Po odebrání bloku dostaneme
tutéž úlohu s k−1 páry; poslední vrchol odebraného B_1 sousedí se
všemi zbývajícími A. Pro k=1 jsou všechny čtyři možnosti možné.
Indukcí je počet cest 4^k=2^(n−2). Konstrukce zároveň dosahuje horní meze.

Jediný rohový konec dovoluje každou orbitu celé dihedrální grupy
ukotvit do (0,0), s jedinou zbývající symetrií: transpozicí. Ta žádnou
takovou cestu nefixuje. Automorfismus konečné cesty fixující jeden
konec totiž fixuje každý vrchol. Všechny buňky transpozičně pevné
cesty by pak ležely na hlavní diagonále a tvořily kliku, nikoli cestu
s alespoň třemi poli. Každá třída má tedy dvě ukotvené polohy a tříd
je 2^(n−3). Pro n=8 dostáváme 64 poloh a 32 tříd, v souladu s již
přijatým úplným výčtem; ten nebyl opakován.

## Cykly a malý okrajový případ

Pro indukované cykly délky alespoň čtyři platí stejný převod. Žádný
list nemůže být na cyklu H, takže zbývá nejvýše n−2 vrcholů S;
bipartitní cyklus má nejvýše 2n−4 hran. Pro n=8 dosahují přijatí
svědci délky 12. Samostatně je třeba vyloučit trojúhelníky hranového
grafu při formulaci obecného tvrzení; uvedenou mez pro n≥4 nepřevýší.

Kniha píše pouze „when n is even“. Pro n=2 dává 2^(n−3)=1/2, což
nemůže být počet tříd. Střelcový graf 2×2 jsou dvě disjunktní hrany;
nejdelší cesta má délku 1, nikoli 0. To je drobná otázka chybějícího
omezení n≥4; hlavní zadání se výslovně týká 8×8. Zatím není označena
za nový potvrzený nález. Starý kontrolní výčet malých desek začínal
na třech polích a pro tuto dvoupolovou cestu neslouží jako důkaz.
