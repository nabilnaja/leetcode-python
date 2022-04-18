from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def backtrack(start=0, res=[]):

            if len(res) == digitsSize:
                solutions.append(''.join(res))
                return

            possible_letters = letters[digits[start]]

            for letter in possible_letters:
                res.append(letter)
                backtrack(start + 1, res)
                res.pop()

        solutions = []
        digitsSize = len(digits)
        backtrack()
        return solutions


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
