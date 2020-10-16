class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        M, N = len(grid), len(grid[0])
        islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    continue

                is_closed = True
                grid[i][j] = 1
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    if r == 0 or r == M-1 or c == 0 or c == N-1:
                        is_closed = False

                    for d in range(len(dr)):
                        if not (0 <= r+dr[d] < M and 0 <= c + dc[d] < N):
                            continue

                        nr = r+dr[d]
                        nc = c+dc[d]
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            q.append((nr, nc))

                if is_closed:
                    islands += 1

        return islands
