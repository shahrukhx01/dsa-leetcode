class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        numSeen = {}

        pairs = 0
        for idx in range(len(nums)):

            if nums[idx] in numSeen:
                del numSeen[nums[idx]]
                pairs += 1
            else:
                numSeen[nums[idx]] = 1

        return [pairs, sum(list(numSeen.values()))]
