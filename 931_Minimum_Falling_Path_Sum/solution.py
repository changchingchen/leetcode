from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)

        for i in range(1, N):
            for j in range(N):
                A[i][j] += min(A[i-1][max(j-1, 0):min(j+2, N)])

        return min(A[-1])
