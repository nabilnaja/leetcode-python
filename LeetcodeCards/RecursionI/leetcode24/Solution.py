from typing import Optional

from DataStructure.datastructure import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node):
            if not node or not node.next:
                return node
            first = node
            second = first.next
            first.next = swap(second.next)
            second.next = first
            return second
        return swap(head)
