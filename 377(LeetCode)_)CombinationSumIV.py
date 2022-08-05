class Solution(object):
    # using memorization
    def combinationSum4(self, nums, target):
        
        dp = [-1] * (target+1)
        
        def solve(nums, target):
            
            if target < 0:
                return 0
            
            if target == 0:
                return 1
            
            if dp[target] != -1:
                return dp[target]

            ans = 0
            for i in range (len(nums)):
                ans += solve(nums, target-nums[i])
            
            dp[target] = ans
            return dp[target]
        
        return solve(nums, target)