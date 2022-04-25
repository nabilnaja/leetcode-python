from functools import cache
from typing import List


class Solution:

    def minCostClimbingStairsBU(self, cost: List[int]) -> int:
        if not cost:
            return 0

        n = len(cost)

        rob_next_plus_one = 0
        rob_next = cost[n - 1]

        for i in range(n - 2, -1, -1):
            best = max(rob_next_plus_one + cost[i], rob_next)
            rob_next_plus_one, rob_next = rob_next, best

        return rob_next

    def minCostClimbingStairsTD(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i <= 1:
                return 0

            down_one = cost[i - 1] + dp(i - 1)
            down_two = cost[i - 2] + dp(i - 2)
            return min(down_one, down_two)

        return dp(len(cost))
