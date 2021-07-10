# strings-grouping-algorithm
algorithm to group strings based on their prefixes/suffixes given the numnber of groups and how many per group.


for example, with the given groups number 6 and the number per group 2 the strings: \
**hello**, **hell!**, **ryan**, **my name is ryan**, **AAA**, **AHAHAHA**, **12345**, **123123**, **move**, **i move?**\
would be grouped into: **hell**(_hello_, _hell!_), **ryan**(_ryan_, _my name is ryan_), **A**(_AAA_, _AHAHAHA_), **123**(_12345_, _123123_), **move**(_move_, _i move?_)

another example:\
with # of groups = 2 and # per group = 3 \
**USA!USA!**, **i hate USA**, **i like usa**, **bacon**, **i am bad**, **bad strings** would group into:\
**USA**(_USA!USA!_, _i hate usa_, _i like usa_), **ba**(_bacon_, _i am bad_, _bad strings_)

the algorithm also converts non-english characters and non-unicode characters (if possible), so an `Á` would be able to match with `A` and `λ¢Ξ$` would match to `ACES`.
