class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomCount = {}
        for ransomChar in ransomNote:
            if ransomChar in ransomCount:
                ransomCount[ransomChar] += 1
            else:
                ransomCount[ransomChar] = 1

        magCounter = {}
        for magChar in magazine:
            if magChar in magCounter:
                magCounter[magChar] += 1
            else:
                magCounter[magChar] = 1

        for ransomChar in ransomCount:
            if (
                ransomChar in magCounter
                and magCounter[ransomChar] >= ransomCount[ransomChar]
            ):
                continue
            else:
                return False

        return True
