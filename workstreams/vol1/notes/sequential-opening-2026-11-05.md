# Obnovený průchod: úvod a §1.1

5. listopadu 2026. Nové zadání: matematika a fakta; rychle nedostupná
bibliografie smí být výslovně přeskočena. Původní důkazy a stavy se
nezahazují. Záznam rozlišuje přečtení stránky, dokončení kontroly a
přeskočený pramen. Výsledky výpočtů z 1.–4. listopadu se bez důvodu
neopakují. Žádný email ani návrh emailu nevzniká.

## Nově uzavřená matematická závislost na straně 7

T_n je průměr počtu dělení L(m,n) pro m=1,...,n, ekvivalentně
Cesàroův průměr přes všechna kladná m. Původní soubor dává stranu7
na obrazu22; původní sazba byla přímo přečtena. Tvrdí T_n ~ c log n,
kde c=12 log(2)/pi^2. Nepředpokládá nesoudělnost m,n.

Použité podklady svazku2: `notes/euclid-discrete.md`, část3,
a `notes/euclid-average.md`, část1. Nově byl otevřen primární článek
Bykovskii–Frolenkov (2017), DOI 10.1070/SM8718, úvod644–646.
Jeho rovnice3 uvádí redukovaný průměr s(a/b)=c log b+C_P−1+
O_epsilon(b^(−1/6+epsilon)). Proto při pevném epsilon=1/12 má
knižní průměr tau_b po přidání prvního nulového podílu tvar
c log b+O(1). Případ b=1 lze zahrnout změnou konstanty.
Jde o externí publikovanou větu s ověřenou normalizací, nikoli
nový vlastní důkaz čtyřicetistránkového článku.

[Primární zdroj](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=8718&what=fullteng).

Pro úplný průměr rozdělíme čitatele podle d=n/gcd(m,n). Počet kroků
se při krácení nemění; každému d|n přísluší phi(d) čitatelů. Proto

    n T_n = sum_(d|n) phi(d) tau_d,
    sum_(d|n) phi(d) = n.

Aritmetická identita ze svazku2 dává

    (1/n) sum_(d|n) phi(d) log d
      = log n − sum_(p^k|n, k>=1) (log p)/p^k.

Označme poslední součet S(n). Pak T_n=c(log n−S(n))+O(1).
Pro ověření vedoucího členu není nutná silná věta o prvočíslech:

    0 <= S(n) <= sum_(p|n) log p/(p−1).

Rozdělme prvočísla v B=log n (n dost velké). Malá prvočísla jsou
omezena součtem přes všechna celá čísla 2<=j<=B, který je
O((log B)^2). Pro velká prvočísla použijeme

    sum_(p|n, p>B) log p/(p−1)
      <= log n/(B−1) = O(1),

protože součin různých prvočinitelů dělí n. Tedy
S(n)=O((log log n)^2)=o(log n), a skutečně T_n~c log n.
Tento přechod je vlastní obecný argument; není odhadnutý z konečných dat.
Výrok na straně7 je v uvedeném smyslu správný. Nový nález nevznikl.

## Další matematika §1.1

Přímo nově přečteny původní strany1–9 a původní poznámka
`algorithms.md`. Zachovány obecné invarianty, ukončení, výpočty
konkrétních gcd, odvození periodických průměrů a doslovný přepisovací
program v této poznámce. Bez nového výčtu4096 vstupů.

Konečnost rozhodování o vynucené výhře v šachu na straně6 lze
ověřit bez vyřešení počáteční pozice: v konečném herním grafu
se spočte nejmenší atraktor bílých vítězných koncových stavů.
Vlastní tah přidá pozici s některým následníkem v atraktoru;
soupeřův tah přidá neterminální pozici, jejíž všichni následníci
už jsou v atraktoru. Terminální nevýherní stavy se nepřidávají
vakuózním univerzálním pravidlem. Rank iterace dá konečnou
vítěznou strategii. Mimo atraktor může soupeř zabránit dosažení
bílého cíle; remíza není bílá výhra. Potřebné údaje pravidel
patří do stavu. Je to stejný princip jako přijatý důkaz
`linked-allocation-root-review.md`, ne nový brute force šachu.

