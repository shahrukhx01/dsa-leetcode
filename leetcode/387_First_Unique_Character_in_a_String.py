class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        for idx in range(len(s)):
            if s[idx] not in s[:idx] + s[idx + 1 :]:
                return idx

        return index
