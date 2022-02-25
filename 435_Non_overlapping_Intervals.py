"""
note:
greedy: local optimal choices leads to ultimate best solution
e.g. number of events you can attend
"""

def eraseOverlapIntervals_greedy(intervals):
    """
    time complexity: O(N)
    space comlexity: O(1)
    """
    count = 0
    intervals.sort(key=lambda interval: interval[1])
    start, end = -float('inf'), -float('inf')
    for interval in intervals:
        if interval[0] < end:
            count += 1
        else:
            start, end = interval
    return count

def eraseOverlapIntervals_dp(intervals):
    """
    time complexity: O(N)
    space complexity: O(N)
    """
    dp = [0] * len(intervals)
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            dp[i] = dp[i-1] + 1
    return dp[-1]

# intervals = [[1,2],[2,3],[3,4],[1,3]]
# c = eraseOverlapIntervals(intervals)
# print(c)

# intervals = [[1,2],[1,2],[1,2]]
# c = eraseOverlapIntervals(intervals)
# print(c)

# intervals = [[1,2],[2,3]]
# c = eraseOverlapIntervals(intervals)
# print(c)
