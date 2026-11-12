# V2-C0100: dva koeficienty v logaritmickém důkazu BBP identity

**confirmed**,2.11.2026. TAOCP2,3.vydání,1.dotisk1997,§4.3.1,
odpověď39,str.628, řádek začínající4S1-2S4-S5-S6 v odstavci Notes.
Původní [strana628](../images/vol2-p628.png) i její
[zvětšený výřez](../images/C0100-bbp-formula.png) vizuálně ověřeny.

Pro l_j=log(1-exp(πij/4)/sqrt2) tisk uvádí mezikrok

```
2l0 - (2-2i)2l1 + 2l4 + (2+2i)l7 = pi.
```

Jsou potřebné dvě opravy: odstranit nadbytečnou2 před l1 a nahradit
poslední plus znaménkem minus. Správně:

```
2l0 - (2-2i)l1 + 2l4 - (2+2i)l7 = pi.
```

Již hodnoty logaritmů uvedené v předchozích řádcích knihy dokazují chybu:
l0+l4=-ln2, l1=-(ln2)/2-iπ/4, l7=-(ln2)/2+iπ/4. Vytištěný výraz je
(π/2-ln2)(1+3i), nikoliπ. Opravený výraz jeπ. Filtr osmých kořenů jednotky
nezávisle dává správné koeficienty (2,-2+2i,0,0,2,0,0,-2-2i).
Viz [obecný důkaz](classical-bbp.md) a blok identities v
[výsledcích](../results/classical-bbp.json).

Samotná BBP řada i zbývající sedm konkrétních identit na této straně jsou
správné. Nejde o selhání algoritmu pro bityπ ani o volbu větve logaritmu.
Všechny uvedené argumenty logaritmů mají kladnou reálnou část; hodnoty
l1/l7 jsou navíc explicitně určeny samotnou knihou.

Čtyři vrstvy all2-prepre,all2-pre,all2,err2 a uložený současný TeX
prohledány2.11.2026 podle místa i obsahu. Dodatek30.9.2024 mění historickou
bibliografii, nikoli tyto koeficienty. Jinou opravu odpovědi39 jsme nenalezli.
Poslední fyzický dotisk, priorita a případná odměna neověřeny; hlášení neodesláno.
