from typing import List

class Solution:

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        if index == len(string):
            if left_count == right_count:
                if rem_count <= self.min_removed:
                    possible_ans = "".join(expr)

                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)
        else:
            current_char = string[index]
            if current_char != '(' and current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)
                expr.append(current_char)
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count + 1)
                elif right_count < left_count:
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)
                expr.pop()

        pass

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Reset the class level variables that we use for every test case.
        self.reset()

        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)

    def removeInvalidParentheses2(self, s: str) -> List[str]:

        left = 0
        right = 0

        for char in s:

            if char == '(':
                left += 1
            elif char == ')':
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left

        def backtrack(index, leftSum, rightSum, s, leftRem, rightRem, res, expr):
            if index == len(s):
                if leftRem == 0 and rightRem == 0:
                    res.add(''.join(expr))
            else:
                if s[index] == '(' and leftRem > 0:
                    backtrack(index + 1, leftSum, rightSum, s, leftRem - 1, rightRem, res, expr)
                elif s[index] == ')' and rightRem > 0:
                    backtrack(index + 1, leftSum, rightSum, s, leftRem, rightRem - 1, res, expr)
                expr.append(s[index])
                if s[index] != '(' and s[index] != ')':
                    backtrack(index + 1, leftSum, rightSum, s, leftRem, rightRem, res, expr)
                if s[index] == '(':
                    backtrack(index + 1, leftSum + 1, rightSum, s, leftRem, rightRem, res, expr)
                if s[index] == ')' and leftSum > rightSum:
                    backtrack(index + 1, leftSum, rightSum + 1, s, leftRem, rightRem, res, expr)
                expr.pop()

        res = set()
        backtrack(0, 0, 0, s, left, right, res, [])
        return list(res)


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses2('()())()'))
