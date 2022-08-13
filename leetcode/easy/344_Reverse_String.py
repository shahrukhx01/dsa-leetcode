class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1

        for i in range((j // 2) + 1):
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            j -= 1
