class Solution:
    def countAsterisks(self, s: str) -> int:
        lst = []
        asterics = 0
        for char in s:
            if char == "|" and char not in lst:
                lst.append(char)
            elif char == "|" and char in lst:
                lst = []
            elif "|" in lst:
                lst.append(char)
            elif char == "*":
                asterics += 1

        return asterics
