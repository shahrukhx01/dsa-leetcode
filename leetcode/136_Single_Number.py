class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count_map = {}

        for num in nums:

            if count_map.get(num) != None:
                del count_map[num]
            else:
                count_map[num] = num

        return list(count_map.keys())[0]
