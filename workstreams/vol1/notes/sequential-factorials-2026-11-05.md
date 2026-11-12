# Souvislý průchod §1.2.5: permutace, faktoriály a gama

5. listopadu 2026. Přečteny originály 45–52 a odpovědi 480–483,
včetně tabulek, grafu a všech tří důkazů vyšších derivací. Přečteny
celé `factorials.md`, `gamma-functions.md`, `composite-derivatives.md`
a navazující kořenové pramenné recenze. Uložené výsledky
`factorials.json` a `gamma-constants.json` byly porovnány s originálem;
úspěšné výpočty se nespouštěly znovu.

Matematika všech 25 úloh je doložena, ale celé úlohy 4 a 13 zůstávají
partial kvůli konkrétním neověřeným historickým tvrzením. Hlavní text
také zůstává partial. Nedostupné doporučené články se mohou přeskočit;
nevyřešené již zaznamenané historické rozpory se tím nepotvrzují.

## Matematická kontrola

Oba konstrukční postupy pro permutace mají jednoznačné inverze,
takže dávají všechny výsledky právě jednou. Faktoriálové a číslicové
údaje, přesný rozklad 20!, 52!, počet 2568 číslic a 249 koncových nul
1000! souhlasí. Časový příklad 10! milisekund je 3628,8 sekundy;
kniha jej sama označuje za hrubou ilustraci, ne univerzální výkonovou
mez. O Uhlerově historické tabulce to samo nic nedokazuje.

Vzorec pro v_p(n!) počítá jeden příspěvek za každou mocninu p dělící
jednotlivý činitel. Číslicová verze, Wilsonovo párování a Stickelbergerova
kongruence jsou správné; případ p=2 je výslovně ošetřen v důkazu.
Permanent požadované matice s prvky i·j je (n!)³. V originálu nejsou
mocniny i^j, které se objevily v chybném pomocném přepisu.

Eulerova limita vede ke stejnoměrně konvergentnímu součinu pro 1/Γ
na kompaktních množinách. Součin má jednoduché nuly právě v nekladných
celých číslech; Γ tedy mimo své póly nemá nuly. Rekurence, Eulerův
integrál a reflexe byly porovnány včetně oboru a orientace Hankelovy
smyčky. Ta se pro Re(z)≥1 nesmí bez dalšího stáhnout do nuly.

Stirlingovo přiblížení má doložený logaritmický zbytek
0<r_n<1/(12n). Posunuté přiblížení přidané v roce 2019 je rovněž
asymptoticky správné a původní vzorec tím nebyl vyvrácen. Divergence
úplné Stirlingovy řady je odlišná od přesnosti konečných aproximací.
Newtonova řada log Γ(x+1) má doložený reálný obor x>−1;
historický Hermitův pramen se čte ve svém kladném oboru. Není zde
tvrzena konvergence téže obyčejné řady na všech záporných číslech.
Původní (12) obsahuje j≤k, takže dřívější C0005 zůstává dismissed.

Graf Γ má správná znaménka, póly a vyznačené celé hodnoty.
Uložené ven zaokrouhlené racionální intervaly zachycují jediný kořen
ψ v (1,2), obě souřadnice minima i všechna otištěná desetinná místa.
Souhlasí také log10(1000!), příklad 39902 a opravený odhad 40318.

Vyšší derivace byly porovnány přes rozklady množiny, rekurenci
koeficientů a konečné Taylorovy koeficienty. Obrázky výrazů, rozkladů
a krabiček odpovídají těmto bijekcím. Operátorový determinant má
výslovný formální komutativní význam: nejprve se rozvine polynom
a pak se vnější derivace aplikují na w. Předčasné derivování jeho
koeficientů by znamenalo jiný operátor, který se zde netvrdí.

## Historie a bibliografické meze

Přijaty již uzavřené primární kontroly Knoppa, Krampa, Hermita,
Hankela, Legendra, Gausse, Capelliho, Wallise, Stickelbergera,
Arbogasta, Walla, Gooda a Faà di Bruna, v rozsazích přesně uvedených
v jejich kořenových poznámkách. Celé jejich knihy ani články nejsou
znovu prohlašovány za auditované. Přeskočen je nedostupný Dutka1984;
u Toscanovy dodatečné citace zůstává pouze bibliografická identifikace.
Soukromý Prattův návrh zkrácení slova permutations není samostatně
ověřen; na argumentu o počtu permutací nezávisí.

C0087 k roku1682 zůstává candidate: katalogová datace ~1703 sama
nedokazuje, že Leibniz výsledek dříve neznal. C0089 k Eulerovu prvenství
zůstává candidate: Bernoulliho dřívější dopis obsahuje ekvivalentní
limitu, ale Euler zmiňuje předchozí komunikaci. Pořadí objevu z těchto
dopisů samotných neplyne. V UI jsou přesně lokalizovány na původní
strany51 a49, nikoli červeně prohlášeny za potvrzené chyby.

Fakticky otevřené zůstávají Stirlingova údajná neschopnost důkazu,
geografická popularita rohové notace a přesná Wrenchova role, 2,5minuty
a trvání ručního výpočtu Uhlera. Lehmerovo vlastní porovnání1000!
se SWAC je již doložené primární svědectví; nenahrazuje naše přímé
porovnání nepřečtené Uhlerovy celé tabulky266–267. Tyto konkrétní
zbytky zachovávají částečné stránky48,49,51 a480.

Známé opravy X0062–X0066 se nemění. Při mapování X0066 je odlišena
prostá změna přiblížení, doplnění citace a vylepšení popisků od defektu:
jen původní interpunkce (19) na s.50 je přímá chyba tohoto dotisku.
Zbývající smíšené položky X0066 nejsou důvodem barvit s.47–49 červeně.
Všechny čtyři vrstvy errat byly prohledány v dnešních shodných kopiích.
Žádný nový nález se tímto blokem nepotvrzuje. Celá s.52 a483 zůstává
částečná do revize začínajícího §1.2.6.
