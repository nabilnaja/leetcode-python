from functools import lru_cache
from typing import List


class Solution:
    """
        Sub problems : r(i,left) max score using multiplicators i , i+1 untill n
        and using element from nums 0 .. left and n - 1 - (i - left)
        Original problem : r(0)
        Relate : r(i) = max(
            r(i + 1,left + 1) + multipliers[i] * nums[left],
            r(i + 1, left) + multipliers[i] * nums[right]
            )
        Base :  r(n) = 0
        Topological order : n, n-1, .. , 0
        Time : O(n) * O(1)
    """

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        @lru_cache(2000)
        def dp(i=0, l=0):
            if i == m:
                return 0
            r = n - (i - l) - 1
            return max(multipliers[i] * nums[l] + dp(i + 1, l + 1), multipliers[i] * nums[r] + dp(i + 1, l))

        return dp()





