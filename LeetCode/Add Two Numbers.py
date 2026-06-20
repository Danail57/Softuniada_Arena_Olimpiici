# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
    def addTwoNumbers(self, l1, l2):

        def length(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        len1 = length(l1)
        len2 = length(l2)

        # Append zeros to shorter list
        if len1 < len2:
            curr = l1
            while curr.next:
                curr = curr.next
            for _ in range(len2 - len1):
                curr.next = ListNode(0)
                curr = curr.next

        elif len2 < len1:
            curr = l2
            while curr.next:
                curr = curr.next
            for _ in range(len1 - len2):
                curr.next = ListNode(0)
                curr = curr.next

        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 and l2:
            add = l1.val + l2.val + carry

            carry = add // 10
            digit = add % 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next
            l2 = l2.next

        if carry:
            tail.next = ListNode(carry)

        return dummy.next
