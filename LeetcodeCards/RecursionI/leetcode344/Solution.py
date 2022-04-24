from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        def inplaceReverse(start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            inplaceReverse(start + 1, end -1)
        inplaceReverse(0, len(s) - 1)
        return s


