class Solution:
    def maxArea(self, height):
        area = 0
        r = len(height) - 1
        l = 0
        while l < r:
            if height[l] > height[r]:
                area = max(area, (r - l) * height[r])
                r -= 1
            else:
                area = max(area, (r - l) * height[l])
                l += 1

        return area
