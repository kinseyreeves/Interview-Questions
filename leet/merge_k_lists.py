# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        smallest = self.get_smallest(lists)
        if(not smallest):
            return None
        idx = 0
        first = ListNode(smallest.val)
        last = first
        
        while (smallest):
            smallest = self.get_smallest(lists)
            if(smallest):
                last = self.insert_list(last, smallest.val)
        
        return first
        
    def get_smallest(self,lists):
        smallest = self.get_non_null(lists)
        if(not smallest):
            return None
        idx = 0
        for i in range(0,len(lists)):
            if(lists[i] and lists[i].val <= smallest.val):
                smallest = lists[i]
                idx = i
        lists[idx] = lists[idx].next
        
        return smallest
    
    def get_non_null(self, lists):
        for l in lists:
            if l:
                return l
        return None
    
    def insert_list(self, first, val):
        first.next = ListNode(val)
        return first.next





        