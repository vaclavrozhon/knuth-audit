# V3-C0070 — The n=0 term is U_N, not the trie inspection count

Confirmed in volume 3, second edition, first printing (1998), printed
p.505, paragraph following equation (14) (file p.516).

The text identifies the n=0 terms of (14) as N-1 plus the number of bit
inspections in a binary trie. In fact the sum is N-1+U_N, with U_N
defined in 5.2.2-(38). The trie inspection total is N+V_N, as answer
6.3-18 correctly states.

Take N=2. The n=0 part of (14) is

    sum_(m>=0) 2^m [(1-2^(-m))^2-1+2*2^(-m)]
      = sum_(m>=0) 2^(-m) = 2.

For two independent random binary keys, the first differing bit has
mean position 2. Looking up both keys in the trie therefore takes
four bit inspections on average. The claimed N-1 plus that total
would be 5, not 2. By contrast U_2=1, so N-1+U_2=2 as required.

Replace the verbal identification by N-1+U_N. The algebraic
calculation in answer 27 already uses this correct quantity.

Original p.505 checked visually and retained. No matching correction
was located in the official layers or limited public searches; see
`sources/digital-searching-errata-review.json`.
