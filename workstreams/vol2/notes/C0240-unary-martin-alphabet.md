# V2-C0240: Algoritmus X potřebuje větev pro jednoprvkovou abecedu

6. listopadu 2026, confirmed, nízká závažnost. Jde pouze o degenerovaný
okraj m=1, který zadání §3.2.2-17 výslovně připouští slovy „positive
integers“. Úloha 29 žádá výpočet právě této funkce. Algoritmus X v její
odpovědi na původní str. 557 pro tento okraj není definován.

Vezměme m=1, k=1, x₁=0. Martinova posloupnost z úlohy 17 je konstantní
nula a správná další cifra je 0. Krok X1 však nastaví (a₀,a₁)=(0,0).
Krok X2 požaduje nejmenší kladné i s aᵢ>0. Žádné takové i neexistuje.
Stejně pro libovolné k≥1 dostaneme po X1 vektor samých nul.

Stačí před X2 doplnit „jestliže m=1, vrať 0“, případně celý algoritmus
výslovně omezit na m≥2 a triviální případ vyřešit zvlášť. Pro m≥2
existenci indexu v X2 zajišťuje sentinel aₖ=m−1>0. Nezpochybňujeme
Martinovu konstrukci ani správnost algoritmu pro netriviální abecedy.

Původní strany 38,40,557 byly vizuálně přečteny. Prohledány všechny
vrstvy all2-prepre, all2-pre, all2, err2 a aktuální err2.textxt; poslední
ověření aktuálnosti souborů 6. listopadu 2026 v 05:47 UTC. U odpovědi 29
je jen výměna bibliografického odkazu z 29. července 2006. Doplnění
větve m=1 nebylo nalezeno. Novější fyzický tisk ani prvenství neověřeny.

Předchozí audit tuto výjimku rozpoznal a přidal ji do vlastního programu
`verify_complete_sequences.py`, ale samostatný nález neevidoval. Jeho
úspěšné testy pro m=1 proto ověřují doplněnou verzi. Souvislý průchod
nyní rozdíl mezi tištěným algoritmem a doplněným modelem výslovně eviduje.
Článek Amram et al. (2019), str.227, sám omezuje netriviální výklad na
abecedu velikosti alespoň 2; nemůže tento okraj tištěného algoritmu uzavřít.

Důkaz je uvedený dvoukrokový průchod, nikoli dlouhý výčet. Přesný malý
záznam je v `results/sequential-other-methods-review.json`. Žádný nový
emailový návrh nevznikl.
