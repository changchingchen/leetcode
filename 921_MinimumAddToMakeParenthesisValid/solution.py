class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        unpaired_cnt = 0
        ans = 0
        for s in S:
            if s == '(':
                unpaired_cnt += 1
            elif unpaired_cnt == 0:
                ans += 1
            else:
                unpaired_cnt -= 1

        ans += unpaired_cnt

        return ans
