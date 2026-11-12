# Původní Dershowitz a dokončení §2.3.4.3–8

Přijímám X0851 a uzavírám dřívější pramennou mezeru X0352.
Celá úloha2.3.4.3–8 nyní může být checked. Její obecný
matematický důkaz, odkaz2.3.2–22 a ostatní konkrétní prameny
byly přijaty již v notes/infinity-lemma-root-review.md;
nové získání je nenahrazuje jiným argumentem ani novým testem.

## Přímý originál

Z [autorova seznamu publikací](https://www.cs.tau.ac.il/~nachumd/pub.html)
vede odkaz na [celou původní sazbu článku](https://www.cs.tau.ac.il/~nachumd/papers/IPL.pdf).
Čtyřstránkové PDF má566185 bajtů, SHA-256
37640ad5683663baf4e88e7d50e114451f62d11fa459f34d6c21f575a2fd946d.
Root přímo přečetl všechny obrazy tištěných212–215, strany
souboru1–4. Hlavičky potvrzují Information Processing Letters9(5),
16. prosince1979; konec bibliografie je na215. Autor, rok,
svazek i rozsah citované na Knuthově588 tedy souhlasí.

První dvě strany definují zjednodušovací uspořádání a dokazují
ukončování přepisování pomocí Kruskalovy stromové věty.
Přepis nahradí podvýraz podle pevného pravidla; uspořádání
musí při takové náhradě klesat i uvnitř většího výrazu
a každý výraz musí převyšovat své vlastní podvýrazy.
Nekonečný běh by pak zároveň striktně klesal a obsahoval
dvojici vložených stromů v opačném směru. Důkaz používá
konečně mnoho symbolů vstupu a pravidel, nikoli nevyjádřený
předpoklad konečné množiny všech výrazů. Strana214 dává
příklady a ukazuje, že kritérium není nutné. Bibliografie215
přímo uvádí Kruskala1960 a Nash-Williamse1963.

Tím je ověřena přesně knižní poznámka o použití k důkazům
ukončování. Neprovádíme audit všech dalších citací samotného
Dershowitzova článku. Jeho listopadové označení v autorově
navigačním seznamu nemění datum přímo vytištěné v originálu;
TAOCP uvádí pouze správný rok1979.

## Návrat ke knize a vymezení uzavření

Root znovu zobrazil původní zadání na386 a celou odpověď8
na587–588. Jde o konečné uspořádané stromy a dříve ověřené
vložení z2.3.2–22. Důkaz minimální špatnou posloupností
je již úplný: levé podstromy dovolí nekonečný rostoucí
výběr a pravé podstromy pak odporují minimální volbě.
Zde se nemění ani silnější původní Kruskalova věta,
ani nezávisle dokázaný doplněk o n-ticích.

Nová kolace čtyř vrstev all1-prepre, all1-pre, all1 a err1
nenašla změnu této bibliografické poznámky či úlohy8.
Položky na587 patří dláždění; nová věta na588 k odpovědi4
další sekce. Jmenné indexové výskyty nejsou opravou citace.
Přesný obsahový rozsah starší četby Kruskalova přehledu1972
zůstává zachován; kniha jej doporučuje pro další vývoj,
netvrdí tím správnost všech jeho jednotlivých výsledků.

Nově uzavíráme jedinou celou úlohu; jiné pramenné mezery
§2.3.4.3 se nepovyšují. Nejde o nový nález chyby knihy,
potvrzení prvenství ani kontrolu fyzického exempláře.
