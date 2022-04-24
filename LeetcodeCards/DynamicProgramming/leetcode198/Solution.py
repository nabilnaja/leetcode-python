from typing import List


class Solution:

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
