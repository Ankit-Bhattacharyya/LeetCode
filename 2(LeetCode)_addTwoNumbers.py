# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None :
            return []
        else:
            while True:
                head = ListNode()
                tail = head
                
                if l1 is None:
                    tail.next = l2
                    break
                if l2 is None:
                    tail.next = l1
                    break
                if l1 is None and l2 is None:
                    break
                
                sumVal = l1.val + l2.val
                
                if sumVal>9:
                    tail.val = sumVal%10
                    carry = sumVal/10
                if carry>0:
                    tail.val = sumVal + carry
                    carry = 0
                if carry>0 and sumVal>9:
                    tail.val = sumVal + carry
                    carry = tail.val/10
                else:
                    tail.val = sumVal
                tail = tail.next
                l1 = l1.next
                l2 = l2.next
            if head.val == 0:
                return head.next
            else:
                return head     

if __name__ == "__main__" :
    obj = Solution()    
    print(obj.addTwoNumbers(l1 = ListNode([2,4,3]) , l2 = ListNode([5,6,4])))