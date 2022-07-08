# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        temp = ListNode()
        
        tail = temp
        
        while True:
            
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
                
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        return temp.next