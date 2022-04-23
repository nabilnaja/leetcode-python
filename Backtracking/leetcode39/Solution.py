from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start=0, currentSum=0, currentRes=[]):
            if currentSum == target:
                res.append(currentRes[:])
                return
            if currentSum > target:
                return
            for i in range(start, len(candidates)):
                currentRes.append(candidates[i])
                backtrack(i, currentSum + candidates[i], currentRes)
                currentRes.pop()

        backtrack()
        return res


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
