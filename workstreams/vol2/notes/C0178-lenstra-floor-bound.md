# V2-C0178: zaokrouhlení ruší pomocnou mez v L1

Stav **confirmed** pro pomocné tvrzení v §4.5.4-42,
odpověď667, krokL1. Netvrdíme, že samotná podlaha způsobí
nesprávný výsledek algoritmu po opravě C0177.

Pro N=36,r=1,s=5 jsou splněny všechny předpoklady zadání.
Máme r'=1,u=1,v=5,w=2 a theta=floor(sqrt(36/5))=2.
Dvojice lambda=mu=1 splňuje

```
(lambda*s+r)(mu*s+r')=6*6=36,
lambda*u+mu=2=w (mod 5).
```

Přesto sqrt(lambda*mu*v)=sqrt(5)>2=theta. Přesně tato
nerovnost je v L1 tištěna s opačným výsledkem.

Náhrada floor hodnotou ceil obnoví tvrzení a umožní
obecný důkaz algoritmu beze změny asymptotické časové meze;
viz [lenstra-residues.md](lenstra-residues.md), (L1)–(L5).
Je to konzervativní oprava. Nenárokujeme její nezbytnost
pro funkčnost algoritmu: na tomto protipříkladu i ve všech
293751 malých testech stačila původní podlaha, když byl
opraven jmenovatel mu. Obecná správnost takové varianty
není zde dokázána ani vyvrácena.

Originál667 vizuálně včetně zvětšení; prohledány všechny
čtyři vrstvy errat a aktuální TeX bez nalezené opravy.
Historický text druhého vydání obsahuje stejnou mez.
Lenstrův vlastní článek na332–335 pracuje s jinými mezemi
a toto tvrzení neobsahuje. Fyzický poslední dotisk ani
prvenství neověřeny, návrh hlášení neodeslán.
