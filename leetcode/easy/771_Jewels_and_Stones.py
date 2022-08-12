class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsCount = 0
        for stone in stones:
            if stone in jewels:
                jewelsCount += 1

        return jewelsCount
