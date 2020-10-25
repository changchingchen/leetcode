class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        dp = [1] * len(obstacleGrid[0])
        for i, o in enumerate(obstacleGrid[0]):
            if o == 1 or dp[i-1] == 0:
                dp[i] = 0

        for i in range(1, len(obstacleGrid)):
            for j, o in enumerate(obstacleGrid[i]):
                if o == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j-1]

        return dp[-1]

# Time: O(m*n)
# Space: O(n)
