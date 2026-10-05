class Solution:
    def fib(self, n: int) -> int:
        cache = {}

        cache[0] = 0
        cache[1] = 1

        for i in range(2, n):
            cache[i] = cache[i - 1] + cache[i - 2]

        if n == 0:
            return 0
        elif n == 1:
            return 1

        return (cache[n - 1] + cache[n - 2])


        