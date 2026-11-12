# MMIX-C0008 — GetArgs měří hranici chunku z nesprávné adresy

**Confirmed, medium**, předběžně pro nezávislý audit. Řešení1.4.3′–16/17, p.124/file132, GetArgs: `AND zz,x,Mem:mask`.

x je interní adresa dat v uzlu simulátoru, z je virtuální adresa požadovaného bufferu. Chunk má4096bytů; uzel navíc obsahuje16bytů hlavičky a8bytů koncových nul. Interní začátky DATA proto obecně nejsou zarovnány na4096. Počet bytů do konce simulovaného chunku je4096−(z &4095), nikoli4096−(x &4095).

Konkrétní platný stav podle rozložení p.77–78 (D=Data_Segment):

- Chunk0=D+#1010; druhý uzel je o#1018 dále, tedy D+#2028. Nechť jeho KEY=D, DATA začíná naD+#2038.
- Argumenty Fread jsou na virtuálníD a obsahují buffer z=D+#ff0, délku17. Tato oblast je v datovém segmentu a je zarovnána.
- MemFind přeloží z na interní x=D+#2038+#ff0=D+#3028. Správný počet zbývajících bytů je16, ale GetArgs vypočte4096−#28=4056.
- SimFread proto chybně považuje všech17bytů za jeden chunk a pošle je jedinému skutečnému Fread. Při17vstupních bytech A se prvních16 uloží správně do simulovaných adresD+#ff0…D+#fff. Sedmnáctý byte se zapíše do interního nulového paddingu naD+#3038, nikoli do simulované adresyD+#1000. Tato virtuální adresa nadále čte0, pokud předtím nebyla nastavena.

Oprava řádku: `AND zz,z,Mem:mask`. Dopad se týká i využití stejné rutiny pro SimFwrite. Nejde o EOF ani neplatný vstup; je k dispozici všech17bytů.

Jde o přesnou ruční adresní stopu, nikoli provedený běh simulátoru. Originální chybný řádek ověřen v images/file-132-p124.png; rozložení uzlů sources/file-085.txt a086.txt. Relevantní historická i současná errata bez odpovídající opravy, viz results/errata-113-134.json. Fyzický výtisk neověřen.
