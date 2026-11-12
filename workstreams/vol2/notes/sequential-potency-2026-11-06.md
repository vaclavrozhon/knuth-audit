# Souvislý průchod §3.2.1.3: potence

6. listopadu 2026, V2-X0089–X0090. Původní str. 23–26 a odpovědi
550–551 přečteny proti `potency.md`, `C0006-quantized-equality.md`
a všem čtyřem řadám errat. Inventář: osm úloh, žádná přidaná.
Strany 23 a 550 jsou nyní celé zkontrolované; na 26 a 551 zbývá §3.2.2.

## Matematická kontrola

Potence s je nejmenší kladný exponent s (a−1)^s≡0 modulo m. Při
plné periodě existuje. Binomický rozvoj geometrického součtu dává
X_n=c Σ binom(n,j+1)b^j modulo m; vyšší mocniny b mizí. Pro b=0
je třeba použít přímo X_n=cn, nikoli dosazovat do dělení 0/0.

Pro potenci 2 druhá diference odpovídá cb modulo m. Meze
−2(m−1)≤x−2y+z≤2(m−1) potvrzují čtyři uvedené možné roviny.
Není tím řečeno, že se každá nutně obsadí. Výpočty potencí pro m=2^35,
obě hodnoty 18 z úlohy 3 a obecné maximum ceil(e/2) souhlasí.

Instrukční posloupnost MIX skutečně násobí B²+1 modulo B⁵ a přidává
1; potence je 3 a časování 7u proti 16u souhlasí s modelem MIX.
Obecná formule max ceil(e_i/f_i), oba vhodné moduly 2^27+1 a 10^9−1
z tabulky a konečná geometrická řada pro inverzi a jsou správné.
Vysoká potence sama negarantuje statistickou kvalitu. Experimentální
doporučení „alespoň 5“ není zde přetvořeno v univerzální větu.

U úlohy 8 lichost X_n dává přesný vztah
X_(n+2)≡2^34+6X_(n+1)−9X_n modulo 2^35. Pro dvacet intervalů
je po doplnění podlahy možných nejvýše 15 třetích hodnot při pevné
první dvojici. Alespoň 2000 z 8000 buněk proto musí zůstat prázdných;
není třeba nový milionový experiment. Rovněž následná relace pro
násobitel 2^33+2^18+5 má konstantní pravou stranu (a−9)c, protože
(a−5)^2 je násobkem modulu.

Celý `verify_potency.py` přečten. Uložené výsledky přijaty bez restartu:
165 791 modelovaných instrukčních přechodů, 341 potencí a inverzí,
151 335 binomických hodnot, 47 926 kontrol rovin. Archivovaný milion
trojic má přesně 2000 prázdných buněk; původní slabší desetinná varianta
má všechny buňky obsazené, počty 12–51. Dodatek z roku 2004 mění
experiment, nikoli nepravdivou algebraickou větu původního zadání.

## C0006 je pouze chyba pozdějšího errata

Původní odpověď na 551 má přibližnou rovnost. Oprava 2004 přechází
na dvacet intervalů, stále s aproximací. Teprve oprava 14. 5. 2016
mění znak na přesnou rovnost bez potřebné podlahy. Přímé obrazy
`all2-prepre-p04.png`, `all2-prepre-p31-direct.png` a
`all2-pre-p13-direct.png` potvrzují tuto posloupnost.

Znovu přijat přesný protipříklad n=75: stavy
12020024059, 27570145521, 5701049043 dávají intervaly (6,16,3).
Rovnost by vyžadovala 6ε₁−9ε₂≡11 modulo 20, ale tento rozdíl je
v otevřeném intervalu (−9,6). Nevyhoví ani libovolná povolená ε.
Podlaha rovnici opravuje. Index n+1 v položce 2016 se navíc liší
od n+2 v předchozím vzorci; tento rozdíl nezachraňuje chybějící podlahu.

UI nyní vede C0006 jako `errata`, původní 551 jen jako související
stránku. Nález není důvodem červené značky původního tisku na 551.
**X0090** samostatně mapuje zveřejněné upřesnění kladnosti s a
nadbytečnou tečku na původní 24. Nový nález v průchodu nepřibyl.

## Přeskočené zdroje

Rychlé vyhledání na webu ACM neposkytlo přímo cílové články
MacLarena–Marsaglii (JACM 12,83–89) a Greenbergera (CACM 8,177–179).
Jejich plný obsah a historické prvenství zůstávají přeskočeny; odkazy
v jiných článcích nejsou vydávány za přečtený primární doklad.
Totéž platí pro blíže neurčené rané experimenty o hranici potence 5.
Vlastní algebraické tvrzení a konkrétní experiment mají uvedené důkazy.

Další kurzor: §3.2.2, původní str. 26 a odpovědi 551.
