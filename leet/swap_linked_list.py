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
        ret_head = head.next if head.next else head
        next2 = self.swap(head, head.next)
        while next2:
            next2 = self.swap(next2, next2.next)
        return ret_head

    def swap(self, node, next_node):
        if(next_node):
            node.next = next_node.next
            next_node.next = node
        else:
            return next_node
        return node.next

    def print_list(self,head):
        print(head.val)
        head = head.next
        while(head):
            print(head.val)
            head=head.next

c = ListNode(val=3)
b = ListNode(val=2, next= c)
a = ListNode(val=1, next =b)

sol = Solution()
out = sol.swapPairs(a)

sol.print_list(out)