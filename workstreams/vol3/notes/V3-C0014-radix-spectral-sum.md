# V3-C0014 — definice spektrálního součtu pro radix exchange

Confirmed, medium. Odpověď §5.2.2-53, s. 637–638 / files 648–649,
definuje δ(n)=Σ Γ(z)n^(−1−z)/h_p pro kořeny p^(−z)+q^(−z)=1,
z≠1. Definice zahrnuje pól a má navíc nesprávnou normalizaci.

Pro všechna 0<p<1, q=1−p je z=−1 kořenem. Vytištěné z≠1 jej
nevyloučí, avšak Γ(−1) není konečné číslo. Musí být vyloučeno z=−1,
jehož dvojnásobný pól již vytvořil hlavní n ln n člen na předchozí straně.

Ani samotná oprava znaménka nestačí. V povoleném případě p=q=1/2
jsou ostatní kořeny z_k=−1+2πik/ln 2, k≠0. Pro D(z)=1−2^(1+z)
platí D′(z_k)=−ln 2. Integrand na s. 637 má v z_k reziduum
−Γ(z_k)n^(−z_k)/ln 2; při posunu kontury doprava se reziduum odečítá.
Oscilující příspěvek k T_n je tedy (n/ln 2)Σ_(k≠0)Γ(z_k)n^(−1−z_k).
Protože hlavní vzorec už vytýká n/h_p=n/ln 2, správné δ v tomto
případě nemá další dělení h_p. Tisk dává o faktor 1/ln 2 jinou amplitudu.
Nenulový Fourierův koeficient Γ(z_1) ukazuje, že rozdíl nelze pohltit O(1).

Obecně je příspěvek jednoduchého kořene do δ roven
−h_p Γ(z)n^(−1−z)/(p^(−z)ln p+q^(−z)ln q), nikoli Γ(z)n^(−1−z)/h_p.
Tím netvrdíme úplné vyřešení konvergence či geometrie všech kořenů;
protipříklad p=q=1/2 obě vady rozhoduje bez tohoto zobecnění.

Sazba files 648–649 prohlédnuta. Všech pět vrstev errat v
sources/exchanging-errata-review.json. Známá oprava odpovědi 53 na
s. 637 (15. 8. 1999) mění index x_n na x_k v úvodní rekurenci;
spektrálního součtu na s. 638 se netýká. Odpovídající oprava nenalezena.
Prvenství/fyzický výtisk neověřeny.
