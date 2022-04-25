from functools import cache


class Solution:

    def tribonacciBU(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        x, y, z = 0, 1, 1

        for i in range(n - 2):
            x, y, z = y, z, x + y + z

        return z

    def tribonacciTD(self, n: int) -> int:
        @cache
        def dp(current):
            if current == 0:
                return 0
            if current < 3:
                return 1
            return dp(current - 1) + dp(current - 2) + dp(current - 3)

        return dp(n)
