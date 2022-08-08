class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        output = [-1] * len(nums)

        for i in range(len(nums)):
            idx = nums[i]
            if idx >= 0 and idx <= len(nums) - 1:
                output[i] = nums[idx]

        return output
