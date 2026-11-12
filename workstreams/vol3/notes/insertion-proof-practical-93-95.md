# Praktický Shellsort93–95, tabulky6–7 a úlohy28–29

7. listopadu 2026. Originály93–95/file104–106 a odpovědi623/file634
přečteny se všemi odpovídajícími opravami2001/2003/2023/2025.
Přebíráme hotové f/g, K, semigrupové meze a celý čas ProgramuD.
Nový výpočet je pouze přesné dosazení do uzavřených vzorců a
součet vytištěných čísel; žádný benchmark ani náhodný soubor.

## P0844: přírůstkové rodiny, celistvost a skutečné zvláštní případy

Všech38 řádků tabulky6 a přidaný řádek2001 jsou přepsány ze sazby
v `results/insertion-table6-arithmetic.json`. Každá posloupnost
je přísně klesající, kladná, menší než N=1000 a končí1.
Algoritmus proto vždy končí úplným1-sortem; použitelnost všech
těchto příkladů nezávisí na jejich rychlosti.

Základní rodiny v proze mají následující přesné významy:

- Shellovy ⌊N/2⌋,⌊N/4⌋,… tvoří při N=2ᵐ celý dělitelný
  řetězec. Již prokázaná P0799 dává jeho kvadratický nejhorší
  případ. Obecně platí ⌊N/2ˢ⌋=2⌊N/2ˢ⁺¹⌋ právě tehdy, když
  příslušný bit N je0. Dlouhý nulový blok tak dává skutečný
  dělitelný úsek; obecné slovo „undesirable“ tím nepovyšujeme
  na nový kvantitativní odhad pro každý takový N.
- Zvětšení sudého členu Shellovy posloupnosti o1 jej činí lichým;
  půlení zajistí pokles až k1 (případné duplicitní1 se vynechá).
  Pro1000 vyjde přesně501,251,125,63,31,15,7,3,1.
- 2ᵏ−1 dává1,3,7,…; 2ᵏ+1 dává3,5,9,… a konečné1 se přidává.
  Tabulkové zkrácené varianty jsou podposloupnosti těchto členů.
- (2ᵏ−(−1)ᵏ)/3 je celé, protože2≡−1 mod3. Pro k=1,2 dává
  tutéž1, dále3,5,11,21,43,85,171,341,683. Od k=2 roste:
  rozdíl sousedních čitatelů je2ᵏ+2(−1)ᵏ>0. Tabulkové
  duplicitní1 se používá jen jednou.
- (3ᵏ−1)/2 je celé a dává1,4,13,40,121,364,…; řádek
  365,122,41,14,5,2,1 analogicky odpovídá(3ᵏ+1)/2.
- Fibonacciho řádky jsou přímo řetězce součtů předchozích dvou
  členů, případně jejich podposloupnost377,144,55,21,8,3,1.

Pro Incerpiho řádekρ=2.5 je336,112,48,21,7,3,1 již prokázaný
prefix P0826. Proρ=2 má báze a₁,…,a₄=(2,5,9,17): prahy2,4,8,16;
4,8,16 jsou zakázaná sudá čísla, ostatní uvedené členy jsou
navzájem nesoudělné. Stejná(8) dává

    1,2,5,10,18,45,90,170,306,

tedy přesně druhý Incerpiho řádek. Tím je zkontrolován i druhý
vytištěný parametr, nikoli pouzeρ=2.5.

## P0845: první osm řádků tabulky6 mají přesné průměry

V každém z prvních osmi řádků dělí další menší přírůstek
bezprostřední větší. První průchod má obvyklé náhodné třídy.
Při pozdějším h-sortu s předchozím H=kh, q=⌊1000/h⌋,
r=1000 mod h použijeme přesně

    E B_h=r f(q+1,k)+(h−r)f(q,k),
    E A_h=r g(q+1,k)+(h−r)g(q,k).

Podmíněná rovnoměrnost uvnitř tříd byla prokázána v H/corollary;
nenahrazujeme ji nezávislostí. Všechny přesné zlomky jsou uloženy,
zde uvádíme hodnoty, které jednoznačně určují tištěné zaokrouhlení:

|První přírůstek / T|E A|E B|
|---|---:|---:|
|1 /1|6.485470861|249750|
|17 /2|64.660360541|41666.544509267|
|60 /3|158.113728937|26360.592651510|
|140 /4|262.185925413|21912.516658969|
|256 /5|361.921252868|20458.946707761|
|576 /6|419.247421803|20087.602209062|
|729 /7|378.290751660|18533.218372751|
|512 /10|492.503125448|16434.665469870|

