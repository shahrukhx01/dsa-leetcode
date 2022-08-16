import operator


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        upper_bound = len(nums)
        counter = {}
        for num in nums:

            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        return max(counter.items(), key=operator.itemgetter(1))[0]
