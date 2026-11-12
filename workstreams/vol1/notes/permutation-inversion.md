# §1.3.3: inverze permutace algoritmy I a J

Kontrola 1. listopadu 2026. Položky V1-X0003, V1-X0006 a V1-X0007.
Výsledek: pseudokód obou algoritmů je správný pro n>=1. Ve vysvětleních
prvního dotisku jsou dvě známé chyby. Strojový kód MIX nebyl emulován.

## Zdroj a označení

Pseudokód byl přečten ze skenů tištěných stran
[176](../images/vol1-file191-p176.png),
[177](../images/vol1-file192-p177.png) a
[178](../images/vol1-file193-p178.png).
Odpovědi §1.3.3-13 a §1.3.3-14 jsou na
[s. 523](../images/vol1-file538-p523.png).

Permutace p je vzájemně jednoznačné zobrazení čísel 1,...,n na sebe.
`p(v)` označuje původní následník v, `p^{-1}(v)` jeho původní předchůdce.
Pole X je měněný pracovní stav; původní p se v důkazech nemění.
Cyklus je posloupnost, po níž se opakováním p vrátíme do výchozího prvku.
Invariant je tvrzení platné při každém příchodu do označeného kroku.

## Algoritmus I

Algoritmus prochází kandidáty m od n dolů. Když narazí na cyklus poprvé,
musí být m jeho největším prvkem: každý větší kandidát už byl zpracován.
Kroky I3–I4 sledují původní následníky a přepisují jednotlivé odkazy
záporným předchůdcem. První záporný zápis slouží jako značka uzavření cyklu;
jeho hodnota nemusí být správným předchůdcem, protože při návratu na maximum
ji I5 přepíše správnou kladnou hodnotou.

V ostatních vrcholech tohoto cyklu je po uzavření už správná záporná inverze.
Při jejich pozdějším navštívení se přejde přímo z I2 do I5 a obrátí se znaménko.
Nezpracovaný cyklus je disjunktní se všemi dokončenými cykly, takže sledování
původních odkazů nemůže zabloudit do dřívější značky. To současně dokazuje
ukončení a správnost pro všechna n>=1.

Každá buňka projde právě jednou záporným zápisem v I3 a kladným zápisem v I5.
I2, I3, I4 a I5 se tedy provedou n-krát, větev uzavírající cyklus C-krát,
kde C je počet cyklů. To ověřuje počty uvedené u Programu I; samotná
strojová implementace a její časové jednotky nejsou tímto testem certifikovány.

### V1-X0006: chybný index v komentáři I5

Při příchodu do I5 je i záporné. Správný vztah je `p(-i)=m`;
sken má v komentáři `X[i]`. Už pro n=1, p(1)=1, je i=-1.
Přiřazení `X[m] <- -i` ve skenu je správné. Chybu komentáře opravuje
`all1-prepre`, s. 15, datum 22. února 1998. Jde o známé erratum.

## Algoritmus J: opravený invariant

Před J2 v iteraci m jsou hotové právě zdrojové vrcholy větší než m.
Pro každý vrchol v platí následující úplný popis X:

1. Pokud `p^{-1}(v)>m`, pak `X[v]=p^{-1}(v)>0`.
2. Jinak začneme ve v a sledujeme p, dokud poprvé nedojdeme do vrcholu
   t<=m; poté `X[v]=-p(t)`.

Druhá procházka vždy skončí: podmínka `p^{-1}(v)<=m` zaručuje, že cyklus
obsahuje dosud nezpracovaný vrchol. Na začátku m=n je t=v a X[v]=-p(v),
což je přesně inicializace J1.

V J3 se jde z m po kladných, tedy obrácených, odkazech přes zpracované
vrcholy. Nelze vytvořit uzavřenou smyčku: cyklus obsahuje nezpracované m.
Označme h vrchol, v němž se narazí na záporný odkaz. Cesta z h po původním
p vede přes právě prošlé vrcholy zpět do m; proto `X[h]=-p(m)`.

Položme w=p(m). Před zpracováním m je X[w] záporné, protože jeho původní
předchůdce je m. Krok J4 provede postupně

