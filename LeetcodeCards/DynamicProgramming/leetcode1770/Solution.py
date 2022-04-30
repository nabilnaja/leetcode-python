from functools import lru_cache
from typing import List


class Solution:

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dp(i, l):
            if i == m:
                return 0
            j = i + 1
            left = dp(j, l + 1) + multipliers[i] * nums[l]
            right = dp(j, l) + multipliers[i] * nums[n - (i - l) - 1]

            return max(left, right)

        n, m = len(nums), len(multipliers)
        return dp(0, 0)
