# strings-grouping-algorithm
algorithm to group strings based on their prefixes/suffixes given the number of groups and how many per group.

for example, let's say you have 12 strings and they are supposed to be grouped into 6 groups of 2: \
**hello**, **hell!**, **ryan**, **my name is ryan**, **AAA**, **AHAHAHA**, **12345**, **123123**, **move**, **i move?**\
would be grouped into: **hell**(_hello_, _hell!_), **ryan**(_ryan_, _my name is ryan_), **A**(_AAA_, _AHAHAHA_), **123**(_12345_, _123123_), **move**(_move_, _i move?_)

another example:\
with # of groups = 2 and # per group = 3 \
**USA!USA!**, **i hate USA**, **i like usa**, **bacon**, **i am bad**, **bad strings** would group into:\
**USA**(_USA!USA!_, _i hate usa_, _i like usa_), **ba**(_bacon_, _i am bad_, _bad strings_)

The algorithm also converts non-english characters and non-unicode characters (if possible), so an `Á` would be able to match with `A` and `λ¢Ξ$` would match to `ACES`.

If the strings are impossible to group based on the given parameters (# groups and # per group), then the algorithm wouldn't be able to come up with anything useful. In that case, it would just randomly group strings into the given number of groups.

The algorithm isn't perfect of course. The most common situation where the algorithm could create wrong groups is when there are overlapping possible groups. For example, let's say you want to group the strings **AABB**, **BBCC**, **CCAA**, **CCBB** into 2 groups of 2. For this group of strings, the algorithm would come up with the groups **CC**(_CCAA_, _CCBB_), **BB**(_AABB_, _BBCC_), but it is possible that the correct solution would be the groups: **AA**(_AABB_, _CCAA_), **BB**(_BBCC_, _CCBB_). 

Since there is no way that I am aware of to optimize this (unless if another parameter such as the name of the groupings were to be included, which would kind of defeat the purpose of this algorithm), the algorithm has some rules for these cases. The algorithm prioritizes combinations that create the most ___prefix___ groups, then looks to create the most same-affix groups - groups that are strictly prefix only or strictly suffix only as opposed to groups with a combination of suffix and prefix matches.

The algorithm was made to deal with groups of strings both relatively small in length (typically <15 characters) and small in number (<15 strings). As a result, as the performance of the algorithm as the number and lengths of strings increases, the performance probably suffers. The worst test case I tried was about 240 strings with an average length of approximately 35 characters sorted into groups of 2 (the smaller the number per group, the worse the performance gets). It took the algorithm roughly 12.8 seconds to solve this test case. But in the circumstances it was designed for, it ensured that solving time rarely exceeded 10 ms (though this does mean that sometimes rather than searching for a perfect solution, it would find a "good enough" solution if finding the best solution would be too costly performance-wise). 
