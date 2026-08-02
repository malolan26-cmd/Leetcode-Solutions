class Solution:
    def isUgly(self, n: int) -> bool:
        
        for prime in 2, 3, 5:
            while n % prime == 0 and (n>0):
                n /= prime

        return n == 1