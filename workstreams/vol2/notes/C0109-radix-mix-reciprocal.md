# V2-C0109: dvě chyby programu bez dělení

**confirmed**, 2. listopadu 2026. TAOCP2, třetí vydání, první dotisk
1997, §4.4-8, strana 636. [Původní program](../images/vol2-p636.png)
byl vizuálně přečten. Jde o funkční chybu převodu, ne o problém
asymptotického odhadu.

Program má dvě nezávislé vady:

1. `MUL =1//10=` používá dolní aproximaci 1/10. Operátor `//`
   je definován ve svazku 1, §1.3.2, strana 153 jako dělení
   `w*A` číslem B se zahazováním zbytku. [Sken definice](../images/radix-vol1-p153.png)
   byl přečten; jde o stranu souboru 168. Pro `w=64^5` je
   konstanta 107374182. Při vstupu u=10 první MUL nechá rA=0
   a rX=1073741820. Program následně uloží hodnotu 10 jako
   jedinou výstupní číslici a skončí.
2. Po výpočtu první číslice je v rA podíl, ale paměť U zůstává
   původní. Instrukce `ADD U` v dalších iteracích tedy odečítá
   desetinásobek nového podílu od nesprávného vstupu. I když
   opravíme konstantu na 107374183, u=10 vydá postupně 0 a 10.

Přepis původních instrukcí i opravená varianta jsou v
`sources/radix-basic.mix`. Oprava pro binární MIX:

- nahradit konstantu `1//10` hodnotou `1//10+1`;
- před každým násobením převrácenou hodnotou uložit aktuální rA
  do pomocného CURRENT a nahradit `ADD U` instrukcí `ADD CURRENT`.

Label návratu vnější smyčky musí být na novém `STA CURRENT`.
Návrat po opravě příliš velkého podílu zůstává na `STA TEMP`,
aby CURRENT nadále obsahovalo vstup dané iterace.

S oběma úpravami se u=10 převede na číslice 0,1. Obecná správnost
plyne z úlohy 7 a opravy zbytku; důkaz mezí mezivýsledků je v
`radix-basic.md`. Instrukční simulace prošla pro 2510 vstupů
na dvou binárních kapacitách slova, včetně 85 skutečných oprav
podílu. Testy oddělených úprav ukazují, že žádná z nich samotná
nestačí. Opravená verze zachovává původní U a stojí
`35M+3+21C` cyklů pro M číslic a C oprav, `C<=1`.

Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
byly prohledány podle 636, odpovědi 8, `TEMP`, `ADD U`,
`STA U`, `JAP`, `1//10` a souvisejících stran. Zjištěna byla
pouze nesouvisející náhrada odpovědi 9. Oprava těchto vad
nebyla nalezena. Nejnovější fyzický dotisk, priorita a odměna
neověřeny. Neodesláno.
