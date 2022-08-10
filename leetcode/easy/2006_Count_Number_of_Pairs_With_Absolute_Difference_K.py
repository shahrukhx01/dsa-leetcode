class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        pair = 0

        for idx, num1 in enumerate(nums):
            for num2 in nums[idx + 1 :]:
                diff = num1 - num2

                if diff < 0:
                    diff *= -1

                if k == diff:
                    pair += 1

        return pair
