# V1-X0768: Barnes, Watson a obecná verze lemmatu

Celá úloha §1.2.11.3–19 je checked. Nově doložené původní citace
doplňují již přijatý obecný důkaz v `asymptotic-gamma.md`.
Nevzniká nový nález a úspěšné matematické testy se neopakovaly.

## Přímá kontrola a meze četby

Root ověřil všech 39 souborů a 10 vnějších závislostí zmrazeného
`parallel/asymptotic-primary-followup/results/barnes-watson-ex19-manifest.json`
(SHA-256 `4247c52d768007fa3778598bd79afcc2fec63f796cb20d96ee3dcbd7581ef935`).
Devět společných vstupů knihy a všech čtyř vrstev errat určuje
`results/readonly-inputs.json` téhož paketu; byly hashově ověřeny.

Přímo zobrazeny Barnesovy tištěné 249, 254–255 a část 256 před
začátkem Part I: titul článku a rozhodující §5. Agent navíc četl
celých 249–256. Z Watsonova původního svazku root zobrazil titul
PDF 5, začátek článku 116 (PDF 170), celé lemma s důkazem 133
(PDF 187) a konec článku 148 (PDF 204). Agentův širší přesný rozsah
je v `notes/barnes-watson-ex19.md`; ostatní aplikace nejsou pokládány
za zkontrolované. Titul má 1918, i když článek byl přednesen 1916;
závěrečný dodatek je datován 15. června 1918. Barnesův tisk uvádí
29. června 1906. Citované roky i rozsahy stran souhlasí.

Root znovu přímo přečetl TAOCP 123 a 507 a původní errata
all1-prepre 36 a all1-pre 16. Hledání všech čtyř úplných vrstev
je uchováno v paketu. Žádná relevantní oprava úlohy 19 nalezena
nebyla; známé doplnění faktoru k v sousední odpovědi 20 z 1.1.2006
se této úlohy netýká.

## Matematické porovnání

Barnesův integrál kolem řezu kladné poloosy má při jeho analytických
předpokladech rozvoj

```text
I(x) ~ sum_(j>=0) c_j / (Gamma(1-beta-j) x^(beta+j)),
f(z) = sum_(j>=0) c_j(-z)^j.
```

Zde Gamma je gama funkce, beta parametr mocniny a c_j koeficienty
lokální řady f. Pro necelé beta>0 a reálné x>0 lze konturu stáhnout:
`I(x)=sin(pi beta)/pi * integral_0^infty exp(-xt) f(t)t^(beta-1)dt`.
Odrazová formule gama funkce převádí koeficient na
`(-1)^j sin(pi beta) Gamma(beta+j)/pi`, tedy přesně na integraci
jednotlivých členů reálné řady. Tím je doložena konkrétní návaznost;
nepřenášíme všechny komplexní obory platnosti Barnesova článku.

Watson na 133 předpokládá konvergentní lokální řadu v mocninách
`t^(1/r)` a exponenciální omezení mimo nulu. Pro komplexní n
v pevném sektoru uvnitř pravé poloroviny dostává po M−1 členech
zbytek omezený `K Gamma(M/r)/(Re(n)-b)^(M/r)`; r>0 je krok
zlomkových mocnin, b a K vhodné konstanty. To je obsahový původ
metody, nikoli doslovně nejširší formulace úlohy v TAOCP.

Kniha žádá jen `f(t)=O(t^alpha)` u nuly, alpha>−1, a existenci
Laplaceova integrálu pro dost velké n. Root znovu prošel již
přijatý důkaz: zvolíme N s existujícím integrálem, r>0 uvnitř
lokálního odhadu a `F(t)=integral_r^t exp(-Nu)f(u)du`.
Existence nevlastního integrálu dává konečné K se `|F(t)|<=K`.
Integrace per partes pak pro n>N omezuje ocas hodnotou
`K exp(-(n-N)r)`. Lokální část je nejvýše
`M Gamma(alpha+1)n^(-alpha-1)`, kde M je konstanta lokálního odhadu.
Argument tedy zachovává i podmíněnou konvergenci; analytické
předpoklady starších článků nejsou nepozorovaně přidány do úlohy.

Původní skeny jsou veřejné kopie přesně uvedené v agentově poznámce
a metadatech. Fyzický výtisk TAOCP zde ověřen nebyl.
