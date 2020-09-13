class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = sec_max_val = 0
        for num in nums:
            if num > max_val:
                max_val, sec_max_val = num, max_val
            elif num > sec_max_val:
                sec_max_val = num

        return (max_val-1) * (sec_max_val-1)
