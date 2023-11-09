def reverseList(head):
    prev, curr = None, head
    while curr:
        saved = curr.next
        curr.next = prev
        prev = curr
        curr = saved
    return prev