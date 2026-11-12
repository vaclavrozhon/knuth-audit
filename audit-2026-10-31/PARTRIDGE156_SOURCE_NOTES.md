# DLX156: symetrie, velikost vstupu a původní citace

Kontrola 3. listopadu 2026. Zadání str. 144, odpověď str. 460,
MCC formulace (61) str. 92. Vizuálně ověřeno v místním PDF a
autorském draftu 2019. Žádný nový úplný výčet.

## Již přijatá matematika

Starý výčet má 2 566 sestav ve výseči, 468 s jednotkou na diagonále,
2 332 tříd D4 a 18 656 sestav bez omezení. Samostatný validátor
zkontroloval geometrii a všechny symetrie každého uloženého modelu.
Jeho soubory i programy zůstávají zmrazené. Úplnost hledání přes první
volnou buňku je odůvodněna v [původních poznámkách](PARTRIDGE_NOTES.md).

Mřížka 36×36 se vejde do 36 slov po 64 bitech, tedy 288 bajtů.
To je velikost reprezentace obsazených buněk, nikoli tvrzení, že
program nepotřebuje zásobník a pole zbývajících násobností.

## Proč stačí dvě okolí jednotky

Jediný čtverec 1×1 nemůže ležet na hraně desky. Kdyby ležel třeba
u horní hrany, levý i pravý soused by pokračovali alespoň o jeden
řádek dolů. Dolní soused má stranu alespoň 2, a musel by překrýt
jednoho z nich. V rohu je stejný spor jen mezi dvěma sousedy.

Ve vnitřku má jednotka čtyři různé sousední čtverce. Každý z nich
musí zabrat alespoň jednu ze dvou přilehlých diagonálních buněk.
Diagonální buňky jsou jen čtyři a nesmějí se překrývat. Každý soused
tedy zabírá právě jednu. Zbývají dvě cyklická uspořádání, zrcadlové
obrazy jeden druhého. Odpovídají přesně dvěma malým kresbám v knize.

`check_partridge156_source.py` přímo dekóduje všechny čtyři úsečky
každé kresby a porovnává je s draftem. Nově také ověřuje pouze
tato lokální okolí v dříve uložených 2 566 modelech. Na diagonále
je 234 sestav každého druhu; každá má v archivu svůj odlišný
zrcadlový obraz druhého druhu. Nejde o nové hledání řešení.

D4 převede každou polohu jednotky do i<18, j≥35−i. Mimo diagonálu
je takový obraz jediný. Na diagonále zůstává právě odraz podle
této diagonály a ten zamění oba druhy okolí. Volbou prvního tedy
získáme přesně jeden reprezentant každé třídy:

2 566 − 468/2 = 2 332; následně 8·2 332 = 18 656.

Netriviální rotace nemůže fixovat jedinou jednotku na sudé desce.
Vodorovné a svislé odrazy také ne; diagonální odraz by změnil
její právě dokázané okolí. Každá sestava má proto osm obrazů,
nezávisle na empirické kontrole starého validátoru.

## MCC: číslo 205 753 není chyba

Je 36²+8 = 1 304 položek. Jednotka má ve výseči
1+2+…+18 = 171 možností; pro k=2,…,8 je jich (37−k)².
Celkem 7 367 možností. Součet skutečných položek v možnostech je

171·2 + Σ(k=2,…,8) (37−k)²(k²+1) = 198 386.

Původní DLX3 počítá navíc jeden spacer na možnost:
198 386 + 7 367 = 205 753. Zdrojový kód u načítání vstupu
vypisuje `last_node-last_itm` a tuto konvenci potvrzuje.
Pro největší dílek je 29² = 841 možností po 65 položkách.
Toto navazuje na starší ověření, nevzniká nový nález.

## Citace a známá oprava E079

Z oficiálního archivu CMS byl získán a vizuálně přečten celý
citovaný článek Ahearna a Jepsena, Crux 19 (1993), 189–191.
Uvádí konstrukci řádu 11 a 16 a rozšíření pokrývající 11 až 33.
Na titulku jsou **Stephen T. Ahearn a Charles H. Jepsen** v tomto
pořadí. Oprava z 7. dubna 2026 na str. 460, řádek −3, je proto
potvrzena; není zapracovaná v našem PDF ani v draftu. Evidujeme
ji jako **E079, známé erratum**, nikoli nový nález.

Wainwrightova vlastní kapitola na str. 279 datuje Cutlerovu první
odpověď několik týdnů po setkání v lednu 1996 a popisuje upravený
program BOX. Hamlynův a Friedmanův přehled připisuje Cutlerovi úplný
počet 2 332. Přesný rok dokončení celého počtu tím není přímo doložen.
Wainwrightův původní dopis Gardnerovi s datem 1981 rovněž nemáme;
kapitola odkazuje na dopis bez uvedení roku.

Poslední věta o řešitelnosti všech n>7 je výslovná domněnka,
nikoli prezentovaný důkaz. Cílené hledání nenašlo její obecné
řešení. Z toho nevyvozujeme absolutní tvrzení o dnešním stavu
literatury. Otevřený výzkumný problém je oddělen od auditu n=8.

## Výslovně vynechané dlouhé reprodukce

- Stromy s 61 636 037 366 a 6 975 499 717 uzly pro přesné
  původní varianty hledání. Náš starý výpočet použil jinou výsečovou
  variantu; jeho počet uzlů není kontrolou těchto údajů.
- Dobové náklady 2,0 Tμ, 235 Gμ a 490,6 Tμ, včetně úplného
  velkého běhu Algorithm M. Žádné dlouhé ladění pořadí či další
  kopie výčtu. Poměr 490 600/235 > 2 000 je aritmeticky správný,
  ale vlastní měření rychlostního poměru se neprovedlo.

Oprávnění: pokyn uživatele z 3. listopadu. Čísla jsou označená jako
nereplikovaná, nikoli ověřená. Matematické počty již ověřené jsou.

**Výsledek:** X156 matematicky checked, celá DLX156 partial kvůli
přesnému původnímu datování. E079 známé, žádný nový F/C. Další 157.

## Evidence

- [Nové lokální a zdrojové kontroly](results/partridge156/source-claims-checked.json)
- [Původní článek CMS](sources/partridge156/crux1993-19-7.pdf)
- [Archivace a hash zdroje](sources/partridge156/retrieval.json)
- [Rozsah historických závěrů](sources/partridge156/source-observations.json)
- [Šest vrstev errat](results/partridge156/errata-check.json)
