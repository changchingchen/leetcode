class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing_nums = set()
        for i in range(len(nums)):
            num = nums[i]
            if num not in existing_nums:
                existing_nums.add(num)
            else:
                return True

        return False
