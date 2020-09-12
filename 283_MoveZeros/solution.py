class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = curr_idx = 0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
                while i < len(nums) and nums[i] == 0:
                    i += 1

                if i >= len(nums):
                    break

            nums[curr_idx] = nums[i]
            curr_idx += 1
            i += 1

        if curr_idx == 0:
            return

        while curr_idx < len(nums):
            nums[curr_idx] = 0
            curr_idx += 1
