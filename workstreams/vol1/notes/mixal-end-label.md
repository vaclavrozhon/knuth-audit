# Oprava auditního assembleru: návěští na END

Podagent při přepisu programu T (§2.2.3) odhalil chybu našeho mixal.py.
Forward odkaz na návěští X na řádku `X END TOPSORT` se chybně přidělil
jako implicitní `X CON 0`; následně vznikla duplicitní definice. Nejde
o chybu knihy. Pravidlo11(f) na156 říká, že návěští END označuje první
místo za automaticky doplněnými slovy; pravidlo13 přiděluje CON0 pouze
symbolům, které v LOC vůbec nejsou. END label proto nyní z automatického
přidělování vyloučíme a definujeme jej v obvyklém pozdějším kroku.

Cílená regrese `check_mixal_end_label.py` obsahuje ručně spočtené adresy
při souběhu END návěští, nedefinovaného symbolu a literálu; také lokální
forward návěští, vlastní použití END labelu, případ bez návěští a skutečnou
duplicitu. Všech740 kontrol ve všech37radicích prošlo. Oprava se dotýká
pouze dosud odmítaného případu forward odkazu na END label. Dřívější
úspěšně sestavené programy s touto chybou sestavit nešlo, jejich výsledky
proto není třeba znovu vytvářet. Agentův lokální rozpis `X EQU *; END`
po explicitním doplnění ostatních konstant má tutéž sémantiku.
