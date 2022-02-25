from typing import List
class Solution:
    def trap_bruteforce(self, height: List[int]) -> int:
        water = 0
        for i in range(len(height)):
            l_max, r_max = 0, 0
            for j in range(0, i+1, 1):
                l_max = max(l_max, height[j])

            for k in range(len(height)-1, i-1, -1):
                r_max = max(r_max, height[k])

            water += min(r_max, l_max) - height[i]
        return water

    def trap_dp(self, height):
        l_max = [0] * len(height)
        r_max = [0] * len(height)
        l_max[0] = height[0]
        r_max[0] = height[len(height)-1]
        for l in range(1, len(height)):
            l_max[l] = max(l_max[l-1], height[l])

        for r in range(len(height)-1, -1, -1):
            r_max[r] = max(r_max[r-1], height[r])

        res = 0
        for i in range(len(height)):
            res += min(l_max[i], r_max[i]) - height[i]

        return res

    def trap_dpv2(self, height):
        l, r = 0, len(height) -1
        l_max, r_max = height[l], height[r]
        res = 0
        while l <= r:
            if l_max < r_max:
                res += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
            else:
                res += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])
        return res

    def trapStack(self, height):
        stack = []
        water = 0
        for i, h in enumerate(height):
            while len(stack) and height[stack[-1]] < h:
                bottom = height[stack.pop()]
                # if stack is empty, left bound does not have wall to contain the water
                if stack:
                    width = i - stack[-1] -1
                    minH = min(height[stack[-1]], h)
                    water += width * (minH - bottom)
            stack.append(i)
        return water