# Souvislý průchod §1.2.11 — 5. listopadu 2026

Přímo přečten celý původní rozsah 107–123 a odpovědi 502–507,
soubor 122–138 a 517–522. Sousední obsah §1.2.10 na 107/502 je
uzavřen v X0944. Na 507 začíná MIX; tato část ještě čeká na další
blok. Přečteny všechny níže uvedené matematické poznámky a přijaté
pramenné recenze. Nový nález nevznikl. Uložené výpočty se neopakovaly.

## X0945: O-notace a všech 13 úloh

Přečteny `asymptotic-notation.md`, `asymptotic-factorial-powers.md`
a `asymptotic-notation-scope.md`. Kontrola zahrnuje jednostranné
množinové rovnosti, nezávislost jednotlivých O-symbolů, jednotnost
konstant při sčítání rostoucího počtu členů, komplexní odhady v nule
a všechny případy m=0. U logaritmu je nutné m>0 a pevná větev.
Exponent a v binomickém rozvoji je pevný; nenulovost děleného faktoru
v (10) je známá oprava 2022, nutná i na konečném počátečním úseku
při doslovném množinovém výkladu funkcí.

Beta integrál dokazuje oba faktoriálové rozvoje pro každé pevné
reálné r a libovolný konečný řád. Divergence v úloze 12 není jen
numerická: předpoklad nulové limity členů by vedl k celistvému
pokračování G a identitě (exp(z)−1)G(z)^2=z exp(z), která v 2πi
dává spor. Knižní faktor je padající faktoriál, nikoli obyčejná mocnina.
V odpovědi 9 doplňujeme krok |exp(w)−1|<=|w|exp(|w|); pouhý horní
odhad modulu exp(w) by vzdálenost od 1 nedokazoval. Opravená věta
je pravdivá, nevytváříme z tohoto doplnění nový nález.

Bachmannův originál 1894, titul a 401–402, je přijat v přesném
rozsahu X0127. X0126 mapujeme na původní 108,109,503: chybějící
n v polynomu, obor nenulového faktoru, „all value“, argument f(z),
absolutní hodnota a (k−1)! místo (n−1)!. Vysvětlení výslovnosti
Eulerova jména na 107, zkrácení „Theta notation“ a povolení jiného
základu logaritmu na 110 nejsou samy původní matematické vady.
Všech 13 úloh i hlavní oddíl již byly checked; počty se nemění.

## X0946: Eulerův sumační vzorec a všech 9 úloh

Přečteny `euler-summation.md`, `euler-applications.md`,
`euler-products.md`, `euler-errata-and-scope.md`,
`euler-summation-originals.md`, `kinkelin-glaisher-root-review.md`,
`euler-primary-root-review.md` a `concrete-citations-root-review.md`.
Uložených 1915 kontrol je přijato jako doplněk obecných důkazů.
Interval konstanty A=[1.2824271291005600,1.2824271291006229]
souhlasí s tištěnými číslicemi; nebyl znovu počítán.

Obě Bernoulliho konvence jsou konzistentní, ale vyžadují jiné krajní
členy součtu. Samotné Bernoulliho polynomy zůstávají stejné.
Integrace po částech probíhá po jednotkových intervalech; spojitost
periodických polynomů od indexu 2 ruší vnitřní hraniční členy.
Fourierův odhad a kladné periodické jádro dokazují velikost i znaménko
zbytku včetně ostrosti za podmínek (13). První vynechaný člen je
první nenulový člen. Nulové derivace a nulový interval se nezaměňují
za ostrou nerovnost. Odhady pro H_n, log(n!), Stirlingův vzorec
i reálný argument gama funkce mají vlastní odhad chyby.

Součty mocnin zahrnují m=0 a 0^0=1. Hyperfaktoriál má správnou
konstantu A a oba její výrazy přes zeta; funkcionální rovnice je
přijatá analytická věta s dohledaným pramenem. Kvadratický argument
an²+bn předpokládá a>0, případ a=0 je oddělený režim. Poměr
binomických koeficientů ověřují dvě nezávislá odvození. Obecná
dyadičnost koeficientů centrálního binomického rozvoje plyne z
celočíselné Newtonovy báze Stirlingových polynomů, nikoli z pár
vypočtených koeficientů.

Euler E25/E47, původní Bernoulliho tabulka, Sekiho tisk1712,
Kinkelin, Glaisher, Steffensen, de Bruijn§3.7 a CMath§9.5 jsou
přijaty jen v rozsazích již doložených recenzí. Přesné Sekiho
Collected Works1974,39–42 a řešení Knuth–Vardi, AMM97(1990),629–630
se podle zadání přeskakují. Matematika má úplné nezávislé důkazy.
Hlavní text a poslední úloha9 se s těmito výjimkami uzavírají;
X0135/X0690 nadále zachovávají neověřený obsah těchto pramenů.

X0134 mapujeme na skutečné původní vady na 112,114,116,503,504:
označení Bernoulliho čísel za koeficienty bez faktoriálového dělení;
argument derivace, znaménko integrálu a absolutní velikost zbytku;
závorky a interpunkce; počáteční polynom v odpovědi2; rok Steffensena;
chybějící (ln a)/2 a závorky odpovědí8/9. Samotná změna konvence2021,
redundantní (−1)^m pro sudé m, názvy a rozšíření vysvětlení nejsou
automaticky původní matematické chyby. Kinkelinův chybný rozsah
122–158 byl vložen až pozdější opravou, v originálu není.

C0082 zůstává bibliografickým kandidátem výhradně k erratu2021.
Aktuální přímý render all1-pre8 skutečně uvádí 8(1735),9–22,
zatímco přijatý titul má ročník1736 a tisk1741. Původní111 E47
vůbec necituje; v mapě je proto pouze související místo, nikoli
původní chyba. Datační konvence není dořešena.

