# Stirling, Euler, Gauss a Legendre: přímá kontrola pramenů

Root převzal zmrazený paket
`parallel/factorial-primary-followup/stirling-euler-legendre/`:
124 souborů, 120781505 bajtů, 30 externích vstupů. Ověřeny všechny
velikosti a SHA-256. Manifest má SHA-256
`3515236237b2710ed28e53e705865e2e5dde7d0d5a7df9705b135881ebe3cc9d`.
X0760 uzavírá níže vymezené kladné historické doklady. X0761 ponechává
ostatní historické výroky partial; C0089 je samostatný kandidát.
Celá §1.2.5 ani její dosud otevřené úlohy se tím neuzavírají.

## Stirlingův vzorec a interpolace

Root přímo četl titul 1730, s. 110, 112, začátek 113, s. 137 a původní
Errata (PDF 7, 122, 124, 125, 149, 166). Agentův širší rozsah je
108–112, začátek 113, 135–138 a konec scholia 139. Knižní s. 47–49
byly rovněž zobrazeny. S. 137 zavádí z = N + 1/2; desetinný logaritmus
N! má hlavní člen z log10(z) − a z + 0.399089934179, kde a = log10(e).
Konstanta je log10(sqrt(2 pi)). Následují −a/(24z), 7a/(2880z^3) atd.
Po umocnění dostaneme sqrt(2 pi)(z/e)^z. Poměr k obvyklému hlavnímu
členu sqrt(2 pi N)(N/e)^N je

    (1 + 1/(2N))^(N+1/2) exp(-1/2) -> 1.

To přesně vysvětluje doplnění (7) z 22. 1. 2019 v all1-pre, s. 6,
které root přímo zobrazil. Původní Stirlingova Errata opravují s. 136–137;
nejde o nový nález v TAOCP. S. 110 dokládá přechod od faktoriálů k jejich
logaritmům při interpolaci. S. 112 a začátek 113 uvádějí půlcelou hodnotu
0.8862269251 a její vztah k pi/4 po umocnění. Moderní formule (11)–(12)
nejsou vydávány za doslovnou původní sazbu; jejich matematika byla již
ověřena v `notes/gamma-functions.md` a nebyla znovu testována.

## Eulerův součin a datum dopisu

Root četl Fuss I, s. 3–5 (PDF 1–2 ve výřezu), a kritickou online edici
2016, s. 99, 102 a komentář 586; také její titul a tiráž (PDF 3–4).
Pro pevné reálné x > 0 označme

    T_n(x) = n^x n! / product_{j=1}^n (x+j).

Eulerova konečná aproximace používá (n+1)^x místo n^x. Její poměr
k T_n(x) je (1+1/n)^x, tedy má tutéž limitu. Dopis proto skutečně
obsahuje zobecnění v knižní (13).

Fuss I tiskne 16. října 1729; kritický přepis na s. 102 uvádí
13. října, záhlaví 13. (24.) října. Jde o přepis autografu evidovaného
R715, RGADA f. 181, č. 1413, III, fol. 44r–45v. Samotné datované
fol. 45v nebylo získáno. Veřejný úplný basilejský PDF 2016 má v tiráži
PRELIMINARY VERSION a nebyl kolacionován s konečným tiskem Springer 2015.
Datum TAOCP je tím obsahově podpořeno; paleografická kontrola se netvrdí.
Euler zmiňuje předchozí komunikaci s Danielem Bernoullim. Prioritu
samostatně rozebírá `notes/euler-priority-root-candidate.md`.

## Původní značky

Root přímo četl Euler E421, s. 95, 98, 120 a 124 (PDF 5, 8, 30, 34).
S. 95 zavádí integrál logaritmické mocniny; s. 120 §43 označuje jeho
hodnotu hranatými závorkami [lambda]. Půlcelá hodnota v §45 na s. 124
je sqrt(pi)/2. Agent četl širší intervaly uvedené v read-log.json.
Obsah a značka jsou doloženy, samostatný ročníkový titul a absolutní
prvenství značky se zde neprokazují.

Root přímo četl Legendre, Exercices 1811, titul, s. 276–277 a 280
(PDF 7, 284, 285, 288). V §53–54 je Gamma(a) integrál na (0,1)
z (log(1/x))^(a−1), nejprve pro 0 < a < 1; následuje rekurence.
Substituce t = −ln(x) dává obvyklý gama integrál. §58 má
Gamma(n+1) = n Gamma(n), Gamma(1) = 1. Proto n! = Gamma(n+1),
nikoli Gamma(n). Jde o jinou publikaci než Essai 1808, s. 8,
citovaný známým erratem k prvočíselným exponentům v n!.

Root přímo četl Gauss, Werke III, s. 144–146 (PDF 158–160).
Rovnice (38) definuje Pi(k,z) = k^z k! / product_{j=1}^k(z+j).
§20 označuje limitu Pi(z); §21 dává rekurenci Pi(z+1) = (z+1)Pi(z)
a Pi(0)=Pi(1)=1, Pi(2)=2, Pi(3)=6, obecně (46) celé faktoriály.
Značka Pi n v TAOCP je přímo doložena. Titul druhého otisku Werke 1876
a údaj o přednesu 1812 byly přijaty v dřívější dávce; původní časopisecká
sazba 1812/1813 se zde nevydává za kolacionovanou.

## Zbylé meze a errata

X0761 ponechává partial historické tvrzení, že Stirling nedokázal
obecnou zlomkovou interpolaci, a popularitu rohové značky v Anglii
a Itálii. Kladné ukázky a dnešní důkaz neprokazují nepřítomnost
historického důkazu. Starší mezery Uhler, Toscano, Dutka a datace
Leibnizova výroku mají vlastní položky a trvají.

Agent prohledal all1-prepre, all1-pre, all1 a err1 podle stran i tématu;
root převzal přesné výsledky a hashe. Root nyní zobrazil all1-prepre
s. 7 a all1-pre s. 6. Doplňky Legendre 1808 a Kramp s. 219 se nemění.
Žádná nalezená oprava nemění Eulerovo prvenství ani zdejší značky.
Úplný rozsah agentova čtení, ostatní historické obrazy a navigace jsou
v neměnném paketu. Root manifest zachycuje také použité sdílené knihy
a čtyři PDF/textové vrstvy errat. Nové matematické testy nebyly potřeba.
