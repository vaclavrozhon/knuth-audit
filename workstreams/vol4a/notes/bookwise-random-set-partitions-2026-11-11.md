# Random set partitions

Reviewed main 426 from “Random set partitions” through 428 before “Partitions of a multiset”, exercises 64–67, and answers 777–778 through answer 67.

Checked the block-profile multinomial count, expected k-block count, Bell-ratio expansion, exact variance and its covariance term, and the limiting Ferrers-profile interpretation. The claimed uniform remainder in (50) fails already at k=floor(sqrt(n)); its exponential correction must be retained. The fixed-k remainder also loses a logarithmic factor. The intermediate error in (51) assumes fixed k, although its final weaker bound is valid for growing k. The variance rate in answer 65 likewise fails near the most common block size; F0107 and F0108 give the respective asymptotic counterexamples and repairs.

Checked Stam's probability normalization and its uniform partition probability by summing the falling-factorial weights. Its moment formula, mean correction and leading variance agree, including the cancellation in the variance. Also read the original 2023 Algorithm P addition: at each step |S|=n-k, inclusion has weight w_(n-1,k), exclusion has weight w_(n,k+1), and the Peirce recurrence makes these choices telescope to uniform probabilities. The n=k transition leaves exactly n-1 elements for the next block. No new issue in this addition.

A short symbolic simplification was used only to confirm the fixed-k second coefficient in the suspect ratio formula. Exact figure/census/cited-limit exceptions are listed separately. Next: multiset partitions from main 428/file 445, exercise 68 and answers from 778/file 795. Shared main 428, exercise 439 and answer 778 remain uncertified; main 431 is still unread.
