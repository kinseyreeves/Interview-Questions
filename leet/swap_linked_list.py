"""
Leetcode Q25
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""
import typing


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if(not head):
            return None
        if not head.next:
            return head   
        ret_head = head.next
        #Only 2 elements
        if(not ret_head.next):
            head.next = None
            ret_head.next = head
            return ret_head
        
        head.next = ret_head.next
        ret_head.next = head

        prev, curr = self.swap(head, head.next, head.next.next)

        while curr:
            prev, curr = self.swap(prev, curr, curr.next)
        return ret_head

    def swap(self, prev, curr, next):
        if(not next):
            return (None,None)
        out = next.next
        prev.next = next
        next.next = curr
        curr.next = out
        return (curr,out)

    def print_list(self,head):
        print(head.val)
        head = head.next
        while(head):
            print(head.val)
            head=head.next

f = ListNode(val=6, next = None)
e = ListNode(val=5, next = None)
d = ListNode(val=4, next = e)
c = ListNode(val=3, next = d)
b = ListNode(val=2, next = c)
a = ListNode(val=1, next = b)

sol = Solution()
#sol.print_list(a)

out = sol.swapPairs(a)
sol.print_list(out)
