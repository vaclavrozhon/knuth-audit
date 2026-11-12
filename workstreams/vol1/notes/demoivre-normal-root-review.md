# §1.2.10–14: de Moivrova normální aproximace

**Celá úloha 14 je checked v opraveném znění.** Zbývající atribuci
dokládá de Moivrův vlastní text pro libovolnou pevnou pravděpodobnost
0<p<1. Již přijatý moderní důkaz v `analysis-probability.md` se nemění.

Koordinátor ověřil 17 souborů a 15 vstupů zmrazeného balíčku
`parallel/analysis-primary-followup/exercise14-demoivre/`.
SHA-256 jeho MANIFEST.json je
`921395023841863688bf331af4bf9d3da624ab16ca1968fb8b778502e5e1ca92`.
Společný originál TAOCP a úplné čtyři PDF errat byly hashově ověřeny
v této dávce u X0756; jejich záznamy jsou připojeny i sem.

Agent přímo přečetl titul a s. 234–243 druhého vydání
*The Doctrine of Chances* (1738), na 243 pouze konec této pasáže.
Koordinátor nezávisle přímo přečetl titul, 234–235 a 241–242,
zadání TAOCP106 a odpověď501. Titul výslovně uvádí druhé vydání
a 1738. Na s. 235 autor říká, že překládá svůj soukromý tisk
z 12.11.1733, s možností dalších dodatků. Proto obsah konkrétních
korolárů nedatujeme bez kolace původního tisku zpětně do1733.
Knižní úloha sama žádný rok ani konkrétní vydání netvrdí.

Lemma3 na241 výslovně užívá obecný poměr kladných vah a:b,
střed an/(a+b) a odchylku l. Koroláry8–10 na242 uvádějí výšku
největšího členu a kvadratický logaritmus poměru členů, s odchylkou
řádu sqrt(n). Pro p=a/(a+b), q=b/(a+b), počet pokusů n a konstantu
c=2pi (obvod kružnice jednotkového poloměru) jsou jejich výrazy

```text
(a+b)/sqrt(abnc) = 1/sqrt(2pi*npq),
-(a+b)^2*l^2/(2abn) = -l^2/(2npq).
```

Po standardizaci l=x*sqrt(npq), kde x je pevná reálná odchylka
v jednotkách směrodatné odchylky, vzniká exp(-x^2/2) se správnou
normalizací. Korolár10 výslovně přenáší výpočet pravděpodobností
na nestejné váhy. Atribuce tedy nepokrývá pouze symetrický případ.

Historická formulace o nekonečné mocnině není vydávána za moderní
odhad zbytku ani za přesnou větu o celočíselném modu. Úloha je již
dokázána rozvojem charakteristické funkce: její logaritmus po
standardizaci je -t^2/2+O(n^(-1/2)). Krajní p=0 nebo1 mají nulový
rozptyl a do této standardizace nespadají.

Všechny čtyři úplné vrstvy errat byly prohledány agentem;
koordinátor přímo četl rozhodné obrazy all1-prepre11/35.
Opravy17.3.1998 (de místo De) a1.8.1997 (závorky exponentu)
jsou známé a zachované. Nový nález nevznikl. Žádné dříve úspěšné
matematické testy se neopakovaly. Nedokládáme absolutní prvenství,
celý de Moivrův spis ani nepřečtený latinský tisk1733.