Všech16 zaokrouhlení souhlasí; důkaz vychází ze vzorců pro
každý průchod, nikoli z opakování původních náhodných pokusů.

## P0846: zbývající pozorované průměry — partial

Řádky9–38 a přidaný řádek39 (190,84,37,16,7,3,1) mají v JSON
jednotlivě výslovný rozsah: ověřeno pořadí/počet přírůstků,
součet S a lineární časové dosazení; **neověřeny empirické A/B**.
Próza uvádí10000 náhodných souborů délky1000, ale tyto vstupy
nejsou součástí zdrojů. Povolené vynechání takové reprodukce
neznamená, že byly průměry matematicky prokázány.

I tvrzení o „usually about15“ pro směrodatnou odchylku A a
„usually about300“ pro B zůstává v tomto přesném experimentálním
rozsahu partial. Nejde o uniformní pravděpodobnostní větu.
Udaný nejmenší pozorovaný B≈6750 odpovídá6745 pro2ᵏ+1 a6755
pro Incerpiρ=2; jde o kontrolu shody s tabulkou, nikoli pravosti
nepřístupného měření. Žádná chyba z toho není odvozena.

## P0847: oba Prattovy typy mají tvrzený asymptotický řád

Pro pevná nesoudělná a,b>1 vezměme všechny aᵖbᑫ<N. Jednoznačnost
je zaručena jednoznačným prvočíselným rozkladem: z aᵖbᑫ=aʳbˢ
a gcd(a,b)=1 plyne p=r,q=s. Plošný důkaz P0812 po náhradě
ln2,ln3 za ln a,ln b dává T=(lnN)²/(2ln a ln b)+O(logN).

Před h-sortem je soubor ah- a bh-ordered, nebo jsou příslušné
podmínky prázdné. V h-třídě je nejvýše(a−1)(b−1)/2 inversí
na pravý prvek. Proto je každý průchod O(N), celý čas
O(Nlog²N). Pro a=5,b=11 je konstanta20; pro7,13 je36.
Dolní mezΘ(Nlog²N) plyne zΘ(log²N) přírůstků<N/2, z nichž
každý má alespoň N/2 vkládacích iterací.

V tabulce jsou tyto množiny zkráceny na h<N/3. Důkaz přesto
zůstává platný: chybí-li ah nebo bh pod hranicíN/3, pak
h>N/(3max(a,b)) a délky h-tříd jsou omezeny konstantou.
Takový horní průchod stojí O(N) přímo; u všech ostatních se
použije semigrupová mez. Počet stáleΘ(log²N).

Množiny pod1000/3 jsou přesně

    {5ᵖ11ᑫ}: 1,5,11,25,55,121,125,275,
    {7ᵖ13ᑫ}: 1,7,13,49,91,169.

Při témže omezení má{2ᵖ3ᑫ} počty9,7,6,4,3,1 pro q=0,…,5,
celkem30. Osm a šest průchodů tak skutečně snižují tuto složku
režie. Neodvozujeme z toho automaticky menší celý čas pro každý N.

## P0848: celá formule(11) a opravený vztah k článku

Pro s=2k a u=2ᵏ má(11) tvar9u²−9u+1; pro s=2k+1 má
tvar16u²−12u+1. Obě jsou celé a kladné. Rozdíl lichého členu
od předchozího sudého je u(7u−3)>0; rozdíl následujícího sudého
od lichého je2u(10u−3)>0. Vzniká tedy přísně rostoucí řada

    1,5,19,41,109,209,505,929,2161,3905,…,

přesně podle tabulek6–7. Sudá podřada je9·4ᵏ−9·2ᵏ+1,
lichá je4ᵏ⁺²−3·2ᵏ⁺²+1: jde o proložení dvou rodin.

Původní připsání meze O(N⁴ᐟ³) přímo této řadě bylo nahrazeno
známou opravou26.5.2025. Primární Sedgewickův článek1986 je
uložen v `sources/sedgewick-1986-shellsort.pdf`. Jeho věta5
na165 má jinou posloupnost1,8,23,77,… a věta6 na168 jinou
1,5,65,377,…. Naproti tomu strana171 výslovně používá proložené
rodiny(11) pro experimenty a odděluje je od nejhorších mezí.
Sazba171 je v `images/insertion-sedgewick-1986-file013.png`.

