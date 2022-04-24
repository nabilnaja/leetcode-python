from typing import List


class Solution:

    def robBU(self, nums: List[int]) -> int:
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        for i in range(N - 2, -1, -1):
            best = max(rob_next_plus_one + nums[i], rob_next)
            rob_next_plus_one, rob_next = rob_next, best

        return rob_next

    def robTD(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cache = {}

        def dp(house=len(nums) - 1):
            if house == 0:
                return nums[0]
            if house == 1:
                return max(nums[0], nums[1])

            if house not in cache:
                cache[house] = max(dp(house - 2) + nums[house], dp(house - 1))

            return cache[house]

        return dp()
