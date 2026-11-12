# §3.1: úvodní modely náhodnosti a odpověď 1

Kontrola 1. listopadu 2026. Úvodní text str. 1–6 a zadání úlohy 1 na
str. 6–7 byly přečteny, odpovědi zkontrolovány na původních stranách
[538](../images/vol2-p538.png) a [539](../images/vol2-p539.png).

## Úloha 1: jaké předpoklady odpovědi používají

Odpovědi rozlišují ideální pravděpodobnostní model od fyzického způsobu
výběru. Nejsou tvrzením, že každý pokus popsaným postupem je přesně
rovnoměrný. Rovnoměrný výběr z deseti cifer znamená pravděpodobnost
`1/10` pro každou cifru.

- Telefonní seznam nemusí mít rovnoměrné koncové cifry; opakované záznamy
  stejného čísla navíc zavádějí závislosti. Číslo náhodně otevřené stránky
  má problém sudosti a nerovnoměrného otevírání. Navržené dělení levé
  stránky dvěma odstraňuje sudost, nikoli mechanickou nerovnoměrnost.
- U ideálního symetrického dvacetistěnu má každá stěna pravděpodobnost
  `1/20`; dvě stěny na cifru dávají `1/10`. Zmínka o značení a povrchu
  výslovně připouští malé fyzické odchylky.
- Pro počítadlo používá odpověď Poissonovo rozdělení: při parametru
  `a>0` je `Pr(Z=k)=exp(-a)*a^k/k!` pro `k>=0`. Pravděpodobnost
  zbytku `d` modulo 10 je součet přes `k=d,d+10,...`. Konkrétně
  `Pr(Z je sudé)=exp(-a)*cosh(a)=(1+exp(-2*a))/2>1/2`, kde
  `cosh(a)=(exp(a)+exp(-a))/2`. Koncová cifra tedy není přesně rovnoměrná.
- Při deseti zaměnitelných měřeních má každá pozice stejnou šanci být
  jednoznačným minimem. „Zaměnitelné“ znamená, že libovolné přeuspořádání
  souřadnic nemění společné rozdělení. Podmíněně na existenci unikátního
  minima je jeho index rovnoměrný. U nezávislých stejně rozdělených
  Poissonových měření s `a>0` má přijetí kladnou pravděpodobnost, takže
  opakování skončí skoro jistě. Mění-li se intenzita mezi měřeními,
  tato symetrie už není zaručena; právě to doplňuje erratum z roku 2008.
- Hodinky vyžadují rovnoměrnou fázi v minutě a pro více cifer také vhodnou
  nezávislost okamžiků čtení. Volba člověka nemá takovou symetrii zaručenu.
- U koní je rozhodující nezávislost přiřazení cifer na výsledku závodu.
  Rovnoměrně promíchané označení dává každé cifře šanci `1/10` bez ohledu
  na výkonnost koní. Zadání s neznámými koňmi má tento model na mysli;
  pouhá neznalost konkrétního člověka sama o sobě není formální důkaz
  rovnoměrnosti. Doplněk o znalosti žokeje tuto výhradu připomíná.

V matematických výpočtech odpovědi nebyla zjištěna nová chyba. Známé
upřesnění fyzikálního modelu počítadla bylo zahrnuto.

## Text úvodu a jeho rozsah

Tvrzení o rovnoměrných nezávislých cifrách na str. 2 jsou přímo důsledkem
součinového rozdělení: konkrétní řetězec délky `r` má pravděpodobnost
`10^(-r)`, takže také podmíněná další cifra po pevně zadaném prefixu
zůstává rovnoměrná. Četnosti jednotlivých cifer a dvojic jsou očekávané
četnosti, nikoli přesné podmínky na každou realizaci. Úloha 2 výslovně
ukazuje, že přesně vyvážená realizace je velmi nepravděpodobná.

Příklad prostředních čtverců, tabulka K, ukončení K11 a celý rozklad
20bitové varianty jsou ověřeny v [poznámce o cyklech](intro-cycles.md).
Čtyřciferný cyklus z textu také přímo vychází:
`6100 -> 2100 -> 4100 -> 8100 -> 6100`, protože se vždy bere
`floor(x^2/100) mod 10000`.

Použití náhodnosti v simulaci, vzorkování, numerice, hrách a algoritmech
je motivační přehled. Výroky o estetickém dojmu a autorova osobní zkušenost
s prvním spuštěním K nejsou formální univerzální tvrzení. Historický
experiment s 38bitovým generátorem a neuvedeným seedem nepředstíráme
znovu provedený; kontrola zahrnuje soulad popisu, aritmetických údajů
a známých oprav podle pravidel [celého auditu](whole-volume-plan.md).

## Relevantní změny textu

Všechny vrstvy errat byly porovnány k 1. 11. 2026:

| Místo | Změna |
|---|---|
| str. 2 | Doplnění kryptografie mezi použití, 27. 2. 2004; přeznačení dalších bodů. |
| str. 3 | Doplnění historického odkazu na F. N. David, 5. 9. 2004. |
| str. 3 | Vypuštění Marsagliovy vedlejší citace, 16. 7. 2020. |
| str. 5, K1 | Drobná typografická úprava u podlahy, 9. 10. 1998; význam beze změny. |
| str. 7 | Úprava zájmena v zadání 1(f,g), 28. 4. 2017. |
| str. 9 | Úloha 19 požaduje asymptotické řešení a má nové hodnocení, 8. 5. 2005. |
| str. 9 | Hodnocení úlohy 21 sníženo na 40, 5. 4. 2007. |
| str. 539 | Opatrnější formulace o deseti měřeních, 18. 6. 2008; dovětek o žokeji, 22. 11. 2006. |

Matematický dodatek k 19 a známá oprava 21 jsou evidovány samostatně;
jejich pouhé uvedení v této tabulce je neuzavírá.