Tím je ověřeno současné opatrnější tvrzení knihy a přesné
rozlišení posloupností. Nepřebíráme neexistující aplikaci těchto
vět na(11) a nevydáváme čtení článku za úplný nový audit jeho
Selmerova/Johnsonova důkazu. Oprava2025 není nový nález.

## P0849: celý nákladový závěr94 v opraveném znění

Přesný čas rozložíme na průchody:

    time_D=1+∑ₕ(9B_h+10(N−h)+13−3A_h).

Proto je správné10(NT−S), jak uvádí oprava2001, a identita
NT−S=∑ₕ(N−h) je přesná. Při h>N/2 mají neprázdné třídy
nejvýše dva členy; existuje N−h dvojic. V prvním průchodu
B_h=A_h je počet obrácených dvojic, takže cena tohoto průchodu
leží mezi13+10(N−h) a13+16(N−h), její průměr je13+13(N−h).
Tvrzení opravy o levném prvním průchodu při h blízko N tím má
přesný obsah i v mezním případě h=N−1.

Srovnání jednoho průchodu s přibližně(10/9)N přesuny je pouze
vedoucí heuristika při zanedbání h, konstanty13 a změny A.
Při vynechání h je přesný rozdíl

    Δtime=9ΔB+10(N−h)+13−3ΔA.

Číslo1111 pro N=1000 je správně zaokrouhlených10000/9 v tomto
vedoucím modelu, nikoli uniformní dovolený přírůstek B pro každé
h. Původní doporučení vynechávat velký první přírůstek bylo
odstraněno; jako tvrzení aktuálního textu jej nepřebíráme.

## P0850: úloha28 a přesné srovnání všech tabulkových časů

Do celého časového vzorce bylo dosazeno všech39 řádků, včetně
známého přídavku2001. Nejmenší tři hodnoty z uvedených průměrů:

    209,109,41,19,5,1         128578u,
    505,209,109,41,19,5,1     129755u,
    929,505,209,109,41,19,5,1 129914u.

Odpověď28 je tedy správnou odpovědí na „which sequence shown
in Table6“, i po přidání řádku190,…,1 (130444u). Tato kontrola
nezaručuje skutečný experimentální průměr; jejími vstupy jsou
výslovně tabulková čísla. Samotné zaokrouhlení A na jednotky
a B na nejbližších pět nemůže překlenout mezeru1177u: chyba
jednoho času je v takovém modelu nejvýše3/2+9·5/2=24u.
Neznámou výběrovou odchylku tím neomezujeme.

## P0851: tabulka7 — všechny součty a rozsah příkladu

Všech12,13 a10 tištěných hodnot B_s bylo sečteno:

    346152,329532,248788.

Přírůstky jsou přesně uvedené tři rodiny2ᵏ−1,2ᵏ+1 (s konečným1)
a(11). Poslední součet je menší než oba ostatní, proto je závěr
o přesunech **v tomto příkladu** správný. Přesné sloupce jsou
v témže JSON, s výslovným omezením „arithmetic sum only“.
Rekonstrukce jednotlivých B_s, tvrzení o totožném náhodném
vstupu a experimentální typičnosti zůstávají partial: vstup
20000 hodnot není znám a nové měření by ho nenahradilo.

## P0852: empirické asymptotiky, rozptyly a doporučení — partial

Zvlášť evidujeme tyto nedoložené experimentální výroky:

1. Weissův fit1.55N⁵ᐟ⁴−4.48N+O(N³ᐟ⁴) v intervalu100 až12000000
   a směrodatnou odchylku≈.065N⁵ᐟ⁴ pro2ᵏ−1.
2. Původní fit.43N⁷ᐟ⁶+18.5N+O(N⁵ᐟ⁶) a rozptylové tvrzení
   pro(11) byly odstraněny opravou2001. Aktuální náhrada se
   dovolává Ciurových testů, které naznačují O(N(logN)²) nebo
   lepší průměr a změnu směrodatné odchylky nad10⁷. Ani tuto
   náhradu nevydáváme za prokázaný asymptotický výsledek.
3. Srovnání „about as good as any other“ pro menší N a praktické
   doporučení(11) pro větší N jsou empirická, nikoli globální
   optimalita. Pozdější Tokudova možnost NlogN je rovněž výslovně
   hypotetická. Nové rozsáhlé reprodukce nebyly spuštěny.
