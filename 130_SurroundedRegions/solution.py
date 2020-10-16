class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        M = len(board)
        N = len(board[0])
        
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        regions = set()
       
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'X':
                    continue

                is_surrounded = True
                q = deque([(i,j)])
                temp_regions = set()
                while q:
                    r, c = q.popleft()
                    board[r][c] = 'X'
                    temp_regions.add((r,c))
                    if r == 0 or r == M-1 or c == 0 or c == N-1:
                        is_surrounded = False

                    for d in range(len(dr)):
                        if r + dr[d] < 0 or r + dr[d] >= M or c + dc[d] < 0 or c + dc[d] >= N:
                            continue
                        
                        new_r = r + dr[d]
                        new_c = c + dc[d]
                        if board[new_r][new_c] == 'O':
                            q.append((new_r, new_c))
                
                if not is_surrounded:
                    regions |= temp_regions

        for r, c in regions:
            board[r][c] = 'O'

# Time limit exceeded
