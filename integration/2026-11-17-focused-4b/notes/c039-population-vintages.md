# C039 — Further population provenance check

The statement on printed page115 attributes the total306,084,180 for the48 contiguous states to an official2010 population. That is exactly the sum in the supplied GraphBase data. The prior comparison found that all49 GraphBase entries, including DC, agree with the2015 estimates base except California, which is1608 smaller.

This follow-up inspected the official Census `CENSUS2010POP` and `ESTIMATESBASE2010` columns for the2011,2012,2013,2014,2016,2017,2018 vintages. California's original census count is37,253,956 throughout; the base values range from37,253,956 to37,254,523. None is the GraphBase value37,252,895. The2015 base37,254,503 was already checked. The downloaded CSVs and exact field extraction are preserved in [the review record](../results/c039-vintage-review.json); source URLs and failed initial filename/case attempts are in [the fetch record](../results/c039-vintage-fetch.json).

The same questionable value appears in later third-party prose and network datasets. This repetition is not independent official corroboration. However, this check still does not establish the exact source originally copied into GraphBase or exclude every historical source. C039 remains a candidate about the attribution, not a finding about the algorithm. No population data, optimization results, or candidate status were changed.

## Follow-up: the matching manynet value

An exact-number search on November17 located California37252895 in the `manynet` dataset `irps_usgeo` (previously `ison_usstates`). Its official repository documentation cites Meghanathan2017 for the state-adjacency graph. However, repository commit `250432d5a9` shows that population was added separately on May24,2024; its inspected patch and dataset documentation do not identify a Census source. The original2017 article was downloaded and its text searched: it studies graph adjacency and centrality, and the located Census references concern geographic regions rather than population counts. This is not independent support for the population's provenance, and its2017 citation must not be taken as a date for the population data. A dependency on the SGB data is plausible but not established from the inspected sources. C039 remains a candidate. No partition or population census was rerun.

Sources and hashes: `../sources/c039-manynet-provenance.json`. The exact source commit is https://github.com/stocnet/manynet/commit/250432d5a9 .
