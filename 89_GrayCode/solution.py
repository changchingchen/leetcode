class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            ans.extend([num + 2**(i-1) for num in ans[::-1]])

        return ans