## X0947: asymptotické výpočty a všech 20 úloh

Přečteny `asymptotic-gamma.md`, `asymptotic-parameters.md`,
`asymptotic-sums.md`, `asymptotic-findings.md`, `ramanujan-bound.md`
a `asymptotic-calculations-scope.md`. Přijaty také recenze Cauchyho,
Tricomiho, Carlitze, Barnese–Watsona, Ramanujanových originálů,
Furche, de Bruijnových metod a přesných mezer Demuth/Gould/Rousseau.
Výsledek 51 symbolických kontrol a Ramanujanův certifikát 147 kontrol
byly přečteny. Kladné koeficienty obou polynomů po posunu n=t+128
zajišťují nekonečný ocas; 127 racionálních intervalů pokrývá menší
n. Konečné vzorky se nevydávají za důkaz všech n.

Neúplná gama funkce, její dvě řady a přesná vazba Q+R jsou správné.
Lokální analytická inverze a Watsonův argument oddělují malý úsek
od exponenciálně zanedbatelného ocasu. Integrál I_2 vyžaduje pro
záporné y odhad na |u|<=|y|; tuto výhradu nelze nahradit pouhým
intervalem 0<=u<=|y|. Výsledný Theorem A pro obě znaménka y platí.
Pohyblivé horní meze v úlohách7–10 mají správné jakobiány a orientaci.
Watsonovo lemma pokrývá i podmíněně konvergentní vzdálený ocas,
pomocí omezené primitivní funkce, bez dodaného předpokladu absolutní
konvergence. Parametrické Q_x/R_x mají všechny reálné větve a
rovnoměrné zbytky po níže uvedené opravě.

V diskrétních součtech se zvlášť kontrolují lokální okno, oba ocasy,
jednotnost Stirlingovy chyby a Eulerovy koncové členy. Necelé t
v úloze14(d) vyžaduje odečíst mocniny s nedostatečnou hladkostí u nuly; vysoké
derivace x^t tam nelze bez vysvětlení předpokládat. Vlastní argument
v poznámce toto doplňuje. Všechny koeficienty P,Q,R,S souhlasí.
Konečné diference a Abelova/Cauchyho identita mají obecné důkazy
i pro nulové základny s exponentem0. Odpověď14 nechybí omylem:
samotné pětidílné zadání tvoří řešení.

Ramanujanův důkaz kontroluje také analytickou větev logaritmu,
celý obrys a konstanty. Dvě chyby koeficientu v citovaném článku1995
jsou zaznamenány ve vlastním certifikátu; nejsou to nové vady TAOCP.
U Temmeho, Odlyzka, Kellerové a Knuthovy vlastní vzpomínky se
přijímá dosavadní přesný rozsah. Konkrétních65 příkladů Odlyzka
bylo inventarizováno; jejich vlastní důkazy se tím neprohlašují
za auditované.

Bibliograficky se přeskakují Demuth1956,67–68 (obsah vedoucího
členu P nebyl přečten), Gould1968,1019–1021 (citovaná bibliografie),
Rousseau1989,159–161 a přesná kolace de Bruijna1961 proti přečtenému
vydání1958. Nejsou tím ověřeny ani vyvráceny tyto konkrétní atribuce.
Hlavní text a poslední úloha20 se podle zadání uzavírají s výjimkami;
X0143/X0769/X0775/X0782 zachovávají neověřené zdroje. Přijaté
historické atribuce nejsou vyčerpávajícím důkazem světového prvenství.

## Čtyři původní nálezy a přesné lokace

- C0016, odpověď4 na505: 1+1/u jde k1, nikoli0. Odhad ocasu
  zůstává platný; závažnost UI opravena z medium na low.
- C0017, odpověď8 na505: symetrický integrál u^(m+1) se pro sudé
  m ruší. Při f=1,r=0,s=2 je skutečný rozdíl kladný. Nutná je
  absolutní hodnota |u|^(m+1); závěr úlohy je správný. Medium.
- C0018, odpověď11 na506: při x=−4 dává přesná identita střídavý
  exponenciální růst místo limity1/5. Pro x<0 je třeba doplnit
  n!x^(n−1)exp(n/x)/n^n. R_x zůstává správně. High.
- C0019, odpověď12 na506: normální integrál je lichý; chybí sgn(x).
  Zadání122 bez omezení x je řešitelné a není samo chybnou formulí.
  Červenou lokací je odpověď506, ne celé zadání. Medium.

X0948 soustřeďuje již známé opravy této části, dříve evidované
uvnitř checked bloku X0144. Původní vady jsou na118 (větev a odkaz),
119 (interval pro záporné y),121 (16/8505),505 (x^x),506 (závorky
jmenovatele) a507 (faktor k). Indexování 0<=k versus k>=0 není
nová chyba. Nová karta známých oprav nepřidává neznámý nález.

Aktuální all1-pre8–11 a all1 7 byly přímo vykresleny z dnešních
stažených PostScriptů a přečteny. Manifest
`sources/sequential-2026-11-05/asymptotic-current-images.json`
uchovává zdrojové i obrazové hashe. Ostatní vrstvy jsou pokryty
přijatými výtahy a dnešním ověřením shody zdrojů.

Po bloku: 861/932 původních úloh uzavřeno,71 partial;18/51 hlavních
oddílů uzavřeno. Dvě nové uzávěrky úloh jsou přesně bibliografické
výjimky výše. Původní nálezy a kandidáti zůstávají od těchto ukazatelů
oddělené. Další souvislý blok začíná §1.3 na124.
