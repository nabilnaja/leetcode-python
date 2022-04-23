from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        count = 0

        def backtrack(index=0, currentSum=0):
            if index == len(nums):
                if currentSum == target:
                    nonlocal count
                    count += 1
                return
            backtrack(index + 1, currentSum + nums[index])
            backtrack(index + 1, currentSum - nums[index])

        backtrack()
        return count


if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
s