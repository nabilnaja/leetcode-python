from typing import Optional

from DataStructure.datastructure import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head;
        head.next = None
        return p
