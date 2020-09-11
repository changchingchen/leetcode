# Time Complexity: O(MN)
# Space : O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        set_row0 = set_col0 = False

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    if i == 0:
                        set_row0 = True
                    if j == 0:
                        set_col0 = True

                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, M):
            if matrix[i][0] == 0:
                for j in range(N):
                    matrix[i][j] = 0

        for j in range(1, N):
            if matrix[0][j] == 0:
                for i in range(M):
                    matrix[i][j] = 0

        if set_row0:
            for j in range(N):
                matrix[0][j] = 0

        if set_col0:
            for i in range(M):
                matrix[i][0] = 0