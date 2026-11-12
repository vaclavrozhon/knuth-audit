# V2-C0106: nejlepší známá dolní mez v odpovědi4.3.3-15

Stav: **confirmed**,2.11.2026. Lokace: TAOCP2,3.vydání,1.dotisk,
str.634,odpověď15, poslední tři řádky. Tvrzení o nejlepší známé
mezi n log n/log log n je pro standardní vícepáskový Turingův
stroj příliš slabé již vzhledem ke stejnému citovanému zdroji.

Paterson–Fischer–Meyer, MIT-LCS-TM-040(1974), Theorem2(ii),
tištěná21/PDF23, dokazuje střední čas Omega(n log n). Definice
modelu na7/PDF9 výslovně používá jednorozměrné pásky. Slabší
mez z Theorem2(i) platí pro obecnější stroje. Stejné rozlišení
potvrzuje druhý citovaný článek Fischer–Stockmeyer1974,str.3,
a Harvey–van der Hoeven2021,str.2.

Oprava: pro standardní páskový model uvést n log n; chce-li text
zachovat obecnější model, výslovně rozlišit obě meze. Nález se týká
slova „best“ a rozlišení modelů, nikoli neplatnosti slabší meze.
Důkaz dolní meze z literatury zde nebyl celý znovu odvozen.

Originální str.634 i uvedené primární stránky byly vizuálně čteny.
Čtyři vrstvy errat: all2-prepre,all2-pre,all2,err2; relevantní
oprava7.8.2020 mění horní mez, dolní ponechává. Hledáno podle634,
online,jmen autorů i logaritmických faktorů dne2.11.2026.

Doklady: [rozbor](fast-online.md),
[primární report](../sources/paterson-fischer-meyer-1974-overlap.pdf),
[věta2](../images/overlap1974-file23.png),
[model](../images/overlap1974-file9.png),
[kniha](../images/vol2-p634.png).
Poslední fyzický dotisk a priorita neověřeny. Hlášení neodesláno.
