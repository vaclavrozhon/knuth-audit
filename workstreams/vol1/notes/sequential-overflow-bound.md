# §2.2.2-17: vyvrácení meze počtu přeplnění

Nález V1-C0034. Jde o neplatné tvrzení úlohy, nikoli pouze slabinu
nabídnutého důkazu. Autoritativní obrazy247,248,254,544 byly zobrazeny;
přesná definice OVERFLOW odpovídá označeným prvním vložením na obr.4,
i když se při přesouvání prázdných zásobníků nekopíruje žádné živé slovo.
Počet přeplnění tedy nelze v této úloze zaměnit za počet kopírovaných slov.

Kapacita j je BASE[j+1]−BASE[j]. Vezměme n=4, L0=0, L∞=4. První
inicializace má kapacity(0,0,0,4), druhá(1,1,1,1). Druhá je přímo
rovnoměrná inicializace(13), nikoli nějaké mimořádné povolení nulové oblasti.
Pro posloupnost I3 D3 I2 D2 I1 D1 I3 D3 I2 jsou po jednotlivých vloženích
kapacity prvního běhu postupně

```
(0,0,1,3), (0,1,0,3), (1,0,0,3), (1,0,1,2), (1,1,0,2).
```

Před každým vložením jsou všechny zásobníky prázdné a kapacita cílového
zásobníku nulová. Každé proto přeteče, a případ(a) na247 přesune nejbližší
pravou volnou buňku doleva. Pop vrátí TOP na BASE, ale dno nezmění.
První běh má pět přeplnění; druhý má nulu, protože každý zásobník má svou
jednu buňku a nikdy neobsahuje více než jeden prvek. Žádné podtečení,
plná společná paměť ani čtení nezapsaných dat se nevyskytne.

Nerovnost požadovaná úlohou se mění na5≤0+4. Tím je vyvrácena. Ve druhém
vložení do zásobníku3 se také vyvrací tvrzení odpovědi o nové rekordní
velikosti: znovu jde pouze o přechod0→1.

## Obecná rodina, nezávislý důkaz

Nechť n≥2, M=n. Označme P_j pár I_j D_j. Pro r=1,...,n−1 postupně
provedeme blok P_(n−1) P_(n−2) ... P_r. Před blokem r má první běh
jednu volnou buňku u každého zásobníku1,...,r−1, žádnou u zásobníků
r,...,n−1, a n−r+1 volných buněk u zásobníku n. V každém páru se
jedna buňka posune ze současného pravého souseda o jedno místo v této
řadě doleva; nový vrchol se následným popem uvolní. Po celém bloku je
jedna buňka navíc u zásobníku r a n−r jich zůstává u n. To indukcí
dokazuje invariant všech bloků a jedno přeplnění na každý pár.
Počet je (n−1)+(n−2)+...+1=n(n−1)/2. Rovnoměrná inicializace má stále0.
Pro n≥4 je rozdíl větší než M=n a jeho poměr k M není omezen konstantou.
Neodvozujeme tím žádnou náhradní horní mez pro obecné posloupnosti.

## Ověření a errata

`check_sequential_overflow_bound.py` porovnává nezávislý model kapacit
s doslovným modelem jednotlivých slov, BASE a TOP. Rozsah výsledků je
v samostatném JSON; obecný důkaz výše není konečným testem nahrazen.
Malý příklad lze celý ověřit z tabulky bez programu.

Čtyři vrstvy all1-prepre/all1-pre/all1/err1 i současný TeX byly prohledány
podle stran254/544, overflow, BASE, initial a tématu relokace. Jediná
přímo relevantní změna odpovědi17 je20.2.2009 less→more. Originál na
`images/sequential-errata-all1-prepre-p41.png` byl přečten. Tato změna
protipříklad neřeší; velikost1 stále nepřekračuje počáteční kapacitu1.
Oprava meze kopírování vlevo6.1.2011 není využita, protože všechny
naše přesuny berou volno zprava.

Zatím byl kontrolován digitální originál prvního dotisku, ne fyzický
výtisk. Netvrdíme prvenství a návrh nebyl nikam odeslán.
