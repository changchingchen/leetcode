from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m+n-2)/factorial(m-1)/factorial(n-1))

'''
To go from top left to bottom right, it need to take (m-1) steps
down and (n-1) steps right. Calculate the combinational of which
(m-1) steps to go down in the total (m-1 + n-1) steps
'''
