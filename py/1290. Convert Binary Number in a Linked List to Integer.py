class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        num = 0

        while current:
            num = (num << 1) | current.val
            current = current.next

        return num
