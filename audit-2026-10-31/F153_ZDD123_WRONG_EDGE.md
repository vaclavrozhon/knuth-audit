# F153: jedna hrana obrázku123 vede do nesprávného stavu

3. listopadu 2026; §7.2.2.1, obrázek123 na str.121, draft str.57.
Zdrojová hrana vede z **01111011 do00101101**. Má vést do **00101011**.

Bity označují dosud nepokryté položky1,…,8. Výchozí stav má položky
{2,3,4,5,7,8}. Zvolený pivot je2 a možnost {2,4} jej má převést na
{3,5,7,8}, tedy00101011. Vytištěný cíl {3,5,6,8} znovu přidává
již pokrytou položku6; takový přechod není možný žádným párovacím krokem.

Vektorová kontrola přečetla všech34 stavů a97 významových hran
v obou verzích. Právě jedna hrana chybí a právě jedna přebývá,
v obou verzích totožně. Zvětšené zdrojové výřezy byly prohlédnuty:
[kniha](images/zdd251-260-original-123-edge.png),
[autorův draft](images/zdd251-260-draft-123-edge.png).

Souřadnice vadného segmentu ve výřezu celé knižní strany jsou
(134.266,481.438)→(164.150,501.361); správný cílový řádek leží
o11.954 bodu níže. V draftu jde o přeložení o(22.08,108.66).
Záznam všech hran a jejich porovnání:
[source-checked.json](results/zdd251_260/source-checked.json).

Jde o chybu diagramu, nikoli o selhání Algorithm Z. Počet signatur,
99 uzlů ZDD a105 párování K8 se touto opravou nemění. Dřívější
přesné výpočty K8 se neopakovaly. Šest vrstev errat bez nalezené opravy;
fyzický výtisk neověřen a prvenství netvrdíme.
