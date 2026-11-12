# Odpovědi466–467 a dodatky A–C — 6. listopadu 2026

Nově souvisle přečteny celé původní466–467 a619–627 a oba obrazy
samostatného Appendix C z2011. Porovnány původní přepisy všech
tabulek, program jejich certifikace, uložené výsledky, obecný
Gaussův důkaz a všechny poznámky k rejstříkům značení a algoritmů.
Čtyři současné vrstvy errat jsou v novém endmatter-errata-extract.json.
Úspěšné numerické běhy se neopakovaly. Nový nález:0.

## Dvě dosud nezapsané stránky odpovědí

466: pět přiřazení provede požadovaný cyklus; první přepis cílové
proměnné vysvětluje minimálnost pěti kroků. F střídá dvě dělení
a testuje nulu před dalším dělením. Řada6099,2166,1767,399,171,57
dává správně gcd57. Čtenářská procedura není konečný určitý
algoritmus. Pro n=5 mají periodické počty dělení2,3,4,3,1
průměr13/5; při pevném m je až na konečný začátek
L(m,n)=1+L(n,m), tedy U_m=T_m+1. Doplňky2014/2017 pouze
zpřesňují již správnou periodickou argumentaci.

467: doslovný přepis s tabulkou b_j,a_j mění exponenty na
(min(m,n),|m−n|); zachovává gcd a snižuje jejich součet.
Prázdný vzor přidává c nalevo, takže pořadí bloků je zachováno.
Znovu přezkoušeny všechny fáze simulačního příkladu, složení
g/h a kladná suma časů j. Podmínka koncovosti2025 se aplikuje
na poslední vzorek každého bloku; složení zůstává platné.

C0001 stále platí: jedno-vstupová metoda je přímo reprezentována
dvěma kopiemi téhož vstupu/výstupu, ale množiny vstupů nejsou
bijektivní. Nezaměňujeme nesymetrickou reprezentaci s její
ekvivalenční obálkou. Vadná je předběžná charakterizace pomocí
izomorfních funkcí, nikoli důkaz tranzitivity. Stejný protipříklad
je veřejný od2019; nejde o nový objev. Přesná červená lokace je467.
Známé změny X0023 jsou na téže straně samostatně evidovány.

