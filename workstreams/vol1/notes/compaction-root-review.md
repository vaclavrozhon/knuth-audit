# Kořenová revize pěti nálezů ve správě paměti

1. listopadu 2026. Přímo přečteny původní strany452,455,607,
613,614,615,617. Přečteny čtyři reporty o kompakci/harmonické sumě,
report exact-fit, PROOFS-compaction a výsledky minimálních reprodukcí.
Všechny použité obrazy původních stránek jsou v aktivním bloku
parallel/dynamic-storage/images; stabilní reporty a reprodukce
se přebírají jednotlivě, celý blok tím zatím není dokončen.

**C0062:** Po posunu [2,4) do[1,3) je stará hlavička na2 nahrazena
datovým slovem. Čtení SIZE(2) po přesunu tedy není čtením délky
přesunutého uzlu. V minimálním příkladu se následně payload považuje
za další živou hlavičku a přepíše správný výsledek. Explicitní uložení
délky před přesunem problém řeší. MIX již právě toto dělá v I5;
nejde o jeho závadu. Pouhá poznámka o vzestupném kopírování v G9
nezajišťuje uchování SIZE na původní adrese.

**C0063:** Kontrakt455 výslovně dovoluje nulové linky. Úvod614
vyžaduje LINK(0) nenulové, zatímco řádky50–52 překládají i nulu.
Žádný mezikrok LINK(0) nenuluje. U jediného dvouslovného uzlu vzniká
ze NULL odkaz na kořen. Dodaný J6Z před LDA zachovává NULL; jeho
čas je započten zvlášť od opravy původního časového součtu.

**C0064:** Root samostatně sečetl vytištěné frekvence s MIX časy.
Sedm skupin dávají11a+8b+8,5,10a+3c+6,10,9c+8d,
11a+9b+6c+9 a12a+2w+6c+9. Součet je
44a+17b+2w+24c+8d+47, koeficient25c se v tisku skutečně nachází.
Příklady s c=1 a2 mají odchylku1 a2, takže ji nelze vysvětlit
konstantním volajícím skokem. Testovací HLT se nevykonává.

**C0065:** Vytištěný levý harmonický součet končí2m+1, pravý
střídavý součet2m−1. Pravý součet je H_(2m−1)−H_(m−1), protože
odečtení dvojnásobku sudých členů dává právě H_(m−1).
Levý proto musí končit2m−1. Při m=2 je rozpor77/60 versus5/6.
Oprava ponechává nerovnost vůči ln2 a výslednou first-fit mez.

**C0066:** Pool0,...,M−1 v odpovědi1 nevyhrazuje sentinel.
PřiděleníN slov z AVAIL končí na AVAIL+N−1, takže rovnost
AVAIL+N=M je přesný fit. Test selhání musí být ostrý >M.
Tisk >= je přímo viditelný na607; M=N=1,AVAIL=0 je platný
protipříklad. Zde nejsou zapotřebí další programové testy.

Všechny čtyři vrstvy errat prohledány po stránkách a s využitím
podrobného vyhledání podagenta také po termínech. Root přímo
prohlédl původní obrazy all1-prepre46–47, all1-pre18, all1-16,
err1-14. Opravy607 se týkají next-fit a značení předchozí sekce;
613 odpovědí28/32,614 pouze autorských iniciál. Pro615/617 není
odpovídající oprava. Výpis příslušných položek je uložen v
results/compaction-and-harmonic-errata.json. Živá errata byla
ověřena v této relaci; pozdější fyzický tisk ani historické
prvenství se netvrdí. Všech pět případů se potvrzuje v přesně
uvedeném rozsahu, nikoli jako stejně závažné závady.
