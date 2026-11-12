# MPR110: největší shoda a současné zachování uspořádání

7. listopadu 2026. Celé zadání p22–23/files42–43, odpověď p387/
file407 a příslušný autorský PS11.9.2019 p22–23/files28–29,
p43/file49 přímo zobrazeny. Šest vrstev errat a tři TeX zdroje
bez použitelné opravy110. Žádný nový matematický běh či restart.

Nechť n≥1, p_k,q_k≥0 a Σp_k=Σq_k=1. Položme
r_k=min(p_k,q_k),r=Σr_k. Z0≤r_k≤p_k plyne0≤r≤1.
Pro libovolný coupling c_ij je c_kk≤Σ_j c_kj=p_k a
c_kk≤Σ_i c_ik=q_k, tedy c_kk≤r_k. Proto
P(X=Y)=Σ_k c_kk≤r, jak tvrdí úvod zadání na p22.
Nulové marginální váhy ani nulové společné atomy se nevylučují.

##(a): každý člen konstrukce a oba kraje

Je-li r1, nezáporné rozdíly p_k−r_k mají součet0, proto
p_k=r_k pro každý k. Stejně q_k=r_k. Coupling
c_ij=r_i[i=j] má tedy obě marginály a shodu1. To rozepisuje
tištěné označení případu za triviální, včetně n1.

Pro r<1 definujeme přesně podle odpovědi

```
u_k=(p_k−r_k)/(1−r), v_k=(q_k−r_k)/(1−r).
```

Oba čitatelé jsou nezáporní a oba jejich součty jsou1−r>0.
Proto u,v jsou normalizovaná rozdělení. Pro každý jednotlivý
k je alespoň jeden z rozdílů p_k−r_k,q_k−r_k nulový, takže
u_k v_k=0. Tato poslední vlastnost je potřebná pro přesnou shodu.

Položme c_ij=(1−r)u_i v_j+r_j[i=j], jak uvádí tisk.
Matice je nezáporná a pro každý řádek i

```
Σ_j c_ij=(1−r)u_i Σ_j v_j+r_i=p_i.
```

Pro každý sloupec j obdobně
Σ_i c_ij=(1−r)v_j Σ_i u_i+r_j=q_j. Celkový součet je1.
Diagonála má c_kk=(1−r)u_k v_k+r_k=r_k, tedy
P(X=Y)=r. Horní mez je skutečně dosažena.
Index r_j v tištěném diagonálním členu je správně: při i=j
je roven r_i, mimo diagonálu se násobí nulou.

Pro r0 jsou původní podpory disjunktní po souřadnicích,
u=p,v=q a konstrukce je součinový coupling s nulovou diagonálou.
Žádné dělení nulou nevzniká. Finální matice může mít nulové
položky, které se jako atomy jednoduše vynechají. Výpočet r,u,v
vyžaduje O(n) aritmetických operací a přímé vypsání celé matice
O(n²); nejsou zde neukončené iterace nebo nezadané náhodné procedury.

##(b): každý reziduální předpoklad a směs

Nyní hodnoty tvoří konečný poset z109 a předpoklad říká
p(U)≤q(U) pro každou horní množinu U. Pro r1 už diagonální
coupling vyhovuje také X≼Y, díky reflexivitě.

Pro r<1 označme r(U)=Σ_(k∈U)r_k. Pak

```
u(U)=(p(U)−r(U))/(1−r)
    ≤(q(U)−r(U))/(1−r)=v(U).
```

Odečítá se tatáž hmotnost a dělí kladným číslem; všechny horní
množiny včetně prázdné a celého prostoru jsou zahrnuty. To je
přesný argument za tištěnou větou, že reziduální rozdělení
splňují hypotézy109. Použijeme celý opravený a nezávisle dokázaný
výsledek D207: existuje coupling h_ij s marginálami u,v,
podporovaný pouze na i≼j. Protože h_kk≤min(u_k,v_k)=0,
má h automaticky nulovou diagonálu, nejen v nějaké zvláštní volbě.

Směs

```
c_ij=(1−r)h_ij+r_j[i=j]
```

má stejné řádkové a sloupcové součty jako konstrukce(a), tedy
p,q. Její kladné atomy jsou buď povolené dvojice z h, nebo
diagonální dvojice, které splňují uspořádání reflexivitou.
Proto X≼Y platí v každém kladném atomu. Diagonála je přesně r_k,
takže současně P(X=Y)=r. Případ r0 používá přímo h; všechny
degenerované podpory i celková shoda r1 jsou tedy ošetřené.
Tato hodnota je maximální i mezi uspořádanými couplingy, neboť
úvodní horní mez platí pro všechny couplingy.

## Bibliografie a přesný rozsah

[Primární Math-Net záznam Dobrushina](https://www.mathnet.ru/php/archive.phtml?jrnid=tvp&option_lang=eng&paperid=1856&wshow=paper)
potvrzuje R. L. Dobrushin, Teoriya Veroyatnostei i ee Primeneniya
15(1970),469–497, a odlišný rozsah anglického překladu458–486.
Knižní ruská citace tedy odpovídá primárním metadatům.

Výslovné bibliografické výjimky bez matematické závislosti:

- Původní citace a obsah Doeblinova článku v Revue mathématique
  de l’Union Interbalkanique2(1938),77–105 nebyly rychle dostupné
  v primárním prameni. Sekundární bibliografie se nepovyšuje na
  prohlédnutí původního článku.
- Přesné historické umístění a rozsah konstrukce v Dobrushinově
  článku nebyly posouzeny; přímé stažení odkazovaného souboru
  nevrátilo PDF a žádný soubor nebyl uložen. Primární metadata
  byla ověřena, matematický argument je úplně vlastní výše.

Celá110(a,b) i horní mez z předchozí stránky jsou checked.
Žádný nález, kandidát nebo nová známá oprava. D207 se přebírá
jen jako již uzavřený konečný couplingový důkaz; žádná chyba
jeho původního tištěného mezikroku se sem nepřenáší.
