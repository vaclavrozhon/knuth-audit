# MMIX-C0013 — StackRoom pushuje tři položky, ne dvě

**Confirmed, low.** Odpověď §1.4.3′–5, p. 117 / file 125, tvrdí,
že StackRoom na řádku 097 pushuje jen dvě položky, protože rL=1,
a sčítá 3+2+3+2=10. Příkaz je ale `PUSHJ res,StackStore` a
`res IS $2` (řádek 053, p. 78). $2 je v tomto okamžiku marginal,
nikoli global. Proto se nejdřív alokuje až po $2, rL se zvětší na 3
a PUSHJ pushuje **tři** položky: staré $0, novou nulu $1 a odkaz 2.
Původní rL=1 není důvod clampovat X na 1; toto pravidlo platí při
**global** destination X≥rG, nikoli při marginal $2.

## Přímý rozpis uvedené cesty

| Call / místo | Nově uložené položky |
|---|---:|
| XDest řádek 218, PUSHJ res,StackRoom | 3 |
| StackRoom řádek 097, PUSHJ res,StackStore | 3 |
| StackStore řádek 078, PUSHJ res,MemFind | 3 |
| Lokály MemFind před BN na řádku 032 | 2 |
| Celkem na této cestě | **11** |

StackRoom při vstupu nemá argumenty; GET $0,rJ vytvoří rL=1.
PUSHJ marginal $2 však alokuje $1 a $2 ještě před přeznačením registrů.
StackStore pak vytvoří $0 a $1, argument v $3; PUSHJ $2 uchová tři
položky a předá jediný argument jako $0. MemFind přidá key do $1,
takže na řádku 032 má dva lokály. Tento count nevyžaduje běh dlouhé
simulace. Přímý spor je už ve vyčíslení jediného příkazu na řádku 097;
netvrdí se tím nově dokázaná globální maximální hloubka všech doplněných
cest interpretu.

Sémantika je uvedena v knize na p. 16 (marginal destination se stane
local) a realizována řádky 208–223 plus 263–276. Potvrzuje ji také
[oficiální zmrazený MMIXware zdroj](https://www-cs-faculty.stanford.edu/~knuth/programs/mmix-20131017.tgz):
`sources/mmix-sim-20131017.w`, řádky 1367–1368 volají instalaci dest,
1841–1857 zvyšují L dokud X<L, a 2243–2252 odebírají X+1.
PUSHJ flags #e0 obsahují X_is_dest_bit. Global větev X≥G je samostatná.
Metadata/hash v `sources/mmix-20131017-metadata.json`; žádný build/run.

Původní sazby p. 78,81,117 byly zobrazeny v images/file-086-p078.png,
file-089-p081.png a file-125-p117.png. Relevantní errata neobsahují
opravu tohoto počtu nebo PUSHJ na řádku 097; viz
results/errata-C0003-C0013.json. Program tím není funkčně chybný,
opravuje se jeho popsaný počet položek při chybovém ukončení.
