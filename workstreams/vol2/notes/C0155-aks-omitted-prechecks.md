# V2-C0155: vynechané předběžné podmínky v Theorem A

**Candidate, nikoli potvrzená nepravdivá věta.** Dodatek z 28. 4. 2005
k §4.5.4, str. 396, po opravě proměnné C0153 tvrdí polynomiální
charakterizaci prvočíselnosti bez předběžného vyloučení netriviálních
mocnin a malých prvočinitelů. Obě podmínky obsahuje citovaný Granville,
str. 4, a kroky 1 a 3 původního AKS na str. 784.

Úplný vlastní důkaz se standardními hypotézami, přesná místa jejich
použití a otevřený zbytek jsou v [primality-aks.md](primality-aks.md),
§1–6. Podmínka `r<n`, kterou Granville rovněž uvádí, byla naopak
pro samotné kritérium odstraněna obecným důkazem v §6. Nepřítomnost
této podmínky v Knuthově dodatku proto není částí podezření.

Přímý přesný test všech vstupů do 2048 a dalších 1215 čtverců
prvočísel neodhalil protipříklad. Nezávislý binomický model a cyklické
násobení kontrolují vymezené podmnožiny výsledků. Tento experiment
neopravňuje prohlásit vynechané podmínky za nadbytečné.

Další konkrétní redukce: žádný přijatý vstup nemůže mít `p^2|n`
s `p-1<=floor(sqrt(r)lg n)`, díky dosazení `z=1,a=p-1`.
Zbývají zejména velké prvočíselné mocniny a možné případy s malými
různými prvočiniteli. Není zde tvrzeno, že nějaký takový případ projde.

Původní sazba errata PDF22, Granville4/17–19 a AKS784–789 vizuálně
přečteny. Všechny čtyři vrstvy errat a aktuální `err2.textxt`
prohledány 3. 11. 2026; doplnění hypotéz nenalezeno. Není připraveno
hlášení tvrdící chybu ani odeslán dotaz. Fyzický poslední dotisk
a priorita nejsou ověřeny.
