# §4.3.3 — rychlé násobení, jednotlivé argumenty a 19 úloh

6. listopadu 2026, V2-X0140. Původní strany 294–318 a odpovědi
632–635 jsou přečteny. Každá úloha a matematické bloky textu jsou
spárovány s uzavřenými argumenty v
`results/sequential-fast-evidence.json`. Nespouštěl se žádný starý
ověřovač, benchmark ani nový matematický výpočet.

Přebírají se důkazy Karatsubova rozkladu, interpolace, řízení T1–T10,
časových mezí A/B a jejich zlepšení (`fast-digital`, `fast-improved`),
šesti modulů a rychlého Garnerova převodu (`fast-modular`), FFT,
škálování a certifikované přesnosti (`fast-fft`). Tabulky a číselné
příklady mají již uložené přesné kontroly. Platí všechny zohledněné
opravy, například m=144 v gigabitovém příkladu, nikoli původní 44.

Algoritmus R má obecný chybový invariant a důkaz rozsahu; dělení
vyžaduje nanejvýš jednu opravu předběžného podílu. Konstantní zvětšení
délky v časovém důkazu se řeší rozdělením na bloky, nikoli neplatným
předpokladem o libovolné monotónní funkci. Tím je uzavřen dopředný
odkaz z původní strany 279. Pole automatů má invariant vážené hodnoty,
časový rozvrh a obecný důkaz potřebného počtu modulů. Referenční
poznámky: `fast-reciprocal.md`, `fast-automata.md`, `fast-models.md`.

Nálezy jsou beze změny důkazního statusu, se závažností podle dopadu:

- C0103 **low**: pomocný postup vrací nekanonický zápis nuly pro
  e=1, u=2^f−1. Hlavní převod používá normalizované zbytky a funguje.
- C0104 **low**: při v=1/2 je chyba přesně nula, a tedy jedna ostrá
  nerovnost v důkazu neplatí. Algoritmus R a konečná mez jsou správné.
- C0105 **candidate/low**: zda úloha 11 zahrnuje přídavné q.
  Obě varianty jsou matematicky doloženy; pro čistý součin má n=2
  výjimku. Nejasný rozsah formulace nepovyšujeme na potvrzenou chybu.
- C0106 **medium**: citovaný pramen obsahuje silnější dolní mez pro
  uvedený páskový model; slabší nerovnost sama není nepravdivá.
- C0107 **candidate/medium**: přesný přechod od algebraické k bitové
  horní mezi v opravě odpovědi 15 není doložen. Slabší známá horní
  mez nevyvrací existenci ostřejšího algoritmu.

**Úloha 15 nově zůstává partial.** Dřívější evidence uzavírala audit
citovaných výsledků, nikoli výzkumnou otázku nejrychlejšího algoritmu.
Pro aktuální individuální průchod nesmí potvrzená dílčí vada C0106
zastírat otevřený přesný odhad C0107 a absenci obecného optimálního
řešení. Tím se nic ze starých důkazů neruší. Ostatních 18 úloh má
argument nebo vymezený experimentální výsledek; benchmark 14 není
tvrzením o univerzálním bodu, od kterého je T nejrychlejší.

Externí věty Schönhage–Strassen, Brent a citované online dolní meze
se přebírají jako explicitní externí vstupy s doloženými modely a
doménami, nikoli jako naše nové důkazy celých článků. Vlastní konstrukce
obvodové hloubky O(log n) a konvolučního jádra Little Fermat jsou
v `fast-context.md`. Odkaz ze strany 280 na hardwarové dolní meze je
ověřen jen bibliograficky; detailní důkazy citovaných prací zůstávají
mimo doložený rozsah. Historické rychlosti, prvenství a nedostupné
prameny mají zachované výslovné výjimky.

Strany 317/318/633/634 zůstávají partial pro otevřené výklady či
výzkumné tvrzení; 632 kvůli C0102 z předchozí sekce a 635 kvůli
začátku odpovědí §4.4. Další kurzor: 319/file331, převody soustav.
