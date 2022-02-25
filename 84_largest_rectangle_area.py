"""
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/1728151/All-4-approaches-shown-oror-O(N2)-oror-O(NlogN)-oror-O(N)(two-pass)-oror-O(N)(one-pass)-with-explanation
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/440433/Python-Detailed-Explanation-for-DP-O(n)-Solution-Beats-99.9-RunTime-100-Memory
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28910/Simple-Divide-and-Conquer-AC-solution-without-Segment-Tree
try dp and segmented tree
"""

def largestRectangleArea_brute_force(heights):
    """
    time complexity: O(n^2)
    space complexity: O(1)
    """
    max_area = float('-inf')
    for m, h in enumerate(heights):
        l, r = m-1, m+1
        while l >= 0 and h < heights[l]:
            l -= 1

        while r < len(heights) and h < heights[r]:
            r += 1

        area = h * (r - l - 1)
        max_area = max(area, max_area)
    return max_area

def largestRectangleArea_stack(heights):
    max_area = 0
    heights = [0] + heights + [0]
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            top = stack.pop()
            max_area = max(
                max_area,
                (i - stack[-1] -1) * heights[top]
            )
        stack.append(i)
    return max_area

def largestRectangleArea_dp(heights):
    pass

test_data_1 = [2,1,5,6,2,3]
result1 = largestRectangleArea_brute_force(test_data_1)
assert test_data_1 == result1