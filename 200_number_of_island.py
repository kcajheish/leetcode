"""
try union find solution!!
https://leetcode.com/problems/number-of-islands/discuss/56354/1D-Union-Find-Java-solution-easily-generalized-to-other-problems
"""
def numIsLandsDFS(grid):
    land = '1'
    sea = '0'
    visited_land = '-1'
    width = len(grid[0])
    height = len(grid)
    def dfs(grid, i, j):
        # if it's out of boarder, stop
        if i < 0 or j < 0 or j >= width or i >= height:
            return

        # if it's sea or land being visited, stop
        if grid[i][j] in {sea, visited_land}:
            return

        grid[i][j] = visited_land

        up, down, left, right = (1,0), (-1, 0), (0, -1), (0, 1)
        for y, x in [up, down, left, right]:
            dfs(grid, i+y, j+x)

    visits = 0
    # visits every square on the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if a land is spotted, explore the land and count it toward total
            if grid[i][j] == land:
                dfs(grid, i, j)
                visits += 1
    return visits

def numIsLandBFS(grid):
    land = '1'
    sea = '0'
    visited_land = '-1'
    width = len(grid[0])
    height = len(grid)

    def bfs(grid, i, j):
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            if i < 0 or j < 0 or i >= height or j >= width:
                continue

            if grid[i][j] in {sea, visited_land}:
                continue

            grid[i][j] = visited_land
            for shift_x, shift_y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                queue.append((shift_y + i, shift_x + j))

    number_of_lands = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == land:
                bfs(grid, i, j)
                number_of_lands += 1
    return number_of_lands
