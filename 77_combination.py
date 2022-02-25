"""
given n ranging from 1 to n, return all combinations of two from 1..n

[1,2,3], k=2 -> 1,2 1,3 2,3
if 1 is picked, the second choice lies in rest [2, 3]
if 2 is picked, the second choice lies in rest [3]

use backtracking:
to from combination with number of k
first picked rely on the rest

if start first pick from i, the next pick will be in [i+1,...n-1]
when start the next pick, keep track of number of picks. if picks reaches
our threshold k, then we register all picks.
"""

def backtrack(n, l, k, track, results):
    """
    if picks is more than limit k, we found combinations
    """
    if len(track) == k:
        results.append(list(track))
        return

    """
    starting pick at l, the next pick lies in l+1...n
    need to try l pick at next value in the option list
    , so pop l entry from the track
    """
    for i in range(l,n+1):
        track.append(i)
        backtrack(n, i + 1, k, track, results)
        track.pop()
    results = []
    backtrack(n, 1, k, [], results)
    return results

