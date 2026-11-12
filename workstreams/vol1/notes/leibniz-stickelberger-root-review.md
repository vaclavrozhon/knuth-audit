# Leibniz a Stickelberger: převzetí původních pramenů

Celá úloha **1.2.5–14 je checked**. U úlohy **13** je doloženo
Leibnizovo autorství příslušného výroku, ale přesný rok **1682**
zůstává otevřený. Nový **V1-C0087** je kandidát k historické revizi,
nikoli potvrzená chyba nebo hotová náhrada roku číslem 1703.

## Rozsah převzetí a přímé četby

Root ověřil všech **193 souborů**, 98 096 875 bajtů, zmrazeného
`parallel/factorial-primary-followup/leibniz-stickelberger/`
a všech **18 sdílených vstupů**. SHA-256 agentova manifestu je
`e6f57a13aba1055627a3742d4c4e4fb89840dac5482faffbed49fa71b00d99dc`.
Přečetl HANDOFF, UNIT_STATUS, oba obsahové rozbory, sources,
read-log a kontrolu errat. Již přijaté matematické testy neopakoval.

Root přímo obrazově četl Stickelbergerův §4 od spodku **342**,
celou **343** a horní návaznost **344**, titul ročníku **1890**;
celý Vaccův článek **113–116**; Mahnkeho **33–34 a 41–43**;
Peanův titul a předmluvu třetího sešitu (PDF **148, 150–151**) a
cílový §Np 12.31 na **85**; Leibnizův list **21r**, zejména tabulku
a blok latinského výroku; TAOCP **51, 480–481**.

Z archivovaného původního HTML root samostatně přečetl katalogové
záznamy **31464 a 32350**, včetně legendy značky `~`. Širší agentova
četba, například Mahnke 29–32, se nepřipisuje rootovi. Rukopis nebyl
úplně paleograficky přepsán a celé historické svazky nejsou označeny
za přečtené pouze proto, že jejich soubory máme.

## Stickelberger a přesný převod

V [původním článku](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0037/LOG_0027.pdf)
je a kladné celé číslo a p prvočíslo; autor výslovně připouští p=2.
Cifry a_i a postupné celočíselné podíly q_i definuje vztahy
`a=a_0+p*q_1`, `q_1=a_1+p*q_2` atd. Jejich součet
`mu=q_1+q_2+...` je exponent p v a!, tedy počet všech jeho faktorů p.
Rovnice (4) na 343 říká

```
a! / (-p)^mu = a_0! a_1! ...    (mod p).
```

Po položení a=n a násobení znaménkem `(-1)^mu` jde přesně o zadání
TAOCP. Původní důkaz opakovaně odděluje násobky p, používá Wilsonův
součin nenulových zbytků a násobí získané kongruence; souhlasí s
knižním důkazem. Při p=2 jsou znaménka modulo p stejná. Přesný rok
je na titulu původního ročníku. Žádná oprava této úlohy ani její
atribuce ve čtyřech vrstvách errat nebyla nalezena.

## Leibnizův výrok a rozdílné datovací doklady

Wilsonova věta říká, že pro prvočíslo p je `(p-1)!` po dělení p
kongruentní k -1. Leibnizova formulace se součinem do čísla o dvě
menšího znamená `(p-2)! = 1 (mod p)`. Pro p>2 jsou ekvivalentní
vynásobením nenulovým zbytkem p-1; pro p=2 platí přímo.

Na [původním listu 21r](https://digitale-sammlungen.gwlb.de/resolve?id=00068261)
je vidět řada faktoriálů, tabulka zbytků a blok začínající
„Productus continuorum“. Jeho shoda s vydaným přepisem je přesvědčivá;
root netvrdí úplnou transkripci všech škrtů. Vacca v roce 1899 a
Mahnke v letech 1912–1913 původní správný výrok přímo přepisují.
Mahnke na 42 vysvětluje také pozdější chybný dodatek vzniklý chybným
výpočtem modulo 17. Ten nevyvrací existenci původního správného výroku.
Kniha netvrdí, že Leibniz zanechal jeho důkaz.

Časové doklady je třeba odlišovat:

- Vacca 114 uvádí „před 1683“ u předchozího **Fermatova** výsledku
  a odkazuje na jiný list datovaný 1. června 1683. Wilsonův výrok
  samostatné datum nemá. Na 115 Vacca upozorňuje na nejisté číslování
  matematických volných listů. Jeho fol. 10 není automaticky dnešní
  fol. 10.
- Mahnke 33 říká, že se pokouší rukopisy chronologicky uspořádat.
  Na 34 je příslušný list 21 položkou 25 bez vlastního data, mezi
  prosincem 1681 a červnem 1682. Toto zařazení je podklad pro starší
  datovací tradici; není kalendářním datem přečteným na listu.
- Peanův přepis na 85 patří k třetímu sešitu z **1899**, což dokládá
  titul i předmluva. Soubory označené peano1897 zachovávají starší
  navigační omyl. Přepis neuvádí 1682 a závisí na Vaccově práci.
- [Pracovní katalog Leibnizovy edice](https://leibniz-katalog.bbaw.de/de/extended-search?sign_ol=3+B+11&view=list)
  datuje jednotlivé strany 21r/21v **~1703**, přičemž legenda výslovně
  definuje `~` jako circa. U 21r má záznam 31464 katalogové číslo
  39249, poznámku Math.Schr.1703 a vodoznak hvězdy v přehybu.
  Vlastní archivní argument pro tuto dataci nebyl získán.
- Agregované datum **1685** u digitálního svazku GWLB označuje jinou
  úroveň popisu. Agent je přímo ověřil; nepřenáší se na každý jeho list.

**V1-C0087:** identifikovaný rukopis podporuje atribuci Leibnizovi,
ale jeho současná individuální katalogová datace je v napětí s
přesným rokem 1682 v knize. Proto je namístě samostatně prověřit
zdroj tohoto roku. Pozdější písemný doklad nevylučuje dřívější znalost
nebo jiný rukopis. Ani přibližná katalogová datace sama neopravňuje
bezvýhradně přepsat knihu na 1703. Celá úloha 13 zůstává partial.

Známá oprava odpovědi 13 z 8. listopadu 2005 mění Law 1.2.4D na B;
s datací nesouvisí. Čtyři veřejné vrstvy neobsahují odpovídající
historickou opravu. Místní anglický podnět nebyl odeslán.

Přesný kořenový soupis je
`results/leibniz-stickelberger-root-manifest.json`. Staré zmrazené
poznámky zůstávají beze změny; tento dodatek nahrazuje jejich starší
informaci o otevřené Stickelbergerově citaci.
