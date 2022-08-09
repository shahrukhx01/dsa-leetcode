class Solution:
    def sanitize_str(self, s):
        removed = True

        while removed:
            removed = False
            for idx, char in enumerate(s):
                if char == "#" and idx - 1 > 0:
                    s = s[: idx - 1] + s[idx + 1 :]
                    removed = True
                    break
                elif char == "#" and idx - 1 <= 0:
                    s = s[idx + 1 :]
                    removed = True
                    break

        return s

    def backspaceCompare(self, s: str, t: str) -> bool:

        s = self.sanitize_str(s)
        t = self.sanitize_str(t)

        return t == s
