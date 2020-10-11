class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        ans = 0
        M = len(grid)
        N = len(grid[0])
        q = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '0':
                    continue

                ans += 1
                grid[i][j] = '0'
                q.append((i,j))
                while q:
                    r, c = q.popleft()
                    for d in range(len(dr)):
                        if r + dr[d] < 0 or r + dr[d] >= M or c + dc[d] < 0 or c + dc[d] >= N:
                            continue

                        new_r = r + dr[d]
                        new_c = c + dc[d]
                        if grid[new_r][new_c] == '1':
                            grid[new_r][new_c] = '0'
                            q.append((new_r, new_c))

        return ans
