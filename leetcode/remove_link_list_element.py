def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    current = dummy
    while current:
        while current.next and current.next.val == val:
            current.next = current.next.next
        current = current.next
    return dummy.next