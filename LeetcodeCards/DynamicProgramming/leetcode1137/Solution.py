class Solution:

    def tribonacciBU(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        x, y, z = 0, 1, 1

        for i in range(n - 2):
            x, y, z = y, z, x + y + z

        return z

    def tribonacciTD(self, n: int) -> int:
        pass
