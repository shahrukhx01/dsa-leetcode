class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()

        counter = {}
        for num in nums:
            if counter.get(num) != None:
                counter[num] += 1
            else:
                counter[num] = 1

        pairs = 0
        for _, item in counter.items():
            if item > 2:
                ## compute pairwise numbers
                pairs += ((item - 1) * item) / 2
            elif item >= 2:
                pairs += 1

        return int(pairs)
