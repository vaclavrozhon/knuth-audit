# §3.5 G: historický kontext a uzavření sekce

Původní sazba 177–178 byla přečtena vizuálně. Jde o kontrolu souvislostí
mezi definicemi a zdrojů, ne o nové dokazování každé věty v citované literatuře.
Matematické části A–F a všech 44 úloh mají samostatné poznámky; zejména
výzkumné úlohy 17, 27 a 38 jsou auditovány v rozsahu tam výslovně uvedeném.
Nejsou vydávány za nově vyřešené problémy.

## 1. Distribuce, četnosti a měřitelné množiny

R1 znamená správné limitní četnosti všech konečných bloků v intervalech.
Přechod mezi reálnou posloupností a Bernoulliho posloupností (bit má
pravděpodobnost p být 1) na straně 177 je správný pro0<p<1, jak
Copeland výslovně požaduje podle Churchovy poznámky11. Směr z reálné
posloupnosti vznikne rozdělením intervalu na [0,p) a [p,1).

Pro obrácený směr vezměme libovolnou binární posloupnost se správnými
četnostmi všech vzorů: vzor s r jedničkami v k místech má četnost
p^r(1−p)^(k−r). Každý její bit nahraďme nezávislou rovnoměrnou hodnotou
v příslušném z obou intervalů. Pro pevný obdélník s racionálními konci
je průměr očekávaných indikátorů oken dán konečným součtem přes vzory
a konverguje k objemu obdélníku. Okna vzdálená alespoň k jsou nezávislá,
takže rozptyl součtu N indikátorů je O(kN). Chebyshevova nerovnost na
N=m², konvergence součtu 1/m² a doplnění mezi sousedními čtverci dokazují
skoro jistou konvergenci. Spočetný průnik přes k a racionální obdélníky
poskytne hledanou reálnou posloupnost. Konstantní posloupnosti při p=0
nebo1 lze zvednout konstantním kódováním, ale libovolnou posloupnost
s degenerovanými Bernoulliho frekvencemi takto přesně zvednout nelze.
Například jediná1 při p=0 je pro práh U<0 nemožná. Celé původní
ekvivalenci se tyto vyloučené kraje nepřidávají; podrobně
`recovery-randomness-history-2026-11-06.md`.

Odmítnutí silnějšího tvrzení o všech Lebesgueovsky měřitelných množinách
na straně 178 je správné: množina všech členů jedné posloupnosti je
spočetná, má míru nula, ale empirickou četnost jedna. To neodporuje
správným četnostem intervalů ani tvrzení „pro každou pevnou množinu
skoro jistě“; pořadí kvantifikátorů je jiné.

## 2. Primární zdroje a jejich rozsah

- Church 1940, str.130–135, byl přečten celý v textové vrstvě původního
  článku. Na str.134 uvádí přesnou efektivní výběrovou definici a důvody
  existence, na str.135 nemožnost vypočitatelné posloupnosti. Historický
  přehled 130–133 potvrzuje návaznost Borel–von Mises–Copeland–Wald.
  Jeho poznámka 17 přímo uvádí Waldův článek 1937,38–72.
- Kolmogorov 1963, str.369–376, byl přečten v textové vrstvě; hlavní
  definice na371 a návaznost na Churcha na373 dovolují adaptivní pořadí
  čtení s rozhodnutím o výběru před zjištěním hodnoty. To je obsah R6/Q2.
  Existenční důkaz na374 odpovídá pravděpodobnostnímu sjednocení špatných
  testů; vlastní přesný důkaz knihy je ve `finite-randomness.md`.
  Závěrečné meze na375–376 nejsou zde vydávány za nový vyřešený problém38.
- Borelův původní článek 1909 se při omezeném pokusu nepodařilo získat
  jako PDF. Oprava z 11.1.2000 v `all2-prepre` mění „normal“ na
  „entirely normal“ a doplňuje informální formulaci věty C v §12.
  Matematický obsah věty C byl ověřen samostatně i z Niven–Zuckerman1951;
  přesná interpretace Borelova §12 ani prvenství nejsou nově certifikovány.
- Pro Loveland1966 byly ověřeny údaje vydavatele:12,279–294, DOI
  10.1002/malq.19660120124. Plný původní článek ani jeho konkrétní
  oscilační mez 1/2 ze str.178 nebyly znovu dokázány. Věta203(d) v níže
  uvedené knize dokládá nestabilitu Churchových výběrů při permutaci,
  ale sama není dokladem přesné Knuthovy oscilační nerovnosti.
- Výrok o existenci R4 bez R6 má vlastní důkaz úlohy37 v
  `selection-extensions.md`. Historické prvenství Herzog–Owings1976,
  konkrétní Waldova chyba v původním1937 článku, Korobov1948,
  Besicovitch1934, Howard1975 a Popperova pasáž jsou evidovány jako
  bibliografické odkazy knihy; jejich celé původní texty nebyly přečteny.
- Programová složitost a primární Martin-Löf1966 jsou rozlišeny v
  `finite-randomness.md`; zde se neopakuje tvrzení o čtení všech
  Kolmogorovových, Chaitinových a Solomonoffových prací.

Toto omezení externí bibliografické kontroly není důkazem nepřítomnosti
chyby v nedostupném zdroji. Obnova X0159 ponechává text G partial:
zejména konkrétní Lovelandova konstrukce a oscilační mez nejsou
uzavřeny. Věta203(d) má v uloženém výňatku pouze formulaci a navíc
sama nedokazuje ani ztrátu R4; nejde o náhradu potřebného důkazu.

## 3. R6 a jednostranná převaha: C0070

Odpověď31 na str.597 označuje analogii Villeova příkladu pro R6 za
neznámou. Tato výzkumná poznámka je zastaralá. Shenův původní článek
1988/anglicky1989 byl přečten celý vizuálně; kniha Shen–Uspensky–
Vereshchagin2017, věta203(b), uvádí přímo převahu nul v každém prefixu.
Uchován jen relevantní výňatek knihy, nikoli celá kniha.

`C0070-r6-prefix-bias.md` dává vlastní úplný důkaz pro přesné reálné R6
knihy a současně pro všechny základy b. Nepoužívá silnější moderní
pojem Kolmogorovovy–Lovelandovy sázkové náhodnosti. Poznámka autora
na163 a177 o intuitivní vhodnosti R6 je filozofické hodnocení; nevedeme
ji jako další nezávislý matematický nález.

Všechny čtyři vrstvy errat i uložený aktuální TeX byly prohledány podle
stran, názvů a témat. Známá oprava177 je zapracována; oprava komentáře
597 nenalezena. Pozdější fyzický dotisk a prvenství nejsou ověřeny.
