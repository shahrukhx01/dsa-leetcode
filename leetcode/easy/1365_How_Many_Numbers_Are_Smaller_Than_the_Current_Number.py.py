class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        smaller_count = []
        for num1 in nums:
            small_counter = 0
            for num2 in nums:
                if num1 > num2:
                    small_counter += 1

            smaller_count.append(small_counter)

        return smaller_count
