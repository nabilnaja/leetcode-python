class Solution:
    def cleanRoom(self, robot):
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                robot.turnRight()

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()


class Robot:
    def move(self):
        pass
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        pass
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        pass
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        pass
        """
        Clean the current cell.
        :rtype void
        """
