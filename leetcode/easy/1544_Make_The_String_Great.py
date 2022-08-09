class Solution:
    def makeGood(self, s: str) -> str:
        isBad = True
        while isBad:
            isBad = False
            for i in range(len(s)):
                if i + 1 <= len(s) - 1:
                    if (
                        s[i].islower() == s[i + 1].isupper()
                        and s[i].lower() == s[i + 1].lower()
                    ):
                        s = s[:i] + s[i + 2 :]
                        isBad = True
        return s
