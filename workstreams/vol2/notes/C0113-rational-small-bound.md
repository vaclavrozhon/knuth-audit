# V2-C0113: maximum mezivýsledku při N=2

**confirmed**, 2. listopadu2026. §4.5.1-7, zadání332, odpověď639,
třetí vydání, první tisk1997. [Zadání](../images/vol2-p332.png)
i [odpověď](../images/vol2-p639.png) přečteny v původní sazbě.

Vstupní čitatele a kladné jmenovatele mají absolutní hodnoty menší
než N. Při sčítání redukovaných zlomků u/a a v/b se počítá
g=gcd(a,b) a t=u*(b/g)+v*(a/g). Odpověď uvádí maximum
(N-1)^2+(N-2)^2 bez omezení N>=3.

Pro N=2 jsou přípustné vstupy1/1 a1/1. Mají g=1,t=2, zatímco
uvedené maximum je1. Oba vstupy jsou redukované, všechny jejich
čitatele a jmenovatele jsou menší než2. Mezivýsledek nemusí být
reprezentovatelný ve vstupním rozsahu; právě jeho velikost úloha zkoumá.

Pro N>=3 je vytištěný vzorec správný a ostrý. Důkaz a rodina
dosahující maxima jsou v [rational-basic.md](rational-basic.md).
Oprava: doplnit N>=3, nebo zvlášť uvést maximum2 pro N=2.
Jde o drobnou okrajovou výjimku, nikoli o chybu hlavního algoritmu.

Čtyři vrstvy errat all2-prepre/all2-pre/all2/err2 prohledány podle
332,639,4.5.1,vzorce a meze; příslušná oprava nebyla nalezena.
Nezávislé úplné ověření77764 dvojic pro N=2,...,16 souhlasí
s opravenou mezí. Výsledky `results/rational-basic.json`, blok maximum.
Poslední fyzický dotisk a priorita neověřeny; návrh hlášení neodeslán.
