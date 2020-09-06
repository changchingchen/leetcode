class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output1 = [1] * len(nums)
        output2 = [1] * len(nums)
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output1[i] = output1[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            output2[i] = output2[i+1] * nums[i+1]

        for i in range(len(nums)):
            output[i] = output1[i] * output2[i]

        return output
