# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Fast & Slow Pointers
def fast_slow_pointer_template(head):
    slow, fast = head, head

    while fast and fast.next:
        # ==================================
        # The core logic is always moving the pointers.
        slow = slow.next
        fast = fast.next.next

        # The problem-specific logic is what you check for.
        # For cycle detection:
        if slow == fast:
            return True # Cycle detected
        # ==================================

    return False # No cycle
