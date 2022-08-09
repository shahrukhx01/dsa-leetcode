class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ## use index-pointer to track unique elements by doing look-aheads
        pointer = 0

        nums[pointer] = nums[0]

        for i in range(1, len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]

        return pointer + 1
