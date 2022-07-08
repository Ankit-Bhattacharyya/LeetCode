# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def getDecimalValue(self, head):
        temp = head
        arr = []
        while(temp) :
            arr.append(temp.val)
            temp = temp.next
        arr.reverse()
        total = 0 
        for i in range (len(arr)) :
            if arr[i]!=0 :
                total = total + 2**i
                
        return total