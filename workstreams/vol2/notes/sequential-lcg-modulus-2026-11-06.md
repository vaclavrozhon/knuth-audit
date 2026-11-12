# Souvislý průchod §3.2 až §3.2.1.1

6. listopadu 2026, V2-X0085–X0086. Přečtena původní sazba str. 10–16
a odpovědi 543–547; poslední odstavec na 16 a odpovědi následující sekce
na 547 budou uzavřeny s §3.2.1.2. Strana 543 je nyní přečtena celá
včetně dříve prověřené odpovědi §3.1-23. Inventář souhlasí: 5 a 14 úloh,
bez přidaných úloh v erratech.

## Matematika a instrukční postupy

Celé poznámky `linear-congruential-intro.md`, `C0004-inverse-lcg.md`,
`modulus-arithmetic.md`, `carry-generators.md` a
`C0005-borrow-periodic-extension.md` byly znovu porovnány se sazbou.
Přečteny také celé validátory tabulky, modulární aritmetiky a přenosů;
jejich uložené výsledky byly převzaty bez nového spuštění.

| Rozsah | Přijatá kontrola |
|---|---|
| 10–11, §3.2.1-1 až 5 | Afinní iterace, geometrický součet před redukcí, pomocná posloupnost Y, permutace pro jednotkový násobitel, obraz velikosti m/gcd(a,m), jediný konečný pevný bod pro sudé a modulo 2^e. |
| 12–13, programy (1),(2) | Dolní polovina součinu modulo w; rozdíl r−q modulo w+1; přetečení právě při výsledku w, je-li původně vypnuté; varianta vynechávající w skončí nejvýše po druhém násobení. |
| 13, dolní cifry | Projekce modulo d dělící m je kongruenční generátor. Pro lichý násobitel modulo 2^e je nejnižší bit konstantní nebo střídavý. Obecný sudý násobitel může mít krátký ocas. Statistická doporučení nejsou zárukou pro libovolnou volbu parametrů. |
| 14 | Všech 92 přepisů rozkladů porovnáno s tabulkou. Přijaté přesné součiny a rekurzivní Lucasovy certifikáty 179 prvočísel; kód validátoru zkontrolován. |
| 15, 543–544, úlohy 1–8 | Předpočtený přírůstek, návrat RANDM a nulování overflow, redukce pomocí polovin součinů, dvojkový i jedničkový doplněk, bezpečné pořadí sčítání/odčítání, rozklady z^n±1. |
| 16, 544–545, úlohy 9–11 | Schrageova redukce, nutnost i postačitelnost r≤q, přesný počet vhodných násobitelů, konstruktivní mez 12 operací včetně malých modulů, oba konkrétní rozklady násobitele 62089911. |
| 16, 545–547, úlohy 12–14 | Ciferné rotace, obecná identita bX_(n+1)=X_n+|m|x_n, invariant přenosu a radixový rozvoj, obě varianty odčítání, add-with-carry. Prvočíselný příklad a přesný řád přijaty s certifikáty; spektrální argument v rozměrech 2 a 3. |

Mez dvanácti násobení/dělení je dokázána. Následná otevřená otázka,
zda vždy stačí jedenáct, není tím vyřešena. Dříve uložený manuál TRNG
znovu přečten v příslušném odstavci; uvádí tutéž horní mez, což samo
nedokazuje optimalitu ani dnešní neexistenci lepšího výsledku.

## Dva znovu potvrzené nálezy

**C0004, str. 543:** pro m=8,a=3,c=1,b=2,a′=3 a X₁=1 dává
druhý inverzní řádek 4, první správně 0. Podmínka aa′≡1 modulo m
neumožňuje po dělení b zachovat kongruenci. Silnější inverze modulo
mb existuje a druhý řádek opravuje. Dodatek „if b=a−1“ z roku 2003
nedostačuje. Protipříklad používá pouze celá dělení.

**C0005, str. 546:** x₋₁₀=2, ostatní počáteční cifry 0 a b₀=1
splňují X₀=1. Periodické předefinování pouze záporných indexů změní
x₋₁₀ na 1, ale b₀ zůstane 1. Rekurence by pak požadovala x₀=0,
přestože bylo vygenerováno x₀=1. Hlavní radixový závěr je pravdivý;
chybný je pomocný krok důkazu. Není třeba vypisovat velkou periodu.

Oba nálezy jsou v původní knize, nikoli pouze v erratech. Jejich karty
nově odkazují přesně na původní strany 543 a 546. Nový matematický
nález v tomto průchodu nepřibyl. Fyzický novější dotisk ani prvenství
nálezů ověřeny nejsou.

## Veřejné opravy a přesné červené stránky

Všechny čtyři řady errat, jejichž aktuálnost byla potvrzena dnešním
stažením, byly prohledány pro 10–16 a 543–547. Původní sazba
`all2-prepre` str. 30 byla znovu zobrazena.

Položka **X0086** mapuje již zveřejněné opravy původního tisku:

- str. 12: nesprávný odkaz na úlohu 3 odstraněn 26. 10. 1998;
- str. 16: nadbytečné „to“ v zadání 9 opraveno 29. 12. 1997;
- str. 546: mocněnec 9999999000→999999900 (2010), znaménko
  výpůjčky +→− v 12(e) a indexy výpůjček v 13 (2007), budoucí cifra
  n−1→n+1 v 13 (1999), nadbytečné slovo (2002);
- str. 547: j-tý ciferný blok musí končit x_(n−j), nikoli x_(n−k),
  oprava 1. 12. 2007. Obecný invariant potvrzuje právě opravený vzorec.

Upřesnění overflow na 13 z roku 2011 není samo protipříkladem původní
věty, která předpokládá vypnutý vstupní příznak. Prohození násobitelů
na 545 v roce 2024 zachovává správnost obou pořadí a samo nezakládá
červenou stránku. Upřesnění „modulo m“ v odpovědi 3 a definice nejmenšího
kladného λ v odpovědi 14 jsou zapracovány. Tyto rozdíly nepřevyprávíme
jako nové matematické chyby.

## Fakta a bibliografické výjimky

Znovu přečteny uložené primární výňatky manuálů DEC (1982, 1–20/1–21
a MUL) a IBM System/370 (1975, MULTIPLY, 136): rozdíl 35 versus 32 bitů
v dolním slově součinu odpovídá textu na str. 15. Prověřena specifikace,
nikoli běh na historickém hardwaru. MIX je kontrolován matematickou
sémantikou instrukcí a předchozím porovnáním s prvním svazkem.

Rychlé vyhledání poskytlo adresy primárních článků Lehmera, Thomsona
a Rotenberga, ale jejich přímé otevření skončilo timeoutem či blokací.
Tyto tři úplné články, přesné datování původního návrhu a historická
priorita jsou proto výslovně přeskočeny; agregované bibliografie nejsou
náhradou primárního dokladu. Totéž platí pro zde citované články
Marsaglii–Braye, Wichmanna–Hilla, Marsaglii–Zamana a Tezuky a kolegů.
Matematické postupy z těchto míst jsou doloženy vlastními důkazy.

Další kurzor: §3.2.1.2 od str. 16, věty o maximální periodě.