Reprezentace přepisovacích stavů na straně8 je efektivní:
nejlevější výskyt ve finitním slově se najde konečným průchodem,
prázdný vzor je na začátku, konečný stav je pevný bod. Rozsah
skokových indexů je vynucen předchozím požadavkem f:Q→Q.
Existence překladu Turingova stroje plyne z kódování jediné hlavy
a stavu do slova a konečných přepisů sousedních symbolů; opačná
simulace prostě prohledá konečné slovo. Historický přesný přepis
Markovovy knihy se tím neprohlašuje za přečtený.

## Errata a bibliografické výjimky

Všech pět oficiálních originálů errat bylo 5.11. znovu staženo;
všechny SHA256 souhlasí s archivem. Viz
`sources/sequential-2026-11-05/errata-refresh.json`.
Aktuálnost není odvozována pouze z data staršího souboru.
Známé opravy nejsou nové objevy. Konkrétní stránky a výjimky
jsou v kořenovém `review-ui/page-coverage.json`. Použité poznámky
ze svazku 2 mají neměnné kopie a manifest v
`sources/sequential-2026-11-05/accepted-vol2/`.

Přeskočené bibliografické cíle: původní Webster1957 a OED;
lexikon1747 a plný Zemanek1981; přesné historické srovnání
Markov1954/Nagorny1984/1988; původní vydání literárních epigrafů.
Tyto věci se nezapočítávají jako ověřené. Výklad o původu slova
na1–2 zůstává historicky částečný; čistě matematická část jej
nepotvrzuje. Dostupné autorovy opravy dat a znění se použijí.

## Prvních 24 obrazů, včetně předmluvy

Nově přímo přečteny všechny místní obrazy1–24: titulní dvojice,
tiráž, předmluva, postup čtení, obsah a §1.1. Obrazy1/2 jsou již
uloženy v parallel/index-continuation/p636-640;3 a12–24 v images/;
4–11 nově v images/sequential-2026-11-05/. Číslo obrazu není
tištěné číslo:1–15 představují ii–xiv,xviii,xix;16 odpovídá1.

Tiráž souhlasí s inventářem a autorovou stránkou TAOCP; ISBN kontrola
dává vážený součet176, dělitelný11. Na ix je převod úspory mikrosekundy
při bilionu iterací správný: 10^12·10^(−6)/86400 = 625/54 dne,
tedy přibližně11,6. Názory a tehdejší publikační plány v předmluvě
nejsou vydávány za dnešní faktický stav publikací.

Na xii po známé opravě rozsahu stran souhlasí větve s xiii–xiv.
Obě podmínky6 i17 jsou neostré, N<=2 a N<=12; OCR chybně zahazuje
rovnost. Záměrný diagnostický dotaz2+2=5 není tvrzení2+2=5.
Krok18 skutečně tvoří nekonečný návrat. §1.1-5 zůstává správně
vyhodnocenou úlohou o tom, proč tato čtenářská procedura není algoritmus.
Obsah xviii–xix porovnán s dříve ověřeným inventářem51 sekcí;
chybějící tečky jsou známá redakční změna, nikoli matematická chyba.

Původní i,xv–xvii,xx ve skenu chybějí. Starší přijaté porovnání
novějšího vydavatelského náhledu zůstává náhradním podkladem,
nikoli důkazem totožného prvního tisku. Proto celý úvod není uzavřen.

Bibliografické výjimky jsou po stránkách v page-coverage.json.
Na stranách1–2 zůstává navíc nepřezkoumaná část historických tvrzení
uvedená jako partial. Totéž platí pro statistický výrok o převaze
nonnumerického používání počítačů v předmluvěvi. Přeskočení pramene
nezměnilo tyto historické výroky na ověřené.

## Známé opravy znovu přiřazené k původním stránkám

Souhrnný záznam V1-X0931 obsahuje výhradně již zveřejněné opravy:
xii, krok2 (16.7.1997); strana1, rok Lovelace1844→1843
(26.2.2007); strana6, „common divisors“ (2.3.2000); strana8,
argument f tvořený uspořádanou dvojicí (5.8.2000); strana9,
výklad čtenářské procedury (25.12.2010) a množiny vstupůI2
(2.5.2008). Nejde o šest nových chyb ani o šest nových karet.
Odpověď467 má své dřívější záznamy X0023 a C0001 a neduplikuje se.
