# X0766: citovaná věta o spojitosti v §1.2.10–13

Celá úloha 13 je **checked s ponecháním potvrzeného C0013**.
Poslední chybějící citace je nyní obsahově přečtena. Dřívější důkaz
normální limity, Gončarov a Flajolet–Soria se přebírají z přijatých
poznámek; testy se neopakovaly. Checked není tvrzení o bezchybnosti
původní odpovědi: chybějící konstanta v ocasovém odhadu zůstává nálezem.

Root ověřil všech 28 souborů a 16 externích vstupů zmrazeného paketu
`parallel/analysis-primary-followup/exercise13-gk/`. Manifest má SHA-256
`88a7307b10de6fc867992840640f9d2d9b3222fa68f6679865dce36c4e672329`.
Úplný PDF reprodukuje anglický překlad Gnedenka–Kolmogorova z roku 1954,
284 stran; SHA-256
`054de465071d08f63d944e8e83df08d37fe20b79b7d1e81f04625074930ec635`.
Veřejná položka IA projektu Mir Titles má novou digitální obálku,
nedoložený fyzický exemplář a prázdnou rubovou stranu titulu.
Obsah překladu lze číst; první fyzický dotisk ani kolofon se netvrdí.

Root přímo zobrazil titul, s. 32–33, 46–47, §13 od nadpisu na 52,
celé 53–54 a úvod 55 před §14. Agent navíc četl překladatelovu
předmluvu v–vi; přesné hranice jsou v jeho read-log.json.
Charakteristická funkce veličiny Y je phi(t)=E exp(i t Y) pro reálné t.
Slabá konvergence rozdělení znamená konvergenci očekávání omezených
spojitých funkcí. S. 33 ji spojuje s konvergencí distribučních funkcí
v bodech spojitosti limitní funkce. S. 46–47 dávají charakteristickou
funkci normálního rozdělení se středem a a rozptylem sigma^2 jako
exp(i a t − sigma^2 t^2/2).

Obě věty na s. 53 a důkazy 53–54 dávají přesný potřebný most:
slabá konvergence implikuje konvergenci charakteristických funkcí;
jejich bodová konvergence ke spojité funkci dává slabou konvergenci.
Druhý důkaz používá integrální odhad hmoty v omezeném intervalu,
tedy zabrání úniku pravděpodobnostní hmoty do nekonečna, a jednoznačnost
limitního bodu. V TAOCP je Y_n=(X_n−mu_n)/sigma_n a limitní funkce
exp(−t^2/2). Je to právě funkce standardního normálního rozdělení.

Zdroj používá Pr(Y<x), TAOCP Pr(Y<=x). Přesný převod nevyžaduje
nepřítomnost atomů u konečných n: pro epsilon>0 je
Pr(Y<x)<=Pr(Y<=x)<=Pr(Y<x+epsilon). Po limitě n a pak epsilon dolů
k nule dává spojitost normální distribuční funkce tentýž výsledek.
Obrácený převod použije x−epsilon. Citovaný obsah proto souhlasí.

Root přímo porovnal TAOCP105/501, all1-prepre11/35 a all1 6.
Titul skutečně uvádí Cambridge42,Mass.,1954, v souladu s opravou
29. 3. 2023. Opravy Pr a závorky se nemění; žádná neodstraňuje C0013.
Všechny čtyři vrstvy byly prohledány a zachyceny v agentově výtahu.
Nejde o audit celé citované monografie ani samostatný důkaz Lévyho
historického prvenství. Hlavní historický text §1.2.10 má dál vlastní
otevřené položky. Podklady fixuje root manifest.
