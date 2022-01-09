# take a dummy node and stand it at end of linked list
# move the list and point it to head
# update the head and the dummy node upto ktimes

def rotate(self, head, k):
    curr = head
    if head.next is None:
        return head

    # code here

    while curr.next is not None:
        curr = curr.next
    while k > 0:
        curr.next = head
        head = head.next
        curr = curr.next
        curr.next = None
        k -= 1

    return head