class Solution(object):
    def longestConsecutive(self, nums):
       s = set()
       ans = 0
       for ele in nums:
         s.add(ele)

       for i in range(len(nums)):

         if (nums[i]-1) not in s:

           j = nums[i]
           while(j in s):
             j += 1

           ans = max(ans, j-nums[i])
       return ans