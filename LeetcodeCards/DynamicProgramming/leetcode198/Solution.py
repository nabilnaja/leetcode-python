from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Sub problems : r(i) max money from i , i+1 untill n (suffix)
        Original problem : r(0)
        Relate : r(i) = max(nums[i] + r(i+2), r(i+1))
        Base :  r(n) = 0
        Topological order : n, n-1, .. , 0
        Time : O(n) * O(1)
        """

        n = len(nums)

        @cache
        def dp(i):
            if i >= n:
                return 0
            return max(dp(i + 2) + nums[i], dp(i + 1))

        def dp():
            memo = [None for _ in range(n + 1)]
            memo[n - 1], memo[n] = nums[n - 1], 0
            for i in range(n - 2, -1, -1):
                memo[i] = max(memo[i + 2] + nums[i], memo[i + 1])
            return memo[0]

        def dp():
            prev = nums[n - 1]
            prevSec = 0
            for i in range(n - 2, -1, -1):
                prev, prevSec = max(prevSec + nums[i], prev), prev
            return prev

        if not nums:
            return 0

        return dp()
