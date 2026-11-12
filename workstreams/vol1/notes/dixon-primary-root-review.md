# §1.2.6-62: Dixonovy dva původní články

Kořenová revize 2. listopadu 2026, V1-X0725. Obě konkrétní
Dixonovy citace jsou checked. Celá úloha62 zůstává partial pro
Rogerse, MacMahona a Dougalla; vlastní konečný matematický důkaz
X0077 zůstává přijat a jeho testy nebyly opakovány.

Root ověřil všech26 souborů, 8600257 bajtů, a12 vstupů paketu
`parallel/binomial-summation-sources/dixon/`. Hash MANIFEST.json je
`f4b23bbc2b5546724dd6d9cac68a2d50b24029149f9c32f54e7b87409f955005`.
Přečetl celé předání a poznámku s převodem, erratový výpis,
obrazově celý vlastní článek79–80 z Messenger, oba tituly,
z Proceedings284–285,289 a začátek následujícího zápisu290.
Přímo porovnal knižní490 a aktuální opravu err1 naPDF11.
Agentův rozsah četby celých284–289 je zachován jako převzatý,
nikoli vydáván za vlastní úplný audit komplexních integrálů.

Pro nezáporná celá l,m,n označme C(A,B) binomický koeficient,
nulový mimo0<=B<=A, a

```text
S(l,m,n)=sum_k (-1)^k C(l+m,l+k) C(m+n,m+k) C(n+l,n+k).
```

Práce z Messenger20 na79–80 dává
`sum_(j=0)^(2n) (-1)^j C(2n,j)^3=(-1)^n(3n)!/(n!)^3`.
Posun j=n+k a zkrácení znaménka dává přesně knižní případ l=m=n.
Původní důkaz převádí koeficient na dvojitý trigonometrický integrál
a konečnou Vandermondovu formuli. Morleymu připisuje pozorování
několika případů. Titul výslovně uvádí May1890–April1891 a rok1891;
neodvozujeme z něj datum jednotlivého sešitu. Nulové n je jediný
člen1, aniž by se autorovi přisuzoval v textu neuvedený rozsah.

V Proceedings35 Dixon definuje hypergeometrickou řadu, tj. řadu
`sum_(j>=0) (a)_j(b)_j(c)_j/[j!(d)_j(e)_j]`, kde (a)_j je
rostoucí součin a(a+1)...(a+j−1) a (a)_0=1. Její zápis je
3F2(a,b,c;d,e;1). Na289 je explicitní sumační formule D1903
z agentovy poznámky. Pomocí duplikace gama funkce a dosazení
d=1+a−b, e=1+a−c přechází na tamní vzorec(D).
Gama funkce rozšiřuje faktoriál: Gamma(t+1)=t! pro celá t>=0.

Root přepočítal přesný konečný převod včetně zdánlivých singularit.
Součin binomických koeficientů má symetrický faktoriálový jmenovatel
`(l+k)!(l-k)!(m+k)!(m-k)!(n+k)!(n-k)!`, takže lze volit l jako
nejmenší parametr. Posun j=k+l dává

```text
S=(-1)^l (m+n)!/((m-l)!(n-l)!(2l)!)
  *3F2(-2l,-l-m,-l-n;1+m-l,1+n-l;1).
```

Pro l=0 je řada1. Pro l>=1 nechme a=−2l+t při pevných
b=−l−m, c=−l−n a t->0. Záporná celá b,c ukončují řadu,
jmenovatele jsou v okolí kladných celých čísel. Jde tedy o konečný
spojitý součet; při t=0 zaniknou členy za j=2l. Ze zbytků gama
funkce u nekladných celých čísel vyjde

```text
Gamma(1-l+t/2)/Gamma(1-2l+t)
 ->2*(-1)^l*(2l-1)!/(l-1)!=(-1)^l*(2l)!/l!.
```

Ostatní gama faktory jsou konečné a pravá strana(D) se zkrátí na
`(-1)^l(2l)!(m-l)!(n-l)!(l+m+n)!/[l!m!n!(m+n)!]`.
S prefaktorem výše je to přesně S=(l+m+n)!/(l!m!n!). Obecná
konvergenční podmínka má v této limitě hodnotu1+l+m+n>0.
Poměr pólů nebyl nesprávně nahrazen poměrem jednotlivých hodnot.

Původní284 uvádí doručení10.října1902, přednes13.listopadu1902
a poznámku o ztrátě rukopisu a přepsání v lednu1903. Titul svazku
má1903 a článek končí289;290 již začíná zápis schůze. Knižní rok
a známá oprava285–289 na284–289 z29.března2023 jsou tedy doloženy.
Čtyři vrstvy errat nemají další změnu Dixonova tvrzení; sousední
q-Pfaffův vzorec a stylistická změna factorial factors jsou odlišeny.

Samostatný paket obsahuje původní mechanický výňatek. Celý výchozí
svazek plms35.pdf se shodným hashem je archivován také; to nerozšiřuje
rozsah četby. Převod potvrzuje konkrétní knižní citaci, nikoli
absolutní historickou prioritu nebo všechny analytické argumenty
obecného komplexního teorému. Žádný nový nález TAOCP nevznikl.
