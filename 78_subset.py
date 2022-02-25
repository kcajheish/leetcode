"""
Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.

"""
def subset(nums):
    """
    """
    def _subset(nums, track, l, results):
        results.append(list(track))
        for i in range(l, len(nums)):
            track.append(nums[i])
            _subset(nums, track, i+1, results)
            track.pop()
    results = []
    _subset(nums, [], 0, results)
    return results

r = subset([1,2,3])
print(r)

