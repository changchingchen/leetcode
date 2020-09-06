# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]

        prev_product = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            output[i] *= prev_product
            prev_product *= nums[i]

        return output
