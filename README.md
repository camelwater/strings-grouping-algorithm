# strings-grouping-algorithm
algorithm to group strings based on their prefixes/suffixes given the numnber of groups and how many per group.\
for example, with the given groups number 6 and the number per group 2 the strings: \ **hello**, **hell!**, **ryan**, **my name is ryan**, **AAA**, **AHAHAHA**, **12345**, **123123**, **move**, **i move?**\
would be grouped into: **__hell__**(_hello_, _hell!_), **__ryan__**(_ryan_, _my name is ryan_), **__A__**(_AAA_, _AHAHAHA_), **__123__**(_12345_, _123123_), **__move__**(_move_, _i move?_)

another example:\
with # of groups = 2 and # per group = 3 \
**USA!USA!**, **i hate USA**, **i like usa**, **bacon**, **i am bad**, **bad strings** would group into:\
**__USA__** (_USA!USA!_, _i hate usa_, _i like usa_) and **__ba__** (_bacon_, _i am bad_, _bad strings_)

the algorithm also converts non-english characters and non-unicode characters (if possible), so an `Á` would be able to match with `A` and `λ¢Ξ$` would match to `ACES`.
