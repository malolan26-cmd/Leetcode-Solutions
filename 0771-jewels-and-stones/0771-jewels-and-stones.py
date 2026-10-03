class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0

        for c in stones:
            if c in jewels:
                counter += 1

        return counter