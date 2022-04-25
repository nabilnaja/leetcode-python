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
        pass
