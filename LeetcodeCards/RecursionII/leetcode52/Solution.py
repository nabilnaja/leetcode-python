class Solution:

    def totalNQueens(self, n: int) -> int:
        result = 0

        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                nonlocal result
                result += 1
                return
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                backtrack(row + 1, diagonals, anti_diagonals, cols)
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

        backtrack(0, set(), set(), set())
        return result


if __name__ == '__main__':
    print(Solution().totalNQueens(4))
