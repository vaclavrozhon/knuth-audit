# Kandidát: společný příklad §2.3-11(b),(c) má jedinou kardinální úroveň

Kořenový stav při předání: **V1-C0045, candidate**. Globální ID přidělil koordinátor; lokální dočasné označení a níže zachovaná historie revize slouží návaznosti evidence.
Stav: **candidate**, připraveno k nezávislé revizi. Nejde o závěr o prvenství nálezu. Tištěné 317, 561–562 prohlédnuty celé. Vrstvy all 1-prepre, all 1-pre, all 1, err 1 prohledány podle 317/561/562 a tématnested, level, Bigelow, uncountable, cardinal; příslušné původní PDF a aktuální TeX přečteny. Známé opravy odpovědi 11 jsou 0→prázdná množina(2001) a upřesnění proper ancestor/descendant(2010), nikoli následující věc.

## Přesné rozlišení dvou výroků

Zadání 317(b) požaduje uzly s nespočetnou úrovní; 317(c) požaduje stupeň alespoň 2 všude a nespočetně mnoho úrovní. Odpověď 562 definuje úroveň uzlu X jako kardinální počet jeho vlastních předků: `level(X)=|ancestors(X)|`. Množina různých úrovní je tudíž `Levels(C)={level(X): X in C}`. Splnění(b) znamená existenci X s nespočetným level(X); přirozené doslovné splnění(c) znamená, že Levels(C) je nespočetná. Tyto vlastnosti nejsou totožné.

Označme `c=|R|`, mohutnost kontinua. Tištěná konstrukce používá, pro 0<a<1 a celá n>=0, 0<=m<2^n,

```text
S[a, m, n] = {(a, y): m/2^n <= y < (m+1)/2^n},
T[a]     = {(x, y): x <= a},
C        = {S[a, m, n]} union {T[a]}.
```

Vlastní předkové jsou podle definice právě přísné nadmnožiny z C.

- NadmnožinyT[a] jsou přesněT[b] s a<b<1. Je jichc: neprázdný reálný interval(a, 1) je v bijekci sR. ŽádnéS[b, m, n] neobsahuje celou polorovinuT[a]. Protolevel(T[a])=c.
- NadmnožinyS[a, m, n] zahrnují přesněT[b] s a<=b<1 a jeho n přísných dyadických nadintervalůS[a, floor(m/2^(n-j)), j], 0<=j<n. Jiná svislá přímka je disjunktní a jiné dyadické intervaly na stejné přímce jsou buď nadintervaly, podintervaly, nebo disjunktní. První skupina má c prvků, druhá je konečná. Protolevel(S[a, m, n])=c+n=c.

Tedy **Levels(C)={c} a |Levels(C)|=1**. To není jen chybějící důkaz, nýbrž přímý výpočet všech úrovní navrženého příkladu podle jeho vlastní definice.

Ostatní části této konstrukce jsou správné. Kolekce je vnořená. KaždéS má dvě dyadické děti, které tvoří dvě komponenty potomků. PotomciT[a] mají dvě komponenty: dyadické intervaly na x=a, a kolekci s indexy b<a; druhá nemá nejvyšší prvek, ale zůstává jedinou komponentou díky hustotě reálných indexů. Stupeň je tedy 2, ačkoliT[a] má jen jedno bezprostřední dítěS[a, 0, 0]. Každý uzel má nespočetně mnoho předků. Konstrukce proto skutečně splňuje(b) a také slabší interpretaci(c): stupeň alespoň 2 a existence uzlu s nespočetně mnoha předky.

## Meze závěru a oprava

Kandidát závisí přesně na tom, že „nespočetně mnoho úrovní“ znamená nespočetně mnoho různých hodnot právě definované funkce level. Pokud má znamenat neformálně nespočetně dlouhou hierarchii nebo nespočetný řetězec předků, navržený příklad ji má; pak je potřeba vyjasnit formulaci a neslučovat ji s kardinální funkcílevel. Netvrdím, že samotná vnořená konstrukce je chybná, ani že úplně jiné řešení původního(c) neexistuje.

Nejmenší místní oprava je změnit(c) na požadavek, že každý uzel má stupeň alespoň 2 a nespočetně mnoho předků (případně nespočetnou úroveň). Tím se tištěný příklad stává řešením přímo podle uvedených definic. Pouhé nahrazení slova cardinal slovem ordinal nepomůže původnímu hustému řetězciT[a]: jeho předkové nejsou dobře uspořádáni v pořadí odshora dolů.

Konečné testy nemohou dokázat rozpor kardinálních počtů a nebyly použity.

## Samostatný dodatek: poznámka o dobrém uspořádání

Původní obraz 562 byl znovu prohlédnut. Poznámka zachovává indexy a dyadické množiny předchozí konstrukce a nahrazuje pouze T výrazem `T[a]={(x, y): x ≻ a}`. Tvrdí, že vhodné dobré uspořádání dovolí každému uzlu nespočetnou úroveň, stupeň 2 a dvě děti.

Při obvyklém čtení, že `≺` je dobré uspořádání a `≻` jeho opačná relace, jsou T koncové úseky. Neprázdná množina použitých indexů I má nejmenší prvek a0. Žádné jiné T není přísnou nadmnožinou T[a0]; žádná jediná svislá dyadická množina S ji také nemůže obsahovat. Proto má T[a0] úroveň 0, nikoli nespočetnou. Přesné rozmístění obvyklého intervalu I=(0, 1) v dobrém uspořádání na tomto argumentu nic nemění. Pokud by T[a0] bylo prázdné, navíc porušíme základní požadavek neprázdných množin.

Ani opačný význam symbolu tento úplný výrok nezachrání: pokud T[a] označuje počáteční úsek před a, nejmenší použitý index a0 nemá pod sebou žádné T[b] ani S[b, m, n] s b v I. Uzel T[a0] má tedy stupeň 0 (nebo je sám prázdný), nikoli stupeň 2. Tento dodatek se týká doslovné deklarované změny, bez dalších neuvedených odstranění uzlů či změn indexové domény.

Silnější vlastnost zamýšlená poznámkou přesto existuje, pouze nepotřebuje dobré uspořádání. Vezměme indexy I=R×Z s lexikografickým pořadím a nahraďme T[a] počátečními úseky zahrnujícími a. Každý a má bezprostředního předchůdce a^-=(r, k-1) a bezprostředního následníka. T[a] má právě děti T[a^-] a S[a, 0, 0]; S má dvě obvyklé dyadické děti. Každý uzel má kontinuum předků T[b]. Vnořená kolekce tak má stupeň 2, dvě děti a nespočetnou kardinální úroveň všude. Celý podklad I×R má mohutnost kontinua, takže jej lze převést na podmnožiny R stejně jako v původní odpovědi. Ani tato opravená konstrukce však nemá nespočetně mnoho *různých kardinálních úrovní*: všechny jsou stále c.
