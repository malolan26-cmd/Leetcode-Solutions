class Solution:
    def climbStairs(self, n: int) -> int:
        # any set of steps is the combination of the two previous step amounts
        a = 0
        b = 1
        for i in range(n):
            a, b = b, (a+b)
        
        return b
        