Rychlá bibliografie466: [vydavatelský obsah Annals141/3](https://www.jstor.org/stable/i310703)
potvrzuje Wiles1995,443–551; obsah článku se tím znovu neprokazuje.
[Folger, IV.1](https://www.folger.edu/explore/shakespeares-works/the-merchant-of-venice/read/4/1/)
potvrzuje slova citátu i Shylocka. Jeho číslování má66, kde TAOCP
uvádí65; bez identifikace použitého vydání nelze rozdíl číslování
považovat za knižní chybu. Přesná edice/řádek65, LeVeque1956ch3,
Ribenboim1979 a Floyd–Beigel1994§3.3 se výslovně bibliograficky
přeskakují. U466 se přidává pouze značka řady Annals(2) a
odpověď na novou úvodní otázku; není zde nová matematická chyba.

## Appendix A

Vstupní přepis souhlasí s původními tabulkami619–621; tři
zaznamenané opravy OCR nejsou opravami knihy. Arb certifikát
pro každý řádek prokazuje0<sign*(hodnota−tisk)<1/(2*b^d).
Tím jsou doloženy všechny číslice i směr zaokrouhlení34
desítkových a44 osmičkových čísel. Kontrola mpmath je pomocná;
certifikace pochází z intervalů, nikoli shody dvou aproximací.
Přečtený kód používá přesné racionální vstupy a derivaci zeta
z mocninné řady. Uložený úspěšný výsledek se neopakoval.

Všech93 hodnot H_n/B_n/F_n je ověřeno racionálními rekurencemi.
Původní B1=−1/2 i generující funkce z/(exp(z)−1) jsou vzájemně
správně. Změna2021 přidává ke generující funkci z, takže mění
pouze B1 na+1/2. Není to obsahová chyba původní tabulky.
Oznámený záměr nahradit osmičkovou soustavu šestnáctkovou není
oprava číslic ani důkaz již vydané nové edice.

622: řada pro H_x absolutně konverguje mimo záporné celočíselné
póly. Fráze „for any x“ se čte v definičním oboru výrazu;
všechny následující argumenty jsou v(0,1). Filtr kořenů jednotky,
spojitá větev logaritmu a párování k/q−k dávají uvedený obecný
vzorec; sudý prostřední člen je nula. Pětiny vyplývají přesně
z poměru sin(2π/5)/sin(π/5)=phi a součinu sqrt(5)/4;
obě znaménka kotangenty i sqrt(5)ln(phi) v tabulce souhlasí.
Všech11 specializací je rovněž součástí starého certifikátu.

Odkaz621 na konstantu v§1.3.3-23 je správný a její40 číslic
i plus již samostatně certifikuje přijatý interval s poloměrem
2.07e−73, viz sequential-permutations-2026-11-05.md.
Historické tvrzení o Wrenchově výpočtu a kontrole v70. letech
nové krátké hledání nedoložilo.621 i celý Appendix A zůstávají
partial právě pro tuto historii, nikoli pro neověřené číslice.
Levé okraje části odstavce621 jsou ve skenu oříznuté; nevyvozuje
se z toho typografická chyba tištěného exempláře.

## Appendix B

Všech105 původních hesel623–627 i nová suma znovu porovnány
s přijatou kontrolou cílů a matematickými definicemi. Stoupající
a klesající faktoriály používají opačné posuny pro záporný řád;
gamma podíly se čtou jako pokračování příslušného výrazu,
nikoli samostatné dělení dvou nedefinovaných čísel v pólu.
Oba Stirlingovy součty mají správně ostré/neostré indexy
a standardní prázdné kombinatorické případy. Multinomický
vzorec2024 je správný pro uvedené nezáporné počty se součtem n.
Mod0=x, znaménko nuly a Fibonacciho počátky souhlasí.

U variance je E[X(X−1)]=g''(1), proto správně
var=g''(1)+g'(1)−g'(1)^2. Součet EX odkazuje na diskrétní
výklad; neúplný gamma integrál se čte v oboru konvergence.
Zkrácený rejstřík není náhradou podmínek příslušných sekcí.
Následníci/předchůdci tří průchodů i převod obecného postorder
na binární inorder odpovídají původnímu výkladu337.
MIX/MIXAL registry, pole, lokální symboly a koncová značka
souhlasí s již prověřenými sekcemi.

Skutečně chybné původní cíle jsou jen delta624:1.2.6→1.2.3
a exp626:1.2.2→1.2.9. Ostatních pět změn X0551 jsou doplnění,
notace a označení sekcí; nepřibarvují původní stránky červeně.
Mezisvazkový odkaz na přibližnou rovnost byl již přímo ověřen
na Vol2/233; není tím předem uzavřena matematika celé§4.2.2.

## Appendix C a mapa prvního dotisku

Přijato ověření137 původních a6 dodatečných položek s159
různými cílovými stranami. Znovu přečteny oba obrazy přílohy
a úplná poznámka k výjimkám: pokračování programů, varianty
označené jen změnou kroku, implementace algoritmu v jiné sekci,
přejmenování na534 i opravy B'/B'',G,H/Z. Shoda názvu a cíle
není nové potvrzení správnosti vadného algoritmu v cílovém textu.
Přijatý Mallatův citát je doložen přetiskem původní předmluvy
v1999; přesný tisk1998 se znovu bibliograficky nekontroluje.

Appendix C vznikl až2011. Jeho628–629 nelze přiřadit jako chybu
k našim původním628–629, na kterých už začíná hlavní rejstřík.
X0593 proto zůstává oddělená evidence oprav pozdější přílohy.

Stránky466–467,619–620,622–627 jsou reviewed;621partial.
Přímé vady jsou467,624,626. Další krok: původní rejstřík628–650.
