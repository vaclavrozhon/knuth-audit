# Exercises 22–23: exact witnesses and structural impossibility; open census claims

Sources: exercises p. 114 / file 129, answers p. 161 / file 176,
original typesetting inspected. The public correction dated 18 January
2025 replaces the feature-total vector by (12,20,15,10,6). The
correction is applied and is not a finding. The relevant complete,
short and primary-TeX F7 errata layers have no other change to these
two answers. This note separates proved statements from the large
enumeration and algorithm-performance claims, which remain partial.

## E22-1: New models, every total, and the capacity maximum

Using feature order moonroof, LED, audio, heated, sport, G=00110 and
H=11101 exactly implement the stated descriptions. For model counts
(A,B,C,D,E,F,G,H)=(7,2,5,4,4,2,4,2), the five totals are

    moonroof: B2+D4+E4+H2=12;
    LED: A7+C5+E4+F2+H2=20;
    audio: B2+C5+F2+G4+H2=15;
    heated: D4+F2+G4=10;
    sport: E4+H2=6.

The model counts sum to 30. Since each q is 2,3 or 5 and divides 30,
partition the sequence into 30/q disjoint windows of that length.
Their upper bounds imply r≤(30/q)p, giving exactly 12,20,15,10,6.
The valid witness below attains all five at once, so the corrected
“maximum conceivable” description is exact, not just an upper bound.

## E22-2: The printed witness and reflection

The printed 30-letter word is

    FEBAGAHDCAGECDACDCEGACDHAGABEF.

`results/car-sequencing-large-witnesses.json` lists its model counts,
feature totals, and all 137 capacity-window checks. Every one obeys
its cap. Thus it proves that the tight problem has a solution.
Its reversal differs only by exchanging AC to CA at zero-based
positions 14–15, exactly as the answer's parenthesis says. Reflection
preserves every capacity window by the already proved E18 argument,
so it supplies the second solution without another search.

Open: this does not prove that these are the only two solutions.
The requested application of Algorithm 7.2.2.1M to both encodings
and its reported 28 gigamems/22 meganodes versus 4 megamems/1670 nodes
have not been reproduced. They remain partial claims, with no
assertion of error. The earlier proof of the MCC reductions does not
verify those particular search traces or their exhaustive counts.

## E23-1: Why four Fs require at least two zero-model cars

With models A…H, a neighbor of F cannot be B,C,G,H or F because all
request audio and the audio cap is 1/2. It cannot be D because D and
F both request heat and lie in the same three-slot window. Therefore
the only allowed adjacent models are A,E,0. Both A and E request
LED, as does F. If an internal F had no zero neighbor, its two
neighbors would be A/E and the three-slot LED window would have
three requests, violating the cap two. Every internal F thus needs
an adjacent zero-model car.

One zero cannot serve two Fs: they would have to appear as F0F, and
the three-slot heat window would contain two requests above cap one.
At most two of four Fs can be endpoints. The other at least two Fs
must therefore have two distinct zero neighbors. The 60-car doubled
instance has none, and the proposed 61-car instance has only one;
both are impossible. This proves the two negative assertions by
hand, independently of Algorithm M or its reported 202 Gμ run.

If there are exactly two zero cars and a feasible sequence, equality
in this argument forces an F at each endpoint, exactly two internal
Fs, and a different zero adjacent to each internal F. Thus the
printed description using two interior occurrences of F0 or 0F is
also justified. It is a necessary structure, not yet a full census.

## E23-2: A 62-car construction and the printed palindromic witness

Let S be the verified 30-car word in E22-2. The concatenation S00S
has exactly the doubled model counts and two zero cars. Every window
internal to either S is already valid. The remaining windows are
checked explicitly in the saved witness record, which lists all
297 windows of this fixed 62-car word. They all pass.

One can also see why the junction is safe from its local form
…ABEF00FEBA…: audio windows have length two, heat and LED windows
have length three, while moonroof and sport windows have length
five. The two Fs are three slots apart, the neighboring Es are five
slots apart, and the intervening zeros create no requests. Every
crossing window has at most the respective caps. The complete saved
check also covers windows reaching farther into the two words.
Together with E23-1, this proves that two added zero cars and length
62 are sufficient and minimal for the doubled instance.

The longer printed symmetric example is unambiguously reconstructed
by taking its first 31 letters

    FEBAF0HDCAGECDCAGEBAGAHDCAGECDA

and appending their reversal. This agrees with every explicitly
printed letter before the ellipsis, including the central AA, and
with the suffix GACDH0FABEF. Its model counts and all 297 capacity
windows are independently listed in the same saved record and pass.
It has Fs at zero-based positions 0,4,57,61, hence two near each end
as claimed. This verifies that particular example, not the claimed
total number of such examples.

## E23-3: Precisely which remaining counts are not closed

The assertions of 19050 total 62-car solutions, 18 reflection-fixed
solutions, exactly six palindromic solutions with the indicated
near-end F arrangement, and the universal FEBA/ABEF prefix/suffix
have not been proved or enumerated. Two displayed witnesses sharing
that prefix do not establish universality. These claims remain
separate partial inventory items.

Conditional on the first two counts, the stated 9516 mirror pairs
is arithmetically and structurally correct: reflection is an
involution; every nonfixed orbit has exactly two members; and
(19050−18)/2=9516. This proves the inference but not its unverified
premises. The reported 69 Gμ needed for the symmetric census is an
additional unreproduced performance claim.

Only three fixed witnesses were evaluated in one short nice15 run:
the 30-car word, its 62-car concatenation, and the reconstructed
palindrome. No model-space search, exhaustive census, long run or
benchmark restart was performed. The remaining partials are not
new findings and do not prevent recording the complete short
impossibility proof separately.
