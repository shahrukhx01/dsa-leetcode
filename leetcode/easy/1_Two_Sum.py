class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1 :]):
                if target - num1 == num2:
                    return [i, i + j + 1]
