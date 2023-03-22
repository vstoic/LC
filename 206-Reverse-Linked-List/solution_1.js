/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
//create a prev
//set var curr to head
// now itterate throught the whole link
// keep the variable for current.next
// change the link and flip it
// change the current
// change the next
var reverseList = function (head) {
  prev = null;
  current = head;
  while (current) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
};
