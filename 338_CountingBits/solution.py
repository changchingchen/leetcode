from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:

        ones = [0] * (num + 1)

        for i in range(1, num+1):
            if i % 2 == 0:
                ones[i] = ones[i//2]
            else:
                ones[i] = ones[i-1] + 1

        return ones
