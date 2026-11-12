# Kandidát: kořen v odpovědi §2.3.1-19

Kořenový stav při předání: **V1-C0049, candidate**. Globální ID přidělil koordinátor; lokální dočasné označení a níže zachovaná historie revize slouží návaznosti evidence.
Dočasné označení `postorder-root-sentinel`; candidate V1-C0049. Původní obrazy 321, 324, 332 a 566 přečteny. Definice na 321 výslovně dává postorder následníku kořene hodnotu LOC(T), tedy HEAD podle 324. Odpověď 19 nejprve najde rodiče Q; pokud P není jeho levé dítě, vrátí Q, jinak opakuje inorder následníka od Q, dokud RTAG(Q)=1.

V jediném uzlu P s hlavičkou H máme `L(H)=P, R(H)=H, LTAG(H)=RTAG(H)=0` a `L(P)=R(P)=H, LTAG(P)=RTAG(P)=1`. Algoritmus F správně vrátí Q=H: přejde do F4, nastaví R=R(P)=H a zjistí P=L(H). Následující popis postorder následníka však má P=L(Q). Proto z Q=H provede inorder následníka, dostane P, jehož RTAG=1, a vrátí P. Požadovaná hodnota je H. Jde o nejmenší neprázdný vstup.

Místní doplnění: po nalezení rodiče Q vrátit HEAD, pokud Q=HEAD; teprve jinak použít uvedené rozlišení levého a pravého dítěte. Pro pravostranně i plně prošívaný strom je kontrola stejná. Pokud se „basic idea“ v odpovědi čte pouze jako popis vnitřního kroku a volající již zvlášť zachytí konec průchodu u kořene, tento doplněný algoritmus funguje. Chybí tedy výslovný hraniční případ v předloženém popisu, nikoli obecná myšlenka určování následníka.

Samostatný model `post_successor(..., guard_root=False)` v `tree_algorithms.py` zachovává doslovný postup, zatímco výchozí verze přidává uvedenou kontrolu. `results/algorithms.json` obsahuje minimální případ; pro všechny tvary n≤7 ověřuje opravenou verzi proti nezávislému rekurzivnímu pořadí. Čtyři vrstvy errat z inventáře podle 321/332/566 a témat parent, postorder, successor neobsahují tento doplněk.
