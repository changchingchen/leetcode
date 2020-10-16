class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        M, N = len(board), len(board[0])

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        q = deque()
        for r in range(M):
            for c in range(N):
                if (r == 0 or r == M-1 or c == 0 or c == N-1) and board[r][c] == 'O':
                    q.append((r,c))

        while q:
            r, c = q.popleft()
            board[r][c] = 'R'

            for d in range(len(dr)):
                if r + dr[d] < 0 or r + dr[d] >= M or c + dc[d] < 0 or c + dc[d] >= N:
                    continue

                new_r = r + dr[d]
                new_c = c + dc[d]
                if board[new_r][new_c] == 'O':
                    q.append((new_r, new_c))

        for r in range(M):
            for c in range(N):
                if board[r][c] == 'R':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
