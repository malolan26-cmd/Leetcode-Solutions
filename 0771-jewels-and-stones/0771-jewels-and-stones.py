class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0

        set_jewels = set(jewels)

        for c in stones:
            if c in set_jewels:
                counter += 1

    
        return counter