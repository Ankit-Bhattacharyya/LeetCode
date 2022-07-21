# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        val = []
        nodes = []
        count = 0
        temp = head
        
        while (temp):
            count += 1
            if count>=left and count<=right:   # | storing value and node in list
                val.append(temp.val)           # | storing value
                nodes.append(temp)             # | storing node
            temp = temp.next

        for node in nodes:
            node.val = val.pop(-1)             # | reversing the values
        return head