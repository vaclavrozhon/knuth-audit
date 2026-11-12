# §1.2.4: původní prameny celých částí

Kořenová revize 2. listopadu 2026, V1-X0714–X0715. Celá úloha 38
a historické citace hlavního textu jsou nově checked. Úlohy 40 a 49
zůstávají partial v níže uvedeném pramenném rozsahu. Nový nález
nevznikl; dříve přijaté matematické testy se neopakovaly.

Před změnou evidence root ověřil délky a SHA-256 všech 80 souborů,
84763639 bajtů, v `parallel/floor-source-followup/MANIFEST.json`.
Hash manifestu je
`32677e362bb0b03b2509648ab29aa6a8e395b36d39c2dad8a717d41d3e92f25f`.
Souhlasí také všechny čtyři hashované textové vstupy errat.
Root přečetl celé předání a všechny čtyři agentovy poznámky;
balík zůstává zmrazený.

## Přímá kořenová četba a převod úlohy 38

Root obrazově přečetl knižní 39, 41, 43 a 478; Buscheho 39, 42–43;
Hermiteho 297, 310–312, 314–315 a celou opravu z roku 1886.
Širší agentova četba je samostatně popsána v jeho HANDOFF; stažení
celých PDF neznamená přečtení celých článků.

Pro reálné t značí floor(t) největší celé číslo nejvýše t a ceil(t)
nejmenší celé číslo nejméně t. Buscheho definice [t] na 39 odpovídá
floor. Jeho formule na 42, pro kladné celé a a 0<alpha,beta<1, je

```text
sum_(j=1)^a floor(j/(a+alpha)+beta)
  = floor((a+alpha)*beta+1-alpha).
```

Případ alpha=1 je výslovně zahrnut koncem 42 a na 43. Pro knižní
y>1 položme m=ceil(y), a=m−1, alpha=y−a a x=q+beta, kde q=floor(x)
a 0<=beta<1. Přidání členu j=0 a posun o q dávají na obou stranách

```text
q*m + floor(beta*y+m-y)
  = floor(x*y+floor(x+1)*(ceil(y)-y)).
```

Pro beta=0 jsou oba normalizované součty nulové. Pro 0<y<=1 je
jediný sčítaný člen floor(x) a 0<=beta*y+1-y<1. Tím převod zahrnuje
všechna reálná x a všechna y>0. Obecný důkaz celé identity již
obsahuje `notes/floor-sums.md`.

Hermite na 315 přímo uvádí
`E(x)+E(x+1/m)+...+E(x+(m−1)/m)=E(m*x)` pro kladné celé m.
Koeficientové počítání na 311 určuje E jako celou část pro
nezáporné argumenty; pomocná konvence pro záporné indexy se nesmí
bez dalšího ztotožnit s floor na celé ose. Rozšíření této konkrétní
identity na záporná x plyne celočíselným posunem. Autorská Correction,
datovaná 19. března 1886, mění sousední váženou identitu pro E_2,
nikoli citovanou formuli pro E. Datum tisku Acta 3. září 1884 je
přímo na první straně článku. Obě citace tedy odpovídají knize.

## Iverson a Fermat v hlavním textu

Root přímo četl Iversonovu copyrightovou stranu a celou stranu 12:
oba znaky, názvy, definice a příklady floor/ceiling souhlasí.
Exemplář má copyright 1962 a čtvrtý tisk v květnu 1967. Dokládá
proto knižní šedesátá léta; nepředstíráme četbu prvního tisku.
Agent navíc četl titul a sousední 11. Tím je konkrétní atribuce
na knižní 39 uzavřena bez tvrzení o vyčerpávající rešerši veškeré
starší notace.

U Fermata root přímo četl titul edice korespondence 1894, záhlaví
dopisu XLIV na 206 a celý rozhodující §4 na 208–209. Dopis
Frénicleovi je datován 18. října 1640. Pro prvočíslo p a celé a,
které p nedělí, uvedené tvrzení o nejmenším exponentu d dělícím
p−1 dává a^(p−1)=1 modulo p. Podmínku p nedělí a výslovně doplňuje
editorská poznámka. Vynásobením a a připojením případu p dělí a
dostáváme přesně knižní a^p=a modulo p. Dopis větu sděluje bez
důkazu; není zdrojem knižního důkazu permutací nenulových zbytků.
Agentovu zmínku o „indukčním důkazu“ v jeho poznámce proto root
nepřebírá. Čtena byla sazba korespondence, nikoli autograf ani
ověřený první veřejný tisk dopisu.

## Zbývající mezery

Dosud nebyly přečteny Mordellovy 371–375 z JLMS 33 (1958)
ani Eiseleho–Hadelerovy 475–477 z AMM 97 (1990). Nové přístupové
pokusy a bibliografická metadata tyto konkrétní stránky nenahrazují.
Yoderův a Hamelův dříve přijatý odkaz zůstává oddělený. X0055 je
proto zúženo na tyto dvě mezery; celé 40 a 49 se neuzavírají.

Všechny čtyři vrstvy errat jsou porovnány v agentově
`notes/scope-and-errata.md`. Známé opravy celočíselnosti hodnot,
chybějícího i a pozdějšího označení řady časopisu zůstávají
známými opravami. Původní tisk 1997 má Mordellův ročník správně.
Zdrojová URL a přesné rozsahy jsou v přijatém `SOURCES.json`.
