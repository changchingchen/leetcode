class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        row_set = set()
        col_set = set()

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in row_set:
            for j in range(N):
                matrix[i][j] = 0

        for j in col_set:
            for i in range(M):
                matrix[i][j] = 0
