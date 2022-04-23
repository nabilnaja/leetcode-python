from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(first=0):
            if first == len(nums):
                result.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return result


if __name__ == '__main__':
    print(Solution().permute([1,2,3]))
