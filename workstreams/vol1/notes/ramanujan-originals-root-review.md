# V1-X0772: Ramanujanovy původní časopisecké texty

Obsah konkrétních citací na s. 121 je checked. Root ověřil 59
souborů a 11 vnějších závislostí zmrazeného paketu
`parallel/asymptotic-primary-followup/results/ramanujan-originals-manifest.json`,
SHA-256 `da4a1891e116f456b4e523516d38fb3919570e214e53143807323bd07dc6056e`.
Přečetl poznámku a stavový soubor a přímo zobrazil tituly obou
původních čísel JIMS: 3(3), červen1911, a4(4), srpen1912.
Zobrazeno zadání294 na128 (PDF38) a celé jeho řešení151–152
(PDF31–32), nikoli okolní nesouvisející úlohy. Původní PDF,
veřejné URL a přesné hashe jsou v agentově poznámce a manifestu.

Pro kladné celé n je Ramanujanova veličina theta určena rovnicí
`exp(n)/2=sum_(j=0)^(n-1) n^j/j!+(n^n/n!)theta(n)`.
Z knižních definic plyne přesně `theta(n)=(R(n)-Q(n))/2`.
Jeho integrál `J(n)=integral_0^infty exp(-z)(1+z/n)^n dz`
se konečným binomickým rozvojem rovná
`(n!/n^n)sum_(j=0)^n n^j/j!`; proto theta je
`n!exp(n)/(2n^n)+1-J(n)`. Substituce t=n+z převádí J na
integrál I_1 v TAOCP a další škálování z=u sqrt(2n) je přímo
vytištěno v řešení. Tím souhlasí funkce i popis metody.

Původní152 má koeficient **−16/(8505 n^3)**, nikoli −1/(8505 n^3).
Root přímo přečetl TAOCP121 a opravu all1-prepre12 z8.2.2000;
jde o známé erratum. Původní Ramanujanovo řešení samo výslovně
uvádí obtížnost důkazu mezí1/3 a1/2 a nedodává obecný odhad zbytku
pro všechny integrální kroky. Jde o doklad původní řady a metody;
úplné moderní důkazy jsou již přijaté v asymptotic-gamma.md
a ramanujan-bound.md. Jejich úspěšné testy se neopakovaly.

Doplňkově root zobrazil tiráž souboru prací (PDF8), stránku xxiii
(PDF27) a konkrétní VII(2) na xxvi (PDF30). Je to **tisk AMS2000**,
nikoli původní1927, přes katalogové pojmenování souboru. Vzorec
`theta(n)=1/3+4/(135(n+k))`, kde k leží mezi2/21 a8/45,
dokládá atribuci silnější nerovnosti úlohy13. Kontext na xxiii
ale výslovně kombinuje přílohy prvního dopisu s pozdějšími dopisy:
konkrétní vzorec zde nedatujeme16.1.1913. Agentův širší rozsah
četby reprintu je samostatně zaznamenán.

Všechny čtyři úplné vrstvy errat prohledány; společné hashové
vstupy jsou v readonly-inputs.json paketu. Nový nález nevznikl.
Není tvrzena vyčerpávající kontrola absolutní priority, celé
Ramanujanovy pozůstalosti ani fyzického exempláře TAOCP.
