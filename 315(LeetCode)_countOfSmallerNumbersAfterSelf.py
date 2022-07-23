class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr, ans = sorted(nums), []
        
        for num in nums :
            i = bisect_left(arr, num)
            ans.append(i)
            del arr[i]
        return ans