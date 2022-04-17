from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, res):
            solution.append(res[:])
            for i in range(start, n):
                res.append(nums[i])
                backtrack(i + 1, res)
                res.pop()

        solution = []
        n = len(nums)
        backtrack(0, [])
        return solution


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
