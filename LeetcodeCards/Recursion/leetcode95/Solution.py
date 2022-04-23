from typing import Optional
from typing import List

from DataStructure.datastructure import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start, end):
            if start > end:
                return [None, ]
            all_trees = []

            for i in range(start, end + 1):
                left = generate_trees(start, i - 1)
                right = generate_trees(i + 1, end)

                for l in left:
                    for r in right:
                        tree = TreeNode(i)
                        tree.left = l
                        tree.right = r
                        all_trees.append(tree)
            return all_trees

        return generate_trees(1, n) if n else []
