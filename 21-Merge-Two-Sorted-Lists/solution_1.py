from typing import ListNode
def mergeTwoLists(list1, list2):
    answer = ListNode()
    answerSpot = answer
    while list1 and list2:
        if list1.val <= list2.val:
            answerSpot.next = list1
            list1 = list1.next
        else:
            answerSpot.next = list2
            list2 = list2.next
        answerSpot = answerSpot.next
    if list1:
        answerSpot.next = list1
    elif list2:
        answerSpot.next = list2
    return answer.next