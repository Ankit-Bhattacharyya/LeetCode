class Solution(object):
    def maxArea(self,h, v,  horizontalCuts,  verticalCuts) :
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(v)
        
        horizontalCuts.sort()
        verticalCuts.sort()


        maxHorizontal = 0
        maxVertical = 0

        for i in range (1, len(horizontalCuts)):
            diff = horizontalCuts[i] - horizontalCuts[i-1]
            maxHorizontal = max(maxHorizontal,diff)

        for i in range(1, len(verticalCuts)) :
            diff = verticalCuts[i] - verticalCuts[i-1]
            maxVertical = max(maxVertical,diff)

        return (int)(maxHorizontal * maxVertical % 1000000007)

if __name__ == "__main__" :
    h = 5
    w = 4
    horizontalCuts = [1,2,4]
    verticalCuts = [1,3]
    obj = Solution()
    print(obj.maxArea(h, w, horizontalCuts, verticalCuts))