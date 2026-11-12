# Kandidát: podmínka Wahidova obrácení bajtů připouští−0

**Stav:** doložený protipříklad, čeká na nezávislou kořenovou revizi;
globální ID nepřiděleno. Jde o chybu podmínky v nové odpovědi23
ze28.2.2018, nikoli o chybu původního Dixonova programu. Prvenství
nálezu ani fyzický výtisk se netvrdí.

## Přesné tvrzení a kontrakt

`all1-pre.pdf`, strana16, položka „Page509 new answer23“,28Feb2018,
uvádí „Second, by George Wahid, if rA >= 0:“ a tento program:

```
3000 ENT1 5:5
3001 SLA 1
3002 ST1 3003(4:4)
3003 ADD 200(*)
3004 DEC1 1:1
3005 J1P 3001
3006 HLT 0
```

Zápisy5:5 a1:1 mají číselné hodnoty45 a9. Před každým ADD se
jeho F přepíše na45,36,27,18,9, tedy na pole(5:5),...,(1:1).
Původní zadání na143 zobrazuje celé vstupní slovo(+,a,b,c,d,e)
a celé požadované slovo(+,e,d,c,b,a). Znaménko+ je výslovné.
Na rozdíl od úlohy22 proto nestačí jen číselná rovnost výsledku.

MIX na134 výslovně stanoví, že minus nula je rovna plus nule.
Na135 jsou podmínky „positive“ a „nonpositive“ popsány číselně,
nikoli jen jako test znaménkového bitu. Proto−0 splňuje rA>=0,
ale není slovem se znaménkem+.

## Úplný počáteční stav a obecný ruční průběh

Pro každý radix b mezi64 a100 zvolme

```
PC = 3000
A = (-,0,0,0,0,0)
mem[200] = (+,0,0,0,0,0)
I1=...=I6=-(b^2-1)
X=(-,b-1,b-1,b-1,b-1,b-1)
J=0, overflow=off, comparison=EQUAL
mem[3000..3006] = uvedený program
ostatní paměť = +0; žádné čekající I/O
```

Velké záporné indexy a X jsou pouze konkrétní volba; mimo I1
se nepoužijí a ENT1 hned I1 přepíše. Protipříklad na nich nezávisí.

Sémantické kroky jsou přímo v originálu:

- Strana135: žádný z posunů nemění znaménka A/X. SLA1 tedy nechá−0.
- Strana131: je-li součet v ADD nulový, znaménko A se nemění.
  Každé z pěti polí mem[200] je kladná nula, takže−0+0 dává−0.
- Pravidlo přetečení ADD na131 se zde neaktivuje: každý součet
  má velikost0, nikoli velikost alespoň b^5. Příznak zůstává off.
  Obecně má A po SLA1 velikost nejvýše b^5−b a přičítá se nejvýše
  b−1, takže ani v běžném Wahidově průchodu ADD nepřeteče.
- ST1, DEC1 a J1P nemění A. Poslední J1P při I1=0 neskáče.
- Strana136: HLT zastaví stroj; při opětovném spuštění má čistý
  účinek NOP. Žádnou normalizaci znaménka neprovádí.

Celá stopa tedy má27 instrukcí, přesně

```
ENT1;
(SLA,ST1,ADD,DEC1,J1P) pětkrát;
HLT.
```

| Průchod | I1 před SLA | F v ADD | A po SLA | A po ADD | I1 po DEC | Další PC po J1P |
|---|---:|---:|---|---|---:|---:|
| 1 | 45 | 45 | −0 | −0 | 36 | 3001 |
| 2 | 36 | 36 | −0 | −0 | 27 | 3001 |
| 3 | 27 | 27 | −0 | −0 | 18 | 3001 |
| 4 | 18 | 18 | −0 | −0 | 9 | 3001 |
| 5 | 9 | 9 | −0 | −0 | 0 | 3006 |

HLT na3006 ponechá A=−0 a PC=3007. Předepsané slovo je+0.
Oba výsledky se shodují ve všech pěti bajtech a liší se právě
znaménkovým bitem. K žádnému nedefinovanému přístupu ani přetečení
nedochází. Program zabere41u před HLT,42u s jeho jednotkovým časem.

## Nezávislá reprodukce a oprava

Ruční invariant výše platí pro všechny radixy. Nový cílený soubor
check_wahid_zero.py navíc ověřil148 případů: pro každý radix
protipříklad, kladnou nulovou kontrolu, nenulový vstup s A=−0
a variantu předem doplněnou o ENTA0. Přesně37 protipříkladů
vrátilo záporné znaménko; ostatní očekávané výsledky souhlasí.
Výstup je results/wahid-zero.json. Starý úspěšný MIX checker
se neopakoval; jeho původní Wahidovy případy začínaly kladným
A=b^5−1 a tuto hranici vůbec netestovaly.

Na žádost kořenové revize následoval jeden dodatečný běh při b=64
s úplnou27krokovou stopou všech instrukcí, nikoli opakování148
případů: trace_wahid_zero.py a results/wahid-zero-full-trace.json.
Stopa zachycuje i skutečná slova přepsaných ADD, příznak přetečení,
poslední J1P a HLT.

Nejmenší redakční oprava zachová sedm slov programu: změnit
podmínku na **„if rA has a plus sign“**. Pro libovolný původní
obsah A lze přidat ENTA0 na2999 a začít tam; podmínka pak není
potřeba, ale program zabere osm slov. Jeho globální prostorová
minimalita tím není dokázána. Nahrazení >= samotným > by také
odstranilo protipříklad, zbytečně by však vyloučilo správnou+0.

## Originály a všechny erratové vrstvy

Přímo zobrazeny tyto obrazy:

- images/vol1-file158-p143.png: přesné slovo se znaménkem+;
- images/vol1-file146-p131.png: nulový součet a přetečení ADD;
- images/vol1-file149-p134.png: −0 a+0 jsou číselně rovny;
- images/vol1-file150-p135.png: podmínky skoků a nezměněná znaménka posunů;
- images/vol1-file151-p136.png: HLT;
- parallel/errata-additions/images/all1-pre-16.png: celé erratum2018.

Cesty jsou relativní ke workstreams/vol1. Sken knihy je3.vydání,
1.dotisk1997; metadata a hash jsou v inventory/books.json.
Všechny101 originální strany čtyř erratových vrstev byly přečteny
v předchozím zmrazeném bloku errata-additions; nyní bylo obnoveno
také věcné hledání Wahid/Dixon/zero/ADD/SLA/HLT a stran131,134,
135,136,138,143,509.

| Vrstva | Relevantní položky | Vztah k protipříkladu |
|---|---|---|
| all1-prepre |143,19Jul1997: doplnění „ability“;509,1997/1999/2007: výkon a podmínky úlohy22; drobnosti131/134/135/138 | Neopravují podmínku ani znaménko výsledku23. |
| all1-pre |509,28Feb2018, PDF16: nový Wahidův program s rA>=0 | Vlastní chybná podmínka. |
| all1-pre |151,29Nov2011: „set to zero“ na „set to positive zero“ | Jiný program v MIXAL; není opravou23. |
| all1 |135,20Dec2023: rozsah instrukcí pro X a indexy; rejstříkové doplnění HLT | Beze změny příslušné sémantiky a odpovědi23. |
| err1 | Tytéž aktuální položky, bez změny odpovědi23 | Žádná pozdější oprava protipříkladu nalezena. |

Minimální návrh hlášení v ASCII je reports/wahid-negative-zero.txt.
