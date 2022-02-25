class Solution:
    def uniquePathsDFS(self, m: int, n: int) -> int:
        return self.dfs(1, 1, m, n, {})

    def dfs(self, x, y, m, n, memo):
        if x == m and y == n:
            return 1

        if x < 1 or x > m or y < 1 or y > n:
            return 0

        if (x,y) in memo:
            return memo[(x,y)]

        down, right = (1, 0), (0, 1)
        count = 0
        for dx, dy in [down, right]:
            count += self.dfs(x+dx, y+dy, m, n, memo)

        memo[(x,y)] = count

        return count