4. Jednotlivé hodnoty B_s tabulky7, jejich původ z téhož souboru
   a tvrzená typičnost nebyly reprodukovány; P0851 uzavírá
   všechny aritmetické součty a srovnání těchto dodaných hodnot.

P0723/P0724 již drží související empirické/výzkumné meze;
tento záznam doplňuje konkrétní parametry a opravené formulace.
Historické články Weiss1991 a Tokuda1992 nebyly rychle získány
v primární úplné podobě; bibliografická shoda není matematický
důkaz jejich experimentů.

## P0853: rekurence(12), zastavení a správné zaokrouhlení Tokudy

Indukcí z h₀=1, hₛ₊₁=3hₛ+1 dostáváme
hₛ=(3ˢ⁺¹−1)/2. Posloupnost roste a končíme vždy alespoň
s přírůstkem1. Pro celočíselné N je původní podmínka3h_t≥N
ekvivalentní opravené h_(t+1)>N, protože h_(t+1)=3h_t+1.
Nejmenší t≥1 splňující podmínku tedy určí konečný seznam
h_(t−1),…,h₀; počet je O(logN) a poslední1 zaručuje správnost.

Nová formule z12.3.2023 je v originální sazbě skutečně **podlaha**:

    hₛ=⌊(4/5)((9/4)ˢ⁺¹−1)⌋.

Zobrazená v `images/insertion-errata-tokuda-detail.png`.
Hodnoty nezaokrouhlujeme opakovaně v rekurenci. Pro rₛ uvnitř
podlahy platí r₀=1 a rₛ₊₁=(9/4)rₛ+1. Proto rₛ roste,
rₛ₊₁−rₛ≥9/4>1 a celé hₛ přísně rostou; h₀=1,
hₛ=Θ((9/4)ˢ). Například prefix je1,3,8,19,45,102,232,524.

To se liší od staré rekurence s průběžným⌊2.25hₛ⌋+1,
která dává1,3,7,16,37,84,190 a patří k přidanému tabulkovému
řádku2001. Odlišný seznam v historickém experimentu není rozpor
s následnou opravou doporučené formule. Internetová varianta
s horním zaokrouhlením není bez primárního článku důvodem
měnit jasnou sazbu Knuthových errat. Zde se dokazuje pouze
platnost/generování formule; její připisované výkony zůstávají P0852.

## P0854: celé aktuální zadání/odpověď29 — experimentální mezera

Úloha žádá hledání empiricky dobrých posloupností. Evidujeme
všechny odpovědi v platném znění: Tribolet373,137,53,19,7,3,1
(≈7210 přesunů) a317,101,31,11,3,1 (≈8170), jeho pravidlo
nejbližšího prvočísla k Nˢᐟᵗ pro nekoncové přírůstky; Siegelův
empirický fit t≈(4/3)ln(N/5.75) pro N≤10000; McNameeho45,7,1
(≈18240) a91,23,7,1 (≈11865). Fit t není přesný vzorec pro
všechna malá N (pro N≤5.75 by ani nedal kladný počet průchodů).
Oprava8.12.2003 nahrazuje Tomlinsonovo „best known“ Ciurovými
sedmiprůchodovými229,96,41,19,10,4,1 (≈6879 přesunů) a
737,176,69,27,10,4,1 (≈125077u).

Posloupnosti jsou legální, jejich poslední1 zajišťuje správnost.
Numerické empirické průměry, optimálnost v rozsahu provedených
testů a odhad počtu průchodů ale nebyly reprodukovány a zůstávají
partial. Původní přibližné časy127720/128593 nelze ověřit jen
z uvedeného B bez původního A; srovnávají navíc totožná
historická data, ne nutně průměry tabulky6. Nehlásíme je jako
chybu kvůli odlišnosti od lineárního dosazení tabulky6.

## Stav

P0844–0845/P0847–0851/P0853 mají uvedené úplné argumenty;
u P0851 je výslovně uzavřen pouze matematický součet, nezveřejněné
experimenty jsou zahrnuty do P0852. P0846/P0852/P0854 partial.
Žádný nový nález. Strany93–95 i odpověď623 proto nejsou celé
argumentově uzavřeny. Další doplnitelný matematický blok: úloha27
na104/623 (Poonenova dolní mez), potom42 a související P0785,
před přechodem k list insertion95–96.
