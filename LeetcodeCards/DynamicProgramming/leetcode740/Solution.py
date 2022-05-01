from typing import List
from functools import cache
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        sortedNums = sorted(points.keys())

        n = len(sortedNums)

        @cache
        def dp(i=max_number):
            if i == 0:
                return 0
            if i == 1:
                return points[1]

            return max(dp(i - 1), dp(i - 2) + points[i])

        def dp():
            memo = [None for _ in range(max_number + 1)]
            memo[0], memo[1] = 0, points[1]

            for i in range(2, len(memo)):
                memo[i] = max(memo[i - 1], memo[i - 2] + points[i])

            return memo[max_number]

        def dp():
            prevSec, prev = 0, points[1]

            for i in range(2, max_number + 1):
                prev, prevSec = max(prev, prevSec + points[i]), prev
            return prev

        """
        create dict with how many points we gain from taking an element
        sort nums and remove duplicates 
        Sub problems : d(i) maximum number of points from nums 0, 1 utill i 
        Original problem : d(0)
        Relate : d(i) = 
        sorteNums(i) != sorted(i+1) + 1 ->  max(dict(num) + s(i+2), s(i+1))
        else ->
        max(
            max(dcit(num) + s(i+1))
        )
        Base :  r(n) = 0 
        Topological order : 0 , 1, ..., n
        Time : O(n) * O(1) + O(m log m)  m count of distinct nums
        """

        @cache
        def dp(i=0):
            if i >= n:
                return 0
            currentNum = sortedNums[i]
            if i + 1 < n and currentNum == sortedNums[i + 1] - 1:
                return max(dp(i + 1), dp(i + 2) + points[currentNum])
            else:
                return dp(i + 1) + points[currentNum]

        def dp():
            memo = [None for _ in range(n + 2)]
            memo[n + 1], memo[n] = 0, 0
            for i in range(n - 1, -1, -1):
                currentNum = sortedNums[i]
                if i + 1 < n and currentNum == sortedNums[i + 1] - 1:
                    memo[i] = max(memo[i + 1], memo[i + 2] + points[currentNum])
                else:
                    memo[i] = memo[i + 1] + points[currentNum]
            return memo[0]

        def dp():
            memo = [None for _ in range(n + 2)]
            prev, prevSec = 0, 0
            for i in range(n - 1, -1, -1):
                currentNum = sortedNums[i]
                if i + 1 < n and currentNum == sortedNums[i + 1] - 1:
                    prev, prevSec = max(prev, prevSec + points[currentNum]), prev
                else:
                    prev, prevSec = prev + points[currentNum], prev
            return prev

        return dp()
