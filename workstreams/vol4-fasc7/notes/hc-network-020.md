# Strana12: HC network a celý přepis(20)

Původní p12/file27 byl zobrazen. Tabulka1 má úplný geometrický argument
J41-c–d v `cubie-junctions-exercise-041.md`; první věta o jedné značce
čáry a dvou koncových podmínkách má argument HC-4 v
`hc-projection-main-011.md`. Zbývající definice, obrázek a tvrzení
této strany jsou jednotlivě ověřeny níže.

## N20-1 — definice a jednoznačnost až na cyklické Y

Vrcholům daného HC obrázku přiřaďme různé pevné názvy. Sousednost
se čte z jeho úseček; proto j' je sousedem j právě tehdy, když j je
sousedem j'. Jde o reciproční konečnou definici neorientovaného grafu,
nikoli o dodatečné geometrické omezení. Názvy větví označují jiné
různé vrcholy, jak přísluší jednotlivým čarám obrázku.

Typ junction určí jeho stupeň a úhly podle HC-1. U V je jedinečný
menší sektor a jeho pořadí po směru hodinových ručiček určí l,r.
U W jsou všechny tři větve v jediném menším sektoru<π; dvě krajní
a prostřední větev jsou určeny jednoznačně a pořadí v tomto sektoru
po směru hodinových ručiček určí l,m,r. U T je právě jedna
kolineární protilehlá dvojice. Třetí větev je m; pořadí l,r se zvolí
tak, aby m bylo vlevo od orientovaného směru r→l. To je právě
pořadí kanonické kresby T s příčkou nahoře a stonkem dolů.

U Y nemá žádná větev význačné počáteční místo, ale orientace roviny
jednoznačně určuje cyklické pořadí a,b,c po směru hodinových ručiček.
Existují právě tři jeho lineární zápisy abc,bca,cab. Ostatní tři
permutace orientaci obracejí a nesmějí se zaměnit s tímto obrázkem.
To dokazuje celé tvrzení o jednoznačnosti pod(20), při pevných názvech
vrcholů, včetně přesného důvodu jediné uvedené volnosti.

## N20-2 — každý původní vrchol a každá hrana

Ze skutečného SVG `sources/file-027.svg` se čtou všechny19 kruhových
obrysů junctions. Písmena byla jednotlivě přečtena v originálu a
přiřazení čísel cest je uloženo v `results/network20.json`; nedochází
k volbě písmen podle požadovaného výsledku grafové izomorfie.
Střed kružnice určuje symetrie jejích nativních Bézierových souřadnic.

Každý konec každé přímé cesty167–174 je přiřazen jednoznačně ke středu
s odchylkou<0.01 bodu. U každého souvislého úseku se navíc vyhledají
všechny středové body ležící uvnitř. Nastává právě jeden takový případ:
cesta168 vede souvisle z k do p, ale obsahuje n přesně na téže přímce.
Rozdělí se tedy na kn a np. Tím se zabrání nesprávnému čtení obrázku
jako grafu bez jeho T. Další čáry se neprotínají mimo své junctions.

Úplná výsledná množina je

ab,ac,bd,be,cd,cm,dg,ef,eg,fh,fq,gh,hj,ij,ik,jl,kl,kn,ls,mn,mo,np,op,or,qs,rs.

Přesně se rovná všem26 neorientovaným párům ze všech19 tištěných
pravých stran(20). V každém případě je výskyt reciproční. Počty
typů jsou t=1,v=5,w=8,y=5. Žádná hrana ani junction nejsou vynechány.

## N20-3 — každý typ a každé pořadí větví

Pro každou pravou stranu se spočítají paprsky od jejího středu
k uvedeným sousedům v původní kresbě. V souřadnicích PDF, kde y
roste dolů, kladný determinant dvou paprsků určuje otočení po směru
hodinových ručiček přes úhel menší nežπ.

U každého V(l,r) vychází det(l,r)>0. U každého W(l,m,r) jsou
det(l,m),det(m,r),det(l,r)>0: m leží mezi krajními paprsky a celkový
sektor je menší nežπ. U každého Y(a,b,c) jsou všechny tři cyklické
determinanty kladné, takže odpovídá správné pořadí i všechny tři
úhly<π. U n=T(k,m,p) jsou k,p přesně protilehlé kolineární větve,
a det(k,m),det(m,p)<0, což odpovídá N20-1. Každý test se týká
konkrétních původních souřadnic; všechny determinanty jsou uloženy.

Konkrétně d=Y(b,g,c) dovoluje právě zápisy d=Y(g,c,b),d=Y(c,b,g).
Záměna d=Y(b,c,g) obrátí nenulové determinanty a neodpovídá obrázku.
Úplná množina ostatních Y je právě {e,h,l,m}, jak uvádí text.

## N20-4 — shoda s původním histoscape, nikoli jen se seznamem(20)

Přebírá se kompletní nezávislý prostorový výsledek pro104(d), který
již byl samostatně porovnán s původním101(d). Tři jednoznačné
reference jsou a=(0,0,4),b=(0,1,4),c=(1,0,4). Určují invertibilní
mapu obrazové roviny s kladným determinantem. Všech19 středů(20)
se pak jednoznačně přiřadí všem19 junctions uzavřeného pohledu;
největší čtverec odchylky je<0.000401 bodu², zatímco druhý
nejbližší kandidát je vzdálen více než1 bod. U všech19 souhlasí typ.

Pro všechny již uzavřené viditelné intervaly fyzických hran se vyberou
všechny junctions, které na nich leží, a spojí sousední v jejich
parametrickém pořadí. Úplná množina výsledných26 hran se přesně
rovná N20-2. Tím je dokázána i věta, že(20) odpovídá Fig.101(d),
nezávisle na samotném přepisu pravých stran. Všechny úspěšné staré
prostorové výpočty se přebírají bez opakování.

Kontrolní program `check_network20.py` pouze zpracuje tyto pevné
vektorové seznamy, žádné grafy ani CSP nehledá; proběhl s nice15.
Tento soubor a předchozí J41/HC-4 uzavírají matematický obsah p12.
Navazující26 proměnných a všechny tuple vztahy(21),(22) se kontrolují
samostatně na p13; nelze je převzít pouze z hotové geometrie.
