class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        M = len(grid)
        N = len(grid[0])

        def dfs(r, c):
            if not (0 <= r < M and  0<= c < N and grid[r][c]):
                return 0

            grid[r][c] = 0

            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        max_area = 0
        for r in range(M):
            for c in range(N):
                max_area = max(max_area, dfs(r, c))

        return max_area
 