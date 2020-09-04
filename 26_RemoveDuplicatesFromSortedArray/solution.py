class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        curr_idx = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[curr_idx]:
                curr_idx += 1
                nums[curr_idx] = nums[idx]

        return curr_idx+1
