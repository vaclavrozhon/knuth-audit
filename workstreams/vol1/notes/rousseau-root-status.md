# V1-X0769: přesná zbývající Rousseauova citace

Úloha §1.2.11.3–20 i odpovídající citace hlavního textu na 121
zůstávají source-partial. Matematický důkaz je hotov v
`asymptotic-gamma.md`; nové podklady nedodaly samotný článek.

Root ověřil všech 21 souborů a 17 vnějších závislostí paketu
`parallel/asymptotic-primary-followup/results/rousseau-ex20-manifest.json`
(SHA-256 `87a7db8b3015ff1569894a45da04e67eba1b692be8539d90277fb354dcebe966`),
přečetl agentovu poznámku, stavový soubor a původní institucionální
životopis. Položka 45 opravdu uvádí Rousseauův článek v Applied
Mathematics Letters 2(2) (1989), 159–161. Bibliografická identita
je tím nezávisle podpořena, nikoli obsah matematického důkazu.

Přímo přečtená odpověď Elsevier API požadavku view=FULL je
`Invalid API Key`, nikoli článek. Zachycené veřejné odpovědi
Wayback pro HTTPS pdf a pdfft mají prázdné archived_snapshots;
pokus pro historické HTTP je HTTP 429 a neumožňuje tvrdit absenci
kopie. Vydavatelská stránka i pdfft vrátily 403. OpenAlex ukazuje
na vydavatele, ale neposkytl samostatný plný text. Dřívější příznak
openArchiveArticle v pouhých metadatech není dokladem získaného PDF.
Žádný z těchto neúspěchů není důkazem obecné nedostupnosti článku.

**Z originálu článku máme přímo přečteno nula ze tří stran.**
Zbývá porovnat normalizaci pravděpodobnosti souvislého náhodného
zobrazení, převod na Laplaceův integrál, inverzní řadu a její zbytek.
Autorův životopis ani vydavatelský abstrakt tuto práci nenahrazují.

Root přímo zobrazil TAOCP 123 a 507 a all1-prepre 36. Původní
oprava z 1.1.2006 doplňuje faktor k vznikající derivováním
`x=sum c_k(2v)^(k/2)`, kde `v=x-log(1+x)` a c_k jsou koeficienty
inverzní řady. Oprava zůstává known_erratum. Hledání všech čtyř
úplných vrstev errat je v zmrazeném paketu, spolu s hashi devíti
společných vstupů. Žádný nový nález, žádné opakované matematické testy.
