# V2-C0157 — chybějící výjimka 3 v Prothově kritériu

**Confirmed.** §4.5.4–27, první odstavec odpovědi na str. 663,
formuluje ekvivalenci pro `N=k*2^n+1`, pokud `3` nedělí `k`
a `k<=2^n+1`. Kladné parametry `k=1,n=1` splňují obě podmínky
a dávají prvočíslo 3. Tištěná kongruence má ale levou stranu
`3^(2^(1-1)*1)=3=0 (mod 3)`, nikoli -1.

Oprava: přidat `N>3`, případně vyřídit 3 zvlášť. Pro všechny
ostatní kladné parametry platí obecný důkaz v
[primality-deterministic.md](primality-deterministic.md), §4.
Původní úloha pro `5*2^n+1` není tímto protipříkladem vyvrácena;
její malý případ `n=1,N=11` se rovněž vyřídí přímo, protože
se nevejde do zobecněné podmínky na k.

Přečtena [původní sazba663](../images/vol2-p663-detail.png).
Čtyři vrstvy errat a aktuální TeX bez opravy této hranice;
opravy2002/2003 mění bibliografii a kvalifikaci malého k.
[Přesný experiment](../results/primality-deterministic.json)
porovnal 5472 parametrů se sítem: jediný rozpor je právě 3.
Obecný důkaz, nikoli tento konečný experiment, potvrzuje opravené znění.
Novější fyzický dotisk ani priorita neověřeny; draft neodeslán.
