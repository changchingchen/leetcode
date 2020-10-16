class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        M = len(grid)
        N = len(grid[0])
        max_area = 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    continue

                grid[i][j] = 0
                area = 1
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    for d in range(len(dr)):
                        if r+dr[d] < 0 or r+dr[d] >= M or c+dc[d] < 0 or c+dc[d] >= N:
                            continue

                        new_r = r + dr[d]
                        new_c = c + dc[d]
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 0
                            area += 1
                            q.append((new_r, new_c))                    

                max_area = max(max_area, area)

        return max_area
 