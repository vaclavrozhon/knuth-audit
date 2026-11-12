# V3-C0013 — zbytek v přesné hodnotě Mellinova integrálu

Confirmed, medium. Úloha §5.2.2-46 na s. 137 žádá hodnotu integrálu
J_s(n)=(1/(2πi))∫_(a−i∞)^(a+i∞) Γ(z)n^(s−z)/(2^(s−z)−1) dz,
s kladné celé, 0<a<s. Odpověď na s. 636 / file 647 uvádí pouze
P_s(n)=(s−1)!/ln 2 + δ_s(n). Chybí nenulový zbytek; jde o asymptotiku,
nikoli přesnou rovnost. δ_s(2n)=δ_s(n) podle vytištěné Fourierovy řady.

Nezávislý krátký důkaz: na integrační přímce rozvineme jmenovatel jako
Σ_(j≥1) 2^(−j(s−z)). Geometrická řada i integrál absolutně konvergují,
proto lze zaměnit součet a integrál. Mellinovou inverzí exp(−x) získáme
J_s(n)=Σ_(j≥1) (n/2^j)^s exp(−n/2^j), také správně uvedené v odpovědi 47.
Posun indexu dává J_s(2n)−J_s(n)=n^s exp(−n)>0 pro každé n>0.
Ale P_s(2n)−P_s(n)=0. Tištěná přesná hodnota tedy nemůže platit ani
pro všechna kladná celá n. Stačí s=1 a dvojice n=1,2.

Pro asymptotický výsledek stačí doplnit O(n^−A) pro libovolné pevné A.
Přesný zbytek je −Σ_(j≥0) (2^j n)^s exp(−2^j n): připojení této
chybějící poloviny dává oboustranný periodický součet P_s(n).
Zbytek je exponenciálně malý, ale nikdy nulový.

Sazba files 148 a 647 prohlédnuta. Pět vrstev errat v
sources/exchanging-errata-review.json. Známá oprava s. 636 z 5. 6. 2000
přidává zbytek v odpovědi 48, nikoli 46. Historická err3-1e, s. 134
(28. 2. 1978 a 23. 5. 1995), opravuje příbuzný vzorec hlavního textu
a upozorňuje na nenulovost jeho zbytku. Tento hlavní vzorec již druhé
vydání opravilo; odpověď 46 ponechává přesnou hodnotu bez zbytku.
Odpovídající lokální oprava 46 nenalezena. Prvenství/fyzický výtisk
neověřeny; související známé opravy nejsou nové nálezy.