```text
X[h] <- X[w]; X[w] <- m.
```

Druhý zápis opraví inverzi ve w. První spojí nezpracovanou část cyklu
za právě odstraněným m: stará hodnota X[w] je záporný následník prvního
zbývajícího nezpracovaného vrcholu. Ostatní záporné cesty se přes m
nemění — jediný jejich možný začátek bez zpracovaného předchůdce je h.
Tím je invariant zachován pro m-1. Pokud h=w, právě se dokončil poslední
nezpracovaný vrchol daného cyklu; první zápis je identita a druhý správně
zanechá kladný odkaz. Po m=1 jsou všechny buňky správnou inverzí.

### V1-X0007: chybějící podmínka v odpovědi §1.3.3-13

Původní odpověď tvrdí zápornou větev bez vyloučení již zpracovaného
předchůdce. Nejmenší protipříklad je p=(2,1). Po iteraci m=2 je X=(2,-2).
Před J2 s m=1 by původní záporná větev pro v=1 požadovala X[1]=-2,
přestože X[1]=2. Oprava z 29. března 2023 v `all1` a `err1`, s. 523,
přidává přesně podmínku, že do v nesmí původním p přicházet žádný vrchol >m.
Viz [obraz errata](../images/errata-all1-file014.png). Algoritmus se nemění.

## Počet průchodů J3: nezávislé odvození průměru

Nechť A je celkový počet čtení X[j] v J3. V iteraci m projdeme opačným
směrem po původním cyklu několik po sobě jdoucích vrcholů >m a skončíme
před prvním předchůdcem <=m. Označme počet těch velkých vrcholů L_m.
J3 se provede L_m+1 krát.

Pro rovnoměrně náhodnou permutaci se při postupném odkrývání předchůdců
vybírá pokaždé rovnoměrně z dosud nepoužitých zdrojových vrcholů. Dokud
nebyl nalezen vrchol <=m, není cyklus uzavřen; jeho uzavření výběrem m
je samo jednou z možností ukončení. Počet prohlédnutých vrcholů má tedy
střední hodnotu pořadí prvního z m označených prvků v náhodném pořadí n
prvků: `(n+1)/(m+1)`. Tato hodnota plyne i rozdělením n-m neoznačených
prvků do m+1 stejně očekávaně dlouhých mezer kolem označených prvků.

Pro harmonické číslo `H_n = sum_{k=1}^n 1/k` proto

```text
E[A] = sum_{m=1}^n (n+1)/(m+1) = (n+1)H_n - n.
```

To souhlasí s odpovědí §1.3.3-14, ale nevyužívá její obrázek s kanonickým
zápisem cyklů. Důkaz E[C]=H_n: při vložení n-tého prvku do náhodné
permutace existuje n stejně možných míst — n-1 za starými vrcholy a jedno
jako nový samostatný cyklus. Přírůstek počtu cyklů má očekávání 1/n.

## Konečná kontrola a hranice výsledku

[Program](../check_first_blocks.py) zkontroloval všech 46 233 permutací
pro 1<=n<=8. Porovnává s nezávislou inverzí získanou hledáním předobrazu
v původním poli, kontroluje opravený invariant J před každou iterací,
komentář I5 a počty kroků I. Průměry A a C počítá přesnými zlomky;
pro n=8 vychází E[A]=4609/280 a E[C]=761/280.
[Výsledky](../results/first-blocks.json) obsahují všechny velikosti.

Nulový vstup není zahrnut do tvrzení správnosti: pseudokód by přistoupil
k X[0]. Jde zde o explicitní omezení rozsahu kontroly, nikoli o nový nález.
Neověřovali jsme mezní velikosti paměti, bajty, přetečení ani úplné MIX programy.
`all1` obsahuje navíc úpravu inicializace Programu J z 23. prosince 2024;
ta zůstává pro budoucí audit strojového kódu. Při rešerši byly zahrnuty
všechny čtyři řady errat a aktuální TeX, s. 176–178, 523 a označení I/J.
