def hasCycle(head):
    # set two var one that moves faster than the other 
    # if the var both ends as the same value return true 
    # else return fasle
    fast = head
    slow = head
    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False