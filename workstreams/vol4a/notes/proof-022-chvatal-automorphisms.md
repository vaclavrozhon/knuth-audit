# P0132/P0148 — přesně osm automorfismů Chvátalova grafu

6. listopadu 2026. Fig. 2(f), p14/file31; otázka §7–44, p39/file56,
odpověď p521/file538. **Checked:** osm realizovaných automorfismů
a obecná horní mez osm. Nejde pouze o osm viditelných symetrií obrázku.
Přesný seznam hran se přebírá z P0397 v `proof-016-colorings-cliques.md`,
ověřeného proti původnímu diagramu `images/proof-chvatal.png`.

## Jednotné označení a osm zobrazení

Rohy označ c₀,c₁,c₂,c₃ po směru hodin od levého horního, indexy modulo 4.
U každého rohu jsou dva vnitřní sousedé x_i,y_i. Převod na dřívější
označení je

    c₀,c₁,c₂,c₃ = A,B,C,D
    x₀,x₁,x₂,x₃ = p,r,t,v
    y₀,y₁,y₂,y₃ = w,q,s,u.

Všech 24 hran tvoří právě:

* vnější cyklus c_i–c_(i+1);
* c_i–x_i a c_i–y_i;
* matching x_i–y_(i+1);
* všechny čtyři hrany mezi {x₀,y₀} a {x₂,y₂}, a všechny čtyři mezi
  {x₁,y₁} a {x₃,y₃}.

Posun každého indexu o 1 zachovává všechny čtyři rodiny hran. Také
zobrazení c_i↦c_(−i), x_i↦y_(−i), y_i↦x_(−i) zachovává hrany:
matching x_i–y_(i+1) se změní na x_(−i−1)–y_(−i), opět matching.
Čtyři posuny a jejich složení s tímto zrcadlením tedy dávají osm různých
automorfismů. Jsou tranzitivní na rozích a zvlášť na všech osmi vnitřních
vrcholech. Tuto prokázanou tranzitivitu lze použít v následujícím počítání.

## Grafový invariant rozlišuje rohy

Počet prostých čtyřcyklů procházejících v je součet přes neuspořádané
dvojice jeho sousedů u,w z počtu jejich společných sousedů různých od v.
Každý čtyřcyklus má právě jednu takovou dvojici a jeden protilehlý vrchol;
nejde proto o násobné započtení.

Pro c₀ jsou sousedé c₁,c₃,x₀,y₀. Ostatní společné sousedy vypíše přímo
seznam hran:

| dvojice | společné sousedy kromě c₀ |
|---|---|
| c₁,c₃ | c₂ |
| c₁,x₀ | y₁ |
| c₁,y₀ | žádný |
| c₃,x₀ | žádný |
| c₃,y₀ | x₃ |
| x₀,y₀ | x₂,y₂ |

Tedy c₀, a tranzitivitou každý roh, leží na **5** čtyřcyklech.
Pro x₀ jsou sousedé c₀,y₁,x₂,y₂:

| dvojice | společné sousedy kromě x₀ |
|---|---|
| c₀,y₁ | c₁ |
| c₀,x₂ | y₀ |
| c₀,y₂ | y₀ |
| y₁,x₂ | y₃ |
| y₁,y₂ | žádný |
| x₂,y₂ | c₂,y₀ |

Tedy každý vnitřní vrchol leží na **6** čtyřcyklech. Každý automorfismus
musí zachovat počet cyklů, proto zachovává čtveřici rohů jako množinu.
Nemůže zaměnit roh za některý ze zbývajících osmi vrcholů.

## Horní mez bez procházení permutací

Rohy indukují C₄. Obraz c₀ má čtyři možnosti a obraz jeho souseda c₁ dvě;
zbylé dva rohy jsou pak nucené. Omezení automorfismu na rohy tedy má
nejvýše osm možností.

Zbývá vyloučit netriviální automorfismus fixující všechny rohy. Takový
automorfismus zachovává každou dvojici I_i={x_i,y_i}, neboť to jsou
právě vnitřní sousedé rohu c_i. Mezi I_i a I_(i+1) je **jediná hrana**
x_i–y_(i+1). Při pevných obou dvojicích proto musí fixovat i její konce.
Pro všechna i tak fixuje všechna x_i i y_i. Fixuje tedy celý graf.

Zobrazení automorfismu na jeho působení na rohy je injektivní. Horní mez
osm a výše realizovaných osm zobrazení se shodují. Důkaz zahrnuje celou
úlohu 44 i počet symetrií na p15. Girth z P0132 se přebírá z P0495,
nemění se ani znovu neodvozuje. Žádný matematický program, nový census,
nový nález nebo celostránkové argumentové uzavření.
