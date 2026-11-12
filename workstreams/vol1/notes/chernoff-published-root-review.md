# X0767: Chernoffův publikovaný důkaz a celá §1.2.10–22

Celá úloha 22 je **checked**. Obecné důkazy částí (a)–(c), okrajové
případy i všechny známé opravy jsou již v `notes/analysis-tails.md`;
root tuto návaznost přečetl, úspěšné testy neopakoval. Nyní je
uzavřena mezera mezi dříve čteným preprintem 1951 a článkem 1952.

Root ověřil všech 30 souborů a 16 externích vstupů v neměnném paketu
`parallel/analysis-primary-followup/exercise22-chernoff/`; manifest
má SHA-256
`e8d312444e4b814c70134ee7889fea10e70ab72d09ead18f47e0d3391038c330`.
Úplné číslo Annals23(4), prosinec1952, je veřejný mikrofilm IA1514501-03,
172 stran, 29607408 bajtů; PDF SHA-256
`41ad558c33815ebbf2a1bf5e07c6da6c3f14105f417f69862ffd1bcc1e079ee4`.
Tmavé obálky nebyly drobným písmem přečteny; identifikace stojí
na metadatech a shodě samotného článku, autora a stránkování.

Root přímo četl 493, 495–496, bibliografii a konec 507 a záhlaví
nového článku na 508. Agent četl souvisle 493–499 a konec507;
500–506 se nevydávají za nově auditované. S. 495 označuje S_n součet
n nezávislých veličin se stejným rozdělením X. Momentová funkce je
M(t)=E exp(tX); m(a)=inf_t exp(−at)M(t). Theorem1 dává pro příslušný
směr odchylky od E(X) horní odhad ocasové pravděpodobnosti m(a)^n.
Rovnice (3.9)–(3.11) na496 přímo dokazují horní odhad exponenciální
funkcí, poté berou infimum. Právě tato metoda je citována v odpovědi22(a).

TAOCP připouští odlišné pravděpodobnosti p_k. Pro nezávislé Bernoulliho
veličiny X_k, tj. Pr(X_k=1)=p_k a Pr(X_k=0)=1−p_k, je místo jedné
mocniny momentové funkce součin product_k(1−p_k+p_k exp(t)).
Při r=exp(t)>0 a mu=sum_k p_k je tento součin nejvýše
exp((r−1)mu). Exponenciální odhad s hranicí mu r tak dává přesně
(r^(−r)exp(r−1))^mu z úlohy. Nerovnosti v (b), prahový odhad v (c)
a případ mu=0 byly již obecně zkontrolovány; nejsou vydávány za
doslovně opsané konstanty původního článku.

Číslování preprintu1951 nelze přenášet na publikovanou verzi:
důkaz zde identifikujeme pomocí Theorem1 a (3.9)–(3.11), nikoli
preprintového Lemma5. Citace „See“ netvrdí absolutní prioritu.
Bibliografie507 má Kolmogorova1933; tato hlavní historická citace
se nepovažuje za přečtenou pouze tím, že je v seznamu literatury.

Root přímo porovnal knižní107/502 a erratové all1-prepre35, all1 6/13.
Nový článek na508 potvrzuje opravu konce rozsahu493–509 na493–507
z 22. 1. 1999. Záporná znaménka exponentů1999, obor p_k a doplňky
2023 souhlasí s přijatou matematikou. Všechny čtyři vrstvy byly
prohledány; nový nález nevznikl. C0015 se týká sousední odpovědi21,
nikoli této úlohy nebo Chernoffova článku. Podklady fixuje root manifest.
