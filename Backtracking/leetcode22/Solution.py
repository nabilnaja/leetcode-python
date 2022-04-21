from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(sol, s=[], leftSum=0, rightSum=0):
            if len(s) == n * 2:
                if leftSum == rightSum and len(s) == n * 2:
                    sol.add(''.join(s))
                return

            if leftSum > rightSum:
                s.append(')')
                backtrack(sol, s, leftSum, rightSum + 1)
                s.pop()

            s.append('(')
            backtrack(sol, s, leftSum + 1, rightSum)
            s.pop()

        result = []
        backtrack(result)
        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
