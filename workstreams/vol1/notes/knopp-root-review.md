# §1.2.9-21: Knoppův §66 a volba integrační konstanty

Kořenová revize 2. listopadu 2026, V1-X0720. Celá úloha 21 je
nově checked; nález V1-C0012 zůstává confirmed. Dřívější mezera
spočívala v nepřečteném citovaném §66, nikoli v chybějícím vlastním
důkazu. Staré úspěšné matematické testy nebyly opakovány.

Root před změnou evidence ověřil všech 28 souborů, 37500010 bajtů,
a 17 závislostí předání
`parallel/generating-primary-followup/results/knopp-manifest.json`.
Hash manifestu je
`2445ed0c99cdd1a08f6e488554599cb2065f8599a86a8b607be2e1e180be60c8`.
Přečetl celé předání, poznámku, zdrojový protokol a původní vlastní
důkaz `factorial-asymptotic.md`. Přímo obrazově četl titul a rub
Knoppova PDF 7–8, tištěné 537, 544–545, 549–550 a 552 a knižní
95/498. Agentova četba celého §66 na 543–553 je přijata s přesným
rozsahem v jeho protokolu; root ji nevydává za vlastní úplnou četbu.

Tiráž přímo potvrzuje druhé anglické vydání 1951, přeložené ze
čtvrtého německého vydání, a skutečný dotisk 1954. Čtený exemplář
tedy není prvním dotiskem 1951. Název, překlad R. C. H. Young
a nakladatel Blackie & Son v London/Glasgow souhlasí s opravenou
knižní citací. Úplný 583stránkový PDF je uložen v předání;
získání celého souboru není tvrzením o přečtení celé knihy.

Pro x>0 definujme

```text
E1(x)=integral_x^infinity exp(-t)/t dt,
F(x)=exp(x)E1(x).
```

Knoppova definice 301 na 537 požaduje pro každý pevný n>=0
`x^n(F(x)-sum_(j=0)^n a_j/x^j)->0`. V bodě 303.3 na 544
je diferenciální rovnice F'−F+1/x=0 a vybrané řešení s rozvojem
`F(x)~1/x−1/x^2+2!/x^3−3!/x^4+...`. Následující bod na 545
jej dokazuje konečným geometrickým rozvojem v integrálu
`F(x)=integral_0^infinity exp(-u)/(x+u) du`. Zbytek má znaménko
prvního vynechaného členu a menší absolutní hodnotu. Nezaměňuje
se zde divergentní nekonečná řada s integrálem.

Pro knižní z<0 položme x=−1/z. Přesný převod je G_0(z)=xF(x),
nikoli G_0=F. Násobení rozvoje x dává koeficienty n! u z^n.
Obecné řešení Knoppovy rovnice je F(x)+C exp(x), a tedy knižní
obecná funkce je G_0(z)+C x exp(x). Pro C!=0 nemá ani požadovanou
limitu 1 při z->0−. To nezávisle podporuje již přijatý V1-C0012:
asymptotické tvrzení v odpovědi vyžaduje C=0. Úplný vlastní důkaz
včetně odhadu zbytku N!|z|^N zůstává v (A2)–(A4) starší poznámky.

Další přímo přečtená místa 549–550 získávají tutéž funkci z momentů
hustoty exp(−u), tj. jejích integrálů proti mocninám u. Bod 304.3(a)
na 552 používá `integral_0^infinity exp(-u)log(1+u/x) du`;
integrace per partes dává F, protože krajní členy jsou nulové.
Ostatní obecné věty o momentových problémech či sčítání řad tím
nejsou samostatně auditovány.

Čtyři hashované vrstvy errat obsahují sjednocení argumentu E1
z 15. dubna 2002 a bibliografické změny z 9. května 2021
a 29. března 2023. Poslední změna přesně odpovídá získanému
vydání a §66. Žádná z těchto oprav nedoplňuje C=0. Počet nálezů
se nemění; uzavírá se konkrétní pramenná mezera.
