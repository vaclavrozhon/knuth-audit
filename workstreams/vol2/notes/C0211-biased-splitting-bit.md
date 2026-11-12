# V2-C0211: nezávislé bity nejsou přesně vyvážené

Stav: **confirmed** pro přesné tvrzení, nikoli pro asymptotickou cenu.
§4.6.2–29, poznámka na687; původní sazba zobrazena. Text předpokládá
pravděpodobnost1/2 nezávisle pro každý faktor a říká, že se tento
předpoklad stane rigorózním při rovnoměrné volbě t stupně <rd.

CRT zajišťuje nezávislost, ale při q=p^d je pravděpodobnost přítomnosti
faktoru v gcd(g,t^((q−1)/2)−1) rovna (q−1)/(2q). Nulový zbytek patří
do druhé třídy. Například p3,d1,r2 má bity pravděpodobnosti1/3,
úspěch rozdělení4/9 a očekávaně9/4 pokusů. Vyvážený model dává2.

Stačí doplnit vychýlení; knižní velké O platí dál. Vlastní důkaz ceny
v [equal-degree.md](equal-degree.md), §3, dokonce potřebuje pouze
nezávislost každé dvojice, a tedy stačí t stupně <2d.
Šest vrstev errat prohledáno4.11.2026; odpovídající oprava nenalezena.
Fyzický dotisk a prvenství neověřeny. Nic neodesláno.
