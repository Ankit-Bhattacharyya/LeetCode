class Solution(object):
    def makesquare(self, matchsticks) :
        n = len(matchsticks)
        per = sum(matchsticks)
        
        if per%4 != 0 :
            return False
        else:
            sides = per/4
            
            
        matchsticks.sort(reverse = True)
        def dfs(a,b,c,d,k):
            if k==n :
                if a==b==c==d:
                    return True
            m = matchsticks[k]
            
            if a+m<=sides and dfs(a+m,b,c,d,k+1) :
                return True
            
            if b+m<=sides and dfs(a,b+m,c,d,k+1) :
                return True
            
            if c+m<=sides and dfs(a,b,c+m,d,k+1) :
                return True

            if d+m<=sides and dfs(a,b,c,d+m,k+1) :
                return True

        return dfs(0,0,0,0,0)