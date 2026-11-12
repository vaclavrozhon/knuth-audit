# V2-C0014: oprava znamének v odpovědi 37 nedošla do dosazení

**Confirmed, 1. listopadu 2026.** §3.2.2-37, str. 558–559, první tisk
vydání 3 a veřejná errata. Jde o zbývající místo **téhož znaménkového
problému**, jehož dva jmenovatele opravil seznam dne 3. 2. 2005.
Nejde o novou chybu hlavního tvrzení o nadrovinách.

V odpovědi jsou s_j=q_(b_j), u_j=a*q_(b_j-1)/s_j a

```
t_j = a-a*q_(b_j+1)*q_(b_j-1)/s_j².
```

q_0=0, q_1=1, q_(n+1)=c*q_n+a*q_(n-1). Správný rozklad příslušné
iterace inverzního generátoru F(x)=c+a/x je

```
F^(b_j)(x) = q_(b_j+1)/s_j + t_j/(x+u_j).
```

Proto veřejné erratum správně mění dva jmenovatele na konci str. 558
z x-u_j na x+u_j. Navazující text na str. 559, řádek 3, však stále
po odstranění jmenovatelů dosazuje v bodech x=u_2,...,x=u_d.
Správně musí dosazovat **x=-u_2,...,x=-u_d**. Právě tyto kořeny
jednotlivých faktorů izolují příslušné koeficienty r_j*t_j.

Konkrétní příklad v povolené třídě: p=7,a=c=1 má plný cyklus

```
0, infinity, 1, 2, 5, 4, 3, 6.
```

Pro b_j=2 je u_j=1 a F²(x)=2-1/(x+1) modulo 7. Pól je 6=-1;
bod 1 uvedený jako dosazení v knize je regulární a F²(1)=5.
Při násobení výrazem x+1 tento faktor v bodě 1 nezmizí.
Nezpochybňujeme výsledek úlohy: [vlastní důkaz](inversive-generators.md)
se správnými zápornými póly potvrzuje celé tvrzení.

## Doklady a stav errat

- Vizuálně přečteny `images/vol2-p558.png`, `images/vol2-p559.png`
  a `images/all2-prepre-p31.png`; poslední je zdroj opravy 3. 2. 2005.
- Prohledány všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
  a aktuální TeX, stažené 1. 11. 2026. Hledány stránky 558/559, odpověď37,
  indexy u a inverzní generátory. Pro str. 559 není doplnění znamének;
  ostatní položky se týkají úlohy 38 a nové sekce 3.3.1.
- V nálezu výslovně rozlišujeme známou opravu dvou jmenovatelů od
  dosud neopravovaného navazujícího dosazení. Navržená oprava je
  rozšířením původního errata, nikoli opětovným hlášením jeho obsahu.
- `verify_inversive.py` / `results/inversive.json` ověřují ukázaný
  cyklus, polohu pólu i obecný rozklad ve 8414 případech; dále
  1201827 nenulových determinantů přímo iterovaných bodů.

Novější fyzický dotisk neověřen; digitální náhled odpovědi neobsahuje.
Draft `reports/C0014-inversive-pole-sign-draft.txt` je neodeslán.
Prvenství ani odměna se netvrdí.
