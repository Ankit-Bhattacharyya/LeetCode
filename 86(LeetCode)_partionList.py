# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        less = ListNode()
        lNode = less
        greater = ListNode()
        gNode = greater
        
        while head :
            
            if head.val < x:
                lNode.next = head
                print(str(lNode.val)+"first")
                lNode = lNode.next
            
            if head.val >= x:
                gNode.next = head
                print(str(gNode.val)+"second")
                gNode = gNode.next
            
            head = head.next
            
        lNode.next, gNode.next = greater.next, None
        
        return less.next