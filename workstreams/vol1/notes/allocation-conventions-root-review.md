# Kořenová revize dvou konvencí alokace

1. listopadu 2026. Přečteny oba předané reporty, reprodukční programy,
celý `PROOFS-allocation.md` i153 řádků `allocation.py`. Původní437,
456,616,618 a související výklad435–436 byly přímo porovnány.
Sentinel byl porovnán s dříve přímo přečtenými443,611 a612.
Úspěšné běhy podagenta se znovu nespouštěly.

## C0073: rozdíl variant first-fit, matematický nález dismissed

First-fit vybírá první dost velký volný blok v pořadí seznamu.
Samotné toto pravidlo neurčuje, ze kterého konce vybraného bloku
se má oddělit požadované místo. Algoritmus A na437 bere horní konec;
pozdější důkaz na618 potřebuje nejnižší dostupnou adresu.

Protipříklady podagenta jsou přesné. Pro fond7, živý objem nejvýše5
a velikosti nejvýše2 postupně zůstanou obsazeny buňky5,3,1; žádná
mezera nemá délku2. Pro fond43, živý objem nejvýše13 a velikosti
nejvýše5 zůstane osm buněk38,33,28,23,18,13,8,3; mezery mají délku
nejvýše4. Přitom43>13 H_5/ln(2), kde H_5=137/60 je páté harmonické
číslo. Dolní racionální odhad logaritmu v reportu toto dokazuje
bez numerického zaokrouhlení. Obecná rodina dává při přidělování
horního konce potřebu řádu mn, nikoli n log(m).

Původní podezření však bylo příliš silné. Zadání43 výslovně říká
„Find a defensive strategy“ a odpověď38 tvrdí existenci „a first-fit
strategy“. Obranná strategie smí zvolit dolní konec. Výrok proto
netvrdí stejné meze pro každou variantu ani konkrétně pro A.
Kořen i podagent se po novém čtení shodli na této interpretaci.

C0073 je zaregistrován jako dismissed matematický nález; protistopy
zůstávají užitečným dokladem rozdílu variant. Explicitní upozornění
na volbu konce by mohlo výklad usnadnit, ale není doložena nepravdivá
věta v knize. Tento závěr nepotvrzuje dosud nepřečtené původní
Robsonovy články a nemění jejich samostatný pramenný stav.

## C0074: sentinel a záporná nula, candidate

Sentinel je zvláštní položka, která ukončí prohledávání seznamů.
Na611 se pro dodatečnou hlavu AVAIL[m+1] požaduje kladný TAG,
tedy znaménko. Instrukce LD4N načítá znaménko i dopředný odkaz
a znaménko obrátí; J4NN se větví, pokud výsledná hodnota není záporná.
Při nulovém odkazu vznikne záporná nula, na níž se J4NN také větví.
Kladné znaménko samo tedy požadované zastavení nezaručuje.

Při m=k=0 a jediné již obsazené buňce splňuje sentinel+0 výslovnou
podmínku, ale program znovu přidělí adresu0. Kontrola v37 bázích
MIX pro m=0 a1 potvrzuje tentýž jev. Obecný důvod plyne již ze
sémantiky dvou instrukcí, nezávisle na konečném testu.

Dostatečnou podmínkou je nenulový dopředný odkaz; přirozená
inicializace prázdné hlavy odkazem na sebe ji splňuje. Rovnice
(12)–(14) výslovně inicializují pouze hlavy0,...,m, nikoli m+1.
Je však možné číst dodatečnou položku implicitně jako standardní
prázdnou hlavu. Proto jde o candidate chybějící podmínky, nikoli
o potvrzené tvrzení, že zamýšlený program musí selhat. Předchozí
úspěšné kontroly buddy systému používaly nenulový vlastní odkaz;
jejich výsledky jsou platné.

Čtyři vrstvy errat jsou doloženy v předaných JSON výpisech.
Nebyly nalezeny opravy těchto konvencí. Nic nebylo odesláno,
pozdější fyzický dotisk nebyl porovnán.
