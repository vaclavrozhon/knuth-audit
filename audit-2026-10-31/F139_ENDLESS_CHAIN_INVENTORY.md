# F139 — vytištěné dílky řetězového hlavolamu nemají řešení

**4B, 7.2.2.1–150, zadání str. 143 / PDF 163.** Řešení str. 458–459.
Stejná chybná sada je v autorově draftu na str. 79 / PDF 85.
Závažnost: vysoká. Doslovně vytištěná úloha je nemožná; není to obtížnost
řešiče ani nezdařený výčet.

![Krátký paritní důkaz](images/f139-parity.png)

## Důkaz bez hledání

Čísluj dílky zleva doprava, nejprve devět v horní řadě, pak devět v dolní.
Počítej **konce středové cesty**, ne jednotlivé čáry kreslící tloušťku článků.

- Dílky **3, 14 a 17** mají lichý počet vodorovných konců: po jednom.
  To je třetí dílek nahoře, pátý dole a osmý dole.
- Všechny ostatní mají vodorovných konců sudý počet. U každého dílku je
  celkový počet konců sudý, takže vodorovný a svislý počet mají stejnou paritu.
- Otočení o 90° oba počty prohodí. Žádné otočení tedy paritu dílku nezmění.
  Součet vodorovných konců celé sady zůstane **lichý**.
- Ve složeném uzavřeném řetězu se vodorovné konce musí párovat na společných
  svislých hranách dílků. Jejich součet proto musí být **sudý**. Spor.

Důkaz dovoluje i více smyček nebo převracení dílků: ani to překážku neodstraní.
Zvláštní spoj posledních dvou dílků je zahrnut; nejde o přehlédnutou půlku článku.
Ekvivalentně sada obsahuje 21 pravých úhlů středové cesty, zatímco každý
uzavřený pravoúhlý cyklus musí mít sudý počet takových změn směru.

Samostatné ověření, standardní Python, žádné balíčky ani data:

```bash
python3 audit-2026-10-31/verify_f139.py
```

## Oprava a co používá knižní řešení

Ve spodní řadě jsou první dva malé dílky stejné: jejich cesta má dvě zatáčky
a konce na protilehlých dlouhých stranách. **Jeden z nich nahraď druhou kopií
třetího dílku horní řady**, jehož cesta má jedinou zatáčku a končí na krátké
a dlouhé straně. Rozměr 1 × 2 se nemění. Stručně: místo jednoho L a dvou S
jsou potřeba **dvě L a jedno S**.

Všechny čtyři vytištěné sestavy na str. 459 používají tuto opravenou sadu.
Každý jejich dílek, všech 64 polí a všech 112 rozhraní byly přečteny přímo
z vektorové kresby v PDF a draftu. Každá má jediný řetěz přes 34 polí.

Jediný úplný výčet opravené sady původním Algorithm M skončil za 22,8 s
s `nice 15` a limitem 60 s. Má **43 řešení**, **8 cest při zachování rámu**
a násobnosti čtyř vytištěných příkladů **1, 15, 9, 3**, přesně jako kniha.
Všech 43 modelů bylo přímo validováno. Pro chybnou sadu se žádný výčet
nespouštěl: její počet nula plyne z parity.

## Rozsah potvrzení

Obrázek zadání byl vizuálně ověřen v našem druhém dotisku PDF i autorově
PostScriptovém draftu převedeném do PDF. Všech 18 dílků se shoduje.
Šest aktuálních a historických vrstev errat zkontrolovaných 3. listopadu
2026 neobsahuje odpovídající opravu. Nejnovější kompletní digitální vydání,
fyzický výtisk a prvenství nejsou ověřeny.

Podrobnosti: [CHAIN150_NOTES.md](CHAIN150_NOTES.md),
[vektorová kontrola](results/chain150/figures-checked.json),
[parita a správné počty](results/chain150/claims-checked.json).
